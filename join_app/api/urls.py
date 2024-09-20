from django.urls import path, include
from .views import UsersView, ContactsView, TasksView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UsersView, basename='users')
router.register(r'contacts', ContactsView, basename='contacts')
router.register(r'tasks', TasksView, basename='tasks')


urlpatterns = [
    path('', include(router.urls)),
    # path('users/', UsersView.as_view()),
    # path('contacts/', ContactsView.as_view()),
    # path('market/<int:pk>/', MarketSingelView.as_view(), name='market-detail'),
    # path('market/<int:pk>/sellers/', SellerOfMarketList.as_view(),),
    # path('seller/', SellersView.as_view()),
    # path('seller/<int:pk>/', seller_editing, name='seller-detail'),
]