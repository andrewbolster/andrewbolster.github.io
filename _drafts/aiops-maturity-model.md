---
layout: post
title: AIOps Maturity Model
tags: [AIOps, MLOps, Maturity Model, Machine Learning, Data Science, DevOps]
category: AI
---


# AIOps Maturity Model

## Introduction

This document outlines an AIOps Maturity Model to help organizations assess and improve their Machine Learning Operations capabilities. It came from my own frustration that there weren't any models that fit the real experience of end-to-end data science and operations relationships that covered _both_ 'conventional' ML, _and_ practically discussing LLM based systems and how completly differently you have to think about them.

This was originally published internally around May '24 and then presented at [NIDC](https://x.com/Bolster/status/1860336184221642896) as an 'Eye Test Model', and I promised that I'd eventualy publish it; this is it, dusted off and tidied up for public consumption.

The model is structured across six key capability areas and five maturity levels, providing a roadmap for organizations to evolve their AIOps practices. This model is based on the reference materials listed below, and is far from original in any way, and probably alread out of date.

## References

- [Microsoft Azure MLOps Maturity Model](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model)
- [Microsoft Azure LLMOps Maturity Model](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-llmops-maturity?view=azureml-api-2)
- [TDR Maturity Model](https://docs.google.com/spreadsheets/d/13sqhjhRZbMMdECLkAK_KqFZ9wGWbXCZTty-a0hJ9V50/edit#gid=235231053)

## Capability Areas

- **People**: Collaboration and communication among data scientists, data engineers, operations teams and software engineers.
- **Data Management and Exploration**: Handling of data sources, data classification, mobility and discovery processes.
- **Generic Model Creation**: Data gathering, compute management, and experiment & feedback tracking.
- **Generic Model Deployment and Release**: Processes for deploying and releasing models.
- **Large Language Model Ops**: Management and deployment of large language models, natural language evaluation, and prompt engineering.
- **Application Integration and Maintenance**: Integration of models into applications and maintenance practices.

## Maturity Model

### People

| Level      | Data Scientists | Data Engineers | Software Engineers |
|------------|-----------------|----------------|--------------------|
| **Initial** | Siloed, not in regular communications with the larger team | Non-Existent | Siloed, receive models remotely from the other team members |
| **Minimal** | Siloed, occationally participate in one-way 'demonstrations' to larger team | Siloed, not in regular communication with the larger team | Siloed, receive model remotely from the other team members |
| **Procedural** | Working directly with data engineers to convert experimentation code into repeatable scripts/jobs | Working with data scientists | Siloed, receive model remotely from the other team members, have visibility to model pipelines etc |
| **Innovative** | Working directly with data engineers to convert experimentation code into managable services/pipelines | Working with data scientists and software engineers to manage inputs/outputs | Working with data engineers to automate model integration into application code |
| **Leading** | Working directly with data engineers to convert experimentation code into managable services/pipelines. Working with software engineers to identify markers for data engineers | Working with data scientists and software engineers to manage inputs/outputs | Working with data engineers to automate model integration into application code. Implementing post-deployment metrics gathering |

### Data Management and Exploration

| Level      | Data Sources | Data Store | Data Sensitivity | Data Access | ETL Tasks |
|------------|--------------|------------|------------------|-------------|-----------|
| **Initial** | Disparate data sources with unaligned identifiers/taxonomies | No shared non-production data stores | Un/underspecified or presumptuious| Individual/Local based case-by-case and dataset-by-dataset | Largely script-driven |
| **Minimal** | Disparate data sources with unaligned identifiers/taxonomies | Shared experimental / dev unstructured data store (with minimal ACL) | Specified by convention but unenforced | Individual/Local based case-by-case and dataset-by-dataset or 'need to know' | Driven by version controlled transformations |
| **Procedural** | Disparate data sources with common external identifiers mappings / shared but unenforced taxonomies | Common downstream unstructured data store with basic dataset/user level ACL | Enforced at the dataset level, specified but unenforced at the attribute level, with informal rules around aggregate sensitivity | Group / RBAC via dataset-specific interfaces| Driven by version controlled & release managed transformations, with replica staging deployments for testing |
| **Innovative** | Aligned / Shared data sources with common entity identifiers and unified taxonomies | Common downstream unstructured and analytical datastores with transparent row/entity-level ACL | Enforced at the row/entity level, specified but unenforced at the attribute level, formal rules around aggregate sensitivity | Data Catalog driven discoverability, RBAC for access, 'need to know' pathway established and auditable | Driven by version controlled & release managed transformations, with replica staging deployments for testing |
| **Leading** | Aligned / Shared data sources with common entity identifiers and unified taxonomies | Common downstream unstructured and analytical datastores with transparent attribute-level ACL | Enforced at the attribute level, specified but unenforced at the attribute level | Universal Schema Discovery with base RBAC access; automated and audited 'need to know' requests; synthetic data for sensitive/confidential streams| Driven by CI/CD transformations, with replica staging deployments for testing |

### Generic Model Creation

| Level      | Data Gathering | Compute Management | Experiment Tracking | End Result |
|------------|----------------|--------------------|---------------------|------------|
| **Initial** | Manually | Likely not managed | Not predictably tracked | Single model file manually handed off with inputs/outputs |
| **Minimal** | Automatically by per-experiment data pipelines | Managed by team | Not predictably tracked | Training Code Version controlled; Single binary model file manually handed off with inputs/outputs |
| **Procedural** | Automatically by shared data pipelines/feature store | Managed as a shared ops capability | Tracked within teams | Both training code and resulting models are version controlled, possibly release managed |
| **Innovative** | Automatically by shared data catalog/feature store | Managed as a budgeted and tracked capability | Tracked within teams with shared experimental repositories | Both training code and resulting models are version controlled & release managed and security tested with A/B or Blue/Green deployments, evaluation feedback available to originating team at staging |
| **Leading** | Automatically by distributed data mesh | Managed as a cost centre with Data teams as 'customers' | Tracked and published internally as derived data products | Retraining triggered automatically based on production metrics. Both training code and resulting models are version controlled. Multiple model versions deployed at once with continuous evaluation feedback available to team in production|

### Generic Model Deployment and Release

| Level      | Process | Scoring Script | Release Management |
|------------|---------|----------------|--------------------|
| **Initial** | Manual | Might be manually created well after experiments, not version controlled | Handled by data scientist or data engineer alone |
| **Minimal** | Manual | Might be manually created well after experiments, likely version controlled | Handed off to software engineers |
| **Procedural** | Automatic | Version controlled with tests | Managed by Software engineering team |
| **Innovative** | Speculative | Triggered by anomaly & corrolation detection, Version controlled with tests | Managed by continuous delivery (CI/CD) pipeline |
| **Leading** | Generative | Triggered by non-statistical events, Version controlled with tests | Managed by continuous integration and CI/CD pipeline |

### Large Language Model Ops

| Level      | Discovery and Testing | Model/Inference Resources | Prompt Management | Deployment | Monitoring |
|------------|-----------------------|---------------------------|-------------------|------------|------------|
| **Initial** | Organic discovery of models and testing prompts | | | | Basic Lab-driven Feedback Evaluation and Monitoring |
| **Minimal** | | Shared model / inference resources | Iterative model augmentation with prompt engineering | Structured Deployment | Prompt-based feedback evaluations |
| **Procedural** | | Centralized model/inference resources | Versioned prompt management with RAG / Tool Calling | Release-driven deployment | Structured deployment and inference based feedback driven evaluations |
| **Innovative** | Consistantly evaluating new models | Model serving/inference 'as a service' with resources under IaC | Comprehensive prompt management | Real-time deployment | Advanced monitoring and automated alerts |
| **Leading** | | Seamless, collaborative environment for CI/CD | Fully automated monitoring and model/prompt refinement | | |

### Application Integration and Maintenance

| Level      | Expertise Reliance | Integration Tests | Release Process | Application Code Tests |
|------------|--------------------|-------------------|-----------------|------------------------|
| **Initial** | Heavily reliant on data scientist expertise to implement | | One-Off releases| |
| **Minimal** | Heavily reliant on data scientist expertise to implement model | Basic integration tests exist for the model | Repeated Manual Releases | Unit tests |
| **Procedural** | Data scientist expertise required, but co-development with SMEs | Basic integration tests exist for the model | Automated | Unit tests |
| **Innovative** | Less reliant on data scientist expertise to implement model; SME's empowered with 'hands off' model proposals | Unit and integration tests for each model release | Automated, in regular release/build pipelines | Unit/integration tests |
| **Leading** | SMEs proposing models that can go to production if passing 'gates' established by data science/ops | Unit and Integration tests for each model release | Continuous | Unit/integration tests |