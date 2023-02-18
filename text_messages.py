class IntroMessages:
    """Has the welcome and option message."""

    @staticmethod
    def intro_message():
        print("Welcome to the Complaints Register.\n"
                "Underneath you have your option.\n")
    
    @staticmethod
    def chose_admin_or_user_message():
        print("Add a complaint or log in as Admin:")

    @staticmethod
    def option_chose_message():
        print("\n0 = Exit\n"
                "1 = Add a new complaint\n"
                "2 = Log in\n")

    @staticmethod
    def options_admin_message():
        print("\n3 = Log out\n"
                "4 = Add a new Admin\n"
                "5 = View all complaints\n"
                "6 = View the unresolved complaints\n"
                "7 = Change the status for a complaint\n"
                # "8 = Delete complaint\n"
                )


class AdminMessages:
    "Has all the Admin messages"

    @staticmethod
    def log_in_message():
        print("You are now logged in!")

    @staticmethod
    def log_out_message():
        print("You have been logged out!")

    @staticmethod
    def must_log_in_message():
        print("You are not logged in! You have to Log in!")

    @staticmethod
    def must_enter_credentials_message():
        print("Enter a Username and a Password:")
    
    @staticmethod
    def goodbye_message():
        print("Thank you using this app!")


class ComplaintsMessages:
    """Has all the complaints function messages."""

    @staticmethod
    def done_add_new_complaint_message():
        print("Your complaint was added!")
    
    @staticmethod
    def view_all_message():
        print("Here all the complaints made until now:")

    @staticmethod
    def add_new_complaint_message():
        print("Here you can add a new complaint:")

    # @staticmethod
    # def del_complaint_message():
    #     print("Enter the id number of the complaint that you want to delete:\n"
    #             "But remember, once you delete it, you can't undo it!")

    @staticmethod
    def mark_as_resolved_message():
        print("Enter the Id number of the complaint that you have resolved:\n")

    @staticmethod
    def unresolved_complaints_message():
        print("This are the unresolved complaints:")
