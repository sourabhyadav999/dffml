import os
import sys
import ast
import subprocess
from io import open

from setuptools import find_packages, setup

self_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(self_path, "dffml_operations_binsec", "version.py"), "r") as f:
    for line in f:
        if line.startswith("VERSION"):
            version = ast.literal_eval(line.strip().split("=")[-1].strip())
            break

with open(os.path.join(self_path, "README.md"), "r", encoding="utf-8") as f:
    readme = f.read()

INSTALL_REQUIRES = [
    "aiohttp>=3.5.4",
    # 'rpmfile>=1.0.0',
    "pyelftools>=0.25",
]

git_rpmfile = "git+https://github.com/pdxjohnny/rpmfile@subfile_close"

try:
    import rpmfile
except (ModuleNotFoundError, ImportError):
    if "--user" in sys.argv:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "--user",
                git_rpmfile,
            ],
            check=False,
        )
    else:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", git_rpmfile],
            check=False,
        )

setup(
    name="dffml-operations-binsec",
    version=version,
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="John Andersen",
    author_email="john.s.andersen@intel.com",
    url="https://github.com/intel/dffml/blob/binsec/README.md",
    license="MIT",
    keywords=["dffml"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=INSTALL_REQUIRES,
    tests_require=[],
    packages=find_packages(),
    entry_points={
        "dffml.operation": [
            "url_to_urlbytes = dffml_operations_binsec.operations:URLToURLBytes",
            "urlbytes_to_tarfile = dffml_operations_binsec.operations:urlbytes_to_tarfile",
            "urlbytes_to_rpmfile = dffml_operations_binsec.operations:urlbytes_to_rpmfile",
            "files_in_rpm = dffml_operations_binsec.operations:files_in_rpm",
            "is_binary_pie = dffml_operations_binsec.operations:is_binary_pie",
            "cleanup_rpm = dffml_operations_binsec.operations:cleanup_rpm",
        ],
    },
)
