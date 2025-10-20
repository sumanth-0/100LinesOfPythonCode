"""Smart Git Commit Generator - Auto-generates conventional commit messages"""
import subprocess, sys

def run_git(cmd):
    """Execute git command"""
    try:
        result = subprocess.run(['git'] + cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except: return ""

def analyze_diff():
    """Analyze staged changes"""
    diff = run_git(['diff', '--cached', '--stat'])
    if not diff: return None
    files = [line.split('|')[0].strip() for line in diff.split('\n') if '|' in line]
    return {'files': files, 'count': len(files)}

def determine_type(files):
    """Determine commit type from files"""
    filenames = [f.lower() for f in files]
    if any('test' in f for f in filenames): return 'test'
    if any(f in filenames for f in ['readme.md', 'contributing.md', 'license']): return 'docs'
    if any(f in filenames for f in ['.gitignore', 'requirements.txt', 'package.json']): return 'chore'
    if any('fix' in f for f in filenames): return 'fix'
    if any(f.endswith('.md') for f in filenames): return 'docs'
    if any(f.endswith(ext) for f in filenames for ext in ['.py', '.js', '.java', '.cpp']): return 'feat'
    return 'chore'

def generate_scope(files):
    """Generate scope from files"""
    if len(files) == 1:
        return files[0].split('/')[0] if '/' in files[0] else 'core'
    dirs = {f.split('/')[0] for f in files if '/' in f}
    return list(dirs)[0] if len(dirs) == 1 else 'multiple'

def generate_description(analysis):
    """Generate commit description"""
    count = analysis['count']
    files = analysis['files']
    if count == 1: return f"update {files[0]}"
    if count <= 3: return f"update {', '.join(files[:2])}"
    return f"update {count} files"

def generate_message(style='conventional'):
    """Generate commit message"""
    analysis = analyze_diff()
    if not analysis: return "No staged changes. Use 'git add' first."
    commit_type = determine_type(analysis['files'])
    scope = generate_scope(analysis['files'])
    desc = generate_description(analysis)
    if style == 'conventional': return f"{commit_type}({scope}): {desc}"
    if style == 'simple': return f"{commit_type.capitalize()}: {desc}"
    return desc.capitalize()

def main():
    """Main entry point"""
    print("🤖 Smart Git Commit Generator\n")
    if not run_git(['rev-parse', '--git-dir']):
        print("❌ Not a git repository!")
        sys.exit(1)
    message = generate_message('conventional')
    if "No staged" in message:
        print(f"⚠️  {message}")
        sys.exit(1)
    print(f"📝 Suggested message:\n  {message}\n")
    print("💡 Alternatives:")
    print(f"  Simple: {generate_message('simple')}")
    print(f"  Basic:  {generate_message('basic')}\n")
    if input("Use suggested message? (y/n): ").lower() == 'y':
        try:
            subprocess.run(['git', 'commit', '-m', message], check=True)
            print("✅ Committed successfully!")
        except: print("❌ Commit failed!")

if __name__ == "__main__":
    main()
