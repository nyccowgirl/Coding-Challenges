"""Find whether two people in an undirected graph are friends.

Let's create a graph and add a bunch of people:

    >>> f = FriendGraph()
    >>> f.add_person("Frodo")
    >>> f.add_person("Sam")
    >>> f.add_person("Gandalf")
    >>> f.add_person("Merry")
    >>> f.add_person("Pippin")
    >>> f.add_person("Treebeard")
    >>> f.add_person("Sauron")
    >>> f.add_person("Dick Cheney")

Now, let's set some friendships:

    >>> f.set_friends("Frodo", ["Sam", "Gandalf", "Merry", "Pippin"])
    >>> f.set_friends("Sam", ["Merry", "Pippin", "Gandalf"])
    >>> f.set_friends("Merry", ["Pippin", "Treebeard"])
    >>> f.set_friends("Pippin", ["Treebeard"])
    >>> f.set_friends("Sauron", ["Dick Cheney"])

We specifically said Sam was a friend of Frodo's, so they should be
connected:

    >>> f.are_connected("Frodo", "Sam")
    True

Our ``set_friends()`` sets the reciprocal relationship automatically
(this is an "undirected graph"), so Sam is also friends with Frodo:

    >>> f.are_connected("Sam", "Frodo")
    True

Sam isn't friends with Treebeard -- but we can find a connection
(Sam -> Frodo -> {Merry or Pippin} -> Treebeard)

    >>> f.are_connected("Sam", "Treebeard")
    True

Poor Sauron. He won't be invited to Frodo's tea party:

    >>> f.are_connected("Frodo", "Sauron")
    False

He does have friends of his own, though:

    >>> f.are_connected("Sauron", "Dick Cheney")
    True

Joel Burton <joel@joelburton.com>
"""


class PersonNode(object):
    """A node in a graph representing a person.

    This is created with a name and, optionally, a list of adjacent nodes.
    """

    def __init__(self, name, adjacent=[]):
        self.name = name
        self.adjacent = set(adjacent)

    def __repr__(self):
        return "<PersonNode %s>" % self.name


class FriendGraph(object):
    """Graph to keep track of social connections."""

    def __init__(self):
        """Create an empty graph.

        We keep a dictionary to map people's names -> nodes.
        """

        self.nodes = {}

    def add_person(self, name):
        """Add a person to our graph.

            >>> f = FriendGraph()
            >>> f.nodes
            {}

            >>> f.add_person("Dumbledore")
            >>> f.nodes
            {'Dumbledore': <PersonNode Dumbledore>}
        """

        if name not in self.nodes:
            # Be careful not to just add them a second time -- otherwise,
            # if we accidentally added someone twice, we'd clear out their list
            # of friends!
            self.nodes[name] = PersonNode(name)

    def set_friends(self, name, friend_names):
        """Set two people as friends.

        This is reciprocal: so if Romeo is friends with Juliet, she's
        friends with Romeo (our graph is "undirected").

        >>> f = FriendGraph()
        >>> f.add_person("Romeo")
        >>> f.add_person("Juliet")
        >>> f.set_friends("Romeo", ["Juliet"])

        >>> f.nodes["Romeo"].adjacent
        set([<PersonNode Juliet>])

        >>> f.nodes["Juliet"].adjacent
        set([<PersonNode Romeo>])
        """

        person = self.nodes[name]

        for friend_name in friend_names:
            friend = self.nodes[friend_name]

            # Since adjacent is a set, we don't care if we're adding duplicates ---
            # it will only keep track of each relationship once. We do want to
            # make sure that we're adding both directions for the relationship.
            person.adjacent.add(friend)
            friend.adjacent.add(person)

    def are_connected(self, name1, name2):
        """Is this name1 friends with name2?"""

        current = self.nodes[name1]

        seen = set()
        to_see = set(current.adjacent)

        while to_see:
            if current == self.nodes[name2]:
                return True
            else:
                seen.add(current)
                current = to_see.pop()
                if current not in seen:
                    to_see = to_see | current.adjacent

        return False


# SOLUTION FILE:

# recursive option

    # def are_connected(self, name1, name2):
    #     """Is this name1 friends with name2?"""

    #     # START SOLUTION

    #     def _are_connected(node, name2, seen):
    #         """Recursive function to check if node connects w/person name.

    #         :seen: is a set of all nodes that have been visited.
    #         """

    #         # Use a DFS (depth-first search) to see if the nodes connect.
    #         # This recurses for each adjacent node of the passed-in node,
    #         # but it keeps track of nodes visited in a set, so it can avoid loops.

    #         if node.name == name2:
    #             # Yes, they're connected
    #             return True

    #         # Keep track of the fact that we've visited here
    #         seen.add(node)

    #         for n in node.adjacent:
    #             # Recursively check all friends of node

    #             if n in seen:
    #                 # We've already checked (or are mid-checking!) this node,
    #                 # so don't start a search again. Otherwise, this could
    #                 # loop forever in a cycle.
    #                 continue

    #             if _are_connected(n, name2, seen):
    #                 # We found a match -- get out of loop and return upward
    #                 return True

    #         # No match here (or deeper) -- so pass upward
    #         return False

    #     # Call recursive function, using node-of-name1 as a start,
    #     # looking for name2, and with a fresh, empty set for people-we've-seen.
    #     return _are_connected(self.nodes[name1], name2, set())


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
