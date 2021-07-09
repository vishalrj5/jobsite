from django.urls import path
from .views import TemplateView

from .views import UserRegView,SigninView,SignOutView,UserProfileCreateView,EmployerProfileCreateView

urlpatterns = [
    path("signup",UserRegView.as_view(),name="signup"),
    # path("signup/Emp",Employee.as_view(),name="Emp"),
    path("signin",SigninView.as_view(),name="signin"),
    path("signout",SignOutView.as_view(),name="signout"),
    path("signin/jobseeker",UserProfileCreateView.as_view(),name="jobseekercreate"),
    path("signin/employer",EmployerProfileCreateView.as_view(),name="employercreate")
]