from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns=[path('api/auth/login/',TokenObtainPairView.as_view()),path('api/posts/',include('posts.urls'))]
