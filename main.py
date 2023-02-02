from authentication import add_admin, must_log_in, log_out, IS_ADMIN_LOGGED_IN
from table_function import *
from text_messages import *


EXIT = 0
ADD_COMPLAINT = 1
LOG_IN = 2
LOG_OUT = 3
ADD_ADMIN = 4
VIEW_ALL = 5
VIEW_UNRESOLVED = 6
CHANGE_STATUS_COMPLAINT = 7
DELETE_COMPLAINT = 8
IS_ADMIN_LOGGED_IN = False


while True:
    try:
        IntroMessages.intro_message()
        IntroMessages.chose_admin_or_user_message()
        IntroMessages.option_chose_message()
        option = int(input("Please select the corresponding number:\n"))
        if option == LOG_IN:
            AdminMessages.must_log_in_message()
            IS_ADMIN_LOGGED_IN = must_log_in()
            if IS_ADMIN_LOGGED_IN == True:
                AdminMessages.log_in_message()
                while IS_ADMIN_LOGGED_IN == True:
                    IntroMessages.options_admin_message()
                    option_admin = int(input("What would you like to do?\n"))
                    if option_admin == ADD_ADMIN:
                        AdminMessages.must_enter_credentials_message()
                        add_admin()
                        continue
                    elif option_admin == VIEW_ALL:
                        ComplaintsMessages.view_all_message()
                        view_all_complaints()
                        continue
                    elif option_admin == VIEW_UNRESOLVED:
                        ComplaintsMessages.unresolved_complaints_message()
                        unresolved_complaints()
                        continue
                    elif option_admin == CHANGE_STATUS_COMPLAINT:
                        ComplaintsMessages.mark_as_resolved_message()
                        mark_as_resolved()
                        continue
                    elif option_admin == DELETE_COMPLAINT:
                        ComplaintsMessages.del_complaint_message()
                        delete_complaint()
                        continue
                    elif option_admin == LOG_OUT:
                        AdminMessages.log_out_message()
                        AdminMessages.goodbye_message()
                        log_out()
                        break
            else:
                break
        elif option == ADD_COMPLAINT:
            ComplaintsMessages.add_new_complaint_message()
            add_new_complaint()
        elif option == EXIT:
            exit()
    except ValueError:
        print("Enter a valid option!")
    