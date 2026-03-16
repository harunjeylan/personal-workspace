# Code Review Workflow

This workflow demonstrates how to use the custom agents for code reviews.

## Setup

1. Ensure opencode CLI is installed
2. Add the custom agents to your opencode configuration
3. Use the agents via CLI commands or interactive sessions

## Usage Examples

### Using Code Reviewer Agent

#### Via CLI Command
```bash
opencode run --agent code-reviewer "Review this code for security issues: [code snippet]"
```

#### Via Interactive Session
1. Start opencode: `opencode`
2. Type `/agent` and select "code-reviewer"
3. Paste your code and ask for a review

### Using TDD Guide Agent

#### Via CLI Command
```bash
opencode run --agent tdd-guide "Help me write tests for this feature: [description]"
```

#### Via Interactive Session
1. Start opencode: `opencode`
2. Type `/agent` and select "tdd-guide"
3. Describe the feature you want to implement

## Example Workflows

### 1. Security Review Workflow
```bash
# Step 1: Ask for security review
opencode run --agent code-reviewer "Check this authentication function for security issues"

# Step 2: Review the suggestions
# Step 3: Implement fixes
# Step 4: Re-run review to verify
```

### 2. TDD Workflow
```bash
# Step 1: Describe the feature
opencode run --agent tdd-guide "I need a function to calculate user score based on activity"

# Step 2: Write tests first
# Step 3: Implement code to pass tests
# Step 4: Refactor and verify
```

### 3. Combined Workflow
```bash
# Step 1: Plan with TDD guide
opencode run --agent tdd-guide "Plan the implementation for user authentication"

# Step 2: Implement tests
# Step 3: Write code
# Step 4: Review with code-reviewer
opencode run --agent code-reviewer "Review the authentication implementation"
```

## Integration with Git Hooks

You can integrate these agents with git hooks for automated code review:

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run code review on staged files
opencode run --agent code-reviewer "Review the staged changes for security issues"
```

### Pull Request Template
Add to your `.github/pull_request_template.md`:
```markdown
## Code Review
- [ ] Security review completed
- [ ] Performance review completed
- [ ] Best practices verified
```

## Configuration

Add to your `.opencode/config.json`:
```json
{
  "agents": {
    "code-reviewer": {
      "path": "./agents/custom-agent/code-reviewer.md",
      "description": "Senior code reviewer for security and performance"
    },
    "tdd-guide": {
      "path": "./agents/custom-agent/tdd-guide.md",
      "description": "TDD expert for test-first development"
    }
  }
}
```

## Tips for Effective Usage

1. **Be Specific**: Provide clear context and requirements
2. **Iterate**: Run multiple reviews for complex changes
3. **Combine Agents**: Use TDD guide first, then code reviewer
4. **Customize**: Adapt the agents for your specific needs
5. **Document**: Keep track of common patterns and solutions
