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
def test_password_to_short(client, user, result):
    response = client.post(reverse('registration'), data={**user['data'],
                                                          **user['passwords']})

    assert response.status_code == 400
    assert response.data.serializer.errors['password'][0].code == result



