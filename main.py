from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.vehicle_controller import router

app = FastAPI(
    title="Vehicle BST API",
    description="Binary Search Tree API for vehicle management",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "Vehicle BST API",
        "version": "1.0.0",
        "docs": "/docs"
    }
