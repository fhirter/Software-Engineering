import pytest
import requests

BASE_URL = "http://localhost:8080"

endpoint = "api/items"

item = {"name": "Test Item", "description": "Test description"}

@pytest.fixture(scope="session")
def base_url():
    """Fixture to provide base URL"""
    return BASE_URL

@pytest.fixture(scope="session")
def items_endpoint(base_url):
    return f"{base_url}/{endpoint}"

@pytest.fixture
def created_item_location(items_endpoint):
    """Fixture to create a test item and clean it up after test"""
    response = requests.post(items_endpoint, json=item)

    location = response.headers["Location"]

    yield location  # Provide item to test

    # Teardown: Delete the item (if it still exists)
    try:
        requests.delete(location)
    except:
        pass


class TestItemsAPI:
    def test_create_item(self, items_endpoint, base_url):
        """Test POST - Create new item"""
        response = requests.post(items_endpoint, json=item)

        location = response.headers["Location"]

        assert response.status_code == 201
        assert "items" in location

        # Cleanup
        requests.delete(f"{base_url}{location}")

    def test_get_all_items(self, items_endpoint, created_item_location):
        """Test GET all items"""
        response = requests.get(items_endpoint)
        response_data = response.json()

        assert response.status_code == 200
        assert isinstance(response_data, list)
        assert any(
            i["name"] == item["name"] and i["description"] == item["description"]
            for i in response_data
        )


    def test_get_specific_item(self, base_url, created_item_location):
        """Test GET specific item"""
        response = requests.get(f"{base_url}/{created_item_location}")

        assert response.status_code == 200
        assert "name" in response.json()


    def test_update_item(self, base_url, created_item_location):
        """Test PUT - Update item"""
        new_name = "Updated Name"
        new_description = "Updated description"

        updated_data = {"name": new_name, "description": new_description}

        response = requests.put(f"{base_url}/{created_item_location}", json=updated_data)

        assert response.status_code == 200

        get_response = requests.get(f"{base_url}{created_item_location}")
        updated_data = get_response.json()
        assert updated_data["name"] == new_name
        assert updated_data["description"] == new_description


    def test_delete_item(self, base_url, created_item_location):
        """Test DELETE item"""
        response = requests.delete(f"{base_url}{created_item_location}")

        assert response.status_code == 200

        # Verify item is deleted
        get_response = requests.get(f"{base_url}{created_item_location}")
        assert get_response.status_code == 404

