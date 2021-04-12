from rest_framework import viewsets, permissions

from budget.models import BudgetCategory, Budget, CashMove
from budget.serializers import BudgetCategorySerializer, BudgetSerializer, CashMoveSerializer


class BudgetCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BudgetCategory.objects.all()
    serializer_class = BudgetCategorySerializer
    filterset_fields = {
        'name': ['icontains'],
    }


class BudgetViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filterset_fields = {
        'name': ['icontains'],
        'owner': ['exact'],
        'category': ['exact'],
    }

class CashMoveViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CashMove.objects.all()
    serializer_class = CashMoveSerializer
    filterset_fields = {
        'name': ['icontains'],
        'amount': ['exact', 'lte', 'gte'],
        'type': ['exact'],
        'budget': ['exact'],
    }