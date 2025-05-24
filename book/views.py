from django.core.mail import message
from django.shortcuts import render, redirect
from .forms import AddBook, AddCat


# Create your views here.

def home(request):
    return render(request, "index.html")

def con(request):
    return render(request, "contact.html")

def Book(request):
    forms=AddBook()
    if request.method=="POST":
        forms=AddBook(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            message.succes(request,"Kitob Muvaffaqiyatli qo'shildi!")
            return redirect("saxifa")
    context={
        "forms":forms
    }
    return render(request,"add_book.html",context)

def Category(request):
    forms=AddCat()
    if request.method=="POST":
        forms=AddCat(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            message.succes(request,"Kitob Muvaffaqiyatli qo'shildi!")
            return redirect("saxifa")
    context={
        "forms":forms
    }
    return render(request,"add_cat.html",context)
