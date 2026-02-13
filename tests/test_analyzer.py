import pytest
from src.analyzer import LogAnalyzer

def test_analyze_counts_errors_correctly(tmp_path):
    """
    Test that the analyzer correctly counts ERROR messages and ignores INFO/WARN.
    Uses 'July' to verify regex support for full month names.
    """
    # Create a temporary log file
    log_file = tmp_path / "test.log"
    log_content = (
        "July 31 16:00:00 host app[123]: INFO Started\n"
        "July 31 16:01:00 host app[123]: ERROR Connection failed\n"
        "July 31 16:02:00 host app[123]: WARN High memory\n"
        "July 31 16:03:00 host app[123]: ERROR Connection failed\n"
        "July 31 16:04:00 host app[123]: ERROR Database timeout\n"
    )
    log_file.write_text(log_content, encoding="utf-8")

    # Initialize analyzer with the temp file
    analyzer = LogAnalyzer(str(log_file))
    analyzer.analyze()

    # Get top errors
    top_errors = analyzer.get_top_errors()

    # Assertions
    assert len(top_errors) == 2, "Should find exactly 2 unique error types"
    
    # Check "Connection failed" count (should be 2)
    assert top_errors[0] == ("Connection failed", 2)
    
    # Check "Database timeout" count (should be 1)
    assert top_errors[1] == ("Database timeout", 1)

def test_file_not_found_exception():
    """
    Test that the analyzer raises FileNotFoundError for non-existent files.
    """
    analyzer = LogAnalyzer("non_existent_file.log")
    
    with pytest.raises(FileNotFoundError):
        analyzer.analyze()

def test_empty_log_file(tmp_path):
    """
    Test that the analyzer handles empty files gracefully.
    """
    log_file = tmp_path / "empty.log"
    log_file.write_text("", encoding="utf-8")

    analyzer = LogAnalyzer(str(log_file))
    analyzer.analyze()

    assert len(analyzer.get_top_errors()) == 0