from boulder_log.data.users import models as user_models

from tests.factories import users as user_factories

import pytest


@pytest.mark.django_db
def test_user_model_base_case():
    """
    Test the User model.
    """
    # Create a User instance
    user = user_factories.User(username="testuser")

    # Check the string representation
    assert str(user) == f"{user.id} - testuser"

    # Check the uuid field
    assert user.uuid is not None

    # Check the created_boulders property
    assert user.get_created_boulders() == []
    # Check the equipment property
    assert user.get_created_equipment() == []

    # Check the climbed_boulders property
    assert list(user.climbed_boulders.all()) == []

    # Check the equipment property
    assert list(user.equipment.all()) == []
