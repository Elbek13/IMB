from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator
from django.core.cache import cache
from .models import News
from .forms import NewsForm
from information.views import role_required


def news_list(request):
    """ Yangiliklar ro‘yxatini ko‘rsatish uchun View """
    limit = request.GET.get('limit', 10)
    page_number = request.GET.get('page', 1)

    # Limit va page_number ni xavfsiz tarzda int ga aylantirish
    limit = min(max(int(limit), 1), 100) if str(limit).isdigit() else 10
    page_number = max(int(page_number), 1) if str(page_number).isdigit() else 1

    # Yangi ma'lumotlarni har doim olish
    news_items = News.objects.all().order_by('-created_at')  # Yangidan eskiga tartiblash
    paginator = Paginator(news_items, limit)
    page_obj = paginator.get_page(page_number)

    # Sessiyadan xabarni olish va darhol o‘chirish
    success_message = request.session.get('success')
    if success_message:
        del request.session['success']  # Xabarni o‘chirish

    form = NewsForm()

    return render(request, 'news_list.html', {
        'news_items': page_obj,
        'form': form,
        'success_message': success_message
    })


@csrf_protect
def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cache.clear()  # Keshni tozalash
            request.session['success'] = "Yangilik muvaffaqiyatli qo‘shildi!"
            return redirect('news_list')
        else:
            news_items = News.objects.all().order_by('-created_at')
            paginator = Paginator(news_items, 10)
            page_obj = paginator.get_page(1)
            return render(request, 'news_list.html', {
                'news_items': page_obj,
                'form': form,
                'success_message': None
            })
    return redirect('news_list')


@csrf_protect
def news_edit(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            cache.clear()  # Keshni tozalash
            request.session['success'] = "Yangilik muvaffaqiyatli tahrirlandi!"
            return redirect('news_list')
    return redirect('news_list')


@csrf_protect
def news_delete(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        news.delete()
        cache.clear()  # Keshni tozalash
        request.session['success'] = "Yangilik muvaffaqiyatli o‘chirildi!"
    return redirect('news_list')


@role_required('moderator')
@csrf_exempt
def m_category_list(request):
    return render(request, 'kategoriya/moderator/m_category.html')


def m_news_list(request):
    """ Yangiliklar ro‘yxatini ko‘rsatish uchun View """
    limit = request.GET.get('limit', 10)
    page_number = request.GET.get('page', 1)

    # Limit va page_number ni xavfsiz tarzda int ga aylantirish
    limit = min(max(int(limit), 1), 100) if str(limit).isdigit() else 10
    page_number = max(int(page_number), 1) if str(page_number).isdigit() else 1

    # Yangi ma'lumotlarni har doim olish
    news_items = News.objects.all().order_by('-created_at')  # Yangidan eskiga tartiblash
    paginator = Paginator(news_items, limit)
    page_obj = paginator.get_page(page_number)

    # Sessiyadan xabarni olish va darhol o‘chirish
    success_message = request.session.get('success')
    if success_message:
        del request.session['success']  # Xabarni o‘chirish

    form = NewsForm()

    return render(request, 'm_news_list.html', {
        'news_items': page_obj,
        'form': form,
        'success_message': success_message
    })


@csrf_protect
def m_news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cache.clear()  # Keshni tozalash
            request.session['success'] = "Yangilik muvaffaqiyatli qo‘shildi!"
            return redirect('m_news_list')
        else:
            news_items = News.objects.all().order_by('-created_at')
            paginator = Paginator(news_items, 10)
            page_obj = paginator.get_page(1)
            return render(request, 'm_news_list.html', {
                'news_items': page_obj,
                'form': form,
                'success_message': None
            })
    return redirect('m_news_list')


@csrf_protect
def m_news_edit(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            cache.clear()  # Keshni tozalash
            request.session['success'] = "Yangilik muvaffaqiyatli tahrirlandi!"
            return redirect('m_news_list')
    return redirect('m_news_list')


@csrf_protect
def m_news_delete(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        news.delete()
        cache.clear()  # Keshni tozalash
        request.session['success'] = "Yangilik muvaffaqiyatli o‘chirildi!"
    return redirect('m_news_list')


@csrf_exempt
def more1(request):
    news_items = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_items, 8)  # Har sahifada 8 ta yangilik
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news1.html', {
        'news_items': page_obj,
        'total_news': news_items.count(),  # Umumiy yangiliklar soni
    })


@csrf_exempt
def news1_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    related_news = News.objects.exclude(id=news_id).order_by('-created_at')  # O'xshash yangiliklar
    paginator = Paginator(related_news, 4)  # Har sahifada 4 ta o'xshash yangilik
    page_number = request.GET.get('related_page')  # URL'dan o'xshash yangiliklar sahifasini olish
    related_page_obj = paginator.get_page(page_number)

    return render(request, 'news1_detail.html', {
        'news': news,
        'related_news': related_page_obj,  # Pagination obyektini yuboramiz
    })


@csrf_exempt
def more2(request):
    news_items = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_items, 8)  # Har sahifada 8 ta yangilik
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news2.html', {
        'news_items': page_obj,
        'total_news': news_items.count(),  # Umumiy yangiliklar soni
    })


@csrf_exempt
def news2_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    related_news = News.objects.exclude(id=news_id).order_by('-created_at')  # O'xshash yangiliklar
    paginator = Paginator(related_news, 4)  # Har sahifada 4 ta o'xshash yangilik
    page_number = request.GET.get('related_page')  # URL'dan o'xshash yangiliklar sahifasini olish
    related_page_obj = paginator.get_page(page_number)

    return render(request, 'news2_detail.html', {
        'news': news,
        'related_news': related_page_obj,  # Pagination obyektini yuboramiz
    })


@csrf_exempt
def more3(request):
    news_items = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_items, 8)  # Har sahifada 8 ta yangilik
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news3.html', {
        'news_items': page_obj,
        'total_news': news_items.count(),  # Umumiy yangiliklar soni
    })


@csrf_exempt
def news3_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    related_news = News.objects.exclude(id=news_id).order_by('-created_at')  # Barcha o'xshash yangiliklar
    paginator = Paginator(related_news, 4)  # Har sahifada 4 ta o'xshash yangilik
    page_number = request.GET.get('related_page')  # URL'dan o'xshash yangiliklar sahifasini olish
    related_page_obj = paginator.get_page(page_number)

    return render(request, 'news3_detail.html', {
        'news': news,
        'related_news': related_page_obj,  # Pagination obyektini yuboramiz
    })
