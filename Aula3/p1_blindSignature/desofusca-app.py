
# desofusca-app.py

"""
Command line app that receives Blind signature, prDashComponents and writes the unblinded signature to STDOUT.
"""

import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python desofusca-app.py -s <Blind Signature> -RDash <pRDashComponents>")

def parseArgs():
    if (len(sys.argv) == 5):
        if(sys.argv[1] == '-s' and sys.argv[3] == '-RDash'):
            main()
        else:
            printUsage()
    else:
        printUsage()

def showResults(errorCode, signature):
    print("Output")
    if (errorCode is None):
        print("Signature: %s" % signature)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")
    elif (errorCode == 2):
        print("Error: blind components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind signature format")

def main():
    blindSignature = sys.argv[2]
    pRDashComponents = sys.argv[4]
    with open('requester.txt', 'rb') as s:
        blindComponents = s.readline()[:-1]
    errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
    showResults(errorCode, signature)

if __name__ == "__main__":
    parseArgs()
