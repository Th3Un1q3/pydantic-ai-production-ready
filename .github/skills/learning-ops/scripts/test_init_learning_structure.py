import tempfile
from pathlib import Path
from scripts import init_learning_structure as ils


def test_create_and_validate():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "learning"
        # init one module
        mod = ils.create_module(root, "99-test-module", title="Test Module")
        assert (mod / "README.md").exists()
        assert (mod / "exercises").exists()
        # validate
        ok = ils.validate_structure(root)
        assert ok
