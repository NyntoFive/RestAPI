from django.urls import path
from portfolio.views import (
    portfolio_view,
    sample_a,
    sample_b,
    task_manager
)

urlpatterns = [
    path('',portfolio_view, name="portfolio"),
    path('a/',sample_a, name="sample_a"),
    path('b/',sample_b, name="sample_b"),
    path('tasks/', task_manager, name="tasks"),
]