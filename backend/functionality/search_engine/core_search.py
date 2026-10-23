from interfaces.query_interfaces import SearchQuery, SearchResponse
from typing import Dict, Any, List, Optional

"""
Holds the core search functionality 

Example: 
- A user enters their cravings, it's gets broken down and sorted in the flavour_mapping functionality
- Semantic and regular matching is done to map to map to ingredients and foods in the database
- If needed, an external search like google search is done
"""


def process_search_description(description: str):
    """
    Inputs: 
        - description: description of cravings 

    Functionality:
        - parses description and searches for matching sensations 

    Returns: 
        - details to help with sematic flavour mappings and suggestions
    """

    print(description)

    return "Okay"


def process_food_history(food_history: list):
    """
    Inputs: 
        - food_history: list of previously eaten foods

    Functionality:
        - Handles taking previuously eaten foods and creating "taste-potential" 
            to map to cravings and what they might want to eat next 

    Returns: 
        - flavour potential object (to be designed)
    """


    return "Okay"


def process_cravings(cravings_list: list):
    """
    Inputs: 
        - cravings_list: List of craving descriptions

    Functionality:
        - Processes the list of cravings and maps to different flavours 

    Returns: 
        - Don't know what yet
    """


    return "Okay"





def handle_cravings_search(query: SearchQuery):
    """
    Inputs: 
        - SearchQuery: body containing search details 

    Functionality:
        - Handles splitting search body into parts used for matching
        - Coordinates semantic and regular matching 

    Returns: 
        - SearchResponse: builds and returns response object
    """

    # Split query into different parts
    search_description = query.message
    craving_list = query.cravings
    food_history = query.previous_meals

    # Initialise response object to build later 
    response: SearchResponse = {}


    # Process search message 
    description_maps = process_search_description(search_description)
    
    # Process cravings list
    cravings_maps = process_cravings(craving_list)

    # Process food history
    food_maps = process_food_history(food_history)



    return response
