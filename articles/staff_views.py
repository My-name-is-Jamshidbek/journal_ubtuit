from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
import collections
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Article
from django.urls import reverse


@login_required
@staff_member_required
def accept_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.status = 1
    article.save()

    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))

    return redirect(redirect_to)


@login_required
@staff_member_required
def buying_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.status = 2
    article.save()

    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))

    return redirect(redirect_to)


@login_required
@staff_member_required
def reject_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.status = 3
    article.save()

    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))

    return redirect(redirect_to)


@login_required
@staff_member_required
def loaded_articles(request):
    articles = Article.objects.filter(status=0).order_by('-id')
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

    return render(request, 'user/pages/articles/loaded.html',
                      {'articles': articles})


@login_required
@staff_member_required
def buying_articles(request):
    articles = Article.objects.filter(status=2).order_by('-id')
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

    return render(request, 'user/pages/articles/loaded.html',
                      {'articles': articles})


@login_required
@staff_member_required
def rejected_articles(request):
    articles = Article.objects.filter(status=3).order_by('-id')
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

    return render(request, 'user/pages/articles/loaded.html',
                      {'articles': articles})


@login_required
@staff_member_required
def accepted_articles(request):
    articles = Article.objects.filter(status=1).order_by('-id')
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

    return render(request, 'user/pages/articles/loaded.html',
                      {'articles': articles})
