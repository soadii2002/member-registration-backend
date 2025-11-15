Overview
The Member Registration API allows you to manage member registrations with personal information and CV uploads. Built with Django REST Framework, it provides a simple and robust interface for creating, reading, updating, and deleting member records.
Technology Stack:

Django 5.0
Django REST Framework 3.15.2
SQLite3 Database
drf-yasg (Swagger/OpenAPI)

Repository: https://github.com/saodii2002/member-registration-backend

Base URL
Local Development
http://127.0.0.1:8000
or
http://localhost:8000
API Root
http://localhost:8000/api/members/

Authentication
Currently, the API does not require authentication. All endpoints are publicly accessible.

Note: For production deployment, consider adding authentication using Django REST Framework's authentication classes (Token Authentication, JWT, etc.)


API Endpoints
1. Create Member
Endpoint: POST /api/members/
Description: Register a new member with personal information and CV upload.
Content-Type: multipart/form-data
Request Parameters:
ParameterTypeRequiredDescriptionnamestringYesMember's full namephone_numberstringYesContact phone numbercollegestringYesCollege/University nameemailstringYesEmail address (must be unique)majorstringYesField of study/majorcvfileYesCV file (PDF, DOC, DOCX - Max 10MB)
Success Response: 201 Created
json{
  "id": 1,
  "name": "John Doe",
  "phone_number": "+20123456789",
  "college": "Engineering College",
  "email": "john@example.com",
  "major": "Computer Science",
  "cv": "/media/cvs/cv_20250115.pdf",
  "cv_url": "http://localhost:8000/media/cvs/cv_20250115.pdf",
  "created_at": "2025-01-15T10:30:00Z"
}
Error Response: 400 Bad Request
json{
  "email": ["member with this email already exists."],
  "cv": ["No file was submitted."]
}

2. List All Members
Endpoint: GET /api/members/
Description: Retrieve a list of all registered members.
Success Response: 200 OK
json[
  {
    "id": 1,
    "name": "John Doe",
    "phone_number": "+20123456789",
    "college": "Engineering College",
    "email": "john@example.com",
    "major": "Computer Science",
    "cv": "/media/cvs/cv_20250115.pdf",
    "cv_url": "http://localhost:8000/media/cvs/cv_20250115.pdf",
    "created_at": "2025-01-15T10:30:00Z"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "phone_number": "+20123456790",
    "college": "Science College",
    "email": "jane@example.com",
    "major": "Biology",
    "cv": "/media/cvs/cv_20250115_2.pdf",
    "cv_url": "http://localhost:8000/media/cvs/cv_20250115_2.pdf",
    "created_at": "2025-01-15T11:45:00Z"
  }
]

3. Get Single Member
Endpoint: GET /api/members/{id}/
Description: Retrieve details of a specific member by ID.
URL Parameters:

id (integer) - Member ID

Success Response: 200 OK
json{
  "id": 1,
  "name": "John Doe",
  "phone_number": "+20123456789",
  "college": "Engineering College",
  "email": "john@example.com",
  "major": "Computer Science",
  "cv": "/media/cvs/cv_20250115.pdf",
  "cv_url": "http://localhost:8000/media/cvs/cv_20250115.pdf",
  "created_at": "2025-01-15T10:30:00Z"
}
Error Response: 404 Not Found
json{
  "detail": "Not found."
}

4. Update Member (Full Update)
Endpoint: PUT /api/members/{id}/
Description: Update all fields of a member. All fields are required.
Content-Type: multipart/form-data
URL Parameters:

id (integer) - Member ID

Request Parameters: All fields from Create Member endpoint
Success Response: 200 OK
json{
  "id": 1,
  "name": "John Doe Updated",
  "phone_number": "+20123456789",
  "college": "Engineering College",
  "email": "john.updated@example.com",
  "major": "Computer Science",
  "cv": "/media/cvs/cv_updated.pdf",
  "cv_url": "http://localhost:8000/media/cvs/cv_updated.pdf",
  "created_at": "2025-01-15T10:30:00Z"
}

5. Update Member (Partial Update)
Endpoint: PATCH /api/members/{id}/
Description: Update specific fields of a member. Only changed fields are required.
Content-Type: multipart/form-data
URL Parameters:

id (integer) - Member ID

Request Parameters: Any subset of fields from Create Member endpoint
Success Response: 200 OK

6. Delete Member
Endpoint: DELETE /api/members/{id}/
Description: Delete a member record.
URL Parameters:

id (integer) - Member ID

Success Response: 204 No Content
Error Response: 404 Not Found

Request & Response Examples
Example 1: Create Member (cURL)
bashcurl -X POST http://localhost:8000/api/members/ \
  -F "name=John Doe" \
  -F "phone_number=+20123456789" \
  -F "college=Engineering College" \
  -F "email=john@example.com" \
  -F "major=Computer Science" \
  -F "cv=@/path/to/cv.pdf"
Example 2: Create Member (JavaScript/Fetch)
javascriptconst formData = new FormData();
formData.append('name', 'John Doe');
formData.append('phone_number', '+20123456789');
formData.append('college', 'Engineering College');
formData.append('email', 'john@example.com');
formData.append('major', 'Computer Science');
formData.append('cv', fileInput.files[0]);

const response = await fetch('http://localhost:8000/api/members/', {
  method: 'POST',
  body: formData,
});

const data = await response.json();
console.log(data);
Example 3: Create Member (Python/Requests)
pythonimport requests

url = 'http://localhost:8000/api/members/'
files = {'cv': open('cv.pdf', 'rb')}
data = {
    'name': 'John Doe',
    'phone_number': '+20123456789',
    'college': 'Engineering College',
    'email': 'john@example.com',
    'major': 'Computer Science'
}

response = requests.post(url, data=data, files=files)
print(response.json())
Example 4: Get All Members (JavaScript)
javascriptconst response = await fetch('http://localhost:8000/api/members/');
const members = await response.json();
console.log(members);
Example 5: Get Single Member (cURL)
bashcurl http://localhost:8000/api/members/1/
Example 6: Update Member (JavaScript)
javascriptconst formData = new FormData();
formData.append('name', 'John Updated');

const response = await fetch('http://localhost:8000/api/members/1/', {
  method: 'PATCH',
  body: formData,
});

const data = await response.json();
Example 7: Delete Member (cURL)
bashcurl -X DELETE http://localhost:8000/api/members/1/

Error Handling
HTTP Status Codes
Status CodeDescription200Success (GET, PUT, PATCH)201Created (POST)204No Content (DELETE)400Bad Request - Validation errors404Not Found - Resource doesn't exist500Internal Server Error
Common Validation Errors
Duplicate Email
json{
  "email": ["member with this email already exists."]
}
Missing Required Fields
json{
  "name": ["This field is required."],
  "email": ["This field is required."]
}
Invalid Email Format
json{
  "email": ["Enter a valid email address."]
}
File Too Large
json{
  "cv": ["File size exceeds maximum allowed size."]
}
No File Uploaded
json{
  "cv": ["No file was submitted."]
}

Testing the API
Option 1: Swagger UI (Recommended)

Start the server: python manage.py runserver
Open browser: http://localhost:8000/swagger/
Expand any endpoint
Click "Try it out"
Fill in the form
Click "Execute"
View the response

Option 2: ReDoc

Open: http://localhost:8000/redoc/
Browse through API documentation
View request/response schemas

Option 3: Postman

Open Postman
Create new request
Set method to POST/GET/etc.
URL: http://localhost:8000/api/members/
For POST: Go to Body → form-data
Add all fields
For CV: Change type to "File"
Send request

Option 4: cURL (Command Line)
See examples in Request & Response Examples

Integration Guide
CORS Configuration
The API is configured to accept requests from:

http://localhost:3000
http://127.0.0.1:3000

To add more origins, update CORS_ALLOWED_ORIGINS in project/settings.py:
pythonCORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",  # Vite
    "http://localhost:4200",  # Angular
    "https://your-frontend.com",
]
React Integration Example
jsximport React, { useState, useEffect } from 'react';

function MemberForm() {
  const [formData, setFormData] = useState({
    name: '',
    phone_number: '',
    college: '',
    email: '',
    major: '',
    cv: null
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const data = new FormData();
    Object.keys(formData).forEach(key => {
      data.append(key, formData[key]);
    });

    try {
      const response = await fetch('http://localhost:8000/api/members/', {
        method: 'POST',
        body: data,
      });

      if (response.ok) {
        const result = await response.json();
        console.log('Success:', result);
        alert('Member registered successfully!');
      } else {
        const errors = await response.json();
        console.error('Validation errors:', errors);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };

  const handleFileChange = (e) => {
    setFormData({ ...formData, cv: e.target.files[0] });
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Name"
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
      />
      {/* Add other inputs */}
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

// Fetch members
async function fetchMembers() {
  const response = await fetch('http://localhost:8000/api/members/');
  const members = await response.json();
  return members;
}
Vue.js Integration Example
javascript// Create member
async createMember(formData) {
  const data = new FormData();
  Object.keys(formData).forEach(key => {
    data.append(key, formData[key]);
  });

  try {
    const response = await fetch('http://localhost:8000/api/members/', {
      method: 'POST',
      body: data,
    });
    return await response.json();
  } catch (error) {
    console.error(error);
  }
}

// Get all members
async getMembers() {
  const response = await fetch('http://localhost:8000/api/members/');
  return await response.json();
}

File Upload Specifications
Accepted File Types

PDF (.pdf)
Microsoft Word (.doc, .docx)

File Size Limit

Maximum: 10MB per file

File Storage

Files are stored in: backend/media/cvs/
Access URL pattern: http://localhost:8000/media/cvs/filename.pdf

File Naming

Files are automatically renamed to prevent conflicts
Original filename is preserved in the database


Database Schema
Member Model
FieldTypeConstraintsidIntegerPrimary Key, Auto-incrementnameString(200)Requiredphone_numberString(20)RequiredcollegeString(200)RequiredemailEmailRequired, UniquemajorString(200)RequiredcvFileRequiredcreated_atDateTimeAuto-generated

Admin Panel
Access Admin Panel
URL: http://localhost:8000/admin/
Features

View all members in a table
Search by name, email, college, major
Filter by college and creation date
Download CV files
Add/edit/delete members manually
View creation timestamps

Create Admin User
bashpython manage.py createsuperuser
# Follow prompts to create username and password

Running the Backend
Prerequisites

Python 3.11 or higher
pip (Python package manager)

Setup Instructions

Clone the repository:

bashgit clone https://github.com/saodii2002/member-registration-backend.git
cd member-registration-backend

Create virtual environment:

bashpython -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

Install dependencies:

bashpip install -r requirements.txt

Run migrations:

bashpython manage.py migrate

Create superuser (optional):

bashpython manage.py createsuperuser

Start the server:

bashpython manage.py runserver

Access the API:


API: http://localhost:8000/api/members/
Swagger: http://localhost:8000/swagger/
Admin: http://localhost:8000/admin/


Deployment Notes
Environment Variables (Production)
Create a .env file with:
envDEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=your-database-url
Security Checklist

 Set DEBUG = False
 Configure ALLOWED_HOSTS
 Use environment variables for secrets
 Set up proper database (PostgreSQL recommended)
 Configure file storage (AWS S3, etc.)
 Add authentication to API endpoints
 Enable HTTPS
 Set up proper CORS origins

Recommended Hosting

Backend: Railway.app, Render.com, Heroku
Database: PostgreSQL on the same platform
File Storage: AWS S3, Cloudinary


Support & Contact
Repository: https://github.com/saodii2002/member-registration-backend
Issues: Create an issue on GitHub repository
Email: [Your contact email]

License
[Specify your license here]

Changelog
Version 1.0.0 (2025-01-15)

Initial release
Member CRUD operations
CV file upload
Swagger documentation
Admin panel
CORS support


Last Updated: January 15, 2025
