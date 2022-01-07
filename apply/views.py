from .models import Person
from .forms import PersonModelForm
from django.views.generic import DetailView
from django.views.generic import ListView
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
        person_list = Person.objects.filter(user_account=request.user)
        if person_list:
            context = {
                "user": request.user,
                "person_list": person_list
            }
        return render(request, "apply/all_person.html", context)
    else:
        return redirect("/accounts/login")     

def all_person(request):
    person_list = Person.objects.all()
    context = {
        'person_list': person_list
    }
    return render(request, "apply/all_person.html", context)

from django.shortcuts import get_object_or_404

# update the data based on the person's primay key
def update_person(request, id):
    obj = get_object_or_404(Person, id = id)
    # obj = Person.objects.get(id = id)
    form = PersonModelForm(request.POST or None, instance = obj)

    print (">> form.is_bound: ", form.is_bound)
    print (">> form.is_valid(): ", form.is_valid())
    print (">> When form is not bound, it is not valid")
    if form.is_valid():
        form.save()
        return render(request, "apply/update_success.html")
 
    context = {'form':form} 
 
    return render(request, "apply/update_person.html", context)