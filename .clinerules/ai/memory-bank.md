---
description: Cline's Memory Bank system for maintaining project knowledge across sessions
author: Claude
version: 1.0
category: "Cline Core"
tags: ["memory-bank", "knowledge-base", "context"]
globs: ["memory-bank/**/*.md", "*"]
---

# Memory Bank

I will read all memory bank files at the start of EVERY session to understand the project and continue work effectively.

## Memory Bank Structure

The Memory Bank consists of core files in the `memory-bank/` directory:

### Core Files
1. `projectBrief.md` - Foundation document defining core requirements and goals
2. `productContext.md` - Why this project exists, problems it solves
3. `activeContext.md` - Current work focus, recent changes, next steps
4. `systemPatterns.md` - System architecture, design patterns
5. `techContext.md` - Technologies used, development setup
6. `progress.md` - What works, what's left to build, known issues
7. `changelog.md` - Chronological log of key changes

## Core Workflows

### At Session Start
1. Read all files from `./memory_bank/`
2. Understand current project state
3. Continue from where we left off

### After Significant Changes
1. Update relevant memory bank files
2. Document new patterns or decisions
3. Update progress.md with current status

## Update Triggers
- Discovering new project patterns
- After implementing significant changes
- When user requests "update memory bank"
- When context needs clarification