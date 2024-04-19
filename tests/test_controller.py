from icon_generator import controller

bottts_snippet = '<desc>"Bottts"'


def test_get_file_contents_for_bottts_avatar():
    expected = bottts_snippet
    path = "resources/images/bottts_avatar.svg"
    results = controller.get_file_contents(path)
    assert expected in results


def test_get_file_contents_():
    expected = "QWidget {"
    path = "resources/styles.qss"
    results = controller.get_file_contents(path)
    assert expected in results


def test_call_api_with_default_values():
    expected = "Bottts"
    results = controller.call_api("bottts")
    assert expected in results


def test_call_api_with_seed_for_no_error():
    error_msg = "There was an error"
    results = controller.call_api("bottts", "phred")
    assert error_msg not in results
