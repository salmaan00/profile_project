from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import*
from .models import*
from django.middleware.csrf import get_token

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after signup
            return redirect('profile', username=user.username)  # Redirect to profile with username
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                print(f"Redirecting to profile with username: {user.username}")
                return redirect('profile', username=user.username)
            else:
                print( "User authentication failed.")
                # Optionally add a message to inform the user of authentication failure
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        print(f"Redirecting to profile with username: {request.user.username}")
        return redirect('profile', username=request.user.username)
    else:
        return render(request, 'home.html')



@login_required
def home_view(request):
    user_profile = None
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None
    return render(request, 'home.html', {'user_profile': user_profile})

# Combined view
def combined_home(request):
    if request.user.is_authenticated:
        username = request.user.username
        print(f"Redirecting to profile with username: {username}")
        
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None
        
        return render(request, 'home.html', {
            'user_profile': user_profile,
            'username': username
        })
    else:
        return render(request, 'home.html')


@login_required
def edit_profile(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        # Handle form submission
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=user.username)
    else:
        form =UserProfileForm(instance=user_profile)
    return render(request, 'profiles/edit_profile.html', {'form': form, 'user_profile': user_profile})

@login_required
def edit_portfolio(request):
    portfolio = Portfolio.objects.get_or_create(user=request.user)[0]
    
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = PortfolioForm(instance=portfolio)
    
    return render(request, 'profiles/edit_portfolio.html', {'form': form})

@login_required
def add_project(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()
            return redirect('user_projects', username=request.user.username)  # Redirect to user projects
    else:
        form = ProjectForm()
    
    return render(request, 'profiles/add_project.html', {'form': form})



def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    portfolio = Portfolio.objects.filter(user=user).first()
    projects = Project.objects.filter(portfolio=portfolio) if portfolio else []

    # Debug print statements
    print(f"Viewing profile of user: {user.username}")
    print(f"Portfolio: {portfolio}")
    print(f"Projects: {projects}")

    return render(request, 'profiles/view_profile.html', {
        'user_profile': user_profile,
        'portfolio': portfolio,
        'projects': projects,
    })



def portfolio_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    portfolio = Portfolio.objects.filter(user=user).first()
    
    if not portfolio:
        # Handle the case where the portfolio does not exist
        return render(request, 'profiles/portfolio_not_found.html', {'user': user})
        
    
    print(f"User: {user}, Portfolio: {portfolio}")  # Debug print
    return render(request, 'profiles/portfolio.html', {'portfolio': portfolio, 'user': user})

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    portfolio = get_object_or_404(Portfolio, id=project.portfolio.id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio', args=[request.user.id]))
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'profiles/edit_project.html', {
        'form': form,
        'project': project,
    })


    # delete

@login_required
def delete_user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Assuming you have implemented logic to cascade delete related objects
    user_profile.delete()
    return redirect('home')  # Redirect to appropriate page after deletion

@login_required
def delete_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id, user=request.user)
    # Delete related projects (assuming cascade delete is implemented)
    portfolio.delete()
    return redirect('home')  # Redirect to appropriate page after deletion

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    portfolio_id = project.portfolio.id  # Save portfolio ID before deletion
    project.delete()
    return redirect('portfolio', user_id=request.user.id)  # Redirect to portfolio page after deletion

@login_required
def user_projects_view(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    
    try:
        portfolio = Portfolio.objects.get(user=user)
        projects = Project.objects.filter(portfolio=portfolio)
    except Portfolio.DoesNotExist:
        portfolio = None
        projects = []

    return render(request, 'profiles/user_projects.html', {
        'user_profile': user_profile,
        'portfolio': portfolio,
        'projects': projects,
    })


def custom_logout(request):
    logout(request)
    return redirect('index')


def login_view(request):
    # Example code to fetch user profile
    user_profile = UserProfile.objects.get(user=request.user) if request.user.is_authenticated else None
    print(f"CSRF Token: {get_token(request)}")  # Debug print for CSRF token
    return render(request, 'login.html', {'user_profile': user_profile})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm  # Make sure you are using the correct form

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


def index_view(request):
    return render(request, 'index/index.html')

def some_other_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect(reverse('user_projects', kwargs={'username': username}))
    else:
        return redirect('login')

