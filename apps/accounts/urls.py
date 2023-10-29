from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
