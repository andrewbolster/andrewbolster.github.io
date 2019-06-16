---
layout: post
title: 'Data Art: Creative Collisions and Getting out of your comfort zone'
---

# Introduction (~250w)

The technology community is known for being strongly inward looking to the point of being miopic at times; we focus on techniques, products, languages, frameworks, and best practices and we consider success and failure based on concrete facts and evidence.

Does it pass the CI? Is the Kanban board clear? Did our KPI’s indicate a winner between A and B? Did we get more traffic this month than last? Did we increase throughput on the pipeline? Did we increase security coverage? Did we get more sign-ups this month? How is our MRR curve?

This empirical approach to development and creation is far from unique to our industry, but quite often, the “outcomes” of this line of work can be cold and deeply impersonal.

We occasionally find ourselves looking over to other industries, like education, art, or politics, with a mix of derision and jealousy

However, some of the best outcomes and experiences come from pushing and stretching our boundaries outside of the safety of our wee community.

In this talk, I’ll be sharing a bit of my background for context, and discussing some of the creative collisions I’ve come across; from using VR technologies to enable creative expression for disabled musicians, empowering artists to use electronics to connect their art to the wider world, and using science data to drive policy and political engagement.

And along the way I’ll hopefully be proving that I can actually pull off a talk with less than a hundred slides and without resorting to Python or Slides-with-text just to piss off Sigma


## My Background, Our Journey and Your Challenge (600w)



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20190.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20190.png "image_tooltip")


My professional background has wandered through a few fields over the years, from taking things apart at a young age and always having a few screws left over at the end and getting robotic dogs to piss on headmasters, eventually turning that skillset into something akin to a trade by studying electronics and software engineering at Queens, during which I got to test the launch of 4G networks in China from the grey comfort of an office in Athlone, moonlit as a technology consultant for a marketing and advertising firm in Belfast and spent a summer developing BIOSs for embedded computers in Switzerland.

After that, and just in time for the financial crisis to make everyone question their career choices, I continued down the academic culvert to do a PhD, stealing shamelessly from the sociologists to make their “science” vaguely useful by teaching autonomous military submarines how to trust each-other.



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20191.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20191.png "image_tooltip")


More recently, I worked with a bunch of psychologists to teach machines how to understand human emotions using biometrics and wearable tech, and now in my current role as a Data Scientist working in AlertLogic, I play with terabytes of data trying to read the minds of hackers and script kiddies across the world who are throwing everything they can at some of the internet's biggest institutions.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20192.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20192.png "image_tooltip")


But beyond the technical side, I was part of the team that built Farset Labs almost 8 years ago now. As it stands, Farset is Northern Irelands’ only hackerspace, and, at least in my opinion, has stood the test of time as being a relatively neutral ground in a technology ecosystem that was historically beset with silos and egos.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20193.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20193.png "image_tooltip")


I’m not saying we’re perfect, but I hope those of us in the room that remember what the tech community was like in Belfast a decade ago would agree that we’ve come a hell of a long way towards getting better at working with each other across the barricades of frontend vs backend, fintech vs academia, Python vs R, and so on.



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20194.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20194.png "image_tooltip")


And we’re even close to a peace deal between Vim and Emacs. But only if Emacs agrees to a Vim Language Act, so I’m not holding my breath.

Part of that “ever closer union” has been driven by the adoption of technology itself.

Meetup is a great example of this.

It has enabled collaboration and knowledge sharing within the tech community in a way unimaginable a few years ago.



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20195.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20195.png "image_tooltip")


But more important than that, in my opinion, has been the connection of personal networks and experiences across the industry, and those interwoven connections has gone a long way to enabling the rapid dissemination of stories, experiences, questions and answers that define this as a tech community rather than just the Northern Ireland Tech Industry.

And that’s where we start to get to the point of this talk, after a full 5 minutes.



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20196.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20196.png "image_tooltip")


There’s more to the world than just tech, and I want to set a challenge to everyone in this room.

This year, do some kind of collaboration outside the tech industry, and to do a lightning talk on it at NIDC 2020.

But what do these collaborations look like? How do they work? And what impacts can they make in the real world? I’d like to go through a few examples that I’ve come across over the past few years, covering the dynamic and subjective world of the arts, but first the great bureaucracy that runs our world that is “the public sector”.


## The Public Sector



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/NIDC-20197.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/NIDC-20197.png "image_tooltip")


For anyone who’s worked with or in the public sector, whether that’s in local government healthcare, community organisations or in any other capacity, it would be very difficult to honestly describe any of their operations as “Agile”, “Innovative” or “Dynamic” in the same sense that we might be able to describe working in Tech.

But for all their perceived sins, the public sector is acutely aware of this, and god love em they’re trying.

One particularly interesting project, both from a political and a technical point of view, was a Small Business Research Initiative (or SBRI) challenge that came from Land and Property Services around “streamlining” the assessment and collection of rates.

Now, before everyone falls asleep, I’m gonna start off with the outcome and work backwards.

A partnership between the boring old school pen and paper rates body and a couple of data driven startups, married with access to government open data, costing about £60k and 9 months ish to build a machine learning based system that has since identifed about half a million pounds of additional rateable income.

How often do you hear about government tech projects that break even let alone turn a profit?!

![alt_text](images/NIDC-20198.png "image_tooltip")

The key insight they arrived at was by gathering all the location and service related open or council-internal data they could get their hands on, and look for multi-dimensional outliers. That all sounds very complex, and I’m sure an awful lot of work and research went into the perfect combination of metrics that was super duper powerful and insightful. However, the biggest **single** factor used in identifying if property should be paying rates?

If they have a food hygiene rating, they should probably be paying rates, right?

But tech collaborations don’t have to be at the scale of a government procurement process or even specifically to do with the application of technologies directly.

![alt_text](images/NIDC-20199.jpg "image_tooltip")

At Farset, I had the pleasure of working with the Northern Ireland Voluntary and Community Agency, or NICVA on stealing some of the practices and protocols we in the tech industry  have to generating new projects into a structure they called “Policy Hacking”.

![alt_text](images/NIDC-201910.jpg "image_tooltip")

Now, anyone who’s been in a “Design Thinking” workshop or a well managed hackathon or has worked in a decently operated scrum process will recognise the idea of starting with a user-focused, solution-oriented journey of problem identification, open discussions across organisation hierarchies, and prototyping, with a rapid iteration cycle.

But this kind of attitude to solving problems was completely unheard of in areas like healthcare, justice, and community policy generation.

![alt_text](images/NIDC-201911.jpg "image_tooltip")

And after facilitating a dozen or so of these “Policy Hacks” on different sectors, NICVA used the policies developed out of these hacks to build their cross-sector strategy and directly inform their consultation on the Northern Ireland Programme for Government.

However, this outcome came just in time for the assembly to implode over various scandals… But as we are all well aware, you can have all the planning and frameworks in the world, and the c-suite can still shit on all your dreams from a great height, so I guess we have that in common with the public sector…

If only there was something we could do about that?...

![alt_text](images/NIDC-201912.png "image_tooltip")

Now this section was literally added during Brians talk before this session, so I apologise for the tappa tappa… Anyway, you may have seen the electionsni.org site, where a load of political wonks contributed near-live count statistics to couple of data saavy people to provide live transfer analytics for the last elections. We’ve just restarted this collaboration so if anyone would like to get involved in analysing, understanding, and presenting election and political data in meaningful ways, please give me, Bob Harper or Colm Burns a shout!

![alt_text](images/NIDC-201913.png "image_tooltip")

Outside of classical government or community group activities, the tech world is facilitating amazing “Grass Roots” public policy debates, and one of the more exciting ones I’ve seen coming down the road is a project kicked off by our own Steven Hylands.

The Climate Fixathon is a 4 week remote hackathon for tech professionals to use their skills to help prevent climate breakdown. I’m technically spoiling Steven’s big reveal that was supposed to be at their meetup next week, but with a room like this why not take the opportunity to promote! Anyway, it’ll run from the 15th of July and is built around three pillars; raising awareness, taking action, and enabling facilitation platforms. And in the context of my challenge from the beginning? Yes, participating in the Fixathon would count!

[https://youtu.be/_ihIYoZB4OI]

Beyond the normal “public sector” operations, there are also really awesome collaborations and prototypes coming out of related sectors like tourism, and while I know you all came here for nice art stuff, not the boring public stuff, I just wanted to show one system that’s been developed locally as a collaboration between the tourist board and a VR/AR startup called Virtual Visit Tours, and I believe was just installed in W5 as part of their new exhibition space. They took hundreds of a mix of 360 and stereo videos to create an AR experience that can transport you from any place with a flat floor, to one of a dozen or so tourist sites across the province.


## The Arts

![alt_text](images/NIDC-201914.png "image_tooltip")

But why I suspect most of you dropped into this talk instead of the fantastic sessions I’m competing with is the crossover between technology and the arts.

One really satisfying projects I’ve been a part of is a collaboration called VRIMM, or Virtual Reality Inclusive Music Making, between the Drake Music Project, QUB’s Sonic Arts Research Centre or SARC, and Farset Labs.

The goals of this project are to give disabled musicians the power to express themselves musically (and eventually visually, but ask me about that after) using Maker-Accessible Electronics and VR Tech.

This was born our of a previous collaboration called Performance without Barriers, where SARC and Drake worked the HTC Vive to develop physically responsive, virtual musical instruments tailored to the experience of the musicians.

![alt_text](images/NIDC-201915.png "image_tooltip")


This is Marie-Louise, under the very expensive mask. She has Cerebral Palsy, which makes is very difficult to control her movements, especially in the kind of fine motor control that you usually need in the creative field. Using a Hive game called EXA, they were able to construct what I like to think of as virtual sonic curtains in 4 spots of VR space around Marie-Louise

Because they were able to customise the musical structure around her to her own range and rate of motion, very quickly Marie-Louise became proficient enough to perform in front of an audience of dozens of people at a concert, along with a few other her old and new friends

![alt_text](images/NIDC-201916.png "image_tooltip")


Another related project with a PhD researcher called Alex, who’s working with another disabled musician with profound multiple disabilities called Eoin, and they’ve been co-developing a virtual guitar, based on a sip/blow switch you can see Alex holding on the right there, which is used to select “chords” of notes, and then arduino powered wireless wearable sensor on Eoins right hand to “strum” the virtual notes.

[https://youtu.be/rcSUfAEhkMc?t=44](https://youtu.be/rcSUfAEhkMc?t=44)

As part of the VRIMM project, we’re bringing strands of this work together, along with workshops both for artists and technologists to share experience and knowledge in things like electronics, embedded programming, games design, musical theory, and music production techniques to create a community of people designing and building devices and systems that can take some of the capabilities of something like the EXA that Marie-Louise used, and make it more accessible, both in terms of price and interoperability. And if anyone wants to get involved in that madness, I’ll be in the project room after lunch playing with some of it!

But moving slightly away from the musical side of things into the visual arts;

[https://youtu.be/jQGa0-lc2JY](https://youtu.be/jQGa0-lc2JY)

One of the very first “in your face” tech/art crossovers I got to experience in Belfast was when an ex-theoretical physicist cum-sonic artist asked if he could take over the workshop in Farset for a while to build some monstrous lightshow with 5000 LEDs and a load of sensors, all to build an interactive ping pong table that’s been touring around the world.

[https://youtu.be/Af2rUNKEe08](https://youtu.be/Af2rUNKEe08)

![alt_text](images/NIDC-201917.png "image_tooltip")


Not to be outdone by himself, Robin then kicked off a collaboration with an environmental scientist at the University of Birmingham to construct an arduino powered pollution sensor, testing it against environmental grade equipment to see exactly how useful $10 chinese imports are. Unsurprisingly they’re not exactly professional grade, but would do for broad brushstrokes of “how dirty is the air?”.

![alt_text](images/NIDC-201918.png "image_tooltip")

 And from a technical perspective, it could have stopped there, maybe with a web dashboard or something; but instead the kit was expanded to include another LED array that flickered based on the amount of particulates detected in the air. This was then taken on a global tour that I was not at all jealous of, to take long-exposure light-painted photographs of the normally invisible spectre of air quality, in far flung fields such as Port Talbot Steelworks and Jakarta

Robin is someone you brings his STEM experience bear to express his art, all in one cat-loving vaguely human shaped box.

Seeing Robin’s projects and especially the reaction to those projects from both the arts and tech communities was a revelation, me sitting somewhat on the periphery of both;

The Arts Community saw him as being some kind of dark wizard of electronica, and then also the tech community seemed to think “Hey, that’s a really cool way of presenting that information, I’d never have thought of that, you crazy artist!”

And while Robin is a crazy artist and a dark wizard, one man can only give a shit about so much. So to make real change in the world, I wanted to build bridges.

For the past couple of years, and directly as a result of ODCamp coming to Belfast in 2017, I started a couple of occasional meetups call, wait for it, Data Art #titledrop

![alt_text](images/NIDC-201919.png "image_tooltip")

The purpose of this meetup was to bring artists, designers, technologists and creators together, mostly to just show off cool shit we’d found, seen or made ourselves. Myself, as a Data Scientist, spent most of my presentations such as they were explaining things like graph theory and machine learning concepts to bemused artists, while they schooled me on colour theory and explained in crushing detail how all my aesthetic choices were just plain wrong.

But at the end of the day, we weren’t sharing or talking about abstract aesthetics of visualisation, or the computational complexity of particular analyses; we were sharing our understanding of the real world around us; we spent a lot of time analysing our wee city here, from geography and connectedness, and mapping that to “historical issues”, and fun fact on that one, the westlink was originally planned to be an overpass, but the Army Corp of Engineers and the RUC at the time **really** liked the idea of being able to shut West Belfast off from the rest of the city at 3 choke points rather than dozens… Which is also why if anything goes wrong with the westlink, the entire city is shafted.

![alt_text](images/NIDC-201920.png "image_tooltip")

Beyond looking at our environment, we also used the tools of math, technology and art together to understand our own lives and those of our families and communities, including an insightful journey in data-logging of Brian Douglas's kid, and using that information in a medical context to tell stories about trends that normally only parents can recognise, and that medical professionals often dismiss.

But apart from just learning each others crafts, part of the purpose of the meetup was to start forming connections and relationships across the barricades of tech.

And one of the relationships that developed was between the Farset community and the Digital Arts Studios, based in the Cathedral Quarter. We ended up working together on a programme that DAS were running called Future Labs which was explicitly a technical training programme for artists, developing workshops on everything from AI to Projection Mapping

![alt_text](images/NIDC-201921.jpg "image_tooltip")

Farset hosted one of the workshops about getting started with the Raspberry Pi, led by the dark wizard himself, where Visual and Sonic artists were given the space and opportunity to play with kit and prototyping equipment normally only sought out to

![alt_text](images/NIDC-201922.jpg "image_tooltip")

About 8 months ago, I was asked to join the board of Vault Artist Studios, an arts collective that used to be the Belfast Bankers who have since taken over the old tech on Tower Street in East Belfast.

![alt_text](images/NIDC-201923.jpg "image_tooltip")

This community of about 100 awesome and only slightly sane artists, designers, musicians, and practitioners are constantly pushing the boundaries of what’s possible, from building-scale marble runs and hula-hoop shows to good old fashioned analogue chip-tune visualisations and a totally legally power rated laser-dong throwers

![alt_text](images/NIDC-201924.png "image_tooltip")


This level of interdisciplinary collaboration is exceedingly rare, even in the arts world, and so far, if they let vote me back in to the board at the AGM next week, I hope to work to be a bridge between our wee worlds.


## Conclusions

It’s sometimes very intimidating to see these kind of projects and collaborations and say “I’m not good enough at tech to help them to do that” or “I’m not arty” or “I don’t know what to do?”



![alt_text](images/NIDC-201925.png "image_tooltip")


The fact is that these things all started off as conversations between a couple people, working out some kind of shared language for their problems, ideas and solutions, and just seeing where the rabbit hole takes them.

All it takes is a conversation. So I’m challenging all of you to find an arty friend or connection, and talk to them about your respective crafts, challenges, perspectives, and see if you can build something awesome together. It doesn’t have to be useful, change the world, or even be pretty; it can just be a bit of fun, seeing how the palettes of Data and Art clash and compliment.



![alt_text](images/NIDC-201926.png "image_tooltip")


You have a year, your time starts now. Thank you for your time, I’m accessible at all of these things, and I’m happy to take any questions you might have.
