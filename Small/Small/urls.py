from django.conf.urls import patterns, include, url
from django.contrib import admin
from Small import views
from .views import *



from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from core.views import shop


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import shop

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounting/',include('accounting.urls')),
    url(r'^core/',include('core.urls')),
    #url(r'^purchase/',include('purchase.urls')),
    url(r'^product/',include('product.urls')),
    url(r'^warehouse/',include('warehouse.urls')),
    url(r'^procurement/',include('procurement.urls')),
    # url(r'^fulfillment/',include('fulfillment.urls')),

    url(r'^$', Home.as_view(), name="home"),
    url(r'^index$', Home.as_view(), name="home"),
    url(r'^pricing$', Pricing.as_view(), name="pricing"),
    url(r'^services$', Services.as_view(), name="services"),
    url(r'^about$', About.as_view(), name="about"),
    url(r'^profile$', views.Profile, name='profile'),

    url(r'^$', Home.as_view(), name="home"),
    url(r'^index$', Home.as_view(), name="home"),
    url(r'^pricing$', Pricing.as_view(), name="pricing"),
    url(r'^services$', Services.as_view(), name="services"),
    url(r'^about$', About.as_view(), name="about"),
    url(r'^accounts/', include('registration.backends.default.urls')),


)

urlpatterns += patterns('django.contrib.auth.views',
                         url(r'^login/$', 'login',
                           {'template_name': 'registration/login.html'},
                           name = 'login'
                       ),

                       url(r'^logout/$', 'logout',
                           {'template_name': 'registration/logout.html'},
                           name = 'logout'
                       ),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
