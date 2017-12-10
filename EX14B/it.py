
import math
# import rsa

def get_lines(initial_line_length: float) -> tuple:
    """get lines."""
    y = initial_line_length
    x = (3 * y - math.sqrt((3*y)**2 - 4 * y**2)) / 2
    my_tuple = (round(x), round(y-x))
    return my_tuple

# # Install the rsa package before running (Alt+Enter -> Install rsa package)
#
# # Replace the 'X' with a number and run the code
# private_key = rsa.PrivateKey(11205043368821276501164085738541636569880815545177500701989999611690504491774405591277064280887202331871750952739234209459546358927036168630891473248155077,
#                              65537,
#                              1249811053696133958275622423192080249718918498485550607008970461898737931053796295426575931191658930367762111316721305144983323230375280961747441719469353,
#                              6484029691686926333068463978243288890305224164824441508305833690895007755939365483,
#                              1728098713549552126609033130920471853761401423186304421868572898161202319)
#
# print()
#
# mes01 = b'T\xaao\xe9?\x98\xd3.\xbf\x1aF\xdco\x06\xed"*\xa4\x8c\xbf?A\x89#\xa6\x10q\xa4\x80\x90f\xb3\x1e\xa8\xf7M\x14\xe5\xe5\xa62\x9ej\xec\x11\x1b\xea\xa1\x82P\xd6\x89\xe9\x9a~\x8b\xf8n\x0cE\x00\x1b#\xed'
# mes02 = b'W\xe3\xd0\xb4!5H6\xa0\x1e\x19u\xa6\xce\x9c\xd9\x96\x84\xf7\x07b\xe8N@\x90\xbc\xa1\xd4_\x06\x96z\xf1\x18\xf2\xf3|\xe32*\x17\x81\x97P\x8c\x0f\xbe?\xbb!\xf5_\x06\xe15u\x8eX\x89\xe2\xc8U\n\xd6'
#
# # Will print the function names to the console
# print(f"EX02 FUNCTION NAME: {rsa.decrypt(mes01, private_key)}")
# print(f"EX03 FUNCTION NAME: {rsa.decrypt(mes02, private_key)}")


def finder(row, col):
    """fndjsbfj."""

    temp_row = row
    row_sum = 0
    col_sum = 0
    while temp_row > 0 :
        row_sum += temp_row
        temp_row -= 1
    col -= 2
    while col >= 0:
        col_sum += row + col
        col -= 1
    return row_sum + col_sum


def clocky(hour, minute):
    """fdsfds."""

    if hour > 12:
        return -1
    if minute > 59:
        return -1
    nurk1 = 30*hour
    nurk2 = 6*minute
    return abs(nurk1 - nurk2)


if __name__ == '__main__':
    print(get_lines(106042)[1] - 1)
    print(clocky(3, 45))