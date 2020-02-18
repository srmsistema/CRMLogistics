from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = UsersSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        serializer = UsersSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data

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
    permission_classes = [IsAuthenticated]


class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    #renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    #renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TradingSetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradingSet.objects.all()
    serializer_class = TradingSetSerializer
    permission_classes = [IsAdminUser]


class TradingSetListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TradingSetSerializer


    queryset = TradingSet.objects.all()


class LegalEntityListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LegalEntitySerializer

    queryset = LegalEntity.objects.all()


class LegalEntityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer
    permission_classes = [IsAuthenticated]

class DriverListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DriversSerializer

    queryset = Driver.objects.all()


class DriverDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriversSerializer
    permission_classes = [IsAuthenticated]


class IndividualListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IndividualsSerializer
    
    queryset = Individual.objects.all()


class IndividualDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualsSerializer
    permission_classes = [IsAuthenticated]


class ManagerListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ManagersSerializer
    
    queryset = Manager.objects.all()


class ManagerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagersSerializer
    permission_classes = [IsAuthenticated]
