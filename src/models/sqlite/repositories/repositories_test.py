import pytest

from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_connection_handler

from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="integração com o banco")
def test_list_pets():
    repository = PetsRepository(db_connection_handler)
    response = repository.list_pets()
    print(response)


@pytest.mark.skip(reason="integração com o banco")
def test_delete_pet():
    name = "gato"
    repository = PetsRepository(db_connection_handler)
    repository.delete_pets(name)


@pytest.mark.skip(reason="integração com o banco")
def test_insert_person():
    repository = PeopleRepository(db_connection_handler)
    repository.insert_person(
        first_name="Test",
        last_name="Name",
        age=15,
        pet_id=1
    )


@pytest.mark.skip(reason="integração com o banco")
def test_get_person():
    person_id = 1

    repository = PeopleRepository(db_connection_handler)
    response = repository.get_person(person_id)
    print()
    print(response)
    print(response.pet_name)
