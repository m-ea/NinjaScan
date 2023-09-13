import dns.resolver
import config

def DnsBrute():
    # Build the wordlist
    wordlist = []
    with open(config.wordlist_file, 'r') as f:
        for line in f:
            wordlist.append(line[:-1])

    # Resolve the DNS query
    answers = []
    for sub in wordlist:
        try:
            answers.append(dns.resolver.resolve(sub + '.' + config.domain, 'cname', raise_on_no_answer=False))
        except dns.resolver.NXDOMAIN:
            continue

    # Print results
    for answer in answers:
        print(answer.canonical_name)

if "__name__" == "__main__":
    DnsBrute()