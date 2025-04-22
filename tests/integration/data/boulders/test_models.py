from boulder_log.data.boulders import models as boulder_models
from boulder_log.data.locations import models as location_models
from boulder_log.data.users import models as user_models

import pytest


@pytest.mark.django_db
def test_boulder_model():
    """
    Test the Boulder model.
    """
    # Arrange
    # Create a user instance
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
    # Create a Boulder instance
    boulder = boulder_models.Boulder.new(
        name="Test Boulder",
        description="A test boulder.",
        grade="V0",
        style="Slab",
        is_private=False,
        location_id=location.id,
        photo=None,
        segmented_image=None,
        created_by_id=user.id,
    )

    # Check the string representation
    assert str(boulder) == f"{boulder.id} - Test Boulder"

    # Check the is_public property
    assert boulder.is_public is True

    # Check the default values
    assert boulder.date_added is not None
    assert boulder.date_modified is not None

    # Check the location property
    assert boulder.location == location

    # Check the created_by property
    assert boulder.created_by == user
