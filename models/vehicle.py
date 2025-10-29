from pydantic import BaseModel, Field


class Vehicle(BaseModel):
    """Vehicle model for BST storage."""
    plate: str = Field(..., description="Vehicle license plate (unique identifier)")
    brand: str = Field(..., description="Vehicle brand")
    color: str = Field(..., description="Vehicle color")
    model: str = Field(..., description="Vehicle model")
    price: float = Field(..., description="Vehicle price")

    class Config:
        json_schema_extra = {
            "example": {
                "plate": "ABC-123",
                "brand": "Toyota",
                "color": "Red",
                "model": "Corolla",
                "price": 25000.00
            }
        }
