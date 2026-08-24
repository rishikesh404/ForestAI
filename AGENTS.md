# ForestAI Agent Instructions

## 1. Project Overview

ForestAI is an AI/ML project focused on applying machine learning and data-driven techniques to forest monitoring, analysis, and eventual environmental decision support.

The project is being developed incrementally, with the initial goal of building a functional and understandable MVP before expanding toward more advanced capabilities.

The project is also a learning project. Code should therefore remain understandable, explainable, reproducible, and aligned with the project's learning objectives.

The long-term project roadmap is:

V1: Data Foundation MVP
    ↓
V2: Machine Learning
    ↓
V3: Improved ML + Spatial Intelligence
    ↓
V4: Automated Forest Monitoring
    ↓
V5: Forest Intelligence Platform

The current version is V1, which is the MVP.


## 2. Current Development Phase

Current phase: V1 MVP

V1 is focused exclusively on building the data foundation required for future machine learning.

The current V1 pipeline is:

Raw Data
    ↓
Data Understanding
    ↓
Data Validation
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis
    ↓
Feature Preparation
    ↓
Processed Dataset

The goal of V1 is to produce a clean, validated, well-understood, and reproducible dataset that can be used by the machine learning system in V2.


## 3. V1 Scope Boundary

V1 is the current MVP.

Do not implement functionality belonging to V2 or later unless the developer explicitly instructs you to do so.

V1 does NOT include:

- Machine learning model training
- Model inference
- Model evaluation
- ML model selection
- ML training pipelines
- Model serving
- Automated prediction
- Computer vision
- Satellite-image processing
- Automated forest monitoring
- APIs for model inference
- Production deployment
- Advanced ML experimentation

The existence of future architecture documentation does not mean future functionality should be implemented now.

The current V1 development areas are:

- `src/data/`
- `src/features/`
- `data/processed/`
- `tests/`

The following areas are reserved for future versions:

- `src/models/` → V2 and later
- `src/evaluation/` → V2 and later

Do not modify, populate, or implement functionality in `src/models/` or `src/evaluation/` during V1 unless explicitly instructed by the developer.

If a requested task appears to cross the V1 boundary:

1. Identify what crosses the boundary.
2. Explain why it belongs to a future version.
3. Suggest the minimum V1-compatible approach.
4. Ask for confirmation before making a major scope change.


## 4. Current V1 Learning Priorities

The developer is currently strengthening the foundations required for ForestAI.

Current priorities include:

- Python
- NumPy
- Pandas
- Data manipulation
- Data validation
- Data cleaning
- Exploratory data analysis
- Feature preparation
- Reproducible data processing
- Understanding ML-ready datasets

Machine learning implementation is a future V2 objective.

When implementing V1 functionality, prefer approaches that help the developer understand the underlying concepts rather than hiding everything behind high-level abstractions.

The project is a learning project, so implementations should remain understandable and should expose important concepts rather than unnecessarily hiding them.


## 5. Technology Stack

Use the following technologies when appropriate for the current version:

### V1

- Python
- NumPy
- Pandas

### V2

- Scikit-learn

### Future Versions

- PyTorch
- Geospatial libraries
- Computer vision libraries
- API frameworks
- Databases
- Cloud infrastructure
- Other technologies only when justified by project requirements

Additional dependencies should not be introduced without a clear reason.

Before adding a significant dependency:

1. Check whether the existing stack can solve the problem.
2. Explain why the dependency is useful.
3. Prefer lightweight and well-established solutions.
4. Confirm that the dependency belongs to the current version.

Do not introduce frameworks or technologies simply because they are popular.

Do not introduce future-version technologies prematurely.


## 6. Development Principles

Follow these principles when modifying the project:

- Prefer simple solutions over unnecessarily complex ones.
- Write readable and maintainable Python.
- Use meaningful names for variables, functions, classes, and files.
- Keep functions and modules focused on clear responsibilities.
- Avoid unnecessary abstraction.
- Avoid premature optimization.
- Do not rewrite working code without a reason.
- Do not modify unrelated files.
- Preserve existing functionality unless the requested change requires otherwise.
- Keep different system responsibilities separated.
- Prefer reproducible processing and experiments.
- Make important assumptions explicit.
- Keep implementation appropriate to the current version.
- Do not introduce future-version complexity into the current MVP.

The code should be understandable to a developer who is actively learning the underlying concepts.


## 7. Agent Workflow

For small, straightforward tasks:

1. Inspect the relevant files.
2. Understand the existing implementation and project structure.
3. Confirm that the task belongs to the current version.
4. Implement the requested change.
5. Run appropriate checks or tests.
6. Report what was changed.

For significant or multi-file tasks:

1. Inspect the existing project structure and relevant files.
2. Understand the existing implementation.
3. Identify dependencies and possible side effects.
4. Check whether the task belongs to the current V1 scope.
5. Identify architectural implications.
6. Propose an implementation approach.
7. Wait for approval if the change involves a major architectural decision or crosses the current version boundary.
8. Implement the smallest reasonable solution.
9. Run relevant tests or validation.
10. Review the resulting changes.
11. Report:
    - What changed
    - Which files changed
    - Tests/checks performed
    - Design decisions
    - Remaining issues
    - Important assumptions

Do not make unrelated improvements while implementing a requested feature.


## 8. Git Rules

The developer controls Git operations.

The agent must:

- Never commit automatically.
- Never push automatically.
- Never create or modify Git history without explicit instruction.
- Never force-push.
- Never delete branches without explicit instruction.
- Never modify Git configuration without explicit instruction.
- Never create pull requests without explicit instruction.

The agent may inspect:

- Git status
- Git history
- Git diffs
- Branch information

when useful.

Before a commit, the developer should be able to review the changes.

Never assume that completing a task means the changes should be committed.


## 9. Data Rules

Raw data must be treated as immutable.

The agent must not modify, overwrite, delete, rename, or transform files inside:

`data/raw/`

unless explicitly instructed.

Processed or generated data should be stored separately:

`data/processed/`

The current V1 dataset is the UCI Covertype dataset.

The current raw-data structure is:

data/
└── raw/
    ├── covertype/
    │   ├── covtype.data.gz
    │   ├── covtype.info
    │   └── old_covtype.info
    └── covertype.zip

Do not modify these source files.

The raw dataset should remain available so that processed outputs can be reproduced.

Do not commit large datasets to Git unless explicitly instructed.

Do not commit:

- Secrets
- Credentials
- API keys
- Tokens
- Passwords
- Private keys
- Other sensitive information


## 10. V1 Data Pipeline Responsibilities

V1 may include the following responsibilities.

### Data Ingestion

- Loading the raw dataset.
- Reading supported file formats.
- Verifying expected structure.
- Preserving source information.
- Recording relevant dataset provenance.
- Creating reproducible data-loading functionality.

### Data Validation

Check for:

- Missing values
- Invalid values
- Unexpected data types
- Duplicate records
- Unexpected ranges
- Incorrect column counts
- Inconsistent representations
- Target inconsistencies
- Potential leakage
- Dataset integrity issues

The validation process should report problems rather than silently hiding them.

Validation should distinguish between:

- Actual data errors
- Expected characteristics of the dataset
- Suspicious values requiring investigation

Do not automatically remove unusual data without understanding why it exists.

### Data Cleaning

Potential operations include:

- Type conversion
- Missing-value handling
- Duplicate handling
- Invalid-value handling
- Consistent representations
- Necessary transformations

Never silently discard problematic data.

Document meaningful cleaning decisions.

Never modify the raw dataset as part of cleaning.

### Exploratory Data Analysis

EDA may include:

- Statistical summaries
- Feature distributions
- Target distributions
- Missing-value analysis
- Outlier analysis
- Correlations
- Feature relationships
- Class distributions
- Data-quality analysis
- Identification of potentially important patterns

EDA should be used to understand the dataset rather than to prematurely optimize a future model.

### Feature Preparation

V1 may prepare:

- Feature columns
- Target column
- Encoded representations where justified
- Scaled representations where justified
- Consistent feature structures
- Model-ready data representations

However, V1 must stop before model training.

The purpose is to create a reliable dataset that V2 can use.


## 11. Data Integrity

Never hide data problems.

When an unexpected condition is discovered:

1. Investigate it.
2. Determine whether it is expected.
3. Report it clearly.
4. Fix the underlying problem when appropriate.
5. Document important decisions.

Do not use broad exception handling to hide errors.

Bad:

```python
try:
    ...
except Exception:
    pass