from django.shortcuts import redirect

def signin_required(fn):


    def wrapper(request,*args,**kwargs):

        if not request.user.is_authenticated:

            return redirect("sign-in")
        
        else:

            return fn(request,*args,**kwargs)
        
    return wrapper

  



