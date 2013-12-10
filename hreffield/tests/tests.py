#LIBRARIES
from django.core.exceptions import ValidationError
from django.test import TestCase

#HREFFIELD
from hreffield.tests.models import (
    Link,
    Blank,
    CustomProtocols,
    NoFragments,
    NoQueryStrings,
)


class HrefFieldTestCase(TestCase):
    """ Tests for the HrefField. """

    def assertDoesNotRaise(self, exception, kallable, *args, **kwargs):
        try:
            kallable(*args, **kwargs)
        except exception as e:
            self.fail(u"%s raised %s" % (kallable, e))

    def test_default_setup(self):
        link = Link(href="http://www.cake.com/")
        self.assertDoesNotRaise(ValidationError, link.full_clean)
