from django import forms

from budjet.models import Expense

from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):



    class Meta:
        model=Expense
        # fields="__all__"

        exclude=(
            "created_date",
            "user",
        )

        
        widgets={

             "title":forms.TextInput(attrs={"class":"form-control"}),
             "amount":forms.NumberInput(attrs={"class":"form-control"}),
             "category":forms.Select(attrs={"class":"form-control"}),
            
         }


class RegistationForm(forms.ModelForm):

    class Meta:

        model=User
        fields=[
            "username",
            "email",
            "password"
        ]



class LoginInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField(widget=forms.PasswordInput)



 

        

   

    
