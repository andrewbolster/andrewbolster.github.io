---
date: 2020-05-22 14:35 +0100
layout: post
tags:
- Archimedes
- Ethics
- Data Science
- Facebook
- Social Media
- Public Policy
- Scientific Ethics
- Technology
- Cambridge Analytica
- Data Governance
title: Pragmatic Data Science; When Unstoppable Math meets Immovable Ethics
---


<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTmW2Ls_Qvj0KGH-7wJvWxPyHGJnwf-Den52J5dm-ejF2WQeXnUEqDPv98uT--mt_WwsgQR6vEh30w6/embed?start=false&loop=true&delayms=0" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

_This is a Rough Transcript from [The Virtual Bash on Ethics](https://www.meetup.com/devbash/events/270315785/)_

# Introduction

Around two thousand, two hundred and 20 years ago, Archimedes said “Give me a place to stand and I will move the world”.

Archimedes has come to be (rightly) associated with many fundamental innovations in mathematics and engineering, and while I’m sure we’re all sick and tired of screws and levers and jumping out of bathtubs, I’d like to start off with a discussion on one of his more mundane creations, the compound pulley.

The Greek biographer Plutarch describes an interaction between him and King Heiro of Syracuse, where Archimedes boasts that he can pretty much move or lift anything. The King was dubious of this, but, being a king, had a few massive warships that required hundreds of men to manoeuvre in and out of dock and put Archies wild claims to the test.

As the story goes, Archie shows up with what we now call a compound pully system, and pulls the kings warship along the dock, with his relatively frail body pulling arm over armfuls of rope. Each chained pully multiplies the expressed force of the previous, pretty much for as many layers as you like, trading distance for force. This, today seemingly simple, technical innovation would find applications across human experience; Archie wasn’t the first to use a pulley, and was almost certainly not the first to come up the compound pully, and he’s almost certainly not the first to use a pully to make a military manoeuvre easier... But Archimedes went beyond the simple application of his stated ‘creations’ like the lever, the water screw and the compound pulley, to mathematically characterise their operation and performance, making them sharable, teachable, and in this day and age we might even say ‘scalable’.





My name’s Andrew Bolster, I’m the team lead of the Data Science team at WhiteHat Security, a director at your friendly neighbourhood hackerspace, Farset Labs, and in past lives I’ve worked on 4G telecoms which definitely don’t cause coronavirus, been an autonomous systems and AI researcher for the defence establishment designing communications networks for smart submarines, and have tried to teach machines how to read and respond to human emotions, and in the next hopefully 20 minutes, I am going to talk about the Missing E from STEM, Ethics, and how within the burgeoning field of Data Science, we have a serious ethics problem, and potentially, how we can work towards redressing it.

We’re going to approach this under three main themes;

·     Ethical Optimisation, via our old friend the trolley problem;

·     Unscrupulous Actors, Perverse Incentives and Bernhardssons Corollary, via our ‘it’s complicated’ friend Facebook; and finally

·     Asilomar, or how an attempt to mess with carcinogenic monkey virus led to what I believe might be a depressingly bureaucratic but optimistically pragmatic approach to, maybe not putting the genie back in the bottle, but putting a leash on it.

So, lets see if I can keep to time. I think there’s a bracket in the slack room, put me down for a tenner on 26 minutes total.

## The Trolley Problem



We all know the story by now; There is a somehow unstoppable indestructible trolley barrelling down the tracks heading for some number of immobilised people, say five in this creative example. You, an innocent bystander, see this calamity and can predict what is going to happen if you do nothing. You also see that on another siding, some other number of people, in this case 1, are similarly restrained, and you can predict what happens if you pull the lever. You, dear bystander, can act to choose to reroute the trolley, killing one to save five.

And as we’re all good Vulcans, we can confidently act to maximise the number of lives; after all, the needs of the many outweigh the needs of the few, or in this case, that poor unfortunate one.

So, what we’ve got here is a good old fashioned optimisation problem. Ok. It’s clear that more lives are saved by acting in this case.

But I’m sure we’ve sat through talks that then go on at length about the combinations of the saps on each track, whether there’s a guy you can push off the tracks to stop the train, or if there’s a baby on one side and an old person on the other, to the point where you eventually work out that the exchange rate between ‘Baby’ and ‘OAP’ is something around 3.235 or whatever.

That’s not what I want to talk about.

Any machine learning system, as well as most data science research is a form of optimisation system; you feed it data, and you give it some way of knowing if it’s “good” or not, and decisions or recommendations pop out of a trained model. These models are generally educated on ‘goodness’ by what is called a fitness function.

Usually, and thankfully, it’s rarely that simple, but lets say you do a massive global study and you somehow create this huge matrix of different peoples decisions so that you can confidently aggregate what the ‘normal’ human would do in a given situation. That sounds like a pretty awesome solution, right? Literally crowdsourcing ethics? Wee buns.

Well, as usual, MIT already did it. In 2017 they had 70,000 participants across 42 countries. And the while the whole paper is a fascinating read, I’ll give you an easy highlight and move on.

To cherry pick; in 82% of responses, Germans, like most europeans, did a Spock and sacrificed the one to save the many. However in China, that number is 58%. And China is not some surprising outlier, there are a smorgasbord of variations in judgement calls that are correlated within regions but vary across regions.

There is no global definition of what “a socially moral act” is, and indeed if you just took the straight average, more people would disagree with it than would agree with it. And this is in quite possibly the ‘simplest’ ethical question we think we can ask, saving lives or not.

So, we can’t optimise for ethics, because no one can or will be able to agree on what ethics is.

## Unscrupulous Actors and Perverse Incentives

In mid 2008, Facebook proudly announced their Connect API. This enabled truly portable social login, and also enabled app developers to access the users social web to recommend, engage, and customise. Fun fact, their proudly launched blog post has since disappeared from the internet, go figure. Apps like Eventbee turned your friends into mini Ticketmasters by enabling them to get a cut of virally recommended ticket sales; Netflix let you share movie ratings within your friend group; Hell, the Watchmen Blue-Ray had the ability to invite your friends for simultaneous watch parties, which would have been handy about now…

This was the dawn of a new age for the web, everything was connected to everyone, and the experience was customised on a per user basis, rather than requiring some bulk data access API or something similarly privacy-crazy.

And then, the quizzes started.

Netizens of a certain age remember the day before Facebook quizzes exploded, and the day after. It was hell. And it made no sense; but you just ignored your dumb-ass mates posts and moved on with your life.

By 2014, Facebook had killed this ‘next generation social network’, and years later, we found out why. But the genie was out of the bottle and the world was already changed. But, how?

How did a proliferation of pointless quizzes and single-purpose app integrations lead to the global manipulation of public opinion on an industrially mechanised scale?

Well, friends, it started off with people like us. Technologists, Data Scientists, Researchers, Academics, Numerical Fiddlers.

Between 2007 and 2016, The University of Cambridge Psychometrics Centre, which is part of the Judge Business School, ran a quiet little side project called ‘MyPersonality’ that, like many other psychometrics research groups across the world, leveraged the kind of viral social media reach that the Connect API enabled, to run playful personality tests to tell you what kind of dog you are or whatever. But these results were genuinely used for bona-fide, ethically moderated, research into the social and psychological questions of the day. The API itself provided a perverse incentive for data driven researchers; the more people you can get to run a quiz, the more people who’s demographic and interest metadata information you could lift at the same time, even if the friends of the obsessive compulsive quiz taker never touched, or consented to, your friendly little app. The movies they liked, the pages they liked, the artists they followed and the mutual-friends with the quiz taker were all on the table.

Today we call this kind of thing ‘Triangulation’, but at this time, it was just an interesting research context to characterise different quiz responses into different social buckets.

Like Age, Race, Occupation, Economic status, Education… Beliefs… And what kind of posts you would ‘like’

And the quizzes themselves, through psychometric aggregation, could score people on estimates like “Respect for authority”, “Voting Intention”, Media Savviness, Neuroticism and more.

I have to confess, I myself played with the same datasets that eventually got called ‘The Cambridge Analytica’ files. I was at the University of Liverpool at the time researching trust networks for applications in autonomous systems, so borrowing structures and activities from human social networks made sense. And I requested access, got vetted for my purposes by diligent academics, and I played with the things I asked for. All good, sounds nice.

Then one academic accidentally published their access credentials onto GitHub…

And there they were for over four years.

The story of what the evidently unscrupulous actors, SCL and Cambridge Analytica did with that data is better documented in other places, but I want to talk about Facebook’s handling of the situation.

Frankly, Facebook didn’t give a poop that there was an aggregated data set of millions of its users, which was in massive violation of the Connect API’s Ts&Cs. And it’s not like they didn’t know about it; a Facebook employee applied to access the data, but was rejected by vetters.

It is here I want to break off for a second. I think most of us are aware of ‘Hanlon’s Razor’; Never attribute to malice that which can be adequately explained by stupidity. Its a great way to stress less about our reptilian overlords and pizza shop basements, but I came across what I have termed “Bernhardssons Corollary”, “Never attribute to stupidity that which can be explained by opportunity cost”.

Facebook didn’t **plan** for their data to be misused by unscrupulous actors, they weren’t too stupid to think about it, and while Zuckerberg might look inhuman when he’s supping on Dihydrogen Monoxide, given the choice between “deep state conspiracy to elect a glorified used car salesman” and “prioritised shipping features over data governance”, my bet is always with over-worked data scientists, developers and product managers on a Sisyphean treadmill. It is easy to say today that ‘yeah, that’s a nice API and all, but what if someone doesn’t adhere to our lazy, unenforceable rules for legitimate research purposes, the same research that we do internally for funzies, and what if a private firm work out how to get access to the aggregate data and use it to isolate and manipulate filter bubbles for the highest bidder?”.

Wargaming Data Governance “What If?” scenarios isn’t prioritised at an executive level; it wasn’t something that could be quantified on a burn down; or allocated story points; and it was never going to end up in the investor briefings or press releases. Well, until it made it into the congressional record.

But lets not just poop over Zuck for this one; our memetastic interweb has an applicable ding on those supposedly responsible for oversight too.

Policy makers are supposed to be experts in policy; politicians ar

And modern corporate governance, that has eschewed internal research teams to optimise for the bottom line, can’t be expected to be informed enough to self-govern in a way that covers the explosive possibilities of the connected world.

But then, when public bodies **do** try and create these kind of structures, they inevitably run in to massive obstacles, particularly in implementation, with technologists tearing their remaining hair out wondering ‘what the hell does “appropriate measures to prevent deanonymisation” mean?’, looking at you GDPR…

They can’t prepare for unforeseen consequences, and they can’t see the perverse incentives until long after they’ve pushed their beautiful code.

## Asilomar and Public Scientific Policy

So, crowdsourced ethics makes no one happy, corporate entities don’t account for moral failure on their balance sheets, and socio-economics prevents governments from effectively legislating this kind of thing, What about practitioners?

In 1974 a biochemist at Stanford called Paul Berg designed an experiment to stuff bits of a carcinogenic monkey virus into some E. Coli bacteria, but when he shared his proposed experimental protocol, he got a very very mixed response from the scientific community at the time. Long story short, they believed that it could cause a quickly spreading cancer causing viral pathogen. Fun times.

Instead of pulling a Frankenstein, the 1975 Asilomar Conference on Recombinant DNA was held with over 100 internationally respected molecular biologists in attendance, with Berg as its chair. There, they established a set of guidelines to be followed by all scientists doing this kind of recombinant DNA research. They considered several classes of experiment and assigned relative levels of risk, from minimal to high. Each level of risk required a corresponding set of containment procedures, designed to minimise the chance of carriers from escaping into the wider world and, in our established parlance, ‘unforeseen consequences’. This included the forbiddance of certain classes of experiments, such as using materials from highly infectious or toxic genomes or running experiments to produce large scales of reagents.

These guidelines were predominantly ‘socially enforced’ rather than being legislated; with a significant strand of the conference discussing the importance of operating ‘in the open’ and bringing their science into the public eye. Some commentators suggest that this is a reflection of the distrust of government in the wake of the Watergate scandal, such that it was easier for the public to trust scientists following scientific consensus than it was to trust scientists following government derived and potentially variably enforced legislation.

This generation of an open consensus within a community of practitioners and experts led to an increasingly positive view of the field within the general public.

Somewhat ironically from our vantage point almost 50 years later, this enabled specialists who had previously confined themselves to academia, to develop ties in the private sector, as shareholders, executives, and consultants; engaging with private industry in a constructive way, because their Biomolecular ‘Hippocratic Oath’ provided a stability and confidence to explore new innovations and opportunities, safely.

Berg went on to earn the Nobel Prize in Chemistry in 1980 and, by the 20th anniversary of the Asilomar conference in 1995, genetics and it’s terminology had become part of the day to day vocabulary and not something restricted to the hallowed halls of university or private research establishments.

I’d argue that if it’s good enough for cancer causing simian stomach bugs, it’s good enough for Data Science. Efforts along these lines are already active, and I would encourage you as practitioners to take part. There are many Data Ethics projects across the world, as well as Gillian’s Human Impact Statements; some of them open source such as the Open Ethics Canvas from the Open Data Institute, or Public Sector, such as GOV.UK’s Data Ethics Framework, which while being good has no interesting graphics associated with it other than Matt Hancocks face, which I won’t subject you to. As well as this there are ranges of ad-hoc and drifting towards professional standards being developed for data governance and ethical data science.

Of particular interest to me at the moment, is the IEEE’s proposed 7000 series of standards on ethically aligned design, which ranges from p7003 concerned with Algorithmic Bias Considerations, P7002 Data Privacy Processes, and one of the weirder ones, P7014, and a bit of a mouthful, Standard for Ethical considerations in Emulated Empathy in Autonomous and Intelligent Systems, which is to do with the strange world of thinking about systems that quantify, respond to, or simulate emotion. And of course I sit on the working group for the weird one.

These groups bring together wide and diverse voices together to interrogate and twist the use and potential misuse of data science and autonomous systems, developing shared standards and guidelines to which we as a community of practice should adhere.

And it’s far from perfect; the bureaucracy involved in engaging a community of practitioners of thousands is not without it’s challenges, with the ever taunting pressures of ‘just get it done’ hanging over us all we have to ask the question; how do we do this?

So we’ve covered the challenge of mathematically operating in an ethical, human, world; the inevitable challenge of unforeseen consequences, and, as usual in software engineering, we think we might be able to steal another fields good ideas to save our own skins. What does this all mean as a Data Scientist today?


## What now?

Frankly, it’s a fraught time to be a Data Scientist.  I don’t have any easy answers.

With an analytical background, and the usual laundry list of ‘skills’ this industry desires, you’re used to developing tools against constraints, but when there’s no accepted, or potentially even possible, standard against which to measure your work ethically, how can you write code or interpretations of data that you can stand behind?


If the Ethics is unaccountable and un-costable, how do we progress with any kind of confidence as an industry?

Or do we just resign ourselves to say that Data Science as a field is the art of fulfilling the ‘lies, damned lies and statistics’ aphorism, or getting trapped in Gillian’s ‘Get It Done’ environment?

For years, I considered myself an Engineer above being a Scientist, approaching problems in the practical mindset of “How do we do the thing that satisfies the requirements in the most practical elegant solution?.

These days, I’ve been forced to accept that we don’t know what the “thing” is, the requirements will be written by the headlines 5 years later; and the best we can hope for is for a generation of data scientists, developers, engineers, and product managers, to take a pragmatic approach, to assess the second order risks like perverse incentives and the acceptance that there are unscrupulous actors that are more ingenious than us, and that take a step back and remember that ethical optimisation is at best a heuristic rather than an algorithm, and above all, try and leave the world a little better, and better documented, than we found it.

It’s on us, as an industry and as a field, to hold each other accountable, and to question and support each others decisions, pragmatically, fairly, and openly.

Thank you.
