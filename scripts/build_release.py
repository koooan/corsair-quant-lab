"""Execute both notebook interfaces and export a local release preview."""
from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))
# Keep local caches inside the ignored project directory, portable across machines.
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".jupyter/matplotlib"))
os.environ.setdefault("IPYTHONDIR", str(ROOT / ".jupyter/ipython"))
os.environ.setdefault("JUPYTER_RUNTIME_DIR", str(ROOT / ".jupyter/runtime"))
os.environ.setdefault("MPLBACKEND", "Agg")

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager
from corsair_lab.evaluation import write_artifacts


def main():
    scores = write_artifacts()
    notebook_path = ROOT / "notebooks/jupyter/01_foundation.ipynb"
    notebook = nbformat.read(notebook_path, as_version=4)
    nbformat.validate(notebook)
    with tempfile.TemporaryDirectory(prefix="corsair-kernels-") as directory:
        kernel_path = Path(directory) / "python3"
        kernel_path.mkdir()
        (kernel_path / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Python 3", "language": "python"}))
        manager = KernelManager(kernel_name="python3", kernel_spec_manager=KernelSpecManager(kernel_dirs=[directory]))
        client = NotebookClient(notebook, km=manager, timeout=120,
                                resources={"metadata": {"path": str(ROOT)}})
        try:
            client.execute()
        finally:
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)
    nbformat.write(notebook, notebook_path)
    if not any("image/png" in output.get("data", {}) for cell in notebook.cells
               if cell.cell_type == "code" for output in cell.outputs):
        raise RuntimeError("Notebook must retain a rendered chart, not just a Figure repr")
    html, _ = HTMLExporter().from_notebook_node(notebook)
    html = html.replace('../../docs/', 'https://github.com/koooan/corsair-quant-lab/blob/main/docs/')
    (ROOT / "artifacts/week01_jupyter.html").write_text(html)
    subprocess.run([sys.executable, "-m", "marimo", "check", "notebooks/marimo/01_foundation.py"], check=True)
    subprocess.run([sys.executable, "-m", "marimo", "export", "html", "notebooks/marimo/01_foundation.py",
                    "-o", "artifacts/week01_marimo.html", "--force", "--no-include-code"], check=True)
    print(scores.to_string(index=False))
    print("Both notebooks executed; HTML previews are in artifacts/.")


if __name__ == "__main__":
    main()
