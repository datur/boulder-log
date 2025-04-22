import factory


class Equipment(factory.django.DjangoModelFactory):
    """
    Factory for creating Equipment instances.
    """

    class Meta:
        model = "equipment.Equipment"
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    equipment_type = factory.Faker("word")
    brand = factory.Faker("word")
    is_private = factory.Faker("boolean")
    created_by_id = factory.Faker("random_int", min=1, max=100)
    photo = factory.django.ImageField(color="blue")
    date_added = factory.Faker("date_time")
    date_modified = factory.Faker("date_time")
