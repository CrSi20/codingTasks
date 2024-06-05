import sys
import os

# This is needed to be able to import modules from the root folder
# I could have added the tests to the root folder to avoid needing
# this line, but according to the course material tests should be
# in a separate folder, so I leave them here.
# I am getting some Flake8 warnings because the other imports should
# come before, but I cannot move them before as this line should be
# before using the other imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from unittest.mock import patch, mock_open
from unittest import mock
from datetime import datetime
import pickle
from models import Appointment, UserAuth
from database_manager import DatabaseManager


class TestDatabaseManager(unittest.TestCase):

    def test_read_appointment_one_appointment(self):
        appointment = Appointment("123", "abc", datetime(2024, 8, 24, 19, 30))

        # We mock the open function, and the load function of
        # pickle, and we define the behavior we need for this test
        # Using side_effect we specify that the first time pickle
        # should return an appointment object, and the second time
        # it should raise an EOFError
        with patch("builtins.open", mock_open(), create=True):
            with mock.patch.object(
                pickle,
                "load",
                side_effect=[appointment, EOFError()],
            ):
                # Arrange
                database_manager = DatabaseManager()

                # Action
                appointments = database_manager.read_appointments()

                # Assertion
                self.assertEqual(len(appointments), 1)
                self.assertEqual(appointments[0], appointment)

    def test_read_appointment_no_appointments(self):
        # We mock the open function, and the load function of
        # pickle, and we define the behavior we need for this test
        # Using side_effect we specify that the first time pickle
        # should raise an EOFError
        with patch("builtins.open", mock_open(), create=True):
            with mock.patch.object(
                pickle,
                "load",
                side_effect=[EOFError()],
            ):
                # Arrange
                database_manager = DatabaseManager()

                # Action
                appointments = database_manager.read_appointments()

                # Assertion
                self.assertEqual(len(appointments), 0)

    def test_check_user_user_exists(self):
        user_auth = UserAuth("abc", "pass123")

        # We mock the open function, and the load function of
        # pickle, and we define the behavior we need for this test
        # Using side_effect we specify that the first time pickle
        # should return a user_auth object, and the second time
        # it should raise an EOFError
        with patch("builtins.open", mock_open(), create=True):
            with mock.patch.object(
                pickle,
                "load",
                side_effect=[user_auth, EOFError()],
            ):
                # Arrange
                database_manager = DatabaseManager()

                # Action
                user_exists = database_manager.check_user("abc", "pass123")

                # Assertion
                self.assertTrue(user_exists)

    def test_check_user_wrong_password(self):
        user_auth = UserAuth("abc", "pass123")

        # We mock the open function, and the load function of
        # pickle, and we define the behavior we need for this test
        # Using side_effect we specify that the first time pickle
        # should return a user_auth object, and the second time
        # it should raise an EOFError
        with patch("builtins.open", mock_open(), create=True):
            with mock.patch.object(
                pickle,
                "load",
                side_effect=[user_auth, EOFError()],
            ):
                # Arrange
                database_manager = DatabaseManager()

                # Action
                user_exists = database_manager.check_user("abc", "pass1234")

                # Assertion
                self.assertFalse(user_exists)

    def test_check_user_user_does_not_exist(self):
        user_auth = UserAuth("abc", "pass123")

        # We mock the open function, and the load function of
        # pickle, and we define the behavior we need for this test
        # Using side_effect we specify that the first time pickle
        # should return a user_auth object, and the second time
        # it should raise an EOFError
        with patch("builtins.open", mock_open(), create=True):
            with mock.patch.object(
                pickle,
                "load",
                side_effect=[user_auth, EOFError()],
            ):
                # Arrange
                database_manager = DatabaseManager()

                # Action
                user_exists = database_manager.check_user("abcd", "pass123")

                # Assertion
                self.assertFalse(user_exists)
