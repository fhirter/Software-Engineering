import pytest
import requests

BASE_URL = "http://localhost:8080/api/items"

item = {"name": "Test Item", "description": "Test description"}

@pytest.fixture(scope="session")
def base_url():
    """Fixture to provide base URL"""
    return BASE_URL


@pytest.fixture
def created_item_location():
    """Fixture to create a test item and clean it up after test"""
    response = requests.post(BASE_URL, json=item)

    location = response.headers["Location"]

    yield location  # Provide item to test

    # Teardown: Delete the item (if it still exists)
    try:
        requests.delete(location)
    except:
        pass


class TestItemsAPI:
    def test_create_item(self, base_url):
        """Test POST - Create new item"""
        response = requests.post(base_url, json=item)
        location = response.headers["Location"]

        assert response.status_code == 201
        assert "items" in location

        # Cleanup
        requests.delete(location)

    def test_get_all_items(self, base_url, created_item_location):
        """Test GET all items"""
        response = requests.get(base_url)

        assert response.status_code == 200
        response_data = response.json()
        assert isinstance(response_data, list)
        assert item in response_data

    def test_get_specific_item(self, base_url, created_item_location):
        """Test GET specific item"""
        response = requests.get(created_item_location)

        assert response.status_code == 200
        assert response.json()["id"] == 1
        assert "name" in response.json()



    def test_update_item(self, base_url, created_item_location):
        """Test PUT - Update item"""
        item_id = created_item_location["id"]
        updated_data = {"name": "Updated Name", "description": "Updated description"}

        response = requests.put(f"{base_url}/{item_id}", json=updated_data)

        assert response.status_code == 200
        assert response.json()["name"] == "Updated Name"
        assert response.json()["description"] == "Updated description"
        assert response.json()["id"] == item_id

    def test_delete_item(self, base_url, created_item_location):
        """Test DELETE item"""
        item_id = created_item_location["id"]

        response = requests.delete(f"{base_url}/{item_id}")

        assert response.status_code == 200
        assert "message" in response.json()

        # Verify item is deleted
        get_response = requests.get(f"{base_url}/{item_id}")
        assert get_response.status_code == 404

