from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import New

def staff_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_staff)(view_func))
    return decorated_view_func

def news_list(request):
    news_items = New.objects.all().order_by('-created_at')
    paginator = Paginator(news_items, 10)  # Show 10 news items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/news_list.html', {'page_obj': page_obj})

def news_detail(request, pk):
    news_item = get_object_or_404(New, pk=pk)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

@staff_required
def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')  # Capture Subtitle
        description = request.POST.get('description')

        if title and description:
            new = New.objects.create(
                title=title,
                subtitle=subtitle,  # Save Subtitle
                description=description,
                creator=request.user
            )
            messages.success(request, 'News item created successfully!')
            return redirect('news_list')
        else:
            messages.error(request, 'Please provide both title and description.')

    return render(request, 'news/create_news.html')

@staff_required
def update_news(request, pk):
    news_item = get_object_or_404(New, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')  # Capture Subtitle
        description = request.POST.get('description')

        if title and description:
            news_item.title = title
            news_item.subtitle = subtitle  # Update Subtitle
            news_item.description = description
            news_item.save()
            messages.success(request, 'News item updated successfully!')
            return redirect('news_list')
        else:
            messages.error(request, 'Please provide both title and description.')

    return render(request, 'news/update_news.html', {'news_item': news_item})

@staff_required
def delete_news(request, pk):
    news_item = get_object_or_404(New, pk=pk)

    if request.method == 'POST':
        news_item.delete()
        messages.success(request, 'News item deleted successfully!')
        return redirect('news_list')

    # No need for a separate delete confirmation page
    # Confirmation handled via modal
    return redirect('news_list')