from . import views
from django.urls import path


urlpatterns = [
     path('', views.EventList.as_view(), name='home'),
     path('yourevents/', views.YourEventList.as_view(), name='your_events'),
     path('eventorg/', views.EventOrg.as_view(), name='event_org'),
     path('ownconpan/', views.OwnConPan, name='own_con_pan'),
     path('<str:event_name>/', views.EventView.as_view(), name='event_view'),
     path('<str:event_name>/eventreg/',
          views.EventReg.as_view(), name='event_reg'),
     path('<str:event_name>/eventunreg/',
          views.EventUnReg.as_view(), name='event_unreg'),
     path('<str:event_name>/eventthanks/',
          views.EventReg.as_view(), name='event_thanks'),
     path('<str:event_name>/rego/', views.UserReg.as_view(), name='user_reg'),
]
