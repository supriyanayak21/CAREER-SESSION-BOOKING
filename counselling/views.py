from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Career, GuidanceSession
from .forms import GuidanceSessionForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CareerSession, CareerCounselor
from .forms import CareerSessionForm

# List all sessions
def session_list(request):
    sessions = CareerSession.objects.all()
    return render(request, 'session_list.html', {'sessions': sessions})

# Counselor can add a session
#@login_required
def add_session(request):
    if request.method == 'POST':
        form = CareerSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.counselor = CareerCounselor.objects.get(user=request.user)
            session.user = request.user
            session.save()
            return redirect('session_list')
    else:
        form = CareerSessionForm()
    return render(request, 'add_session.html', {'form': form})

# View session details
def session_detail(request, session_id):
    session = get_object_or_404(CareerSession, id=session_id)
    return render(request, 'session_detail.html', {'session': session})
def index(request):
    return render(request,'base.html')
@login_required
def career_list(request):
    careers = Career.objects.all()
    return render(request, 'career_list.html', {'careers': careers})

'''@login_required
def book_session(request):
    if request.method == 'POST':
        form = GuidanceSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('career_list')
    else:
        form = GuidanceSessionForm()
    return render(request, 'book_session.html', {'form': form})'''

def book_session(request):
    if request.method == "POST":
        form = GuidanceSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)  # Save form but don't commit yet
            session.user = request.user  # Assign the session to the logged-in user
            session.save()  # Now save to the database
            
            # Send email confirmation
            subject = "Your Career Guidance Session is Booked!"
            message = (
                f"Hello {request.user.username},\n\n"
                f"Your session for {session.career} is successfully booked on {session.session_date}.\n\n"
                "Thank you for using our service!"
            )
            recipient_email = form.cleaned_data['email']  # Use entered email
            #send_mail(subject, message, 'EnterSEnderEmail', [recipient_email])
            return redirect('success_page')  # Redirect to success page

    else:
        form = GuidanceSessionForm()

    return render(request, 'book_session.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")  # Change 'home' to your main page
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})
# Create your views here.
