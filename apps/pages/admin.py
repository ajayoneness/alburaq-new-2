from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline
from .models import (Service, TeamMember, AboutContent, SuccessStory,
                     Agent, AgentTeamMember, Catalog, ImportTip, ShippingCountry, Team)


@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display = ['get_title', 'slug', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('slug',)}
    
    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    get_title.short_description = 'Title'


@admin.register(Team)
class TeamAdmin(TranslatableAdmin):
    list_display = ['get_name', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    
    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)
    get_name.short_description = 'Team Name'


@admin.register(TeamMember)
class TeamMemberAdmin(TranslatableAdmin):
    list_display = ['get_name', 'get_position', 'is_manager', 'get_team', 'work_phone', 'order', 'is_active']
    list_editable = ['is_manager', 'order', 'is_active']
    list_filter = ['is_active', 'is_manager', 'team']
    search_fields = ['translations__name', 'work_phone']
    
    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)
    get_name.short_description = 'Name'
    
    def get_position(self, obj):
        return obj.safe_translation_getter('position', any_language=True)
    get_position.short_description = 'Position'
    
    def get_team(self, obj):
        return obj.team.safe_translation_getter('name', any_language=True) if obj.team else '-'
    get_team.short_description = 'Team'


@admin.register(AboutContent)
class AboutContentAdmin(TranslatableAdmin):
    list_display = ['section_type', 'get_title', 'is_active']
    list_editable = ['is_active']
    list_filter = ['section_type', 'is_active']
    
    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    get_title.short_description = 'Title'


@admin.register(SuccessStory)
class SuccessStoryAdmin(TranslatableAdmin):
    list_display = ['get_title', 'get_client', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'created_at']
    
    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    get_title.short_description = 'Title'
    
    def get_client(self, obj):
        return obj.safe_translation_getter('client_name', any_language=True)
    get_client.short_description = 'Client'


class AgentTeamMemberInline(TranslatableTabularInline):
    model = AgentTeamMember
    extra = 1
    fields = ['name', 'position', 'photo', 'order']


@admin.register(Agent)
class AgentAdmin(TranslatableAdmin):
    list_display = ['get_country', 'get_company', 'phone', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    inlines = [AgentTeamMemberInline]
    
    def get_country(self, obj):
        return obj.safe_translation_getter('country_name', any_language=True)
    get_country.short_description = 'Country'
    
    def get_company(self, obj):
        return obj.safe_translation_getter('company_name', any_language=True)
    get_company.short_description = 'Company'


@admin.register(Catalog)
class CatalogAdmin(TranslatableAdmin):
    list_display = ['get_title', 'pdf_file', 'order', 'is_active', 'uploaded_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'uploaded_at']
    
    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    get_title.short_description = 'Title'


@admin.register(ImportTip)
class ImportTipAdmin(TranslatableAdmin):
    list_display = ['get_title', 'slug', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'created_at']
    
    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    get_title.short_description = 'Title'


@admin.register(ShippingCountry)
class ShippingCountryAdmin(TranslatableAdmin):
    list_display = ['get_country', 'service', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['service', 'is_active']
    
    def get_country(self, obj):
        return obj.safe_translation_getter('country_name', any_language=True)
    get_country.short_description = 'Country'
