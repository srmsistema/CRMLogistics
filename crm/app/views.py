from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render
from .forms import SignupForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import SignupForm

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from crm import settings
from django.shortcuts import render
from .renderers import UserJSONRenderer
from .models import *
from .serializers import *
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView


class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = UsersSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        serializer = UsersSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user')

        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        self.renderer_classes = JSONRenderer

        user_id = request.data.get('user_id', None)

        try:
            user = self.queryset.get(id=user_id)
        except User.DoesNotExist:
            raise Http404
        else:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class UserListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UsersSerializer

    queryset = User.objects.all()


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TradingSetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradingSet.objects.all()
    serializer_class = TradingSetSerializer

class TradingSetListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TradingSetSerializer

    queryset = TradingSet.objects.all()

class LegalEntityListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LegalEntitySerializer

    queryset = LegalEntity.objects.all()