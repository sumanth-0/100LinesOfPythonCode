# Contributing Guidelines

We welcome contributions from developers of all skill levels! Whether you're submitting a Python snippet, fixing bugs, improving documentation, or adding new features, your contributions make a big difference.

If you are a first-time contributor, see [this guide](https://opensource.guide/how-to-contribute/) on how to contribute to open source.

Please follow [Code of Conduct](/CODE_OF_CONDUCT.MD) in all your interactions with the project.

# Code Requirements

Ensure your code snippet follows these requirements:

- It is under 100 lines of code.
- It is well-commented and easy to understand.
- It provides something interesting - this could be a unique algorithm, a cool use case, or a clever trick in Python.
- It follows Python’s [PEP 8 style guide](https://peps.python.org/pep-0008/) to keep the code clean and readable.

# How to Contribute

Please follow the steps below to contribute. Remember to check if your idea is already implemented in our existing snippets.

## 1. Create an Issue

Create a new [issue](https://github.com/sumanth-0/100LinesOfPythonCode/issues). Add a short title that describes your code and a brief description.

## 2. Fork the Repository

At the top of the [main repository page](https://github.com/sumanth-0/100LinesOfPythonCode/tree/main), click the "Fork" button. 

In the following page, click "Create fork". This will create a copy of the repository in your GitHub account.

## 3. Clone Your Fork

Clone your forked repository to your local machine with the following bash command:

```bash
git clone https://github.com/<your-github-name>/100LinesOfPythonCode.git
```

Navigate into the cloned directory:

```bash
cd 100LinesOfPythonCode
```

## 4. Create a New Branch

Create a new branch for your contribution:

```bash
git checkout -b <your-branch-name>
```

Replace `<your-branch-name>` with something descriptive, like `add-python-snippet` or `fix-typo-in-docs`.

## 5. Add Your Python Code and README.md

Create a new folder and give it a short name that describes your script. Name your file using a descriptive title of what the code does. For example:

`snippets/fibonacci_sequence.py`

**Note**: Do not use spaces in folder or file names; instead, use underscores (`_`) to separate words.

Add your Python code file into your folder.

Add a README.md into that folder which explains your script and any prerequisites it may have.

## 7. Test Your Code

Ensure your code works by running it locally. If you can, write test cases to validate its functionality.

## 8. Commit and Push Your Changes

After you've made your changes and tested your code, commit your work:

```bash
git add .
git commit -m "Add <description-of-your-code>"
git push origin <your-branch-name>
```

## 9. Open a Pull Request

Go to your forked repository on GitHub and click the "Compare & pull request" button. In the pull request:

- Describe the changes you've made.
- Tag the issue you created.
- Reference discussions if necessary.

We will review your pull request, and once approved, it will be merged into the main repository.

# Issues

If you find a bug, have a question, or would like to suggest a new feature, feel free to open an issue. Please include a detailed description so we can understand the problem or feature request.

Thank you for contributing!

# Our Contributors

<a href="https://github.com/sumanth-0/100LinesOfPythonCode/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sumanth-0/100LinesOfPythonCode&max=1000" />
</a>
