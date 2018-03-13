from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'profiles'

urlpatterns = [
    path('all/profile',views.AllProfilesView.as_view(), name="allProfiles"),
    path('profile/<username>', views.ProfileView.as_view(), name="profileView"),
    path('profile/edit/<pk>', views.UpdateProfileView.as_view(), name="editProfile"),
    path('profile/create/<pk>', views.CreateProfileView.as_view(), name="createProfile"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
