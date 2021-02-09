"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from kb import views as kbviews
from ds import views as dsviews
#from ds.views import PhotoCreateView
#from roadmaps.views import CreateRoadmapView, CreateRoadmapUrlView, UpdateRoadmapUrlView
from argus import views as aviews
from process import views as pviews
from roadmaps import views as rviews
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', dsviews.home, name='home'),
    re_path('login/$',
            auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path('logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('ckdeditor/', include('ckeditor_uploader.urls')),
    #path('roadmaps/', rviews.roadmapList, name="roadmap_list"),
    #path('roadmaps/<pk>', rviews.roadmapPage, name='roadmap_page'),
    #path('roadmaps_add/', CreateRoadmapUrlView.as_view(), name="new_roadmap"),
    #path('roadmaps/<pk>/edit', UpdateRoadmapUrlView.as_view(), name="edit_roadmap"),
    #path('arcade_weekly_roadmap/', rviews.arcadeWeeklyPage, name="roadmap"),
    #path('upload/', CreateRoadmapView.as_view(), name='upload'),
    #path('upload_photo/', PhotoCreateView.as_view(), name='upload_photo'),
    path('profile_page/', dsviews.profile_page, name='profile_page'),
    path('edit_profile_photo/', dsviews.edit_profile_photo, name='edit_profile_photo'),
    path('edit_profile/', dsviews.edit_profile, name='edit_profile'),
    path('team', dsviews.teams, name='team_page'),
    path('team_member/<username>', dsviews.team_member, name='team_member'),
    path('kb/', kbviews.kb, name='kb'),
    path('kb/overall/', kbviews.overall, name='overall'),
    path('kb/search', kbviews.searchQA, name='faq_search'),
    path('kb/<name>/', kbviews.category_faq, name='faq'),
    path('kb/<name>/<faq_pk>', kbviews.faq_answer, name='answer'),
    path('kb/<name>/faq/new', kbviews.new_question, name='new_FAQ'),
    path('kb/<name>/<faq_pk>/edit', kbviews.editQA, name="edit_FAQ"),
    path('kb/<name>/<faq_pk>/change_log', kbviews.changeLog, name="change_Log"),
    path('kb/<name>/<faq_pk>/pinqa', kbviews.pinQuestion, name="pinQuestion"),
    path('kb/<name>/<faq_pk>/unpinqa', kbviews.unpinQuestion, name="unpinQuestion"),
    path('kb/<name>/<faq_pk>/change_log/source',
         kbviews.changeLogSource, name="changelog_source"),
    path('kb/<name>/<faq_pk>/add_tag', kbviews.addTag, name="add_Tag"),
    path('kb/<name>/<faq_pk>/create_tag', kbviews.createTag, name="create_Tag"),
    path('kb/<name>/<faq_pk>/delete_tag', kbviews.tagDelete, name="delete_Tag"),
    path('kb/tag/<tag_pk>/', kbviews.tagPage, name='tag_page'),

    path('ds/clientlist/', dsviews.clientlist, name='clientlist'),
    path('ds/clientlist_all/', dsviews.clientlist2, name='clientlist2'),
    path('ds/search/', dsviews.searchCompany, name='searchCompany'),
    path('ds/client/<orgid>/', dsviews.client_pages, name='client_pages'),
    path('ds/client/<orgid>/newinteraction/',
         dsviews.new_interaction, name='new_interaction'),
    path('ds/client/<orgid>/interaction/<interaction_pk>/edit/',
         dsviews.InteractionUpdate.as_view(), name='edit_interaction'),
    path('ds/client/<orgid>/newxraccount', dsviews.new_xr_account, name='new_xr_account'),
    path('ds/client/<orgid>/xr_user/<pk>/edit/',
         dsviews.XRAccountUpdate.as_view(), name='edit_xr_account'),
    path('ds/client/<orgid>/newsubscription/',
         dsviews.new_subscription, name='new_subscription'),
    path('ds/client/<orgid>/subscription/<subscription_pk>/edit/',
         dsviews.SubscriptionUpdate.as_view(), name='edit_subscription'),
    path('ds/client/<orgid>/newxrsubscription/',
         dsviews.new_xr_subscription, name='new_xr_subscription'),
    path('ds/client/<orgid>/xrsubscription/<xr_sub_id>/edit/',
         dsviews.XRSubscriptionUpdate.as_view(), name='edit_xr_subscription'),
    path('ds/client/<orgid>/newaccount/', dsviews.new_account, name='new_account'),
    # path('ds/client/<orgid>/account/<account_pk>/edit/',
    #      dsviews.AccountUpdate.as_view(), name='edit_account'),
    path('ds/newclient/', dsviews.new_company, name='new_company'),
    path('ds/expiring_accounts/', dsviews.expiringSub, name='expiring_account'),
    path('ds/client/<pk>/edit/',
         dsviews.CompanyUpdate.as_view(), name='edit_company'),

    path('rekt/', pviews.rekthome, name='rekthome'),
    path('rekt/earlyaccess_progress', pviews.process, name='current'),
    path('rekt/live_progress', pviews.liveprocess, name='liveprocess'),
    path('rekt/earlyaccess_sandbox', pviews.sandboxea, name='sandboxea'),
    path('rekt/live_sandbox', pviews.sandboxlive, name='sandboxlive'),
    path('rekt/earlyaccess_history', pviews.eaHistory, name='eahistory'),
    path('rekt/earlyaccess_hisotry/search', pviews.eaSearch, name='easearch'),
    path('rekt/live_history', pviews.liveHistory, name='livehistory'),
    path('rekt/live_hisotry/search', pviews.liveSearch, name='livesearch'),


    path('dslog/', dsviews.logtable, name='logtable'),
    path('dslog/<oid>', dsviews.logpage, name='logcompany'),
    path('dslog/client/search', dsviews.searchLog, name='logSearch'),


    path('argus/', aviews.argushome, name="argushome"),
    path('argus/devname', aviews.devName, name="devName"),
    path('argus/pubname', aviews.pubName, name="pubName"),
    path('argus/titlecase', aviews.titleCase, name="titleCase"),
    path('argus/whitespace', aviews.whiteSpace, name="whiteSpace"),
    path('argus/duplicate_market_level',
         aviews.DuplicateMarket, name="DuplicateMarket"),
    path('argus/duplicate_market_level_genre',
         aviews.DuplicateMarketGenre, name="DuplicateMarketGenre"),
    path('argus/duplicate_market_level_platform',
         aviews.DuplicateMarketPlatform, name="DuplicateMarketPlatform"),
    path('argus/duplicate_title_level',
         aviews.DuplicateTitle, name="DuplicateTitle"),
    path('argus/negative_market_level',
         aviews.NegativeMarket, name="NegativeMarket"),
    path('argus/negative_market_level_genre',
         aviews.NegativeMarketGenre, name="NegativeMarketGenre"),
    path('argus/negative_market_level_platform',
         aviews.NegativeMarketPlatform, name="NegativeMarketPlatform"),
    path('argus/negative_title_level', aviews.NegativeTitle, name="NegativeTitle"),
    path('argus/title_conversion_ingame',
         aviews.titleConIngame, name="titleConIngame"),
    path('argus/title_conversion_micro', aviews.titleConMicro, name="titleConMicro"),
    path('argus/title_mau_lifetime_downloads',
         aviews.TitleMauVsLifetimeDownloads, name="TitleMauVsLifetimeDownloads"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
