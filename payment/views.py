from django.shortcuts import render

# Create your views here.


def goOffers(request):
    return render(request,'offers.html')


def goChoose_offer(request,amount):
    print(amount)
    # return render(request,'posts.html')




# def goCharge(request):
#     print(mount)