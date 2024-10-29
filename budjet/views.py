from django.shortcuts import render,redirect

from django.views.generic import View

from budjet.forms import ExpenseForm,RegistationForm,LoginInForm

from django.contrib import messages

from budjet.models import Expense

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.db.models import Q

from budjet.decorators import signin_required

from django.utils.decorators import method_decorator

from django.views.decorators.cache import never_cache



@method_decorator([signin_required,never_cache],name="dispatch")
class ExpenseCreateView(View):
    def get(self,request,*args,**kwargs):

        form_instance=ExpenseForm()

        return render(request,"create.html",{"form":form_instance})
    


    def post(self,request,*args,**kwrags):

        form_instance=ExpenseForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.user=request.user

            form_instance.save()

            messages.success(request,"expense is added successfully")

            return redirect("expense-list")
        
        else:
            messages.error(request,"expense is not added")

            return render(request,"create.html",{"form":form_instance})
        


        
@method_decorator([signin_required,never_cache],name="dispatch")
class ExpenseListView(View):

    def get(self,request,*args,**kwargs):


        search_text=request.GET.get("search_text")

        selected_category=request.GET.get("category","all")

        if  selected_category =="all":
            qs=Expense.objects.filter(user=request.user)

        else:
            qs=Expense.objects.filter(category=selected_category,user=request.user)
    

        if search_text!=None:
            qs=Expense.objects.filter(user=request.user)
            qs=qs.filter(title__contains=search_text)


        return render(request,"expense_list.html",{"expense":qs,"selected":selected_category})
    

        
@method_decorator([signin_required,never_cache],name="dispatch")
class ExpenseDetailView(View):

    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")

        qs=Expense.objects.get(id=id)

        return render(request,"expense_detail.html",{"expense":qs})
    


  

@method_decorator([signin_required,never_cache],name="dispatch")
class ExpenseUpdataView(View):

    def get(self,request,*args,**kwargs):
       
        id=kwargs.get("pk")

        qs=Expense.objects.get(id=id)  

        form_instance=ExpenseForm(instance=qs)

        return render(request,"expense_update.html",{"form":form_instance}) 
    

    def post(self,request,*args,**kwargs):

        form_instance=ExpenseForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Expense.objects.filter(id=id).update(**data)

            return redirect("expense-list")
        
        else:

             return render(request,"expense_update.html",{"form":form_instance}) 
        

@method_decorator([signin_required,never_cache],name="dispatch")
class ExpenseDeleteView(View):

    def get(self,request,*args,**kwrags):

        id=kwrags.get("pk")

        qs=Expense.objects.get(id=id).delete()

        return redirect("expense-list")
    


@method_decorator([signin_required,never_cache],name="dispatch") 
class ExpenseSummaryView(View):

    def get(self,request,*args,**kwrags):

        qs=Expense.objects.filter(user=request.user)

        total_expense_count=qs.count()

        context={
            "total_expense_count":total_expense_count
        }

      

        return render(request,"expense_summary.html",context)
            

      

class SignUpView(View):
    def get(self,request,*args,**kwargs):

        form_instance=RegistationForm()

        return render(request,"sign_up.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=RegistationForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            return redirect("sign-in")
        
        else:

            return render(request,"sign_up.html",{"form":form_instance})


            
class SignInView(View):

    def get(self,request,*args,**kawargs):

        form_instance=LoginInForm()

        return render(request,"sign_in.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=LoginInForm(request.POST)

        if form_instance.is_valid():

            username=form_instance.cleaned_data.get("username")

            password=form_instance.cleaned_data.get("password")

            user_obj=authenticate(request,username=username,password=password)

            if user_obj:

                login(request,user_obj)

                return redirect("expense-list")

        else:
            return render(request,"sign_in.html",{"form":form_instance})
        

@method_decorator([signin_required,never_cache],name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):

        logout(request)    

        return redirect("sign-in")    


            

            


        
    



    













