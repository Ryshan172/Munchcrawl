from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional

"""
Interfaces related to search queries
"""

# Query that gets sent by a user
class SearchQuery(BaseModel):
    message: str
    cravings: Optional[List[str]]
    previous_meals: Optional[List[str]]


# Food suggestion object
class Suggestion(BaseModel):
    item_name: str
    provider_name: str
    provider_location: str


# Search response from query
class SearchResponse(BaseModel):
    message: str
    suggestions: Optional[list[Suggestion]]


