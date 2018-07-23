from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testingg

def test_hello():
    response = client.get("/hello")
    assert response.data == b"Hello, World!"
