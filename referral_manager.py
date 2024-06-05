from database_manager import DatabaseManager


class ReferralManager:
    """ Class that allows a referral to be created."""

    def __init__(self):
        """ Instantiates an object"""
        self.database_manager = DatabaseManager()

    def create_referral(self, patient_id: str, doctor_id: str, hospital_id: str):
        """Creates a referral.

        Arguments:
        - patient_id: str - the patient id
        - doctor_id: str - the doctor id
        - hospital_id: str - the hospital id
        """

        self.database_manager.create_referral(patient_id, doctor_id, hospital_id)
