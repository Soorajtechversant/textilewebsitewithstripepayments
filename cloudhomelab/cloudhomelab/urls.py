from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from membership.views import *
from membership import views
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    path('',include('membership.urls')),



    # path('accounts/login/', auth_views.LoginView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
