from pydantic_ai_shared.config import LEARNING_ROOT


def test_learning_root_points_to_learning_dir() -> None:
    assert LEARNING_ROOT.name == "learning"
    assert LEARNING_ROOT.exists()
    assert LEARNING_ROOT.is_dir()
