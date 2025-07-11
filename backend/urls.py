"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
] 


from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({'message': 'Django setup successful!'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world), 
]



from django.contrib import admin
from django.urls import path, include 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


from django.urls import path, include

urlpatterns = [
    path('api/', include('myapp.urls')),
]




from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # 🔥 This enables /admin/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 🔑 Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 🔁 Refresh
    path('api/', include('myapp.urls')),  # 🔁 Your public/protected endpoints
]
   

