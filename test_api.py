import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_create_post():
    new_post = {
        "title": "Мой первый пост",
        "body": "Текст поста",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert data["userId"] == new_post["userId"]
    assert "id" in data


def test_update_post():
    updated_data = {
        "id": 1,
        "title": "Обновлённый заголовок",
        "body": "Новый текст поста",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/1", json=updated_data)

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Обновлённый заголовок"
    assert data["body"] == "Новый текст поста"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code in [200, 204]


def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999")

    assert response.status_code == 404

def test_create_post_without_data():
    response = requests.post(f"{BASE_URL}/posts", json={})
    assert response.status_code != 200