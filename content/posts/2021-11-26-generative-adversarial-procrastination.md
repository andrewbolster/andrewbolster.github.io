---
aliases:
- /2021/11/generative-adversarial-procrastination/
- /2021/11/generative-adversarial-procrastination.html
cover:
  image: img/generative-adversarial-procrastination.generated.png
date: 2021-11-26 15:07:00+00:00
tags:
- Data Science
- Machine Learning
- Productivity
title: Generative Adversarial Procrastination
---
_TL:DR "Don't worry about being a procrastinator, just make sure that your procrastinations are worthwhile."_

There's an implicit irony in this post that I've been thinking / talking about writing it for at least 6 months, and it finally came down to a [tweet](https://twitter.com/Bolster/status/1464233419714568198?s=20) to force me to do it.

> Fun fact, in the time it took for me to write this procrastination post, the twitter poll changed, so I guess I gotta delete it all and play Satisfactory now?

I'm a procrastinator. Ridiculously so. To a degree that my procrastination at the moment is procrastination from procrastinating. To misquote a misquote from the New York Times; "It's Procrastination all the way down".

However, I'm still surprisingly productive in my own way; I've contributed to the operation of numerous charities, side projects, talks, meetups, guest lecture series; spent a load of time on deep background to local journalists who end up out of their depth in the stranger parts of the tech world; did a masters project on a 36 hour sleep cycle, and a 3 year PhD in 5 years, still play the Start-Up game every so often (or, at least, the fun bit of setting the world to rights in the bar with a few friends / colleagues convinced that we've got an idea that will change the world), and still faff around with a load of hardware and home automation stuff (that never seems to work for long)...

So I'm a workaholic right? Christ no. This morning I got out of bed at around noon after getting caught up on [BlindBoy](https://play.acast.com/s/blindboy) and [Robert Evans podcasts](https://open.spotify.com/show/0rOatMqaG3wB5BF4AdsrSX)

Must be one of those 'mono-taskers'? Nope; I currently have 2 different IDE's open, 12 text documents in various stages of progress and [currently 55 tabs open](/2021/07/counting-tabs-and-background-tasks-taunting-goodharts-demon/), along with 3 different 'in flight' books, one has been 'in-flight' for over a year...

You must take great notes and plan everything and have a schedule for all the things? Nope, used to do that, and it's more trouble than it's worth. These days probably around 75+% of my 'working time' is 'unstructured' (including the 'semi-structured' bits I talk about below)

I think I finally worked out what my working style is, and considering my professional practice as a Data Scientist working in Machine Learning, it's blindingly obvious in retrospect; I'm a Adversarial Procrastinator.

For that to make sense; I need to first talk about Ian Goodfellow, who IMO basically changed the game in terms of practical ML in 2014 with his publication of [*Generative Adversarial Nets*](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf). Put simply; why train one big neural network with a whole pile of data, when you can train two neural networks both trying to 'beat' eachother? This is the basis of almost _all_ of the "Oh wow, that's fake?" posts that you've seen shared around for the guts of a decade;

[ThisPersonDoesNotExist.com](https://thispersondoesnotexist.com/) (or [cats](https://thiscatdoesnotexist.com/))? GAN

Deepfakes? GANs on Video

That classic video game that had it's textures from 20 years ago upscaled to 4k? GANs

Google Pixel 6's "Magic Eraser"? GANs on image segmentation

Those Style Transfers of ["What if Kandinsky painted a Lab?"](https://www.tensorflow.org/tutorials/generative/style_transfer); Origionally a CNN, but GANs have been used to identify 'genuine' pieces.

Put simply, for a given target task, GAN's consist of two parts;

* Discriminator - This tries to accomplish the task by expressing a lower dimensionality output, usually a label or number, based on a higher dimensional input, usually an image
* Generator - This tries to 'trick' the discriminator, by expressing a candidate input for the Discriminator, based on a candidate label.

Basically, if the Generator tricks the Discriminator, the Discriminator then gets retrained with the new 'fake' information as a negative label, and the Generator gets retrained with the digital equivalent of a pat on the head for a good job done. Together, and in this loop, you end up with one network that's really good at mapping from 'images' to 'labels', and one that's really good at mapping from 'labels' to 'images'.

This is the 'Adversarial' part, and it's become pretty clear to me, that I do the same thing with my procrastination; I continuously push new 'tasks' onto the stack, so that when I'm getting pissed off / frustrated / bored / stuck with one thing that I have on my plate, I can 'constructively' procrastinate away from Task A by working on Task B.

This makes my use of task managers / issue trackers / calendars really ... Strange.

I will block off sections of time in my calendar with built in procrastination targets, because I've accepted that if I'm not going to feel like doing Task A, I may as well do Task B instead.

For instance; 1400-1500 on Thursdays, I work on Project Management (yey jira....😭), or Documentation, that way, if I can't be arsed looking at Jira again, I dive in to one of the many outstanding documentation tasks (mostly reviews, don't worry) that are floating around.

(I balance this by having an 'Personal Admin/faffing around' block on Monday mornings that leans more heavily on the Faffing side, and a 'Wrap Up' on Friday nights that is really just there to make sure my American colleagues don't accidentally invite me to a meeting that I have to take from a pub smoking area, don't tell my CPO 😛 (_I'm kidding, they know already_))

Or, like I'm doing right now, I'm 4,000 words into a probably 6,000 word lecture on 'Lies, Damned Lies and Data Science' that I'm delivering to UU's MSc Data Science classes next week, but instead I'm finally writing out something that I've been meaning to do for ages...

This all may indeed be stating the obvious, this is almost certainly not a 'new task management paradigm', but it took me a couple of years to work out and accept what I was doing, and to be able to 'tame the discriminator' to accept that I can 'generate' procrastination tasks that are actually long term at least as worth while as 'the target task'; and that when I _do_ get around to the 'target task', I'm coming to it fresh, with energy, and not just doing it "because you told yourself that you would".

Anyway, guess that's about it;

Don't worry about being a procrastinator, just make sure that your procrastinations are worthwhile.
