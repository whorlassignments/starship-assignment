import os

from inventory.specs import ItemSpec

class ThermoCube(ItemSpec):

    consumable = False

    def __init__(self):
        """Constructor"""
        super().__init__(__name__)
        self.volume = 1

    def __str__(self):
        return f"""A big sticker reads: 'Do not anger the ThermoCube.'"""
