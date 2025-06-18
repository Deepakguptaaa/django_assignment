from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

# def hello_view(request):
#     return HttpResponse("Hello, Django!")




from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, world!")


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public endpoint."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "This is a protected endpoint only for authenticated users."})




from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])  
def public_view(request):
    return Response({"message": "This is a public endpoint!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}. This is a protected endpoint!"})
