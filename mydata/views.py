from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def resume(request):
    return render(request,'resume.html')

def logout(request):
    msg = '''Logout successfully
            click login to display resume'''
    return render(request,'login.html',{'msg':msg})