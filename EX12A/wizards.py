"""Wands and Wizards."""


class Wand:
    """Class for wand."""
    def __init__(self, wood_type, core):
        """Class constructor."""
        self.wood_type = wood_type
        self.core = core

    def set_wood_type(self, wood_type):
        """Set the type of wood."""
        self.wood_type = wood_type

    def set_core(self, core):
        """Set core."""
        self.core = core

    @staticmethod
    def check_wand(wand):
        """Check if wand information is correct."""
        if not isinstance(wand, Wand) or not wand.wood_type or not wand.core:
            raise MismatchError("The wand like that does not exist!")
        else:
            return True

    def __str__(self):
        """Return wand information."""
        return f'{self.wood_type}, {self.core}'


class Wizard:
    """Class for wizards."""
    def __init__(self, name, wand=None):
        """Class constructor."""
        self.name = name
        self.wand = wand
        if wand is not None:
            Wand.check_wand(wand)

    def set_wand(self, wand):
        """Check Wand."""
        Wand.check_wand(wand)
        self.wand = wand

    def get_wand(self):
        """Return wizard wand."""
        return self.wand

    def __str__(self):
        """Return wizard name."""
        return f'{self.name}'


class School:
    """Class for wizard schools."""
    schools = [
        "Hogwarts School of Witchcraft and Wizardry",
        "Durmstrang Institute",
        "Ilvermorny School of Witchcraft and Wizardry",
        "Castelobruxo", "Beauxbatons Academy of Magic"]

    def __init__(self, name: str):
        """School."""
        self.name = name
        self.wizards = []
        if name not in School.schools:
            raise MismatchError("There is no such school!")

    def add_wizard(self, wizard):
        """Add new wizard."""
        if not isinstance(wizard, Wizard) or wizard is None or wizard.wand is None:
            raise MismatchError("It's a filthy muggle!")
        elif wizard in self.wizards:
            return f'{wizard} is already studying in this school!'
        else:
            self.wizards.append(wizard)
            return f'{wizard} started studying in {self.name}.'

    def remove_wizard(self, wizard):
        """Remove wizard."""
        if wizard in self.wizards:
            self.wizards.remove(wizard)

    def get_wizards(self):
        """All school wizards."""
        return self.wizards

    def get_wizard_by_wand(self, wand):
        """Find wizard by wand."""
        if wand is not None:
            Wand.check_wand(wand)
        elif wand is None:
            return

    def __str__(self):
        """Return school name."""
        return f'{self.name}'


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
