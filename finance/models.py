from django.db import models
from django.contrib.auth import get_user_model

class Transaction(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(
        max_length=2,
        choices=TRANSACTION_TYPE_CHOICES,
        default=EXPENSE,
    )

    def __str__(self):
        return self.title
