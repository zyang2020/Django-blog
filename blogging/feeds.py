# feeds.py
from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestPostsFeed(Feed):
    title = 'Blog Posts'
    link = ''
    description = 'Updates on new posts'

    def items(self):
        return Post.objects.order_by('-published_date')

    def item_title(self, item):
        return item.title

    def item_descripiton(self, item):
        return item.description

    # have already added the get_absolute_url() in Post model.
    # so we don't need the following 'item_link()' method.
    #def item_link(self, item):
    #    return reverse('blog_detail', args=[item.pk])
