---
author: admin
date: 2017-09-21 19:05:52+0100
layout: post
tags:
- human factors
- complexity
- user experience design
- human cognition
- phd
- autonomy
- adaptive automation
- ml
- decision support systems
- information overload
- research
- HCI
- ai
- human-machine interfaces
- autonomous systems
- distributed decision making
- cognitive biases
title: Human Factors related to Trusted Operation of Autonomous Systems
---

# Preface

It's nearly a year to the day since I passed my Ph.D Viva (And since I last updated the blog...), so I thought
it'd be fun to very-gently tidy up one of my appendices that's a bit
relevant to current stories about the end of the world and machines
taking over and such.

It's a piece of work that I enjoyed researching and had originally had
as a significant part of the main [thesis](https://github.com/andrewbolster/thesis/releases/download/v1.0/Thesis.pdf), but it just didn't fit in
anywhere sensible, so it got stripped to it's bare minimum and kicked to the end.

If there's an interest in this stuff, I'll have a go at revisiting the most painful document of my career and tear out the interesting bits!

So without further ado, here's a rant about how human factors and HCI
impact human/AI teams.

---


This [work](https://github.com/andrewbolster/thesis/releases/download/v1.0/Thesis.pdf) has largely considered autonomous systems as entities of wider
systems, implicitly involving human operators/agents in some part of the
desired operation. We refer to these systems as Autonomous Collaborative
Systems (ACS). As described in [Chapter 2](https://github.com/andrewbolster/thesis/releases/download/v1.0/Thesis.pdf)
Operational Trust has two main aspects, trust in the system to behave as
expected and trust in the interfaces between systems (human/machine and
machine/machine). Of all of the interfaces in an Autonomous
Collaborative System, the most problematic is that arguably that between
the ACS and the human operator / team of operators. [Cummings et. al. (2010)](http://journals.sagepub.com/doi/abs/10.1518/155723410X12849346788660) identified
the main challenges to Human Supervisory Control (HSC), summarised below:

Information Overload
---
---
---
---
---
---
--

Operator efficiency exhibits an optimum at moderate levels of cognitive
engagement, above which cognitive ability is overloaded and performance
drops (Otherwise known as the Yerkes-Dodson Law). Additionally, in the
case of under-engagement, operators can fall foul of boredom, and become
desensitised to changing factors. *However, predicting this point of
over-saturation is an open psychophysiological research problem.*

Adaptive Automation
---
---
---
---
---
---
-

Automation is well tailored to consistent levels of activity. This is
quite simply not the case in many domains. Particularly in defence and
military applications, activity is characterised by long periods of
“routine” punctuated by high intensity, usually unpredictable, activity.
At those interfaces between “calm” and “storm”, where real time
situational awareness is imperative, temporary Information Overload is
highly probable. Adaptive Automation enables autonomous systems to
increase their Level of Automation (LOA) based on specific events in the task environment, changes
in operator performance or task loading, or physiological methods. It is
taken as given that for routine operations, and increased LOA reduces
operator workload, and vice versa. However, this relationship is highly
task dependent and can create severe problems in cases of LOA being greater,
or indeed lesser, than is required. In the cases of overly-high LOA,
operator skill is degraded, situational awareness is reduced as the
operator is not as engaged, and the automated system may not be able to
handle unexpected events, requiring the operator to take over, which,
given the previous points, is a difficult prospect. Alternatively, in
sub-optimal LOA, Information Overload can result in the case of high
intensity situations, but also the system can fall foul of
overly-sensitive human cognitive biases, false positive pattern
detection, boredom, and complacency in the case where less is going on.
Therefore, as a corollary to Information Overload challenges, there is a
need to define the interrelationship between levels of situational
activity (or risk) and appropriate levels of automation. *Under what
circumstances can adaptive automation be used to change the LOA of a system?
Does the autonomous system or the human decide to change LOA ? What LOAs are
appropriate for what circumstances?*

Distributed Decision Making
---
---
---
---
---
---
---
---
---


In a modern, non-hierarchical, often distributed or cellular military
management system (Network Centric Warfare doctrine for example), tools
are increasingly being used to mitigate information asymmetry within
command and control. A simple example of this is shared watch-logs in
Naval operations, providing temporal collaboration between watch-teams
separated in time. The DoD Global Information Grid is another example of
a spatial collaborative framework. Recent work has demonstrated the
power of collaborative analysis and human-machine shared sensing
technologies even with low levels of training on the part of the
operators providing superior results and resource efficiencies than
either humans or machines alone in survey and search-and-rescue
scenarios ([Ahmed et. al. (2014)](https://www.researchgate.net/publication/292850135_Enabling_robust_human-robot_cooperation_through_flexible_fully_Bayesian_shared_sensing)). As these temporal and spatial collaboration
tools increase in complexity and ability, decisions that previously
required situational awareness that was only available at higher
echelons within the standard hierarchy are available to commanders on
the ground, or even to individual team members, enabling the potential
for informed decisions to be taken faster and more effectively, enabled
by automated strategies to present relevant information to teams based
on the operational context. However there are a range of operational,
legal, psychological and technical challenges that need to be addressed
before confidence in these distributed management structures can be
established. Studies into situational awareness sharing techniques
(tele-present table-top environments, video conferencing, and
interactive whiteboards) have generally yielded positive results,
however investigations into interruptive-communications (such as instant
messaging chat) have demonstrated a negative impact on operational
efficiency. In short, the biggest problem with distributed decision
making in the context of supervisory systems is that *there is no
consensus on whether it is advantageous or not, and what magnitude of
operational delta is introduced, if any.*

Complexity
---
---
---
-

Beyond simple Information Overload, increasing complexity of information
presented to operators is having a negative effect on operational
efficiency. In HSC, displays are designed to reduce complexity, introducing
abstractions with an aim to presenting the minimum amount of information
to the operator required to maintain an accurate and up-to-date mental
model of the environmental and operational state. This has led to the
development of many domain specific decision support interfaces,
however, in academic research, there has been nothing but ‘mixed
results’. One commonly raised negative is the general bias on the “cool
factor” of interfaces. Immersive 3D visual, aural, or haptic interfaces
that at first appraisal seem to provide more approachable information to
the operator, and are indeed tacitly preferred by operators in use.
However, there has not been any evidence to demonstrate performance
improvement when using these tools, and in-fact, *improving the
“fidelity” of the interfaces has led to operators’ overly-relying on
these representations of the environment rather than remaining engaged
in the environment.*

Cognitive Biases and Failing Heuristics
---
---
---
---
---
---
---
---
---
---
---
---
---


In many areas, operators are required to make rapid decisions with
imperfect information, driven by massively increased information
availability and rates of change in areas such as battlefield tactics
and global finance markets. However, Human decision making isn’t always
rational (especially under pressure), and operators use personally
derived heuristics to make “rational shortcuts”. This is a double edged
sword, where these heuristics can be employed to greatly reduce the
normative cognitive load in a stressful situation, but also introduce
destructive biases, where these shortcuts make assumptions that don’t
bear out in reality.

For example, in the context of decision support systems, “Autonomy Bias”
has been observed as a complement to the already well known
“Confirmation Bias”[^1] and “Assimilation Bias”[^2], where operators
that have been provided with a “correct” answer by a decision support
system do not look (or see, depending on perspective) for any
contradictory information, and will unquestionably follow, increasing
error rates significantly.

This behaviour isn’t only the reserve of decision support systems, but
also in the generic allocation of operator attention; scheduling
heuristics are used to decide how much time tasks should be worked on,
and time and again, humans are found to be far from optimal in this
regard, especially in time-pressured scenarios where these heuristics
are in even more demand. Even when operators are given optimal
scheduling rules, these quickly fall apart, often due to primary task
efficiency degradation after interruption. This highlights a critical
interface in the adoption of complex autonomous systems that still
demand ‘Man in the loop’ functionality; if a system is required to have
full-time concentrated supervision (e.g. flying a UCAV), but also
event-based reactive decision making (e.g. alerts from non-critical
subsystems), both tasks are negatively impacted. In an assessment of
factors influencing trustutono in autonomous vehicles and medical
diagnosis support systems, Carlson et al also identified that a major
factor in an operator or users’ trust in a system was not only dependant
on past performance and current accuracy but also on “soft factors” such
as the branding and reputation of the manufacture /
designer ([Carlson et. al. (2014)](https://www.researchgate.net/publication/288091386_Identifying_factors_that_influence_trust_in_automated_cars_and_medical_diagnosis_systems)). Further, autonomous decision support /
detection / classification systems have an “uncanny valley” to overcome
in terms of accuracy, in that there is a dangerous period when such
systems are used but not perfect, but operators become complacent,
causing an increased error rate, until such a time that those autonomous
systems can match or exceed the detection rates of their human
counterparts.

Conclusions
---
---
---
--

The separate fields of automation and user experience design have been
running in parallel for several years. However, there will soon come a
point (in some cases already past) where human operators must place
their “Trust” in autonomous systems to not only accomplish what they
want and what they expect, but to do it in a way they are
psychologically comfortable with. Further, there is the aspect of how
are (or should) autonomous systems being “trained” in how to deal with the
systematic failings in human cognition? At what point does the machine
need to trust the _operator_ before it performs “responsibly” in the face
of a possibly irrational or cognitively broken usage, and if so, how can
it communicate this state to the operator or some higher order command
structure?

These are massively open research questions I didn’t
get to attempt to answer anywhere other than the appendices and the pub,
and there is no easy avenue to start from, so this author suggests
Asimov’s [“The Robot Collection”](https://www.amazon.co.uk/Complete-Robot-Isaac-Asimov/dp/0586057242).

[^1]: Confirmation Bias is the tendency for people to preferentially
    select from available information that information that supports
    pre-existing beliefs or hypotheses.

[^2]: Assimilation Bias is often thought of as a subset of Confirmation
    Bias, whereby it specifies that instead of seeking out information
    supporting of current views, any incoming data is interpreted as
    being supportive of a particular view without questioning that view,
    even if it appears contradictory.
