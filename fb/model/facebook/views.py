from django.shortcuts import render
from fb.models import login


def login1(request):
    if request.method == 'POST':
        usernsam = request.POST['user']
        password = request.POST['password']
        x = login(name=usernsam, password=password)
        x.save()
        return render(request, 'fb.html')
    else:
        return render(request, 'fb.html')
