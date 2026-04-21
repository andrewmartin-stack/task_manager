AI Agents & MCP Integration Guide
================================

This document explains how AI agents (e.g. OpenClaw, Claude, any MCP client)
can interact with this Django application via the django-mcp-server package,
how to run and develop locally, and how to test the MCP tools.

Overview
--------
- This Django project exposes an MCP endpoint via the django-mcp-server
  package. The MCP endpoint is mounted through the package's URL inclusion
  and is available at: /mcp (the package default)
- REST API endpoints have been intentionally disabled from project routing.
  Interaction is expected via the Django Admin and the MCP server tools.

Files added / changed
---------------------
- task_manager/mcp.py
  - Implements TaskQueryTool (ModelQueryToolset) and TaskTools (MCPToolset)
    so the Task model is available as MCP tools.
- tests/test_mcp.py
  - Test updated to validate the mcp_server API is importable under Django
    and that the global MCP server object exposes tools.
- TODO.md
  - Project TODOs for future MCP development and security considerations.
- .gitignore updated to ignore virtualenvs (.venv, .venv314, venv, ENV)

Quickstart (local development)
-------------------------------
We used pyenv to install Python 3.14.4 and created a virtualenv (example .venv314).
Follow these steps locally to reproduce the environment used here:

1. Install pyenv and pyenv-virtualenv (macOS Homebrew example):
   - brew install pyenv pyenv-virtualenv

2. Install Python 3.14.x with pyenv:
   - pyenv install 3.14.4

3. Create and activate a virtualenv (example used in this repo):
   - pyenv shell 3.14.4
   - python -m venv .venv314
   - source .venv314/bin/activate

4. Install dependencies:
   - pip install --upgrade pip setuptools wheel
   - pip install -r requirements.txt

5. Apply migrations:
   - python manage.py migrate

6. Run the project or tests:
   - python manage.py runserver 0.0.0.0:8000
   - python manage.py test

Starting/Inspecting the MCP server
----------------------------------
- The django-mcp-server package provides a management command to run the
  global MCP server over different transports. In this repo the available
  management command is:

  - python manage.py stdio_server

  This starts the MCP server attached to STDIO (developer usage, e.g. Claude
  Desktop). The package also exposes programmatic access to the global
  server object via mcp_server.mcp_server (a DjangoMCP instance).

- Note: The third-party package version used here does not expose a management
  command named mcp_inspect, so tests were updated to use the package API
  directly.

How AI agents should connect
----------------------------
- Streamable HTTP endpoint (recommended for remote clients) — the package
  publishes an endpoint at /mcp. Example client usage from the README:

  Use the MCP client to connect to streamable HTTP:

  ```python
  from mcp.client.streamable_http import streamablehttp_client
  from mcp import ClientSession

  async with streamablehttp_client("http://localhost:8000/mcp") as (read_stream, write_stream, _):
      async with ClientSession(read_stream, write_stream) as session:
          await session.initialize()
          result = await session.call_tool("get_alerts", {"state": "NY"})
  ```

- STDIO transport is useful for local agent clients (Claude Desktop); start
  it with `python manage.py stdio_server` and configure the client to use
  manage.py stdio_server as the command for the server.

Security / Authentication
-------------------------
- This repository is configured for local development and does not enable
  authentication for the MCP endpoint. For production or non-local use,
  configure `DJANGO_MCP_AUTHENTICATION_CLASSES` in settings.py and integrate
  an OAuth2 provider (django-oauth-toolkit) as described in the package docs.

MCP tool details (Task model)
-----------------------------
- task_manager/mcp.py provides two tool classes:
  - TaskQueryTool (ModelQueryToolset): exposes querying of Task objects but
    excludes tasks with status='cancelled' by default.
  - TaskTools (MCPToolset): provides a helper method list_titles() that
    returns a list of recent task titles.

Testing notes
-------------
- The tests were updated to import the mcp_server global instance under Django
  and assert tools are discoverable. If you prefer tests that exercise
  network transports, we can add an integration test that starts the stdio
  server and uses a local MCP client.

Developer notes / commands used here
-----------------------------------
- Installed pyenv and pyenv-virtualenv via Homebrew
- Installed Python 3.14.4 via pyenv and created a venv .venv314
- pip install -r requirements.txt installed django-mcp-server and dependencies
- Applied migrations: python manage.py migrate
- Verified `python manage.py stdio_server --version` (returned Django version)
- Updated .gitignore to ignore virtualenvs

TODOs
-----
- Add more MCP tools for other models
- Add integration tests that exercise the STDIO and HTTP transports
- Add authentication configuration for non-local deployments
