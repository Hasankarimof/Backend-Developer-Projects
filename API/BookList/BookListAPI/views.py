from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET','POST'])
def books(request):
    return Response('list of books',
                    status=status.HTTP_200_OK)

class Orders():
    @staticmethod
    @api_view(['POST','GET','DELETE'])
    def listOrders(request):
        return Response({'message':'list of orders'},200)

class BookView(APIView):
    def list(self, request):
        return Response({"message":"All books"},status.HTTP_200_OK)
    def create(self, request):
        return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"},status.HTTP_200_OK)
    def destroy(self, request,pk=None):
        return Response({"message":"Deleting a book"},status.HTTP_200_OK)

