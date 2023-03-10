from typer.testing import CliRunner

from appModules import cli
from appModules.init import appname,version

cliRunner = CliRunner()

def test_version():
    result = cliRunner.invoke(cli.typerApp, ["--version"])
    assert result.exit_code == 0
    assert f"{appname} v{version}\n" in result.stdout
