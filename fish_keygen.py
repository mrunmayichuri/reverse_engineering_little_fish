#! /usr/bin/python
#Mrunmayi Churi
#Keygen for http://crackmes.de/users/vik3790/little_fish./

import sys

def generate_key(username):
    C = 0
    m = min(len(username),4)

    for i in range (0, m):
        C |= ord(username[i]) << (3 - i) * 8
    C = (C*15 + 0xFF) & 0xFFFFFFFF
    return "%X" %C

if __name__ == "__main__":

    if len(sys.argv) !=2:
        print "Use the following format: %s username" % sys.argv[0]
        sys.exit(1)

print "The password is: %s" % generate_key(sys.argv[1])






