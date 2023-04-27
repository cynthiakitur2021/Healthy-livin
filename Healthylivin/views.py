from django.shortcuts import render, redirect
from .models import Patient



def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        idnum = request.POST.get('idnum')
        age = request.POST.get('age')
        gender = request.POST.get('gender')


        query = Patient(name=name, email=email, idnum=idnum, age=age, gender=gender, )
        query.save()
        return redirect("/")
def indexpage(request):
    data = Patient.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context)

def deleteData(request, id):
    d = Patient.objects.get(id= id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        idnum = request.POST.get('idnum')
        age = request.POST.get('age')
        gender = request.POST.get('gender')


        edit = Patient.objects.get(id = id)
        edit.name = name
        edit.email = email
        edit.idnum = idnum
        edit.age = age
        edit.gender = gender

        edit.save()

        return  redirect("/")
    d = Patient.objects.get(id=id)
    context = {"d" : d}
    return render(request, "edit.html", context)
