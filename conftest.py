try:
    import yaml
except ImportError:
    raise ImportError("PyYAML is not installed. Please install it with 'pip install pyyaml'.")
import pytest

@pytest.fixture(scope='session')
def config():
    with open('testdata/configs/qa.yaml') as f:
        return yaml.safe_load(f)