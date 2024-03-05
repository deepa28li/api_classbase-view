from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from app.serializers import *
from rest_framework.response import Response


class ProductCrud(APIView):
    def get(self,request):
        PDO=Product.objects.all() #orm obj
        PJO=Productmodelserializer(PDO,many=True) #json obj
        return Response(PJO.data)
    
    def post(self,request):
        JDO=request.data
        PDO=Productmodelserializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted successfully'})
        else:
            return Response({'Error':'Data is not Inserted'})
        
    
