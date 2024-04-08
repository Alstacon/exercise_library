from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from core.views import CreateUserView, PasswordUpdateView

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup-view'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update_password/', PasswordUpdateView.as_view(), name='change_password-view'),
]
