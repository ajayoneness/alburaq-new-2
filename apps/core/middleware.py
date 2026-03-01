from django.utils import translation
from django.conf import settings

class ForceArabicDefaultMiddleware:
    """
    Middleware to force Arabic as the default language if no language preference 
    (cookie or session) is set, overriding the browser's Accept-Language header.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if language cookie is present
        language_cookie = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
        
        # Check if language is set in session
        language_session = request.session.get('_language')
        
        # If no explicit preference is set (no cookie, no session), force Arabic
        if not language_cookie and not language_session:
            translation.activate('ar')
            request.LANGUAGE_CODE = 'ar'
            
        return self.get_response(request)
