"""Farm OS MCP server using FastMCP."""

from fastmcp import FastMCP
from static_data import FARMS, FIELDS, LIVESTOCK, EQUIPMENT, SENSORS

# Create the MCP server
mcp = FastMCP("Farm OS Server")


@mcp.tool
def get_farm_info(farm_id: str) -> dict:
    """Get information about a specific farm.
    
    Args:
        farm_id: The unique identifier for the farm (e.g., 'farm_001')
    
    Returns:
        Dictionary containing farm information
    """
    if farm_id not in FARMS:
        return {"error": f"Farm with ID '{farm_id}' not found"}
    
    farm = FARMS[farm_id]
    # Get related data
    farm_fields = [f for f in FIELDS.values() if f["farm_id"] == farm_id]
    farm_livestock = [l for l in LIVESTOCK.values() if l["farm_id"] == farm_id]
    farm_equipment = [e for e in EQUIPMENT.values() if e["farm_id"] == farm_id]
    
    return {
        **farm,
        "fields": farm_fields,
        "livestock": farm_livestock,
        "equipment": farm_equipment,
    }


@mcp.tool
def list_all_farms() -> list:
    """List all available farms.
    
    Returns:
        List of all farms with basic information
    """
    return [
        {
            "id": farm["id"],
            "name": farm["name"],
            "location": farm["location"],
            "type": farm["type"],
            "area_acres": farm["area_acres"],
        }
        for farm in FARMS.values()
    ]


@mcp.tool
def get_field_info(field_id: str) -> dict:
    """Get information about a specific field.
    
    Args:
        field_id: The unique identifier for the field (e.g., 'field_001')
    
    Returns:
        Dictionary containing field information
    """
    if field_id not in FIELDS:
        return {"error": f"Field with ID '{field_id}' not found"}
    
    field = FIELDS[field_id]
    # Get related sensor data
    field_sensors = [s for s in SENSORS.values() if s["field_id"] == field_id]
    
    return {
        **field,
        "sensors": field_sensors,
    }


@mcp.tool
def list_fields_by_farm(farm_id: str) -> list:
    """List all fields for a specific farm.
    
    Args:
        farm_id: The unique identifier for the farm
    
    Returns:
        List of fields belonging to the farm
    """
    if farm_id not in FARMS:
        return {"error": f"Farm with ID '{farm_id}' not found"}
    
    return [field for field in FIELDS.values() if field["farm_id"] == farm_id]


@mcp.tool
def get_livestock_info(livestock_id: str) -> dict:
    """Get information about specific livestock.
    
    Args:
        livestock_id: The unique identifier for the livestock group
    
    Returns:
        Dictionary containing livestock information
    """
    if livestock_id not in LIVESTOCK:
        return {"error": f"Livestock with ID '{livestock_id}' not found"}
    
    return LIVESTOCK[livestock_id]


@mcp.tool
def list_livestock_by_farm(farm_id: str) -> list:
    """List all livestock for a specific farm.
    
    Args:
        farm_id: The unique identifier for the farm
    
    Returns:
        List of livestock belonging to the farm
    """
    if farm_id not in FARMS:
        return {"error": f"Farm with ID '{farm_id}' not found"}
    
    return [livestock for livestock in LIVESTOCK.values() if livestock["farm_id"] == farm_id]


@mcp.tool
def get_equipment_info(equipment_id: str) -> dict:
    """Get information about specific equipment.
    
    Args:
        equipment_id: The unique identifier for the equipment
    
    Returns:
        Dictionary containing equipment information
    """
    if equipment_id not in EQUIPMENT:
        return {"error": f"Equipment with ID '{equipment_id}' not found"}
    
    return EQUIPMENT[equipment_id]


@mcp.tool
def list_equipment_by_farm(farm_id: str) -> list:
    """List all equipment for a specific farm.
    
    Args:
        farm_id: The unique identifier for the farm
    
    Returns:
        List of equipment belonging to the farm
    """
    if farm_id not in FARMS:
        return {"error": f"Farm with ID '{farm_id}' not found"}
    
    return [equipment for equipment in EQUIPMENT.values() if equipment["farm_id"] == farm_id]


@mcp.tool
def get_sensor_readings(field_id: str) -> list:
    """Get all sensor readings for a specific field.
    
    Args:
        field_id: The unique identifier for the field
    
    Returns:
        List of sensor readings for the field
    """
    if field_id not in FIELDS:
        return {"error": f"Field with ID '{field_id}' not found"}
    
    return [sensor for sensor in SENSORS.values() if sensor["field_id"] == field_id]


@mcp.tool
def search_by_crop_type(crop_type: str) -> list:
    """Search for fields by crop type.
    
    Args:
        crop_type: The type of crop to search for (e.g., 'Corn', 'Wheat')
    
    Returns:
        List of fields matching the crop type
    """
    matching_fields = [
        field for field in FIELDS.values() 
        if field["crop_type"].lower() == crop_type.lower()
    ]
    return matching_fields


@mcp.tool
def get_farm_summary(farm_id: str) -> dict:
    """Get a comprehensive summary of a farm including all its assets.
    
    Args:
        farm_id: The unique identifier for the farm
    
    Returns:
        Dictionary containing comprehensive farm summary
    """
    if farm_id not in FARMS:
        return {"error": f"Farm with ID '{farm_id}' not found"}
    
    farm = FARMS[farm_id]
    fields = [f for f in FIELDS.values() if f["farm_id"] == farm_id]
    livestock = [l for l in LIVESTOCK.values() if l["farm_id"] == farm_id]
    equipment = [e for e in EQUIPMENT.values() if e["farm_id"] == farm_id]
    
    # Calculate statistics
    total_livestock = sum(l["count"] for l in livestock)
    total_field_area = sum(f["area_acres"] for f in fields)
    operational_equipment = sum(1 for e in equipment if e["status"] == "operational")
    
    return {
        "farm": farm,
        "summary": {
            "total_fields": len(fields),
            "total_field_area_acres": total_field_area,
            "total_livestock_count": total_livestock,
            "total_equipment": len(equipment),
            "operational_equipment": operational_equipment,
        },
        "fields": fields,
        "livestock": livestock,
        "equipment": equipment,
    }


if __name__ == "__main__":
    # Run the server
    mcp.run()

