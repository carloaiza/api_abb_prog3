# Vehicle BST API

A FastAPI-based REST API that implements a Binary Search Tree (BST) for managing vehicle data.

## Features

- **Binary Search Tree Implementation**: Efficient vehicle storage and retrieval using plate as the key
- **CRUD Operations**: Create, Read, Update, Delete vehicles
- **Tree Traversals**: Inorder, Preorder, and Postorder traversals
- **Persistent Storage**: CSV-based data persistence
- **Pydantic Models**: Type-safe data validation
- **FastAPI**: Modern, fast web framework with automatic API documentation

## Project Structure

```
api_abb_prog3/
├── models/
│   ├── __init__.py
│   └── vehicle.py          # Vehicle Pydantic model
├── core/
│   ├── __init__.py
│   ├── bst.py              # Binary Search Tree implementation
│   └── bst_node.py         # BST Node class
├── services/
│   ├── __init__.py
│   └── csv_service.py      # CSV persistence service
├── controllers/
│   ├── __init__.py
│   └── vehicle_controller.py # API routes (MVC Controller)
├── data/
│   └── vehicles.csv        # Vehicle data storage
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── test_main.http          # API test requests
└── README.md              # This file
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Vehicle Management

- **POST** `/api/vehicles/` - Create a new vehicle
- **GET** `/api/vehicles/` - Get all vehicles (inorder traversal)
- **GET** `/api/vehicles/{plate}` - Get a specific vehicle by plate
- **PUT** `/api/vehicles/{plate}` - Update a vehicle
- **DELETE** `/api/vehicles/{plate}` - Delete a vehicle

### Tree Traversals

- **GET** `/api/vehicles/traversal/inorder` - Get vehicles in inorder traversal (sorted by plate)
- **GET** `/api/vehicles/traversal/preorder` - Get vehicles in preorder traversal
- **GET** `/api/vehicles/traversal/postorder` - Get vehicles in postorder traversal

## Vehicle Model

```json
{
  "plate": "ABC-123",
  "brand": "Toyota",
  "color": "Red",
  "model": "Corolla",
  "price": 25000.00
}
```

### Fields:
- **plate** (string, required): Vehicle license plate (unique identifier)
- **brand** (string, required): Vehicle brand/manufacturer
- **color** (string, required): Vehicle color
- **model** (string, required): Vehicle model
- **price** (float, required): Vehicle price

## Testing

Use the provided `test_main.http` file to test all endpoints. You can run these requests using:
- VS Code REST Client extension
- Postman
- curl commands

Example with curl:
```bash
# Create a vehicle
curl -X POST "http://127.0.0.1:8000/api/vehicles/" \
  -H "Content-Type: application/json" \
  -d '{
    "plate": "ABC-123",
    "brand": "Toyota",
    "color": "Red",
    "model": "Corolla",
    "price": 25000.00
  }'

# Get all vehicles
curl "http://127.0.0.1:8000/api/vehicles/"

# Get specific vehicle
curl "http://127.0.0.1:8000/api/vehicles/ABC-123"

# Update vehicle
curl -X PUT "http://127.0.0.1:8000/api/vehicles/ABC-123" \
  -H "Content-Type: application/json" \
  -d '{
    "plate": "ABC-123",
    "brand": "Toyota",
    "color": "White",
    "model": "Corolla",
    "price": 26000.00
  }'

# Delete vehicle
curl -X DELETE "http://127.0.0.1:8000/api/vehicles/ABC-123"

# Get inorder traversal
curl "http://127.0.0.1:8000/api/vehicles/traversal/inorder"
```

## Data Persistence

Vehicle data is automatically persisted to `data/vehicles.csv`. The file is created automatically on first run.

## Architecture

### MVC Pattern
- **Model**: `models/vehicle.py` - Pydantic Vehicle model
- **View**: FastAPI automatic documentation and JSON responses
- **Controller**: `controllers/vehicle_controller.py` - API route handlers

### Core Components
- **BST**: `core/bst.py` - Binary Search Tree with all operations
- **BST Node**: `core/bst_node.py` - Individual tree node
- **CSV Service**: `services/csv_service.py` - Data persistence layer

## Best Practices Implemented

✅ MVC architecture pattern
✅ Type hints throughout the codebase
✅ Pydantic models for validation
✅ Proper HTTP status codes
✅ Error handling with meaningful messages
✅ CSV persistence
✅ CORS middleware enabled
✅ English naming conventions
✅ Modular project structure
✅ Comprehensive API documentation
