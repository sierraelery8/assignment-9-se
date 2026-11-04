
class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Add a friend if they are not already connected
        if friend is self:
            return

        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        # Check if the person already exists
        if name in self.people:
            print(f"{name} already exists in the network.")
            return

        # Create a new Person object and store it
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        # Check if both people exist
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Create a bidirectional friendship
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        # Display each person and their friends
        for person_name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]

            connected_friends = ", ".join(friend_names)

            print(f"{person_name} is friends with: {connected_friends}")


# ==========================================
# TEST YOUR SOCIAL NETWORK
# ==========================================

if __name__ == "__main__":

    network = SocialNetwork()

    # Add at least 6 people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Test duplicate person
    print("\n--- Testing Duplicate Person ---")
    network.add_person("Alex")

    # Create at least 8 friendships
    print("\n--- Creating Friendships ---")

    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Test nonexistent person
    print("\n--- Testing Missing Person ---")
    network.add_friendship("Jordan", "Johnny")

    # Test duplicate friendship
    print("\n--- Testing Duplicate Friendship ---")
    network.add_friendship("Alex", "Jordan")

    # Print the complete network
    print("\n--- Complete Social Network ---")
    network.print_network()


# ==========================================
# DESIGN MEMO
# ==========================================

'''
I chose to use a graph for this social network because it makes
the most sense for showing how people are connected. Each person
is a node, and their friendships are the connections between them.
Since friendships go both ways, a graph works really well for
this type of project.

I don't think a regular list would work as well because it
mostly keeps things in order but doesn't really show how
different people are connected to each other. A tree wouldn't
be the best choice either because it has a parent-child structure.
In a social network, nobody is really at the top. Everyone can
have their own friends and be connected to multiple people.

One thing I noticed while working on this project is that when
two people become friends, both people's friend lists need to
be updated. This makes sure the friendship works in both
directions. Adding a friend is pretty simple, but checking
whether someone is already on the list takes a little more
work as the list gets bigger.

I also learned that using an adjacency list helps save memory
because it only keeps track of actual friendships instead of
every possible connection. Printing the network means going
through each person and showing who they are friends with.
Overall, I think a graph was the best choice for this project
because it makes it easy to add people, create friendships,
and keep everything organized as the network grows.
'''