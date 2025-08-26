import json
from click.testing import CliRunner
from src.main import cli

def test_run_command_json():
    runner = CliRunner()
    result = runner.invoke(cli, ["run", "--query", "What is AI?", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["ok"] is True
    assert "response" in data
    assert "latency_seconds" in data

def test_health_command_json():
    runner = CliRunner()
    result = runner.invoke(cli, ["health", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "pipeline_status" in data
    assert "s3_ok" in data
    assert "version" in data
