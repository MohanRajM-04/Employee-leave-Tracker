from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from employee import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.decorators import login_required
from app1.models import Employee, Employee_leave, holiday
from app1.forms import Employee_leave_form, update_emp_details

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = Employee_leave_form()
        leave = Employee_leave.objects.filter(user=user).order_by('id')
        return render(request, 'index.html', context={'form': form,'leave': leave,})

def login(request):

    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {"form": form1}
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {"form": form}
            return render(request, 'login.html', context=context)

def signup(request):
    if request.method == "POST":
        employeename = request.POST['employeename']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Employee.objects.filter(email=email).exists():
                messages.info(request, "Email Id Exists...!!! Try Another...")
                return redirect('signup')

            else:
                user = User.objects.create_user(username=employeename, email=email, password=password2)
                user.save()
               # employee.save()

                # Email Generation Block

                subject = ''
                content = f'Hiii {employeename} Thank you for registering'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email,]
                email = EmailMessage(
                                subject,
                                content,
                                email_from,
                                recipient_list,
                                    )

                email.send()

                messages.info(request, "User Successfully Created")
                return redirect('signup')

        else:
            messages.info(request, "Password Not Match...!!!")
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def apply_leave(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = Employee_leave_form(request.POST)
        if form.is_valid():
            date = request.POST['date']
            # num= request.POST['reason']

            print('********************', date, '*********************')
            from datetime import datetime
            import holidays
            ind_holidays = holidays.India()
            mm=int(date[0:2])
            dd=int(date[3:5])
            yyyy=int(date[-4:])
            x = datetime(yyyy,mm,dd, 00, 00, 00, 0000)
            print('Weekday Number:', x.weekday())
            if x.weekday() == 5 or x.weekday() == 6:
                pass
            elif '%d-%d-%d'%(dd,mm,yyyy) in ind_holidays:
                print('hi buddy')
            else:
                print(form.cleaned_data)
                leave = form.save(commit=False)
                leave.user = user
                leave.save()
                print(leave)
                return redirect("home")
            return redirect("home")

        else:
            return render(request, 'index.html', context={'form': form, })


def delete_leave(request, id):
    print(id)
    Employee_leave.objects.get(pk=id).delete()
    return redirect('home')


@login_required(login_url='login')
def update(request):
    form = update_emp_details()
    if request.method == 'POST':
        form = update_emp_details(request.POST)
        if form.is_valid():
            Employee.user = request.user
            form.save(commit=True)
            return redirect("/")
        else:
            print("Error Form Invalid")
    return render(request, 'update.html', {'form': form})













