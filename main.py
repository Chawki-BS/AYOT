import json

import typer
import whois
import nmap3
import requests
from lxml import html
from Wappalyzer import Wappalyzer, WebPage
import json
import pyfiglet
from rich.console import Console

console = Console()

app = typer.Typer()


def print_banner():
    """ Print the banner and the sub banner """
    banner = pyfiglet.figlet_format("# AYOT #", font="big")
    banner_lines = banner.split('\n')
    center_spaces = ' ' * ((console.width - len(banner_lines[0])) // 2)
    console.print(f"[bold green]{center_spaces}{banner_lines[0]}[/bold green]")
    for line in banner_lines[1:]:
        console.print(f"[bold green]{center_spaces}{line}[/bold green]")
    console.print("#" * console.width, style="red")

    def sub_bann(title):
        """ Print the sub banner """
        width = console.width
        padding = (width - len(title)) // 2
        border = "#" * (padding - 1)

        console.print(f"[red]{border}[/red] [bold green]{title}[/bold green] [red]{border}[/red]")

    # Print the sub banner
    sub_bann("Automate Your Own Tools")
    sub_bann(
        "AYOT is a Python-based command-line tool for analyzing web pages and performing various operations such as port scanning, domain lookup, and form analysis")
    sub_bann("Made by Chawki Ben Salem")
    console.print("#" * console.width, style="red")
    print()


print_banner()


def get_page(url: str, proxy: str = None):
    """Perform a GET request and return a response object."""
    proxies = None
    if proxy:
        proxies = {"http": f"http://{proxy}"}
    response = requests.get(url, proxies=proxies)
    return response


@app.command()
def analyze(url: str, proxy: str = None):
    """Analyze page and display framework and versions."""
    response = get_page(url, proxy)
    webpage = WebPage.new_from_response(response)
    wappalyzer = Wappalyzer.latest()
    results = wappalyzer.analyze_with_versions_and_categories(webpage)
    print(json.dumps(results, indent=2))


@app.command()
def is_form(url: str, proxy: str = None):
    """Find a form in a page, and print form details."""
    response = get_page(url, proxy)
    tree = html.fromstring(response.content)
    for form in tree.xpath("//form"):
        print(f"Found a {form.method} form for {form.action}")
        for field in form.fields:
            print(f"Contains input field {field}")


#            choice = input("Would you like to extract data from the form ? (Y / N)")
#            while choice not in ['y','y','N','n']:
#                print("invalid choice")
#                choice = input("Would you like to extract data from the form ? (Y / N)")
#                if choice in ['Y','y']:


@app.command()
def domain_lookup(name: str):
    """Print the domain resgistrant's name and orgranization"""
    results = whois.whois(name)
    print(f"{name} is registered by {results.name} - {results.org}")


@app.command()
def port_scan(target: str, top: int = 10):
    """Perform a port scan against a target on TOP 10 ports
    and print the open ports and services."""
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(target, default=top)
    ip, *_unused = results.keys()
    for port in results[ip]["ports"]:
        if "open" in port["state"]:
            print(f"++ {port['portid']} open : {port['service']['name']} >> reason : {port['reason']}")
        elif "closed" in port["state"]:
            print(f"-- {port['portid']} closed : {port['service']['name']} >> reason : {port['reason']}")


if __name__ == "__main__":
    app()
