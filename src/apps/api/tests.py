from django.test import TestCase
from mixer.backend.django import mixer

from apps.api.models import User


def test_smth(db):
    user = mixer.blend(User)
    assert user.pk == 2