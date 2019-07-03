from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from . import forms
app_name = 'accounts'


urlpatterns = [
    url(r"^role1login/$", auth_views.LoginView.as_view(template_name="accounts/role1/login.html",
        extra_context={'next': '#',},redirect_authenticated_user=True,authentication_form=forms.RoleOneLogin),
        name='role1_login'),
    url(r"^role1logout/$", auth_views.LogoutView.as_view(), name="role1_logout"),
    url(r"^role1signup/$", views.RoleOneSignUp.as_view(), name="role1_signup"),
    url(r"^role2login/$", auth_views.LoginView.as_view(template_name="accounts/role2/login.html",redirect_authenticated_user=True,authentication_form=forms.RoleTwoLogin),name='role2_login'),
    url(r"^role2logout/$", auth_views.LogoutView.as_view(), name="role2_logout"),
    url(r"^role2signup/$", views.RoleTwoSignUp.as_view(), name="role2_signup"),
]
