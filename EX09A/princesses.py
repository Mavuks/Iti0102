"""Generate list of princesses."""

from base64 import b64decode

def read(read_file) -> list:
    """
    Read, decrypt and save information from the given file.

    :param file: the file we read from
    :exception: Exception
    :return: lines
    """
    princesses = []
    try:
        with open("princesses.txt", "r", encoding='utf-8') as file:
            for line in file:
                princesses.append(line.strip())
    except:
        return "File not found"


    return princesses


def decode(line: str) -> str:
    """
    Decode each line.

    Hint: base64.
    :param line: line from the encoded file.
    :return: same decoded line. String.
    """
    return b64decode(line).decode('UTF-8')


def extract_information(line: str) -> list:
    """
    Extract information from each line (without spaces or extra tabulation symbols).

    Example output: ['Helen-elizabeth', 'IN PANIC', 'Ancient Ruins', None]
    Example output: ['Julianne', 'EATEN', 'Heaven', 'Will rule the kingdom'].
    Obviously, she won't rule anything, however. How sad.
    :param line: decrypted line from the file.
    :return: information about single princess
    """
    statuses = [
        "INJURED", "BORED", "EATEN", "SAVED",
        "IN PANIC", "SLAYED THE DRAGON HERSELF",
        "FIGHTS FOR LIFE",
    
        "Dark Cave", "Dungeon", "Old Shack",
        "High Mountain", "Abandoned Prison",
        "Misty Swamp", "Ancient Ruins", "Castle",
        "Pub", "Town Hall", "Office",
        "Library", "Underworld", "Heaven",
    
        "Pretty", "Can cook", "Likes books", "Programmer",
        "Will rule the kingdom", "Afraid of spiders",
        "Sassy", "None"
    ]
    information = []
    information.append(line.split()[0])
    for status in statuses:
        if status in line:
            information.append(status)
    return information





def filter_by_status(lines) -> list:
    """
    Filter out non-relevant statuses.

     Statuses to filter: "EATEN", "SAVED", "SLAYED THE DRAGON HERSELF". There is no point to save those.

    :param lines: lines
    :return: list
    """
    filtered = []
    for i in range(len(lines)):
        if lines[i][1] != "EATEN" and lines[i][1] != "SAVED" and lines[i][1] != "SLAYED THE DRAGON HERSELF":
            filtered.append(lines[i])
    return filtered


def sort_by_status(filtered_lines) -> list:
    """
    Sort lines by pattern FIGHTS FOR LIFE > INJURED > IN PANIC > BORED.

    FIGHTS FOR LIFE comes before INJURED etc.

    :param filtered_lines:
    :return: sorted lines.
    """
    sorted = []
    for i in range(len(filtered_lines)):
        if filtered_lines[i][1] == "FIGHTS FOR LIFE":
            sorted.append(filtered_lines[i])
    for i in range(len(filtered_lines)):
        if filtered_lines[i][1] == "INJURED":
            sorted.append(filtered_lines[i])
    for i in range(len(filtered_lines)):
        if filtered_lines[i][1] == "IN PANIC":
            sorted.append(filtered_lines[i])
    for i in range(len(filtered_lines)):
        if filtered_lines[i][1] == "BORED":
            sorted.append(filtered_lines[i])
    return sorted


def write(read_file):
    """
    Write the sorted lines to the new file 'princesses_to_save.txt'.

    The last princess is NOT followed by a blank line.

    Format:
            Name
            Status
            Place
            Details
            <NEW LINE>
    Example:
            Kathi
            FIGHTS FOR LIFE
            Old Shack
            Sassy
    :param read_file: the file we read from
    :return: None
    """
    with open("princesses_to_save.txt", "w") as file:
        text = sort_by_status(filter_by_status(read(read_file)))
        for line in range(len(text)):
            if text[line] == text[-1]:
                file.write(f'{text[line][0]}')
                for i in range(1, len(text[line])):
                    file.write(f'\n{text[line][i]}')
            else:
                for i in range(len(text[line])):
                    file.write(f'{text[line][i]}\n')
                file.write(f'\n')
        file.close()



if __name__ == '__main__':
    print(decode("TWFybmkgICAgICAgICAgICAgICAgICAgICAgICAgRklHSFRTIEZPUiBMSUZFICAgICAgICAgICAgICAgT2xkIFNo"
                 "YWNrICAgICAgICAgICAgICAgICAgICAgV2lsbCBydWxlIHRoZSBraW5nZG9tCg=="))
    print(extract_information(
        "Marni                         FIGHTS FOR LIFE               Old Shack                     Will rule the kingdom"))
    print(write(read_file))

