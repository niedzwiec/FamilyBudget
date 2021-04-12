from rest_framework import serializers

from .models import Budget, BudgetCategory, CashMove


class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ["id", 'name']


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'owner', 'shared', 'category']


class CashMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashMove
        fields = ['id', 'amount', 'type', 'budget']
