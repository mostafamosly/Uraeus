from django.conf.urls import patterns, url
from accounting import views


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^accounts$', views.accounts_list, name='account_list'),
    url(r'^account/new$', views.account_create, name='account_add'),
    url(r'^account/edit/(?P<pk>\d+)$', views.account_update, name='account_edit'),
    url(r'^account/delete/(?P<pk>\d+)$', views.account_delete, name='account_delete'),


    url(r'^balance_sheets$', views.ListBalanceSheets.as_view(), name='balance_sheets_list'),
    url(r'^balance_sheet/new$', views.CreateBalanceSheet.as_view(), name='balance_sheet_add'),


    url(r'^assets$', views.assets_list, name='assets_list'),
    url(r'^asset/new$', views.asset_create, name='asset_add'),
    url(r'^asset/edit/(?P<pk>\d+)$', views.asset_update, name='asset_edit'),
    url(r'^asset/delete/(?P<pk>\d+)$', views.asset_delete, name='asset_delete'),


    url(r'^liabilities$', views.liabilities_list, name='liabilities_list'),
    url(r'^liability/new$', views.liability_create, name='liability_add'),
    url(r'^liability/edit/(?P<pk>\d+)$', views.liability_update, name='liability_edit'),
    url(r'^liability/delete/(?P<pk>\d+)$', views.liability_delete, name='liability_delete'),


    url(r'^equities$', views.equities_list, name='equities_list'),
    url(r'^equity/new$', views.equity_create, name='equity_add'),
    url(r'^equity/edit/(?P<pk>\d+)$', views.equity_update, name='equity_edit'),
    url(r'^equity/delete/(?P<pk>\d+)$', views.equity_delete, name='equity_delete'),

    url(r'^nvd$', views.nvd3, name='nvd3'),
    url(r'^pdf$', views.pdf, name='pdf'),

    )
