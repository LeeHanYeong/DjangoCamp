from django.contrib.auth.models import User
from django.db import models

# 안건
class Votes(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    due_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%d. %s' % (self.id, self.title)

# 안건 선택지
class VoteSelect(models.Model):
    votes_name = models.ForeignKey(Votes)   # 안건
    message = models.TextField()

    def get_count(self):
        return self.paper_set.count()

# 투표용지
class Paper(models.Model):
    votes_name = models.ForeignKey(Votes)
    user = models.ForeignKey(User)
    votes_select = models.ForeignKey(VoteSelect)
    # votes_select = models.ManyToManyField(VoteSelect)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('user', 'votes_name'),
        )
