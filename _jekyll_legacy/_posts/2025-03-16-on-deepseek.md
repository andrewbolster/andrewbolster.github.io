---
layout: post
title: On Deepseek
categories: [AI, Commentary]
tags:
- DeepSeek
- OpenAI
- LLM
- AI
- Open Source
- Innovation
- market impact
- competition
date: 2025-03-16 13:02 +0000
---
[!["I can't believe ChatGPT lost its job to AI"](/img/2025/deepseek.png)](https://x.com/tekbog/status/1883973153145381064)

> **Note:**
> The continuing adventures of 'a dozen people asked what I thought about [a new AI model](/2024/09/on-openai-o1) in work so I put them together and republished it a few months later when I got a quiet weekend'...

So, Deepseek stripped billions from the market on Monday. Do we care?

My 2c is that this is a fantastic series of innovations on the core design of LLMs, and based on those innovations, I wouldn't be surprised if the training costs quoted as being in the mid-to-high-single-digit-millions-of-dollars are around the right order of magnitude for this (assuming you already had the team expertise of a PhD fueled quant-hedge fund in house and didn't pay them SV salaries).

Yes, it is hilarious that [ChatGPT lost its job to AI](https://x.com/tekbog/status/1883973153145381064)

No, I have no sympathy for OpenAI claiming that Deepseek used their model outputs for training; [Ask the New York Times](https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html) how they feel about OpenAI's 'hunger'

No, it shouldn't be surprising that either Intellectual Property, Salaries, or Import Regimes are 'relaxed' in China; that's been [40 years of globalisation policies coming home to roost](https://www.csis.org/analysis/china-dominates-global-manufacturing).

No, China isn’t taking over the world or hiding illicit H100’s; it’s genuinely a clever architectural twist on the training and inference paradigms (I’m particularly entertained by the [FP8](https://arxiv.org/pdf/2209.05433) linearisation / quantisation coupled with the [paired token inference](https://huggingface.co/blog/samchain/token-merging-fast-inference) and the reduced indexing implications of that, see here for that [story](https://youtubetranscriptoptimizer.com/blog/05_the_short_case_for_nvda)),

No, NVidia isn’t ‘doomed’, but [Sam might be a little warm under the collar](https://bsky.app/profile/edzitron.com/post/3lguc6txf522u),

Yes, [Apple called it](https://www.wsj.com/tech/ai/apple-ai-siri-development-behind-9ea65ee8) with the ‘don’t get in a model arms race’;

Yes, Meta is probably paying 10-50x of the ‘proposed’ training costs just for the salaries of a couple of the leads on their team, but hey, [that’s capitalism](https://ai.meta.com/blog/future-of-ai-built-with-llama/)

On the 'OpenSource' ness of all this, the release of DeepSeek undeniably showcases the immense potential of open-source LLM innovation (somewhat ironically following in the footsteps of "Open"AI releasing both [GPT-2](https://github.com/openai/gpt-2) and BERT in the open in 2019/2020 which arguably kicked off this whole mess). By making such a powerful model available under an MIT license, it not only democratizes access to cutting-edge technology but also fosters innovation and collaboration across the global AI community.

DeepSeek's (rumoured) use of OpenAI "Chain of Thought" (Which I commented on before) originated data for its initial training highlights the importance of transparency and shared resources in advancing AI. In the context of 'Open Source AI,' it’s crucial that the underlying training and evaluation data are open, not just the architecture, evaluations and the resultant model weights. DeepSeek’s achievement in AI efficiency (leveraging a clever Reinforcement Learning-based multi-stage training approach, rather than the current trend of using larger datasets for bigger models), signals a future where AI is accessible beyond the billionaire-classes. Open-source AI, with its transparency and collective development, often outpaces closed source alternatives in terms of adaptability and trust.

> **Note:**
> This is a little 'inside baseball' but retained for posterity.

~~Naturally, several people have been asking me when we're putting DeepSeek on the LLM Gateway, and the short answer is no, we’re not deploying any self-hosted / open models at the moment.~~ (We put it on the internal LLM gateway once it was supported in Azure AI Foundry as a self service model).

As for running it locally with ollama, this is totally fine under our LLM Guidelines; and Deepseek-coder is one of the more performant models on my 32GB 2021 M1 Pro, so go have fun, but no, we’ve no current plans to self-host a model through the LLM Gateway.

As a related side note, to me this all shows that while innovations are still happening in the foundational and reasoning modelling space, the best place that we can invest our time to make the most of these is in domain-specific data collection, representation, and modelling to make the most of these natural language systems, and that’s where the Data Science group are spending the majority of our resources.

## Recommended Coverage

- [The Short Case for NVDA](https://youtubetranscriptoptimizer.com/blog/05_the_short_case_for_nvda): Pairs well with this long read that goes into a deep dive both of the Deep Seek architecture innovations (I’m particularly entertained by the [FP8](https://arxiv.org/pdf/2209.05433) linearisation / quantisation coupled with the [paired token inference](https://huggingface.co/blog/samchain/token-merging-fast-inference) and the reduced inference indexing implications of that) and the impacts to NVIDIA around the [interconnect space](https://groq.com/wp-content/uploads/2020/06/ISCA-TSP.pdf), also covers the ["Giant Chip on One Wafer"](https://cerebras.ai/product-chip/) crew. **If you read nothing else read this**
- [DeepSeek FAQ](https://stratechery.com/2025/deepseek-faq): High level overview of DeepSeek innovations and impacts towards OpenAI/ AGI investments.
- [Grand Unified Model of Reinforcement Learning](https://arxiv.org/abs/2402.03300): One of the most interesting DeepSeek innovations that I haven't fully digested yet is the 'grand unified model of Reinforcement Learning', which is really cool in theory, but I don't fully understand it yet... Help appreciated!
- My team naturally got asked for a comment Monday and got some quotes out.
    - [DeepSeek: What to Know About the Chinese Artificial Intelligence Model](https://www.securitymagazine.com/articles/101337-deepseek-what-to-know-about-the-chinese-artificial-intelligence-model)Security Magazine
    - [DeepSeek open-source AI model stuns the tech world](https://www.processexcellencenetwork.com/ai/news/deepseek-open-source-ai-model-stuns-global-tech-landscape)
    - [Chinese AI App DeepSeek Rattles Tech Markets](https://www.technewsworld.com/story/chinese-ai-app-deepseek-rattles-tech-markets-179551.html){card-appearance="inline"}
    - [What is DeepSeek and What is All the Fuss About](https://www.securityinfowatch.com/cybersecurity/article/55263769/what-is-deepseek-and-what-is-all-the-fuss-about){card-appearance="inline"}
    - [Market Plummets: China DeepSeek AI](https://www.secureworld.io/industry-news/market-plummets-china-deepseek-ai?utm_content=323084806&utm_medium=social&utm_source=linkedin&hss_channel=lcp-106644){card-appearance="inline"}
    - [DeepSeek Rise Leads to $1 Trillion Loss for US Tech Giants](https://www.techerati.com/news-hub/deepseek-rise-leads-to-1-trillion-loss-for-us-tech-giants/){card-appearance="inline"}
    - [Making Good on the Promise of Open Source AI](https://thenewstack.io/making-good-on-the-promise-of-open-source-ai/){card-appearance="inline"}
