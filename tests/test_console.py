#!/usr/bin/python3
"""File for console test"""

import unittest
from unittest.mock import patch
import json
from io import StringID
import console
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Test Console """

    def test_quit_EOF(self):
        """ test quit and EOF functions in cmd """
        self.assertEqual(HBNBCommand().onecmd("EOF"), True)
        self.assertEqual(HBNBCommand().onecmd("quit"), True)

    def test_doc_console(self):
        """ test_doc_console(self): to test if module and class has docs """
        self.assertIsNotNone(HBNBCommand.__doc__, 'no docs for Base class')
        self.assertIsNotNone(console.__doc__, 'no docs for module')

    def test_empty_line(self):
        """ Test handling empty lines """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertEqual("", output.getvalue())


class TestCreate(unittest.TestCase):
    """Test Creating a new instance of Class,
    saves it (to the JSON file)"""

    def test_args_length(self):
        """test if args length < 1 to print [** class name missing **]"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())

    def test_create(self):
        """test creating a new instance of a Class,
        saves it (to the JSON file)"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create BaseModel"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "BaseModel.{}".format(captured_id)
            input = "create BaseModel"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create User"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "User.{}".format(captured_id)
            input = "create User"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create Amenity"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "Amenity.{}".format(captured_id)
            input = "create Amenity"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create State"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "State.{}".format(captured_id)
            input = "create State"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create Place"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "Place.{}".format(captured_id)
            input = "create Place"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create City"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "City.{}".format(captured_id)
            input = "create City"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create Review"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "Review.{}".format(captured_id)
            self.assertIn(inst_key, storage.all().keys())

    def test_invalid_className(self):
        """Test if input is not a valid class"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create UnknownClass"
            expected = "** class doesn't exist **"
            HBNBCommand().onecmd(input)  # excute command
            self.assertEqual(expected, output.getvalue().strip())
