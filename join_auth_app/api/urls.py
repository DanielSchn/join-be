from django.urls import path, include
from .views import RegistrationView, CustomLoginView, UserViewSet, ProfileViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user'),
router.register(r'profiles', ProfileViewSet, basename='user-profile'),


urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login')
]