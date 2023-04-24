import requests
import argparse
import os
from rich.console import Console
import urllib3

# Disable insecure cert check
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

console = Console()

def main(args):
    headers = {
        "User-Agent": args.user_agent,
        "Cookie": args.cookie
    }

    # Clean trailing slash
    args.url = args.url.rstrip('/')

    # Get extensions to test
    extensions = [""]

    if args.extensions:
        extensions.extend(args.extensions.split(','))

    # Get status codes to detect (Default 200)
    status_codes = ['200']

    if args.status_code:
        if ',' in args.status_code:
            status_codes.extend(args.status_code.split(','))
        else:
            status_codes = [args.status_code]

    # Create output file if it does not exist
    if args.output and not os.path.exists(args.output):
        with open(args.output, "w"): pass

    try:
        with open(args.wordlist, "r") as f:
            for line in f.readlines():
                line = line.strip()

                for ext in extensions:
                    target_url = args.url + "/" + line + ext

                    response = requests.get(target_url, headers=headers, verify=False)

                    if str(response.status_code) in status_codes:
                        console.print(f"[green][+][/green] [bold blue]{target_url}[/bold blue] ([green]{response.status_code}[/green])")

                        if args.output:
                            with open(args.output, "a") as f:
                                f.write(f"[{response.status_code}] == {target_url}\n")

    except KeyboardInterrupt:
        console.print("[red][-] Interrupted by user, exiting...[/red]")
        exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advanced Url Scanner Tool', epilog='''Example Uses:
    python3 url-scanner.py http://example.com/
    python3 url-scanner.py --url http://example.com/ --wordlist /usr/share/dirb/wordlists/common.txt
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --output output.txt
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --status_code 404
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --user_agent <User-Agent> --cookie "sessionid=123456789"
    ''', formatter_class=argparse.RawDescriptionHelpFormatter)

    # Get arguments
    parser.add_argument("url", help="URL to scan")
    parser.add_argument("-w", "--wordlist", help="path to wordlist file", default="/usr/share/dirb/wordlists/common.txt")
    parser.add_argument("-ua", "--user_agent", help="User-Agent header value")
    parser.add_argument("-c", "--cookie", help="Cookie header value")
    parser.add_argument("-s", "--status_code", help="HTTP status code to filter for")
    parser.add_argument("-e", "--extensions", help="file extensions to scan, separated by commas")
    parser.add_argument("-o", "--output", help="file to write results to")
    args = parser.parse_args()

    main(args)
