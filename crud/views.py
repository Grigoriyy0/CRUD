from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    if request.method == 'POST':
        name = request.get('name')
        age = request.get('age')
        return HttpResponse(f'<h2> Привет, {name}, твой возраст: {age} </h2>')
    else:
        userform = UserForm()
        return render(request, 'crud/index.html', {'form':userform})