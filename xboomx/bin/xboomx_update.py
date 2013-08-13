import shelve
import fileinput
import os


def main():
    # open db
    db = shelve.open(os.getenv("HOME") + '/.xboomx/xboomx.db')

    # get item to update
    item = fileinput.input().next()
    item = item.strip('\n')

    # update item
    db[item] = db.get(item, 0) + 1

    # clean up
    db.sync()
    db.close()


main()
