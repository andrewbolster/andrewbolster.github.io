---
aliases:
- /2024/04/context-all-the-way-down-primer-on-methods-of-experience-injection-for-llms/
- /2024/04/context-all-the-way-down-primer-on-methods-of-experience-injection-for-llms.html
categories:
- AI
- Software Engineering
- Commentary
cover:
  image: img/context-all-the-way-down-primer-on-methods-of-experience-injection-for-llms.generated.png
date: 2024-04-29 20:58:00+00:00
tags:
- AI
- LLM
- Machine Learning
- NLP
title: '"Context all the way down": Primer on methods of Experience injection for
  LLMs'
---
Much hay has been made that LLM’s can be infinitely trained on infinite data to do infinite jobs, in an approach generally described as [‘LLM Maximalism’](https://explosion.ai/blog/against-llm-maximalism). This post is a bit of a braindump to explain my thought process in how to practically use LLMs in a safe way in production/client facing environments, with a little bit of a discussion as to where I see the current blockers to this in most organisations, and where organisations should be focusing investment to be able to meet these challenges without loosing their competitive edge/expertise.


## Black Boxes, Training, Fine Tuning, and the edge of computability

While LLM’s like ChatGPT do a respectable job at a lot of disparate tasks, the reason *why* they do a decent job of these diverse but ‘toy’ problems can be overlooked; they’re trained on the whole internet and with each iteration, spend a whole pile of often un-documented time going through Reinforcement Learning with Human Feedback (RLHF). These LLMs are nearly-perfect ‘do-anything and look realistic’ machines, because their ‘target function’, both in the pure training phase and in the RL phase, is to ‘look like a human responded’. Not an ‘expert’ or not someone that’s even ‘correct’, but just that the response doesn’t blow up the Turing Test.

This has been great/horrifying for ‘feels-like’ jobs like turning bullet points in to prose or vice versa, or even generic programming completion or authoring (thanks StackExchange), but this approach of ‘throw it all in the training data and GPU’s go brrrrr' is often a very expensive hammer to nail in a screw.

## Training

The reason why I say that is a fundamentally different issue (i.e., screw), is that trying to ‘teach’ the base LLM model about a given specific domain is possibly the worst form of information ‘compression’ imaginable, and fundamentally wastes a load of time, energy, money and GPUs.

LLM’s, like any neural network derived machine learning process are *just* big collections of big matrices (when someone says a model has X-Billion ‘Parameters’, each ‘parameter’ is a number in a massive set of multi-dimensional matrices aka tensors).

And the ‘training’ for these neural networks is *just* repeatedly running partial data through the model, comparing the model output to the sampled/expected data, and then (using very very clever math) trying to selectively ‘punish' parts of the model network for how *wrong* it was, without messing up any of the *other* training answers it has in it’s corpus.

So, the same piece of ‘training’ data is effectively compiled and recompiled over and over again in the model until it stops being ‘wrong’ (for a certain value of ‘wrong’, which is a whole art in and of itself…)

When people use the word ‘Training’, they usually mean that they are taking complete collection of input training data (aka training corpus), adding in your ‘domain specific content' like their own codebase or documentation to that training corpus, and then letting the GPU’s go brrrrr. Hopefully it’s clear that this is a stupid approach; because at the same time that the model is ‘learning’ that a “Cross Site Scripting vulnerability” and a “XSS vulnerability” probably refer to the same underlying concept and are thus, synonyms; it’s also learning that ‘cat’ and ‘dog’ are ‘mammals’ and ‘pets’, but ‘brick’ is something different.

## Fine-Tuning

The recognition of the wastefulness of this approach led directly to the concept of ‘fine-tuning’, which is a fancy way of saying ‘take an already trained model, and train it some more’; this way around you’re *only* training an already trained model on your ‘domain specific context’,
but it’s still fundamentally doing the same ‘punish/adjust/test' loop, baking the ‘experience’ into the mystical model matrices.

> :memo: I’m personally very dismissive of fine-tuning in most contexts, but one area where it is extremely valuable is in the area of giving a particular natural language model a ‘feel’ or ‘style’, but not necessarily focusing on or impacting the expected ‘knowledge’ of a model. Like a finishing school for making sure they speak english good.  This has valid opportunities for maintaining a consistent communication style for client facing usecases such as [REDACTED], but this fine-tuning should be the last optimization made to a solution, and requires the scale of data we have in [REDACTED] at the moment to even contemplate fine-tuning (and even then, the value of this ‘styling’ with respect to the investment required is arguable at the moment)


So, now there’s a whole pile of people using pre-trained models from `huggingface` etc and "fine-tuning" them to solve some particular task to questionable value.

## Prompt-Engineering

But where there were “real” successes was in a whole separate domain of interaction with LLM’s; Prompt Engineering.

As a light refresher; when you fire up [chat.openai.com](https://chat.openai.com) or similar, you’ve got a big blank chat screen and you enter a few lines of text and send that message to the backend Agent. This ‘message’ would be called a ‘User Prompt’ or ‘User Message’ and unsurprisingly, it’s you telling the underlying agent what you expect to get back. That agent then responds with its own conversational response, generally termed an ‘Agent’ or ‘AI’ message.

```
> User: Hello AI, what's you're name?
>
> ---
>
> AI: I dunno dude, I'm stuck in this black box, I don't even know what a 'name' is!
```

> :memo: This is technically an example of ‘Zero-Shot’ learning, i.e. the Agent was not given any context specific examples for what a ‘good’ answer looks like

However, there are almost always additional hidden  “System Prompts” that effectively ‘prefix’ the User Prompt going in to the first invocation of of the agent. These prompts can be considered as ‘hints’ to kick start the model execution (this will be explained in a bit… just bear with it)
```
> System: You are a helpful AI bot, your name is Harlan and you write dystopian fiction in the style of the author Harlan Ellison
>
> User: Hello AI, what's your name?
>
> ---
>
> AI: I am Harlan, and I must scream
```

> :memo: In this contrived example, note that the AI’s response is pulling both from the system prompt and from the underlying context about Harlan Ellison’s body of work which, to quote Chat GPT: _“If the text is not in the public domain and not part of the training dataset licensed or created by OpenAI, it would not be directly used for training. Instead, the model would learn about such works indirectly through summaries, analyses, and discussions available in the public domain or in the training data.”_

Developers and system integrators can not only add additional `System` prompts (I like to think of these as a ‘Narrator’ giving stage directions before a scene starts, but you can sort out your own headcanon). but can also give examples of User/AI conversations in advance of ‘real’ user interaction.

> :memo: This would be an example of ‘Few-Shot’ (or ‘One shot, if only one example was given’)

```
> System: You are a helpful AI bot, your name is Harlan and you write dystopian fiction in the style of the author Harlan Ellison
>
> User: Why don't they play poker on the computer in "I Have No Mouth, and I Must Scream"?
>
> AI: Because every time they try, the computer insists on being the dealer and always deals a hand of despair!
>
> User: What's Harlan Ellison's favorite way to start a story?
>
> AI: With a typewriter, a strong opinion, and absolutely no apologies!
>
> User: Hello AI, what's your name?
>
> ---
>
> AI: I am Harlan, and I must scream
```

> :memo: _This is important to conceptualize;_ as far as the AI is concerned there is _no difference whatsoever_ between a ‘User:’ message included in the context as a form of prompt engineering, or a ‘real’ human user input message. Yes, this is ironic.

## Context and Tokens

Each invocation of the underlying agent is being fed the whole conversation history as its “Context”, and indeed, is adding its own partial-responses as they’re being generated to this ‘Context Window’ as it’s answering your prompts. This “Context Window” is around 2-4 thousand ‘tokens’ in GPT3/3.5 or 8k in GPT4, which roughly translates to around 1,500 words in English.

This ‘context window’ is often used as the billing metric for SaaS LLM invocations, such that a query with a very small context window with only a few tokens like “Hello AI, what is your name?” with 8 [tokens](https://platform.openai.com/tokenizer) would be charged differently than the full prompt including the system prompt above is around 45 tokens.

> :memo: Response token lengths are usually billed as well but are also generally configurable depending on the model you are invoking, but that’s an exercise for the reader

## Prompt Placeholders

One useful “tool” of prompt engineering is that most LLM’s “recognize” placeholders in examples where you might want to sanitize or generalize particular prompt data; for instance, if you were prompting a model based on a customer interaction, you might take a Agent-Client chat conversation, and remap it to a ‘AI-User’ interaction and use it as a prompt, but blanking out sensitive / specific data.
```
> System: You are a helpful and conscientious customer success manager, motivated to make your clients applications and services as safe and stable as possible
>
> User: Hi, this is {contact_name} from {client_name}, and we've been having trouble with XSS findings on our site, what can we can we do to prevent these in future?
>
> AI: Hi {contact_name}, I'm sorry to hear that, let me help you; it looks like you've had several XSS findings on {target_name} in the past 6 months. We would recommend that you assess your client-side Javascript UI library dependencies and ensure that you are sanitizing your inputs
```
Using this “Prompt”, the agent will replicate similar responses to similar structures without getting stuck in the context of a particular customer.

> :memo: This is not *really* templating as in Jinja or Python f-strings, but the `{}` are enough for the models tokenizer to treat these tokens are something separate from the standard language corpus and thus, avoid any accidental correlations to particular instances of names.

## Retrieval Augmented Generation

Retrieval Augmented Generation (RAG) takes a completely different approach to providing an LLM-based Agent with non-training-corpus experience/knowledge, and while it sounds slightly magical; it’s fundamentally really simple.

Give the LLM it’s own search engine.

While “simple”, the reason why this is at the end of this “primer” is that it also gently changes the mental model for how LLMs interact. Throughout this discussion, the LLM Agent has been treated as a [blind parrot driven by trained matrices](https://en.wikipedia.org/wiki/Stochastic_parrot) and tokens that just regurgitates whatever sequence of tokens is “least surprising” for a provided context, and this is still true, but the ‘provided context’ can be augmented in constructive ways.

RAG is a method for greatly expanding the “real” Context Window of an LLM by *almost* creating multiple phases for generating the prompt context for a given invocation, but it does it by ‘cheating’ a bit.

Consider the below `prompt` string

```
> You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question at the end. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
>
> Context: {context}
>
> Question: {question}
>
> Answer:
```

> :warning: **Warning: This time the `{placeholders}` are actually string-replacement placeholders!**

Observant readers will note that “Just say you don’t know” is about as reliable as “thoughts and prayers” and in no way guarantees that an LLM even knows what it doesn’t know; as such in any production/client-facing system that you might care about, additional steps to verify and validate responses should be put in place. (all adding additional potential costs…)

A contrived Python example of how to use this prompt is below

```python
messages = prompt.invoke(
  {"context": "filler context", "question": "filler question"}
)
response = messages[-1]
```

In this manner, developers can present additional ‘context’ to the LLM by populating the prompt string at invocation time by replacing the `{context}` placeholder, **and** if the context wasn’t sufficient to confidently answer the question (the meaning of ‘confidence’ in the context of LLM’s is a whole different minefield I’m not touching right now), it’ll say so.

The crux of RAG is identifying relevant context from a much much larger source corpus that could be viably trained against, or indeed included blindly in the invocation context window.

This is usually accomplished by taking some ‘embedding’ of the tokenized question itself and then looking in a database, document store, or other indexed environment to identify the most relevant pieces that fit into the desired context window. This process is operated by a ‘Retrieval Agent’ or just ‘retriever’.

> :memo: Example cherry-picked from [here](https://python.langchain.com/docs/use_cases/question_answering/quickstart "https://python.langchain.com/docs/use_cases/question_answering/quickstart")

Given the Question `"What is Task Decomposition?"`, and using text extracted from a [single webpage](https://lilianweng.github.io/posts/2023-06-23-agent/) hitting around 10k tokens, there is no way the full text could reliably fit into the context window, so the text from this page is chunked up and keyed against the same OpenAI Embeddings used by the underlying OpenAI model.

Based on the previously discussed context prompt, below is the actual prompt that is invoked by the agent to the LLM backend;

```
> Use the following pieces of context to answer the question at the end.
> If you don't know the answer, just say that you don't know, don't try to make up an answer.
> Use three sentences maximum and keep the answer as concise as possible.
> Always say "thanks for asking!" at the end of the answer.
>
> Fig. 1. Overview of a LLM-powered autonomous agent system.
> Component One: Planning#
> A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.
> Task Decomposition#
> Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.
>
> Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.
>
> Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.
>
> Resources:
> 1. Internet access for searches and information gathering.
> 2. Long Term memory management.
> 3. GPT-3.5 powered Agents for delegation of simple tasks.
> 4. File output.
>
> Performance Evaluation:
> 1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.
> 2. Constructively self-criticize your big-picture behavior constantly.
> 3. Reflect on past decisions and strategies to refine your approach.
> 4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.
>
> (3) Task execution: Expert models execute on the specific tasks and log results.
> Instruction:
>
> With the input and the inference results, the AI assistant needs to describe the process and results. The previous stages can be formed as - User Input: {{ User Input }}, Task Planning: {{ Tasks }}, Model Selection: {{ Model Assignment }}, Task Execution: {{ Predictions }}. You must first answer the user's request in a straightforward manner. Then describe the task process and show your analysis and model inference results to the user in the first person. If inference results contain a file path, must tell the user the complete file path.
>
> Fig. 11. Illustration of how HuggingGPT works. (Image source: Shen et al. 2023)
> The system comprises of 4 stages:
> (1) Task planning: LLM works as the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task type, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.
> Instruction:
>
> The AI assistant can parse user input to several tasks: [{"task": task, "id", task_id, "dep": dependency_task_ids, "args": {"text": text, "image": URL, "audio": URL, "video": URL}}]. The "dep" field denotes the id of the previous task which generates a new resource that the current task relies on. A special tag "-task_id" refers to the generated text image, audio and video in the dependency task with id as task_id. The task MUST be selected from the following options: {{ Available Task List }}. There is a logical relationship between tasks, please note their order. If the user input can't be parsed, you need to reply empty JSON. Here are several cases for your reference: {{ Demonstrations }}. The chat history is recorded as {{ Chat History }}. From this chat history, you can find the path of the user-mentioned resources for your task planning.
> Question: What is Task Decomposition?
> Helpful Answer:
```

This is now “only” around 900 tokens and elicits the following response after 1 invocation.
```
> Task decomposition is the process of breaking down a complex task into smaller and simpler steps. It can be done through techniques like Chain of Thought (CoT) or Tree of Thoughts, which involve dividing the problem into multiple thought steps and generating multiple thoughts per step. Task decomposition helps in enhancing model performance and understanding the thinking process of the model. Thanks for asking!
```
Obviously, this ‘context’ doesn’t exactly read well for humans, but it’s perfect for providing *just* enough context to the LLM for it to extract the relevant information and then regurgitate that into a nice human readable answer, based on the underlying source.

It’s also valuable to note that this methodology also allows including the references to the parts of the source dataset that were used in the context, and where those parts reside in the retrieval index.

## Conclusion

LLMs occasionally feel like magic, but the reality is, they're a collection of very expensively trained matrices are pretty great at generating things that look like what they were trained on. (I'll leave it to the philosophers to discuss if that defines us too...)

Training these systems to 'know' specific knowledge by training or fine-tuning isn't "hard", but it _will_ be expensive, noisy, and really hard to update.

In my opinion, RAG is the only practical option for the vast majority of users wanting to mix real data/knowledge/experience with the natural language interface and apparrent 'reasoning' of LLMs but it's also the one that requires actual work.

The challenge with implementing RAG systems for many organisations isn’t anything to do with “AI” or LLMs; but instead to do with data mobility within organisations. RAG is just a search engine for LLMs to synthesise more text to answer a question; if your organisation doesn’t have the structured, accurate and available data for that search engine to ‘crawl’, then before you can even think about making your nice chatbot, you’ll have to build out those datastores first.
