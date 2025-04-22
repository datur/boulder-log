import factory


class Boulder(factory.django.DjangoModelFactory):
    """
    Factory for creating Boulder instances.
    """

    class Meta:
        model = "boulders.Boulder"
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    grade = factory.Faker("word")
    style = factory.Faker("word")
    is_private = factory.Faker("boolean")
    location_id = factory.Faker("random_int", min=1, max=100)
    created_by_id = factory.Faker("random_int", min=1, max=100)
    photo = factory.django.ImageField(color="blue")
    segmented_image = factory.django.ImageField(color="red")
    date_added = factory.Faker("date_time")
    date_modified = factory.Faker("date_time")
