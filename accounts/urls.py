from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import (
    RegisterView,LogoutView,ChangePasswordView,PasswordResetRequestView,PasswordResetConfirmView,
    ProfileView
)

app_name='accounts'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset_request/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password_reset_confirm/<uuid:uuid>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('change_password/',ChangePasswordView.as_view(), name='change_password'),
    path('profile/<str:username>/',ProfileView.as_view(), name='profile')
]