# TODO LIST of improvements of ONNX2RDF

## Mayor Upgrades

### Tester

Add complex tester for preprocess module and test yarrrml file

### Progress Bar Update

Add functionalities to have progress bar on top of the log messeges using tqdm.


### Complex Types and raw-data

Type checking of complex types and check raw_data entry validation

### Fill operator

The function fill_operator_metadata should be able to build more info considering types of inputs/outputs

### Device Configuration
onnx 1.18 introduces Device configuration with an update of the IR. Add those new data to the parser.

### Onnxruntime custom libraries

Find a method to add OPSchemas of custom libraries if possible


## Minor Upgrades

### Logger 
Refactor code in relation to warnings and error messeges, being able to define multiple levels of warnings.

With the objective of having warnings that should not be considered as error or the model has a problem.

### Error messeges improvemente
Make sure all error/warning messeges are similar and follow a consistant style


### Option to add custom yarrrml rml files that encapsulated all files
In the case of multiple model (folder path) the option extrafiles is executed with each model.
In case metadata encapssulates all rdf files option to add new yarrmls, to be executed and created a new output.

For now function "yarrml2_rdf_pipeline" solves this issues given the option to execute the parser with customs yarrrml.



