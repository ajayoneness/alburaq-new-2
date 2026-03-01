from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(TranslatableModel):
    """Company services"""
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name="Title"),
        short_description=models.TextField(verbose_name="Short Description"),
        full_description=models.TextField(verbose_name="Full Description", blank=True),
    )
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=100, default='fa-shipping-fast', verbose_name="Icon Class")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Service {self.pk}"

    @property
    def display_title(self):
        return self.safe_translation_getter('title', any_language=True) or ""

    @property
    def display_short_description(self):
        return self.safe_translation_getter('short_description', any_language=True) or ""

    @property
    def display_full_description(self):
        return self.safe_translation_getter('full_description', any_language=True) or ""

    @property
    def display_icon_class(self):
        icon = (self.icon or "").strip()
        if not icon:
            return "fas fa-shipping-fast"
        if icon.startswith(("fas ", "far ", "fab ", "fal ", "fat ", "fa-solid ", "fa-regular ", "fa-brands ")):
            return icon
        if icon.startswith("fa-"):
            return f"fas {icon}"
        return icon


class Team(TranslatableModel):
    """Team/Department for organizing team members"""
    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name="Team Name"),
        description=models.TextField(verbose_name="Team Description", blank=True),
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Team"
        verbose_name_plural = "Teams"
    
    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or f"Team {self.pk}"

    def get_active_members(self):
        return self.members.filter(is_active=True, is_manager=False)


class TeamMember(TranslatableModel):
    """Team members for About page"""
    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name="Name"),
        position=models.CharField(max_length=200, verbose_name="Position"),
        bio=models.TextField(verbose_name="Biography", blank=True),
        short_description=models.CharField(max_length=300, verbose_name="Short Description", blank=True),
    )
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True, verbose_name="Phone Number")
    work_phone = models.CharField(max_length=50, blank=True, verbose_name="Work Phone")
    is_manager = models.BooleanField(default=False, verbose_name="Is Manager/Executive")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members', verbose_name="Team")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
    
    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or f"Member {self.pk}"


class AboutContent(TranslatableModel):
    """About page content sections"""
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name="Section Title"),
        content=models.TextField(verbose_name="Content"),
    )
    section_type = models.CharField(
        max_length=50,
        choices=[
            ('intro', 'Introduction'),
            ('history', 'History'),
            ('vision', 'Vision'),
            ('mission', 'Mission'),
            ('values', 'Values'),
        ],
        unique=True
    )
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "About Content"
        verbose_name_plural = "About Contents"
    
    def __str__(self):
        return self.get_section_type_display()


class SuccessStory(TranslatableModel):
    """Success stories/case studies"""
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name="Title"),
        client_name=models.CharField(max_length=200, verbose_name="Client Name"),
        description=models.TextField(verbose_name="Description"),
    )
    image = models.ImageField(upload_to='success_stories/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Success Story"
        verbose_name_plural = "Success Stories"
    
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Story {self.pk}"


class Agent(TranslatableModel):
    """Alburaq agents/partners around the world"""
    translations = TranslatedFields(
        country_name=models.CharField(max_length=200, verbose_name="Country Name"),
        company_name=models.CharField(max_length=200, verbose_name="Company/Agency Name"),
        main_agent_name=models.CharField(max_length=200, verbose_name="Main Agent Name"),
        main_agent_position=models.CharField(max_length=200, verbose_name="Main Agent Position"),
        address=models.TextField(verbose_name="Address"),
    )
    country_flag = models.ImageField(upload_to='agents/flags/', blank=True, null=True, verbose_name="Country Flag")
    main_agent_photo = models.ImageField(upload_to='agents/photos/', blank=True, null=True, verbose_name="Main Agent Photo")
    phone = models.CharField(max_length=50, verbose_name="Phone Number")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
    
    def __str__(self):
        return self.safe_translation_getter('country_name', any_language=True) or f"Agent {self.pk}"


class AgentTeamMember(TranslatableModel):
    """Team members for each agent"""
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='team_members')
    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name="Name"),
        position=models.CharField(max_length=200, verbose_name="Position/Responsibility"),
    )
    photo = models.ImageField(upload_to='agents/team/', blank=True, null=True, verbose_name="Photo")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Agent Team Member"
        verbose_name_plural = "Agent Team Members"
    
    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or f"Team Member {self.pk}"


class Catalog(TranslatableModel):
    """Product catalogs for download"""
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name="Catalog Title"),
        description=models.TextField(verbose_name="Description", blank=True),
    )
    pdf_file = models.FileField(upload_to='catalogs/', verbose_name="PDF File")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"
    
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Catalog {self.pk}"


class ImportTip(TranslatableModel):
    """Import tips and experiences blog posts"""
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name="Title"),
        content=models.TextField(verbose_name="Content"),
    )
    slug = models.SlugField(unique=True, verbose_name="URL Slug")
    image = models.ImageField(upload_to='import_tips/', blank=True, null=True, verbose_name="Featured Image")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Import Tip"
        verbose_name_plural = "Import Tips"
    
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Tip {self.pk}"


class ShippingCountry(TranslatableModel):
    """Country-specific shipping information for services"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='shipping_countries')
    translations = TranslatedFields(
        country_name=models.CharField(max_length=200, verbose_name="Country Name"),
        shipping_details=models.TextField(verbose_name="Shipping Details (prices, duration, etc.)"),
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Shipping Country"
        verbose_name_plural = "Shipping Countries"
    
    def __str__(self):
        return f"{self.safe_translation_getter('country_name', any_language=True)} - {self.service}"

    @property
    def display_country_name(self):
        return self.safe_translation_getter('country_name', any_language=True) or ""

    @property
    def display_shipping_details(self):
        return self.safe_translation_getter('shipping_details', any_language=True) or ""
