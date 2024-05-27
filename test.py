import unittest
from main import TreeStore


class TestTreeStore(unittest.TestCase):
    def setUp(self) -> None:
        self.items = [
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 3, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
            {"id": 7, "parent": 4, "type": None},
            {"id": 8, "parent": 4, "type": None},
        ]
        self.ts = TreeStore(self.items)

    def test_get_all(self):
        self.assertEqual([{"id": 1, "parent": "root"}, {"id": 2, "parent": 1, "type": "test"}, {"id": 3, "parent": 1, "type": "test"}, {"id": 4, "parent": 2, "type": "test"}, {
                         "id": 5, "parent": 2, "type": "test"}, {"id": 6, "parent": 2, "type": "test"}, {"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}], self.ts.get_all())

    def test_get_item(self):
        self.assertEqual({"id": 7, "parent": 4, "type": None},
                         self.ts.get_item(7))

    def test_get_children(self):
        self.assertEqual([{"id": 7, "parent": 4, "type": None}, {
                         "id": 8, "parent": 4, "type": None}], self.ts.get_children(4))
        self.assertEqual([], self.ts.get_children(5))
        self.assertEqual([{"id": 4, "parent": 2, "type": "test"}, {"id": 5, "parent": 2, "type": "test"}, {
                         "id": 6, "parent": 2, "type": "test"}], self.ts.get_children(2))

    def test_get_all_parents(self):
        self.assertEqual([{"id": 4, "parent": 2, "type": "test"}, {"id": 2, "parent": 1, "type": "test"}, {
                         "id": 1, "parent": "root"}], self.ts.get_all_parents(7))


if __name__ == "__main__":
    unittest.main()
