---
aliases:
- /2012/06/litreview-an-overview-on-behaviour-based-methods-for-auv-control/
- /2012/06/litreview-an-overview-on-behaviour-based-methods-for-auv-control.html
categories:
- Uni
comments: true
date: 2012-06-12 09:32:15+00:00
slug: litreview-an-overview-on-behaviour-based-methods-for-auv-control
tags:
- Autonomous Systems
- MATLAB
- Maritime
- Robotics
- Simulation
title: 'LitReview: An Overview on Behaviour based methods for AUV Control'
---
# Biblio

Carreras, Batlle, Ridao, and Roberts;

[An Overview on Behaviour based methods for AUV control, ](http://www.mendeley.com/research/overview-behaviourbased-methods-auv-control/)

Girona, Spain

# What is this work about?

A review and analysis of four AUV behaviour based reactionary control architectures, presenting four control architectures; Scheme, Subsumption, PDL, and Action Selection Dynamics, i.e. cooperative (schema, PDL) and competitive (Sub, ASD)

# What are the main findings of this work?

Competitive models are often easier to design as only one behaviour is resident at a time, however this leads to ’jaunty’ and often sub-optimal results, as in this case where authors say the resultant pats for both competitive models are non-optimal

# What gap in our understanding does this work fill?

I had no idea about any of these modelling schemes, but it was surprising to find that competitive models as described re less optimal. Additionally goes some way to describing major behaviours, i.e. ’GoTo’, ’Obstacle Avoidance’, ’Avoid Trapping’ (don’t run over ones own path), target-following, target-tracking, and bottom-following.

# What research tradition/approach/method is used?

Simulation with MatLab/Simulink with a dynamic model from Fossen 1995 based on the GARBI ROV. Four simulations in a simulated bumpy marine environment with three goal points. Three behaviours are integrated together for each model; Obstacle avoid, Avoid trapping, and Go To (directed at the goal points)

# How is this work connected to the wider research
field?

Quite an old work, late 90’s development of ROV’s did not consider collaborative inter-vector behaviours.

# How is this work relevant to your assignment?

Contextual: Establishment of body of knowledge about the usual behaviours of AUVs. From a control perspective, this is just ’interesting’. Will also be useful in generating simulation framework.

# What are the limitations of this work?

Doesn’t explain why the stated ’non-optimal’ paths (Fig 10, 14) are non-optimal. . . I would have said that the larger sweeping paths across a wider area satisfy the three stated behaviours much better than the twisty coiled behaviours (Fig 9, 12), will approach Wasif about this.

# Useful snippit?

[latex]A = (M_{RB}+M_A)^{-1}(T+G-D(V)V-(C_{RB}(V)+C_A(V))V)[/latex]

Dynamic model from Fossen '95
