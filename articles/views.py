from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from journals.models import Journal, JournalArticle
from .additional_functions import get_last_quarter_dates
from .models import Article
from .forms import ArticleForm
from collections import defaultdict
from datetime import datetime
import collections
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('home')  # Replace 'home' with your desired URL
    else:
        form = ArticleForm()
    return render(request, 'admin/journals/create_article.html', {'form': form})


@login_required
def update_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.user != request.user or article.status in [1, 2]:
        raise Http404("Bu amalni bajarishga ruxsatingiz yo‘q.")
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('my_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'user/pages/my_update_article.html', {'form': form, 'article': article})


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.user != request.user and article.status in [1, 2]:
        raise Http404("Bu amalni bajarishga ruxsatingiz yo‘q.")
    if request.method == 'POST':
        article.delete()
        return redirect('list_article')
    return render(request, 'user/pages/my_delete_article.html', {'article': article})


# Read
def article_detail(request, article_id):
    query = request.GET.get('q')
    # print(Journal.objects.all())
    print(1)
    article = get_object_or_404(Article, pk=article_id)
    # if request.user != article.user and not (request.user.is_superuser or request.user.is_staff):
    #     article = get_object_or_404(Article, pk=article_id)
    return render(request, 'user/pages/article_detail.html', {'article': article})

def journal_detail(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    articles = JournalArticle.objects.filter(journal=journal)
    return render(request, 'user/pages/journal_detail.html', {'articles': articles, 'journal': journal})


# List
def journal_list(request):
    query = request.GET.get('q')
    search_year = request.GET.get('search_year')
    search_issue = request.GET.get('search_issue')
    last_quarter_start, last_quarter_end = get_last_quarter_dates()
    if query:
        journals = Journal.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).filter(
            created_at__lt=last_quarter_start  # Exclude journals from last quarter
        ).order_by('-created_at')
    else:
        journals = Journal.objects.all()

    if search_year:
        journals = journals.filter(created_at__year=search_year)

    if search_issue:
        quarter_months = {
            '1': [1, 2, 3],
            '2': [4, 5, 6],
            '3': [7, 8, 9],
            '4': [10, 11, 12]
        }
        journals = journals.filter(created_at__month__in=quarter_months[search_issue])
    paginator = Paginator(journals, 14)  # 14 journals per page
    page = request.GET.get('page')
    try:
        journals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        journals = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        journals = paginator.page(paginator.num_pages)
    return render(request, 'user/pages/journal_list.html', {'journals': journals})


@login_required
# User List
def user_article_list(request):
    articles = Article.objects.filter(user=request.user)
    return render(request, 'user/pages/my_articles.html', {'articles': articles})

def search_articles(request):
    query = request.GET.get('q')
    search_year = request.GET.get('search_year')
    search_issue = request.GET.get('search_issue')
    last_quarter_start, last_quarter_end = get_last_quarter_dates()
    if query:
        articles = Article.objects.filter(
            status=1
        ).filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).filter(
            created_at__lt=last_quarter_start  # Exclude articles from last quarter
        ).order_by('-created_at')
    else:
        articles = Article.objects.filter(status=1).all().filter(
            created_at__lt=last_quarter_start  # Exclude articles from last quarter
        ).order_by('-created_at')

    if search_year:
        articles = articles.filter(created_at__year=search_year)

    if search_issue:
        quarter_months = {
            '1': [1, 2, 3],
            '2': [4, 5, 6],
            '3': [7, 8, 9],
            '4': [10, 11, 12]
        }
        articles = articles.filter(created_at__month__in=quarter_months[search_issue])
    paginator = Paginator(articles, 14)  # 14 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    articles_years = Article.objects.filter(status=1).all().filter(
            created_at__lt=last_quarter_start  # Exclude articles from last quarter
        ).values_list('created_at__year')
    articles_months = Article.objects.filter(status=1).all().filter(
            created_at__lt=last_quarter_start  # Exclude articles from last quarter
        ).values_list('created_at__year', 'created_at__month')
    issues_years = {i[0]: set() for i in articles_years}
    for year, month in articles_months:
        if month < 4:
            issues_years[year].add(1)
        elif month < 7:
            issues_years[year].add(2)
        elif month < 10:
            issues_years[year].add(3)
        else:
            issues_years[year].add(4)
    issues_years = dict(sorted(issues_years.items(), reverse=True))
    now_year = datetime.now().year
    now_month = datetime.now().month
    if now_month < 4:
        now_issue = 1
    elif now_month < 7:
        now_issue = 2
    elif now_month < 10:
        now_issue = 3
    else:
        now_issue = 4
    return render(request, 'user/pages/article_list.html', {'articles': articles, 'issues': issues_years, 'now_year': now_year, "now_issue": now_issue, "query": query})
