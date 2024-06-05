from appointment_manager import AppointmentManager
from authentication_manager import AuthenticationManager
from datetime import datetime
from referral_manager import ReferralManager


class UserInterface:
    """ A class for displaying a menu, allowing the user login and
        managing appointments and creating referrals.
    """

    def __init__(self):
        """ Initialise appointment_manager, authentication manager
            and referral manager.
        """
        self.appointment_manager = AppointmentManager()
        self.authentication_manager = AuthenticationManager()
        self.referral_manager = ReferralManager()

    def start_application(self):
        """" Displays a menu to the user"""

        while True:
            print()
            print("Welcome to the Appointment Manager application.")
            print()

            print("1. View appointments")
            print("2. Create an appointment")
            print("3. Cancel appointment")
            print("4. Update appointment")
            print("5. Create referral")
            print("6. Register user")
            print("7. Quit")
            print()

            choice = input("Enter your choice: ")
            print()
            if choice == "1":
                result = self.login()
                if result:
                    self.appointment_manager.print_appointment()
                else:
                    print("Sorry, authentication failed")

            elif choice == "2":
                result = self.login()
                if result:
                    self.create_appointment()
                else:
                    print("Sorry, authentication failed")

            elif choice == "3":
                result = self.login()
                if result:
                    self.cancel_appointment()
                else:
                    print("Sorry, authentication failed")

            elif choice == "4":
                result = self.login()
                if result:
                    self.update_appointment()
                else:
                    print("Sorry, authentication failed")

            elif choice == "5":
                result = self.login()
                if result:
                    self.create_referral()
                else:
                    print("Sorry, authentication failed")

            elif choice == "6":
                self.register_user()

            elif choice == "7":
                break

            else:
                print("Invalid choice. Please try again.")
                print()

    def login(self) -> bool:
        """ Allows the user to verify if the user_id and
            passwords are correct.
            If correct returns True otherwise False
        """
        user_id = input("Please enter you user id: ")
        password = input("Please enter your password: ")
        print()
        return self.authentication_manager.authenticate_user(user_id, password)

    def create_appointment(self):
        """ Allows the user to enter the details
        to create an appointment.
        """
        patient_id = input("Please enter your patient id: ")
        doctor_id = input("Please enter your doctor id: ")
        year = int(input("Please enter the year: "))
        month = int(input("Please enter the month: "))
        day = int(input("Please enter the day: "))
        hour = int(input("Please enter the hour: "))
        minutes = int(input("Please enter the minutes: "))
        self.appointment_manager.create_appointment(
            patient_id, doctor_id, datetime(year, month, day, hour, minutes)
        )

    def register_user(self):
        """Allows the user to register.
        Asks the user to re-enter password to confirm that it
        is correct.
        """
        user_id = input("Please enter you user id: ")
        password = input("Please enter your password: ")
        password2 = input("Please enter your password again: ")
        if password == password2:
            self.authentication_manager.create_user(user_id, password)
        else:
            print("\nThe passwords do not match.")

    def cancel_appointment(self):
        """Allows the user to cancel appointment."""
        self.appointment_manager.print_appointment()
        appointment_number = int(input("Please select an appointment to cancel: "))
        self.appointment_manager.cancel_appointment(appointment_number)

    def update_appointment(self):
        """Allows the user to update an appointment."""
        self.appointment_manager.print_appointment()
        appointment_number = int(input("Please select an appointment to update: "))
        doctor_id = input("Please enter your doctor id: ")
        year = int(input("Please enter the year: "))
        month = int(input("Please enter the month: "))
        day = int(input("Please enter the day: "))
        hour = int(input("Please enter the hour: "))
        minutes = int(input("Please enter the minutes: "))
        self.appointment_manager.update_appointment(
            appointment_number, doctor_id, datetime(year, month, day, hour, minutes)
        )

    def create_referral(self):
        """Allows the user to create a referral."""
        patient_id = input("Please enter your patient id: ")
        doctor_id = input("Please enter your doctor id: ")
        hospital_id = input("Please enter your hospital id: ")
        self.referral_manager.create_referral(patient_id, doctor_id, hospital_id)
