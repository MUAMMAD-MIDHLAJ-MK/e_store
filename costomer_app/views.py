
from .forms import costomerRegistrationForm
#from .models import costomer

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
#from django.http import HttpResponse 
  



def register_costomer(request):
    if request.method == 'POST':
        form = costomerRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.password = make_password(form.cleaned_data['password'])
            obj.save()

            messages.success(request, "registered successfully.")
            return redirect('register')
    else:
        form = costomerRegistrationForm()

      

    return render(
         request,
         'register.html',
          {
            'form': form,
          
          }
    )
    
    '''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import costomerRegistrationForm

def register_costomer(request):
    if request.method == 'POST':
        form = costomerRegistrationForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.password = make_password(form.cleaned_data['password'])
            obj.save()

            messages.success(request, "Registered Successfully")
            return redirect('costomer_app:register')# Change to your URL name

    else:
        form = costomerRegistrationForm()

    return render(request, 'register.html',
                  {'form': form
                   })

'''