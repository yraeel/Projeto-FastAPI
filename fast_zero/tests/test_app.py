from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Ola mundo'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testuser',
            'password': 'password',
            'email': 'email@email.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'testuser',
        'email': 'email@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testuser',
                'email': 'email@email.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '',
            'username': 'testuser2',
            'email': 'email@email.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testuser2',
        'email': 'email@email.com',
        'id': 1,
    }


def delete_update_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
