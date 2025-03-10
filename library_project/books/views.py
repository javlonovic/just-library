from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, FeedbackForm
from .models import Book, Category, Feedback

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'books/register.html', {'form': form})

@login_required
def home(request):
    # This view is for the home page with school information
    return render(request, 'books/home.html')

@login_required
def library(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    
    if selected_category:
        books = Book.objects.filter(category__name=selected_category).order_by('-created_at')
    else:
        books = Book.objects.all().order_by('-created_at')
        
    context = {
        'categories': categories,
        'books': books,
        'selected_category': selected_category
    }
    
    return render(request, 'books/library.html', context)

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, 'Your feedback has been submitted successfully!')
            return redirect('contact')
    else:
        form = FeedbackForm()
    
    return render(request, 'books/contact.html', {'form': form})