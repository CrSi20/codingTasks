from datetime import datetime


class Appointment:
    """A class for the appointment"""

    def __init__(self, patient_id: str, doctor_id: str, appointment_datetime: datetime):
        """ Initiates the object.

        Arguments:
            patient_id: str - the patient id
            doctor_id: str - the doctor id
            appointment_datetime: str - appointment date and time
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_datetime = appointment_datetime


class UserAuth:
    """A class for user auth """

    def __init__(self, user_id: str, password: str):
        """ Initiates the object.

        Arguments:
            user_id: str - the user id
            password: str - the password
        """
        self.user_id = user_id
        self.password = password


class Referral:
    """A class for referral"""

    def __init__(self, patient_id: str, doctor_id: str, hospital_id: str):
        """ Initiates the object

        Arguments:
            patient_id: str - the patient id
            doctor_id: str - the doctor id
            hospital_id: str - the hospital id
        """
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.hospital_id = hospital_id
