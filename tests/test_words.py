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

def test_create_word_html(client):
    response = client.post("/words", json={
        "word": "<b>Flask</b>"
    })
    assert response.status_code == 201
    response = client.get("/words/" + str(response.json["id"]))
    assert response.json['name'] == '&lt;b&gt;Flask&lt;/b&gt;'

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

def test_update_word(client):
    word_id = 3
    response = client.put("/words", json={
        "id": word_id,
        "word": "<div>Flask App</div>"
    })
    response = client.get("/words/" + str(word_id))
    assert response.status_code == 200
    assert response.json['name'] == '&lt;div&gt;Flask App&lt;/div&gt;'

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
