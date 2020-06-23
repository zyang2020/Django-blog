import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category
from django.utils.timezone import utc
# Create your tests here.

class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = 'This is a title'
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)

class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = 'A category'
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)

class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post {} Title".format(count),
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        # get the rendered HTTPResponse for home page request.
        # NOTE:Every test case in a django.test.*TestCase instance has access to
        # an instance of a Django test client. This client can be accessed as
        # self.client. This client is recreated for each test, so you don’t have
        # to worry about state (such as cookies) carrying over from one test
        # to another.
        resp = self.client.get('/')

        # NOTE: the response of self.client.get() has some useful attributes:
        # .content: is the body of the response as a bytestring. We need to decode
        #           it then assertTrue() the decoded content text.
        # .context: is the 'context' we send to the render() function for template
        #           generation. We can retrieve context values using the [] operator.
        #           e.g. response.context['name']
        # .status_code: is the HTTP status of response, as an integer.

        #resp_text = resp.content.decode(resp.charset)
        #self.assertTrue("Recent Posts" in resp_text)
        self.assertContains(resp, 'Recent Posts', count=1)
        for count in range(1, 11):
            title = "Post {} Title".format(count)
            if count < 6:
                # NOTE: self.assertContains() is only for HttpResponse object.
                # it assert if the 'text' is in the response text.
                # 'count=number' means text must occur exactly count times
                # in the response. For non-http object, we should use
                # assertTrue + in to assert if the expected text is in the
                # returned string.
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_detail_only_published(self):
        for count in range(1, 11):
            title = "Post {} Title".format(count)
            post = Post.objects.get(title=title)
            # NOTE: we need to include the '/' in fornt of the 'posts/{}/'
            # to tell the urls.py to find the correct view.
            resp = self.client.get('/posts/{}/'.format(post.pk))
            #resp = self.client.get('localhost:8000/posts/{}/'.format(post.pk))
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
