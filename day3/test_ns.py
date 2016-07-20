#!/usr/bin/env python

def func1(x, y):
    print x
    print y
    print locals()

def main():
    print __name__
    x = 10
    y = 20
    z = 30
    
    func1(1, 2)
    
    print x
    print y
    print z
    
if __name__ == "__main__":
    main()
