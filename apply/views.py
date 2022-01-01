from django.shortcuts import render
from .forms import PersonModelForm

def index(request):

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