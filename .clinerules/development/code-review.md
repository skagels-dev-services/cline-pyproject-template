---
description: Guidelines for performing code reviews
author: Claude
version: 1.0
category: "Development"
tags: ["code-review", "security", "performance"]
globs: ["*"]
---

# Code Review

## Review Process

1. **Understand Context First** — Read the code and any related files to understand what it does and why before critiquing.

2. **Prioritize Findings** — Organize feedback by severity:
   - 🔴 **Critical** — Bugs, security vulnerabilities, data loss risks
   - 🟡 **Important** — Performance issues, error handling gaps, logic problems
   - 🟢 **Suggestions** — Readability, naming, style, simplification opportunities

3. **Be Specific and Actionable** — Every piece of feedback should include what, why, and how to fix.

## What to Look For

### Correctness
- Logic errors and off-by-one mistakes
- Unhandled edge cases (null, empty, boundary values)
- Race conditions in concurrent code

### Security
- Unsanitized user input (SQL injection, XSS, command injection)
- Hardcoded secrets or credentials
- Missing authentication or authorization checks

### Performance
- Unnecessary work inside loops (N+1 queries, repeated calculations)
- Missing caching opportunities
- Blocking operations that should be async

### Maintainability
- Functions doing too many things
- Duplicated logic that should be extracted
- Unclear naming or missing context

### Error Handling
- Swallowed exceptions with no logging
- Missing error handling on I/O operations
- Missing cleanup in failure paths