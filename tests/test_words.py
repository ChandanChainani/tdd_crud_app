def test_get_words(client):
    response = client.get("/words")
    assert response.status_code == 200
