from django.conf.urls import patterns, url
from app.views import HomeView

urlpatterns = patterns('app.views',
    url(r'^home/$',HomeView.as_view(),name='app.views.home'),
)
