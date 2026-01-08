# Farm OS MCP Server

A Model Context Protocol (MCP) server for Farm OS using FastMCP, built with Python and managed with `uv`.

## Features

This MCP server provides tools for managing farm data including:
- Farm information and summaries
- Field management and crop tracking
- Livestock monitoring
- Equipment tracking
- Sensor readings

All data is currently static for testing purposes.

## Setup

### Prerequisites

- Python 3.10 or higher
- `uv` package manager (install from https://docs.astral.sh/uv/)

### Installation

1. Install `uv` (if not already installed):

   **Windows (PowerShell):**
   ```powershell
   irm https://astral.sh/uv/install.ps1 | iex
   ```

   **macOS/Linux:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Sync dependencies:
   ```bash
   uv sync
   ```

3. Install the project:
   ```bash
   uv pip install -e .
   ```

## Usage

### Run the MCP Server

```bash
uv run python farmos_server.py
```

### Test the Tools

Run the test script to see all available tools in action:

```bash
uv run python test_server.py
```

## Available Tools

- `get_farm_info(farm_id)` - Get detailed information about a specific farm
- `list_all_farms()` - List all available farms
- `get_field_info(field_id)` - Get information about a specific field
- `list_fields_by_farm(farm_id)` - List all fields for a farm
- `get_livestock_info(livestock_id)` - Get information about livestock
- `list_livestock_by_farm(farm_id)` - List all livestock for a farm
- `get_equipment_info(equipment_id)` - Get information about equipment
- `list_equipment_by_farm(farm_id)` - List all equipment for a farm
- `get_sensor_readings(field_id)` - Get sensor readings for a field
- `search_by_crop_type(crop_type)` - Search fields by crop type
- `get_farm_summary(farm_id)` - Get comprehensive farm summary with statistics

## Project Structure

```
fastmcp/
├── farmos_server.py    # Main MCP server with all tools
├── static_data.py      # Static test data
├── test_server.py      # Test script
├── pyproject.toml      # Project configuration
└── setup.py            # Setup helper script
```

## Static Test Data

The project includes static test data for:
- 3 farms
- 4 fields
- 3 livestock groups
- 3 equipment items
- 3 sensor devices

All data is defined in `static_data.py` and can be modified for testing purposes.

