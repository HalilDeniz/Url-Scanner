import os
import requests
import argparse
from colorama import init, Fore, Style

class UrlScanner:
    def __init__(self, url, wordlist, user_agent=None, cookie=None, status_code=None, extensions=None, output=None):
        self.url = url
        self.wordlist = wordlist
        self.user_agent = user_agent
        self.cookie = cookie
        self.status_code = status_code
        self.extensions = extensions
        self.output = output
        init(autoreset=True)  # Colorama initialization for automatic reset of color changes
        self.extensions = self.extensions.split(",") if self.extensions else [""]
        if self.output and not os.path.exists(os.path.dirname(self.output)):
            os.makedirs(os.path.dirname(self.output))

    def scan(self):
        try:
            with open(self.wordlist, "r") as f:
                for line in f.readlines():
                    self.scan_word(line.strip())
        except KeyboardInterrupt:
            print(Fore.RED + "Interrupted by user, exiting...")
            exit(0)

    def scan_word(self, word):
        for ext in self.extensions:
            target_url = f"{self.url}/{word}{ext}"
            try:
                response = requests.get(target_url, headers=self.get_headers(), verify=True)
                if response.status_code == 200:
                    self.print_result(response.status_code, target_url)
                    self.save_output(response.status_code, target_url)
            except requests.exceptions.SSLError:
                print(Fore.RED + f"SSL/TLS certificate is missing, cannot scan {target_url}")
                continue
            except requests.exceptions.ConnectionError:
                print(Fore.RED + f"Connection error: {target_url}")
                continue

    def print_result(self, status_code, target_url):
        print(Fore.GREEN + f"[{status_code}] == {target_url}")

    def save_output(self, status_code, target_url):
        if self.output:
            with open(self.output, "a") as f:
                f.write(f"[{status_code}] == {target_url}\n")

    def get_headers(self):
        headers = {}
        if self.user_agent:
            headers["User-Agent"] = self.user_agent
        if self.cookie:
            headers["Cookie"] = self.cookie
        return headers

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advanced URL Scanner Tool')
    parser.add_argument("url", help="URL to scan")
    parser.add_argument("-w", "--wordlist", help="path to wordlist file", default="/usr/share/dirb/wordlists/common.txt")
    parser.add_argument("-ua", "--user_agent", help="User-Agent header value")
    parser.add_argument("-c", "--cookie", help="Cookie header value")
    parser.add_argument("-s", "--status_code", help="HTTP status code to filter for")
    parser.add_argument("-e", "--extensions", help="file extensions to scan, separated by commas")
    parser.add_argument("-o", "--output", help="file to write results to")
    args = parser.parse_args()

    scanner = UrlScanner(args.url, args.wordlist, args.user_agent, args.cookie, args.status_code, args.extensions, args.output)
    scanner.scan()
