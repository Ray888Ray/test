from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def achievments_view(request):
    return render(request, 'achievments.html')