def test_get_words(client):
    response = client.get("/words")
    assert response.status_code == 200

def test_create_word(client):
    response = client.post("/words", json={
        "word": "Flask"
    })
    assert response.status_code == 201
    assert response.json["id"] > 0

def test_delete_word(client):
    response = client.delete("/words", json={
        "word": "Flask"
    })
    assert response.status_code == 200
