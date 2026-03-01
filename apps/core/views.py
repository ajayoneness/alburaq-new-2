from django.shortcuts import render
from django.utils.translation import get_language
from django.conf import settings
from .models import Office, SocialLink, CompanySettings, HeroSlide, TelegramChannel
from apps.pages.models import Service, Agent
from apps.store.models import Category


def home(request):
    """Homepage view"""
    static_service_slugs = [
        'air-shipping',
        'sea-shipping',
        'land-shipping',
        'sourcing',
        'quality-control',
        'assembly-packing',
        'documentation-customs',
        'how-it-works',
    ]
    context = {
        'hero_slides': HeroSlide.objects.filter(is_active=True),
        'offices': Office.objects.filter(is_active=True),
        'services': Service.objects.filter(is_active=True),
        'extra_services': Service.objects.filter(is_active=True).exclude(slug__in=static_service_slugs)[:8],
        'categories': Category.objects.filter(is_active=True)[:6],
        'social_links': SocialLink.objects.filter(is_active=True),
        'telegram_channels': TelegramChannel.objects.filter(is_active=True),
        'agents': Agent.objects.filter(is_active=True),
    }
    return render(request, 'core/home.html', context)


def set_language(request):
    """Language switching view"""
    from django.http import HttpResponseRedirect
    from django.utils import translation
    
    lang_code = request.GET.get('lang', settings.LANGUAGE_CODE)
    next_url = request.GET.get('next', '/')
    
    response = HttpResponseRedirect(next_url)
    
    if lang_code in [code for code, name in settings.LANGUAGES]:
        if hasattr(request, 'session'):
            request.session['_language'] = lang_code
        
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME,
            lang_code,
            max_age=365 * 24 * 60 * 60,
            httponly=False  # Allow JS access if needed
        )
        translation.activate(lang_code)
    
    return response


def serviceworker(request):
    """Serve the service worker file"""
    response = render(request, 'serviceworker.js')
    response['Content-Type'] = 'application/javascript'
    response['Service-Worker-Allowed'] = '/'
    return response
