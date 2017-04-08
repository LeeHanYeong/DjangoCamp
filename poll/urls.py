from django.conf.urls import url
import poll.views

urlpatterns = [
    # /polls/
    url(r'^$', poll.views.poll_list),
    url(r'^(?P<poll_id>[0-9]+)$', poll.views.poll_view),
    url(r'^(?P<poll_id>[0-9]+)/vote$', poll.views.poll_vote),
]
