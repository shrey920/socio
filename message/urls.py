from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'message'

urlpatterns = [
    path('message/create/<username>',views.CreateMessageView.as_view(), name="createMessage"),
    path('message/<username>',views.MessagesView.as_view(), name="messages"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
