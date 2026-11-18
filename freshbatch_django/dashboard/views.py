# from django.contrib.auth.mixins import (
#     LoginRequiredMixin, UserPassesTestMixin
#     )
# from django.views.generic import TemplateView
# from accounts.models import CustomUser

# class AdminPanelView(LoginRequiredMixin,
#                      UserPassesTestMixin,
#                      TemplateView):
#     template_name = "dashboard/admin_panel.html"

# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = "dashboard/home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["member_count"] = CustomUser.objects.count()
#         context["is_admin"] = (
#             self.request.user.role == CustomUser.Role.ADMIN
#         )
#         return context

#     def test_func(self):
#         user = self.request.user
#         return user.role == CustomUser.Role.ADMIN

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from accounts.models import CustomUser

class DashboardRouterView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.role == CustomUser.Role.BAKERY:
            return redirect("bakery_dashboard")
        return redirect("consumer_dashboard")

class ConsumerDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard/consumer_dashboard.html"

    def test_func(self):
        return self.request.user.role == CustomUser.Role.CONSUMER

class BakeryDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard/bakery_dashboard.html"

    def test_func(self):
        return self.request.user.role == CustomUser.Role.BAKERY