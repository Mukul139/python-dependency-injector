"""`Factory` providers with init injections example."""

from objects.providers import Factory
from objects.injections import KwArg


class User(object):

    """Example class User."""

    def __init__(self, main_photo):
        """Initializer.

        :param main_photo: Photo
        :return:
        """
        self.main_photo = main_photo
        super(User, self).__init__()


class Photo(object):

    """Example class Photo."""

# User and Photo factories:
photos_factory = Factory(Photo)
users_factory = Factory(User,
                        KwArg('main_photo', photos_factory))

# Creating several User objects:
user1 = users_factory()  # Same as: user1 = User(main_photo=Photo())
user2 = users_factory()  # Same as: user2 = User(main_photo=Photo())

# Making some asserts:
assert isinstance(user1, User)
assert isinstance(user1.main_photo, Photo)

assert isinstance(user2, User)
assert isinstance(user2.main_photo, Photo)

assert user1 is not user2
assert user1.main_photo is not user2.main_photo
