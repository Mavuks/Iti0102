
"""Orwell 1984."""


class Citizen:
    """Class which represents a single citizen."""

    allowed_statuses = ["citizen", "prole", "nonperson", "under surveillance"]

    def __init__(self, name, party, status="citizen"):
        """
        Class constructor.

        :param name: name of the citizen
        :param party: party which he belongs to
        :param status: status
        """
        self.name = name
        self.party = party
        self.status = status
        if status not in Citizen.allowed_statuses:
            self.Status = "citizen"
        if status is "prole":
            self.party = None
        if status is "nonperson":
            self.name = None
            self.party = None
        self.party = []
        if self.party is not None:
            self.party.append(Citizen)




    def set_party(self, party):
        """
        Set citizen's party. The method does not return anything.

        :param party: new party (Inner or Outer, both are Party class instances)
        """
        pass

    def get_party(self):
        """
        Get the citizen's party.

        :return: party object
        """
        return self.party

    def set_status(self, status):
        """
        Set citizen's status. The method does not return anything.

        :param status: new status
        """
        pass

    def get_status(self):
        """
        Get the citizen's status.

        :return: status
        """
        return self.status

    def set_name(self, name):
        """
        Set the citizen's name. The method does not return anything.

        :param name: new name
        """
        pass

    def get_name(self):
        """
        Get the citizen's name.

        :return: name
        """
        return self.name

    def __str__(self):
        """
        Compute string representation of this object.

        :return: f"BIG BROTHER IS WATCHING YOU, {self.name}"
        """
        pass
        return f"BIG BROTHER IS WATCHING YOU, {self.name}"

class Party:
    """Party class."""

    def __init__(self):
        """Class constructor."""
        pass

    def get_party_members(self):
        """
        Get the list of party members.

        :return: list
        """
        pass

    def add_party_member(self, citizen):
        """
        Add the citizen to the party members' list.

        Citizen must be instance of Citizen class, must have name, must not already be a member and must not have a
        'nonperson' status.
        Does not return anything.
        :param citizen Citizen class instance
        """
        pass

    def remove_party_member(self, citizen):
        """Remove the citizen from the party members' list."""
        pass

    def vaporize(self, citizen):
        """
        Remove the citizen from the party members, set his name and party to None and status to nonperson.

                    The method does not return anything.
        :param citizen: Citizen class instance

        """
        pass

    def get_privileges(self):
        """
        Get privileges granted by party.

        :return: None
        """
        pass

    @staticmethod
    def get_slogan():
        r"""
        Get the party slogan.

        :return: "WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH"
        """
        return f"WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH"


class InnerParty(Party):
    """Inner party class, which extends the Party class."""

    def get_privileges(self):
        """
        Get privileges granted by party (Override).

        :return: "Everything"
        """
        return f"Everything"

    def __str__(self):
        """
        Compute string representation of this object.

        :return: "Inner party"
        """
        return f"Inner party"


class OuterParty(Party):
    """Outer party class, which extends the Party class."""

    def __str__(self):
        """
        Compute string representation of this object.

        :return: "Outer party"
        """
        return f"Outer party"


class BigBrother:
    """Big brother class."""

    def __init__(self, inner_party, outer_party):
        """
        Class constructor.

        :param inner_party: inner party object
        :param outer_party: outer party object
        """
        pass

    def get_all_citizens(self):
        """
        Get all citizens who are members in the parties.

        :return: list
        """
        pass

    def massive_vaporize(self, status):
        """
        Vaporize people with a given status.

        :param status: string
        :return: number of vaporized people per session
        """
        pass

    def get_number_of_vaporized(self):
        """
        Get number of vaporized people of all time.

        :return: integer
        """
        pass


if __name__ == '__main__':
    ip = InnerParty()
    op = OuterParty()

    c = Citizen("Winston Smith", op, "under surveillance")
    c1 = Citizen("Julia", op, "under surveillance")

    assert (c.get_name()) == 'Winston Smith'
    assert str(c.get_party()) == 'Outer party'
    assert (c.get_status()) == 'under surveillance'
    assert str(c) == 'BIG BROTHER IS WATCHING YOU, Winston Smith'
    assert str(c1) == 'BIG BROTHER IS WATCHING YOU, Julia'
    c.set_party(ip)
    assert str(c.get_party()) == 'Inner party'
    assert len(ip.get_party_members()) == 1
    assert len(op.get_party_members()) == 1
    assert not (c in op.get_party_members())
    c.set_party(op)
    assert str(c.get_party()) == 'Outer party'
    assert len(op.get_party_members()) == 2

    c2 = Citizen("O'Brien", ip)
    assert (c2.get_name()) == "O'Brien"
    assert str(c2.get_party()) == 'Inner party'
    assert (c2.get_status()) == 'citizen'

    c3 = Citizen("Syme", op, "nonperson")
    assert (c3.get_name()) is None
    assert (c3.get_party()) is None
    assert (c3.get_status()) == 'nonperson'

    c4 = Citizen("Smb", op, "prole")

    assert (c4.get_name()) == 'Smb'
    assert (c4.get_party()) is None
    assert (c4.get_status()) == 'prole'

    assert len(ip.get_party_members()) == 1
    assert len(op.get_party_members()) == 2
    assert str(ip) == 'Inner party'
    assert str(op) == 'Outer party'
    assert (ip.get_privileges()) == 'Everything'
    assert (op.get_privileges()) is None

    assert (ip.get_slogan()) == 'WAR IS PEACE\nFREEDOM IS SLAVERY\nIGNORANCE IS STRENGTH'

    bb = BigBrother(ip, op)
    assert len(bb.get_all_citizens()) == 3
    assert (bb.massive_vaporize("under surveillance")) == 2
    assert len(bb.get_all_citizens()) == 1
    assert (c.get_name()) is None
    assert (c.get_party()) is None
    assert (c.get_status()) == 'nonperson'
    assert len(ip.get_party_members()) == 1
    assert len(op.get_party_members()) == 0
    assert (bb.massive_vaporize("citizen")) == 1
    assert (bb.get_number_of_vaporized()) == 3