from django.urls import path
from .views import SignUpView, RegistrationAPIView, UserListAPIView, UserRetrieveUpdateAPIView, LoginAPIView, \
    TradingSetDetailAPIView, TradingSetListAPIView, LegalEntityListAPIView
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url
# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('users/password_change/', TemplateView.as_view(template_name="password_change_form.html"), name='password_change'),
#     path('users/password_change/done/', TemplateView.as_view(template_name='password_change_done.html'), name='password_change_done'),
#     path('users/password_reset/', TemplateView.as_view(template_name='password_reset_form.html'), name='password_reset'),
#     path('users/password_reset/done', TemplateView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
#     path('users/reset/<uidb64>/<token>/', TemplateView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
#     path('users/reset/done/', TemplateView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
# ]

urlpatterns = [
    path('signup/', RegistrationAPIView.as_view(), name='signup'),
    path('user/<int:pk>/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', UserListAPIView.as_view(), name='user'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('obtain_token/', obtain_jwt_token),
    path('trading_set/', TradingSetListAPIView.as_view(), name='tradingset'),
    path('trading_set/<int:pk>/', TradingSetDetailAPIView.as_view(), name='tradingset'),
    path('legal_entity/', LegalEntityListAPIView.as_view(), name='tradingset')
]
