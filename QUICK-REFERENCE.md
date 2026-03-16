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
**Location:** `agents/custom-agent/tdd-guide.md` (also in `.opencode/agents/`)  
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

### Ubuntu Manager
**Location:** `.opencode/agents/ubuntu-manager.md`  
**Purpose:** Ubuntu system management (packages, config, files)  
**Tools:** read, edit, write, glob, grep, bash, webfetch  
**Mode:** All-purpose

**Usage:**
```bash
# CLI
opencode run --agent ubuntu-manager "How do I install Node.js on Ubuntu?"

# Interactive
opencode
> /agent ubuntu-manager
> How do I update my system?
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

### `/install`
Install packages on Ubuntu using the ubuntu-manager agent.

**Usage:**
```bash
opencode
> /install
> nodejs
```

### `/update-system`
Update the Ubuntu system using the ubuntu-manager agent.

**Usage:**
```bash
opencode
> /update-system
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

## Available Skills

### Code Review Skill
**Location:** `skills/code-review-skill/SKILL.md`  
**Purpose:** Comprehensive code reviews with security, performance, and best practices focus.

**Usage:**
```bash
opencode run "Review this code for security issues using code-review-skill"
```

### Commit Message Skill
**Location:** `skills/commit-message-skill/SKILL.md`  
**Purpose:** Generate conventional commit messages based on code changes.

**Usage:**
```bash
opencode run "Generate a commit message for these changes using commit-message-skill"
```

### Documentation Skill
**Location:** `skills/documentation-skill/SKILL.md`  
**Purpose:** Generate and maintain documentation for code and projects.

**Usage:**
```bash
opencode run "Write documentation for this function using documentation-skill"
```

## Files Structure

```
.
├── .opencode/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── tdd-guide.md
│   │   └── ubuntu-manager.md
│   └── config.json
├── agents/
│   ├── custom-agent/
│   │   ├── code-reviewer.md
│   │   └── tdd-guide.md
│   └── README.md
├── skills/
│   ├── code-review-skill/
│   │   └── SKILL.md
│   ├── commit-message-skill/
│   │   └── SKILL.md
│   └── documentation-skill/
│       └── SKILL.md
├── tools/
│   └── machine-manager.sh
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
