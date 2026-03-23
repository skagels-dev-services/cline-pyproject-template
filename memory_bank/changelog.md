# Changelog

## [Unreleased] - 2025-03-23

### Added
- Created Python project template with Cline integration
- Added 24 .clinerules organized into 8 subdirectories
- Added memory_bank/ directory with 7 files for context persistence
- Added .gitignore with comprehensive Python ignores
- Added pyproject.toml with dev dependencies and tool configs (Ruff, Black, MyPy, pytest)
- Added .env.example template
- Added .github/workflows/ci.yml for GitHub Actions CI/CD (Python 3.10-3.12)
- Added README.md and TEMPLATE_README.md
- Added python-style.md clinerule for Python conventions

### Reorganized
- .clinerules/ reorganized into subdirectories: ai/, development/, infrastructure/, mcp/, meta/, project/, python/, security/, specialized/
- web-developer-vanilla-stack.md moved from infrastructure/ to development/

### Rules Included (24 total)
- ai/: cline-architecture.md, memory-bank.md, self-improving-cline.md, sequential-thinking.md
- development/: baby-steps.md, code-review.md, general-development-rules.md, testing-strategy.md, web-developer-vanilla-stack.md
- infrastructure/: helm-chart-developer.md
- mcp/: mcp-development-protocol.md, mcp_env_configuration.md
- meta/: cline-for-webdev-ui.md, codebase-onboarding.md, new-task-automation.md, writing-effective-clinerules.md
- project/: create-documentation.md, mermaid-plans.md, version-increment.md, workflow-rules.md
- python/: python-style.md, uv-python-usage-guide.md
- security/: security-audit.md
- specialized/: claude-code-subagents.md
