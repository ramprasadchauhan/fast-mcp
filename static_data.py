"""Static data for Farm OS testing."""

# Static farm data
FARMS = {
    "farm_001": {
        "id": "farm_001",
        "name": "Green Valley Farm",
        "location": "California, USA",
        "area_acres": 150,
        "owner": "John Smith",
        "established": "2015",
        "type": "mixed",
    },
    "farm_002": {
        "id": "farm_002",
        "name": "Sunset Ranch",
        "location": "Texas, USA",
        "area_acres": 250,
        "owner": "Maria Garcia",
        "established": "2010",
        "type": "livestock",
    },
    "farm_003": {
        "id": "farm_003",
        "name": "Riverbend Organic",
        "location": "Oregon, USA",
        "area_acres": 80,
        "owner": "David Johnson",
        "established": "2018",
        "type": "crop",
    },
}

# Static field data
FIELDS = {
    "field_001": {
        "id": "field_001",
        "farm_id": "farm_001",
        "name": "North Field",
        "area_acres": 50,
        "crop_type": "Corn",
        "planting_date": "2024-04-15",
        "expected_harvest": "2024-09-20",
        "status": "growing",
    },
    "field_002": {
        "id": "field_002",
        "farm_id": "farm_001",
        "name": "South Field",
        "area_acres": 60,
        "crop_type": "Wheat",
        "planting_date": "2024-03-10",
        "expected_harvest": "2024-07-15",
        "status": "growing",
    },
    "field_003": {
        "id": "field_003",
        "farm_id": "farm_002",
        "name": "Pasture A",
        "area_acres": 100,
        "crop_type": "Grass",
        "planting_date": "2023-05-01",
        "expected_harvest": None,
        "status": "active",
    },
    "field_004": {
        "id": "field_004",
        "farm_id": "farm_003",
        "name": "Vegetable Garden",
        "area_acres": 30,
        "crop_type": "Mixed Vegetables",
        "planting_date": "2024-05-01",
        "expected_harvest": "2024-08-30",
        "status": "growing",
    },
}

# Static livestock data
LIVESTOCK = {
    "livestock_001": {
        "id": "livestock_001",
        "farm_id": "farm_002",
        "type": "Cattle",
        "breed": "Angus",
        "count": 120,
        "field_id": "field_003",
        "health_status": "healthy",
        "last_vaccination": "2024-05-15",
    },
    "livestock_002": {
        "id": "livestock_002",
        "farm_id": "farm_002",
        "type": "Sheep",
        "breed": "Dorper",
        "count": 80,
        "field_id": "field_003",
        "health_status": "healthy",
        "last_vaccination": "2024-05-10",
    },
    "livestock_003": {
        "id": "livestock_003",
        "farm_id": "farm_001",
        "type": "Chickens",
        "breed": "Rhode Island Red",
        "count": 200,
        "field_id": None,
        "health_status": "healthy",
        "last_vaccination": "2024-04-20",
    },
}

# Static equipment data
EQUIPMENT = {
    "equipment_001": {
        "id": "equipment_001",
        "farm_id": "farm_001",
        "name": "John Deere Tractor",
        "type": "Tractor",
        "model": "6R 155",
        "year": "2020",
        "status": "operational",
        "last_maintenance": "2024-05-01",
    },
    "equipment_002": {
        "id": "equipment_002",
        "farm_id": "farm_001",
        "name": "Harvester Combine",
        "type": "Harvester",
        "model": "S760",
        "year": "2021",
        "status": "operational",
        "last_maintenance": "2024-04-15",
    },
    "equipment_003": {
        "id": "equipment_003",
        "farm_id": "farm_002",
        "name": "Irrigation System",
        "type": "Irrigation",
        "model": "Center Pivot",
        "year": "2019",
        "status": "maintenance",
        "last_maintenance": "2024-05-10",
    },
}

# Static sensor data
SENSORS = {
    "sensor_001": {
        "id": "sensor_001",
        "field_id": "field_001",
        "farm_id": "farm_001",
        "type": "Soil Moisture",
        "location": "North Field - Center",
        "last_reading": {
            "timestamp": "2024-06-15T10:30:00Z",
            "value": 65.5,
            "unit": "percentage",
        },
    },
    "sensor_002": {
        "id": "sensor_002",
        "field_id": "field_001",
        "farm_id": "farm_001",
        "type": "Temperature",
        "location": "North Field - North End",
        "last_reading": {
            "timestamp": "2024-06-15T10:30:00Z",
            "value": 22.5,
            "unit": "celsius",
        },
    },
    "sensor_003": {
        "id": "sensor_003",
        "field_id": "field_002",
        "farm_id": "farm_001",
        "type": "Humidity",
        "location": "South Field - West",
        "last_reading": {
            "timestamp": "2024-06-15T10:30:00Z",
            "value": 58.3,
            "unit": "percentage",
        },
    },
}

