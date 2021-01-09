import urllib.request

import click


@click.command()
@click.option("--url", "-ul", prompt="Enter the url: ", help="Check site connection")
def is_internet(url):
    try:
        urllib.request.urlopen(url, timeout=1)
        click.echo("You're connicted")
    except:
        click.echo("You're not connicted")


if __name__ == "__main__":
    is_internet()
