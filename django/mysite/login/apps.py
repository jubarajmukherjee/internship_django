from django.apps import AppConfig


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'



from rest_framework.views import APIView 

from rest_framework.response import Response 

from rest_framework.permissions import IsAuthenticated 

  

  

class HelloView(APIView): 

    permission_classes = (IsAuthenticated, ) 

  

    def get(self, request): 

        content = {'message': 'Hello, GeeksforGeeks'} 

        return Response(content) 
