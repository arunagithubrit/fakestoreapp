from django.shortcuts import render

# Create your views here.
from store.models import Category,User,Products
from store_api.serializers import CategorySerializer,ProductSerializer
from store_api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import action

class CategoryView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CategorySerializer
    model=Category
    queryset=Category.objects.all()

    @action(methods=["post"],detail=True)
    def add_product(self,request,*args,**kwargs):
        cid=kwargs.get("pk")
        obj=Category.objects.get(id=cid)
        
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    
class UserCreationView(APIView):
    
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class ProductView(ModelViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductSerializer
    queryset=Products.objects.all()
    model=Products

    








