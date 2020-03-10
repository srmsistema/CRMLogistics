from .serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from Deal.permissions import IsManager, IsClient, IsDriver



class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
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
    permission_classes = [IsAdminUser]


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TradingSetCreateAPIView(generics.CreateAPIView):
    queryset = TradingSet.objects.all()
    serializer_class = TradingSetSerializer
    permission_classes = [IsAdminUser]


class TradingSetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradingSet.objects.all()
    serializer_class = TradingSetSerializer
    permission_classes = [IsAdminUser]


class TradingSetListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TradingSetSerializer
    queryset = TradingSet.objects.all()


class DriverCreateAPIView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = DriversSerializer


class DriverListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DriversSerializer
    queryset = Driver.objects.all()


class DriverDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriversSerializer
    permission_classes = [IsAdminUser]


class IndividualListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = IndividualsSerializer
    
    queryset = Individual.objects.all()


class IndividualDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualsSerializer
    permission_classes = [IsAdminUser]


class ManagerCreateAPIView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ManagersSerializer



class ManagerListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser|IsManager]
    serializer_class = ManagersSerializer
    queryset = Manager.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff and self.request.user:
            return Clients.objects.all()
        elif self.request.user.is_manager and self.request.user:
            return Clients.objects.filter(user=self.request.user)

class ManagerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagersSerializer
    permission_classes = [IsAdminUser]


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Clients.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        user = self.request.user
        user.is_client = True
        user.save()

class ClientListAPIView(generics.ListAPIView):
    queryset = Clients.objects.all()
    permission_classes = [IsAdminUser|IsClient]
    serializer_class = ClientSerializer

    def get_queryset(self):
        if self.request.user.is_staff and self.request.user:
            return  Clients.objects.all()
        elif self.request.user.is_client and self.request.user:
            return Clients.objects.filter(user = self.request.user)






