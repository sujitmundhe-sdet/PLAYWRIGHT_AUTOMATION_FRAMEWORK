import yaml
import pytest

@pytest.fixture(scope='session')
def config():
    with open('testdata/configs/qa.yaml') as f:
        return yaml.safe_load(f)