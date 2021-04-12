from django.db import models
from django.conf import settings


class BudgetCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('id',)


class Budget(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='budgets')
    shared = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared')
    category = models.ForeignKey(BudgetCategory, on_delete=models.SET_NULL, null=True)


class CashMove(models.Model):
    TYPES = (
        (1, 'Income'),
        (2, 'Expanse'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=TYPES)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
