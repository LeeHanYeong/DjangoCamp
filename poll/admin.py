from django.contrib import admin
from poll.models import Votes, VoteSelect, Paper

admin.site.register(Votes)
admin.site.register(VoteSelect)
admin.site.register(Paper)
