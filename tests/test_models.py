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
from datetime import datetime
from models import Appointment, UserAuth, Referral


class TestModels(unittest.TestCase):

    def test_appointment(self):
        # Arrange
        # Action
        appointment = Appointment("123", "abc", datetime(2024, 8, 24, 19, 30))

        # Assertion
        self.assertEqual(appointment.patient_id, "123")
        self.assertEqual(appointment.doctor_id, "abc")
        self.assertEqual(
            appointment.appointment_datetime, datetime(2024, 8, 24, 19, 30)
        )

    def test_user_auth(self):
        # Arrange
        # Action
        user_auth = UserAuth("testuser", "abcpass")

        # Assertion
        self.assertEqual(user_auth.user_id, "testuser")
        self.assertEqual(user_auth.password, "abcpass")

    def test_referral(self):
        # Arrange
        # Action
        referral = Referral("123", "abc", "london123")

        # Assertion
        self.assertEqual(referral.patient_id, "123")
        self.assertEqual(referral.doctor_id, "abc")
        self.assertEqual(referral.hospital_id, "london123")
