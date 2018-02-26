# BlindSignature-app.py

"""
Command line app that receives signer's private key from file and Passphrase, Blind message from STDIN,
reads initComponents from signer's file and writes Blind signature to STDOUT.
"""

from eVotUM.Cripto import utils
import sys
from eVotUM.Cripto import eccblind

def printUsage():
    print("Usage: python BlindSignature-app.py -key <private-key> -bmsg <Blind message>")

def parseArgs():
    if (len(sys.argv) == 5):
        if(sys.argv[1] == '-key' and sys.argv[3] == '-bmsg'):
            main()
        else:
            printUsage()
    else:
        printUsage()

def showResults(errorCode, blindSignature):
    if (errorCode is None):
        print("Blind signature: %s" % blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")

def main():
    pemKey = utils.readFile(sys.argv[2])
    print("Input")
    passphrase = raw_input("Passphrase: ")
    blindM = sys.argv[4]
    with open('signer.txt', mode = 'rb') as initFile:
        initComponents = initFile.readline()[:-1]
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM, initComponents)
    showResults(errorCode, blindSignature)

if __name__ == "__main__":
    parseArgs()
