from django.conf import settings


def vite_context(_request):
    return {
        "VITE_CLIENT_URL": settings.VITE_CLIENT_URL
    }
