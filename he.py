import click
import requests


@click.command()
@click.option("--url", "-ul", prompt="Url to ckeck: ", help="Enter the url that you want to see its status code", type=str)
def check_url(url):
    respons = requests.get(url)
    click.echo(respons.status_code)

    if respons.status_code == 200:
        click.echo("Your request is good 200")

    elif respons.status_code == 400:
        click.echo("Your request is bad 400")

    elif respons.status_code == 401:
        click.echo("Your request is Unauthorized 401")


if __name__ == "__main__":
    check_url()
