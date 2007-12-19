# For these tests to run successfully, two conditions must be met:
# 1. MEDIA_URL and MEDIA_ROOT must be set in settings
# 2. The user running the tests must have read/write access to MEDIA_ROOT 

# Unit tests:
from sorl.thumbnail.tests.classes import ThumbnailTest, DjangoThumbnailTest
from sorl.thumbnail.tests.templatetags import ThumbnailTagTest

# Doc tests:
from sorl.thumbnail.tests.utils import utils_tests
__test__ = {
    'utils_tests': utils_tests,
}