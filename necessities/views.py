from django.shortcuts import render, redirect, get_object_or_404
from .models import Necessities
from .forms import NecessitiesForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required
@staff_member_required
def create_necessity(request):
    if request.method == 'POST':
        form = NecessitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_necessities')  # Replace 'necessity_list' with your desired URL
    else:
        form = NecessitiesForm()
    return render(request, 'user/pages/necessities/create.html', {'form': form})


def read_necessity(request, necessity_id):
    necessity = get_object_or_404(Necessities, id=necessity_id)
    return render(request, 'user/pages/necessities/list.html', {'necessity': necessity})


@login_required
@staff_member_required
def update_necessity(request, necessity_id):
    necessity = get_object_or_404(Necessities, id=necessity_id)
    if request.method == 'POST':
        form = NecessitiesForm(request.POST, instance=necessity)
        if form.is_valid():
            form.save()
            return redirect('list_necessities')
    else:
        form = NecessitiesForm(instance=necessity)
    return render(request, 'user/pages/necessities/update.html', {'form': form, 'necessity': necessity})


@login_required
@staff_member_required
def delete_necessity(request, necessity_id):
    necessity = get_object_or_404(Necessities, id=necessity_id)
    if request.method == 'POST':
        necessity.delete()
        return redirect('list_necessities')
    return render(request, 'user/pages/necessities/delete.html', {'necessity': necessity})


def list_necessities(request):
    necessities = Necessities.objects.all()
    return render(request, 'user/pages/necessities/list.html', {'necessities': necessities})
