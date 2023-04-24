# Advanced Url Scanner


Url-Scanner Name is a powerful and easy-to-use tool for scanning websites to discover hidden directories and files. With a simple command-line interface and a robust set of features, Url-Scanner is the perfect tool for penetration testers, security researchers, and web developers.

## Installation

To install Url-scanner, you can simply clone the repository from GitHub:

```
git clone https://github.com/HalilDeniz/Url-Scanner.git
```

## Requirements

Before you can use Url-Scanner, you need to make sure that you have the necessary requirements installed. You can install these requirements by running the following command:

```
pip install -r requirements.txt
```

## Getting Started

To use Url-Scanner, simply run the following command:

```
python url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt
```

This will start the scan and output the results to the console.

## Help Menu

To see the full list of options and commands for Tool Name, run the following command:

```
python3 main.py --help
usage: main.py [-h] [-w WORDLIST] [-ua USER_AGENT] [-c COOKIE] [-s STATUS_CODE] [-e EXTENSIONS] [-o OUTPUT] url

Port Scan Tool

positional arguments:
  url                   URL to scan

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        path to wordlist file
  -ua USER_AGENT, --user_agent USER_AGENT
                        User-Agent header value
  -c COOKIE, --cookie COOKIE
                        Cookie header value
  -s STATUS_CODE, --status_code STATUS_CODE
                        HTTP status code to filter for
  -e EXTENSIONS, --extensions EXTENSIONS
                        file extensions to scan, separated by commas
  -o OUTPUT, --output OUTPUT
                        file to write results to

Example Uses:
    python3 url-scanner.py http://example.com/
    python3 url-scanner.py --url http://example.com/ --wordlist /usr/share/dirb/wordlists/common.txt
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --output output.txt
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --status_code 404
    python3 url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --user_agent <User-Agent> --cookie "sessionid=123456789"

```

This will display the help menu, which includes information about all of the available options and commands.

## Usage Examples

Here are five different ways that you can use Tool Name:

1. Scan a single website with a custom wordlist:

```
python url-scanner.py --url https://example.com --wordlist /path/to/custom/wordlist.txt
```

2. Scan multiple websites with a default wordlist:

```
python url-scanner.py --url https://example.com https://example.net https://example.org
```

3. Scan a website and save the results to a file:

```
python url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --output /path/to/output.txt
```

4. Scan a website and filter the results by HTTP status code:

```
python url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --status_code 404
```

5. Scan a website with custom HTTP headers:

```
python url-scanner.py --url https://example.com --wordlist /path/to/wordlist.txt --user_agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" --cookie "sessionid=123456789"
```

## Contact

If you have any questions, comments, or suggestions about Tool Name, please feel free to contact me:

- LinkedIn: https://www.linkedin.com/in/halil-ibrahim-deniz/
- TryHackMe: https://tryhackme.com/p/halilovic
- Instagram: https://www.instagram.com/deniz.halil333/
- YouTube: https://www.youtube.com/c/HalilDeniz
- Email: halildeniz313@gmail.com

## License

Tool Name is released under the MIT License. See LICENSE for more information.