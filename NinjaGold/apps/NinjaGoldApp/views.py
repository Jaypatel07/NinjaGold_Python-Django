from django.shortcuts import render, redirect, HttpResponse
import random
# Create your views here.
def index(request):
    if 'score' not in request.session:
        request.session['score'] = 0
    if 'farm' not in request.session:
        request.session['farm'] = 0
    
    
    return render(request, 'NinjaGoldApp/index.html')
def money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            request.session['score'] += random.randint(10,20)
            return redirect('/')
        if request.POST['building'] == 'house':
            request.session['score'] += random.randint(5,10)
            
        if request.POST['building'] == 'cave':
            request.session['score'] += random.randint(2,5)

        if request.POST['building'] == 'casino':
            request.session['score'] += random.randint(-50,50) 
      
        return redirect('/')
    
def reset(request):
    if request.method == "POST":
        if request.POST['reset'] == 'reset':
            request.session['score'] = 0
            request.session.clear()
            return redirect('/')