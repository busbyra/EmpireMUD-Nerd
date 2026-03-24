"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""

from evennia.objects.objects import DefaultCharacter

from .objects import ObjectParent
from world.rules import initialize_pools


class Character(ObjectParent, DefaultCharacter):
    """
    The Character just re-implements some of the Object's methods and hooks
    to represent a Character entity in-game.

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Object child classes like this.

    """

    def at_object_creation(self):
        """
        Called once, when the object is first created.
        """
        super().at_object_creation()

        # Core EmpireMUD Attributes
        # 1 is the default starting attribute in the legacy codebase
        self.db.strength = 1
        self.db.dexterity = 1
        self.db.charisma = 1
        self.db.greatness = 1
        self.db.intelligence = 1
        self.db.wits = 1

        # We also need a way to track the modified version of attributes (aff_attributes)
        # This can be handled dynamically via properties or a separate dict later,
        # but for now we store the base.

        # Determine if character is a vampire (placeholder logic, mortal by default)
        is_vampire = False

        # Initialize Resource pools (Health, Move, Mana, Blood)
        initialize_pools(self, is_vampire=is_vampire)

    def at_init(self):
        """
        Called every time the object is loaded into memory.
        """
        super().at_init()

        # Determine if character is a vampire (placeholder logic)
        is_vampire = False

        # Re-initialize the resource pools when loaded into memory,
        # because ndb (non-persistent database) is lost on reboot/reload.
        # This will set up self.ndb.health, self.ndb.move, etc.
        # We also need to restore their values from persistent storage (db) if we
        # implement persistence for pools later, but for now we'll just initialize them.
        initialize_pools(self, is_vampire=is_vampire)
