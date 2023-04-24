import requests
import argparse
import os
from rich.console import Console

console = Console()


def main(url, wordlist, user_agent=None, cookie=None, status_code=None, extensions=None, output=None):
    headers = {}
    if user_agent:
        headers["User-Agent"] = user_agent
    if cookie:
        headers["Cookie"] = cookie

    # Varsayılan uzantıları ayarla
    if extensions:
        extensions = extensions.split(",")
    else:
        extensions = [""]

    if output:
        if not os.path.exists(os.path.dirname(output)):
            os.makedirs(os.path.dirname(output))

    try:
        with open(wordlist, "r") as f:
            for line in f.readlines():
                line = line.strip()
                for ext in extensions:
                    target_url = url + "/" + line + ext
                    try:
                        response = requests.get(target_url, headers=headers, verify=True)
                    except requests.exceptions.SSLError:
                        console.print(f"[red]SSL/TLS sertifikası olmadığından {target_url} taranamadı[/red]")
                        continue

                    if status_code:
                        if "," in status_code:
                            codes = status_code.split(",")
                            if str(response.status_code) in codes:
                                console.print(
                                    f"[green][{response.status_code}][/green] == [bold blue]{target_url}[/bold blue]")
                                if output:
                                    with open(output, "a") as f:
                                        f.write(f"[{response.status_code}] == {target_url}\n")
                        else:
                            if response.status_code == int(status_code):
                                console.print(
                                    f"[green][{response.status_code}][/green] == [bold blue]{target_url}[/bold blue]")
                                if output:
                                    with open(output, "a") as f:
                                        f.write(f"[{response.status_code}] == {target_url}\n")
                    else:
                        if response.status_code == 200:
                            console.print(
                                f"[green][{response.status_code}][/green] == [bold blue]{target_url}[/bold blue]")
                            if output:
                                with open(output, "a") as f:
                                    f.write(f"[{response.status_code}] == {target_url}\n")
    except KeyboardInterrupt:
        console.print("[red]Interrupted by user, exiting...[/red]")
        exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advanced Url Scanner Tool',
                                     epilog='''Example Uses:
    python3 url-scanner.py http://example.com/
    python3 url-scanner.py --url http://example.com/ --wordlist /usr/share/dirb/wordlists/common.txt
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --output output.txt
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --status_code 404
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --user_agent <User-Agent> --cookie "sessionid=123456789"
    ''', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url", help="URL to scan")
    parser.add_argument("-w", "--wordlist", help="path to wordlist file",
                        default="/usr/share/dirb/wordlists/common.txt")
    parser.add_argument("-ua", "--user_agent", help="User-Agent header value")
    parser.add_argument("-c", "--cookie", help="Cookie header value")
    parser.add_argument("-s", "--status_code", help="HTTP status code to filter for")
    parser.add_argument("-e", "--extensions", help="file extensions to scan, separated by commas")
    parser.add_argument("-o", "--output", help="file to write results to")
    args = parser.parse_args()

    main(args.url, args.wordlist, args.user_agent, args.cookie, args.status_code, args.extensions, args.output)
