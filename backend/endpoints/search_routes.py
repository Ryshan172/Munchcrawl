import os
from fastapi import APIRouter, HTTPException
from interfaces.query_interfaces import Query

"""
Where endpoints related to searches should go
"""


# Initialise router
router = APIRouter()

# Test route 
@router.post("/test")
def test_endpoint():
    try:
        return {
            "message": "success"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running test: {e}")

