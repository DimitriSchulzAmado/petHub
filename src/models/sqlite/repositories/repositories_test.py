import pytest

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
