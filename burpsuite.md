  # Burp Suite — Notes

## What it is
Burp Suite is a penetration testing tool used to intercept, inspect, and modify web traffic between the browser and a server.

## Setup
- Install the FoxyProxy extension in the browser.
- Set the proxy port to 8080 (Burp's default).
- Burp also has its own built-in browser — needs a couple of settings enabled to allow it to launch.

## Core workflow
- Turn on intercept to catch a request before it reaches the server.
- From there you can **Forward** (send it on) or **Drop** (kill it).
- Keep intercept **off** when not actively testing — leaving it on makes the browser hang constantly.

## Key tabs
- **Proxy** — where intercepted traffic shows up.
- **Target** — has the site map (shows all requests/responses for a site) and **Scope**, where you paste the specific URL you want to focus on. Setting scope also cleans up the site map by filtering out noise like ads/analytics/CDN traffic.
- **Repeater** — send the same request over and over with manual edits. Used for testing one payload or parameter at a time.
- **Intruder** — automated version of Repeater. Fires many payloads at one spot in a request — used for fuzzing and brute-forcing parameters.
- **Decoder** — encode/decode text (Base64, URL encoding, hex, etc.) — used a lot for reading or crafting payloads.
- **Comparer** — diffs two requests or responses side by side to spot differences.

## Example: testing XSS
Intercepting a request lets you modify it *after* the browser has already applied its own validation — so you can inject payloads (like XSS) that the browser's client-side checks would normally block, and send the modified request straight to the server.

## Key takeaway
Burp sits between you and the target site, letting you see and manipulate every request instead of just what the browser lets you send. That's the whole point of it.
