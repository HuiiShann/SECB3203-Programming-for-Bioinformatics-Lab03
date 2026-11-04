from qc import classify_read, trim_low_quality

def test_classify_read_length_boundary():
    """Test the exact boundary for minimum length (500)."""
    # Exactly 500 should pass
    assert classify_read(length=500, n_count=0, gc=50.0) == "pass"
    # 499 should be rejected immediately
    assert classify_read(length=499, n_count=0, gc=50.0) == "reject"

def test_classify_read_gc_boundary():
    """Test the exact boundary for the maximum GC percentage (70.0)."""
    # Exactly 70.0 is inclusive, so it should pass
    assert classify_read(length=550, n_count=0, gc=70.0) == "pass"
    # 70.1 is just outside the inclusive range, triggering a review
    assert classify_read(length=550, n_count=0, gc=70.1) == "review"

def test_trim_low_quality_exact_threshold():
    """Test that a quality score exactly equal to the threshold is kept, and empty lists are handled."""
    # Score of 20 exactly matches the threshold, so it should NOT be trimmed.
    # [30, 20, 19, 15] -> keeps 30 and 20. Length to keep is 2.
    assert trim_low_quality([30, 20, 19, 15], threshold=20) == 2
    
    # Boundary test for an empty list 
    assert trim_low_quality([]) == 0