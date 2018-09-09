from django.conf.urls import url
from django.urls import path
from fifa import views
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.HomepageView.as_view()),
    path('league/<int:league_id>/', views.LeagueView.as_view(), name = 'league'),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
