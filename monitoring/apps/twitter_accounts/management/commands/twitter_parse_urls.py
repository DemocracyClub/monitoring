import json
from collections import Counter

from django.core.management.base import BaseCommand

from twitter_accounts.models import Tweet


class Command(BaseCommand):

    def handle(self, **options):
        ALL_USERNAMES = []
        ALL_URLS = []
        ALL_HASHTAGS = []
        TOP_RTS = {}
        for tweet in Tweet.objects.all():
            raw = json.loads(tweet.raw_data)
            TOP_RTS[raw['text']] = raw.get('retweet_count', 0)
            ALL_USERNAMES.append(raw['user']['screen_name'])
            if 'urls' in raw.keys():
                ALL_URLS += raw.get('urls').values()
            if 'hashtags' in raw.keys():
                ALL_HASHTAGS += raw['hashtags']


        url_count = Counter(ALL_URLS)
        print "TOP URLS:"
        print "\t",
        print "\n\t".join(
            ["%s: %s" % (x[1], x[0]) for x in url_count.most_common(10)]
            )
        print
        print

        user_count = Counter(ALL_USERNAMES)
        print "TOP USERS:"
        print "\t",
        print "\n\t".join(
            ["%s: %s" % (x[1], x[0]) for x in user_count.most_common(10)]
            )
        print
        print


        hashtags_count = Counter(ALL_HASHTAGS)
        print "TOP HASHTAGS:"
        print "\t",
        print "\n\t".join(
            ["%s: %s" % (x[1], x[0]) for x in hashtags_count.most_common(10)]
            )
        print
        print

        top_rts_counter = Counter(TOP_RTS)
        print "TOP RTs:"
        print "\t",
        print "\n\t".join(
            ["%s: %s" % (x[1], x[0]) for x in top_rts_counter.most_common(10)]
            )
        print
        print

