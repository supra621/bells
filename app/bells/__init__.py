"""
This is a Django project that incorporates additional libraries and build
systems. It serves as a reference implementation.

Included are:
- Channels
- Daphne
- Node.js
- SolidJS
- Typescript
- Vite

In dev, I have Vite set up as the static server, with Django `runserver` using
the `--nostatic` option. Django's `STATIC_URL` setting points to the Vite
server host:port. This works, but doesn't resemble how a load balancer or
reverse proxy would fit in the mix.

It does bring about an interesting thought, though. If I remember right, Django
static file requests bypass middleware.
"""

from .celery import app as celery_app

__all__ = ('celery_app',)
