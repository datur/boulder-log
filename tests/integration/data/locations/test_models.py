import pytest

from boulder_log.data.locations import models as location_models
from boulder_log.data.users import models as user_models
from boulder_log.data.boulders import models as boulder_models


@pytest.mark.django_db
def test_location_model():
    """
    Test the Location model.
    """
    # Create a User instance
    user = user_models.User.new(
        username="testuser",
        password="password123",
        email="test@test.com",
        first_name="Test",
        last_name="User",
    )
    # Create a Location instance
    location = location_models.Location.new(
        name="Test Location",
        description="A test location.",
        latitude=40.7128,
        longitude=-74.0060,
        is_private=False,
        created_by_id=user.id,
    )

    # Check the string representation
    assert str(location) == f"{location.id} - Test Location"

    # Check the is_public property
    assert location.is_public is True

    # Check the default values
    assert location.date_added is not None
    assert location.date_modified is not None

    # Check the created_by property
    assert location.created_by == user

    with pytest.raises(boulder_models.Boulder.DoesNotExist):
        location.boulders.all()
