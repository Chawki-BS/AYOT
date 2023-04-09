

import typer
import whois

app = typer.Typer()


@app.command()
def domain_lookup(name: str):
    """Print the domain resgistrant's name and orgranization"""
    results = whois.whois(name)
    print(f"{name} is registered by {results.name} - {results.org}")


if __name__ == "__main__":
    app()