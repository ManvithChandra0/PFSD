from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')

            # Send notification email
            subject = 'Login notification'
            message = f'User {username} has logged in.'
            from_email = 'your_email@gmail.com'
            recipient_list = ['recipient1@example.com', 'recipient2@example.com']
            send_mail(subject, message, from_email, recipient_list)

            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')
