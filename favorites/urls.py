from django.urls import path
from .views import MovieSearchView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('movies/', MovieSearchView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
]
