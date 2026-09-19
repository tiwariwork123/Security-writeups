# Gobuster — Notes

## What it is
Gobuster is a tool for brute-forcing directories, files, subdomains, and virtual hosts on a web server — used during reconnaissance (gathering info about a target before attacking).

## Core modes
- `gobuster dir -u http://sitename.com -w wordlist.txt` — brute-force directories/files on a target URL.
- `gobuster vhost -u http://sitename.com -w wordlist.txt` — discover virtual hosts on a domain.
- `gobuster dns -d sitename.com -w wordlist.txt` — brute-force subdomains via DNS.

## Useful flags
- `-w` — wordlist (required).
- `--exclude-length 250-320` — filters out responses in that byte range (usually default/junk pages), leaving the real hits easier to spot.
- `-m GET` / `-m POST` — sets HTTP method in dir mode.
- `--help` — lists all available flags when stuck.

## Wordlists
- For directory/subdomain/DNS enumeration, use SecLists wordlists — not rockyou.txt (that's for password cracking, not enumeration). Using the wrong one made a scan take hours instead of minutes when I mixed this up.

## Workflow example
1. Ran gobuster dir against offensivetools.thm, filtered noise with `--exclude-length`, kept responses with status 200.
2. Found a hidden file, used `wget` to download it, then `cat` to read its contents.

## Key takeaway
Match the wordlist to the job — directories need directory wordlists, passwords need password wordlists. Using the wrong one doesn't just fail, it wastes real time.
