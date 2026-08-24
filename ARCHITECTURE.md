# ForestAI Architecture

## 1. Purpose

This document describes the technical architecture of ForestAI, including the current MVP architecture and the planned evolution of the system.

ForestAI is being developed incrementally. The architecture therefore separates the current implementation from capabilities planned for future versions.

The immediate objective is to build a reliable and understandable **data foundation in V1**. Machine learning is introduced in V2, followed by spatial intelligence, automated monitoring, and eventually a real-world decision-support platform.

The architecture should remain modular so that individual components can be improved or replaced without requiring the entire system to be rewritten.

---

# 2. Architectural Philosophy

ForestAI follows a modular pipeline architecture.

The core principle is:

```text
Data → Validation → Processing → Analysis → Features
```

V2 extends this foundation with:

```text
Prepared Data → Model → Training → Validation → Evaluation → Inference
```

Future versions extend the system further toward:

```text
Data → AI Analysis → Validation → Insights → Human Decision → Action
```

Each stage should have a clear responsibility.

The system should avoid tightly coupling unrelated components.

For example:

* Data processing should not depend on machine learning models.
* Model training should not depend on the user interface.
* Inference should not contain training logic.
* Visualization should consume results rather than implement ML logic.
* Raw data should remain separate from processed data.
* Future APIs should coordinate system components rather than contain their internal logic.

This separation allows ForestAI to evolve without repeatedly restructuring the entire project.

---

# 3. Version Architecture

ForestAI is divided into progressive development stages.

```text
V1
Data Foundation
    ↓
V2
Machine Learning
    ↓
V3
Improved ML + Spatial Intelligence
    ↓
V4
Automated Monitoring
    ↓
V5
Forest Intelligence Platform
```

Each version builds upon the previous version.

Complexity should only be introduced when the project has a clear reason for requiring it.

---

# 4. V1 Architecture: Data Foundation MVP

The V1 architecture focuses exclusively on understanding and preparing data.

The current conceptual architecture is:

```text
                    ┌─────────────────────┐
                    │    Raw Forest Data │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Data Ingestion      │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Data Validation      │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Data Cleaning        │
                    │ & Preprocessing      │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Exploratory Data     │
                    │ Analysis             │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Feature Preparation  │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Processed Dataset    │
                    └─────────────────────┘
```

### V1 does not contain:

* Model training
* Model inference
* Model evaluation
* Automated prediction
* Model serving

The purpose of V1 is to produce a reliable dataset that V2 can use.

---

# 5. V1 Data Layer

The data layer is responsible for bringing forest-related information into the ForestAI project and preparing it for analysis.

## Responsibilities

The data layer may include:

* Dataset acquisition
* Dataset loading
* Dataset provenance
* Data validation
* Data inspection
* Data cleaning
* Data transformation
* Processed dataset generation

The data layer should not contain machine learning model logic.

---

# 6. Raw Data

Raw data represents the original source material obtained from datasets or external sources.

The intended structure is:

```text
data/
└── raw/
```

Raw data should be treated as immutable.

ForestAI should never modify the original dataset directly.

The intended flow is:

```text
Raw Data
   ↓
Processing
   ↓
Processed Data
```

The original source should remain available so that the entire processing pipeline can be reproduced.

---

# 7. Current V1 Dataset

The current V1 development dataset is the **UCI Covertype dataset**.

The dataset is used as the initial learning dataset for ForestAI because it provides a manageable forest-related tabular dataset suitable for developing the V1 data pipeline.

The current raw data structure is:

```text
data/
└── raw/
    ├── covertype/
    │   ├── covtype.data.gz
    │   ├── covtype.info
    │   └── old_covtype.info
    └── covertype.zip
```

The files in `data/raw/` should remain untouched.

The V1 pipeline should read from these files and produce processed data separately.

---

# 8. Data Validation Layer

Data validation is a first-class component of V1.

Its purpose is to determine whether the input dataset is suitable for analysis and future machine learning.

Validation may include:

* File integrity
* Expected number of columns
* Expected data types
* Missing values
* Duplicate records
* Invalid values
* Unexpected ranges
* Class distribution
* Feature consistency
* Target consistency
* Potential data leakage
* Dataset documentation consistency

The validation layer should report problems rather than silently hiding them.

Invalid or suspicious data should be investigated rather than automatically discarded without explanation.

---

# 9. Data Cleaning and Preprocessing

The preprocessing layer transforms validated raw data into a clean representation.

Potential operations include:

```text
Raw Data
   ↓
Type Conversion
   ↓
Missing Value Handling
   ↓
Duplicate Handling
   ↓
Invalid Value Handling
   ↓
Feature Transformation
   ↓
Clean Dataset
```

The exact operations depend on the characteristics of the dataset.

Preprocessing must not modify the original raw files.

---

# 10. Exploratory Data Analysis

Exploratory Data Analysis is responsible for understanding the cleaned dataset.

EDA may include:

* Statistical summaries
* Feature distributions
* Target distribution
* Missing-value analysis
* Outlier analysis
* Feature relationships
* Correlation analysis
* Class distribution
* Feature ranges
* Identification of unusual patterns

EDA should primarily be an analytical layer.

It should not become tightly coupled with future production inference systems.

---

# 11. Feature Preparation

Feature preparation converts the cleaned dataset into a consistent representation suitable for future machine learning.

Potential operations include:

* Feature selection
* Feature transformation
* Encoding
* Scaling
* Creating consistent feature representations
* Separating features from the target

The output of V1 should be a **model-ready dataset**, but no model should be trained during V1.

---

# 12. V1 Output

The final output of V1 is:

```text
Raw Dataset
    ↓
Validated Dataset
    ↓
Cleaned Dataset
    ↓
Explored Dataset
    ↓
Prepared Dataset
```

The final processed dataset should be reproducible from the original raw data.

V1 is complete when this pipeline is reliable, understandable, and documented.

---

# 13. V2 Architecture: Machine Learning

V2 introduces the first machine learning system.

The V2 architecture extends the V1 pipeline:

```text
                    ┌─────────────────────┐
                    │   V1 Processed Data │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Train / Validation  │
                    │ / Test Preparation   │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Model Training       │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Model Validation     │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Model Evaluation     │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Trained Model        │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Inference            │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Predictions          │
                    └─────────────────────┘
```

The V2 model will initially use the UCI Covertype dataset as a multiclass classification problem.

The objective is to predict forest cover type from the available cartographic and environmental features.

---

# 14. Separation of Training and Inference

Beginning in V2, ForestAI must maintain a clear distinction between training and inference.

## Training

```text
Prepared Data
     ↓
Train / Validation / Test
     ↓
Training
     ↓
Validation
     ↓
Model Selection
     ↓
Final Model
```

## Inference

```text
New Input
     ↓
Same Required Preprocessing
     ↓
Trained Model
     ↓
Prediction
     ↓
Result
```

A model should not be retrained every time a prediction is requested.

The preprocessing used during inference must remain consistent with the preprocessing used during training.

---

# 15. V2 Model Layer

The model layer contains the machine learning models used by ForestAI.

The first model should be a simple classical ML baseline.

Potential approaches include:

* Logistic regression
* Decision trees
* Random forests
* Other suitable classical ML algorithms

The exact model should be selected based on:

* Problem characteristics
* Dataset characteristics
* Interpretability
* Performance
* Learning objectives

The model layer should contain model-specific logic but should not handle data acquisition or user-interface logic.

---

# 16. Model Validation

Model validation becomes part of ForestAI beginning in V2.

The system should determine whether a model generalizes beyond the data used for training.

Validation should consider:

* Train/validation/test methodology
* Overfitting
* Generalization
* Model stability
* Appropriate evaluation metrics
* Class imbalance
* Error patterns

Because Covertype contains geographically related observations, V2 should explicitly document the limitations of simple random splitting and investigate spatially aware validation where appropriate.

---

# 17. Model Evaluation

Model evaluation determines how well a trained system performs.

For the initial Covertype classification problem, appropriate metrics may include:

* Accuracy
* Precision
* Recall
* F1 score
* Confusion matrix

Additional metrics can be introduced when justified by the problem.

Metrics should not be selected solely because they produce attractive numbers.

The evaluation strategy should reflect the actual characteristics of the task.

---

# 18. V3 Architecture: Improved ML and Spatial Intelligence

V3 expands ForestAI beyond the initial tabular ML system.

Potential additions include:

* Better feature engineering
* Multiple model architectures
* Hyperparameter tuning
* Improved validation strategies
* Spatial validation
* Geospatial data
* Satellite imagery
* Remote sensing
* Computer vision
* Deep learning

A possible architecture is:

```text
              ┌───────────────────────┐
              │ Environmental Data    │
              └───────────┬───────────┘
                          ↓
              ┌───────────────────────┐
              │ Tabular Data Pipeline │
              └───────────┬───────────┘
                          ↓
              ┌───────────────────────┐
              │ Classical ML          │
              └───────────┬───────────┘
                          │
                          │
              ┌───────────┴───────────┐
              ↓                       ↓
      ┌───────────────┐       ┌────────────────┐
      │ Spatial Data  │       │ Satellite Data │
      └───────┬───────┘       └───────┬────────┘
              ↓                       ↓
      ┌───────────────┐       ┌────────────────┐
      │ Geospatial    │       │ Computer Vision│
      │ Processing    │       │ / Deep Learning│
      └───────┬───────┘       └───────┬────────┘
              └───────────┬───────────┘
                          ↓
                  Model Evaluation
                          ↓
                       Results
```

This is a future architecture and is not part of V1.

---

# 19. V4 Architecture: Automated Monitoring

V4 moves ForestAI from manually executed analysis toward automated monitoring.

A potential workflow is:

```text
Scheduled Data Collection
          ↓
Data Validation
          ↓
Data Processing
          ↓
Model Inference
          ↓
Change / Anomaly Detection
          ↓
Validation
          ↓
Results
          ↓
Alerts / Reports
```

Potential capabilities include:

* Periodic data ingestion
* Automated preprocessing
* Automated inference
* Forest change detection
* Anomaly detection
* Historical comparisons
* Automated reports
* Monitoring pipelines

Automation should only be introduced when the underlying analysis is sufficiently reliable.

---

# 20. V5 Architecture: Forest Intelligence Platform

V5 represents the long-term direction toward an interactive environmental decision-support system.

A possible architecture is:

```text
                         ┌─────────────────────┐
                         │    Data Sources     │
                         │                     │
                         │ Satellite           │
                         │ Government          │
                         │ Field Data          │
                         │ Environmental Data  │
                         └──────────┬──────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ Data Ingestion       │
                         └──────────┬──────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ Data Processing      │
                         │ & Validation         │
                         └──────────┬──────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ AI / ML Layer        │
                         └──────────┬──────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ Inference / Analysis │
                         └──────────┬──────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ Evidence / Results  │
                         └──────────┬──────────┘
                                    ↓
                    ┌───────────────┴───────────────┐
                    ↓                               ↓
           ┌─────────────────┐             ┌─────────────────┐
           │ Visualization   │             │ Backend API     │
           └────────┬────────┘             └────────┬────────┘
                    └───────────────┬───────────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ Organizations       │
                         │ NGOs / Authorities  │
                         │ Researchers         │
                         └──────────┬──────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ Human / Local       │
                         │ Validation          │
                         └──────────┬──────────┘
                                    ↓
                         ┌─────────────────────┐
                         │ Environmental       │
                         │ Action / Monitoring │
                         └─────────────────────┘
```

This architecture represents the long-term direction rather than the current implementation.

---

# 21. Real-World Validation Architecture

A major long-term objective is connecting AI-generated insights with independent real-world evidence.

The conceptual feedback loop is:

```text
ForestAI Prediction
        ↓
Evidence / Confidence
        ↓
Expert or Local Review
        ↓
Field / External Validation
        ↓
Confirmed / Rejected / Uncertain
        ↓
Feedback
        ↓
Model / System Improvement
```

Potential validation sources include:

* Field observations
* Government records
* Forest departments
* Environmental NGOs
* Research organizations
* Satellite observations
* Domain experts
* Local communities

The feedback process should be carefully controlled.

A human or external observation should not automatically become training data without checking its reliability.

---

# 22. Human-in-the-Loop Decision Support

ForestAI is intended to assist decision-making rather than independently make environmental decisions.

The long-term architecture should therefore follow:

```text
Data
 ↓
AI Analysis
 ↓
Prediction / Insight
 ↓
Evidence & Confidence
 ↓
Human Validation
 ↓
Decision Support
 ↓
Action
```

The final decision remains with the responsible organization, authority, researcher, or domain expert.

---

# 23. Future Data Sources

As ForestAI develops, the system may integrate multiple types of data.

## Structured Data

* Forest inventories
* Environmental measurements
* Weather information
* Geographic information
* Government datasets

## Remote Sensing

* Satellite imagery
* Aerial imagery
* Multispectral data
* Vegetation indices

## Field Data

* Observations
* Surveys
* Environmental measurements
* Local reports

## External Knowledge

* Scientific research
* Environmental reports
* NGO datasets
* Government records

Different data sources should be integrated through well-defined interfaces rather than tightly coupling the entire system to one source.

---

# 24. Reproducibility

ForestAI should prioritize reproducibility throughout development.

The project should aim to record:

* Dataset source
* Dataset version
* Data preprocessing approach
* Feature configuration
* Model configuration
* Hyperparameters
* Random seeds where applicable
* Evaluation metrics
* Experiment results

V1 should establish reproducible data processing.

V2 should extend reproducibility to machine learning experiments.

As the project grows, dedicated experiment tracking may be introduced when justified.

---

# 25. Architecture and Repository Structure

The current repository is intentionally small.

The current structure is:

```text
ForestAI/
├── AGENTS.md
├── ARCHITECTURE.md
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── evaluation/
│
└── tests/
```

The current directories correspond primarily to the V1 and future pipeline boundaries.

Not every directory needs implementation immediately.

For example:

* `src/data/` is relevant to V1.
* `src/features/` is relevant to V1.
* `src/models/` becomes active in V2.
* `src/evaluation/` becomes significantly more important in V2.

Additional directories should only be introduced when the project requires them.

---

# 26. Training and Inference Separation

Once V2 begins, training and inference must remain separate responsibilities.

```text
TRAINING

Processed Dataset
       ↓
Data Split
       ↓
Training
       ↓
Validation
       ↓
Evaluation
       ↓
Model Artifact


INFERENCE

New Data
       ↓
Required Preprocessing
       ↓
Model Artifact
       ↓
Prediction
       ↓
Result
```

This separation becomes increasingly important when ForestAI moves toward automated monitoring and deployment.

---

# 27. Scalability

The MVP should prioritize simplicity rather than scalability.

V1 should be able to run locally using a manageable dataset.

As ForestAI grows, scalability may become important for:

* Larger datasets
* Multiple data sources
* Satellite imagery
* Automated monitoring
* Multiple models
* Multiple geographic regions
* Concurrent users
* Large-scale inference

Scalability should be introduced when required rather than prematurely.

---

# 28. Security and Data Integrity

As ForestAI evolves toward real-world deployment, security and data integrity will become increasingly important.

Future considerations may include:

* Authentication
* Authorization
* Secure APIs
* Input validation
* Data validation
* Model integrity
* Audit logs
* Secure storage
* Protection of sensitive environmental information

These concerns are not primary V1 requirements but should be considered before production deployment.

---

# 29. Architecture Evolution Principles

Future architectural changes should follow these principles:

1. Preserve clear separation of responsibilities.
2. Avoid unnecessary coupling.
3. Prefer modular components.
4. Introduce complexity only when justified.
5. Maintain reproducibility.
6. Preserve raw data.
7. Keep training and inference separate once ML is introduced.
8. Validate important outputs.
9. Keep humans involved in high-impact environmental decisions.
10. Prefer extensible designs without over-engineering the MVP.
11. Keep the current version focused on its defined objectives.
12. Do not introduce future-version technologies prematurely.

---

# 30. Current Architectural Goal

The immediate architectural goal is to build a **small, understandable, modular data pipeline**.

V1 should establish:

```text
Data
 ↓
Validation
 ↓
Processing
 ↓
EDA
 ↓
Feature Preparation
 ↓
Processed Dataset
```

V2 will extend this foundation:

```text
Processed Dataset
 ↓
ML Model
 ↓
Training
 ↓
Validation
 ↓
Evaluation
 ↓
Inference
```

Later versions will extend the system toward:

```text
Environmental Data
 ↓
AI Analysis
 ↓
Validation
 ↓
Insights
 ↓
Human Decision
 ↓
Environmental Action
```

Everything beyond the V1 pipeline is considered future expansion unless explicitly added to the current version.

---

# 31. Final Architectural Principle

ForestAI should evolve from:

```text
A learning-focused data pipeline
```

into:

```text
A machine learning system
```

then into:

```text
A validated environmental intelligence
and decision-support system
```

without sacrificing reliability, transparency, reproducibility, or human oversight.

The architecture should grow **because the real-world problem requires it**, not simply because more technology is available.
