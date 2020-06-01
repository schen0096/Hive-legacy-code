from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
import argus.models as m
from django.db import connections
from django.db.utils import OperationalError


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
        T1 = m.TitleLevelConversionIngame.objects.using('argus').all().count()
        T2 = m.TitleLevelConversionMicro.objects.using('argus').all().count()
        T3 = m.TitleLevelMauVsLifetimeDownloadsExcess.objects.using('argus').all().count()
        T4 = m.TitleLevelPlatformVsSubplatformF2PConsoleMau.objects.using('argus').all().count()
        T5 = m.TitleLevelPlatformVsSubplatformF2PConsoleRevenue.objects.using('argus').all().count()
        T6 = m.TitleLevelPlatformVsSubplatformF2PPcMau.objects.using('argus').all().count()
        T7 = m.TitleLevelPlatformVsSubplatformF2PPcRevenue.objects.using('argus').all().count()
        T8 = m.TitleLevelPlatformVsSubplatformMobileMau.objects.using('argus').all().count()
        T9 = m.TitleLevelPlatformVsSubplatformMobileRevenue.objects.using('argus').all().count()
        T10 = m.TitleLevelPlatformVsSubplatformP2PPcMau.objects.using('argus').all().count()
        T11 = m.TitleLevelPlatformVsSubplatformP2PPcRevenue.objects.using('argus').all().count()
        T12 = m.TitleLevelPlatformVsSubplatformPremiumConsoleMau.objects.using('argus').all().count()
        T13 = m.TitleLevelPlatformVsSubplatformPremiumConsoleRevenue.objects.using('argus').all().count()
        T14 = m.TitleLevelPlatformVsSubplatformPremiumPcMau.objects.using('argus').all().count()
        T15 = m.TitleLevelPlatformVsSubplatformPremiumPcRevenue.objects.using('argus').all().count()
        T16 = m.TitleLevelRegionVsSubregionF2PConsoleMau.objects.using('argus').all().count()
        T17 = m.TitleLevelRegionVsSubregionF2PConsoleRevenue.objects.using('argus').all().count()
        T18 = m.TitleLevelRegionVsSubregionF2PPcMau.objects.using('argus').all().count()
        T19 = m.TitleLevelRegionVsSubregionF2PPcRevenue.objects.using('argus').all().count()
        T20 = m.TitleLevelWwVsRegionsF2PConsoleMau.objects.using('argus').all().count()
        T21 = m.TitleLevelWwVsRegionsF2PConsoleRevenue.objects.using('argus').all().count()
        T22 = m.TitleLevelWwVsRegionsF2PPcMau.objects.using('argus').all().count()
        T23 = m.TitleLevelWwVsRegionsF2PPcRevenue.objects.using('argus').all().count()
        T24 = m.TitleLevelWwVsRegionsP2PPcMau.objects.using('argus').all().count()
        T25 = m.TitleLevelWwVsRegionsP2PPcRevenue.objects.using('argus').all().count()
        T26 = m.TitleLevelWwVsRegionsPremiumConsoleMau.objects.using('argus').all().count()
        T27 = m.TitleLevelWwVsRegionsPremiumConsoleRevenue.objects.using('argus').all().count()
        T28 = m.TitleLevelIngameRevenueAggregate.objects.using('argus').all().count()
        h1 = m.HighConversionRateMarketLevel.objects.using('argus').all().count()
        h2 = m.HighConversionRateMarketLevelGenre.objects.using('argus').all().count()
        h3 = m.HighConversionRateMarketLevelPlatform.objects.using('argus').all().count()
        h4 = m.HighConversionRateTitleLevel.objects.using('argus').all().count()
        h5 = m.HighArpmauTitleLevel.objects.using('argus').all().count()
        h6 = m.HighIngameArppuMarketLevel.objects.using('argus').all().count()
        h7 = m.HighIngameArppuMarketLevelPlatform.objects.using('argus').all().count()
        h8 = m.HighIngameArppuTitleLevel.objects.using('argus').all().count()
        h9 = m.HighIngameArppuMarketLevelGenre.objects.using('argus').all().count()
        return render(request, 'argus/argus_home.html',
                      {'a':String1, 'b':String2, 'c':String3, 'd':String4, 'e':Duplicate1,
                       'f':Duplicate2, 'g':Duplicate3, 'h':Duplicate4, 'i':Negative1,
                       'j':Negative2,'k':Negative3,'l':Negative4,'m':T1,'n':T2,
                       'o':T3,'p':T4,'q':T5,'r':T6,'s':T7,'t':T8,'u':T9,'v':T10,
                       'w':T11,'x':T12,'y':T13,'z':T14,'t15':T15,'t16':T16,'t17':T17,
                       't18':T18,'t19':T19,'t20':T20,'t21':T21,'t22':T22,'t23':T23,
                       't24':T24,'t25':T25,'t26':T26,'t27':T27,'t28':T28,'h1':h1,'h2':h2,
                       'h3':h3,'h4':h4,'h5':h5,'h6':h6,'h7':h7,'h8':h8,'h9':h9})
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
@user_passes_test(check_group,login_url='home')
def NegativeMarket(request):
    table=m.NegativeCheckMarketLevel.objects.using('argus').all()
    return render(request, 'argus/negative_market.html',{'table':table})

@login_required
@user_passes_test(check_group,login_url='home')
def NegativeMarketGenre(request):
    table = m.NegativeCheckMarketLevelGenre.objects.using('argus').all()
    return render(request, 'argus/negative_market_genre.html',{'table':table})

@login_required
@user_passes_test(check_group,login_url='home')
def NegativeMarketPlatform(request):
    table=m.NegativeCheckMarketLevelPlatform.objects.using('argus').all()
    return render(request, 'argus/negative_market_platform.html',{'table':table})

@login_required
@user_passes_test(check_group,login_url='home')
def NegativeTitle(request):
    table = m.NegativeCheckTitleLevel.objects.using('argus').all()
    return render(request, 'argus/negative_title.html',{'table':table})


@login_required
@user_passes_test(check_group,login_url='home')
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