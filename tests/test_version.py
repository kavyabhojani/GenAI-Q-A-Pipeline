from click.testing import CliRunner
from src.main import cli

def test_version_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert "GenAI Q&A Pipeline - Version" in result.output
