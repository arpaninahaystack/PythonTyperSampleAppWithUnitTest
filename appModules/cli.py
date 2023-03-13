"""This module provides the CLI."""

from pathlib import Path
from typing import Optional

import typer


typerApp = typer.Typer()

#import app name and version

from appModules import config
from appModules.init import appname,version,SUCCESS ,DIR_ERROR,FILE_ERROR,ERROR
from controller import mainController


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{appname} v{version}")
        raise typer.Exit()
    

@typerApp.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return   

#@typerApp.command()
# def init() -> None:
#     """Initialize """
#     app_init_error = config.init_app()
#     if app_init_error:
#         typer.secho(
#             f'Creating config file failed with "{ERROR}"',
#             fg=typer.colors.RED,
#         )
#         raise typer.Exit(1)
#     else:
#         typer.secho(f"Config file created !!", fg=typer.colors.GREEN)

def result() -> mainController.MainController:
    return mainController.MainController  


@typerApp.command(name="getResult")
def getResult(param: str) -> None:
    data = result()
    res = data.printResult(param)
    if len(res) == 0:
        typer.secho(
            "There are no data to print", fg=typer.colors.RED
        )
        raise typer.Exit()
    else:
       typer.secho(
            "Data available : "+res, fg=typer.colors.GREEN
        ) 


