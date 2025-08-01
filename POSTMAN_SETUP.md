# Postman Collection Setup for Job Creation API

## Overview

This Postman collection provides comprehensive testing for your Django job creation API endpoints. The collection includes all CRUD operations, sample data, and error testing scenarios.

## Setup Instructions

### 1. Import the Collection

1. Open Postman
2. Click "Import" button
3. Select the `postman_collection.json` file
4. The collection will be imported with all endpoints and sample data

### 2. Configure Environment Variables

The collection uses the following variables:

- `base_url`: Set to `http://localhost:8000/api` (default)
- `job_id`: Automatically populated when creating jobs

### 3. Start Your Django Server

Before testing, ensure your Django server is running:

```bash
python manage.py runserver
```

## Collection Structure

### 📁 Jobs Folder

Contains the main CRUD operations:

#### **Create Job** (POST)

- **URL**: `{{base_url}}/jobs/`
- **Purpose**: Create a new job/listing
- **Sample Data**: Includes complete property details, products, team members, and contacts
- **Response**: Returns job ID and all associated resource IDs

#### **Get All Jobs** (GET)

- **URL**: `{{base_url}}/jobs/`
- **Purpose**: Retrieve all jobs/listings
- **Response**: List of all jobs with their associated resource IDs

#### **Get Job by ID** (GET)

- **URL**: `{{base_url}}/jobs/{{job_id}}/`
- **Purpose**: Retrieve a specific job by its ID
- **Note**: Requires `job_id` variable to be set

#### **Update Job (Full)** (PUT)

- **URL**: `{{base_url}}/jobs/{{job_id}}/`
- **Purpose**: Completely update a job with new data
- **Note**: Requires `job_id` variable to be set

#### **Update Job (Partial)** (PATCH)

- **URL**: `{{base_url}}/jobs/{{job_id}}/`
- **Purpose**: Partially update specific fields of a job
- **Note**: Requires `job_id` variable to be set

#### **Delete Job** (DELETE)

- **URL**: `{{base_url}}/jobs/{{job_id}}/`
- **Purpose**: Delete a job by its ID
- **Note**: Requires `job_id` variable to be set

### 📁 Sample Data Folder

Contains pre-configured sample jobs for different types:

#### **Create Sample Job - Property**

- Residential property job with keysafe access
- Includes occupant details and basic package

#### **Create Sample Job - Commercial**

- Commercial property job with agent access
- Includes security clearance requirements

#### **Create Sample Job - Industrial**

- Industrial property job with occupant access
- Includes safety requirements (hard hat)

### 📁 Error Testing Folder

Contains test cases for error handling:

#### **Create Job - Invalid Data**

- Tests API response with invalid field values
- Expected: 400 Bad Request with validation errors

#### **Get Non-existent Job**

- Tests 404 response for non-existent job ID
- Expected: 404 Not Found

## Testing Workflow

### 1. Basic CRUD Testing

1. **Create**: Use "Create Job" to create a new job
2. **Read**: Use "Get All Jobs" to see all jobs, or "Get Job by ID" for specific job
3. **Update**: Use "Update Job (Full)" or "Update Job (Partial)" to modify jobs
4. **Delete**: Use "Delete Job" to remove jobs

### 2. Sample Data Testing

1. Run the sample data requests to populate your database with different job types
2. Use "Get All Jobs" to verify the data was created correctly

### 3. Error Testing

1. Run the error test cases to verify proper error handling
2. Check that validation errors are returned appropriately

## Automatic Features

### Auto Job ID Extraction

The collection includes a test script that automatically extracts the job ID from create responses and sets it as a collection variable. This allows subsequent requests (GET, UPDATE, DELETE) to work automatically.

### Response Validation

Each request includes basic response validation:

- Status code validation
- Response structure validation
- Required field presence checks

## API Field Reference

### Job Types

- `Property`: Residential properties
- `Commercial`: Commercial properties
- `Industrial`: Industrial properties

### Status Codes

- `1`: Pending
- `2`: In Progress
- `3`: Completed
- `4`: Cancelled

### Access Methods

- `1`: Keysafe
- `2`: Agent
- `3`: Occupant
- `4`: Other

### Required Fields

- `type`: Job type (Property/Commercial/Industrial)
- `status`: Job status (1-4)
- `method_of_access`: Access method (1-4)
- `listing_agent`: Agent name
- `requested_datetime`: ISO datetime string
- `property`: Property object with required fields

### Property Required Fields

- `street_number`: Street number
- `street_name`: Street name
- `suburb`: Suburb name
- `postcode`: Postcode
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `levels`: Number of levels
- `land_size`: Land size in square meters
- `house_size`: House size in square meters

## Troubleshooting

### Common Issues

1. **Connection Refused**

   - Ensure Django server is running on `localhost:8000`
   - Check if the port is available

2. **404 Not Found**

   - Verify the API endpoint is correct
   - Check if the job ID exists in the database

3. **400 Bad Request**

   - Review the request body for required fields
   - Check data types and validation rules

4. **500 Internal Server Error**
   - Check Django server logs for detailed error messages
   - Verify database connection and migrations

### Debug Tips

1. **Check Response Headers**: Look for content-type and status codes
2. **Review Request Body**: Ensure all required fields are present
3. **Database Verification**: Use Django admin or shell to verify data
4. **Server Logs**: Monitor Django development server output

## Customization

### Adding New Test Cases

1. Duplicate existing requests
2. Modify the request body and URL as needed
3. Update the description and test scripts

### Modifying Base URL

1. Edit the `base_url` collection variable
2. Update all requests will use the new base URL

### Adding Authentication

If you add authentication later:

1. Add authorization headers to requests
2. Update collection variables for tokens
3. Modify test scripts for auth validation

## Support

For issues with the API or collection:

1. Check Django server logs
2. Verify database migrations
3. Test individual endpoints manually
4. Review API documentation and models
