from django.urls import path
from .views import TemplateView

from .views import UserRegView

urlpatterns = [
    path("signup",UserRegView.as_view(),name="signup"),
    # path("signup/Emp",Employee.as_view(),name="Emp"),
    path("signin",TemplateView.as_view(template_name="./jobapp/login.html"),name="signin")
]