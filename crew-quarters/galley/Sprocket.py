import os

from inventory.specs import ItemSpec

class Sprocket(ItemSpec):

    consumable = False

    def __init__(self):
        """Constructor"""
        super().__init__(__name__)
        self.volume = 1

    def __str__(self):
        return f"""Says 'Spaceley's Sprockets'."""
