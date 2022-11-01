#!/usr/bin/python3
"""Module for Place model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implementing Place model

    Arguments:
        city_id (str): City id.
        user_id (str): User id.
        name (str): Name of Place.
        description (str): description of place.
        max_guest (int): maximum number of Guests.
        price_by_night (int): price by night.
        latitude (float): latitude of place
        longitude (float): longitude of place
        number_rooms (int): number of rooms
        number_bathrooms (inrt): number of bathrooms
        amenity_ids (list): listr of amenity id
        """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
