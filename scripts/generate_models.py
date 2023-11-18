"""System Bridge: Generate Models"""
import os
import subprocess
import sys

# Install datamodel-code-generator and black
print("Updating datamodel-code-generator and black..")
command = [
    sys.executable,
    "-m",
    "pip",
    "install",
    "--upgrade",
    "datamodel-code-generator",
    "pyupgrade",
    "isort",
    "black",
]
print(" ".join(command))
with subprocess.Popen(command) as process:
    process.wait()

print("Generating models..")

path_from_schemas = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "schemas",
    )
)
path_to_models = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "systembridgemodels",
    )
)

for root, _, files in os.walk(path_from_schemas):
    for file in files:
        if file.endswith(".json"):
            module = file.split(".")[0]

            path_from = os.path.join(root, file)
            path_to = os.path.join(path_to_models, module + ".py")

            print(f"Generating model {module} from {path_from} to {path_to}")

            command = [
                "datamodel-codegen",
                "--disable-timestamp",
                "--class-name",
                module,
                "--input",
                path_from,
                "--input-file-type",
                "jsonschema",
                "--output",
                path_to,
                "--snake-case-field",
                "--use-schema-description",
                "--use-standard-collections",
            ]

            print(" ".join(command))

            with subprocess.Popen(command) as process:
                process.wait()

            command = [
                "pyupgrade",
                path_to,
            ]

            print(" ".join(command))

            with subprocess.Popen(command) as process:
                process.wait()

            command = [
                "isort",
                "--rm",
                "from typing import Dict",
                "--rm",
                "from typing import List",
                "--rm",
                "from typing import Optional",
                "--rm",
                "from typing import Union",
                path_to,
            ]

            print(" ".join(command))

            with subprocess.Popen(command) as process:
                process.wait()

            command = [
                sys.executable,
                "-m",
                "black",
                path_to,
            ]

            print(" ".join(command))

            with subprocess.Popen(command) as process:
                process.wait()
