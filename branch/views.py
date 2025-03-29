from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.core.cache import cache
from .models import Branch
from .forms import BranchForm

# @cache_page(60 * 10)
@csrf_protect
@csrf_exempt
def branch_list(request):
    """ Filiallar ro‘yxatini ko‘rsatish uchun View """
    # Limitni dinamik qilish (5, 10, 15)
    limit_options = [5, 10, 15]
    limit = request.GET.get('limit', 10)
    page_number = request.GET.get('page', 1)

    # Limitni tekshirish va standart qiymat
    limit = int(limit) if str(limit).isdigit() and int(limit) in limit_options else 10
    page_number = max(int(page_number), 1) if str(page_number).isdigit() else 1

    # Ma'lumotlarni olish
    branches = Branch.objects.all()
    paginator = Paginator(branches, limit)
    page_obj = paginator.get_page(page_number)

    # Sahifa raqamlari oralig‘ini cheklash (faqat 3 ta ko‘rinadi)
    current_page = page_obj.number
    total_pages = paginator.num_pages
    page_range = range(max(1, current_page - 1), min(total_pages + 1, current_page + 2))

    # Success xabarini faqat redirectdan keyin ko‘rsatish
    success_message = None
    if 'success' in request.session and request.method == 'GET' and 'HTTP_REFERER' in request.META:
        success_message = request.session.pop('success')

    form = BranchForm()

    return render(request, 'branch_list.html', {
        'branches': page_obj,
        'form': form,
        'success_message': success_message,
        'page_range': page_range,  # Cheklangan sahifa oralig‘i
        'limit': limit,           # Joriy limit
        'limit_options': limit_options,  # Tanlash uchun limitlar
    })



@csrf_protect
@csrf_exempt
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
@csrf_exempt
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
@csrf_exempt
def branch_delete(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.method == "POST":
        branch.delete()
        cache.clear()
        request.session['success'] = "Filial muvaffaqiyatli o‘chirildi!"
    return redirect('branch_list')
