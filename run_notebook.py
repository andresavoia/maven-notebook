"""Run the assignment cells and print the results.

Skips the Colab shell cells and the middle demos. Runs Part 1 and the RBAC
self-check, which are the cells that grade this notebook.
"""

import io
import os
import sys
import traceback
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import nbformat
from nbformat.v4 import new_output

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / "001. Agentic Router.ipynb"
os.chdir(ROOT)

# Pip, Colab shell magics, and the repeated demo calls.
SKIP = {3, 8, 13, 14, 17, 18, 28, 29, 30, 31, 32, 37, 38, 39, 40, 45}
SAVE_OUTPUT = {46, 49}


def main() -> int:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    namespace = {"__name__": "__main__"}

    for index, cell in enumerate(notebook.cells):
        if cell.cell_type != "code" or index in SKIP:
            continue

        source = cell.source if isinstance(cell.source, str) else "".join(cell.source)
        print(f"\n===== cell {index} =====", flush=True)
        stdout, stderr = io.StringIO(), io.StringIO()
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                exec(compile(source, f"cell_{index}", "exec"), namespace)
        except Exception:
            captured = stdout.getvalue() + stderr.getvalue()
            error = traceback.format_exc()
            print(captured)
            print(error)
            if index in SAVE_OUTPUT:
                cell.outputs = [
                    new_output(output_type="stream", name="stdout", text=captured),
                    new_output(output_type="stream", name="stderr", text=error),
                ]
                nbformat.write(notebook, NOTEBOOK)
            return 1

        captured = stdout.getvalue() + stderr.getvalue()
        if captured.strip():
            print(captured, end="" if captured.endswith("\n") else "\n")
        if index in SAVE_OUTPUT:
            cell.outputs = [new_output(output_type="stream", name="stdout", text=captured)]
            nbformat.write(notebook, NOTEBOOK)

    print("\nNOTEBOOK_RUN_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
