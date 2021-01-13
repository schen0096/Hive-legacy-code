import calendar
import csv
#import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (company, arcade_user, subscription_history, interaction,
                     orgid as orggid, company_log, arcade_user_log,
                     subscription_history_log, interaction_log,
                     ArcadeSubscriptionsRekt, ActiveArcadeSubscriptions,
                     profile, profile_photo, label, xr_user, xr_subscription_history,
                     PageSummary, GatekeeperLogAccount, GatekeeperLogSubscription,
                     GatekeeperLogUser, PermissionMaster, UsersEmailMapping, generator,
                     id_generator)
from django.db.models import Q, Max, Count
from django.db.models.functions import Lower
from django.views.generic import UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group, User
from datetime import datetime, timedelta
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import connections
from django.db.utils import OperationalError
from .form import (NewInteraction, NewSubscription,
                   NewAccount, NewCompany, EditCompany, UploadPic,
                   EditProfile, NewXRAccount, NewXRSubscription)
from django.urls import reverse_lazy
from itertools import chain
from django.http import HttpResponse

dbConnTab = connections['live']
try:
    d = dbConnTab.cursor()
except OperationalError:
    connectedToTab = False
else:
    connectedToTab = True

def check_group(user):
    if (user.groups.filter(name='Level 3').exists()
            or user.groups.filter(name='Level 4').exists()
            or user.groups.filter(name='Level 5').exists()):
        return True

def check_group2(user):
    if (user.groups.filter(name='Level 4').exists()
            or user.groups.filter(name='Level 5').exists()):
        return True


@login_required
def home(request):
    return render(request, 'home.html', {})

@login_required
@user_passes_test(check_group, login_url='home')
def clientlist(request):
    #companys=company.objects.filter(client_status="ACTIVE").order_by('cname')
    currentUser=request.user
    if currentUser.groups.filter(name='demo').exists():
        companies = company.objects.annotate(
            num_user=Count('arcade_user',
                           filter=Q(
                               arcade_user__aracde_user_status="ACTIVE"))).filter(cname__icontains='demo').order_by('cname')

    else:
        companies = company.objects.annotate(
            num_user=Count('arcade_user',
                           filter=Q(arcade_user__aracde_user_status=
                                    "ACTIVE"))).filter(client_status=
                                                       "ACTIVE").order_by('cname')
    page = request.GET.get('page', 1)
    paginator = Paginator(companies, 25)

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)
    latest = subscription_history.objects.all().values(
        'company_id').annotate(latest=Max('subscription_start'))
    latest2 = subscription_history.objects.all().values(
        'company_id').annotate(latest=Max('subscription_end'))
    return render(request, 'ds/clientlist.html',
                  {'companys':companies, 'latest':latest,
                   'latest2':latest2})

@login_required
@user_passes_test(check_group, login_url='home')
def clientlist2(request):
    companys = company.objects.annotate(
        num_user=Count('arcade_user',
                       filter=Q(arcade_user__aracde_user_status=
                                "ACTIVE"))).order_by('cname')
    page = request.GET.get('page', 1)
    paginator = Paginator(companys, 25)

    try:
        companys = paginator.page(page)
    except PageNotAnInteger:
        companys = paginator.page(1)
    except EmptyPage:
        companys = paginator.page(paginator.num_pages)

    latest = subscription_history.objects.all().values(
        'company_id').annotate(latest=Max('subscription_start'))
    latest2 = subscription_history.objects.all().values(
        'company_id').annotate(latest=Max('subscription_end'))
    #Usercount=arcade_user.objects.filter(aracde_user_status='ACTIVE').count()
    return render(request, 'ds/clientlist_all.html',
                  {'companys':companys, 'latest':latest, 'latest2':latest2})


@login_required
@user_passes_test(check_group, login_url='home')
def client_pages(request, orgid):
    c = get_object_or_404(company, orgid=orgid)
    #arcade_users = c.arcade_user.all().order_by('arcade_user_id')
    current_users = UsersEmailMapping.objects.using(
        'arcade_frontend').filter(subscription_id=c.arcade_id)
    xr_users = c.xr_user.all().order_by('xr_user_status')
    arcadeID = c.arcade_id
    history = c.subscription_history.all().order_by('-subscription_start')
    xr_histories = c.xr_sub_history.all().order_by('-xr_subscription_start')
    contractURL = c.contract.replace("https://", "")

    try:
        xr_tiers = c.xr_sub_history.all().order_by(
            '-xr_subscription_start')[0].xr_tier
    except IndexError:
        xr_tiers = ""
    if connectedToTab:
        try:
            activeSubList = (
                ActiveArcadeSubscriptions.objects.using('arcade_frontend').filter(
                    subscription_id=str(c.arcade_id)).values('ftp', 'status')[0])
            ftpStatus = activeSubList['ftp']
            arcadeStatus = activeSubList['status']
        except (IndexError, OperationalError):
            ftpStatus = 0
            arcadeStatus = 0

        try:
            subList = ArcadeSubscriptionsRekt.objects.using(
                'live').filter(subscription_id=arcadeID)
        except IndexError:
            subList = []
    else:
        ftpStatus = "N/A"
        arcadeStatus = "N/A"
        subList = []
    inter = c.interaction.all()
    # UserCount = c.arcade_user.filter(aracde_user_status='ACTIVE').count()
    UserCount = current_users.filter(status=1).count()
    XRUserCount = c.xr_user.filter(xr_user_status='ACTIVE').count()
    #PageSummary.objects.using('timber').update(username = Lower('username'))
    user_log = PageSummary.objects.using('timber').filter(username__in = 
        [user.email for user in current_users])

    return render(request, 'ds/clientpage.html',
                  {'company':c, 'auser':current_users, 'history':history,
                   'interaction':inter, 'count':UserCount, 'ftpStatus':ftpStatus,
                   'arcadeStatus':arcadeStatus, 'subList':subList, 'xr_users':xr_users,
                   'xr_histories':xr_histories, 'xr_tiers':xr_tiers,
                   'XRUserCount':XRUserCount,'contractURL':contractURL,
                   'user_log':user_log}
                   )


################################################
##########ADD/EDIT COMPANY######################
@login_required
@user_passes_test(check_group2, login_url='home')
def new_company(request):
    labels = label.objects.all()

    if request.method == "POST":
        form = NewCompany(request.POST)
        labelName = request.POST.get('select_labels')
        companyLabel = label.objects.get(label_name=labelName)
        if form.is_valid():
            Orgid = form.writeord()
            c = form.save(commit=False)
            c.company_label = companyLabel
            c.orgid = Orgid
            c.arcade_id = id_generator()
            c.save()
            # Orgid = generator()
            # company.orgid = Orgid
            # company.save()
            log = form.log()
            log.updated_by = request.user
            log.orgid = Orgid
            log.arcade_id = c.arcade_id
            log.log_notes = 'Add'
            log.label = companyLabel
            log.save()
            return redirect('clientlist')
        else:
            error=form.errors
            return render(request, 'test.html', {'error1':error})

    else:
        form = NewCompany()


    return render(request, 'ds/new_company.html', {'form':form, 'labels':labels})


@method_decorator(login_required, name='dispatch')
class CompanyUpdate(UpdateView):
    model = company
    form_class = EditCompany
    template_name = 'ds/edit_company.html'
    context_object_name = 'company'
    pk_url_kwarg = 'pk'
    def test_func(self):
        return self.request.user.groups.filter(Q(name="Level 4")|Q(name="Level 5")).exists()
    def handle_no_permission(self):
        return redirect('home')

    def form_valid(self, form):
        c = form.save(commit=False)
        c.save()
        oid = get_object_or_404(orggid, orgid_value=c.orgid)

        log = form.log()
        log.updated_by = self.request.user
        log.orgid = oid
        log.log_notes = 'Edit'
        log.save()
        return redirect('client_pages', orgid=c.orgid)

################################################################
###############ADD/EDIT ARCADE ACCOUNTS#########################


@login_required
@user_passes_test(check_group2, login_url='home')
def new_account(request, orgid):
    c = get_object_or_404(company, orgid=orgid)
    oid = get_object_or_404(orggid, orgid_value=c.orgid)
    if request.method == "POST":
        form = NewAccount(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.company_id = c
            account.save()

            log = form.log()
            log.orgid = oid
            log.updated_by = request.user
            log.log_notes = 'Add'
            log.save()
            return redirect('client_pages', orgid=orgid)
    else:
        form = NewAccount()
    return render(request, 'ds/new_account.html', {'company': c, 'form':form})


# @method_decorator(login_required, name='dispatch')
# class AccountUpdate(UserPassesTestMixin, UpdateView):
#     model = arcade_user
#     form_class = NewAccount
#     template_name = 'ds/edit_account.html'
#     pk_url_kwarg = 'account_pk'
#     context_object_name = 'account'

#     def test_func(self):
#         return self.request.user.groups.filter(
#             Q(name="Level 4")|Q(name="Level 5")).exists()
#     def handle_no_permission(self):
#         return redirect('home')

#     def form_valid(self, form):
#         account = form.save(commit=False)
#         account.save()
#         oid = get_object_or_404(orggid, orgid_value=account.company_id.orgid)
#         log = form.log()
#         log.orgid = oid
#         log.updated_by = self.request.user
#         log.log_notes = 'Edit'
#         log.save()
#         return redirect('client_pages', orgid=account.company_id.orgid)

################################################################
###############ADD/EDIT ARCADE SUBSCRIPTION#####################
@login_required
@user_passes_test(check_group2, login_url='home')
def new_subscription(request, orgid):
    c = get_object_or_404(company, orgid=orgid)
    oid = get_object_or_404(orggid, orgid_value=c.orgid)
    if request.method == "POST":
        form = NewSubscription(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.company_id = c
            subscription.save()

            log = form.log()
            log.orgid = oid
            log.sub_id = subscription.sub_id
            log.updated_by = request.user
            log.log_notes = 'Add'
            log.save()
            return redirect('client_pages', orgid=orgid)
    else:
        form = NewSubscription()
    return render(request, 'ds/new_subscription.html',
                  {'company': c, 'form':form})

@method_decorator(login_required, name='dispatch')
class SubscriptionUpdate(UpdateView):
    model = subscription_history
    form_class = NewSubscription
    template_name = 'ds/edit_subscription.html'
    pk_url_kwarg = 'subscription_pk'
    context_object_name = 'subscription'
    def test_func(self):
        return self.request.user.groups.filter(
            Q(name="Level 4")|Q(name="Level 5")).exists()
    def handle_no_permission(self):
        return redirect('home')
    def form_valid(self, form):
        subscription = form.save(commit=False)
        subscription.save()
        oid = get_object_or_404(orggid, orgid_value=subscription.company_id.orgid)
        log = form.log()
        log.orgid = oid
        log.sub_id = subscription.sub_id
        log.updated_by = self.request.user
        log.log_notes = 'Edit'
        log.save()
        return redirect('client_pages', orgid=subscription.company_id.orgid)

############################################################
###############ADD/EDIT XR ACCOUNT#########################
@login_required
@user_passes_test(check_group2, login_url='home')
def new_xr_account(request, orgid):
    c = get_object_or_404(company, orgid=orgid)
    oid = get_object_or_404(orggid, orgid_value=c.orgid)
    if request.method == "POST":
        form = NewXRAccount(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.company_id = c
            account.save()

            log = form.log()
            log.orgid = oid
            log.updated_by = request.user
            log.log_notes = 'Add'
            log.save()
            return redirect('client_pages', orgid=orgid)
    else:
        form = NewXRAccount()
    return render(request, 'ds/new_xr_account.html', {'company': c, 'form':form})

@method_decorator(login_required, name='dispatch')
class XRAccountUpdate(UserPassesTestMixin, UpdateView):
    model = xr_user
    form_class = NewXRAccount
    template_name = 'ds/edit_xr_account.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'xr_user'
    def test_func(self):
        return self.request.user.groups.filter(
            Q(name="Level 4")|Q(name="Level 5")).exists()
    def handle_no_permission(self):
        return redirect('home')

    def form_valid(self, form):
        xr_account = form.save(commit=False)
        xr_account.save()
        oid = get_object_or_404(orggid, orgid_value=xr_account.company_id.orgid)
        log = form.log()
        log.orgid = oid
        log.updated_by = self.request.user
        log.log_notes = 'Edit'
        log.save()
        return redirect('client_pages', orgid=xr_account.company_id.orgid)

############################################################
###############ADD/EDIT XR SUBSCRIPTION#####################
@login_required
@user_passes_test(check_group2, login_url='home')
def new_xr_subscription(request, orgid):
    c = get_object_or_404(company, orgid=orgid)
    oid = get_object_or_404(orggid, orgid_value=c.orgid)
    if request.method == "POST":
        form = NewXRSubscription(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.company_id = c
            subscription.save()

            log = form.log()
            log.orgid = oid
            log.xr_sub_id = subscription.xr_sub_id
            log.updated_by = request.user
            log.log_notes = 'Add'
            log.save()
            return redirect('client_pages', orgid=orgid)
    else:
        form = NewXRSubscription()
    return render(request, 'ds/new_xr_subscription.html',
                  {'company': c, 'form':form})

@method_decorator(login_required, name='dispatch')
class XRSubscriptionUpdate(UpdateView):
    model = xr_subscription_history
    form_class = NewXRSubscription
    template_name = 'ds/edit_xr_sub.html'
    pk_url_kwarg = 'xr_sub_id'
    context_object_name = 'XRSub'
    def test_func(self):
        return self.request.user.groups.filter(
            Q(name="Level 4")|Q(name="Level 5")).exists()
    def handle_no_permission(self):
        return redirect('home')
    def form_valid(self, form):
        subscription = form.save(commit=False)
        subscription.save()
        oid = get_object_or_404(orggid, orgid_value=subscription.company_id.orgid)
        log = form.log()
        log.orgid = oid
        log.xr_sub_id = subscription.xr_sub_id
        log.updated_by = self.request.user
        log.log_notes = 'Edit'
        log.save()
        return redirect('client_pages', orgid=subscription.company_id.orgid)

############################################################
###############ADD/EDIT CLIENT NOTES#####################
@login_required
@user_passes_test(check_group2, login_url='home')
def new_interaction(request, orgid):
    c = get_object_or_404(company, orgid=orgid)
    oid = get_object_or_404(orggid, orgid_value=c.orgid)
    if request.method == "POST":
        form = NewInteraction(request.POST)
        if form.is_valid():
            inter = form.save(commit=False)
            inter.user_id = request.user
            inter.company_id = c
            inter.save()

            log = form.log()
            log.orgid = oid
            log.userid = request.user
            log.updated_by = request.user
            log.interaction_id = inter.interaction_id
            log.log_notes = 'Add'

            log.save()
            return redirect('client_pages', orgid=orgid)

    else:
        form = NewInteraction()
    return render(request, 'ds/new_interaction.html', {'company': c, 'form':form})

######################################################
##############ADD/EDIT CLIENT NOTES###################
@method_decorator(login_required, name='dispatch')
class InteractionUpdate(UpdateView):
    model = interaction
    form_class = NewInteraction
    template_name = 'ds/edit_interaction.html'
    pk_url_kwarg = 'interaction_pk'
    context_object_name = 'interaction'
    def test_func(self):
        return self.request.user.groups.filter(
            Q(name="Level 4")|Q(name="Level 5")).exists()
    def handle_no_permission(self):
        return redirect('home')

    def form_valid(self, form):
        inter = form.save(commit=False)
        inter.save()

        oid = get_object_or_404(orggid, orgid_value=inter.company_id.orgid)
        interuser = get_object_or_404(User, username=inter.user_id.username)
        log = form.log()
        log.orgid = oid
        log.userid = interuser
        log.interaction_id = inter.interaction_id
        log.updated_by = self.request.user
        log.log_notes = 'Edit'
        log.save()
        return redirect('client_pages', orgid=inter.company_id.orgid)

@login_required
@user_passes_test(check_group2, login_url='home')
def searchCompany(request):
    template = 'ds/clientlist_all.html'
    query = request.GET.get('q')
    results = company.objects.annotate(
        num_user=Count('arcade_user',
                       filter=Q(arcade_user__aracde_user_status="ACTIVE")
                       )).filter(Q(cname__icontains=query)|
                                 Q(arcade_id__icontains=query)|
                                 Q(arcade_user__arcade_user_id__icontains=query)).order_by('cname')
    latest = subscription_history.objects.all().values(
        'company_id').annotate(latest=Max('subscription_start'))
    latest2 = subscription_history.objects.all().values(
        'company_id').annotate(latest=Max('subscription_end'))
    return render(request, template,
                  {'companys':results, 'latest':latest, 'latest2':latest2})

###############################################################################
###########################Data Schedule Log Table#############################
###############################################################################
###############################################################################
@login_required
@user_passes_test(check_group2, login_url='home')
def logtable(request):
    Orgid = orggid.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(Orgid, 30)
    try:
        Orgid = paginator.page(page)
    except PageNotAnInteger:
        Orgid = paginator.page(1)
    except EmptyPage:
        Orgid = paginator.page(paginator.num_pages)

    cname = company.objects.all().values('cname', 'orgid')
    return render(request, 'ds/log.html', {'log':Orgid, 'cname':cname})


@login_required
@user_passes_test(check_group2, login_url='home')
def logpage(request, oid):
    c = get_object_or_404(company, orgid=oid)
    oid = get_object_or_404(orggid, orgid_value=oid)
    arcade_users = UsersEmailMapping.objects.using('arcade_frontend').filter(
        subscription_id=c.arcade_id)
    companies = company_log.objects.filter(orgid=oid)
    arcade_client = GatekeeperLogUser.objects.using('arcade_frontend').filter(
        subscription_id__in = [user.subscription_id for user in arcade_users])
    history = subscription_history_log.objects.filter(orgid=oid)
    interactions = interaction_log.objects.filter(orgid=oid)
    return render(request, 'ds/logcompany.html',
                  {'oid':oid, 'company':companies, 'auser':arcade_client,
                   'history':history, 'interaction':interactions})


@login_required
@user_passes_test(check_group2, login_url='home')
def searchLog(request):
    template = 'ds/logsearch.html'
    query = request.GET.get('q')
    results = orggid.objects.filter(
        Q(company_log__cname__icontains=query)).distinct()
    return render(request, template, {'results':results})

@login_required
@user_passes_test(check_group2, login_url='home')
def expiringSub(request):
    today = datetime.today()
    currentMonth = today.month
    currentYear = today.year
    if currentMonth == 12:
        nextMonth = 1
        nextYear = currentMonth+1
    else:
        nextMonth = currentMonth+1
        nextYear = currentYear
    nextMonthStr = calendar.month_name[nextMonth]
    nextExp = nextMonthStr+' '+str(nextYear)
    q = str(currentYear)+'-'+str(currentMonth).zfill(2)
    expSubHist = subscription_history.objects.filter(
        Q(subscription_end__icontains=q)).order_by('subscription_end')
    HistLog = subscription_history_log.objects.filter(
        Q(subscription_end__icontains=q))
    p = str(nextYear)+'-'+str(nextMonth).zfill(2)
    nextExpSub = subscription_history.objects.filter(
        Q(subscription_end__icontains=p)).order_by('subscription_end')
    nextHistLog = subscription_history_log.objects.filter(
        Q(subscription_end__icontains=p))

    expActive = subscription_history.objects.all().values(
        'company_id__cname', 'company_id__orgid').annotate(
            last=Max('subscription_end'), subID=Max('sub_id')).filter(
                Q(last__lte=today), Q(company_id__arcade_access_status="ACTIVE"))
    logExpActive = subscription_history_log.objects.all().values(
        'orgid__orgid_value', 'sub_id').annotate(last=Max('time'))
    return render(request, 'ds/expiring_sub.html',
                  {'expSubHist':expSubHist, 'HistLog':HistLog,
                   'nextExpSub':nextExpSub, 'nextHistLog':nextHistLog,
                   'nextExp':nextExp, 'expActive':expActive,
                   'logExpActive':logExpActive})



@login_required
def profile_page(request):
    currentUser = request.user
    userPhoto = currentUser.profile.photo
    if userPhoto != None:
        url = userPhoto.upload_photo.url
    else:
        url = ""
    gamingList = profile.objects.filter(
        user=currentUser).values('steam_id', 'twitch_id',
                                 'epic_id', 'switch_id', 'blizzard_id',
                                 'playstation_id', 'discord_id', 'riot_id')[0]
    socialList = profile.objects.filter(
        user=currentUser).values('twitter_id', 'instagram_id')[0]
    return render(request, 'ds/profile_page.html', {'currentUser':currentUser,
                                                    'gamingList':gamingList,
                                                    'socialList':socialList, 'url':url})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_page')
    else:
        profile_form = EditProfile(instance=request.user.profile)
        args = {'profile_form':profile_form}
        return render(request, 'ds/edit_profile.html', args)


@login_required
def edit_profile_photo(request):
    currentProfile = get_object_or_404(profile, id=request.user.profile.id)
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, instance=request.user.profile)
        photo_form = UploadPic(request.POST, request.FILES)
        if profile_form.is_valid() and photo_form.is_valid():
            profile_instance = profile_form.save(commit=False)
            instance = photo_form.save(commit=False)
            instance.updated_by = request.user
            instance.save()
            profile_instance.photo = instance
            profile_instance.save()
            return redirect('profile_page')
        # else:
        #     error1 = profile_form.errors
        #     error2 = photo_form.errors
        #     return render(request, 'test.html', {'error1':error1, 'error2':error2})
    else:
        profile_form = EditProfile(instance=request.user.profile)
        photo_form = UploadPic()
        photo = request.user.profile.photo
        args = {'profile_form':profile_form, 'photo_form':photo_form, 'photo': photo}
        return render(request, 'ds/edit_profile_pic.html', args)

@login_required
def teams(request):
    techTeam = User.objects.filter(
        groups__name='Technovation').order_by('last_name', 'first_name')
    researchTeam = User.objects.filter(
        groups__name='Research').order_by('last_name', 'first_name')
    commercialTeam = User.objects.filter(
        groups__name='Commercial').order_by('last_name', 'first_name')
    productsTeam = User.objects.filter(
        groups__name='Products').order_by('last_name', 'first_name')
    marketingTeam = User.objects.filter(
        groups__name='Marketing').order_by('last_name', 'first_name')
    return render(request, 'ds/team_members.html',
                  {'techTeam':techTeam, 'researchTeam':researchTeam,
                   'commercialTeam':commercialTeam, 'productsTeam':productsTeam,
                   'marketingTeam':marketingTeam})

@login_required
def team_member(request, username):
    member = get_object_or_404(User, username=username)
    memberPhoto = member.profile.photo
    if memberPhoto != None:
        url = memberPhoto.upload_photo.url
    else:
        url = ""
    gamingList = profile.objects.filter(
        user=member).values('steam_id', 'twitch_id',
                            'epic_id', 'riot_id', 'switch_id', 'blizzard_id',
                            'playstation_id', 'discord_id')[0]
    socialList = profile.objects.filter(
        user=member).values('twitter_id', 'instagram_id')[0]
    return render(request, 'ds/member.html',
                  {'member':member, 'url':url,
                   'gamingList':gamingList, 'socialList':socialList})
