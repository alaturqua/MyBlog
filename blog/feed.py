from django.contrib.syndication.views import Feed
from blog.models import Entry

class LatestPosts(Feed):
    title = "MyBlog"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Entry.objects.published()[:5]
