---
categories:
- AI
- Software Engineering
- Philosophy
cover:
  alt: AI-generated featured image for Being a DORC in the age of Generative AI
  caption: Generated with AI based on post content
  image: img/test-dorc.png
date: 2025-07-14 14:16:00+01:00
tags:
- AI
- LLM
- Machine Learning
- ethics
- software development
title: Being a DORC in the age of Generative AI
---

Lots of people have written about the impact of [generative AI](/2024/02/generative-ai-impact-on-software-development-and-security/) on the world of software engineering, and while I write this I'm fighting with [CoPilot](https://github.com/features/copilot) to stop filling out the rest of the sentence. Gimme a second...

...

That's better. Anyway. This is just a blurb/brain-dump of a shower-thought. Don't come to me for deep insightful stuff about the productivity gains about [Generative AI](/2024/02/generative-ai-impact-on-software-development-and-security/) in Software Development, or whether it will be the end of 'Juniors' in software engineering, or how we're going to _grow_ juniors in future.

I'm just gonna rant about how I've been thinking about my own place and direction in all of this, and over the past few days/weeks/months, I've landed on "Being a DORC", Discernment, Ownership, Responsibility and Credit. And as I'll hopefully explain, it's as much about your own sanity and the sanity of your peers and colleagues as it is about 'doing good software', with or without 'AI'.

# Discernment

When '[Minds](https://theculture.fandom.com/wiki/Mind)' [trained on the entirety of human creation](https://arxiv.org/abs/2211.15533) are allowed to splutter out whatever slop falls on the right side of a [probability curve](https://jalammar.github.io/illustrated-transformer/), _discernment_ and the ability to make choices, decisions, and judgments based on your own experience, probing, and ultimately 'taste', is going to be a huge differentiator in the 'Brave New World'.
Not just for the surface level **'Herp derp of course a human will have decision making power herp derp'**, but IMO more importantly, for the mental health of the folks holding desperately onto the reins of whatever future AI based systems are driving the industry.
The ability to make a decision or choice based on the best of your knowledge and ability and to stand behind it without infinitely spiraling into 'what ifs' or continuously trying to refine a 'test'.
Make a call and move on; if new evidence comes in and shows that you were incorrect, misguided or whatever; walk it off. You'll be better next time.
[Strong Opinions, Loosely Held](https://www.saffo.com/02008/07/26/strong-opinions-weakly-held/).

# Ownership

When glorified [lava lamps](https://blog.cloudflare.com/randomness-101-lavarand-in-production/) are piping hot, steaming, 'decisions' out of near-infinitely deep latticeworks of maths, it's tempting to imagine a world where every decision gets made by these 'perfect' machines. This not only forgets how these machines got so good in the first place ([Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning) is basically [Pavlovian BDSM for Vectors](/2024/04/context-all-the-way-down-primer-on-methods-of-experience-injection-for-llms/)), but also forgets how the entire post-modern capitalist project works.
If you're fortunate enough to be put in any kind of 'decision making position', it's tempting to think that you're there because you're _so great_.
The cold reality is that you're there to _own_ the outcome of your decisions, Right or Wrong.
That means that if you made the call, you should follow that call through the sausage-machine of development and do your best to help other poor souls who are downstream of your 'decisions'.
In this industry, Owners won't be able to sit back and rent-seek for much longer, waiting for everyone else to get the work done and report back at the end of the month/sprint.
That way, if it all goes to shit, you'll also be best placed to understand how best to update your 'discernment'. And also best placed to accept...

# Responsibility

Responsibility is the obvious follow on from Ownership, and I can understand people thinking this is redundant, but for me, Ownership derives from Decisions and Responsibility derives from Outcomes and Impacts.
One way I think about this is that when I took the decision to build out [Black Ducks'](https://www.blackducksoftware.com/) [LLM](https://en.wikipedia.org/wiki/Large_language_model) inference infrastructure way back in 2023, I chose not to support 'BYO-Models' and opted for the serverless inference provided by the various cloud providers; I own that decision, but I'm responsible for that infrastructure and it's my responsibility when new models roll out from 'The House of [Altman](https://en.wikipedia.org/wiki/Sam_Altman)', to make those available in a reasonable time. Nothing to do with my job description, or the description of my team; I made that choice, I own that decision, and until I find another part of the org to safely hand that over to, that's my responsibility.
The term "[AI-Agents](https://en.wikipedia.org/wiki/Intelligent_agent)" is an oxymoron because by definition the only thing they _don't_ have is '[agency](https://en.wikipedia.org/wiki/Agency_(philosophy))'; they cannot and do not 'grow forward' without some kind of push, trigger, or prompt.
And without agency, they have no capacity to be held responsible for their actions in the world.

# Credit

Speaking of teams; a lot of this rant has been 'me me me', because fortunately for you, there's only one seat available to the one-man-show that is my internal monologue. But a critical part of this whole '[GenAI](/2024/02/generative-ai-impact-on-software-development-and-security/) to revolutionize X in Y years' is remembering where all this came from.

* [Bayes theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) is from 1763.
* The '[Least Squares](https://en.wikipedia.org/wiki/Least_squares)' method of approximation is from 1805.
* [Markov chains](https://en.wikipedia.org/wiki/Markov_chain) are from 1913
* [K-nearest neighbour](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) is from 1951, as is [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning).
* First [chatbot](https://en.wikipedia.org/wiki/ELIZA) is from 1965.
* [Recurrent Neural Networks](https://en.wikipedia.org/wiki/Hopfield_network) from 1982 and [Boltzmann machines](https://en.wikipedia.org/wiki/Boltzmann_machine) from 1986 - both foundational to the [2024 Nobel Prize in Physics](https://www.nobelprize.org/prizes/physics/2024/summary/)

All of this was before I was even born, but all of this directly or indirectly contributes to my career 'discernment' today; but, I didn't "get lucky" finding a gigantic intellectual ladder, but rather, [standing on the shoulders of giants](https://www.bbc.co.uk/worldservice/learningenglish/movingwords/shortlist/newton.shtml).

(If you want the rest of the list, check out my ['Building Beyond Buzzwords'](https://youtu.be/0v3dBt65POI?t=257) talk from last year)

'Giving Credit where Credit is Due' isn't about maintaining a lineage of who did what when and why, or being able to give citations for every action; it's about understanding your participation in a [continuously growing system of knowledge and experience](http://matt.might.net/articles/phd-school-in-pictures/).

But it goes beyond that; LLMs aren't "clever" because of some arbitrary maths; they're "clever" because they were trained on human expertise/experience/interactions. "Reinforcement Learning with Human Feedback" is still the mask behind the [Lovecraftian mathematics](https://knowyourmeme.com/memes/shoggoth-with-smiley-face-artificial-intelligence) under these systems. And they're dumb for exactly the same reasons.

As our work with, around, and towards AI evolves, it will be increasingly critical to maintain an understanding of the causality and credit around the behaviours of these systems and our relationships with these systems; both positive and negative.

# Conclusion, I guess.

So, I'm a DORC when it comes to AI, and I'm fairly sanguine about it; the way I put it to my team is that "We do the hard boring 'plumbing', so the sexy 'innovation' is easy"

Anyway, brought to you by a bank holiday weekend and wanting to test out typing while on a walking pad...
