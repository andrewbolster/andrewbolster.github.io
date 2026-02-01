---
date: 2021-03-24T06:06:00+00:00
layout: post
tags:
- Cybersecurity
- Data Science
- WhiteHat Security
- Machine Learning
- AI
- Artificial Intelligence
- Big Data
title: 'Dr StrangeBot: Or How I Learned to Stop Worrying and Trust Machine Learning'
---

> This post was originally published as part of my role at WhiteHat Security
> Links have been added for context/comedy/my own entertainment, but no content has been modified


Beneath the cynicism, hyperbole, market–making and [FUD](https://www.urbandictionary.com/define.php?term=Fud); the strategic importance of AI in Cybersecurity is only constrained by us ‘meatbags’.

Being a data science practitioner in the cybersecurity space has been a double–edged sword for several years. On the one hand, with the proliferation of automated security testing, network IDS advances, the sheer growth in traffic and the threat surface of our increasingly complex, interconnected application development practices, these roiling oceans of flotsam and datum are everything our data hungry little hearts desire. Related innovations in data engineering in the past decade mean that questions that had previously only lived in the craven dreams of executive officers and deranged analysts are now the kind of tasks that we hand off to interns to make sure they have correctly set up their workstations.

But this glut of “Big Data” and computational wizardry leads inevitably to the other side of that coin; the zombie-esque re-emergence of casualties from the last “[AI Winter](https://link.springer.com/article/10.1007/s13347-020-00396-6),” proselytising that “now is the time.” Revolutions in highly specific fields like natural language processing and computer vision previously only imagined in big budget Sci-Fi tentpole movie franchises were now accessible with URLs like [ThisCatDoesNotExist](https://thiscatdoesnotexist.com/) and QuickChat.ai with links to the code on Github for all to emulate.

“This isn’t your parents AI,” was the rallying call of the entire B2B software engineering industry, “this time it’s different,” and AI would make it all better, and “no-code” AI / ML deep learning adversarial recurrent network solutions on the blockchain were the proverbial White Whales that just needed to be chased through these oceans of data. And finally, after years of promising research, Captain Ahab would have his prize of Human-Like Intelligence, able to take ‘meatbag’ expertise, judgement and wisdom, and scale indefinitely, or as much as your cloud compute budget could tolerate.

“Powered by AI,” has become an albatross across many parts of the software engineering industry, no more so than in cybersecurity. Considering the fundamental premise of our industry is ‘computer systems can be bent to induce unintended behavior’, the magic wand of ‘AI’ often ends up being relegated to a square in our socially distanced buzzword bingo cards.

The real opportunity for the techniques pioneered in the ‘Big Data’ and ‘Artificial Intelligence’ research spaces are already well voiced; “joining the best of human and machine intelligence,” but the question of how this is accomplished remains unclear at best and at worst is misleading.  

At WhiteHat Security, we have pioneered an [Active Learning](https://algorithmia.com/blog/active-learning-machine-learning) approach to our development of machine learning models that opportunistically takes tasks off our security experts’ work queues when that model has confidence in its assessment of a piece of evidence. These items are then either directly and invisibly actioned on behalf of our security team, or, on a probabilistic basis, the item still goes to our security teams to assess, along with the model’s assessment of that piece of evidence so that we can cross verify the ongoing performance of the models under test. This ensures that both that our security teams have the most ‘un-boring’ experience possible and that our models receive continual feedback so that performance or accuracy deviations can be quickly identified, and any models with reduced accuracy can be retrained and the old ones decommissioned rapidly without any loss of security oversight.

Within a standardized deployment and interaction architecture is a behind the scenes core approach. It is a “decision system” based on mutual trust between the Data Science capabilities of analysing and modelling data to use optimal techniques per scenario context. This means that our partners in the rest of the product organization can understand and rely on the “decision support systems” that we as a Data Science group release. Fundamental to this “decision support system” approach is that whatever techniques, tools, strategies, technologies or [technomancy](https://powerlisting.fandom.com/wiki/Technological_Magic) that are used to pre-process, clean, analyze and train models, that their integration is as simple as possible; a decision support system is fed some evidence, and it responds with a set of recommendations and related confidences.  

These specific confidences being expressed and exposed as part of the system fosters the development of a form of ‘trust’ between the decision support system, and the security practitioners that then makes decisions based on that data. And finally, when the decision support systems themselves have conflicting or low confidence in their assessments, not only are these borderline or edge cases raised with the security teams, but they’re also collated by our Data Science team, where they’re analyzed separately, and if any patterns can be observed in the ‘confusing’ evidence, these are raised with our R&D and security teams and new models are trained against this novel finding.

The intent is not to somehow replace or supplant the contextually informed human expert but rather to provide cognitive shortcuts and contextual evidence to empower them to make heuristic decisions on the edges.

AI, ML, Bots, Black Boxes, Decision Support Systems; whatever the phrasing, the place of these technologies in the modern cybersecurity landscape is simple; answer the easy questions for me and get out of the way, or give me enough contextual information and trusted advice to take on the hard questions myself.  

## Author Bio

Andrew Bolster Ph.D leads the Data Science group in WhiteHat Security. His professional and academic experience spans from teaching autonomous submarines to collaborate on port protection, [establishing guidelines](https://andrewbolster.info/2017/09/legal-considerations-for-trusted-autonomy.html) for military application of AI, using biosensors to monitor and communicate human emotions, establishing IEEE standards for applying [ethics in AI](https://andrewbolster.info/2020/04/is-your-ai-ethical.html), and curating data playgrounds for cybersecurity researchers and professionals to experiment with multi-terabyte streaming datasets for product innovation. In his “spare time”, he is a founding trustee of the [Farset Labs hackerspace](https://www.farsetlabs.org.uk/), and on the board of [Vault Artist Studios](https://www.vaultartiststudios.com/), both in Belfast, Northern Ireland

> Final fun note; this was my first time using Github's VSCode Codespaces as an online Markdown editing environment and it wasn't a disaster!
