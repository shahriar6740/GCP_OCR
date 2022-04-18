from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ImageResponseView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
                  path('upload/', ImageResponseView.as_view(), name='upload'),
                  path('login-token/', obtain_auth_token, name='api_token_auth'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
