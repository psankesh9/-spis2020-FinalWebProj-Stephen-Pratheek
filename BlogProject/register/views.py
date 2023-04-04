from django.shortcuts import render, redirect
from .forms import RegisterForm

#Rendering the registration page
def register(response):
    form = RegisterForm()
    if response.method == "POST": #if registration form is submitted
        form = RegisterForm(response.POST) #gets the submitted data
        if form.is_valid():
            form.save() #save the data in the database to create a new user
        return redirect("/") #redirects to homepage
    else:
        #failure to comply to submission requirements results in the same page
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})