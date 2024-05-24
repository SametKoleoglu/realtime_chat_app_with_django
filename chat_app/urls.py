from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('friends/<str:pk>', views.detail, name='detail'),
    path('sent_msg/<str:pk>', views.sent_messages, name='sent_msg'),
    path('rec_msg/<str:pk>', views.received_messages, name='rec_msg'),
    path('notification', views.chat_notification, name='notification'),
]
