# from django.urls import path
# from .views import DashboardView, AdminPanelView

# urlpatterns = [
#     path("", DashboardView.as_view(), name="dashboard"),
#     path("admin_panel/", AdminPanelView.as_view(),
#         name="admin_panel"),
# ]

from django.urls import path
from .views import DashboardRouterView, ConsumerDashboardView, BakeryDashboardView

urlpatterns = [
    path("", DashboardRouterView.as_view(), name="dashboard"),
    path("consumer/", ConsumerDashboardView.as_view(), name="consumer_dashboard"),
    path("bakery/", BakeryDashboardView.as_view(), name="bakery_dashboard"),
]