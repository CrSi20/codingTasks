""" This is the code for task 18.
    For this task I decided to create an Appointment Manager
    application. The user interface display a menu. To access options
    the user needs to first enter a user id and password. If the
    user details do not exist in the file or password is incorrect,
    then authentication fails and the user cannot access the option.
    The menu also has a register option to create new users.

    I have three classes, AppointmentManager, ReferralManager and
    AuthenticationManager, which are responsible for actions related
    to appointments, referrals and authentication. These classes
    user another class, DatabaseManager to access the data.
    DatabaseManager uses files to write and read appointments, referrals
    and user objects. I have used pickle to write and read objects on files.

    The view of my application is through the UserInterface class.

    I have written unit tests for these functionalities. I have used mocking
    for testing DatabaseManager, as I did not want my test to use real files

"""

from user_interface import UserInterface

if __name__ == "__main__":
    user_interface = UserInterface()
    user_interface.start_application()
