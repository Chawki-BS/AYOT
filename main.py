

import typer
import whois
import nmap3

app = typer.Typer()


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
        if "open" in port["ports"]:
            print(f"++ {port['portid']} open : {port['service']['name']} >> reason : {port['reason']}")
        elif "closed" in port["ports"]:
            print(f"-- {port['portid']} closed : {port['service']['name']} >> reason : {port['reason']}")


if __name__ == "__main__":
    app()