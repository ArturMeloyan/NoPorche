
import random
from django.shortcuts import render



def generator(request):
    return render (request,'generator/generator.html' )


def about(request):
    return render (request,'generator/about.html' )




def password(request): 
    alp=list('qwertyuiopasdfghjklzxcvbnm')
    upp=list('QWERTYUIOPASDFGHJKLZXCVBNM')
    chrr=list('!@#$%&*')
    num=list('1234567890')

    lenght_password = int(request.GET.get("lenght"))


    thepassword = ''

    if request.GET.get('uppercase'):
        alp=alp+upp
    if request.GET.get('number'):
        alp=alp+num
    if request.GET.get('character'):
        alp=alp+chrr

    for i in range(lenght_password):
        thepassword += random.choice(alp)

    context = {"thepassword":thepassword}

    return render (request,'generator/password.html',context)


