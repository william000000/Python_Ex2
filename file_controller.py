"""
File Controller
"""
PART_SEPARATOR = " "
INPUT_FILE_NAME = 'items.txt'


class FileController:
    """
    It includes all operations on these exercise
    """

    def __init__(self):
        self.list_of_data = []

    def load_data(self, file_name: str) -> str:
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

                loaded_obj['sequence'] = int(sequence)
                loaded_obj['size'] = int(size)
                loaded_obj['priority'] = priority

                self.list_of_data.append(loaded_obj)

        except FileNotFoundError:
            pass
        return self.list_of_data

    @staticmethod
    def is_sort_column_valid(sort_column: str) -> bool:
        """
        This check whether input(sort_column) is valid or Not
        :param sort_column:
        :return:
        """
        sort_column = sort_column.lower()
        if sort_column in ('sequence', 'priority', 'size'):
            return True
        return False

    def sort_by_input(self, order_by_desc: str, sort_column: str) -> str:
        """
        This function sort the input
        :param order_by_desc:
        :param sort_column:
        :return:
        """
        order_by_desc = str(order_by_desc)
        sort_column = sort_column.lower()

        if order_by_desc in ('yes', 'y'):
            sorted_data = sorted(self.list_of_data, key=lambda x: x[sort_column], reverse=True)
            self.save_to_file(sort_column, sorted_data)

        else:
            sorted_data = sorted(self.list_of_data, key=lambda x: x[sort_column])
            self.save_to_file(sort_column, sorted_data)

    @staticmethod
    def save_to_file(sort_column: str, data: str):
        """
        It saves data in a specified file accordingly
        :param sort_column:
        :param data:
        :return:
        """
        try:
            file_name = f'order_by_{sort_column}.txt'
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
