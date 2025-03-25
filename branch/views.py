from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from .models import Branch
from .forms import BranchForm
from django.core.paginator import Paginator
from django.core.cache import cache


@cache_page(60 * 10)
def branch_list(request):
    """ Filiallar ro‘yxatini ko‘rsatish uchun View """
    limit = request.GET.get('limit', 10)
    page_number = request.GET.get('page', 1)

    limit = min(max(int(limit), 1), 100) if str(limit).isdigit() else 10
    page_number = max(int(page_number), 1) if str(page_number).isdigit() else 1

    branches = Branch.objects.all()
    paginator = Paginator(branches, limit)
    page_obj = paginator.get_page(page_number)

    # Success xabarini faqat redirectdan keyin ko‘rsatish
    success_message = None
    if 'success' in request.session and request.method == 'GET' and 'HTTP_REFERER' in request.META:
        success_message = request.session.pop('success')

    form = BranchForm()

    return render(request, 'branch_list.html', {
        'branches': page_obj,
        'form': form,
        'success_message': success_message
    })


@csrf_protect
def branch_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            cache.clear()
            request.session['success'] = "Filial muvaffaqiyatli qo‘shildi!"
            return redirect('branch_list')
    return redirect('branch_list')


@csrf_protect
def branch_edit(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            cache.clear()
            request.session['success'] = "Filial muvaffaqiyatli tahrirlandi!"
            return redirect('branch_list')
    # GET so'rov uchun modalda forma ko'rsatish
    return render(request, 'branch_list.html', {
        'branches': Branch.objects.all(),
        'form': BranchForm(instance=branch),
        'edit_branch': branch
    })


@csrf_protect
def branch_delete(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.method == "POST":
        branch.delete()
        cache.clear()
        request.session['success'] = "Filial muvaffaqiyatli o‘chirildi!"
    return redirect('branch_list')
