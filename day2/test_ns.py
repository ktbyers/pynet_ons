#!/usr/bin/env python

def my_func(x, y, z=30):
    x = 40
    print "inside my_func"
    print "x: {}".format(x)
    print "y: {}".format(y)
    print "z: {}".format(z)

def my_func2(x, y, z=30):
    x = 40
    print "inside my_func"
    print "x: {}".format(x)
    print "y: {}".format(y)
    print "z: {}".format(z)


def main():
    my_var = 10
    # executable code here
    MY_CONST = 'whatever'
    print "whatever"

if __name__ == "__main__":
    y = 20
    main()
