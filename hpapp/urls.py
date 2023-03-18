from . import views
from django.urls import path


urlpatterns = [
     path('', views.EventList.as_view(), name='home'),
     path('eventorg/', views.EventOrg.as_view(), name='event_org'),
     path('ownconpan/', views.OwnConPan, name='own_con_pan'),
     path('<str:event_name>/', views.EventView.as_view(), name='event_view'),
     path('<str:event_name>/eventreg/',
          views.EventReg.as_view(), name='event_reg'),
     path('<str:event_name>/eventthanks/',
          views.EventReg.as_view(), name='event_thanks'),
]
