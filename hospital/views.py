from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Doctor,Patient,Appointment

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def appointment(request):
    return render(request,'appointment.html')

def dashboard(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    a=Doctor.objects.count()
    b=Patient.objects.count()
    c=Appointment.objects.count()

    return render(request,'index.html',{'num_doctor':a,'num_patient':b,'num_appointment':c})

def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('admin_login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def view_doctor(request):
    if not request.user.is_staff:
        redirect('login')
    doctors=Doctor.objects.all()
    return render(request,'view_doctor.html',{'doctors':doctors})

def view_patient(request):
    if not request.user.is_staff:
        redirect('login')
    patients=Patient.objects.all()
    return render(request,'view_patient.html',{'patients':patients})

def view_appointment(request):
    if not request.user.is_staff:
        redirect('login')
    appointments=Appointment.objects.all()
    return render(request,'view_appointment.html',{'appointments':appointments})

def delete_doctor(request,pk):
    if not request.user.is_staff:
        redirect('login')
    doctor=Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('view_doctor')

def delete_patient(request,pk):
    if not request.user.is_staff:
        redirect('login')
    patient=Patient.objects.get(id=pk)
    patient.delete()
    return redirect('view_patient')

def delete_appointment(request,pk):
    if not request.user.is_staff:
        redirect('login')
    appointment=Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('view_appointment')

def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=='POST':
        name=request.POST['name']
        special=request.POST['special']
        mobile=request.POST['mobile']
        try:
            Doctor.objects.create(name=name,mobile=mobile,special=special)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_doctor.html',d)

def add_patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        mobile=request.POST['mobile']
        age=request.POST['age']
        address=request.POST['address']
        try:
            Patient.objects.create(name=name,gender=gender,mobile=mobile,age=age,address=address)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_patient.html',d)

def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()

    if request.method=='POST':
        d=request.POST['doctor']
        p=request.POST['patient']
        da=request.POST['date']
        t=request.POST['time']
        doctor=Doctor.objects.filter(name=d).first()
        patient=Patient.objects.filter(name=p).first()
        try:
            #doctor=Doctor.objects.get(pk=doctor_id)
            #patient=Patient.objects.get(pk=patient_id)
            Appointment.objects.create(doctor=doctor,patient=patient,date=da,time=t)
            error='no'
        except:
            error='yes'
    d={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)

def look_patient(request):
    patients=Patient.objects.all()
    return render(request, 'patient.html',{'patients':patients})


def update_patient(request,pk):
    if request.user.is_authenticated:
        current_patient= Patient.objects.get(id=pk)
        patients=Patient(request.POST or None,instance=current_patient)
        if patients.is_valid():
            patients.save()
            messages.success(request,"Patient details have been Updated!")
            return redirect('home')
        return render(request,'update_patient.html',{'patients':patients})
    else:
        messages.success(request,'You must be logged in!')
        return redirect('home')