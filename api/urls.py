from django.conf.urls import include, url
from api.views import hello_world,list_events,get_event
urlpatterns = [
    # Examples:
    # url(r'^$', 'announce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^events.json', list_events),
    url(r'^hello.json', hello_world),
    url(r'^event/(?P<id>\d+).json', get_event),

]
