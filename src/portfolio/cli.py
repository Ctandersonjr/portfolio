import typer
import uvicorn

from portfolio.database.db import init_table

cli = typer.Typer()


@cli.command()
def init(

) -> None:
    """Initialize table."""
    init_table()
    typer.echo("Table initialized")


@cli.command()
def run(
    host: str = "127.0.0.1",
    port: int = 5432,
    reload: bool = False,
) -> None:
    """Run Fastapi app."""
    uvicorn.run(
        "portfolio.features.routes:app",
        host=host,
        port=port,
        reload=reload,
    )

def main() -> None:
    cli()

if __name__ == "__main__":
    main()
