from django.shortcuts import render
import nowa
# Create your views here.

def artykuly(request):
    return render('nowa.html',{'nowa': nowa.objects.all()})

def artykul(request, article_id):
    return render('nowa.html',{'nowa': nowa.objects.get(id=article_id)})