from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    class CategoryType(models.TextChoices):
        INCOME = 'income', 'Income'
        EXPENSE = 'expense', 'Expense'

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='categories')
    
    name = models.CharField(max_length=64)

    type = models.CharField(max_length=10,
                            choices=CategoryType.choices,
                            default=CategoryType.EXPENSE)
    
    def __str__(self):
        return f"{self.name} - {self.type}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "name"], name='unique_user_category')
        ]
    

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='transactions')
    
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='transactions')
    
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2)
    
    description = models.TextField(null=True, blank=True)

    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}: {self.amount} -> {self.category.name} {self.date}"
