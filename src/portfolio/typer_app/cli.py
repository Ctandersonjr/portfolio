import typer
import uvicorn

from typer_app.db import init_table

cli = typer.Typer()

@cli.command()
def init(

) -> None:
    """Initialize table"""
    init_table()
    typer.echo("Table initialized")

@cli.command()
def run(
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True,
) -> None:
    """Run Fastapi app"""
    uvicorn.run(
        "typer_app.main:app",
        host=host,
        port=port,
        reload=reload,
    )

def main() -> None:
    cli()

if __name__ == "__main__":
    main()