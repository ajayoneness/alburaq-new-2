from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    # Dedicated DB-driven service detail route to avoid conflicts with static service pages.
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    # Individual service pages (must come before the generic slug pattern)
    path('services/air-shipping/', views.service_air_shipping, name='service_air_shipping'),
    path('services/sea-shipping/', views.service_sea_shipping, name='service_sea_shipping'),
    path('services/land-shipping/', views.service_land_shipping, name='service_land_shipping'),
    path('services/sourcing/', views.service_sourcing, name='service_sourcing'),
    path('services/quality-control/', views.service_quality_control, name='service_quality_control'),
    path('services/assembly-packing/', views.service_assembly_packing, name='service_assembly_packing'),
    path('services/documentation-customs/', views.service_documentation_customs, name='service_documentation_customs'),
    path('services/how-it-works/', views.service_how_it_works, name='service_how_it_works'),
    # Legacy slug-based service detail (kept for backward compatibility)
    path('services/<slug:slug>/', views.service_detail, name='service_detail_legacy'),
    path('success-stories/', views.success_stories, name='success_stories'),
    path('contact/', views.contact, name='contact'),
    path('become-agent/', views.become_agent, name='become_agent'),
    path('import-tips/', views.import_tips, name='import_tips'),
    path('import-tips/<slug:slug>/', views.import_tip_detail, name='import_tip_detail'),
]
