# Python — Web Scraper (requests + BeautifulSoup)

## What it does
Scrapes quotes.toscrape.com for all quotes and their authors, with proper error handling — a basic recon/OSINT-style script (fetch a page, parse structured data out of it).

## Core flow
1. `requests.get(url, timeout=10)` — fetch the page, with a timeout so it doesn't hang.
2. Check `response.status_code == 200` before doing anything else — don't try to parse a failed response.
3. `BeautifulSoup(html, 'html.parser')` — parse the HTML.
4. `find_all('div', class_="quote")` — get every quote block on the page.
5. Loop through each block, `find()` the quote text and author inside it individually.

## Safety checks
- `try/except requests.exceptions.RequestException` — catches connection errors, not just timeouts.
- `if quotes is not None and authors is not None` — prevents a crash if a block is missing expected data; skips it and prints a message instead of failing.

## Bug I caught and fixed
Originally had `authors = lines.find(...)` sitting inside an unnecessary inner loop. It worked by coincidence (the loop always ran at least once), but wasn't safe — if a block ever had zero children, `authors` would never get defined and the script would crash with a NameError instead of hitting the None-check. Pulled it out to run every time, unconditionally.

## Why this matters for security
Fetch + parse + handle failures gracefully is the base pattern for recon scripting — pulling structured info off pages automatically, without a script crashing the moment it hits one unexpected page.
