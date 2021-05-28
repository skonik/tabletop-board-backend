import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from ..models import Table


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def owner():
    user = get_user_model().objects.create_user(
        username='tester',
        email='tester',
    )

    return user


@pytest.mark.django_db
@pytest.fixture
def tables(owner):
    tables = [
        Table(
            title="First D&D Table",
            description="First ever D&D table",
            owner=owner,
            header_image=None,
            start_date=timezone.now(),
            game='D&D',
        ),
        Table(
            title="First Monopoly Table",
            description="First ever Monopoly table",
            owner=owner,
            header_image=None,
            start_date=timezone.now(),
            game='Monopoly',
        ),
        Table(
            title="First Arkham Horror Table",
            description="First ever Arkham Horror table",
            owner=owner,
            header_image=None,
            start_date=timezone.now(),
            game='Arkham Horror',
        ),
    ]
    Table.objects.bulk_create(tables)

    return tables


@pytest.fixture
def list_endpoint_url():
    return reverse('tables-list')


@pytest.mark.django_db
def test_list_tables_api(tables, api_client, list_endpoint_url, owner):
    response = api_client().get(
        list_endpoint_url,
    )
    first_item = response.json()['results'][0]
    first_table = tables[0]

    assert response.status_code == 200
    assert response.json()['count'] == len(tables)
    assert first_item['title'] == first_table.title
    assert first_item['description'] == first_table.description
    assert first_item['owner'] == owner.id
    assert first_item['header_image'] == first_table.header_image
    assert first_item['game'] == first_table.game
    assert parse_datetime(first_item['start_date']) == first_table.start_date
