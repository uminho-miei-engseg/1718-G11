# init-app.py

"""
Command line app that writes initComponents and pRDashComponents to a file.
"""

import sys
from eVotUM.Cripto import eccblind
import os

def printUsage():
    print("Usage:\n Run \"python init-app.py -init\" to generate and save pRDashComponents and initComponents to a file " +
     " followed by \"python init-app.py\" to return pRDashComponents")

def parseArgs():
    if (len(sys.argv) > 1):
            if (sys.argv[1]=="-init"):
                initComponents()
            else:
                printUsage()
    else:
        if (os.path.isfile('./signer.txt')):
            showR()
        else:
            printUsage()

def initComponents():
    initComponents, pRDashComponents = eccblind.initSigner()
    with open('signer.txt', 'w') as signer:
        signer.write(initComponents)
        signer.write('\n')
        signer.write(pRDashComponents)
    print("Components saved!")


def showR():
    with open('signer.txt', 'rb') as s:
       lines = s.readlines();
       pRDashComponents = lines[1]
    print("OUTPUT")
    print("pRDashComponents: %s" % pRDashComponents)

if __name__ == "__main__":
    parseArgs()
