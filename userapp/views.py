from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def auth_page(request):
    if request.method == "POST":
        action = request.POST.get("action")

        # Register
        if action == "register":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirmpassword = request.POST.get("confirmpassword")

            if password == confirmpassword:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exists")
                elif User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                else:
                    User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    messages.success(request, "Account created successfully")
                    return redirect("login")
            else:
                messages.error(request, "Passwords do not match")

        # Login
        elif action == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password")

    return render(request, "auth.html")

#logout
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("index")