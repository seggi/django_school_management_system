from django.shortcuts import render, redirect
from django.views.generic import TemplateView

def shuleHome(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin:admin_home')
        elif request.user.is_cachier: 
            return redirect('cachier:cachier_home')
        elif request.user.is_secretary:
            return redirect('secretary:secretary_home')

    return render(request, 'registration/login.html')


