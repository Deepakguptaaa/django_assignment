# from django.urls import path
# from .views import hello_view

# urlpatterns = [
#     path('', hello_view, name='hello'),
# ]




from django.urls import path
from .views import hello_view

urlpatterns = [
    path('', hello_view),
]


from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




from django.urls import path
from .views import public_view, protected_view

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
]
