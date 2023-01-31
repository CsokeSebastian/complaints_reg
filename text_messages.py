class Messages:

    @staticmethod
    def intro_message():
        print("Welcome to the Complaints Register.\n"
                "Underneath you have your option.\n")

    @staticmethod
    def log_in_message():
        print("You are now logged in!")

    @staticmethod
    def log_out_message():
        print("You have been logged out!")

    @staticmethod
    def must_log_in_message():
        print("You are not logged in! You have to Log In!")

    @staticmethod
    def must_enter_credentials():
        print("Enter your username and password:")

    @staticmethod
    def add_new_complaint():
        print("Here you can add a new complaint:")

    @staticmethod
    def del_complaint():
        print("Enter the id number of the complaint that you want to delete:\n")

    @staticmethod
    def mark_as_resolved_message():
        print("Enter the Id number of the task that you have resolved:\n")

    @staticmethod
    def unresolved_complaints_message():
        print("That are the unresolved complaints")
