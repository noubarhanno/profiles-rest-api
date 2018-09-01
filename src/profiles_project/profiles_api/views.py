from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):
        """Return a list of API View Features"""

        an_apiview=[
            'Uses HTTP methods as function (get, post ,patch , put ,delete)',
            'it is similar to a traditional django view',
            'Gives you the most control over your logic',
            'is mapped manually to urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """Handles updating an object."""

        return Response({'method':'post'})

    def patch(self , request, pk=None):
        """path request, only updates fields provided in the request"""

        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """deletes an object"""

        return Response({'message':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializers

    def list(self,request):
        """Return a hello Message"""

        a_viewset = [
            'uses actions (list , create , retrieve , update , partial_update)',
            'automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self , request):
        """Create a new Hello message"""

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID"""

        return Response({'http_method':'GET'})

    def update(self , request , pk=None):
        """Handles updating an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self , request , pk=None):
        """Handles updating part of an object"""

        return Response({'http_method':'PATCH'})

    def destroy(self , request , pk=None):
        """Handles removing an object"""

        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles Creating and updating Profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
