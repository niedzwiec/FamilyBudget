from django.urls import include, path
from rest_framework import routers
from budget import views

router = routers.DefaultRouter()
router.register(r'budget_category', views.BudgetCategoryViewSet)
router.register(r'budget', views.BudgetViewSet)
router.register(r'cash_move', views.CashMoveViewSet)


urlpatterns = [
    path('', include(router.urls)),
]