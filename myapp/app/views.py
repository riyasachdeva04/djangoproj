from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
    feature1 = Feature()
    feature1.id  
    return render(request, 'index.html')
    #  name =  "John"
    context = {
        'name' : 'Patrick', 
        'age' : 23,
        'Nationality' : 'British'
    }
    # return render(request, 'index1.html', context)
    return render(request, 'form.html')

# def counter(request):
    words = request.POST['text']
    amountofwords = len(words.split())
    return render(request, 'counter.html',{'amount' : amountofwords} )