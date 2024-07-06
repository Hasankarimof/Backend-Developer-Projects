from django.shortcuts import render, redirect
from .models import Booking,Menu
from .forms import BookingForm,ContactForm, UserRegistrationForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def booking_view(request):
    if request.method == 'POST':
        print("Form POST request received")
        form = BookingForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('success_page')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ContactForm()
    return render(request, 'contact.html',{'form':form})

def success_view(request):
    return render(request, 'success.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'User.html',{'form': form})

def index(request,name):
    context = {"name":name}
    return HttpResponse(request, 'hello.html',context)


def about(request):
    menu_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, \
                     focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, \
                     Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. \
                      The restaurant has a rustic and relaxed atmosphere with moderate prices, \
                       making it a popular place for a meal any time of the day."}
    return render(request, "about.html", menu_content)


def menu(request):
    newmenu = {
        'pricechart': [
            {'name': 'falafel', 'price': '12'},
            {'name': 'shawarma', 'price': '15'},
            {'name': 'gyro', 'price': '10'},
            {'name': 'hummus', 'price': '5'},
        ]
    }
    return render(request, 'menu.html', newmenu)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request,'menu_card.html', newmenu_dict)


def homee(request):
    return render(request,'homee.html')

def aboutt(request):
    return render(request,'aboutt.html')

def menuu(request):
    return render(request,'menuu.html')