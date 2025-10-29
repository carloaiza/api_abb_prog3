from typing import Optional
from models.vehicle import Vehicle


class BSTNode:
    """Binary Search Tree Node for storing vehicles."""

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    def __repr__(self) -> str:
        return f"BSTNode(plate={self.vehicle.plate})"
