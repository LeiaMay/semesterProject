"""
Test Suite for the Personal Finance Tracker class in personal_finance_tracker.py. 
Contains unit tests for each method of the Personal Finance Tracker class
"""

import unittest
from datetime import datetime
from io import StringIO
import sys
import os
from personal_finance_tracker import PersonalFinanceTracker

class TestPersonalFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.finance_tracker = PersonalFinanceTracker()

    def tearDown(self): 
        """called after each test case"""
        del self.finance_tracker

    def test_add_transaction(self): 
        """tests add transaction method"""
        self.finance_tracker.add_transaction('2024-04-01', 'Test Transaction', 100, 'Test Category')
        self.assertEqual(len(self.finance_tracker.transactions), 1)

    def test_view_transactions(self): 
        """tests view transactions method"""
        self.finance_tracker.add_transaction('2024-04-01', 'Test Transaction', 100, 'Test Category')
        captured_output = StringIO()
        sys.stdout = captured_output
        self.finance_tracker.view_transactions()
        sys.stdout = sys.__stdout__
        self.assertIn('Test Transaction', captured_output.getvalue())

    def test_calculate_summary(self): 
        """tests calculate summary method"""
        self.finance_tracker.add_transaction('2024-04-01', 'Test Expense', -50, 'Expense')
        self.finance_tracker.add_transaction('2024-04-02', 'Test Income', 100, 'Income')
        captured_output = StringIO()
        sys.stdout = captured_output
        self.finance_tracker.calculate_summary()
        sys.stdout = sys.__stdout__
        self.assertIn('Total Expenses: -50', captured_output.getvalue())
        self.assertIn('Total Income: 100', captured_output.getvalue())

    def test_categorize_transactions(self): 
        """tests categorize transactions method"""
        self.finance_tracker.add_transaction('2024-04-01', 'Test Expense', -50, 'Expense')
        self.finance_tracker.add_transaction('2024-04-02', 'Test Income', 100, 'Income')
        captured_output = StringIO()
        sys.stdout = captured_output
        self.finance_tracker.categorize_transactions()
        sys.stdout = sys.__stdout__
        self.assertIn('Expense', captured_output.getvalue())
        self.assertIn('Income', captured_output.getvalue())

    def test_export_import_transactions(self): 
        """tests export transactions method"""
        filename = 'test_transactions.csv'
        self.finance_tracker.add_transaction('2024-04-01', 'Test Expense', -50, 'Expense')
        self.finance_tracker.export_transactions_to_csv(filename)
        self.assertTrue(os.path.exists(filename))
        self.finance_tracker = PersonalFinanceTracker()  # Resetting finance tracker
        self.finance_tracker.import_transactions_from_csv(filename)
        self.assertEqual(len(self.finance_tracker.transactions), 1)
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
