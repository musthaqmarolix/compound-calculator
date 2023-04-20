from django.shortcuts import render
from django.http import HttpResponse

# def compoundCal(request):
#     data= {
#         'tittle' : 'Compound calculator'
#     }
#     return render(request,"index.html",data)
def compound_interest(principal, time, rate):
    amount = principal * (1 + rate/100) ** time
    ci = amount - principal
    return ci

def index(request):
    interest = None
    if request.method == 'POST':
        principal = float(request.POST.get('principal'))
        time = float(request.POST.get('time'))
        rate = float(request.POST.get('rate'))
        interest = compound_interest(principal, time, rate)
    return render(request, 'index.html',{'interest' : interest})






# return render(request, 'index.html', {'interest': interest})
