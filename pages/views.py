from django.shortcuts import render
from articles.models import Article
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.additional_functions import get_current_quarter, get_last_quarter_dates


def home(request):
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
    issues_head = dict(list(issues_years.items())[:2])
    return render(request, 'user/pages/home.html', {'articles': articles, 'issues': issues_years, 'now_year': now_year, "now_issue": now_issue, "query": query, "issues_head": issues_head})
