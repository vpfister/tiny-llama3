# vim:fenc=utf-8
from click.testing import CliRunner
import tiny_llama3
from tiny_llama3.__main__ import cli


def test_true():
    assert 1 == 1


def test_click_cli():
  runner = CliRunner(mix_stderr=False)
  result = runner.invoke(cli, ['--help'])
  assert result.exit_code == 0
  assert 'Start tiny-llama3 in server mode' in result.output
  assert 'Start tiny-llama3 in server mode' in result.stdout
  assert '' == result.stderr

  result = runner.invoke(cli, ['--version'])
  assert result.exit_code == 0
  assert 'cli, version 0.0.1' in result.output
