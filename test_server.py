"""Test script for Farm OS MCP server."""

from static_data import FARMS, FIELDS, LIVESTOCK, EQUIPMENT, SENSORS
import json


def print_json(data):
    """Pretty print JSON data."""
    print(json.dumps(data, indent=2))


def main():
    """Test all tools."""
    print("=" * 60)
    print("Farm OS MCP Server - Test Script")
    print("=" * 60)
    
    print("\n1. List all farms:")
    farms_list = [
        {
            "id": farm["id"],
            "name": farm["name"],
            "location": farm["location"],
            "type": farm["type"],
            "area_acres": farm["area_acres"],
        }
        for farm in FARMS.values()
    ]
    print_json(farms_list)
    
    print("\n2. Get farm info (farm_001):")
    farm_id = "farm_001"
    if farm_id in FARMS:
        farm = FARMS[farm_id]
        farm_fields = [f for f in FIELDS.values() if f["farm_id"] == farm_id]
        farm_livestock = [l for l in LIVESTOCK.values() if l["farm_id"] == farm_id]
        farm_equipment = [e for e in EQUIPMENT.values() if e["farm_id"] == farm_id]
        print_json({
            **farm,
            "fields": farm_fields,
            "livestock": farm_livestock,
            "equipment": farm_equipment,
        })
    
    print("\n3. Get farm summary (farm_001):")
    farm_id = "farm_001"
    if farm_id in FARMS:
        farm = FARMS[farm_id]
        fields = [f for f in FIELDS.values() if f["farm_id"] == farm_id]
        livestock = [l for l in LIVESTOCK.values() if l["farm_id"] == farm_id]
        equipment = [e for e in EQUIPMENT.values() if e["farm_id"] == farm_id]
        total_livestock = sum(l["count"] for l in livestock)
        total_field_area = sum(f["area_acres"] for f in fields)
        operational_equipment = sum(1 for e in equipment if e["status"] == "operational")
        print_json({
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
        })
    
    print("\n4. List fields by farm (farm_001):")
    print_json([field for field in FIELDS.values() if field["farm_id"] == "farm_001"])
    
    print("\n5. Get field info (field_001):")
    field_id = "field_001"
    if field_id in FIELDS:
        field = FIELDS[field_id]
        field_sensors = [s for s in SENSORS.values() if s["field_id"] == field_id]
        print_json({**field, "sensors": field_sensors})
    
    print("\n6. Search by crop type (Corn):")
    crop_type = "Corn"
    matching_fields = [
        field for field in FIELDS.values() 
        if field["crop_type"].lower() == crop_type.lower()
    ]
    print_json(matching_fields)
    
    print("\n7. Get sensor readings (field_001):")
    print_json([sensor for sensor in SENSORS.values() if sensor["field_id"] == "field_001"])
    
    print("\n8. List livestock by farm (farm_002):")
    print_json([livestock for livestock in LIVESTOCK.values() if livestock["farm_id"] == "farm_002"])
    
    print("\n9. Get livestock info (livestock_001):")
    print_json(LIVESTOCK.get("livestock_001", {}))
    
    print("\n10. List equipment by farm (farm_001):")
    print_json([equipment for equipment in EQUIPMENT.values() if equipment["farm_id"] == "farm_001"])
    
    print("\n11. Get equipment info (equipment_001):")
    print_json(EQUIPMENT.get("equipment_001", {}))
    
    print("\n12. Test MCP server import:")
    try:
        from farmos_server import mcp
        print("[OK] MCP server imported successfully")
        print(f"[OK] Server name: {mcp.name if hasattr(mcp, 'name') else 'Farm OS Server'}")
        tools_count = len(list(mcp.list_tools())) if hasattr(mcp, 'list_tools') else 'N/A'
        print(f"[OK] Number of tools registered: {tools_count}")
    except Exception as e:
        print(f"[ERROR] Error importing MCP server: {e}")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

