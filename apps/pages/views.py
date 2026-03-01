from django.shortcuts import render, get_object_or_404
from .models import (Service, TeamMember, AboutContent, SuccessStory,
                     Agent, AgentTeamMember, Catalog, ImportTip, ShippingCountry, Team)
from apps.core.models import Office, CompanySettings


def about(request):
    """About Us page"""
    context = {
        'about_contents': AboutContent.objects.filter(is_active=True),
        'team_managers': TeamMember.objects.filter(is_active=True, is_manager=True),
        'teams': Team.objects.filter(is_active=True).prefetch_related('members'),
        'offices': Office.objects.filter(is_active=True),
    }
    return render(request, 'pages/about.html', context)


def services(request):
    """Services listing page"""
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
        'services': Service.objects.filter(is_active=True),
        'extra_services': Service.objects.filter(is_active=True).exclude(slug__in=static_service_slugs),
    }
    return render(request, 'pages/services.html', context)


def service_detail(request, slug):
    """Individual service detail page"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    other_services = Service.objects.filter(is_active=True).exclude(pk=service.pk)[:4]
    shipping_countries = ShippingCountry.objects.filter(service=service, is_active=True)
    
    # For Import Tips service, get all tips
    import_tips = None
    if 'import' in slug or 'tips' in slug:
        import_tips = ImportTip.objects.filter(is_active=True)
    
    context = {
        'service': service,
        'other_services': other_services,
        'shipping_countries': shipping_countries,
        'import_tips': import_tips,
    }
    return render(request, 'pages/service_detail.html', context)


def success_stories(request):
    """Success stories page"""
    context = {
        'stories': SuccessStory.objects.filter(is_active=True),
    }
    return render(request, 'pages/success_stories.html', context)


def contact(request):
    """Contact page"""
    context = {
        'offices': Office.objects.filter(is_active=True),
    }
    return render(request, 'pages/contact.html', context)


def become_agent(request):
    """Become an Agent page"""
    settings = CompanySettings.get_settings()
    context = {
        'catalogs': Catalog.objects.filter(is_active=True),
        'whatsapp_number': settings.whatsapp_number,
        'agents': Agent.objects.filter(is_active=True).prefetch_related('team_members'),
    }
    return render(request, 'pages/become_agent.html', context)


def import_tips(request):
    """Import Tips listing page"""
    context = {
        'tips': ImportTip.objects.filter(is_active=True),
    }
    return render(request, 'pages/import_tips.html', context)


def import_tip_detail(request, slug):
    """Individual import tip detail page"""
    tip = get_object_or_404(ImportTip, slug=slug, is_active=True)
    other_tips = ImportTip.objects.filter(is_active=True).exclude(pk=tip.pk)[:3]

    context = {
        'tip': tip,
        'other_tips': other_tips,
    }
    return render(request, 'pages/import_tip_detail.html', context)


# ── Individual Service Pages ──────────────────────────────────────────────────

def service_air_shipping(request):
    return render(request, 'pages/services/air_shipping.html', {})


def service_sea_shipping(request):
    return render(request, 'pages/services/sea_shipping.html', {})


def service_land_shipping(request):
    return render(request, 'pages/services/land_shipping.html', {})


def service_sourcing(request):
    return render(request, 'pages/services/sourcing.html', {})


def service_quality_control(request):
    return render(request, 'pages/services/quality_control.html', {})


def service_assembly_packing(request):
    return render(request, 'pages/services/assembly_packing.html', {})


def service_documentation_customs(request):
    return render(request, 'pages/services/documentation_customs.html', {})


def service_how_it_works(request):
    return render(request, 'pages/services/how_it_works.html', {})
