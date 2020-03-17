from django.urls import path
from .views import *
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users/password_change/', TemplateView.as_view(template_name="password_change_form.html"), name='password_change'),
    path('users/password_change/done/', TemplateView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('users/password_reset/', TemplateView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('users/password_reset/done', TemplateView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('users/reset/<uidb64>/<token>/', TemplateView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('users/reset/done/', TemplateView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

urlpatterns += [
    path('signup/', RegistrationAPIView.as_view(), name='signup'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', UserListAPIView.as_view(), name='user'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('obtain_token/', obtain_jwt_token),
    path('trading_sets/', TradingSetListAPIView.as_view(), name='tradingset'),
    path('trading_sets/<int:pk>/', TradingSetDetailAPIView.as_view(), name='tradingset_detail'),
    path('drivers/', DriverListAPIView.as_view(), name='driver'),
    path('drivers/create', DriverCreateAPIView.as_view(), name='driver_create'),
    path('drivers/<int:pk>', DriverDetailAPIView.as_view(), name='driver_detail'),
    path('individuals/', IndividualListAPIView.as_view(), name='individual'),
    path('individuals/<int:pk>', IndividualDetailAPIView.as_view(), name='individual_detail'),
    path('managers/', ManagerListAPIView.as_view(), name='manager'),
    path('managers/create', ManagerCreateAPIView.as_view(), name='manager_create'),
    path('managers/<int:pk>', ManagerDetailAPIView.as_view(), name='manager_detail'),
    path('clients/', ClientListAPIView.as_view(), name='client_list'),
    path('clients/create', ClientCreateAPIView.as_view(), name='client_create'),
]

urlpatterns += [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]