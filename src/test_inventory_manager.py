import unittest
from inventory_manager import InventoryManager
from unittest.mock import patch

class TestInventoryManager(unittest.TestCase):

    @patch('inventory_manager.load_inventory')
    @patch('inventory_manager.save_inventory')
    def setUp(self, mock_save_inventory, mock_load_inventory):
        mock_load_inventory.return_value = {'apple': 10, 'banana': 5}
        self.manager = InventoryManager('test_inventory.xlsx')

    def test_display_inventory(self):
        expected_inventory = {'apple': 10, 'banana': 5}
        actual_inventory = self.manager.display_inventory()
        self.assertEqual(actual_inventory, expected_inventory)

if __name__ == '__main__':
    unittest.main()