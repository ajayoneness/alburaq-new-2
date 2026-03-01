from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError


DEFAULT_SERVICES = [
    {
        "slug": "air-shipping",
        "title": "Air Shipping",
        "short_description": "Fast and reliable air freight services for time-sensitive shipments from China to the world.",
        "full_description": "Fast and reliable air freight for urgent shipments with tracking and customs support.",
        "icon": "fas fa-plane",
        "order": 10,
    },
    {
        "slug": "sea-shipping",
        "title": "Sea Shipping",
        "short_description": "Cost-effective ocean freight solutions for large volume shipments.",
        "full_description": "FCL and LCL ocean freight solutions with booking, documentation, and customs handling.",
        "icon": "fas fa-ship",
        "order": 20,
    },
    {
        "slug": "land-shipping",
        "title": "Land Shipping",
        "short_description": "Rail and road freight connecting China to key regional destinations.",
        "full_description": "Road and rail logistics for regional delivery with border and customs coordination.",
        "icon": "fas fa-train",
        "order": 30,
    },
    {
        "slug": "sourcing",
        "title": "Sourcing & Purchasing",
        "short_description": "Product sourcing from verified Chinese factories and suppliers.",
        "full_description": "Supplier discovery, negotiation, and procurement support to secure quality products.",
        "icon": "fas fa-search-dollar",
        "order": 40,
    },
    {
        "slug": "quality-control",
        "title": "Quality Control",
        "short_description": "Inspection and quality assurance before shipping.",
        "full_description": "Pre-shipment checks and reporting to ensure products meet required standards.",
        "icon": "fas fa-check-circle",
        "order": 50,
    },
    {
        "slug": "assembly-packing",
        "title": "Assembly & Packing",
        "short_description": "Professional assembly, packaging, and consolidation services.",
        "full_description": "Custom packing, branding, and consolidated shipments prepared to your requirements.",
        "icon": "fas fa-box",
        "order": 60,
    },
    {
        "slug": "documentation-customs",
        "title": "Documentation & Customs",
        "short_description": "Complete customs clearance and documentation handling.",
        "full_description": "Import/export documentation and customs workflow management for smooth clearance.",
        "icon": "fas fa-file-alt",
        "order": 70,
    },
    {
        "slug": "how-it-works",
        "title": "How It Works",
        "short_description": "A clear step-by-step process from order to delivery.",
        "full_description": "Transparent logistics workflow so clients understand each step of their shipment journey.",
        "icon": "fas fa-cogs",
        "order": 80,
    },
]


def sync_default_services():
    # Import lazily to avoid app-loading side effects.
    from .models import Service

    lang = getattr(settings, "LANGUAGE_CODE", "en")

    for item in DEFAULT_SERVICES:
        service = Service.objects.filter(slug=item["slug"]).first()
        if service is None:
            service = Service(
                slug=item["slug"],
                icon=item["icon"],
                order=item["order"],
                is_active=True,
            )
            service.save()

        changed = False
        if not service.icon:
            service.icon = item["icon"]
            changed = True
        if service.order is None:
            service.order = item["order"]
            changed = True
        if changed:
            service.save()

        if not service.has_translation(lang):
            service.set_current_language(lang)
            service.title = item["title"]
            service.short_description = item["short_description"]
            service.full_description = item["full_description"]
            service.save()


def sync_default_services_safe(*args, **kwargs):
    try:
        sync_default_services()
    except (OperationalError, ProgrammingError):
        # DB/table might not be ready yet during startup; ignore safely.
        return
