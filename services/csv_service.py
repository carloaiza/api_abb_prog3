import csv
import os
from typing import List
from models.vehicle import Vehicle


class CSVService:
    """Service for managing vehicle data in CSV format."""

    def __init__(self, filepath: str = "data/vehicles.csv"):
        self.filepath = filepath
        self._ensure_directory()
        self._ensure_file()

    def _ensure_directory(self) -> None:
        """Ensure the data directory exists."""
        directory = os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def _ensure_file(self) -> None:
        """Ensure the CSV file exists with headers."""
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['plate', 'brand', 'color', 'model', 'price'])
                writer.writeheader()

    def save_all(self, vehicles: List[Vehicle]) -> None:
        """Save all vehicles to CSV file."""
        with open(self.filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['plate', 'brand', 'color', 'model', 'price'])
            writer.writeheader()
            for vehicle in vehicles:
                writer.writerow(vehicle.model_dump())

    def load_all(self) -> List[Vehicle]:
        """Load all vehicles from CSV file."""
        vehicles = []
        if not os.path.exists(self.filepath):
            return vehicles

        with open(self.filepath, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:
                    try:
                        vehicle = Vehicle(
                            plate=row['plate'],
                            brand=row['brand'],
                            color=row['color'],
                            model=row['model'],
                            price=float(row['price'])
                        )
                        vehicles.append(vehicle)
                    except (KeyError, ValueError):
                        continue
        return vehicles

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a single vehicle to CSV file."""
        with open(self.filepath, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['plate', 'brand', 'color', 'model', 'price'])
            writer.writerow(vehicle.model_dump())

    def remove_vehicle(self, plate: str) -> None:
        """Remove a vehicle from CSV file by plate."""
        vehicles = self.load_all()
        vehicles = [v for v in vehicles if v.plate != plate]
        self.save_all(vehicles)

    def update_vehicle(self, plate: str, updated_vehicle: Vehicle) -> None:
        """Update a vehicle in CSV file."""
        vehicles = self.load_all()
        for i, v in enumerate(vehicles):
            if v.plate == plate:
                vehicles[i] = updated_vehicle
                break
        self.save_all(vehicles)
