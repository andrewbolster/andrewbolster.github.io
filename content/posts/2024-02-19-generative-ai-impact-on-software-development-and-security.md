---
date: 2024-02-19T12:54:00+00:00
layout: post
categories: [AI, Software Engineering, Security]
tags:
- AI
- 'Application Security'
- Cybersecurity
- LLM
- 'Machine Learning'
- 'Software Development'
- cybersecurity
title: 'Generative AI: Impact on Software Development and Security'
---

_This was a piece written as part of my work at Synopsys SIG and was published in a [few](https://ap-verlag.de/generative-ki-hat-enorme-auswirkungen-auf-softwareentwicklung-und-softwaresicherheit/86448/) [places](https://www.teiss.co.uk/artificial-intelligence/generative-ai-software-development-and-security), but I liked it and wanted to keep it... At least until the lawyers chase me down._

Since the release of ChatGPT, the technology industry has been scrambling to establish and operationalise the practical implications of these human-level conversational interfaces.
Now, almost every major organisation is connecting their internal or product documentation to a large language model (LLM) to enable rapid question-answering, and some are starting to wade into the use of generative AI systems to aid in the design and creation of new technical solutions, be it in marketing content, web application code or chip design.
But the hype has had its sharp edges as well; the word ‘hallucination’ is never far from the lips of anyone discussing chatbots, and the assumptions that people have around human-like language being equivalent to ‘common sense’ have been seriously challenged. Potential users of LLM derived systems would be wise to take an optimistic but pragmatic approach.
The release of the first major public Large Language Model (LLM) set off successive waves of amazement, intrigue and often, fear, on the part of a public unprepared for the surprisingly ‘human’ behaviour of this ‘chatbot’. It appeared to communicate with intentionality, with consideration, and with a distinctively ‘natural human’ voice. Over successive chat-enquiries, it was able to ‘remember’ its own answers to previous questions, enabling users to build up coherent and seemingly complex conversations, and to attempt to answer surprisingly ‘deep’ questions.
Yet, these systems should be treated as one would treat a child savant; it might know all the right words in the right order but may not really have the experience or critical thinking to evaluate its own view of the world; the outputs of these systems have not ‘earned’ our institutional trust, and care must be taken in leveraging these systems without significant oversight.
## Emergence of Generative AI
A later revelation was that as successive versions of these LLMs were released (ChatGPT by OpenAI, Bard by Google, Claude by Anthropic, and the open source LLaMA model by Meta), use expanded from playful simulation natural language conversations with virtual ‘oracle’, to constructing poetry from abstract documentation, laying out personal statements and cover letters for job seekers, designing presentations for speakers, and summarising articles for journalists (and sometimes writing them…). As ‘prompt engineering’ became one of the most searched for terms of the year, these models started to be used to generate any kind of textual, visual, or audio content imaginable.
This ‘generative AI’ capability quickly gained the attention of both security researchers and cyber-criminals; for many forms of online fraud and cyber-crime, the ‘barrier to entry’ is the cost of having a human attempt to convince another human to shuffle some asset around, whether it’s convincing an IT helpdesk to reset your password, convincing a befuddled computer user to pay for tech support via untraceable gift vouchers, that your CFO really needs you to pay this unapproved invoice ‘right now’, or enticing that optimistic ‘investor’ that a foreign ‘prince’ really will pay you back.
Now, such interactions could be automated on an unheard-of scale, at a predictable price.

## LLM’s in Software Development; Friend? Foe? Frustration?
Of particular interest to the cybersecurity industry was the emergence of GitHub Copilot; a LLM based tool that was able to analyse code, and propose additions or corrections based on ‘prompts’, either directly from a chat-like interface, or as a form of advanced ‘code-completion’. Security leaders began to reflect on the potential risks of this utility; not just only in the surface level estimation of ‘Will these LLM’s always generate “secure” code?’, but on the deeper implications for the software development industry.
If the risk to software integrity was just the risk introduced by LLM generated code having some occasional, hallucinated, bad security practices, the resolution could have been simple enough; lock it down. And indeed, it has been observed that many organisations took this approach as they were developing their LLM response policies.
But rather, it was recognised that in the complex world of software engineering, where well intentioned developers pulling code from the internet to fix a hair-raisingly-frustrating problem is not so much as a ‘meme’, insomuch as it’s recognised industry strength, the introduction of these LLM’s into any part of the software supply chain infers significant downstream risks. (This fact is recognised repeatedly in the UK NCSC’s Guidelines on Secure AI System Development released 27th Nov).
It gets worse; we have already seen sites like Reddit, StackOverflow, Wikimedia, and more have taken steps to block content that ‘appears to be’ generated by such LLM’s; but the guidelines for assessing that ‘appearance’ are extremely subjective, down to things like ‘speed of response’ rather than quality or correctness of content. Google and others have effectively thrown their hands in the air by saying that they will ‘watermark’ generated content, implying that they have not identified a suitably generic method for detecting LLM generated content, so they have to police it on the ‘supply side’.
These actions imply that the internet may already be ‘infected’ with LLM derived content, which, returning to the software development space, now means that that ‘intern with access to the internet’ is just as dangerous as that un-trusted LLM.

## How to approach security
Taken together, LLMs muddy the software development water in many ways, and security leaders have little choice but to expand their DevSecOps positions to encompass any ML or AI derived features and content and must be proactive in identifying where that risk lies in their own SDLC’s.
It’s no longer simply a case to run a scan against your codebase and declare that you are ‘safe’; increasingly, security leaders are pushing for a wider, more holistic view of security that includes these upstream AI/ML risks. Furthermore, ‘Application Security Posture Management’ must include validating the operation, deployment, and even training data origin, as a first-class part of the software development lifecycle, rather than just an experimental afterthought.
Ultimately, organisations will have to take a fundamentally different approach to application and service security; rather than just having build- or deploy-time scanning to ‘attest’ that an application is secure, organisations will have to regularly and repeatedly validate that the behaviour of their third party service integrations (and therefore, their own services) still behaves the same way as expected.
