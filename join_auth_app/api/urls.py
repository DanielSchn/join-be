from django.urls import path
from .views import UserProfileList, UserProfileDetail, RegistrationView, CustomLoginView, UserList, UserDetailList
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailList.as_view(), name='userdetail-list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    # path('login/', obtain_auth_token, name='login'),
    path('login/', CustomLoginView.as_view(), name='login')
]
