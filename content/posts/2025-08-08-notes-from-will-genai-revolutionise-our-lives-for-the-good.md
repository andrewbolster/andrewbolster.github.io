---
layout: post
title: Notes from "Will GenAI Revolutionise our Lives for the Good?"
categories:
- AI
- Commentary
tags:
- AI
- Belfast
- 'Farset Labs'
- LLM
- 'Machine Learning'
- NVIDIA
date: 2025-08-08T17:25:00+01:00
---
[![](/img/2025/genai-debate-header.jpg)](/img/2025/genai-debate-header.jpg)

I was fortunate enough to be invited to participate in a debate raising money for [Farset Labs](https://www.farsetlabs.org.uk), a cause obviously close to my cold cynical heart.

[Will GenAI Revolutionise Our Lives For The Good In The Next 5 Years](https://lu.ma/d94zscul) is _top tier troll-bait_ from Garth and Art, and I'm very grateful to have shared the stage with the 5 other speakers. Even the lanky english one. I was particularly impressed by my teammates in their very human-led approach to this question (although everyone was great!)

Anyway, first up, my initial braindump; would have probably run to around 10 minutes, and was more 'information' than 'punch'.

# The Original

I'm Andrew Bolster, I earned a masters in electronics and software engineering from [Queen's University Belfast](https://www.qub.ac.uk/) just as the economy collapsed around us in the late naughties, specialising in GPU engineering and algorithmic optimisation project under Dr Alastair McKinley of Analytics Engines and now SciLeads fame, then I defected to the [University of Liverpool](https://www.liverpool.ac.uk/) with Prof Alan Marshall to earn my PhD in Electrical Engineering, focusing on the [trust and collaboration of autonomous intelligent multi-agent systems](/2017/09/human-factors-in-autonomous-systems) in constrained environments as part of a joint UK/French defence collaboration, just at the height of 'Brexit fever'.

Since then, I've been a data scientist in various roles in bioinformatics, empathic computing (along with my honoured adversary, Mr Ben Bland), and particularly in the past decade, in cybersecurity, assessing and stewarding the intelligent application of decision theory on data driven, high value low risk systems for various multinationals and survived several acquisitions and carveouts, now running the Data Science team at [Black Duck Software](https://www.blackduck.com/).

That overly detailed introduction is to say; I have been thinking about, interrogating, and assessing the safety, security, ethics, and performance of intelligent systems for a long time.

And with that, let's talk about what these magical black box generative AI’s actually are; the latest and probably last gasp of a 200+ year drive to automate away labour, love and liberty in exchange for increased shareholder value, and that we’re not at the beginning of a revolution, rather at the edge of a collapse.

But let's start off with something simple; who has had the experience of buying something on amazon only to then be recommended 6 near identical things afterwards? And those recommendations to follow you through for many days or weeks; Auld Jeff has our collective and individual purchase habits going back nearly two decades, and these [‘recommendations’](https://medium.com/enrique-dans/why-amazons-recommendation-system-is-a-disaster-2f8fdc970d3) are still little more than keyword associations rather than introducing anything new or salient or joyful into the shopping experience. If Auld Jeff hasn’t been able to replace a conversation or a recommendation from a friend who knows you in his giant data-sucking walled garden, I have little hope for these Agentic AI workflows meaningfully replacing anything. And certainly not for upwards of $200 a month.

But where did this all come from anyway? Arguably, we can go right back to [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) with his [Difference Engine](https://en.wikipedia.org/wiki/Difference_engine), which really started the nasty collision in peoples minds of 'oh shit, that object can do the thing that people do, what if object do more like people do!?'. Charlie started off with Maths. Or, I should say, [Lady Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace) made the mechanics of the Difference Engine do the fancy maths that blew peoples minds.

This tick/tock between the physical machine and the logical algorithms permeates the next 200+ years of what would eventually come to be known as ‘Machine Learning’ and if you want a louder, longer version of it, check out my NIDC talk from last year on youtube called Building Beyond Buzzword. In short; there have been at several periods of explosive hype when ‘Machine Learning’ learnt how to wield some new toy, and the world lost their damned mind for a while that ‘The Singularity Cometh’... and then the market imploded when expectation collided with grim economic or physical reality, cursing the field for a decade or more before anyone would deign to try again with the mythological ideal of ‘a slave in a bottle’.

First recent example was the collapse in the 70s after the perceptron couldn’t do anything useful with text, the second was when neural network inspired machines _could_ do the fancy brain-like-things, but no one could get them to do anything useful to justify their extreme pricetag, and third was a simple social one in the late nineties and early naughties were everyone branded every ‘smart system’ as ‘AI’ so hard that it took two decades for anyone to seriously consider using that term in actual product branding again.

This time around, it's the joint innovations of the physical explosion of massively parallel GPU cores for computation, coupled with one of the most influential papers of the past 50 years, ["Generative Adversarial Nets"](https://arxiv.org/abs/1406.2661) by [Ian Goodfellow](https://en.wikipedia.org/wiki/Ian_Goodfellow). It's a bit in the weeds but it's where we get the first expression of getting a pair of differently targeted neural networks to effectively 'train each other', so one would generate pictures of cats and the other one would try and pick out the real cats from the fake ones. This started a wildfire of image generation and image recognition technologies through the 2010's, which joined Cryptocurrency in driving the non-gaming consumption of GPUs through the roof along with NVidias stock price.

This data hungry adversarial loop evolved and grew beyond the 2D space of images into the already established natural language embedding space, where we’d been ‘projecting’ words and phrases into a highly dimensional space to identify relationships between those words and phrases since at least the start of the 20th century. This was where we got the wave of text-based ['Are you a robot' capchas](https://en.wikipedia.org/wiki/CAPTCHA), where, ironically, you were participating in an adversarial training system where your filthy human eyes were teaching the machine how to read old textbooks…. So that the machine could feed the content of those textbooks into the next training cycle of the optical character recognition bot that could be sold as part of a scanner or a phone.

This data hungry adversarial loop has continued to swallow every piece of text, every forum post, every facebook message, every book published, copyrighted or not, every picture taken, every painting put to canvas and increasingly, every frame ever put to film. And now when we engage with these generative systems, we're "replaying" a fuzzy jpeg of all of recorded human knowledge. And it still [gets it wrong](https://arstechnica.com/information-technology/2025/07/ai-coding-assistants-chase-phantoms-destroy-real-user-data/) around as often as it gets it right, if you can ask 'nicely'. A few times over. And [pay a few hundred dollars for the pleasure](https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed).

As an aside, it's now believed that [Nvidia and nvidia alone represents around 10% of the US's economy](https://www.wheresyoured.at/the-haters-gui/). All for probabilistically recalling what is the most likely next word in some ancient stackexchange thread with the most conventional, average, answer.

So now we have giant models training smaller models to generate more data that people can chuck on the internet or in the office as their own pearls of wisdom; copying and pasting their bosses email to get the bullet point version, when that same boss just fed the bullet points into their fancy assistant that's getting [more and more expensive and limited](https://www.msn.com/en-us/news/technology/claude-pro-ai-subscribers-face-new-weekly-usage-caps/ar-AA1JA7ma) but being priced below cost to get [Sam Altman](https://en.wikipedia.org/wiki/Sam_Altman) through the next funding round before he has to demonstrate any actual economic viability, all while burning [multiple countries worth of water, CO2 and funding](https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence), to such a ridiculous degree that in the past 6 months, [more was spent on building datacentres than the entire US consumer economy](https://www.derekthompson.org/p/how-ai-conquered-the-us-economy-a)…

All of this without any of the features or capabilities that we as a society, culture and economy actually value; do you think you’re employed to just write code, or build powerpoints, or write research reports? No, you’re employed to perform to the best of your experience, earned through education and success and failure. You're employed for your agency and, ultimately for your [responsibility](/2025/07/being-a-dorc-in-the-age-of-generative-ai) to take the hit if you screw up; and then the organisation learns how to hire, or more optimistically, mentor, better. These models have no embodied experience, no curiosity, no guilt, no pride, no shame, no culpability, and despite appearances, no ‘Sentience’.

Generative AI isn't some kind of revolutionary technology that will take the world by storm or unleash a wave of sentient terminators or 'Her'-style friends and partners; at best, it is the end state of a direction of research that's been going since [Andrey Markov](https://en.wikipedia.org/wiki/Andrey_Markov) was analysing Russian poetry just before World War 1, and we've long since ran out of new human data to feed the beast.

Now, all that's left is a speculative bubble with every "AI" company on the planet getting [higher and higher valuations](https://archive.md/H9JNt) with fewer and fewer actual, real, economically or socially positive use cases.

It's been a wild ride over the past couple of decades in the Machine Learning space, but to me, it looks more like [the end of the line](https://en.wikipedia.org/wiki/AI_winter) than a new frontier.

Thank you.

---
Next up is the 'last minute' (i.e. the morning of the event) rewrite that I sprung on my team mates, slightly undercutting the main 'AI==Bad' thesis of the overall discussion and pivoting more to declare 'the end of AI!'; it's not 100% what I actually believe ([Context Collapse](https://en.wikipedia.org/wiki/Context_collapse) and [Dead Internet Theory](https://en.wikipedia.org/wiki/Dead_Internet_theory) are real, but they're more socially relevant than technically relevant; and I do believe that there's a big Nvidia-centred bubble that could go pop if Sam or Dario need to take a down-round... ), but this was more punchy and fun!

# The Alternate (and Delivered) Bombastic Version

Hello folks; So far we’ve tackled the good, the bad and the ugly of the question before us; assessing the ‘our’ ness of the question, the ‘goodness’ of the AI. But before we wrap up tonight, I want to take another word in this boondoogle of a question to task; Revolutionise.

I put it to you, good people of the Black Box, Generative AI will not ‘revolutionise’ anything anymore, and in fact, we are at the end of a 200 year long search for sentience and sapience, and we’ve run out of road.

I and most every other of the AI commentariat have talked about [Babbage and Lovelace's Difference Engine](https://en.wikipedia.org/wiki/Difference_engine), Franklin's Mechanical Turk, McCullough's 'Artificial Neuron', Hillis's Connection Machines, Hopfields Recurrent Neural Networks, and pointed to them as examples of moments in history where there was a nasty collision in peoples minds of 'oh shit, that object can do the thing that people do, what if object do more like people do!?'

To me, the most interesting of these, and the most indicative for my thesis that we're running out of revolutionary road, is [Ian Goodfellow's](https://en.wikipedia.org/wiki/Ian_Goodfellow) 2014 invention of [Generative Adversarial networks](https://en.wikipedia.org/wiki/Generative_adversarial_network);

You see, for over 200 years, we had been limited to testing out our theories of computation, vision, and intelligence on actual stuff. Books. Pictures. Handwriting samples. Photos of garbled Textbooks in ['Are you a robot' CAPTCHAs](https://en.wikipedia.org/wiki/CAPTCHA).

Generative Adversarial Networks flipped the script, pitting two models against each other, one generator to make stuff up, and a discriminator to predict if the stuff was made up or was real.

This data hungry adversarial loop has continued to swallow every piece of text, every forum post, every facebook message, every book published, copyrighted or not, every picture taken, every painting put to canvas and increasingly, every frame ever put to film. And now when we engage with these generative systems, we’re “replaying” a fuzzy jpeg of all of recorded human knowledge. And it still [gets it wrong](https://arstechnica.com/information-technology/2025/07/ai-coding-assistants-chase-phantoms-destroy-real-user-data/) around as often as it gets it right… If you can ask ‘nicely’.... A few times over… And [pay a few hundred dollars for the pleasure](https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed).

As an aside, it's now believed that [Nvidia and Nvidia alone represents around 10% of the US's economy](https://www.wheresyoured.at/the-haters-gui/).

That’s bigger than every single individual state in the union except for California.

All this for intricately pancaked sand that is probabilistically recalling the most likely next word in some ancient stackexchange thread with the most average, abstract, anodyne, answer.

Since then, it's been [cat pictures](https://www.bbc.com/news/technology-18595351) and [LSD stained dream-spaces](https://www.theguardian.com/artanddesign/2016/mar/28/google-deep-dream-art) and [deepfakes](https://medium.com/@songda/a-short-history-of-deepfakes-604ac7be6016) and [lingerie clad waifus](https://www.tomsguide.com/ai/i-tried-groks-new-companion-feature-and-ive-never-felt-so-uncomfortable) and [golden gaza](https://www.bbc.co.uk/news/videos/cj675j69gxgo) and post after post and article after article and video after video of spiralling and circling questionable content constantly contending for our consciousness, cravenly clamouring for the quietest cloistered corner of our cerebrum that isn't yet completely crammed with synthetic fears, imagined goals and hallucinated dreams.

Employees copy and paste coiffeured press releases spread by sycophantic C-suites into claude desktop to compress them down to actionable bullet points; which bear absolutely no resemblance to the bullet points that the MBA-brained middle manager mewed into Microsoft Copilot in the first place.

In the meantime, despite these services getting [more and more expensive and limited](https://www.msn.com/en-us/news/technology/claude-pro-ai-subscribers-face-new-weekly-usage-caps/ar-AA1JA7ma), these are priced waaaaaay below cost to get [Sam Altman](https://en.wikipedia.org/wiki/Sam_Altman), [Dario Amodei](https://en.wikipedia.org/wiki/Dario_Amodei) and the rest of the Context Collapse Cabal through the next funding round before they have to demonstrate any actual economic viability, all while burning [multiple countries worth of water, CO2 and funding](https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence), to such a ridiculous degree that in the past 6 months in the US, [spending on building datacentres contributed to more 'growth' than the entire consumer economy](https://www.derekthompson.org/p/how-ai-conquered-the-us-economy-a)…

All of this without any of the features or capabilities that we as a society, culture and economy actually value; do you think you’re employed to just write code, or build powerpoints, or write research reports?

No, you’re employed to perform to the best of your experience, earned through education and life; success and failure; taste and discernment.

You’re employed for your agency and, ultimately for your [responsibility](/2025/07/being-a-dorc-in-the-age-of-generative-ai) to take the hit if you screw up; and then the organisation learns how to hire, or more optimistically, mentor, better.

These models have no embodied experience, no curiosity, no guilt, no pride, no shame, no culpability, and despite appearances, no 'Sentience'. And we've long past ran out of anything else to train them on that isn't already compromised by covert computational content.

Generative AI isn't some kind of revolutionary technology that will take the world by storm or unleash a wave of sentient terminators or 'Her'-style friends and partners; at best, it is the end state of a direction of research that's been going since [Andrey Markov](https://en.wikipedia.org/wiki/Andrey_Markov) was analysing Russian poetry before World War 1, and we've long since ran out of new human data to feed the beast.

Now, all that's left is a speculative bubble with every "AI" company on the planet getting [higher and higher valuations](https://archive.md/H9JNt) with fewer and fewer actual, real, economically or socially positive use cases.

It's been a wild ride over the past couple of decades in the Machine Learning space, but to me, it looks more like [the end of the line](https://en.wikipedia.org/wiki/AI_winter) than a new frontier.

Thank you.

## What I/We skipped

(AKA what I might turn into a bigger talk)

* Geopolitical chain between *AI-NVidia-TSMC-Taiwan-China + ASML potentially being a trigger
* Environmental impact of data centres in general
* Token Inflation (i.e. tokens get cheaper but models get more long winded)
* Sycophancy/'You're absolutely correct, I am a stupid twat!' 'guilt-less' responses
* Scaling of fraud and its impacts on non-tech-savvy (Your grandma doesn't know what an emdash is and thinks bullet points are clever)
* "To Catch A Thief": So your Agent is watched by a Supervisor who is prompted by a Planner; how are you evaluating all of those?
