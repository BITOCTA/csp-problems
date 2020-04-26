from data_loader import load_sudoku


class Sudoku:
    def __init__(self, cells):

        self.cells = cells
        self.domains = {}

        DEFAULT_DOMAIN = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        for i in range(0, len(cells)):
            self.domains[i] = DEFAULT_DOMAIN if self.cells[i] == '.' else {int(self.cells[i])}

    def get_cell(self, row, column):
        index = (row - 1) * 9 + (column - 1)
        if 0 <= index < 81:
            return self.cells[index]
        else:
            raise IndexError

    def used_in_row(self, row, value):
        for i in range(1, 10):
            if self.get_cell(row, i) == str(value):
                return True
        return False

    def used_in_column(self, column, value):
        for i in range(1, 10):
            if self.get_cell(i, column) == str(value):
                return True
        return False

    def used_in_grid(self, grid_number, value):

        if grid_number >= 7:
            row = 7
        elif grid_number >= 4:
            row = 4
        else:
            row = 1

        if grid_number == 1 or grid_number == 4 or grid_number == 7:
            column = 1
        elif grid_number == 2 or grid_number == 5 or grid_number == 8:
            column = 4
        else:
            column = 7

        for i in range(3):
            for j in range(3):
                if self.get_cell(i + row, j + column) == str(value):
                    return True
        return False

    def get_begin_row_col(self, row, col):
        return 7 if row >= 7 else 4 if row >= 4 else 1, 7 if col >= 7 else 4 if col >= 4 else 1

    def get_restricted_values(self, row, col):
        restricted_values = self.get_restricted_column(col).union(self.get_restricted_row(row)).union(
            self.get_restricted_grid(row, col))
        return restricted_values

    def get_restricted_column(self, column):
        restricted_values = set()
        for i in range(1, 10):
            if self.get_cell(i, column) != '.':
                restricted_values.add(self.get_cell(i, column))
        return restricted_values

    def get_restricted_row(self, row):
        restricted_values = set()
        for i in range(1, 10):
            if self.get_cell(row, i) != '.':
                restricted_values.add(self.get_cell(row, i))
        return restricted_values

    def get_restricted_grid(self, row, column):
        row, column = self.get_begin_row_col(row, column)
        restricted_values = set()
        for i in range(3):
            for j in range(3):
                if self.get_cell(i + row, j + column) != '.':
                    restricted_values.add(self.get_cell(i + row, j + column))
        return restricted_values

    def print_grids(self):
        print("-" * 32)
        print("|", end='')
        for i in range(1, 82):
            print(f' {self.cells[i - 1]}', end=' ')
            if i == 81:
                print('|')
                print("-" * 32, end='\n')
            elif i % 27 == 0:
                print('|')
                print("-" * 32, end='\n|')
            elif i % 9 == 0:
                print('|\n', end='|')
            elif i % 3 == 0:
                print('|', end=' ')


a = Sudoku(load_sudoku()[0])
a.print_grids()
print(a.get_restricted_values(8, 9))
