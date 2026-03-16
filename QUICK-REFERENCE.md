# Quick Reference: Custom Agents

## Available Agents

### Code Reviewer
**Location:** `agents/custom-agent/code-reviewer.md`  
**Purpose:** Security, performance, and best practices review  
**Tools:** read, edit, write, glob, grep, webfetch  
**Mode:** All-purpose

**Usage:**
```bash
# CLI
opencode run --agent code-reviewer "Review this code"

# Interactive
opencode
> /agent code-reviewer
> Paste code and ask for review
```

### TDD Guide
**Location:** `agents/custom-agent/tdd-guide.md`  
**Purpose:** Test-driven development guidance  
**Tools:** read, edit, write, glob, grep  
**Mode:** Subagent

**Usage:**
```bash
# CLI
opencode run --agent tdd-guide "Help me write tests for X"

# Interactive
opencode
> /agent tdd-guide
> Describe the feature
```

## Custom Commands

### `/review`
Runs comprehensive code review using the code-reviewer agent.

**Usage:**
```bash
opencode
> /review
> Paste your code
```

### `/tdd`
Starts test-driven development with the tdd-guide agent.

**Usage:**
```bash
opencode
> /tdd
> Describe your feature
```

## Workflow Examples

### 1. Security Review
```bash
opencode run --agent code-reviewer "Check authentication function for vulnerabilities"
```

### 2. TDD Session
```bash
opencode run --agent tdd-guide "Implement user registration with validation"
```

### 3. Combined Approach
1. Start with TDD guide to plan tests
2. Implement code
3. Use code reviewer to verify security and performance

## Configuration

The agents are configured in `config/opencode.json`. To use them globally:

1. Copy `config/opencode.json` to `~/.config/opencode/config.json`
2. Or use per-project configuration in `.opencode/config.json`

## Files Structure

```
.
├── agents/
│   ├── custom-agent/
│   │   ├── code-reviewer.md
│   │   └── tdd-guide.md
│   └── README.md
├── skills/
│   └── code-review-skill/
│       └── SKILL.md
├── workflows/
│   └── code-review-workflow.md
└── config/
    └── opencode.json
```

## Tips

1. **Be Specific**: Provide clear context for better results
2. **Iterate**: Run multiple reviews for complex changes
3. **Combine Agents**: Use TDD guide first, then code reviewer
4. **Customize**: Modify agents for your specific needs
5. **Document**: Keep notes on common patterns
