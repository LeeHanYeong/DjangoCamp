from django.http import HttpResponse
from django.shortcuts import render, redirect

from poll.models import Votes, Paper, VoteSelect


def poll_list(request):
    return render(request, 'poll/list.html', context={
        'votes': Votes.objects.all()
    })


def poll_view(request, poll_id):
    vote = Votes.objects.get(id=poll_id)
    return render(request, 'poll/view.html', context={
        'vote': vote
    })


def poll_vote(request, poll_id):
    import django.db.utils
    try:
        Paper.objects.create(
            votes_name=Votes.objects.get(id=poll_id),
            user=request.user,
            votes_select=VoteSelect.objects.get(id=request.GET['item_id'])
        )
    except django.db.utils.IntegrityError:
        return HttpResponse('이미 투표에 참여하셨습니다.')
    return redirect('/polls/%s' % poll_id)
