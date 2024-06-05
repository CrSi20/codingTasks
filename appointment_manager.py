from datetime import datetime
from database_manager import DatabaseManager


class AppointmentManager:
    """ Class that allows management of appointments."""

    def __init__(self):
        """Instantiates an object:
        """
        self.database_manager = DatabaseManager()

    def create_appointment(
        self, patient_id: str, doctor_id: str, appointment_datetime: datetime
    ):
        """Creates an appointment.

        Arguments:
        - patient_id: str - the patient id
        - doctor_id: str - the doctor id
        - appointment_id: datetime -  appointment date and time
        """
        self.database_manager.create_appointment(
            patient_id, doctor_id, appointment_datetime
        )

    def print_appointment(self):
        """Prints the appointments.
        """
        appointments = self.database_manager.read_appointments()

        if (len(appointments) == 0):
            print("There are no appointments.")

        for index, appointment in enumerate(appointments):

            print(
                f"{index + 1}. Appointment for patient {appointment.patient_id}",
                f" with doctor {appointment.doctor_id}",
                f" at {appointment.appointment_datetime}\n",
            )

    def cancel_appointment(self, appointment_number: int) -> None:
        """Cancels an appointment

        Arguments:
        - appointment_number: int - the appointment number
        """

        self.database_manager.cancel_appointment(appointment_number)

    def update_appointment(self, appointment_number: int, doctor_id: str, appointment_datetime: datetime) -> None:
        """Updates an appointment.

        Arguments:
        - appointment_number: int - the appointment number
        - doctor_id: str - the doctor id
        - appointment_datetime: datetime - appointment date and time
        """

        self.database_manager.update_appointment(appointment_number, doctor_id, appointment_datetime)
