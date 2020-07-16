from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connections
from django.db.utils import OperationalError
from django.apps import apps
import argus.models as m

dbConnLab = connections['argus']
try:
    c = dbConnLab.cursor()
except OperationalError:
    connectedToLab = False
else:
    connectedToLab = True

def check_group(user):
    if (user.groups.filter(name='Tech').exists() or
            user.groups.filter(name='QA').exists() or
            user.groups.filter(name='Analytics').exists()):
        return True

# Create your views here.
@login_required
@user_passes_test(check_group, login_url='home')
def argushome(request):
    ##Need a better solution instead of hardcoding all tables
    if connectedToLab:
        app_models = apps.get_app_config('argus').get_models()
        tname = []
        rcount = []
        for model in app_models:
            tname.append(model._meta.verbose_name)
            rcount.append(model.objects.using('argus').count())
        table = list(zip(tname, rcount))
        String1 = m.StringCheckDeveloperNameUnification.objects.using('argus').count()
        String2 = m.StringCheckPublisherNameUnification.objects.using('argus').count()
        String3 = m.StringCheckTitleCaseSensitivity.objects.using('argus').count()
        String4 = m.StringCheckWhitespace.objects.using('argus').all().count()
        Duplicate1 = m.DuplicateRowCheckMarketLevel.objects.using('argus').all().count()
        Duplicate2 = m.DuplicateRowCheckMarketLevelGenre.objects.using('argus').all().count()
        Duplicate3 = m.DuplicateRowCheckMarketLevelPlatform.objects.using('argus').all().count()
        Duplicate4 = m.DuplicateRowCheckTitleLevel.objects.using('argus').all().count()
        Negative1 = m.NegativeCheckMarketLevel.objects.using('argus').all().count()
        Negative2 = m.NegativeCheckMarketLevelGenre.objects.using('argus').all().count()
        Negative3 = m.NegativeCheckMarketLevelPlatform.objects.using('argus').all().count()
        Negative4 = m.NegativeCheckTitleLevel.objects.using('argus').all().count()
        titleCheck = list(table[12:16])
        titleCheckPlatformVsSub = list(table[16:28])
        titleCheckRegionVsSub = list(table[28:32])
        titleCheckWWVsRegion = list(table[32:40])
        highCheck = list(table[40:44])
        highARPMAUCheck = list(table[44:45])
        highInGameCheck = list(table[45:49])
        return render(request, 'argus/argus_home.html', {
            'a':String1, 'b':String2, 'c':String3, 'd':String4, 'e':Duplicate1,
            'f':Duplicate2, 'g':Duplicate3, 'h':Duplicate4, 'i':Negative1, 'j':Negative2,
            'k':Negative3, 'l':Negative4, 'm':titleCheck, 'n':titleCheckPlatformVsSub,
            'o':titleCheckRegionVsSub, 'p': titleCheckWWVsRegion, 'q':highCheck,
            'r':highARPMAUCheck, 's':highInGameCheck})
    else:
        return render(request, 'argus/argus_error.html')

# String check tables
@login_required
@user_passes_test(check_group, login_url='home')
def devName(request):
    table = m.StringCheckDeveloperNameUnification.objects.using('argus').all()
    return render(request, 'argus/developer_name.html', {'devNameTable':table})

@login_required
@user_passes_test(check_group, login_url='home')
def pubName(request):
    table = m.StringCheckPublisherNameUnification.objects.using('argus').all()
    return render(request, 'argus/publisher_name.html', {'pubNameTable':table})


@login_required
@user_passes_test(check_group, login_url='home')
def titleCase(request):
    table = m.StringCheckTitleCaseSensitivity.objects.using('argus').all()
    return render(request, 'argus/title_case.html', {'titleCaseTable':table})


@login_required
@user_passes_test(check_group, login_url='home')
def whiteSpace(request):
    table = m.StringCheckWhitespace.objects.using('argus').all()
    return render(request, 'argus/white_space.html', {'whiteSpaceTable':table})

@login_required
@user_passes_test(check_group, login_url='home')
def pubName(request):
    table = m.StringCheckPublisherNameUnification.objects.using('argus').all()
    return render(request, 'argus/publisher_name.html', {'pubNameTable':table})

# Duplicate check tables
@login_required
@user_passes_test(check_group, login_url='home')
def DuplicateMarket(request):
    table = m.DuplicateRowCheckMarketLevel.objects.using('argus').all()
    return render(request, 'argus/duplicate_market.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def DuplicateMarketGenre(request):
    table = m.DuplicateRowCheckMarketLevelGenre.objects.using('argus').all()
    return render(request, 'argus/duplicate_market_genre.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def DuplicateMarketPlatform(request):
    table = m.DuplicateRowCheckMarketLevelPlatform.objects.using('argus').all()
    return render(request, 'argus/duplicate_market_platform.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def DuplicateTitle(request):
    table = m.DuplicateRowCheckTitleLevel.objects.using('argus').all()
    return render(request, 'argus/duplicate_title.html', {'table':table})

# Negative Check Tables
@login_required
@user_passes_test(check_group, login_url='home')
def NegativeMarket(request):
    table = m.NegativeCheckMarketLevel.objects.using('argus').all()
    return render(request, 'argus/negative_market.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def NegativeMarketGenre(request):
    table = m.NegativeCheckMarketLevelGenre.objects.using('argus').all()
    return render(request, 'argus/negative_market_genre.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def NegativeMarketPlatform(request):
    table = m.NegativeCheckMarketLevelPlatform.objects.using('argus').all()
    return render(request, 'argus/negative_market_platform.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def NegativeTitle(request):
    table = m.NegativeCheckTitleLevel.objects.using('argus').all()
    return render(request, 'argus/negative_title.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def titleConIngame(request):
    table = m.TitleLevelConversionIngame.objects.using('argus').all()
    return render(request, 'argus/t_conversion_ingame.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def titleConMicro(request):
    table = m.TitleLevelConversionMicro.objects.using('argus').all()
    return render(request, 'argus/t_conversion_micro.html', {'table':table})

@login_required
@user_passes_test(check_group, login_url='home')
def TitleMauVsLifetimeDownloads(request):
    table = m.TitleLevelMauVsLifetimeDownloadsExcess.objects.using('argus').all()[:200]
    return render(request, 'argus/t_mau_lifetime_downloads.html', {'table':table})

#####Title Platform vs Subplaform
@login_required
@user_passes_test(check_group, login_url='home')
def F2PConsoleMau(request):
    table = m.TitleLevelPlatformVsSubplatformF2PConsoleMau.objects.using('argus').all()[:200]
    return render(request, 'argus/platform_subplatform/f2p_console_mau.html', {'table':table})


@login_required
@user_passes_test(check_group, login_url='home')
def F2PConsoleRevenue(request):
    table = m.TitleLevelPlatformVsSubplatformF2PConsoleRevenue.objects.using('argus').all()[:200]
    return render(request, 'argus/platform_subplatform/f2p_console_revenue.html', {'table':table})

