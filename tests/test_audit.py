from iotpatch import scan_device

def test_scan():
    report = scan_device("127.0.0.1")
    assert "score" in report
