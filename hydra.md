# Hydra — Notes

## What it is
Hydra is a brute-force tool used to crack login credentials by testing combinations against a target service (SSH, FTP, RDP, HTTP forms, etc.).

## Core logic
Three scenarios depending on what you know:
- Known username, unknown password → use a password list against it.
- Known password, unknown username → use a username list against it.
- Neither known → use a common username list against a common password list (most realistic real-world case).

## Key flags
- `-l` (lowercase) — a single, exact username.
- `-L` (uppercase) — a file containing a list of usernames.
- `-p` (lowercase) — a single, exact password.
- `-P` (uppercase) — a file containing a list of passwords.
- `-t <number>` — number of threads (parallel attempts), e.g. `-t 4`.
- `-V` — verbose mode, shows each attempt live instead of running silently.

## Example commands
- SSH: `hydra -l root -P passwords.txt ssh://10.0.2.5 -V`
- FTP: `hydra -l root -P passwords.txt ftp://10.0.2.5 -V`
- RDP: `hydra -V -f -L usernames.txt -P passwords.txt rdp://10.0.2.5`

The protocol (`ssh://`, `ftp://`, etc.) goes at the end — it tells Hydra which service to attack.

## Key takeaway
Hydra is only as good as the lists you feed it — a weak or mismatched wordlist wastes time or misses the real credentials entirely (same lesson learned the hard way with Gobuster and rockyou.txt).
