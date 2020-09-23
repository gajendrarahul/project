from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from owner.models import Owner
from django.db.models import Q
from django.contrib import messages
from owner.form import AddOwner


def Home(request):
    return render(request, 'home.html')

def search(request):
    if request.method == "POST":
        search = request.POST['search']

        if search:
            match = Owner.objects.filter(Q(bike_no__icontains=search) | (Q(owner_name__icontains=search)))
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                messages.error(request, 'No result found ')
                return render(request,'home.html')
        else:
           return render(request,'home.html')

    return render(request,'home.html')
def Form(request):
    return render(request,'addowner.html')

def AddOwner(request):
    if request.method == "POST":
        try:
            name = request.POST['ownername']
            bno = request.POST['bikenumber']
            lno = request.POST['licencenumber']
            bgroup = request.POST['bloodgroup']
            ltpaid = request.POST['lasttaxpaid']
            ownerinfo = Owner(owner_name=name, bike_no=bno,licence_no=lno,blood_group=bgroup,last_tax_paid=ltpaid)
            ownerinfo.is_valid()
            ownerinfo.save()
            return render(request,'home.html')
        except:
            messages.error(request,'Please enter the credential in correct order ')
            return redirect('search')
    else:
        messages.error(request,'no data saved')
        return redirect('search')

