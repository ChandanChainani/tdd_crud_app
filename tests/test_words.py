def test_get_words(client):
    response = client.get("/words")
    assert response.status_code == 200

def test_create_word(client):
    response = client.post("/words", json={
        "word": "Flask"
    })
    assert response.status_code == 201
