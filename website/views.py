from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signupform

#login et logout sont des fonctions, donc les views crees doivent
# avoir un nom differents pour eviter le conflit avec les fonctions


# Create your views here.

# processus d'auhentification
def home(request):
    
    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        
        #  verification de l'authentification
        user = authenticate (request, username = username, password = password)
        if user is not None:
            login (request, user)
            messages.success (request, "vous etes connecté, Bienvenue!!")
            return redirect ('home')
        else:
            messages.success (request, "Erreur de connexion, merci de reessayer")
            return redirect ('home')
    else:        
        return render(request, 'home.html', {})



def  logout_user(request): 
    logout (request)
    messages.success (request, "you have been logout")
    return render(request, 'home.html', {})


def  register_user(request): 
        if request.method == 'POST':
            form = signupform(request.POST)
            if form.is_valide():
                form.save
                
                #Authentification et Login
                username = form.cleaned_data ['username']
                password = form.cleaned_data ['password1']
                user= authenticate(username = username, password = password)
                login(request, user)

                messages.succes(request, "Vous avez été enregistré")
                return redirect('home')
            else:
                form = signupform()    
                return render(request, 'register.html', {'form':form})