from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile/<username>', views.ProfileView.as_view(), name="profileView"),
    path('profile/edit/<pk>', views.UpdateProfileView.as_view(), name="editProfile"),
    path('profile/create/<pk>', views.CreateProfileView.as_view(), name="createProfile"),
    path('profile/<username>/requests',views.FriendRequestView.as_view(), name="friendRequests"),
    path('request/<pk>',views.newFriendRequest, name="newFriendRequest"),
    path('request/accept/<pk>',views.acceptRequest, name="acceptRequest"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
