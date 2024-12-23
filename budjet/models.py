from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):

    title=models.CharField(max_length=200)

    amount=models.PositiveIntegerField()

    created_date=models.DateTimeField(auto_now=True)

    category_expense=(
        ("food","food"),
        ("travel","travel"),
        ("health","health"),
        ("other","other"),
    )

    category=models.CharField(max_length=200,choices=category_expense)

    user=models.ForeignKey(User,on_delete=models.CASCADE)


   



    def __str__(self) -> str:
        return self.title


 
