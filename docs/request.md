# requests

Requests allows you to send HTTP/1.1 requests extremely easily. Automatic addition of query strings to your URLs, or to form-encode your POST data. It capable of Keep-alive and HTTP connection pooling are automatic.

## Make a Request

Making a request with Requests is very simple. Begin by importing the Requests module:

``` python
import requests
```

Now, let's try to get a webpage. For this example, let's get GitHub's public timeline:

``` python
r = requests.get('https://api.github.com/events')
```

Make an HTTP POST request:

``` python
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
```

Making PUT, DELETE, HEAD and OPTIONS request:

``` python
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
```

## Passing Parameters In URLs

You often want to send some sort of data in the URL's query string.

``` python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
```

## Response Content

The response from the server can be decode to unicode charsets

### Status code

We can check the response status code:

``` python
r = requests.get('https://httpbin.org/get')
r.status_code
```

### Text Response Content

We can read the content of the server's response.

``` python
import requests
r = requests.get('https://api.github.com/events')
r.text
```

### Binary Response Content

You can also access the response body as bytes, for non-text requests:

``` python
r.content
```

### JSON Response Content

There's also a builtin JSON decoder, in case you're dealing with JSON data:

``` python
import requests
r = requests.get('https://api.github.com/events')
r.json()
```

### Raw Response Content

Once you do, you can do this:

``` python
r = requests.get('https://api.github.com/events', stream=True)
r.raw
```

## Custom Headers

If you'd like to add HTTP headers to a request, simply pass in a `dict` to the `headers` parameter.

For example, we didn't specify our user-agent in the previous example:

``` python
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

## More complicated POST requests

### Posting a form

Your dictionary of data will automatically be form-encoded when the request is made:

``` python
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
```

There are times that you may want to send data that is not form-encoded. If you pass in a `string` instead of a `dict`, that data will be posted directly.

For example, the GitHub API v3 accepts JSON-Encoded POST/PATCH data:

``` python
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
```

Instead of encoding the `dict` yourself, you can also pass it directly using the `json` parameter (added in version 2.4.2) and it will be encoded automatically:

``` python
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
```

### POST a Multipart-Encoded File

Requests makes it simple to upload Multipart-encoded files:

``` python
url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text
```

You can set the filename, content_type and headers explicitly:

```python
url = 'https://httpbin.org/post'
>>> files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

>>> r = requests.post(url, files=files)
>>> r.text
```

## Response Headers¶

We can view the server's response headers using a Python dictionary:

    r.headers

## Cookies

If a response contains some Cookies, you can quickly access them:

``` python
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']
```

To send your own cookies to the server, you can use the `cookies` parameter:

``` python
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text
```

## Redirection and History

By default Requests will perform location redirection for all verbs except HEAD. We can use the history property of the Response object to track redirection. The Response.history list contains the Response objects that were created in order to complete the request. The list is sorted from the oldest to the most recent response.

``` python
r = requests.get('http://github.com/')
print(r.url)
print(r.history)
"""output
https://github.com/
[<Response [301]>]
"""
```

If you're using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable redirection handling with the allow_redirects parameter:

``` python
r = requests.get('http://github.com/', allow_redirects=False)
```

If you're using HEAD, you can enable redirection as well:

``` python
r = requests.head('http://github.com/', allow_redirects=True)
```

## Timeouts

You can tell Requests to stop waiting for a response after a given number of seconds with the `timeout` parameter. Nearly all production code should use this parameter in nearly all requests. Failure to do so can cause your program to hang indefinitely:

``` python
requests.get('https://github.com/', timeout=0.001)
```

## Session Objects

The Session object allows you to persist certain parameters across requests.

A Session object has all the methods of the main Requests API.

Let's persist some cookies across requests:

``` python
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
```

Sessions can also be used to provide default data to the request methods. This is done by providing data to the properties on a Session object:

``` python
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
```

# requests_html

This is a package built on top request so all the features available with original request is applicable.

Features of request_html

-   Full JavaScript support!
-   CSS Selectors (a.k.a jQuery-style, thanks to PyQuery).
-   XPath Selectors, for the faint at heart.
-   Mocked user-agent (like a real web browser).
-   Automatic following of redirects.
-   Connection--pooling and cookie persistence.
-   The Requests experience you know and love, with magical parsing abilities.

## Making request

Make a GET request to python.org, using Requests:

``` python
from requests_html import HTMLSession
session = HTMLSession() ## to create a session
r = session.get('https://python.org/')
```

## Finding links

Grab a list of all links on the page, as--is (anchors excluded):

``` python
r.html.links
```

Grab a list of all links on the page, in absolute form

``` python
r.html.absolute_links
```

## CSS selector

Select an Element with a CSS Selector

``` python
about = r.html.find('#about', first=True)
```

Grab an Element's text contents:

``` python
print(about.text)
```

Introspect an Element's attributes

``` python
about.attrs
```

Select an Element list within an Element

``` python
about.find('a')
```

Search for links within an element:

``` python
about.absolute_links
```

You can also select only elements containing certain text:

``` python
r = session.get('http://python-requests.org/')
r.html.find('a', containing='kenneth')
```

## Selecting by text

Search for text on the page:

``` python
r.html.search('Python is a {} language')[0]
```

## Selecting by XPath

XPath is also supported

``` python
 r.html.xpath('a')
```