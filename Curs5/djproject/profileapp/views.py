from django.shortcuts import render, redirect

# Create your views here.


def profile_view(request):
    context = {}

    if not request.user.is_authenticated:
        return redirect("login")


    print("Este utilizatorul logat?:", request.user)

    return render(request, "profile.html", context)