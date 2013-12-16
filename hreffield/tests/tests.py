#LIBRARIES
from django.core.exceptions import ValidationError
from django.test import TestCase

#HREFFIELD
from hreffield.fields import HrefField
from hreffield.tests.models import (
    Link,
    Blank,
    CustomProtocols,
    Paths,
    Fragments,
    QueryStrings,
)


class HrefFieldTestCase(TestCase):
    """ Tests for the HrefField. """

    def assertDoesNotRaise(self, exception, kallable, *args, **kwargs):
        try:
            kallable(*args, **kwargs)
        except exception as e:
            self.fail(u"%s raised %s" % (kallable, e))

    def test_default_setup(self):
        """ Test the validation checks of the default set up. """
        #Check various valid hrefs
        link = Link(href="http://www.cake.com/")
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.href = "https://www.cake.com/"
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.href = "https://www.cake.com/?a=1&b=2"
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.href = "/path/with/no/domain?a=1&b=2"
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.href = "//domain.without.protocol.com/some/path/"
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        #Check various invalid hrefs
        link.href = "javascript:alert('evil');"
        self.assertRaises(ValidationError, link.full_clean)
        link.href = "spotify:open.spotify.com/some/song"
        self.assertRaises(ValidationError, link.full_clean)

    def test_blankness(self):
        """ Test that the `blank` argument dictates the correct behaviour. """
        link = Blank(
            blankable_href="",
            not_blankable_href="http://www.cake.com/",
        )
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.not_blankable_href = ""
        self.assertRaises(ValidationError, link.full_clean)

    def test_custom_protocols(self):
        """ Test that the `protocols` argument does what it should. """
        link = CustomProtocols()
        for protocol in link.protocols:
            link.href = "%s:whatever-la-la-la" % protocol
            self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.href = "abcxyzfesfasc:nonense-la-la-la"
        self.assertRaises(ValidationError, link.full_clean)

    def test_validation_of_custom_protocols(self):
        """ Test that the `protocols` argument does not accept jibberish. """
        self.assertRaises(TypeError, HrefField, protocols=12345) #not iterable
        self.assertRaises(TypeError, HrefField, protocols=["withsemicolon:"])
        self.assertRaises(TypeError, HrefField, protocols=["nonsense$@^"])
        self.assertDoesNotRaise(TypeError, HrefField, protocols=["javascript", "custom"])

    def test_allow_paths(self):
        """ Test that the `allow_paths` argument dictates the correct behaviour. """
        link = Paths(
            allows_paths_href="/some/path/",
            no_paths_href="http://www.domain.com/some/path/",
        )
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.no_paths_href = "/some/path/"
        self.assertRaises(ValidationError, link.full_clean)

    def test_fragments(self):
        """ Test that the `allow_fragments` argument dictates the correct behaviour. """
        link = Fragments(
            allows_fragments_href="#i-am-a-fragment",
            no_fragments_href="http://www.domain.com/#i-am-a-fragment",
        )
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.no_fragments_href = "#i-am-a-fragment"
        self.assertRaises(ValidationError, link.full_clean)

    def test_allow_query_strings(self):
        """ Test that the `allow_query_strings` argument dictates the correct behaviour. """
        link = QueryStrings(
            allows_query_strings_href="?key=value",
            no_query_strings_href="http://www.domain.com/?key=value",
        )
        self.assertDoesNotRaise(ValidationError, link.full_clean)
        link.no_query_strings_href = "?key=value"
        self.assertRaises(ValidationError, link.full_clean)




