---
categories:
- Commentary
comments: true
date: 2013-05-28 12:08:23+00:00
slug: those-who-can
tags:
- Education
- Python
title: Those who can...
---

I was digesting "[The Design of Design](http://www.amazon.co.uk/Design-Essays-Computer-Scientist/dp/0201362988)" by Fred Brooks as a bit of holiday reading, which talks in great depth about the nature of [technical](http://www.cs.unc.edu/~brooks/DesignofDesign/experiences.html) and [architectural](http://www.cs.unc.edu/~brooks/DesignofDesign/kitchen_design_notes.pdf) design from a practical perspective, and it made me thinking about my own experience and the "future" of that experience. Blessing or curse, due to my inability to say no and (publically) boundless <del>patience</del> exploration of a range of areas, in technology, security, academia, business, and society; several people have made flippant, off the cuff comments about some form of predicted success, usually financial or technical.

Reflecting on this, along with the narrative of DoD, I rested on a platitude that I'd used on many many occasions, mostly as a spear to lob haphazardly at teachers and educators for being 'lesser'.

> He who can, does;
He who cannot, teaches.

_[George Bernard Shaw](http://www.phrases.org.uk/meanings/176500.html)_ - Man and Superman, 1903

On reflection this just doesn't cover it.

I've recently been playing with the concepts of [Unit Testing](https://en.wikipedia.org/wiki/Unit_testing) and [Code Coverage](http://stackoverflow.com/questions/195008/what-is-code-coverage-and-how-do-you-measure-it), and [Continuous Integration](http://martinfowler.com/articles/continuousIntegration.html) in scientific computing, constantly endeavouring to maintain logical integrity of the simulation systems I operate as part of my research, so refactoring this platitude into pseudocode (i.e. OO Python), we can get...


    if self.can_do():
        self.do();
    else:
        self.teach()

Read that again; we are logically requiring teaching to be done by the incapable. From a systems design perspective, it looks like the Shaw missed something (deciding whether he was being sarcastic, cynical, or just pessimistic is a game for better literary minds than me);

Doing something is, more often than not, 'easier' that teaching it. Go to a local [Code Club](http://www.codeclub.org.uk/) or [Coder Dojo](http://coderdojo.com/) and try it sometime. It's quite frustrating, unless you are well practiced in explanation.

The ability to take an internalised process, extract the isolated kernel of 'experience', and to refactor and externalise the context within which that 'experience' operates, as well as how to arrive at both the 'experience' and the context, is exponentially more difficult than just 'doing it'.

If I was to now re-architect that platitude for the greatest technical, social, and cultural benefits, I'd make a few structural changes.


    while():
        if self.can_teach():
            self.teach()
        else:
            try:
                self.do()
            except Failure as experience:
                self.reflect(experience)
                continue

This also combines another of the traits exposed not just in DoD but in Paul Graham's "[Hackers and Painters](http://www.amazon.co.uk/Hackers-Painters-Big-Ideas-Computer/dp/1449389554/ref=la_B001ILHE5O_1_2?ie=UTF8&qid=1369736411&sr=1-2)" that I've also been digesting recently; Failure is fine, it is the reflection on failure and the recovery from failure to try again is more important.

And as your experience grows, you will eventually be able to teach, be it taking a [CoderDojo](http://fsl-dojo.eventbrite.com/), writing a book, taking on a lectureship, or just writing a blog.
