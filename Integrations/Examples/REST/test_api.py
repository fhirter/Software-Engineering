import pytest
import requests

BASE_URL = "http://localhost:8080/api/items"


@pytest.fixture(scope="session")
def base_url():
    """Fixture to provide base URL"""
    return BASE_URL


@pytest.fixture
def new_item():
    """Fixture to create a test item and clean it up after test"""
    # Setup: Create an item
    item = {"name": "Test Item", "description": "Test description"}

    response = requests.post(BASE_URL, json=item)

    location = response.headers["Location"]

    yield item  # Provide item to test

    # Teardown: Delete the item (if it still exists)
    try:
        requests.delete(f"{BASE_URL}/{item['id']}")
    except:
        pass


class TestItemsAPI:

    def test_get_all_items(self, base_url, new_item):
        """Test GET all items"""
        response = requests.get(base_url)

        assert response.status_code == 200
        response_data = response.json()
        assert isinstance(response_data, list)
        assert new_item in response_data

    def test_get_specific_item(self, base_url):
        """Test GET specific item"""
        response = requests.get(f"{base_url}/1")

        assert response.status_code == 200
        assert response.json()["id"] == 1
        assert "name" in response.json()

    def test_create_item(self, base_url):
        """Test POST - Create new item"""
        new_item = {"name": "New Test Item", "description": "Test description"}
        response = requests.post(base_url, json=new_item)

        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["name"] == "New Test Item"
        assert response.json()["description"] == "Test description"

        # Cleanup
        requests.delete(f"{base_url}/{response.json()['id']}")

    def test_update_item(self, base_url, new_item):
        """Test PUT - Update item"""
        item_id = new_item["id"]
        updated_data = {"name": "Updated Name", "description": "Updated description"}

        response = requests.put(f"{base_url}/{item_id}", json=updated_data)

        assert response.status_code == 200
        assert response.json()["name"] == "Updated Name"
        assert response.json()["description"] == "Updated description"
        assert response.json()["id"] == item_id

    def test_delete_item(self, base_url, new_item):
        """Test DELETE item"""
        item_id = new_item["id"]

        response = requests.delete(f"{base_url}/{item_id}")

        assert response.status_code == 200
        assert "message" in response.json()

        # Verify item is deleted
        get_response = requests.get(f"{base_url}/{item_id}")
        assert get_response.status_code == 404

