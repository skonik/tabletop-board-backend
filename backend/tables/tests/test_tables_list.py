from datetime import datetime

import pytest
from rest_framework.test import APIClient
from ..models import Table
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model


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
            start_date=datetime.now(),
            game='D&D',
        ),
        Table(
            title="First Monopoly Table",
            description="First ever Monopoly table",
            owner=owner,
            header_image=None,
            start_date=datetime.now(),
            game='Monopoly',
        ),
        Table(
            title="First Arkham Horror Table",
            description="First ever Arkham Horror table",
            owner=owner,
            header_image=None,
            start_date=datetime.now(),
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
    first_table = response.json()['results'][0]

    assert response.status == 200
    assert response.json()['count'] == len(tables)
    assert first_table['title'] == tables[0].title
    assert first_table['description'] == tables[0].description
    assert first_table['owner'] == owner
    assert first_table['header_image'] == tables[0].header_image
    assert first_table['header_image'] == tables[0].header_image
