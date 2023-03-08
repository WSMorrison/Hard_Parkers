from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<str:event_name>/', views.EventView.as_view(), name='event_view'),
    path('<str:event_name>/eventreg/',
         views.EventReg.as_view(), name='event_reg'),
    path('<str:event_name>/eventthanks/',
         views.EventReg.as_view(), name='event_thanks'),
]
