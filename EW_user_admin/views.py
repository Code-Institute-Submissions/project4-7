from django.shortcuts import render, HttpResponse

# Create your views here.
def user_info (request):
    return render (request, 'user_info.template.html')