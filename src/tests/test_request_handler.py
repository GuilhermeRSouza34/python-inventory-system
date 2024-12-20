# src/tests/test_request_handler.py

import unittest
from src.request_handler import RequestHandler
from unittest.mock import Mock

class TestRequestHandler(unittest.TestCase):
    def setUp(self):
        self.mock_inventory_manager = Mock()
        self.request_handler = RequestHandler(self.mock_inventory_manager)

    def test_register_request_success(self):
        self.mock_inventory_manager.process_request.return_value = True
        self.request_handler.register_request('Produto A', 'Setor 1', 10)
        self.mock_inventory_manager.process_request.assert_called_with('Produto A', 10)

    def test_register_request_failure(self):
        self.mock_inventory_manager.process_request.return_value = False
        self.request_handler.register_request('Produto A', 'Setor 1', 10)
        self.mock_inventory_manager.process_request.assert_called_with('Produto A', 10)

if __name__ == '__main__':
    unittest.main()