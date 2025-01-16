import os

from inventory.specs import ItemSpec

class FluxCapacitor(ItemSpec):

    consumable = False

    def __init__(self):
        """Constructor"""
        super().__init__(__name__)
        self.volume = 1

    def __str__(self):
        return f"""Manufacture date: 21 October 2015. Inspected by: Marty M."""
