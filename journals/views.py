from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from articles.models import Article
from journals.models import Journal, JournalArticle


def index(request):
    return render(request, 'admin/journals/index.html', context={'journals': Journal.objects.all() })

# Function-based view to display details of a single journal
def journal_detail(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    articles = JournalArticle.objects.filter(journal=journal)
    return render(request, 'admin/journals/journal_detail.html', {'journal': journal, 'articles': articles})

# Function-based view to create a new journal
def journal_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file_url = request.FILES.get('file_url')
        journal = Journal(user=request.user, title=title, description=description, file_url=file_url)
        journal.save()
        return redirect('journal_detail', pk=journal.pk)
    return render(request, 'admin/journals/journal_form.html')

# Function-based view to update an existing journal
def journal_update(request, pk):
    journal = get_object_or_404(Journal, pk=pk, user=request.user)
    if request.method == 'POST':
        journal.title = request.POST.get('title')
        journal.description = request.POST.get('description')
        if 'file_url' in request.FILES:
            journal.file_url = request.FILES['file_url']
        journal.save()
        return redirect('journal_detail', pk=journal.pk)
    return render(request, 'admin/journals/journal_form.html', {'journal': journal})

# Function-based view to delete a journal
def journal_delete(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    if request.method == 'POST':
        journal.delete()
        return redirect('journals')
    return redirect('journal_detail', pk=pk)


# Create Article
@login_required
def article_create(request, pk):
    journal = get_object_or_404(Journal, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file_url = request.FILES.get('file_url')

        article = JournalArticle(
            user=request.user,
            title=title,
            description=description,
            file_url=file_url,
            journal=journal
        )
        article.save()
        messages.success(request, 'Article created successfully!')
        return redirect('journal_detail', pk=pk)
    messages.success(request, 'Invalid request!')
    return redirect('journal_detail', pk=pk)

# Update Article
@login_required
def article_update(request, pk):
    article = get_object_or_404(JournalArticle, pk=pk, user=request.user)

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.description = request.POST.get('description')
        if 'file_url' in request.FILES:
            article.file_url = request.FILES['file_url']
        article.save()
        return redirect('journal_detail', pk=article.journal.pk)

    return HttpResponse("Invalid request method", status=400)

# Delete Article
@login_required
def article_delete(request, pk):
    article = get_object_or_404(JournalArticle, pk=pk, user=request.user)

    if request.method == 'POST':
        journal_id = article.journal.pk
        article.delete()
        return redirect('journal_detail', pk=journal_id)

    return HttpResponse("Invalid request method", status=400)