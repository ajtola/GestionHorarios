from django.shortcuts import render, redirect
from schedule_mgmt.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    return render(request, 'homepage.html')

def homepage_login(request):
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado correctamente"
                    
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "Credenciales incorrectas"
    else:
        form = LoginForm()
    if request.user.is_authenticated():
        return redirect('homepage')  
    return render(request, 'homepage_login.html', {'message': message, 'form': form} )

def logout_view(request):
    logout(request)
    return redirect('homepage')