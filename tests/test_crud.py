import pytest
import crud

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup: limpiar la lista antes de cada test
    crud.data.clear()
    yield
    # Teardown: limpiar la lista después de cada test
    crud.data.clear()

def test_create_and_read():
    crud.create("item1")
    assert "item1" in crud.read()

def test_update():
    crud.create("item2")
    assert crud.update(0, "item2_updated")
    assert crud.read()[0] == "item2_updated"

def test_update_invalid_index():
    assert not crud.update(99, "nuevo")

def test_delete():
    crud.create("item3")
    assert crud.delete(0)
    assert "item3" not in crud.read()

def test_delete_invalid_index():
    assert not crud.delete(99)
