from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    return render(request, 'user/pages/create_article.html', {'form': form})


@login_required
def update_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.user != request.user:
        raise Http404("Bu amalni bajarishga ruxsatingiz yo‘q.")
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'user/pages/update_article.html', {'form': form, 'article': article})


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.user != request.user:
        raise Http404("Bu amalni bajarishga ruxsatingiz yo‘q.")
    if request.method == 'POST':
        article.delete()
        return redirect('list_article')
    return render(request, 'user/pages/delete_article.html', {'article': article})


# Read
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'user/pages/article_detail.html', {'article': article})


# List
def article_list(request):
    query = request.GET.get('q')
    search_year = request.GET.get('search_year')
    search_issue = request.GET.get('search_issue')
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        articles = Article.objects.all()

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
    articles_years = Article.objects.all().values_list('created_at__year')
    articles_months = Article.objects.all().values_list('created_at__year', 'created_at__month')
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
    return render(request, 'user/pages/article_list.html', {'articles': articles, 'issues': issues_years, 'now_year': now_year, "now_issue": now_issue})


# User List
def user_article_list(request):
    articles = Article.objects.filter(user=request.user)
    return render(request, 'user/pages/my_articles.html', {'articles': articles})
