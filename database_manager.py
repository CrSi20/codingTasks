import pickle
from datetime import datetime
from models import Appointment, UserAuth, Referral
import constants


class DatabaseManager:
    """ Class that allows management of database"""

    def create_appointment(
        self, patient_id: str, doctor_id: str, appointment_datetime: datetime
    ):
        """ Creates an appointment and saves it in a file.

        Arguments:
            - patient_id: str - the patient id
            - doctor_id : str - the doctor id
            - appointment_datetime: datetime - the datetime of the appointment
        """

        # Instantiate an Appointment object
        appointment = Appointment(patient_id, doctor_id, appointment_datetime)

        # Serialization of an appointment and storing it in a file.
        with open(constants.DATABASE_FILE_APPOINTMENTS, "ab") as appointments_file:
            pickle.dump(appointment, appointments_file, pickle.HIGHEST_PROTOCOL)

    def read_appointments(self):
        """Function that allows to retrieve appointments to be read.
            If no file found with appointments then returns an empty list.
            returns - the list of appointments
        """

        list_appointments = []

        try:
            with open(constants.DATABASE_FILE_APPOINTMENTS, "rb") as appointments_file:
                while True:
                    try:
                        appointment = pickle.load(appointments_file)
                        list_appointments.append(appointment)
                    except EOFError:
                        return list_appointments
        except FileNotFoundError:
            return []

    def create_user(self, user_id: str, password: str):
        """ Creates a user and saves it in a file.
        Arguments:
        - user_id: str - the user id
        - password: str - the password
        """

        # Instantiation of user-authentication
        user_auth = UserAuth(user_id, password)

        # Save the user auth object in the file
        with open(constants.DATABASE_FILE_USER_AUTH, "ab") as users_file:
            pickle.dump(user_auth, users_file, pickle.HIGHEST_PROTOCOL)

    def check_user(self, user_id: str, password: str) -> bool:
        """Checks if the user id and password exists in the file.

            Arguments:
            - user_id: str - the user id
            - password: str - the password

            Returns: If the user exists then will return true or if does not
            returns false.
        """

        try:
            with open(constants.DATABASE_FILE_USER_AUTH, "rb") as users_file:
                while True:
                    try:
                        user_auth = pickle.load(users_file)
                        if (
                            user_auth.user_id == user_id
                            and user_auth.password == password
                        ):
                            return True
                    except EOFError:
                        return False

        except FileNotFoundError:
            return False

    def cancel_appointment(self, appointment_number: int) -> None:
        """Cancels an appointment. Retrieves the appointment from
            a file and deletes it.

            Arguments:
            - appointment_number: int - the appointment number
        """

        appointments = self.read_appointments()
        del appointments[appointment_number - 1]
        with open(constants.DATABASE_FILE_APPOINTMENTS, "wb") as appointments_file:
            for appointment in appointments:
                pickle.dump(appointment, appointments_file, pickle.HIGHEST_PROTOCOL)

    def update_appointment(
        self, appointment_number: int, doctor_id: str, appointment_datetime: datetime
    ) -> None:
        """Updates an appointment.

        Arguments:
        - appointment_number: str - the appointment number
        - doctor_id: str - the doctor id
        - appointment_datetime: datetime - the appointment datetime
        """

        appointments = self.read_appointments()

        old_patient_id = appointments[appointment_number - 1].patient_id
        appointments[appointment_number - 1] = Appointment(
            old_patient_id, doctor_id, appointment_datetime
        )

        with open(constants.DATABASE_FILE_APPOINTMENTS, "wb") as appointments_file:
            for appointment in appointments:
                pickle.dump(appointment, appointments_file, pickle.HIGHEST_PROTOCOL)

    def create_referral(self, patient_id: str, doctor_id: str, hospital_id: str):
        """"Creates a referral and saves the referral in a file.

            Arguments:
            - patient_id: str - the patient id
            - doctor_id: str - the doctor id
            - hospital_id : str - the hospital id
        """

        referral = Referral(patient_id, doctor_id, hospital_id)

        with open(constants.DATABASE_FILE_REFERRALS, "ab") as referrals_file:
            pickle.dump(referral, referrals_file, pickle.HIGHEST_PROTOCOL)
