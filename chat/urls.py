from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'chat'

urlpatterns = [
    path('chat/',views.ChatRooms.as_view(),name='chatRooms'),
    path('chat/<pk>',views.chats,name='chats'),
    path('save_message/', views.save_message, name='chat_save_message'),
]
