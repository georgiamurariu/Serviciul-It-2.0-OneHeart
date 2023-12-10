from django.shortcuts import render, redirect,get_object_or_404
from.forms import UserProfile
from .models import UserProfile


def index(request):
    return render(request, "app/index.html")

def navbar(request):
    return render(request, "app/navbar.html")

def da(request):
    return render(request, "app/da.html")

def create_account(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            return redirect('generate_qr_code', user_id=user_profile.id)
    else:
        form = UserProfileForm()

    return render(request, 'create_account.html', {'form': form})


def generate_qr_code(request, user_id):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    return render(request, 'generate_qr_code.html', {'user_profile': user_profile})
def login(request):
    return render(request,'login.html')
                  