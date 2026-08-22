---
title: "The AI Bubble Isn’t Bursting. Its Reflections Are."
date: 2026-08-22T10:30:25+01:00
categories: [AI, Security]
tags: [AI, application security, AppSec, DevOps, LLM, tokens, bubble, code generation, context, vibe coding, SAST, vulnerability management, Black Duck]
description: "Originally published on The AI Journal — Why the next chapter of AI security will be defined by tokenomics, sovereign models, and normalizing models as first–class software components"
---

*This post was originally published on [The AI Journal](https://aijourn.com/the-ai-bubble-isnt-bursting-its-reflections-are/) on August 19, 2026.*

*Why the next chapter of AI security will be defined by tokenomics, sovereign models, and normalizing models as first–class software components.* 

Every few weeks, someone asks me if the AI bubble is about to pop. That’s the wrong question to ask. There’s no  single “bubble” that will pop and send us back to the pre-GPT ‘stone  age’. Rather, there is an ecosystem of ‘AI bubbles’, each inflating on a different timeline, some combining and becoming more ‘stable’, others  getting frothy and ready to pop, and each with very different  consequences for the security leaders who have to live with the  outcomes. 

The use of AI isn’t going away; you can’t  put a genie back in a bottle. What is going to correct, sharply, are the derivative bubbles wrapped around it: the circular data center  investment cycles, the securitization of model providers, the treatment  of a handful of hyperscaler stocks as proxy bets on the entire  technology. Those are financial phenomena. The engineering reality  underneath is more interesting and, for CISOs and CIOs, considerably  more actionable. Welcome to the year of tokenomics. 

## **The end of the loss-leader era** 

For two years, enterprises have been  playing with generative AI on venture-subsidized subscriptions. The  playbook was familiar, the same one Uber ran when it rolled into a new  city: get everyone on the app, commodetize ‘mobility’ below cost with  amorphous VC fund cash, ramp up margins later when you’ve established a  dominant market penetration. And frontier AI labs have done exactly that with tokens. 

That era is over. Anthropic, OpenAI, and  Google have all quietly re-tuned their pricing, and the bills are  landing. I am familiar with organizations where individual power users  are generating monthly AI spend well into the mid-five figures. Not the  team. The user. Whether that spend is ‘justified’ is an engineering  management ‘can’ that’s been kicked down the road for the past two  years, but every CFO is about to make it a security and governance  problem too, because the fastest way to control cost is to control  access; and the fastest way to control access is to route it (or, choke  it) through policy. Further, shadow AI has gone from a hypothetical to a very real risk to IP and security in an age of highly virulent supply  chain threats. 

## **Sovereignty stops being a slogan** 

The second correction is geopolitical. For years, the frontier labs marketed their models by telling us how  dangerous they were. That was useful for valuations. It was less useful  once export controls, dual-use technology rules, and weapons-adjacent  legislation caught up. If you spend three years telling regulators your  product is a strategic weapon, you should not be surprised when they  treat it like one. 

The response from the rest of the world  has been rational, and in some cases overdue. Europe is standing up  sovereign clouds. France has Le Chat. Gulf states and several countries  across Asia that have quietly invested in sovereign LLM capability for  the last three to five years are barely blinking at the latest access  debates, because they built in preparation for this. Even historically  aligned partners like the UK are drawing up backup plans. 

For enterprise buyers in regulated sectors such as defense, finance, healthcare, and critical infrastructure, this is not abstract. If your AI provider is a single US-headquartered  company and your regulator sits in Frankfurt, Riyadh, Singapore, or  London, you already carry a supply-chain risk. You just may not have  priced it yet. 

## **The pendulum swings back to local** 

The good news is that the technical answer is arriving faster than the policy answer. The competency gap between  frontier closed models and the leading open-weight models like Llama,  Kimi, Qwen, DeepSeek, and their descendants, is narrowing down to a  quarter or two rather than ‘3-5 years behind’ as has occasionally been  claimed. This evolution is a consequence of how the global academy works rather than some kind of ‘conspiracy against commerce’; Researchers  don’t get promoted for keeping secrets. They get promoted for  publishing, and for proving their approach beats the next lab’s.  Openness compounds. 

Combine that with a decade of aggressive  silicon investment by Apple, Google, and the broader ecosystem, and you  get a specific outcome: developer and workstation hardware that can run  capable models locally, without a round trip to somebody else’s data  center. We have seen this movie before. Computing has spent sixty years  oscillating; from mainframe to minicomputer, desktop to internet, mobile edge to cloud compute — and we are about to swing back again. 

For security architects, that is both a  gift and a warning; A gift, because local model execution shrinks the  data-exfiltration surface of AI-assisted work; your prompts, your code,  your customer records no longer have to leave the perimeter to deliver  value; but also a warning, because the model itself is now inside your  development or build system, and you need to treat it accordingly. 

## **Treat the model like a giant binary dependency** 

The single most useful mental shift I can  offer security and engineering leaders right now is this: stop treating  LLMs as magical services and start treating them as giant, opinionated,  non-deterministic, dependencies. Because that’s what they are. They are  components of your software. They ship with a version, a provenance, a  license, a set of ‘advertied’ behaviors, (along with a set of unknown  ones…), and a supply chain that terminates somewhere you probably cannot audit. 

Everything your organization already knows how to do for third-party components such as SBOM discipline,  provenance tracking, vulnerability ingest and management, license  review, and deprecation planning applies directly. The industry spent  fifteen years learning how to secure open-source software supply chains. That muscle memory transfers. You don’t need a brand new governance  regime for AI; you need to extend the one you have. You need to weave AI into the fabric of your security value chain. 

The trick is not to draw the governance  boundary around ‘AI’ as a category; that boundary is useless and will be obsolete in eighteen months. Draw it around the data. Know what you  have, at what classification, at what need-to-know level, at the  attribute level, and not just the dataset level. GDPR, stripped of its  scariness, asks exactly one question: do you know what data you have,  and why? Answer that well, and most of your AI governance falls out of  it for free; at its core the EU’s AI Act is asking the same question; do you understand what AI systems are part of your operations, and do you  have controls in place to make sure that usage is safe and transparent  for your customers, vendors and regulators. 

## **Three moves, starting now** 

If I were briefing a board this quarter, I would give them three things to track. First, watch your AI unit  economics the way you watch cloud spend, as they are about to behave the same way. Second, assume at least one meaningful workload will need to  move to a sovereign or local model within eighteen months, and start the architecture work now, not after compliance asks. Third, retire the  fantasy that AI is a separate discipline. It is software. Govern the  data, secure the supply chain, version the models. 

The froth in AI narratives is going to  settle one way or another; be it popping or gradually lowering the  temperature. The whiplash around it will correct. The technology itself  will keep getting more useful, more local, and more embedded in the  software you already ship. The organizations that come out of this cycle strong will be the ones that stopped treating AI as an event and  started treating it as a component. Auditable, defensible, and  buildable. In security, that is the only kind of magic that has ever  mattered. 
