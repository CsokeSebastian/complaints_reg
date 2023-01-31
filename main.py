from authentication import *
from table_function import *
from text_messages import *


EXIT = 0
LOG_IN = 1
LOG_OUT = 2
ADD_USER = 3
ADD_COMPLAINT = 4
VIEW_ALL = 5
CHANGE_STATUS_COMPLAINT = 6
DELETE_COMPLAINT = 7
IS_USER_LOGGED_IN = False
IS_ADMIN_LOGGED_IN = False



print("EXIT = 0\n"
"LOG_IN = 1\n"
"LOG_OUT = 2\n"
"ADD_USER = 3\n"
"ADD_COMPLAINT = 4\n"
"VIEW_ALL = 5\n"
"CHANGE_STATUS_COMPLAINT = 6\n"
"DELETE_COMPLAINT = 7\n")

try:
    while True:
        option = int(input("Please select the corresponding number:\n"))
        if option == 1:
            must_log_in(IS_USER_LOGGED_IN)
            if option == 4:
                add_new_complaint()
            elif option == 2:
                log_out(IS_USER_LOGGED_IN)
                break
        elif option == 3:
            add_user()
        elif option == 4:
            add_new_complaint()
        elif option == 5:
            view_all_complaints()
        elif option == 6:
            mark_as_resolved()
        elif option == 7:
            delete_complaint()
        elif option == 2:
            log_out(IS_USER_LOGGED_IN)
            break
except ValueError:
    print("Enter a valid option")


