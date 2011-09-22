import os, sys, re

def this_computer_is_running_centos():
    f = open("/etc/redhat-release", "r")
    centos = False
    for line in f.readlines():
        if re.search("CentOS",  line):
            centos = True
            break
    f.close()
    return centos

def mapserv(mapfile, mapserv):
    if os.environ["REQUEST_METHOD"] == "GET":
        if os.environ["QUERY_STRING"] == "":
            QUERY_STRING = "map=%s" % mapfile
        else:
            QUERY_STRING = "map=%s&%s" % (mapfile,os.environ["QUERY_STRING"])
        os.putenv("QUERY_STRING", QUERY_STRING)
        os.execv(mapserv, [])
    elif os.environ["REQUEST_METHOD"] == "POST":
        CONTENT_LENGTH = int(os.environ["CONTENT_LENGTH"])
        QUERY_STRING = sys.stdin.read(CONTENT_LENGTH)
        if QUERY_STRING == "":
            QUERY_STRING = "map=%s" % mapfile
        else:
            QUERY_STRING = "map=%s&%s" % (mapfile,QUERY_STRING)
        os.putenv("QUERY_STRING", QUERY_STRING)
        os.putenv("REQUEST_METHOD", "GET")
        os.execv(mapserv, [])
    else:
        print "I only understand GET or POST requests"
        sys.exit(1)


