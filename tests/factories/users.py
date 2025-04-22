import factory


class User(factory.django.DjangoModelFactory):
    """
    Factory for creating User instances.
    """

    class Meta:
        model = "users.User"
        django_get_or_create = ("username",)

    username = factory.Faker("user_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
