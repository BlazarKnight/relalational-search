"""
Command-line interface for relational-search.
"""
import click
@click.command()
def main():
    """Run the relational-search tool."""
    click.echo("relational-search CLI is running!")
if __name__ == "__main__":
    main()
