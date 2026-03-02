# Repository Overview

This is a *very small* example of a bank transfer system built to demonstrate **Test‑Driven Development (TDD)** with Python and pytest.  There is no framework, no database, and the entire domain lives in `app/` with tests under `tests/`.

The only declared dependency is **pytest** (see `requirements.txt`).  The `README.md` simply identifies the project as a TDD example.

## Key Directories & Modules

- `app/`: application code.  Currently contains:
  - `account.py` – expected to define an `Account` class (balance, deposit/withdraw, etc.)
  - `transfer_service.py` – expected to implement transfer logic between accounts.

- `tests/`: pytest test modules.  At the moment `test_transfer_service.py` is empty; tests are the entry point for development.

There are no other packages or sub‑directories.

## Development Workflow

1. **Install dependencies**
   ```bash
   python -m pip install -r requirements.txt
   ```
2. **Run the test suite**
   ```bash
   pytest         # run from project root
   ```
   or `python -m pytest` if you prefer explicit module invocation.

3. **TDD cycle**
   - write a failing test in `tests/test_transfer_service.py` (or add new test files under `tests/`).
   - run pytest to see the failure.
   - implement just enough logic in `app/account.py` or `app/transfer_service.py` to satisfy the test.
   - repeat until all requirements are covered.

All production code lives in the `app` package; tests mirror module names (e.g. `test_account.py` tests `account.py`).

## Project‑Specific Patterns

- **Minimalist design**: no external dependencies other than pytest.  Avoid importing anything not already in `requirements.txt`.
- **Domain objects**: `Account` instances should encapsulate their own balance and provide methods such as `deposit`, `withdraw`, and properties as needed.
- **Atomic transfer**: `transfer_service.py` should expose a function or class method like `transfer(from_acc, to_acc, amount)` that adjusts both accounts and enforces rules (no overdrafts, no negative amounts, etc.).
- **Error handling**: raise built‑in exceptions (e.g. `ValueError`) when operations are invalid; tests should assert these.
- **Naming**: use snake_case for functions and methods, PascalCase for classes.

## Testing Conventions

- Tests should live under `tests/` and be discoverable by pytest (`test_*.py`).
- Use plain assertions; no test utilities are provided yet.
- Start new tests with the simplest scenario first (e.g. "transfer succeeds when sender has sufficient balance").
- Add edge cases gradually (insufficient funds, negative amounts, same account, etc.).
- You can import application code with
  ```python
  from app.account import Account
  from app.transfer_service import transfer
  ```
  (or however you design the API).

## Commands & Debugging

- There is no build step.  Editing Python files and running `pytest` is the primary feedback loop.
- Use any Python debugger (`pdb`, `breakpoint()`) inside tests or application code if needed.
- You can run individual tests with `pytest tests/test_transfer_service.py::test_name`.

## Contribution Notes for AI Agents

- When filling in code, prefer idiomatic Python 3 with type hints only if tests require them.
- Stay inside `app/` for logic; do not modify tests unless you're adding new cases.
- If a new module is needed, create it under `app/` and mirror in `tests/`.
- Because the repository is small and purely educational, prioritise clarity and explicitness over clever abstractions.

> **Note:** There are currently no existing tests or implementations.  Your first task as an agent is usually to add a minimal failing test to drive the initial `Account` class or transfer function.

---

Feel free to ask for clarification if any section of this guide is unclear or seems incomplete.