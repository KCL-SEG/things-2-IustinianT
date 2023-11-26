from django.shortcuts import render
from .forms import ThingForm

def home(request):
    #if request.method == 'POST':
    form = ThingForm(request.POST)
        #name = form.cleaned_data('name')
        #description = form.cleaned_data('description')
        #quantity = form.cleaned_data('quantity')
        #thing = Thing
        #return render(request, 'home.html', {'form': form})
    
    return render(request, 'home.html', {'form': form})
