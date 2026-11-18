# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from .forms import CustomUserCreationForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     template_name = "registration/signup.html"
#     success_url = reverse_lazy("login")

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, UserProfileUpdateForm
from .models import CustomUser

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Account created successfully! Please log in."

class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileUpdateForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("profile")
    success_message = "Profile updated successfully!"

    def get_object(self, queryset=None):
        # Ensures users can ONLY view and edit their own profile
        return self.request.user