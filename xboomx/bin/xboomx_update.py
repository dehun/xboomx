import shelve
import fileinput


def main():
    # open db
    db = shelve.open('~/.xboomx/xboomx.db')

    # get item to update
    item = fileinput.input().next()

    # update item
    db[item] = db.get(item, 0) + 1

    # clean up
    db.sync()
    db.close()


main()
