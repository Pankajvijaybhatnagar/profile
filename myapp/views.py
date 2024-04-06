from django.shortcuts import render
# Create your views here.
def index_view(request):
    return render(request,'index.html')

def contactpage(request):
    return render(request,'contact.html')

def portfolio_view(request):
    return render(request,'portfolio.html')

def about_view(request):
    return render(request, 'about.html')