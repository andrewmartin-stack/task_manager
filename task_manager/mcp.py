# MCP integration for Task model
# Exposes Task as a ModelQueryToolset so MCP clients (like OpenClaw)
# can query tasks through the MCP endpoint.

from mcp_server import ModelQueryToolset, MCPToolset
from .models import Task


class TaskQueryTool(ModelQueryToolset):
    """Expose the Task model for querying.

    By default this publishes typical query operations for the model. We
    provide a small override of get_queryset to avoid returning cancelled
    tasks to clients by default.
    """

    model = Task

    def get_queryset(self):
        # Filter out cancelled tasks for typical queries
        return super().get_queryset().exclude(status='cancelled')


class TaskTools(MCPToolset):
    """Small collection of utility tools for Task objects."""

    def list_titles(self) -> list:
        """Return a short list of task titles (non-blocking helper)."""
        return list(Task.objects.order_by('-created_at').values_list('title', flat=True)[:50])
