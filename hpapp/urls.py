from . import views
from django.urls import path


urlpatterns = [
     path('', views.EventList.as_view(), name='home'),
     path('yourevents/', views.YourEventList.as_view(), name='your_events'),
     path('eventorg/', views.EventOrg.as_view(), name='event_org'),
     path('eventcreate/', views.EventCreate.as_view(), name='event_create'),
     path('eventedit/<str:event_name>',
          views.EventEdit.as_view(), name='event_edit'),
     path('eventthanks/<str:event_name>',
          views.EventThanks.as_view(), name='event_thanks'),
     path('ownconpan/', views.OwnConPan, name='own_con_pan'),
     path('<str:event_name>/', views.EventView.as_view(), name='event_view'),
     path('eventreg/<str:event_name>/',
          views.EventReg.as_view(), name='event_reg'),
     path('eventunreg/<str:event_name>',
          views.EventUnReg.as_view(), name='event_unreg'),
     path('eventdelete/<str:event_name>',
          views.EventDelete.as_view(), name='event_delete'),
     path('confirmdelete/<str:event_name>',
          views.ConfirmDelete.as_view(), name='confirm_delete'),
#    path('eventthanks/<str:event_name>/',
#         views.EventReg.as_view(), name='event_thanks'),
     path('register/<str:event_name>/',
          views.UserReg.as_view(), name='user_reg'),

]
