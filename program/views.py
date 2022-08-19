from django.shortcuts import render
import random

def inputdata(request):
    return render(request, 'program/inputdata.html')

def result(request):
    lis = []
    # lis.append(request.GET['a'])
    # lis.append(request.GET['b'])


    # sum = int(lis[0]) + int(lis[1])
    
    # ans = sum


    num = request.GET['a']
    for i in range(int(num)):
        lotto = random.sample(range(1,46),6)
        lis.append(lotto)
    ans = lis

    



    return render(request, 'program/result.html', {'ans':ans, 'num':num})
    # return render(request, 'program/result.html')

# Create your views here.
