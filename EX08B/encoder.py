import re

def _correct_message(message):
    list = []
    arv = 0
    kood = re.split(r'\s',message)

    kooda = ''.join(kood[0])
    kood1 = re.findall(r'[a-zA-Z]',kooda)
    kood2= ''.join(kood1)
    list.append(kood2)

    return list



if __name__ == '__main__':

    print(_correct_message("H8e%&l6&%l@8095o a@/9^65$n228d w%e60$$#&9l3@/c6o5m3e t2835185$o p$11%/*&&y&17574t9#33/3$&h2o6//30*#4n02, p0#a2l"))