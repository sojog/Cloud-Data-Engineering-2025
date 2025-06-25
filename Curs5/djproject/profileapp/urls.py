from django.urls import include, path
from .views import profile_view

urlpatterns = [
    path('profile/', profile_view, name="profile_url")
]
