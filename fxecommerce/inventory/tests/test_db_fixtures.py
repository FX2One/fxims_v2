import pytest
from fxecommerce.inventory import models


"""regular parametrize test"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_id, category_name, description, image",
    [
        (1,'football','All equipment related to Sports','default.png')
    ],
)
def test_inventory_category_dbfixture(
  db, django_database_fixture_setup, category_id, category_name, description, image
):
    result = models.Category.objects.get(category_id=category_id)
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image


"""parametrize with FactoryBoy package"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_name, description, image",
    [
        ('football','All football equipment','default.png'),
        ('basketball','All basketball equipment','default.png'),
        ('volleyball','All volleyball equipment','default.png')
    ],
)
def test_inventory_category_dbfixture_insert_fb(
        db, category_factory, category_name, description, image
):
    result = category_factory.create(
        category_name=category_name,
        description=description,
        image=image
    )
    assert result.category_name == category_name
    assert result.description == description
    assert result.image == image

"""parametrize using factory.Sequence to autopopulate not defined field"""
"""parametrize with FactoryBoy package"""
@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "category_name, image",
    [
        ('football','default.png'),
        ('basketball','default.png'),
        ('volleyball','default.png')
    ],
)
def test_inventory_category_dbfixture_insert_fb2(
        db, category_factory, category_name, image
):
    result = category_factory.create(
        category_name=category_name,
        image=image
    )
    print(result.description)
    assert result.category_name == category_name
    assert result.image == image