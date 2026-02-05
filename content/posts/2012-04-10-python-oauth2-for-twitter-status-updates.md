---
categories:
- Instructional
comments: true
date: 2012-04-10 15:46:08+00:00
slug: python-oauth2-for-twitter-status-updates
tags:
- Python
- Social Media
- Web Development
title: Python + Oauth2 for Twitter Status Updates
---

Working on the [Farset Labs](http://blog.farsetlabs.org.uk) Big Red Button for space occupancy, had to find a simple way to tweet a status. This is a post to remind myself and anyone else who has [dived](https://dev.twitter.com/docs/twitter-libraries#python) through hundreds of incorrect, out of date, or inapplicable examples of Oauth 2 with Twitter using a  pre-generated auth-token pair.


    import oauth2 as oauth
    import urllib

    ckey='$CONSUMER_KEY'
    csecret='$CONSUMER_SECRET'
    akey='$AUTH_TOKEN'
    asecret='$AUTH_SECRET'

    def post_twitter(status):
        try:
            consumer = oauth.Consumer(key=ckey, secret=csecret)
            token = oauth.Token(key=akey, secret=asecret)
            client = oauth.Client(consumer, token)
            resp, content = client.request(
                postapi,
                method='POST',
                body = urllib.urlencode({"status": status,
                                         "wrap_links": True}),
                #headers=http_headers,
                #force_auth_header=True
                )
        except oauth.Error as err:
            print("Twitter Error:"+err)
        return resp, content

    post_twitter("Hello Twitterverse")
