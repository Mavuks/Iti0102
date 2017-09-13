"""Conversion from row, col => cell index and vice versa."""


def get_cell_index(row, col, row_len):
    """
    Return cell index for row, col and table width.

    Given the row and column indices and the number of columns in the table
    return cell index at the given location.

    :param row: row index
    :param col: column index
    :param row_len: number of columns in the table
    :return: cell index at the given location
    """
    # cell_index = row * row_len + col
    return (row * row_len + col)


def get_row_and_col(cell_index, row_len):
    """
    Return row, col for cell index and table width.

    Given the cell index and the number of columns in the table
    return tuple with row and col indices.

    :param cell_index: cell index
    :param row_len: number of columns in the table
    :return: row index, col index as tuple
    """
    # cell_index = row * row_len + col
    return ((cell_index - (cell_index % row_len)) // row_len), (cell_index % row_len)


def get_row_len(row, col, cell_index):
    """
    Return table width for row, col and cell index.

    Given the row and column indices and the cell index
    return the number of columns in the table.

    If the given setup is not possible
    or it is not possible to deduct column count
    return -1

    :param row: row index
    :param col: column index
    :param cell_index: cell index
    :return: number of columns in the table
    """

    row_len = (cell_index - col) / row
    if row is 0 or ((cell_index - col) / row) < col:
        return -1
    else:
            return row_len


if __name__ == '__main__':

    print(get_cell_index(0, 0, 10))  # => 0
    print(get_cell_index(0, 3, 10))  # => 3
    print(get_cell_index(11, 12, 13))  # => 155

    print(get_row_and_col(3, 2))  # => (1, 1)
    print(get_row_and_col(2, 3))  # => (0, 2)
    print(get_row_and_col(123, 17))  # => (7, 4)

    print(get_row_len(1, 3, 4))  # => -1
    print(get_row_len(1, 0, 3))  # => 3
    print(get_row_len(12, 0, 12))  # => 1