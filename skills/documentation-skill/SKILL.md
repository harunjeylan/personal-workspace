---
name: documentation-skill
description: Helps generate and maintain documentation for code and projects
---

# Documentation Skill

This skill helps generate, maintain, and improve documentation for code, projects, and systems.

## When to Use This Skill

Use this skill when:
- Writing README files for projects
- Generating API documentation
- Creating inline code comments
- Writing user guides and tutorials
- Maintaining documentation standards

## Documentation Types

### 1. README Files
- Project overview
- Installation instructions
- Usage examples
- Configuration options
- Contributing guidelines

### 2. API Documentation
- Endpoint descriptions
- Request/response examples
- Parameter documentation
- Error codes and handling
- Authentication requirements

### 3. Code Comments
- Function/method descriptions
- Parameter explanations
- Return value documentation
- Usage examples
- Edge case notes

### 4. User Guides
- Step-by-step tutorials
- Feature explanations
- Best practices
- Troubleshooting sections

## How to Use This Skill

### Basic Usage
Ask for documentation generation:
```
Generate documentation for this function:
[function code]
```

### Specific Types
Request specific documentation types:
```
Write a README for a React component library
```

### Update Existing
Improve or expand existing documentation:
```
Improve the documentation for this API endpoint
```

## Response Format

The skill provides:
1. **Structure**: Organized documentation sections
2. **Clarity**: Clear, concise explanations
3. **Examples**: Practical usage examples
4. **Consistency**: Follows documentation standards
5. **Completeness**: Covers all important aspects

## Examples

### Function Documentation
```javascript
/**
 * Calculates the total price including tax
 *
 * @param {number} price - Base price of the item
 * @param {number} taxRate - Tax rate as decimal (e.g., 0.08 for 8%)
 * @returns {number} Total price including tax
 * @throws {Error} If price or taxRate is negative
 *
 * @example
 * const total = calculateTotal(100, 0.08); // Returns 108
 */
function calculateTotal(price, taxRate) {
  if (price < 0 || taxRate < 0) {
    throw new Error('Price and tax rate must be non-negative');
  }
  return price * (1 + taxRate);
}
```

### README Section
```markdown
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/project.git
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```
```

### API Documentation
```markdown
## POST /api/users

Create a new user account.

### Request Body
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe"
}
```

### Response
```json
{
  "id": "12345",
  "email": "user@example.com",
  "name": "John Doe",
  "createdAt": "2024-01-01T00:00:00Z"
}
```

### Errors
- `400`: Invalid input
- `409`: Email already exists
- `500`: Server error
```

## Documentation Standards

### Markdown Guidelines
- Use proper heading hierarchy
- Include code examples in code blocks
- Use tables for parameter documentation
- Include links to related sections
- Use consistent formatting

### Code Comment Guidelines
- Document public APIs
- Explain complex logic
- Note edge cases and limitations
- Keep comments up to date
- Use standard comment formats (JSDoc, XMLDoc, etc.)

## Tools and Integration

### Markdown Linters
- `markdownlint`: Enforce markdown standards
- `remark-lint`: Check markdown consistency

### Documentation Generators
- `JSDoc`: JavaScript documentation
- `Sphinx`: Python documentation
- `Doxygen`: C/C++ documentation

## Best Practices

1. **Write for Your Audience**: Consider who will read the documentation
2. **Keep It Updated**: Documentation should reflect current code
3. **Use Examples**: Show, don't just tell
4. **Be Concise**: Avoid unnecessary words
5. **Use Active Voice**: "Run the command" not "The command should be run"
6. **Organize Logically**: Group related information together
7. **Include Searchable Keywords**: Help users find information quickly

## Common Documentation Patterns

### Installation Guides
1. Prerequisites
2. Installation steps
3. Configuration
4. Verification
5. Troubleshooting

### API Documentation
1. Endpoint description
2. HTTP method and URL
3. Request parameters
4. Response format
5. Error codes
6. Example requests/responses

### Code Examples
1. Simple usage
2. Advanced usage
3. Error handling
4. Best practices
5. Common pitfalls

## Tips for Effective Documentation

1. **Start Early**: Write documentation as you code
2. **Review Regularly**: Keep documentation current
3. **Get Feedback**: Have others review your documentation
4. **Use Tools**: Automate where possible
5. **Version Control**: Track documentation changes
6. **Make It Searchable**: Use clear headings and keywords
7. **Include Visuals**: Use diagrams when helpful
