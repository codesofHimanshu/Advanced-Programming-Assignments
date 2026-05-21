import pytest
from score_processor import ScoreProcessor


def test_process_score_file_success(tmp_path):
    # Create a temporary valid file
    file = tmp_path / "score.txt"
    file.write_text("5")

    processor = ScoreProcessor()

    result = processor.process_score_file(str(file))

    assert result == 50


def test_process_score_file_missing():
    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing_file.txt")