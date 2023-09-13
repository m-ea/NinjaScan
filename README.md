# NinjaScan
A modular tool that scans for subdomains passively.

## Modules:
- Certificate scanner ```-c```
    Identifies subdomains that are associated with unexpired SSL certificates.
- DNS Brute ```-d```
    Specify a wordlist to query DNS resolvers. Careful not to get rate limited.

## Usage:
Edit config.py to specify target domain and wordlist location.
```python ninja.py [options]```

### Options
- ```-c```, ```--certscan``` Activates the certscanner module
- ```-d```, ```--dnsbrute``` Actives the DNS brute module