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
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=test_data, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 201:
            print("✅ Job created successfully!")
            print("Response:")
            print(json.dumps(response.json(), indent=2))
        else:
            print("❌ Job creation failed!")
            print("Error Response:")
            print(json.dumps(response.json(), indent=2))
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the server. Make sure the Django server is running:")
        print("   python manage.py runserver")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Testing Job Creation API...")
    print("=" * 50)
    test_job_creation() 