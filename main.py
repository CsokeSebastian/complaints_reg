from authentication import add_admin, must_log_in, log_out, is_admin_logged_in
from table_function import *
from text_messages import *


exit_app = 0
add_complaint = 1
login = 2
logout = 3
add_new_admin = 4
view_all = 5
view_resolved = 6
change_status_complaint = 7
is_admin_logged_in = False


while True:
    try:
        IntroMessages.intro_message()
        IntroMessages.chose_admin_or_user_message()
        IntroMessages.option_chose_message()
        option = int(input("Please select the corresponding number:\n"))
        if option == login:
            AdminMessages.must_log_in_message()
            is_admin_logged_in = must_log_in()
            if is_admin_logged_in == True:
                AdminMessages.log_in_message()
                while is_admin_logged_in == True:
                    IntroMessages.options_admin_message()
                    option_admin = int(input("What would you like to do?\n"))
                    if option_admin == add_new_admin:
                        AdminMessages.must_enter_credentials_message()
                        add_admin()
                        continue
                    elif option_admin == view_all:
                        ComplaintsMessages.view_all_message()
                        view_all_complaints()
                        continue
                    elif option_admin == view_resolved:
                        ComplaintsMessages.unresolved_complaints_message()
                        unresolved_complaints()
                        continue
                    elif option_admin == change_status_complaint:
                        ComplaintsMessages.mark_as_resolved_message()
                        mark_as_resolved()
                        continue
                    elif option_admin == logout:
                        AdminMessages.log_out_message()
                        AdminMessages.goodbye_message()
                        log_out()
                        break
            else:
                continue
        elif option == add_complaint:
            ComplaintsMessages.add_new_complaint_message()
            add_new_complaint()
            ComplaintsMessages.done_add_new_complaint_message()
        elif option == exit_app:
            exit()
    except ValueError:
        print("Enter a valid option!")
