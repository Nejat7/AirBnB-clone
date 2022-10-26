#!/usr/bin/python3
"""Module for Place model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implementing Place model

    Arguments:
        city_id (str): City id.
        usr_id 9str): User id.
        name (str): Name of Place.
        dcr (str): description of place.
        max_G (int): maximum number of Guests.
        PBN (int): price by night.
        lat (float): latitude of place
        lot (float): longitude of place
        num_room (int): number of rooms
        num_bath (inrt): number of bathrooms
        am_id (list): listr of amenity id
        """
        city_id = ""
        usr_id = ""
        name = ""
        dcr = ""
        num_room = 0
        num_bath = 0
        max_G = 0
        PBN = 0
        lat = 0.0
        lot = 0.0
        am_id = []
