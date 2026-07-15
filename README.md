<p align="center">
  <img src="public/discord.png" alt="Multiagent Developer Bot" />
</p>

<h1 align="center">Multiagent Developer Bot</h1>

<p align="center">
  An AI-assisted software development team built with Google ADK and Google Cloud.
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#agents">Agents</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#documentation">Documentation</a>
</p>

## Overview

Multiagent Developer Bot coordinates specialized AI agents to assist with software
planning, implementation guidance, security review, and operational debugging.
The system exposes a consistent agent workflow across supported user platforms
while keeping orchestration, persistence, and infrastructure concerns separate.

## Agents

### Orchestrator Agent

The Orchestrator is the primary user-facing agent. It delegates work to Frontend,
Backend, DevOps, Scrum, and Security specialists and combines their results into a
coherent response.

Code produced by a specialist is reviewed by the Security Agent before it can be
reported as compliant. A failed review returns structured findings to the
originating specialist for remediation. Reviews use a bounded retry workflow;
unresolved findings are escalated to the user after the configured attempt limit.
The Security Agent provides recommendations only and does not modify code or
approve deployments.

### Debug Agent

The Debug Agent is an independently deployed operational agent. It has read-only,
least-privilege access to approved logs and produces evidence-based root-cause
analysis with possible remediation steps. It remains isolated from the
Orchestrator because it serves a different workflow and security boundary.

## Roadmap

### v1.0 — Discord Prototype

Status: Completed

- Initial multi-agent developer bot available through Discord
- Flask webhook deployed as a containerized AWS Lambda service
- Infrastructure managed with AWS Cloud Development Kit
- Direct OpenAI API integration for agent responses
- Established the initial Frontend, Backend, DevOps, and Scrum agent roles

### v2.0 — Google Cloud and ADK

Status: Work in progress

- FastAPI service deployed to Google Cloud Run
- Multi-agent orchestration with Google Agent Development Kit and Gemini
- Specialist agents for frontend, backend, DevOps, Scrum, and security review
- Separate Debug Agent for read-only operational analysis
- A2A support for independently deployed agent communication
- Cloud Firestore for project, task, workflow, and review state
- Secret Manager, Artifact Registry, Cloud Build, and Cloud Logging
- Discord support, with website and Slack adapters planned

### v3.0 — Kubernetes and Distributed Agents

Status: Planned

- Add Google Kubernetes Engine as a supported deployment target while preserving
  Cloud Run compatibility
- Run independently scalable agents and services with A2A communication
- Introduce Workload Identity, health probes, resource policies, autoscaling,
  network policies, and distributed observability
- Retain the v2 agent contracts and data model across deployment environments

## Documentation

Architecture, setup, and version-specific implementation notes are maintained in
the [project documentation](https://tommyoh0428.github.io/multiagent-docs/).
