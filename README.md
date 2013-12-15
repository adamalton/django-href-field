django-href-field
=================

Django HrefField - a model field for storing the value of an HTML href attribute


## Spec

`HreField` takes the following keyword arguments:

* `protocols` (iterable) - allows you to specify which protocols are allowed.
  * Defaults to `('http', 'https', 'mailto', 'tel')`.
  * You may add other protocols such as `ftp`, `spotify`, `javascript` or `myownprotocol`.
  * Validators are provided for the default protocols plus `ftp`.  You will need to provide your own validation for other protocols via the `validators` keyword argument.
* `allow_paths` (boolean) - specifies whether protocol-less paths, such as `/` or `/about-us` are allowed.
  * Defaults to `True`.
* `allow_fragments` (boolean) - specifies whether fragment only hrefs such as `#edit` are allowed.
  * Defaults to `True`.
* `allow_query_strings` (boolean)- specifies whether query string-only hrefs such as `?sausage=1` are allowed.
  * Defaults to `True`.

`HrefField` is a subclass of `CharField`, so it exhibits the same behaviour in terms of `blank` and `null`, i.e. it defaults to `""`, so `null=True` is not required unless you specifically want to store `None`.


## Example

```
class Link(models.Model):

    text = models.CharField(max_length=100)

    href = HrefField(
        protocols=('http', 'https', 'mailto'),
        blank=True,
    )
```
