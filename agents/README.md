# Custom Agents

This directory contains custom specialized AI agents for the opencode CLI.

## Available Agents

### 1. Code Reviewer (`code-reviewer.md`)
A senior code reviewer with expertise in security, performance, and software architecture.

**Use when:**
- Reviewing pull requests
- Checking for security vulnerabilities
- Optimizing performance
- Ensuring code quality and best practices

**Tools available:** read, edit, write, glob, grep, webfetch

**Mode:** All-purpose (can function as primary or subagent)

### 2. TDD Guide (`tdd-guide.md`)
A test-driven development expert that helps write tests before implementation code.

**Use when:**
- Starting new features
- Refactoring existing code
- Ensuring test coverage
- Following TDD methodology

**Tools available:** read, edit, write, glob, grep

**Mode:** Subagent (invoked by other agents)

## How to Use

### Via CLI Command
```bash
opencode run --agent code-reviewer "Review this code for security issues"
```

### Via Interactive Session
1. Start opencode: `opencode`
2. Type `/agent` and select your custom agent
3. Or use the agent selector in the TUI

### Via Configuration
Add to your `.opencode/config.json`:
```json
{
  "agents": {
    "code-reviewer": {
      "path": "./agents/custom-agent/code-reviewer.md"
    }
  }
}
```

## Creating New Agents

1. Create a new Markdown file in this directory
2. Follow the frontmatter format:
   ```markdown
   ---
   name: agent-name
   description: What this agent does
   mode: all | primary | subagent
   tools: comma-separated-list
   model: provider/model
   ---
   ```
3. Write the agent's system prompt and guidelines
4. Test the agent in opencode

## Best Practices

- Keep agents focused on a specific domain
- Define clear constraints and response formats
- Specify the tools needed for the agent's tasks
- Use appropriate modes (subagent for specialized tasks)
- Document when to use each agent
