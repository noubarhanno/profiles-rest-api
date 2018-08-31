from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Return a list of API View Features"""

        an_apiview=[
            'Uses HTTP methods as function (get, post ,patch , put ,delete)',
            'it is similar to a traditional django view',
            'Gives you the most control over your logic',
            'is mapped manually to urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
