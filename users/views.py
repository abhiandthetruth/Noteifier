from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('notes:home')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
