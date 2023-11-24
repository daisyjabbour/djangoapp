from django.shortcuts import render, redirect
from .forms import TestUserForm
from .models import TestUser

def login(request):
    if request.method == 'POST':
        form = TestUserForm(request.POST)
        if form.is_valid():  # Fixed the typo: should be 'is_valid'
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # For testing purposes, save the data directly to the database
            TestUser.objects.create(username=username, password=password)

            return render(request, 'login.html') #redirect here to home page when you create one

    else:
        form = TestUserForm()
    return render(request, 'login.html')
