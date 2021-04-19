"""
File Controller
"""
PART_SEPARATOR = " "
INPUT_FILE_NAME = 'items.txt'
ORDER_BY_SIZE_FILE = 'order_by_size.txt'
ORDER_BY_SEQUENCE_FILE = 'order_by_sequence.txt'
ORDER_BY_PRIORITY_FILE = 'order_by_priority.txt'


class FileController:
    """
    It includes all operations on these exercise
    """

    def __init__(self):
        self.list_of_data = []

    def load_data(self, file_name):
        """
        Load all data from items.txt
        :param file_name:
        :return:
        """
        try:
            with open(file_name, 'r') as result_file:
                datafile = result_file.readlines()
            for line in datafile:
                loaded_obj = {}
                row = line.strip().split(PART_SEPARATOR)
                sequence = row[0].strip()
                size = row[1].strip()
                priority = row[2].strip()

                if priority == 'LOW':
                    priority = 0
                if priority == 'MEDIUM':
                    priority = 1
                if priority == 'HIGH':
                    priority = 3

                loaded_obj['sequence'] = sequence
                loaded_obj['size'] = size
                loaded_obj['priority'] = priority

                self.list_of_data.append(loaded_obj)

        except FileNotFoundError:
            pass
        return self.list_of_data

    @staticmethod
    def is_sort_column_valid(sort_column):
        """
        This check whether input(sort_column) is valid or Not
        :param sort_column:
        :return:
        """
        sort_column = sort_column.lower()
        if sort_column in ('sequence', 'priority', 'size'):
            return True
        return False

    def sort_by_input(self, order_by_desc: str, sort_column: str):
        """
        This function sort the input
        :param order_by_desc:
        :param sort_column:
        :return:
        """
        order_by_desc = str(order_by_desc)
        if order_by_desc in ('yes', 'y'):
            sorted_data = sorted(self.list_of_data, key=lambda x: x[sort_column], reverse=True)
            self.save_to_file(sort_column, sorted_data)

        else:
            sorted_data = sorted(self.list_of_data, key=lambda x: x[sort_column])
            self.save_to_file(sort_column, sorted_data)

    @staticmethod
    def save_to_file(sort_column, data):
        """
        It saves data in a specified file accordingly
        :param sort_column:
        :param data:
        :return:
        """
        try:
            if sort_column == 'sequence':
                file_name = ORDER_BY_SEQUENCE_FILE
            if sort_column == 'size':
                file_name = ORDER_BY_SIZE_FILE
            if sort_column == 'priority':
                file_name = ORDER_BY_PRIORITY_FILE

            with open(file_name, 'w') as final_file:
                for obj in data:
                    sequence = obj['sequence']
                    size = obj['size']
                    priority = obj['priority']
                    if priority == 0:
                        priority = 'LOW'
                    if priority == 1:
                        priority = 'MEDIUM'
                    if priority == 3:
                        priority = 'HIGH'

                    line = f'{sequence} {size} {priority} \n'
                    final_file.write(line)
        except FileNotFoundError:
            pass
        return True
