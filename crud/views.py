from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def index(request):
    userForm = UserForm()
    return render(request, 'crud/index.html', {'form':userForm})