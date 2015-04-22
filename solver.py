"""
solver.py
Original version by Bruce Eckel
Solves one portion of a problem, in a separate process on a separate CPU
"""
import sys, random, math
from twisted.spread import pb
from twisted.internet import reactor

class Solver(pb.Root):

    def __init__(self, id):
        print "solver.py %s: solver init" % id
        self.id = id

    def remote_initialize(self, initArg):
        return "%s initialized" % self

    # Alias methods, for demonstration version:
    remote_step1 = step


    def remote_status(self):
        print "solver.py %s: remote_status" % self.id
        return "%s operational" % self

if __name__ == "__main__":
    port = int(sys.argv[1])
    reactor.listenTCP(port, pb.PBServerFactory(Solver(sys.argv[1])))
    reactor.run()