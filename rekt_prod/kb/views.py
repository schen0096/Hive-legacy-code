from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import UpdateView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import category, faq, tag, answer, faq_log_id, faq_log
from .forms import FAQForm, AnswerForm, TagForm, QuetionTagForm

def check_group(user):
    if (user.groups.filter(name='Level 2').exists() or
                user.groups.filter(name='Level 5').exists()):
        return True

@login_required
def kb(request):
    currentUser = request.user
    if currentUser.groups.filter(name='Technovation').exists():
        c = category.objects.all()
    else:
        c = category.objects.exclude(name="Technovation")
    return render(request, 'kb/kb.html', {'category':c})


@login_required
def category_faq(request, name):
    c = get_object_or_404(category, name=name)
    question = (faq.objects.filter(category_id__name=name).
                order_by("-pin_value", "last_updated"))
    page = request.GET.get('page', 1)
    paginator = Paginator(question, 35)

    try:
        question = paginator.page(page)
    except PageNotAnInteger:
        question = paginator.page(1)
    except EmptyPage:
        question = paginator.page(paginator.num_pages)
    return render(request, 'kb/faq.html', {'question':question, "category":c})


@login_required
@user_passes_test(check_group, login_url='home')
def new_question(request, name):
    c = get_object_or_404(category, name=name)
    FAQTag = get_object_or_404(tag, tag_name=name)
    if request.method == 'POST':
        qform = FAQForm(request.POST)
        aform = AnswerForm(request.POST)
        if qform.is_valid() and aform.is_valid():
            faqform = qform.save(commit=False)
            faqform.category_id = c
            faqform.starter = request.user
            faqform.save()
            faqform.tag_faq.add(FAQTag)

            ans = aform.save(commit=False)
            ans.faq = faqform
            ans.created_by = request.user
            ans.save()

            FaqLogID = faq_log_id(faq_id_value=faqform.pk)
            FaqLogID.save()
            FaqLog = faq_log(subject=faqform.subject, answer=ans.answer)
            FaqLog.editor = request.user
            FaqLog.faq_id = FaqLogID
            FaqLog.category_id = c
            FaqLog.save()
            return redirect('answer', name=c.name, faq_pk=faqform.pk)

    else:
        qform = FAQForm()
        aform = AnswerForm()

    return render(request, 'kb/new_question.html',
                  {'category':c, 'qform':qform, 'aform':aform})


@login_required
def overall(request):
    question = faq.objects.all().order_by("-pin_value", "last_updated")
    page = request.GET.get('page', 1)

    paginator = Paginator(question, 35)
    try:
        question = paginator.page(page)
    except PageNotAnInteger:
        question = paginator.page(1)

    return render(request, 'kb/all_questions.html', {'question':question})

@login_required
def searchQA(request):
    template = 'kb/all_questions.html'
    query = request.GET.get('q')
    results = (faq.objects.filter
               (Q(subject__icontains=query) |
                Q(tag_faq__tag_name__icontains=query)).distinct())
    return render(request, template, {'question':results})


@login_required
def faq_answer(request, name, faq_pk):
    faq_ans = get_object_or_404(faq, category_id__name=name, pk=faq_pk)
    lastest = (faq_log.objects.filter
               (faq_id__faq_id_value=faq_pk).order_by('-faq_logging_id')[0])
    return render(request, 'kb/answer.html', {'faq':faq_ans, 'lastest':lastest})


@login_required
@user_passes_test(check_group, login_url='home')
def editQA(request, name, faq_pk):
    question = get_object_or_404(faq, pk=faq_pk)
    template = 'kb/edit_qa.html'
    c = get_object_or_404(category, name=name)
    answer = question.answer.all()[0]
    if request.method == "POST":
        qform = FAQForm(data=request.POST, instance=question)
        aform = AnswerForm(request.POST, instance=answer)
        if qform.is_valid() and aform.is_valid:
            faqform = qform.save(commit=False)
            faqform.category_id = c
            faqform.save()

            ans = aform.save(commit=False)
            ans.faq = faqform
            ans.created_by = request.user
            ans.save()

            FaqLogID = faq_log_id(faq_id_value=faqform.pk)
            FaqLogID.save()
            FaqLog = faq_log(subject=faqform.subject, answer=ans.answer)
            FaqLog.editor = request.user
            FaqLog.faq_id = FaqLogID
            FaqLog.category_id = c
            FaqLog.save()
            return redirect('answer', name=c.name, faq_pk=faqform.pk)
    else:
        qform = FAQForm(instance=question)
        aform = AnswerForm(instance=answer)
    return render(request, template,
                  {'qform':qform, 'aform':aform, 'c':c, 'question':question})

@login_required
@user_passes_test(check_group, login_url='home')
def pinQuestion(request, name, faq_pk):
    c = get_object_or_404(category, name=name)
    question = get_object_or_404(faq, pk=faq_pk)
    try:
        question.pin_value = True
        question.save()
    except Exception:
        return redirect(request, 'kb/kb.html', {'category':c})
    return redirect('faq', name=c.name)

@login_required
@user_passes_test(check_group, login_url='home')
def unpinQuestion(request, name, faq_pk):
    c = get_object_or_404(category, name=name)
    question = get_object_or_404(faq, pk=faq_pk)
    try:
        question.pin_value = False
        question.save()
    except Exception:
        return redirect(request, 'kb/kb.html', {'category':c})
    return redirect('faq', name=c.name)

@login_required
@user_passes_test(check_group, login_url='home')
def changeLog(request, name, faq_pk):
    questionLog = (faq_log.objects.filter
                   (faq_id__faq_id_value=faq_pk).
                   order_by('-faq_logging_id'))
    latest = faq_log.objects.filter(faq_id__faq_id_value=faq_pk).order_by(
        '-faq_logging_id')[0]
    return render(request, 'kb/changelog.html',
                  {'questionLog':questionLog, 'latest':latest})


@login_required
@user_passes_test(check_group, login_url='home')
def changeLogSource(request, name, faq_pk):
    questionLog = (faq_log.objects.filter
                   (faq_id__faq_id_value=faq_pk).
                   order_by('-faq_logging_id'))
    latest = faq_log.objects.filter(faq_id__faq_id_value=faq_pk).order_by(
        '-faq_logging_id')[0]
    return render(request, 'kb/changelog_source.html',
                  {'questionLog':questionLog, 'latest':latest})
#Add tags to a question
@login_required
@user_passes_test(check_group, login_url='home')
def addTag(request, name, faq_pk):
    question = get_object_or_404(faq, pk=faq_pk)
    c = get_object_or_404(category, name=name)
    t = tag.objects.order_by('tag_name')
    existTag = question.tag_faq.order_by('tag_name')
    tagPKList = []
    if request.method == "POST":
        tagList = request.POST.getlist('tags')
        for x in tagList:
            tagPK = tag.objects.get(tag_name=x).pk
            tagPKList.append(tagPK)
            question.tag_faq.set(tagPKList)
        return redirect('answer', name=c.name, faq_pk=question.pk)
    return render(request, 'kb/new_tag.html',
                  {'question':question, 'c':c, 'tag':t, 'existTag':existTag})

#Create a new tag
@login_required
@user_passes_test(check_group, login_url='home')
def createTag(request, name, faq_pk):
    question = get_object_or_404(faq, pk=faq_pk)
    c=get_object_or_404(category, name=name)
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tagform = form.save(commit=False)
            try:
                tagobj = tag.objects.get(tag_name=tagform.tag_name)
                return redirect('add_Tag', name=c.name, faq_pk=question.pk)
            except tag.DoesNotExist:
                tagform.save()
                return redirect('add_Tag', name=c.name, faq_pk=question.pk)
    else:
        form = TagForm()
    return render(request, 'kb/create_tag.html',
                  {'tagform':form, 'question':question, 'c':c})

@login_required
def tagPage(request, tag_pk):
    tagQuestion = faq.objects.filter(tag_faq__pk=tag_pk)
    Tag = get_object_or_404(tag, pk=tag_pk)
    template = 'kb/tagpage.html'
    return render(request, template, {'question':tagQuestion, 'tag':Tag})

@login_required
@user_passes_test(check_group, login_url='home')
def tagDelete(request, name, faq_pk):
    question = get_object_or_404(faq, pk=faq_pk)
    c = get_object_or_404(category, name=name)
    t = tag.objects.all()
    if request.method == "POST":
        x = request.POST.get('tags')
        try:
            deleteTag = tag.objects.get(tag_name=x)
            deleteTag.faq_set.clear()
            deleteTag.delete()
            #return redirect('add_Tag',name=c.name,faq_pk=question.pk)
            return redirect('answer', name=c.name, faq_pk=question.pk)
        except tag.ObjectDoesNotExist:
            return render(request, 'kb/delete_tag.html',
                          {'question':question, 'c':c, 'tag':t})
    return render(request, 'kb/delete_tag.html',
                 {'question':question, 'c':c, 'tag':t})
