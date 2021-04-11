import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

from .conftest import INCORRECT_PASSWORD_USER


@pytest.mark.django_db
def test_user_registration(client, users_correct_dict):
    model = get_user_model()
    for user in users_correct_dict:
        response = client.post(reverse('registration'), data={**user['data'], **user['passwords']})
        assert model.objects.filter(**response.data).count() == 1


@pytest.mark.parametrize("user, result", INCORRECT_PASSWORD_USER)
@pytest.mark.django_db
def test_user_registration_incorrect_password(client, user, result):
    response = client.post(reverse('registration'), data={**user['data'],
                                                          **user['passwords']})

    assert response.status_code == 400
    assert response.data.serializer.errors['password'][0].code == result


@pytest.mark.django_db
def test_user_authorization(client, user_with_password):
    user, password = user_with_password
    data = {
        'username': user.username,
        'password': password
    }
    response = client.post(reverse('login'), data=data)
    assert response.status_code == 200
    assert 'auth_token' in response.data

@pytest.mark.django_db
def test_user_fail_authorization(client, user_with_password):
    user, password = user_with_password
    data = {
        'username': user.username,
        'password': ""
    }
    response = client.post(reverse('login'), data=data)
    assert response.status_code == 400
    assert response.data.serializer.errors['non_field_errors'][0].code == 'invalid_credentials'
