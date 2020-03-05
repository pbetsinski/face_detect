from pytest import fixture
from images.images import Images


@fixture(scope='session')
def images():
    images = Images()
    return images
