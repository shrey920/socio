from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('message/create/<username>',views.CreateMessageView.as_view(), name="createMessage"),
    path('message/<username>',views.MessagesView.as_view(), name="messages"),

]
