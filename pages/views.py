from django.shortcuts import render
from articles.models import Article
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.additional_functions import get_current_quarter, get_last_quarter_dates
from journals.models import Journal
from news.models import New


def home(request):
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

    latest_news = New.objects.all().order_by('-created_at')[:10]

    return render(request, 'user/pages/home.html', {'journals': journals, 'news_obj': latest_news})
