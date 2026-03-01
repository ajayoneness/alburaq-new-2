from django.shortcuts import render
from django.db.models import Prefetch
from .models import FAQCategory, FAQ


def faq_list(request):
    """FAQ listing page with accordion"""
    active_faqs = FAQ.objects.filter(is_active=True).select_related('category').order_by('order')
    categories = FAQCategory.objects.filter(faqs__is_active=True).distinct().order_by('order').prefetch_related(
        Prefetch('faqs', queryset=active_faqs, to_attr='active_faqs')
    )
    uncategorized_faqs = active_faqs.filter(category__isnull=True)

    context = {
        'categories': categories,
        'uncategorized_faqs': uncategorized_faqs,
        'faqs': active_faqs,
    }
    return render(request, 'faq/faq_list.html', context)
