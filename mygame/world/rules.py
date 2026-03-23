"""
rules.py

This module contains the core rulesets for the game.
This includes character attributes, pools (Resources), and other core logic.
"""

class Resource:
    """
    A generic resource class for handling character pools like Health, Move, Mana, and Blood.
    """
    def __init__(self, obj, name, current=0, max_val=0, hidden=False):
        self.obj = obj
        self.name = name
        self.current = current
        self.max = max_val
        self.hidden = hidden

    def modify(self, amount):
        """Modifies the current resource amount, keeping it within bounds."""
        self.current += amount
        if self.current > self.max:
            self.current = self.max
        elif self.current < 0:
            self.current = 0

    def set(self, current, max_val=None):
        """Sets the resource value directly."""
        if max_val is not None:
            self.max = max_val
        self.current = current
        if self.current > self.max:
            self.current = self.max
        elif self.current < 0:
            self.current = 0

    def restore(self):
        """Restores the resource to its maximum value."""
        self.current = self.max

    def is_empty(self):
        """Checks if the resource is depleted."""
        return self.current <= 0

    def __str__(self):
        return f"{self.name}: {self.current}/{self.max}"

# The core pools used by characters in EmpireMUD
class Health(Resource):
    def __init__(self, obj, current=100, max_val=100):
        super().__init__(obj, "Health", current, max_val)

class Move(Resource):
    def __init__(self, obj, current=100, max_val=100):
        super().__init__(obj, "Move", current, max_val)

class Mana(Resource):
    def __init__(self, obj, current=100, max_val=100):
        super().__init__(obj, "Mana", current, max_val)

class Blood(Resource):
    def __init__(self, obj, current=100, max_val=100, is_vampire=False):
        # Blood is hidden for mortals, visible and necessary for vampires
        hidden = not is_vampire
        super().__init__(obj, "Blood", current, max_val, hidden=hidden)

def initialize_pools(obj, is_vampire=False):
    """Initializes the core resource pools for a character."""
    obj.ndb.health = Health(obj)
    obj.ndb.move = Move(obj)
    obj.ndb.mana = Mana(obj)
    obj.ndb.blood = Blood(obj, is_vampire=is_vampire)
