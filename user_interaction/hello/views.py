from django.shortcuts import render, redirect
from .forms import NameForm

# Create your views here.
def greet(request, name):
    return render(request, 'hello/greet.html', {'name':name.capitalize})

def askName(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return redirect('hello:greet', name=name)
    return render(request, 'hello/ask.html', {'form':NameForm})


def tasks(request):
    task = ''
    if request.method == 'POST':
        task = request.POST['task'].capitalize()
        print(task)
    return render(request, 'hello/tasks.html', {'task': task})
