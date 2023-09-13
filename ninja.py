import argparse
import modules.certscanner as certscanner
import modules.dnsbrute as dnsbrute

parser = argparse.ArgumentParser(description='Find subdomains passively')
parser.add_argument('-c', '--certscan', action='store_true', required=False, help='Look for subdomains associated with valid SSL certificates')
parser.add_argument('-d', '--dnsbrute', action='store_true', required=False, help='Brute force a wordlist against DNS looking for subdomains. Be careful about rate limiting.')
args = parser.parse_args()

if args.certscan == True:
    certscanner.CertScanner()

if args.dnsbrute == True:
    dnsbrute.DnsBrute()