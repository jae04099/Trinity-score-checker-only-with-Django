from django.shortcuts import render, redirect
from .forms import Login

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Login(request.POST)
        form.save()
        return redirect('result')
    
    else:
        form = Login()
        return render(request, 'index.html', {'form': form})

def result(request):
    return render(request, 'result.html')
