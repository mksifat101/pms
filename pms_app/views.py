from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pms_app.models import Category, Company, Developer, Manager, Project


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        if password == rpassword:
            if User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                auth.login(request, user)
                return redirect('home')
                user.save()
                return redirect('login')
        else:
            return redirect('register')
    return render(request, 'auth/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
            url = request.META.get('HTTP_REFERER')
        else:
            return redirect('login')
    return render(request, 'auth/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    company = Company.objects.all().count()
    manager = Manager.objects.all().count()
    developer = Developer.objects.all().count()
    project = Project.objects.all().count()
    context = {
        'company': company,
        'manager': manager,
        'developer': developer,
        'project': project,
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def company(request):
    company = Company.objects.all()
    context = {
        'company': company,
    }
    return render(request, 'company/company.html', context)


@login_required(login_url='login')
def addcompany(request):
    if request.method == "POST":
        name = request.POST['name']
        logo = request.POST['logo']
        information = request.POST['information']
        website = request.POST['website']
        contact = request.POST['contact']
        email = request.POST['email']
        company = Company(name=name, logo=logo, information=information,
                          website=website, contact=contact, email=email)
        company.save()
        return redirect('company')
    return render(request, 'company/addcompany.html')


@login_required(login_url='login')
def manager(request):
    manager = Manager.objects.all()
    context = {
        'manager': manager,
    }
    return render(request, 'manager/manager.html', context)


@login_required(login_url='login')
def addmanager(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        status = request.POST['status']
        manager = Manager(name=name, contact=contact,
                          email=email, status=status)
        manager.save()
        return redirect('manager')
    return render(request, 'manager/addmanager.html')


@login_required(login_url='login')
def developer(request):
    developer = Developer.objects.all()
    context = {
        'developer': developer,
    }
    return render(request, 'developer/developer.html', context)


@login_required(login_url='login')
def adddeveloper(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        status = request.POST['status']
        developer = Developer(name=name, contact=contact,
                              email=email, status=status)
        developer.save()
        return redirect('developer')
    return render(request, 'developer/adddeveloper.html')


@login_required(login_url='login')
def project(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/project.html', context)


@login_required(login_url='login')
def addproject(request):
    company = Company.objects.all()
    category = Category.objects.all()
    manager = Manager.objects.all()
    developer = Developer.objects.all()
    context = {
        'company': company,
        'category': category,
        'manager': manager,
        'developer': developer,
    }
    if request.method == "POST":
        company_id = request.POST['company_id']
        category_id = request.POST['category_id']
        manager_id = request.POST['manager_id']
        description = request.POST['description']
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        project = Project(company_id=company_id, category_id=category_id, manager_id=manager_id,
                          description=description, name=name, start_date=start_date, end_date=end_date)
        project.save()
        return redirect('project')
    return render(request, 'project/addproject.html', context)
