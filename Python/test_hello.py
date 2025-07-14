from hello import hello

def test_argument():
    for name in ["Alex", "Olga"]:
        assert hello(name) == f"Hello, {name}"

def test_default():
    assert hello() == "Hello, world"
