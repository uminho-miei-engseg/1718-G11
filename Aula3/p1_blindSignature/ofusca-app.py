# ofusca-app.py
######################################################################
"""
Command line app that receives the message to sign, the pRDashComponents, writes
blindMessage to STDOUT and saves blindComponents and pRComponents in a file called requester.txt
"""

import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage:\n > python ofusca-app.py -msg <message to sign> -RDash <pRDashComponents>")

def parseArgs():
    if (len(sys.argv) == 5):
        if(sys.argv[1] == '-msg' and sys.argv[3] == '-RDash'):
            main()
        else:
            printUsage()
    else:
        printUsage()

def saveComponents(blindComponents, pRComponents):
    with open('requester.txt', 'w') as r:
        r.write(blindComponents)
        r.write('\n')
        r.write(pRComponents)

def showResults(errorCode, result):
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        saveComponents(blindComponents, pRComponents)
        print("Components saved!")
        print("Blind message: %s" % blindM)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main():
    data = sys.argv[2]
    pRDashComponents = sys.argv[4]
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)

if __name__ == "__main__":
    parseArgs()
