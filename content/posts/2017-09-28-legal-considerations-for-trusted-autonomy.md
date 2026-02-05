---
cover:
  image: img/legal-considerations-for-trusted-autonomy.generated.png
date: 2017-09-28 18:02:12+0100
tags:
- AI
- Autonomous Systems
- Machine Learning
- Maritime
- PhD
- Research
- Robotics
title: Legal Considerations for Trusted Defence Autonomy
---

This is another short extract from the [Thesis](https://github.com/andrewbolster/thesis/releases/download/v1.0/Thesis.pdf) that I thought was particularly relevant given [recent](https://www.theguardian.com/technology/2017/sep/27/robots-destabilise-world-war-unemployment-un) [news](http://www.telegraph.co.uk/news/science/science-news/11633838/Killer-robots-will-leave-humans-utterly-defenceless-warns-professor.html) coverage of the dangers of autonomy and AI, particularly in the field of "killer robots".

# Legal Considerations in Design Trust

If there is one key feature of the application of robotics and autonomy
to the defence field that separates it from applications in commercial
and civil fields, it is the potential direct impact on life and safety.

The process of some entity, be it human or autonomous, to commit to the
decision to fire any kind of weapon is a critical one, and the
criticality of this decision making process weighs heavily on the
development of autonomous weapons systems and
platforms [^Defense2012][^Banks2010][^STANAG4586]. Key
challenges to autonomy in this space include accurate friend-or-foe
identification, rapid assessment of incoming threat, and discerning
“appropriate levels of force”, all of which are key parts of
international combat doctrine and law [^Lin2009]. Beyond these ethical
and operational challenges, one key piece of legislation that makes the
dissemination of fire control to autonomous weapons systems particularly
challenging; under the 1907 Hague Conventions [^HagueIV], lawful combat
requires any combatant “to be commanded by a person.”, and in
particular, The Martens Clause of that convention (originally introduced
in the earlier 1899 convention) specifically demands the application of
“the principle of humanity” in combat [^Ticehurst1997]. The problem
presented by these principles is that modern remote operation systems perform with the operator
“on-the-loop” for the majority of time, with on-board autonomy taking
over “simple” on-board processes such as local navigation, collision
avoidance, positioning etc.

Once this “on-the-loop” platform is in theatre, direct control must be
assumed before any fire-orders are given, otherwise commanders would be
in direct breach of the above conventions. Whether such breaches have
already occurred is outside the scope of this work, and as discussed in (the [Thesis](https://github.com/andrewbolster/thesis/releases/download/v1.0/Thesis.pdf) )
, this work is primarily concerned with actions that involve no fire
control what so ever. However, there is one potentially relevant area of
application to which these doctrines may arguably apply; a significant
area of application of maritime autonomy is in Explosive Ordinance
Disposal as part of Mine Counter Measures operations, i.e. mine-clearance
with explosive devices.
Current operational doctrine as well as currently in-testing systems utilise
autonomous survey and mine localisation, and then this information is used to
send in a human diving team to perform clearance, placing them at
extreme risk.

However, none of the above applies to this work and is presented for
context.

[^Defense2012]: US Department of Defence. (2012). Directive 3000.09, (3000). Retrieved from http://www.dtic.mil/whs/directives/corres/pdf/300009p.pdf
[^Banks2010]: Banks, A., & Bowman, N. (2010). A framework of requirements for the design and management of dependable network enabled capability system of systems. System of Systems. https://doi.org/10.1109/SOSE.2010.648
[^STANAG4586]: NATO Standardization Office. (2012). STANAG 4586 Standard Interfaces of UAV Control System (UCS) for Nato Uav Interoperability Ed: 3. Brussels, Belgium. Retrieved from http://nso.nato.int/nso/zPublic/stanags/current/4586eed03.pdf
[^Lin2009]: Lin, P., Bekey, G., & Abney, K. (2009). Robots in War : Issues of Risk and Ethics. In R. Capurro & M. Nagenborg (Eds.), Ethics and Robotics (pp. 49–67). AKA Verlag Heidelberg.
[^HagueIV]: Convention (IV) respecting the Laws and Customs of War on Land and its annex: Regulations concerning the Laws and Customs of War on Land. The Hague, (1907). Brussels. Retrieved from https://ihl-databases.icrc.org/ihl/INTRO/195
[^Ticehurst1997]: Ticehurst, R. (1997). The Martens Clause and the Laws of Armed Conflict. International Review of the Red Cross, 317. Retrieved from https://www.icrc.org/eng/resources/documents/article/other/57jnhy.htm
