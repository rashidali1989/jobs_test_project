# Job Creation API

A Django REST Framework API for creating and managing job records with PostgreSQL database support.

## Features

- **Job Creation Endpoint**: Create new jobs with property, products, team members, and contacts
- **Property Reuse**: Automatically reuses existing properties based on address matching
- **PostgreSQL Database**: Robust database backend with proper relationships
- **RESTful API**: Clean REST API with proper serialization

## Environment Setup

The project uses environment variables for configuration. Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

### Environment Variables

```bash
# Database Configuration
DB_CONNECTION=pgsql
DB_HOST=host.docker.internal
DB_PORT=5432
DB_DATABASE=jobs_test_db
DB_USERNAME=your_username
DB_PASSWORD=your_password

# Django Configuration
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Note**: The `.env` file is not committed to version control for security reasons.

## Installation

1. Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your database credentials and settings
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Populate sample data:

```bash
python manage.py populate_sample_data
```

5. Start the development server:

```bash
python manage.py runserver
```

## API Endpoints

### Create Job

**POST** `/api/jobs/`

Creates a new job record with associated property, products, team members, and contacts.

#### Request Body

```json
{
  "type": "Property",
  "status": 1,
  "method_of_access": 1,
  "access_details": "Keysafe: 1992",
  "listing_agent": "3xqv568s",
  "occupant_name": null,
  "occupant_mobile": null,
  "access_other": null,
  "products": ["sd8eas6d2", "a9d83k2m1", "x8d72j1k3"],
  "package": null,
  "property": {
    "unit": null,
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
  "assigned_team_members": ["vx7p3s0d", "fipuhsgb"],
  "contacts": ["wtlc111k", "u93agwnf"],
  "requested_datetime": "2025-08-02T10:00:00Z"
}
```

#### Response

```json
{
  "id": 1,
  "type": "Property",
  "status": 1,
  "method_of_access": 1,
  "access_details": "Keysafe: 1992",
  "listing_agent": "3xqv568s",
  "occupant_name": null,
  "occupant_mobile": null,
  "access_other": null,
  "package": null,
  "requested_datetime": "2025-08-02T10:00:00Z",
  "property_id": 1,
  "product_ids": ["sd8eas6d2", "a9d83k2m1", "x8d72j1k3"],
  "assigned_team_member_ids": ["vx7p3s0d", "fipuhsgb"],
  "contact_ids": ["wtlc111k", "u93agwnf"]
}
```

### List Jobs

**GET** `/api/jobs/`

Returns a list of all jobs with IDs for nested resources.

### Get Job

**GET** `/api/jobs/{id}/`

Returns a specific job with IDs for nested resources.

## Key Features

### Property Reuse

The API automatically checks if a property already exists based on:

- `street_number`
- `street_name`
- `suburb`
- `postcode`

If a matching property is found, it reuses the existing property instead of creating a new one.

### Sample Data

The project includes sample data for testing:

- **Products**: Property Inspection, Photography, Floor Plan
- **Team Members**: John Smith, Jane Doe
- **Contacts**: Bob Wilson, Alice Brown

## Testing

Run the test script to verify the API functionality:

```bash
python test_job_creation.py
```

## Models

### Job

- Job type, status, access method
- Property relationship
- Many-to-many relationships with Products, TeamMembers, and Contacts
- Timestamps for creation and updates

### Property

- Address information (street, suburb, state, postcode)
- Property details (bedrooms, bathrooms, land/house size)
- Unique constraint on address fields

### Product, TeamMember, Contact

- Simple models with ID, name, and contact information
- Used for job associations

## Technologies Used

- **Django 3.1.1**: Web framework
- **Django REST Framework**: API framework
- **PostgreSQL**: Database backend
- **psycopg2-binary**: PostgreSQL adapter
- **python-dotenv**: Environment variable management
