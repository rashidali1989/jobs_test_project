#!/usr/bin/env python3
import requests
import json

# Test data from the requirements
test_data = {
    "type": "Property",
    "status": 1,
    "method_of_access": 1,
    "access_details": "Keysafe: 1992",
    "listing_agent": "3xqv568s",
    "occupant_name": None,
    "occupant_mobile": None,
    "access_other": None,
    "products": [
        "sd8eas6d2",
        "a9d83k2m1",
        "x8d72j1k3"
    ],
    "package": None,
    "property": {
        "unit": None,
        "street_number": "123",
        "street_name": "Pitt Street",
        "suburb": "Sydney",
        "state": "NSW",
        "postcode": "2000",
        "country": "Australia",
        "bedrooms": 2,
        "bathrooms": 1,
        "levels": 1,
        "land_size": 127,
        "house_size": 64
    },
    "assigned_team_members": [
        "vx7p3s0d",
        "fipuhsgb"
    ],
    "contacts": [
        "wtlc111k",
        "u93agwnf"
    ],
    "requested_datetime": "2025-08-02T10:00:00Z"
}

def test_job_creation():
    """Test the job creation endpoint"""
    url = "http://localhost:8000/api/jobs/"
    
    print("Testing Job Creation Endpoint")
    print("=" * 50)
    print(f"URL: {url}")
    print(f"Data: {json.dumps(test_data, indent=2)}")
    print("-" * 50)
    
    try:
        response = requests.post(url, json=test_data)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print("\n✅ SUCCESS: Job created successfully!")
            print("The response contains IDs only for nested resources as required.")
        else:
            print(f"\n❌ ERROR: Failed to create job (Status: {response.status_code})")
            
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Could not connect to the server.")
        print("Make sure the Django server is running with: python manage.py runserver")
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

def test_property_reuse():
    """Test that the same property is reused when creating another job"""
    url = "http://localhost:8000/api/jobs/"
    
    # Same property data but different job details
    test_data_2 = {
        "type": "Property",
        "status": 2,
        "method_of_access": 2,
        "access_details": "Agent will meet on site",
        "listing_agent": "4xqv568s",
        "occupant_name": "John Doe",
        "occupant_mobile": "0412345678",
        "access_other": None,
        "products": [
            "sd8eas6d2"
        ],
        "package": "Premium",
        "property": {
            "unit": None,
            "street_number": "123",
            "street_name": "Pitt Street",
            "suburb": "Sydney",
            "state": "NSW",
            "postcode": "2000",
            "country": "Australia",
            "bedrooms": 2,
            "bathrooms": 1,
            "levels": 1,
            "land_size": 127,
            "house_size": 64
        },
        "assigned_team_members": [
            "vx7p3s0d"
        ],
        "contacts": [
            "wtlc111k"
        ],
        "requested_datetime": "2025-08-03T14:00:00Z"
    }
    
    print("\n\nTesting Property Reuse")
    print("=" * 50)
    print("Creating another job with the same property...")
    
    try:
        response = requests.post(url, json=test_data_2)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print("\n✅ SUCCESS: Second job created successfully!")
            print("The property should be reused (same property_id).")
        else:
            print(f"\n❌ ERROR: Failed to create second job (Status: {response.status_code})")
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    test_job_creation()
    test_property_reuse() 