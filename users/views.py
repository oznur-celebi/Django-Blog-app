from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BioUpdateForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect ('login')
    else:
        form =UserRegisterForm()
        # context ={
        #     'form' :form
        # }
    return render(request, 'users/register.html', {'form' :form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_edit(request):
    u_form =UserUpdateForm() 
    p_form =ProfileUpdateForm()
    b_form =BioUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'b_form': b_form,

    } 

    return render(request, 'users/edit.html', context)
