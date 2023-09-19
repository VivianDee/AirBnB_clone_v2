#!/usr/bin/python3
"""The TestConsole Class"""
import unittest
from io import StringIO
from console import HBNBCommand
import sys
import uuid


class TestConsole(unittest.TestCase):
    """Test class for the HBNBCommand console"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        """Clean up the test environment"""
        self.console = None
        self.mock_stdout.close()

    def test_exists(self):
        """Check if command docstrings exist"""
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_create_error(self):
        """Test create command with errors"""
        temp_out = StringIO()
        sys.stdout = temp_out

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_create("base")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()

    def test_create_success(self):
        """Test create command with success"""
        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_create("BaseModel")
        output = temp_out.getvalue().strip()
        self.assertTrue(uuid.UUID(output, version=4))
        sys.stdout = sys.__stdout__

    def test_create_with_args(self):
        """Test create command with arguments"""
        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_create("State name=\"California\"")
        output = temp_out.getvalue().strip()
        self.assertTrue(uuid.UUID(output, version=4))
        sys.stdout = sys.__stdout__

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_create("Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
        output = temp_out.getvalue().strip()
        self.assertTrue(uuid.UUID(output, version=4))
        sys.stdout = sys.__stdout__

    def test_show_error(self):
        """Test show command with errors"""
        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_show(None)
        self.assertEqual(temp_out.getvalue(), '** class name missing **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_show("base")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_show("BaseModel")
        self.assertEqual(temp_out.getvalue(), '** instance id missing **\n')
        temp_out.close()
        sys.stdout = sys.__stdout__

    def test_destroy_error(self):
        """Test destroy command with errors"""
        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_destroy(None)
        self.assertEqual(temp_out.getvalue(), '** class name missing **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_destroy("base")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_destroy("BaseModel")
        self.assertEqual(temp_out.getvalue(), '** instance id missing **\n')
        temp_out.close()
        sys.stdout = sys.__stdout__

    def test_update_error(self):
        """Test update command with errors"""
        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_update(None)
        self.assertEqual(temp_out.getvalue(), '** class name missing **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_update("base")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        self.console.do_update("BaseModel")
        self.assertEqual(temp_out.getvalue(), '** instance id missing **\n')
        temp_out.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
