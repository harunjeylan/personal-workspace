---
name: code-review-skill
description: Helps developers conduct comprehensive code reviews with security, performance, and best practices focus
---

# Code Review Skill

This skill provides a structured approach to code reviews, ensuring thorough analysis of security, performance, and code quality.

## When to Use This Skill

Use this skill when:
- Reviewing pull requests or merge requests
- Checking code for security vulnerabilities
- Optimizing performance bottlenecks
- Ensuring adherence to coding standards
- Providing constructive feedback to developers

## How to Use This Skill

### Basic Usage
Simply ask for a code review:
```
Review this code for security issues
```
or
```
Provide a comprehensive review of this function
```

### Specific Focus
You can request specific aspects:
- Security-focused review
- Performance optimization review
- Best practices review
- Full comprehensive review

## Review Process

### Step 1: Understand Context
- What is the purpose of this code?
- What are the requirements and constraints?
- What is the technology stack?

### Step 2: Security Analysis
Check for:
- Input validation and sanitization
- Authentication and authorization
- SQL injection, XSS, CSRF vulnerabilities
- Secret management
- Data protection

### Step 3: Performance Analysis
Look for:
- Algorithm complexity
- Memory usage
- Database query optimization
- Caching opportunities
- Asynchronous operations

### Step 4: Code Quality
Evaluate:
- Function length and complexity
- Naming conventions
- Error handling
- Code duplication
- SOLID principles

### Step 5: Testing
Recommend:
- Unit test coverage
- Integration tests
- Edge cases
- Test strategies

## Response Format

The skill structures responses as:

1. **Summary** - Brief overview of findings
2. **Critical Issues** - Security or major bugs (priority)
3. **Performance Concerns** - Efficiency issues
4. **Code Quality** - Maintainability improvements
5. **Suggestions** - Optional enhancements
6. **Test Recommendations** - Testing improvements

## Example Reviews

### Security-Focused
```
Critical: SQL injection vulnerability detected
- Issue: Direct string concatenation in query
- Fix: Use parameterized queries
- Example: db.query("SELECT * FROM users WHERE id = ?", [userId])
```

### Performance-Focused
```
Performance: Consider caching for expensive operation
- Issue: Repeated database calls in loop
- Fix: Cache results or use batch queries
- Impact: 10x performance improvement possible
```

## Common Patterns

### Input Validation
Always validate and sanitize user input:
```javascript
function sanitizeInput(input) {
  return input.replace(/[<>\"']/g, '');
}
```

### Error Handling
Use proper error handling patterns:
```javascript
try {
  const result = await riskyOperation();
  return result;
} catch (error) {
  logger.error('Operation failed', error);
  throw new AppError('Failed to process request');
}
```

## Tips for Effective Reviews

1. **Be Specific**: Provide concrete examples
2. **Be Constructive**: Focus on improvements, not criticism
3. **Prioritize**: Highlight critical issues first
4. **Provide Solutions**: Don't just point out problems
5. **Consider Context**: Understand the project requirements
6. **Follow Up**: Ask questions to clarify intent

## Integration with Agents

This skill works well with:
- `code-reviewer` agent: For detailed security analysis
- `tdd-guide` agent: For test-first development
- Other agents: As part of a larger workflow
