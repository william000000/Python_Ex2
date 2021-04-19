"""
My Main App
"""
import sys
import file_controller
INPUT_FILE_NAME = 'items.txt'
TRIAL_NUMBER = 1
IS_SORT_COLUMN_VALID = False

if __name__ == '__main__':
    FileController = file_controller.FileController()
    loaded_data = FileController.load_data(INPUT_FILE_NAME)

    sort_by = input("Which column do you want to sort by? ")
    IS_SORT_COLUMN_VALID = FileController.is_sort_column_valid(sort_by)

    while not IS_SORT_COLUMN_VALID and TRIAL_NUMBER > 0:
        sort_by = input("Please tell us a correct column to sort by? ")
        IS_SORT_COLUMN_VALID = FileController.is_sort_column_valid(sort_by)
        TRIAL_NUMBER = TRIAL_NUMBER - 1

    if not IS_SORT_COLUMN_VALID:
        print("Sorry Try again later")
        sys.exit(1)

    is_desc_order = input("Do you want to sort by descending order? type (yes/y)"
                          " or anything for ascending: ")

    FileController.sort_by_input(is_desc_order, sort_by)
