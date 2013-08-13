import shelve
import fileinput
import os


def main():
    # open db
    db = shelve.open(os.getenv("HOME") + '/.xboomx/xboomx.db')

    # read lines and set weight according to db
    items = []

    for input_item in fileinput.input():
        input_item = input_item.strip('\n')
        items.append((db.get(input_item, 0), input_item))


    # sort items
    items.sort(key= lambda x: x[0], reverse=True)

    # print items
    for item in items:
        print item[1]

    # clean up
    db.close()




main()
