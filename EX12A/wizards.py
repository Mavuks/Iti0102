"""nodasicnids."""

class Wand:
    """Wand."""

    def __init__(self, wood_type, core):
        """Wand."""
        self.wood_type = wood_type
        self.core = core


    def set_wood_type(self, wood_type):
        """Wood type."""



    def set_core(self, core):
        """Core."""

    @staticmethod
    def check_wand(wand):
        """Check wand."""

    def __str__(self):
        """fafdsf."""

class Wizard:
    """Wixard."""

    def __init__(self, name, wand=None):
        """Wdnasifn."""
        self.name = name
        self.wand = wand

    def set_wand(self, wand):
        """Set wand."""

    def get_wand(self):
        """get wand."""

        return self.wand

    def __str__(self):
        """Return wizard name."""

class School:
    """Scool."""

    def __init__(self, name: str):
        """fddsaffds."""
        self.name = name

    def add_wizard(self, wizard):
        """add Wizard."""


    def remove_wizard(self,wizard):
        """remove wizard."""

    def get_wizards(self):
        """Get wizards."""


    def get_wizard_by_wand(self,wand):
        """get wizard by wand."""


    def __str__(self):
        """return scool"""
        return name







class MismatchError(Exception):
    """
    Class MismatchError inherits its properties from Exception class.

    Should have user-defined message.
    """

    def __init__(self, message):
        """
        Class constructor.

        :param message: user message
        """
        self.message = message


if __name__ == '__main__':

    wand1 = Wand("Holly", "Phoenix feather")
    wand2 = Wand("Vine", "Dragon heartstring")
    bad_wand = Wand(None, "empty")
    assert str(wand1) == 'Holly, Phoenix feather'
    assert str(wand2) == 'Vine, Dragon heartstring'

    wizard1 = Wizard("Harry Potter")
    wizard2 = Wizard("Hermione Granger")
    assert str(wizard1) == 'Harry Potter'
    assert str(wizard2) == 'Hermione Granger'

    bad_wizard = Wizard(None, None)
    school = School("Hogwarts School of Witchcraft and Wizardry")
    assert str(school) == 'Hogwarts School of Witchcraft and Wizardry'

    assert wizard1.get_wand() is None
    wizard1.set_wand(wand1)
    assert str(wizard1.get_wand()) == 'Holly, Phoenix feather'
    # wizard1.set_wand(bad_wand)  # --> MismatchError: The wand like that does not exist!

    assert school.add_wizard(wizard1) == 'Harry Potter started studying in Hogwarts School of Witchcraft and Wizardry.'
    assert school.get_wizards().__len__() == 1

    # school.add_wizard(wizard2)  # --> MismatchError: It's a filthy muggle!
    # school.add(bad_wizard)  # --> MismatchError: It's a filthy muggle!
    wizard2.set_wand(wand2)
    assert school.add_wizard(wizard2) == 'Hermione Granger started studying in Hogwarts School of Witchcraft and Wizardry.'

    assert school.get_wizards().__len__() == 2
    assert school.add_wizard(wizard1) == 'Harry Potter is already studying in this school!'

    assert str(school.get_wizard_by_wand(wand1)) == 'Harry Potter'
    assert str(school.get_wizard_by_wand(wand2)) == 'Hermione Granger'

    school.remove_wizard(wizard1)

    assert school.get_wizard_by_wand(wand1) is None

    School.schools.append("Example school")
    assert "Example school" in School.schools
