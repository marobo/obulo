"""
Serve static and media files in production (e.g. Docker with DEBUG=False).
Django's static() only serves when DEBUG=True; these views serve files safely.
"""
import os
from django.conf import settings
from django.http import FileResponse, Http404


def _serve_from_root(request, path, root_setting):
    """Serve a file from a root dir. Path must be relative; no directory traversal."""
    root = os.path.abspath(root_setting)
    path = path.lstrip("/")
    if ".." in path or path.startswith("/"):
        raise Http404("Invalid path")
    file_path = os.path.normpath(os.path.join(root, path))
    file_path = os.path.abspath(file_path)
    if not file_path.startswith(root) or not os.path.isfile(file_path):
        raise Http404("File not found")
    return FileResponse(open(file_path, "rb"), as_attachment=False)


def serve_static(request, path):
    """Serve a file from STATIC_ROOT."""
    return _serve_from_root(request, path, settings.STATIC_ROOT)


def serve_media(request, path):
    """Serve a file from MEDIA_ROOT."""
    return _serve_from_root(request, path, settings.MEDIA_ROOT)
