from .models import Person
from .forms import PersonModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def welcome(request):
    if request.user.is_authenticated:
        return redirect("/bonus")
    else:    
        return render(request, "apply/welcome.html")

@login_required
def apply(request):
    if request.method == "POST":
        # save to DB
        form = PersonModelForm(request.POST)
        context = {'form': form}    
        if form.is_valid():
            form.save()
            # re-direct to a html (show success information)
            return render(request, "apply/apply_success.html", context)            
        else:
            return render(request, "apply/apply_fail.html", context) 
    form = PersonModelForm()

    context = {
        'form': form
    }

    # field the form
    return render(request, "apply/apply.html", context)

@login_required
def myapply(request):
    if request.user.is_authenticated:
        # get the person
        person = Person.objects.filter(account=request.user)
        if person:
            context = {
                "user": request.user,
                "person": person[0]
            }
        return render(request, "apply/my_apply.html", context)
    else:
        return redirect("/accounts/login")     