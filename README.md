# Agentic Router

This repository is the result of the following exercise.

This assignment focuses on extending the Agentic Router notebook with improved query routing and access control.

The required task implements sub-query division, where compound questions are split into smaller independent queries. Each sub-query is routed to the most relevant source, and the retrieved information is combined into a single response while preserving citations.

The bonus task introduces RBAC-aware semantic caching, ensuring cached responses respect role-based access permissions and prevent information leakage across different access levels.

The solution and the local run output are in `001. Agentic Router.ipynb`.

`run_notebook.py` was added only so I could test the notebook from my console. It is not part of the assignment.
