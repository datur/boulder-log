import factory


class Location(factory.django.DjangoModelFactory):
    """
    Factory for creating Location instances.
    """

    class Meta:
        model = "locations.Location"
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    is_private = factory.Faker("boolean")
    created_by_id = factory.Faker("random_int", min=1, max=100)
    photo = factory.django.ImageField(color="blue")
    date_added = factory.Faker("date_time")
    date_modified = factory.Faker("date_time")
