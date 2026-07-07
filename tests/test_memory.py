from pathlib import Path

from app.memory.memory import Memory


def test_memory_round_trip(tmp_path: Path) -> None:
    file_path = tmp_path / "memory.json"
    store = Memory()
    store.file = str(file_path)
    store.data = {}
    store.save()

    store.remember("profile", "name", "Aeden")
    assert store.recall("profile") == {"name": "Aeden"}

    store.remember("profile", "status", "ready")
    assert store.recall("profile") == {"name": "Aeden", "status": "ready"}
