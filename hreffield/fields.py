from django.db.models import CharField


DEFALT_PROTOCOLS = ('http', 'https', 'mailto', 'tel')


class HrefField(CharField):

    def __init__(
            self,
            protocols=DEFALT_PROTOCOLS,
            allow_paths=True,
            allow_fragments=True,
            allow_query_strings=True,
            max_length=255,
            **kwargs):
        self.protocols = protocols
        self.allow_paths = allow_paths
        self.allow_fragments = allow_fragments
        self.allow_query_strings = allow_query_strings
        kwargs['max_length'] = max_length
        super(HrefField, self).__init__(**kwargs)


        #TODO - FUNCTIONALITY!

