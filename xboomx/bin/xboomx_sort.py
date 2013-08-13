import shelve
import fileinput


def main():
    # open db
    db = shelve.open('~/.xboomx/xboomx.db')

    # read lines and set weight according to db
    items = []

    for input_item in fileinput.input():
        items.append((db.get(input_item, 0), input_item))


    # sort items
    items.sort(key= lambda x: x[0])

    # print items
    for item in items:
        print item[1]

    # clean up
    db.close()




main()
