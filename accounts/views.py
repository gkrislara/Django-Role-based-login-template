from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class RoleOneSignUp(CreateView):
    form_class = forms.RoleOneCreateForm
    success_url = reverse_lazy("accounts:role1_login")
    template_name = "accounts/role/signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'role_one'
        return super().get_context_data(**kwargs)


class RoleTwoSignUp(CreateView):
    form_class = forms.RoleTwoCreateForm
    success_url = reverse_lazy("accounts:role2_login")
    template_name = "accounts/role2/signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'role_two'
        return super().get_context_data(**kwargs)
