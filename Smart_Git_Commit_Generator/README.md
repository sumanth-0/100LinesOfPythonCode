# Smart Git Commit Message Generator 🤖

An intelligent tool that analyzes your staged git changes and generates meaningful commit messages following best practices and conventional commit format.

## Features ✨

- **Automatic Analysis**: Examines staged changes to understand context
- **Conventional Commits**: Follows conventional commit format
- **Smart Type Detection**: Identifies commit type (feat, fix, docs, etc.)
- **Scope Generation**: Determines appropriate scope from files
- **Multiple Formats**: Offers different message styles
- **Interactive**: Prompts for confirmation or custom message
- **Best Practices**: Built-in commit message guidelines

## Usage 🚀

### Basic Usage

```bash
# Stage your changes first
git add .

# Run the generator
python git_commit_generator.py
```

### Example Output

```
🤖 Smart Git Commit Message Generator

📝 Suggested commit message:

  feat(auth): update authentication and user validation

💡 Alternative formats:
  Simple:  Feat: update authentication and user validation
  Basic:   Update authentication and user validation

Use suggested message? (y/n):
```

## Commit Types 📋

The generator automatically detects the appropriate commit type:

| Type | Description | Triggers |
|------|-------------|----------|
| `feat` | New feature | Code files (.py, .js, .java) |
| `fix` | Bug fix | Files with 'fix' in name |
| `docs` | Documentation | README.md, .md files |
| `test` | Tests | Files with 'test' in name |
| `chore` | Maintenance | Config files, dependencies |
| `refactor` | Code refactoring | Code restructuring |
| `style` | Formatting | Style-only changes |

## Message Formats 🎨

### 1. Conventional Commits (Default)
```
<type>(<scope>): <description>

Example: feat(auth): add user login functionality
```

### 2. Simple Format
```
<Type>: <description>

Example: Feat: add user login functionality
```

### 3. Basic Format
```
<description>

Example: Add user login functionality
```

## How It Works 🔧

1. **Check Repository**: Verifies you're in a git repository
2. **Analyze Diff**: Examines staged changes with `git diff --cached`
3. **Detect Type**: Identifies commit type from file patterns
4. **Generate Scope**: Determines scope from file locations
5. **Create Description**: Builds description from changes
6. **Format Message**: Combines into conventional commit format
7. **Interactive**: Offers to commit with message

## Smart Detection Examples 🎯

### Feature Addition
```
Changed files: src/api/users.py, src/models/user.py
Generated: feat(api): update users and user
```

### Documentation Update
```
Changed files: README.md, docs/api.md
Generated: docs(documentation): update README and api
```

### Bug Fix
```
Changed files: src/bugfix_auth.py
Generated: fix(src): update bugfix_auth
```

### Test Addition
```
Changed files: tests/test_user.py, tests/test_auth.py
Generated: test(tests): update test_user and test_auth
```

## Scope Detection 📂

Scopes are automatically determined from file structure:

- **Single File**: Uses file's directory name
- **Common Directory**: Uses shared parent directory
- **Multiple Directories**: Uses 'multiple' as scope
- **Root Files**: Uses 'core' as scope

## Requirements 📦

- Python 3.6+
- Git installed and available in PATH
- Must be run from within a git repository
- Requires staged changes (`git add`)

## Installation 💾

```bash
# Clone repository
git clone <repo-url>

# Navigate to folder
cd Smart_Git_Commit_Generator

# Make executable (optional)
chmod +x git_commit_generator.py

# Run
python git_commit_generator.py
```

## Workflow Integration 🔄

### Quick Commit Workflow
```bash
# 1. Make changes
vim src/feature.py

# 2. Stage changes
git add src/feature.py

# 3. Generate and commit
python git_commit_generator.py

# 4. Push
git push
```

### Alias Setup (Optional)
```bash
# Add to ~/.bashrc or ~/.zshrc
alias gcg='python /path/to/git_commit_generator.py'

# Usage
gcg
```

## Best Practices Built-In 📚

The generator follows these commit message guidelines:

1. **Present Tense**: "add feature" not "added feature"
2. **Lowercase**: descriptions start with lowercase
3. **No Period**: no trailing period in description
4. **Imperative Mood**: "change" not "changes"
5. **Type Prefix**: always includes type
6. **Scope Context**: adds scope for clarity
7. **Concise**: keeps descriptions brief

## Example Scenarios 🎬

### Scenario 1: New Feature
```bash
$ git add src/payments/stripe.py src/payments/webhook.py
$ python git_commit_generator.py

Output: feat(payments): update stripe and webhook
```

### Scenario 2: Documentation
```bash
$ git add README.md CONTRIBUTING.md
$ python git_commit_generator.py

Output: docs(documentation): update README and CONTRIBUTING
```

### Scenario 3: Bug Fix
```bash
$ git add src/fix_memory_leak.py
$ python git_commit_generator.py

Output: fix(src): update fix_memory_leak
```

## Error Handling ⚠️

- **Not a Git Repo**: Detects and warns if not in git repository
- **No Staged Changes**: Reminds to use `git add` first
- **Git Command Failures**: Gracefully handles git errors
- **Empty Diff**: Handles cases with no actual changes

## Customization 💡

Modify the script to customize:

- Add more file type patterns
- Change commit type detection rules
- Adjust scope generation logic
- Modify message format templates
- Add custom commit types

## Tips 🎓

1. **Stage Carefully**: Only stage related changes together
2. **Review Generated**: Always review before accepting
3. **Custom When Needed**: Use custom message for complex changes
4. **Atomic Commits**: Keep commits focused on one change
5. **Meaningful Scopes**: Organize files for better scope detection

## Limitations ⚡

- Under 100 lines (repository requirement)
- Basic pattern matching (not AI-powered)
- English language only
- No breaking change detection
- No commit body generation

## Future Enhancements 🚀

- AI-powered description generation
- Breaking change detection
- Multi-line commit messages
- Commit body templates
- Interactive type selection
- Custom rules configuration

## Contributing 🤝

Part of the 100LinesOfPythonCode project. Contributions welcome!

## License 📜

Open source - free to use and modify.

---

**Author**: Contributed for Hacktoberfest 2025
**Project**: 100LinesOfPythonCode
