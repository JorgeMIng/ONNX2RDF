from setuptools import setup, find_packages

# Read the contents of your README file (optional but recommended)
with open("README.md", "r") as fh:
    long_description = fh.read()
import subprocess

def warn_if_no_java():
    try:
        subprocess.run(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except Exception:
        print("⚠️ WARNING: Java (OpenJDK) not found. This package may not work correctly without Java.")

warn_if_no_java()

# Define the setup function for setuptools
setup(
    name="ONNX2RDF",  # Replace with your project name
    version="0.1.0",  # Replace with your version
    author="Jorge M",  # Replace with your name
    author_email="jorge.martin.izquierdo@upm.es",  # Replace with your email
    description="ONNX to rdf parser",  # A short description
    long_description=long_description,  # Long description from README
    long_description_content_type="text/markdown",  # Set content type to markdown if README is .md
    #url="https://github.com/yourusername/yourproject",  # Replace with your project's URL
    packages=find_packages(),  # This will find all Python modules inside the ONNX2RDF folder
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change the license type if different
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",  # Define the minimum required Python version
    install_requires=[  # List any dependencies your project has
       "onnx","onnxruntime","torch","ruamel.yaml","pathvalidate"  # Example of a dependency
    ],
    package_data={
        'ONNX2RDF': [
            'mappings/*.*',  # Include all files in the mappings folder
            'ontology/*.*',  # Include all files in the ontology folder
            './rmlmapper-7.3.1-r374-all.jar'  # Include the rmlmapper.java file
        ],
    },
    entry_points={  # Optional: Define command-line interface if applicable
        "console_scripts": [
            "onnx-parser=ONNX2RDF.parser:call_main_with_args",  # Example of command-line entry
        ],
    },
    # Optional: Include data files if needed
    # package_data={
    #     "your_package": ["data/*.txt"],
    # },
)