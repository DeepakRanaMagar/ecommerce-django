from django.shortcuts import render, redirect
from .forms import RegisterForm


'''
    Registration Section
'''
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form} )