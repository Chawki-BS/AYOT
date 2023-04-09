import json

import typer
import whois
import nmap3
import requests
from lxml import html
from Wappalyzer import Wappalyzer, WebPage
import json

app = typer.Typer()

def get_page(url: str, proxy: str=None):
    """Perform a GET request and return a response object."""
    proxies = None
    if proxy:
        proxies = {"http": f"http://{proxy}"}
    response = requests.get(url, proxies = proxies)
    return response


@app.command()
def analyze(url :str, proxy :str=None):
    """Analyze page and display framework and versions."""
    response = get_page(url, proxy)
    webpage = WebPage.new_from_response(response)
    wappalyzer = Wappalyzer.latest()
    results = wappalyzer.analyze_with_versions_and_categories(webpage)
    print(json.dumps(results, indent=2))


@app.command()
def is_form(url: str, proxy: str=None):
    """Find a form in a page, and print form details."""
    response = get_page(url,proxy)
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
def port_scan(target: str, top: int=10):
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