from django.shortcuts import render, get_object_or_404
from .models import (UploadProgressCurrent, UploadProgressCount,
                     SandboxLogLive, SandboxLogEarlyaccess,
                     UploadProgressHistorical, WebsitePingResult)
from datetime import datetime, timezone, timedelta
from django.contrib.auth.decorators import login_required
import pytz
from django.db import connections
from django.db.utils import OperationalError
import requests
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Check database connectionto mysql
dbConnLab = connections['dashboard']
try:
    c = dbConnLab.cursor()
except OperationalError:
    connectedToLab = False
else:
    connectedToLab = True

dbConnTab=connections['live']
try:
    d = dbConnTab.cursor()
except OperationalError:
    connectedToTab = False
else:
    connectedToTab = True

dbConnSuper=connections['supreme']
try:
    d = dbConnSuper.cursor()
except OperationalError:
    connectedToSuper = False
else:
    connectedToSuper = True

dbConnArena = connections['arena']
try:
    d = dbConnArena.cursor()
except OperationalError:
    connectedToArena = False
else:
    connectedToArena = True

dbConnXR=connections['xr']
try:
    d = dbConnXR.cursor()
except OperationalError:
    connectedToXR = False
else:
    connectedToXR = True


@login_required
def rekthome(request):
    datetimeFormat = '%Y-%m-%d %H:%M:%S'
    statusDict={'connectedToTab':connectedToTab,'connectedToLab':connectedToLab,
                'connectedToSuper':connectedToSuper,'connectedToArena':connectedToArena,
                'connectedToXR':connectedToXR}
    response = requests.get("https://status.slack.com/api/current")
    if response.status_code == 200:
        slackApi = response.json()
        slackStatus = slackApi['status']
        if slackStatus == "ok":
            dateUpdated=slackApi["date_updated"]
            slackDict={'slackStatus':slackStatus,'dateUpdated':dateUpdated}
        else:
            dateUpdated = slackApi["date_updated"]
            slackTitle = slackApi["title"]
            slackType = slackApi["type"]
            slackDict={'slackStatus':slackStatus,'dateUpdated':dateUpdated,
                       'slackTitle':slackTitle,'slackType':slackType}
    else:
        slackDict = {}
    statusDict.update(slackDict)
#get ping results for websites
    webStatus = WebsitePingResult.objects.using('default').order_by('-id')[:4]
    webDict = {'webStatus':webStatus}
    statusDict.update(webDict)
#data for EA upload
    if connectedToLab:
        eaCurrent = UploadProgressCurrent.objects.using('dashboard').latest('time_start')
        eaCount = UploadProgressCurrent.objects.using('dashboard').count()
        eaFirstProcess = UploadProgressCurrent.objects.using('dashboard')[0]
        tz = pytz.timezone('America/New_York')
        eaStartTime = eaFirstProcess.time_start
        eaStartTimeString = eaStartTime.strftime(datetimeFormat)
        eaEndTime = eaCurrent.time_start
        eaUploadType = eaFirstProcess.current_upload_type
        now = datetime.now(tz)
        nowString = now.strftime(datetimeFormat)
        if eaUploadType is None:
            eaUploadType = 'Starting'
            eaTotalNum = 1
            eaPercent = 0
        else:
            eaUploadType = eaUploadType.capitalize()
            eaTotal = UploadProgressCount.objects.using(
                'dashboard').get(upload_type=eaUploadType)
            eaTotalNum = eaTotal.count_num
            eaPercent = eaCount/eaTotalNum*100

        if eaCount == eaTotalNum and eaCurrent.time_elapsed is not None:
            eaTime = datetime.strptime(eaCurrent.time_elapsed, '%H:%M:%S')
            eaElapsed = eaEndTime-eaStartTime + timedelta(
                hours=eaTime.hour, minutes=eaTime.minute, seconds=eaTime.second)

        else:
            eaElapsed = (datetime.strptime(nowString, datetimeFormat)
                         - datetime.strptime(eaStartTimeString, datetimeFormat))
        eaDict = {'eaCurrent':eaCurrent, 'eaCount':eaCount,
                  'eaTotalNum':eaTotalNum, 'eaUploadType':eaUploadType,
                  'eaElapsed':eaElapsed, 'eaPercent':eaPercent}
        statusDict.update(eaDict)
    if connectedToTab:
        liveCurrent = UploadProgressCurrent.objects.using('live').latest('time_start')
        liveCount = UploadProgressCurrent.objects.using('live').count()
        liveFirstProcess = UploadProgressCurrent.objects.using('live')[0]
        liveUploadType = liveFirstProcess.current_upload_type
        liveStartTime = liveFirstProcess.time_start
        liveStartTimeString = liveStartTime.strftime(datetimeFormat)
        liveEndTime = liveCurrent.time_start
        if liveUploadType is None:
            liveUploadType = 'Starting'
            liveTotalNum = 2
            livePercent = 0
        else:
            liveUploadType = liveUploadType.capitalize()
            liveTotal = UploadProgressCount.objects.using(
                'live').get(upload_type=liveUploadType)
            liveTotalNum = liveTotal.count_num
            livePercent = liveCount/liveTotalNum*100

        if liveCount == liveTotalNum and liveCurrent.time_elapsed is not None:
            liveTime = datetime.strptime(liveCurrent.time_elapsed, '%H:%M:%S')
            liveElapsed = (liveEndTime
                           - liveStartTime
                           + timedelta(hours=liveTime.hour,
                                       minutes=liveTime.minute, seconds=liveTime.second))
        else:
            liveElapsed = (datetime.strptime(nowString, datetimeFormat)
                           -datetime.strptime(liveStartTimeString, datetimeFormat))
        liveDict = {'liveCurrent':liveCurrent, 'liveCount':liveCount,
                    'liveTotalNum':liveTotalNum, 'liveUploadType':liveUploadType,
                    'liveElapsed':liveElapsed, 'livePercent':livePercent}
        statusDict.update(liveDict)
    if not connectedToLab and not connectedToTab:
        errorBoth = True
        statusDict = {'errorBoth':errorBoth}

    return render(request, 'status/rekt.html', statusDict)
@login_required
def process(request):
    data = UploadProgressCurrent.objects.using('dashboard').all()
    return render(request, 'status/labprocess.html', {'data':data})

@login_required
def liveprocess(request):
    livedata = UploadProgressCurrent.objects.using('live').all()
    return render(request, 'status/liveprogress.html', {'data':livedata})

@login_required
def sandboxea(request):
    table = SandboxLogEarlyaccess.objects.using('sandbox').all()
    return render(request, 'status/sandbox_ea.html', {'table':table})

@login_required
def sandboxlive(request):
    table = SandboxLogLive.objects.using('sandbox').all()
    return render(request, 'status/sandbox_live.html', {'table':table})

@login_required
def eaHistory(request):

    eaHistoryTable = UploadProgressHistorical.objects.using(
        'dashboard').filter(Q(year=2020)& Q(month=1)).order_by('-month', '-day')
    page = request.GET.get('page', 1)
    paginator = Paginator(eaHistoryTable, 200)
    try:
        eaHistoryTable = paginator.page(page)
    except PageNotAnInteger:
        eaHistoryTable = paginator.page(1)
    except EmptyPage:
        eaHistoryTable = paginator.page(paginator.num_pages)
    return render(request, 'status/ea_history.html', {'historyTable':eaHistoryTable})

@login_required
def eaSearch(request):
    template = 'status/ea_history.html'
    page = request.GET.get('page', 1)
    query = request.GET.get('q')
    query2 = request.GET.get('p')
    results = UploadProgressHistorical.objects.using(
        'dashboard').filter(Q(year=query)& Q(month=query2)).order_by('-day')
    paginator = Paginator(results, 200)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return render(request, template, {'historyTable':results})

@login_required
def liveHistory(request):
    liveHistoryTable = UploadProgressHistorical.objects.using(
        'live').order_by('-year', '-month', '-day')
    page = request.GET.get('page', 1)
    paginator = Paginator(liveHistoryTable, 200)
    try:
        liveHistoryTable = paginator.page(page)
    except PageNotAnInteger:
        liveHistoryTable = paginator.page(1)
    except EmptyPage:
        liveHistoryTable = paginator.page(paginator.num_pages)
    return render(request, 'status/live_history.html',
                  {'liveHistoryTable':liveHistoryTable})

@login_required
def liveSearch(request):
    template = 'status/live_history.html'
    page = request.GET.get('page', 1)
    query = request.GET.get('q')
    query2 = request.GET.get('p')
    results = UploadProgressHistorical.objects.using(
        'live').filter(Q(year=query)& Q(month=query2)).order_by('-day')
    paginator = Paginator(results, 200)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return render(request, template, {'liveHistoryTable':results})


#####ROADMAPS#######

@login_required
def roadmapList(request):
    roadmaps = RoadmapUrls.objects.all()
    return render(request, 'status/roadmaps/roadmap_list.html', {'roadmaps':roadmaps})

@login_required
def roadmapPage(request, roadmap_title):
    roadmap = get_object_or_404(RoadmapUrls, roadmap_title=roadmap_title)
    return render(request, 'status/roadmaps/roadmap_page.html', {'roadmap':roadmap})
