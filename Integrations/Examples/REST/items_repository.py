class ItemsRepository:
    def __init__(self):
        self.items = [
            {"id": 1, "name": "Item 1", "description": "First item"},
            {"id": 2, "name": "Item 2", "description": "Second item"}
        ]

    def get_all(self):
        """Get all items"""
        return self.items

    def get(self, item_id):
        """Get a specific item by ID"""
        return next((item for item in self.items if item["id"] == item_id), None)

    def create(self, name, description=""):
        """Create a new item"""
        new_item = {
            "id": max([item["id"] for item in self.items]) + 1 if self.items else 1,
            "name": name,
            "description": description
        }
        self.items.append(new_item)
        return new_item

    def update(self, item_id, name=None, description=None):
        """Update an existing item"""
        item = self.get(item_id)
        if not item:
            return None

        if name is not None:
            item["name"] = name
        if description is not None:
            item["description"] = description

        return item

    def delete(self, item_id):
        """Delete an item by ID"""
        item = self.get(item_id)
        if not item:
            return False

        self.items = [item for item in self.items if item["id"] != item_id]
        return True