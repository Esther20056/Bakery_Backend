from django.urls import path
from .views import Signup, Login

urlpatterns = [
    path('signup/', Signup),
    path('login/', Login),
]