from django.contrib import admin
from django.urls import include, path

# REST API endpoints have been disabled. Interaction should happen via the
# Django admin and the MCP server. Keep API implementation files in place
# (api.py, serializers.py) but do not expose them here.

urlpatterns = [
    path('admin/', admin.site.urls),
    # MCP server integration for OpenClaw. Exposes the MCP endpoint at /mcp
    path("", include('mcp_server.urls')),
]
