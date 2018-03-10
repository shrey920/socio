from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile/<username>', views.ProfileView.as_view(), name="profileView"),
    path('profile/edit/<pk>', views.UpdateProfileView.as_view(), name="editProfile")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
