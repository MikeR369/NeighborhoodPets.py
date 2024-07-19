# Author: Michael Russell
# GitHub username: Mike369
# Date: 07/18/2024
# Description: Write a class named NeighborhoodPets that has methods for adding a pet, deleting a pet, searching for
# the owner of a pet, saving data to a JSON file, loading data from a JSON file, and getting a set of all pet species.

import json


class DuplicateNameError(Exception):
    """Exception raised when a duplicate pet name is added."""
    pass


class NeighborhoodPets:
    """
    A class to manage neighborhood pets with methods to add, delete, search, save, load, and list pet species.

    Attributes:
    pets (list): A list to store pet data.
    """

    def __init__(self):
        """
        Initializes the NeighborhoodPets class with an empty list of pets.

        Parameters:
        None

        Returns:
        None
        """
        self.pets = []

    def add_pet(self, name, species, owner):
        """
        Adds a pet to the list if the name is not a duplicate.

        Parameters:
        name (str): The name of the pet.
        species (str): The species of the pet.
        owner (str): The name of the pet's owner.

        Returns:
        None

        Raises:
        DuplicateNameError: If a pet with the same name already exists.
        """
        for pet in self.pets:
            if pet['name'] == name:
                raise DuplicateNameError(f"A pet with the name {name} already exists.")
        self.pets.append({"name": name, "species": species, "owner": owner})

    def delete_pet(self, name):
        """
        Deletes a pet from the list by name.

        Parameters:
        name (str): The name of the pet to delete.

        Returns:
        None
        """
        self.pets = [pet for pet in self.pets if pet['name'] != name]

    def get_owner(self, name):
        """
        Gets the owner of a pet by name.

        Parameters:
        name (str): The name of the pet.

        Returns:
        str: The name of the pet's owner, or None if not found.
        """
        for pet in self.pets:
            if pet['name'] == name:
                return pet['owner']
        return None

    def save_as_json(self, filename):
        """
        Saves the current list of pets to a JSON file.

        Parameters:
        filename (str): The name of the JSON file to save the data.

        Returns:
        None
        """
        with open(filename, 'w') as file:
            json.dump(self.pets, file)

    def read_json(self, filename):
        """
        Loads pet data from a JSON file, replacing the current list.

        Parameters:
        filename (str): The name of the JSON file to read the data from.

        Returns:
        None
        """
        with open(filename, 'r') as file:
            self.pets = json.load(file)

    def get_all_species(self):
        """
        Gets a set of all species in the pet list.

        Parameters:
        None

        Returns:
        set: A set of all pet species.
        """
        return set(pet['species'] for pet in self.pets)
