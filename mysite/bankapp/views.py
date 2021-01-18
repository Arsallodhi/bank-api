from django.shortcuts import render
from .models import Bank, Account
from .serializers import BankSerializer, AccountSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsOwner

class LBankAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CBankAPI(GenericAPIView, CreateModelMixin):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RUDBankAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LCAccountAPI(GenericAPIView,ListModelMixin, CreateModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwner]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class RUDAccountAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
