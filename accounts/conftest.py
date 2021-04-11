import pytest

from django.test import Client


def create_user_dict(number, password, password2=None):
    if password2 is None:
        password2 = password
    return {'data':
                {'username': f'bear_{number}',
                 f'first_name': f"John_{number}",
                 'last_name': f'smith_{number}',
                 'email': f'js_{number}@wp.pl'},
            'passwords':
                {'password': password,
                 'password2': password2}
            }


INCORRECT_PASSWORD_USER = (
    (create_user_dict(0, 'beefbee'), 'password_too_short'),
    (create_user_dict(0, 'temporary'), 'password_too_common'),
    (create_user_dict(0, 'beefbeef', 'beefbeef2'), 'invalid'),
)


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def users_correct_dict():
    users = []
    for i in range(10):
        password = f'beefbeef_{i}!'
        users.append(create_user_dict(i, password))
    return users


@pytest.fixture
def user_password_to_short():
    return create_user_dict(0, 'beefbee')


@pytest.fixture
def user_password_to_common():
    return create_user_dict(0, 'temporary')
