def test_get_words(client):
    response = client.get("/words")
    assert response.status_code == 200

def test_create_word_no_parameters(client):
    response = client.post("/words", json={})
    assert response.status_code == 400

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

def test_delete_word_no_parameters(client):
    response = client.post("/words", json={})
    assert response.status_code == 400

def test_update_word(client):
    response = client.put("/words", json={
        "id": 3,
        "word": "Flask App"
    })
    assert response.status_code == 200

def test_update_word_no_parameters(client):
    response = client.put("/words", json={})
    assert response.status_code == 400

def test_get_word_by_id(client):
    response = client.get("/words")
    response = client.get("/words/" + str(response.json[0]["id"]))
    assert response.status_code == 200

def test_get_word_by_id(client):
    response = client.get("/words/abc")
    assert response.status_code == 404
