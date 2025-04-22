import pytest

from boulder_log.data.equipment import models as equipment_models
from boulder_log.data.users import models as user_models


@pytest.mark.django_db
def test_equipment_model():
    """
    Test the Equipment model.
    """

    # Create a User instance
    user = user_models.User.new(
        username="testuser",
        password="password123",
        email="test@test.com",
        first_name="Test",
        last_name="User",
    )

    # Create an Equipment instance
    equipment = equipment_models.Equipment.new(
        name="Test Equipment",
        description="A test equipment.",
        equipment_type="Climbing Shoes",
        brand="Test Brand",
        is_private=False,
        photo=None,
        created_by_id=user.id,
    )

    # Check the string representation
    assert str(equipment) == f"{equipment.id} - Test Equipment"

    # Check the is_public property
    assert equipment.is_public is True

    # Check the default values
    assert equipment.date_added is not None
    assert equipment.date_modified is not None

    # Check the created_by property
    assert equipment.created_by == user
