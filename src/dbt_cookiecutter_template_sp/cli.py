"""Console script for dbt_cookiecutter_template_sp."""
import dbt_cookiecutter_template_sp

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for dbt_cookiecutter_template_sp."""
    console.print("Replace this message by putting your code into "
               "dbt_cookiecutter_template_sp.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
