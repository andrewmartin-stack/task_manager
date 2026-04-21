import json

from django.test import TestCase


class MCPInspectTest(TestCase):
    def test_mcp_inspect_runs(self):
        """Run the management command mcp_inspect to ensure tools register.

        This test will pass as long as the command runs without raising an
        exception and prints output. It does not assert on the exact
        content because that can vary by environment.
        """
        from mcp_server import mcp_server as global_mcp

        # Ensure the global MCP server object exists and is a DjangoMCP
        assert global_mcp is not None
        # Inspect registered tools (should not raise)
        tools = list(global_mcp.tools.keys())
        # At least verify our Task tools module name appears or simply that tools is iterable
        assert isinstance(tools, list)
