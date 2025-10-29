from fastapi import APIRouter, HTTPException, status
from typing import List
from models.vehicle import Vehicle
from core.bst import BinarySearchTree
from services.csv_service import CSVService

router = APIRouter(prefix="/api/vehicles", tags=["vehicles"])

# Initialize BST and CSV service
bst = BinarySearchTree()
csv_service = CSVService()

# Load existing data from CSV on startup
_vehicles = csv_service.load_all()
for vehicle in _vehicles:
    bst.insert(vehicle)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_vehicle(vehicle: Vehicle) -> dict:
    """Create a new vehicle."""
    if bst.search(vehicle.plate):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Vehicle with plate '{vehicle.plate}' already exists"
        )
    
    bst.insert(vehicle)
    csv_service.add_vehicle(vehicle)
    return {"message": "Vehicle created successfully", "vehicle": vehicle}


@router.get("/{plate}")
async def get_vehicle(plate: str) -> dict:
    """Get a vehicle by plate."""
    vehicle = bst.search(plate)
    if not vehicle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with plate '{plate}' not found"
        )
    return {"vehicle": vehicle}


@router.get("/")
async def list_all_vehicles() -> dict:
    """Get all vehicles in inorder traversal."""
    vehicles = bst.inorder()
    return {"count": len(vehicles), "vehicles": vehicles}


@router.put("/{plate}")
async def update_vehicle(plate: str, updated_vehicle: Vehicle) -> dict:
    """Update a vehicle by plate."""
    if not bst.search(plate):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with plate '{plate}' not found"
        )
    
    # Prevent changing the plate (primary key)
    if updated_vehicle.plate != plate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot change vehicle plate"
        )
    
    bst.update(plate, updated_vehicle)
    csv_service.update_vehicle(plate, updated_vehicle)
    return {"message": "Vehicle updated successfully", "vehicle": updated_vehicle}


@router.delete("/{plate}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle(plate: str):
    """Delete a vehicle by plate."""
    if not bst.delete(plate):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with plate '{plate}' not found"
        )
    
    csv_service.remove_vehicle(plate)
    return None


@router.get("/traversal/inorder")
async def get_inorder_traversal() -> dict:
    """Get all vehicles in inorder traversal (sorted by plate)."""
    vehicles = bst.inorder()
    return {"traversal": "inorder", "count": len(vehicles), "vehicles": vehicles}


@router.get("/traversal/preorder")
async def get_preorder_traversal() -> dict:
    """Get all vehicles in preorder traversal."""
    vehicles = bst.preorder()
    return {"traversal": "preorder", "count": len(vehicles), "vehicles": vehicles}


@router.get("/traversal/postorder")
async def get_postorder_traversal() -> dict:
    """Get all vehicles in postorder traversal."""
    vehicles = bst.postorder()
    return {"traversal": "postorder", "count": len(vehicles), "vehicles": vehicles}
