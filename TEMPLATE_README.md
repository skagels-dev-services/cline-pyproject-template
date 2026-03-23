# Python Project Template

This is a template for creating new Python projects with Cline integration.

## Quick Start

To create a new project from this template:

```bash
# 1. Create new directory
mkdir my-new-project
cd my-new-project

# 2. Initialize git
git init

# 3. Copy template files (excluding git-specific)
rsync -av --exclude='.git' /path/to/template/ .

# 4. Update placeholders
find . -type f -name "*.md" -o -name "*.toml" -o -name "*.yml" | xargs sed -i '' 's/{{project-name}}/my-new-project/g'
find . -type f | xargs sed -i '' 's/{{author-name}}/Your Name/g'
find . -type f | xargs sed -i '' 's/{{author-email}}/you@example.com/g'

# 5. Initialize UV project
uv init --name my-new-project

# 6. Install dependencies
uv sync --all-extras

# 7. Set up pre-commit
uv run pre-commit install
```

## What's Included

### .clinerules/ (24 rules organized by category)
```
.clinerules/
├── ai/                      # AI assistance (4 rules)
│   ├── cline-architecture.md
│   ├── memory-bank.md
│   ├── self-improving-cline.md
│   └── sequential-thinking.md
├── development/             # Development methodology (5 rules)
│   ├── baby-steps.md
│   ├── code-review.md
│   ├── general-development-rules.md
│   ├── testing-strategy.md
│   └── web-developer-vanilla-stack.md
├── infrastructure/         # Infrastructure (1 rule)
│   └── helm-chart-developer.md
├── mcp/                    # MCP related (2 rules)
│   ├── mcp-development-protocol.md
│   └── mcp_env_configuration.md
├── meta/                   # Meta/rules about rules (4 rules)
│   ├── cline-for-webdev-ui.md
│   ├── codebase-onboarding.md
│   ├── new-task-automation.md
│   └── writing-effective-clinerules.md
├── project/                # Project management (4 rules)
│   ├── create-documentation.md
│   ├── mermaid-plans.md
│   ├── version-increment.md
│   └── workflow-rules.md
├── python/                 # Python-specific (2 rules)
│   ├── python-style.md
│   └── uv-python-usage-guide.md
├── security/               # Security (1 rule)
│   └── security-audit.md
└── specialized/           # Specialized domains (1 rule)
    └── claude-code-subagents.md
```

### memory_bank/ (7 files)
- `projectBrief.md` - Foundation document defining core requirements and goals
- `productContext.md` - Why this project exists, problems it solves
- `activeContext.md` - Current work focus, recent changes, next steps
- `systemPatterns.md` - System architecture, design patterns
- `techContext.md` - Technologies used, development setup
- `progress.md` - What works, what's left to build, known issues
- `changelog.md` - Chronological log of key changes

### Project Configuration
- `pyproject.toml` - Dependencies and tool configs (Ruff, Black, MyPy, pytest)
- `.gitignore` - Comprehensive Python gitignore
- `.env.example` - Environment variables template
- `.github/workflows/ci.yml` - GitHub Actions CI/CD (Python 3.10-3.12)

## Customization

1. Update `memory_bank/projectBrief.md` with your project details
2. Customize `.clinerules/` rules as needed
3. Update `README.md` with project-specific documentation
4. Configure `.env.example` with relevant environment variables

## Development Workflow

```bash
# Install dev dependencies
uv sync --all-extras

# Run tests
uv run pytest

# Run linters
uv run ruff check .
uv run black --check .

# Run type checker
uv run mypy src/

# Build package
uv build
```

## How Memory Bank Works

At the start of EVERY session, Cline reads all files from `./memory_bank/` to understand project state. Files are updated when significant changes occur. This ensures context persistence across sessions since Cline's memory resets between sessions.