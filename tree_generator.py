import os

my_test = os.walk("HelloWorld", topdown=True)


def list_tree(path_):
    for root, dirs, files in os.walk(path_, topdown=True):
        level = root.replace(path_, '').count(os.sep)
        indent = " " * 4 * level
        print("{}{}/".format(indent, os.path.basename(root)))
        subindent = " " * 4 * (level + 1)
        for f in files:
            my = []
            my.append(f)
            print("{}{}".format(subindent, f))


list_tree("C:\\Users\\abdullrauf.alhariri\\Desktop\\test")
