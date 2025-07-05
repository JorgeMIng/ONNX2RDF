

## 🔗 URI Construction Reference for ONNX2RDF

➡️ Refer to the main [README (link)](README.md) for CLI usage and library integration. This file focuses purely on how the URI are design and created.

This section describes how URIs are dynamically constructed for ONNX resources parsed with **ONNX2RDF**. These URIs define RDF subjects uniquely within the model's structure.

The base formats for every URI are:

```text
{base_url}{model_name_path}/{resource_type}/{resource_id}
```

```text
{base_onnx_url}/{resource_type}/{resource_id}
```

`base_onnx_url` is already defined and cannot be changes as it represents common elements independant of the model.

`base_url` is completly custom to the user and is used to change the desired endpoints eg: `https://my.ontology.me/resource`

`model_name_path` is a semi-custom parameter that is build dynamically depending on the `input-path` given (file or folder with files) and a parameter given by the user

`resource_type` is the class name of the resource the uri is representing

`resource_id` is the semantically created identifier of a instance of the class





## Model and Main Graph

### Model

-
    <font size="3">{base_url}{model_name_path}`/Model`


### Graph

- 
    <font size="3">{base_url}{model_name_path}`/Graph/Graph-{graph_name}`



##  Nodes 
###  Nodes Entry 

- 
    <font size="3">{base_url}{model_name_path}`/Node`/Graph-{graph_name}`-Node-{node_name}`
### Nodes Inputs

- **List Container**
    <font size="3">{base_url}{model_name_path}`/NodeInputs`/Graph-{graph_name}-Node-{node_name}`-inputs`

- **Input Entry**
    <font size="3">{base_url}{model_name_path}`/NodeInput`/Graph-{graph_name}-Node-{node_name}-inputs`-idx-{idx}`

### Nodes Outputs

- **List Container**
    <font size="3">{base_url}{model_name_path}`/NodeOutputs`/Graph-{graph_name}-Node-{node_name}`-outputs`

- **Output Entry**
    <font size="3">{base_url}{model_name_path}`/NodeOutput`/Graph-{graph_name}-Node-{node_name}-outputs`-idx-{idx}`


## Operators

### Operators Entry

- `Non Empty` domain

    <font size="3">{base_onnx_url}`/Operators/name-{name}-domain{domain}-v{version}`

    <font size="3">{base_url}{model_name_path}`/Operators/name-{name}-domain{domain}-v{version}` (Custom operator)

- `Empty domain` (domain is default ONNX domain):

    <font size="3">{base_onnx_url}`/Operators/name-{name}-v{version}`

### Operators Status

- `Status STABLE` domain

    <font size="3">{base_onnx_url}/`StatusStable`

- `Status EXPERIMENTAL` (domain is default ONNX domain):

    <font size="3">{base_onnx_url}/`StatusExperimental`



### Operator Sets

- `Non Empty` domain

    <font size="3">{base_onnx_url}`/OperatorSet/domain{domain}-v{version}`

    <font size="3">{base_url}{model_name_path}`/OperatorSet/domain{domain}-v{version}` (Custom sets)

- `Empty domain` (domain is default ONNX domain):

    <font size="3">{base_onnx_url}`/OperatorSet/v{version}`


## Attributes

### Attribute Entry
-
    <font size="3">{base_url}{model_name_path}`/Attribute`/Graph-{graph_name}-Node-{node_name}`-Attribute-{attribute_name}`


### Attribute Single Value


-
    <font size="3">{base_url}{model_name_path}`/AttributeType`/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}`-{attribute_type}`

    - `AttributeType` class and `attribute_type` can be:
        - `SimpleValue` (INT, FLOAT, STRING)
        - `Tensor`, `SparseTensor` (TENSOR, SPARSE_TENSOR)
        - `GraphValue`, `ValueInfo` (GRAPH, TYPE_PROTO)
        - `UNDEFINED_DATA` (UNDEFINED)


### Attribute Typed Ordered Lists

- **List Container**

    <font size="3">{base_url}{model_name_path}`/TypedOrdererList`/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`{attribute_type}`

- **List Items**

    <font size="3">{base_url}{model_name_path}`/AttributeType`/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`{attribute_type}-idx{index}`

    - `AttributeType` class and `attribute_type` can be:
        - `SimpleValue` (INTS, FLOATS, STRING)
        - `Tensor`, `SparseTensor` (TENSORS, SPARSE_TENSORS)
        - `GraphValue`, `ValueInfo` (GRAPHS, TYPE_PROTOS)
        - `UNDEFINED_DATA` (UNDEFINED)





## Functions

### Functions Entry

- `Non Empty` overload

    <font size="3">{base_url}{model_name_path}`/Functions/Func-name-{name}-domain{domain}-overload{overload}`

- `Empty` overload

    <font size="3">{base_url}{model_name_path}`/Functions/Func-name-{name}-domain{domain}`




### Function ValueInfos
- 
    <font size="3"> {base_url}{model_name_path}`/ValueInfos`/Func-name-{name}-domain{domain}-valuesInfo-`{valueInfo_name}`

-   
    <font size="3">{base_url}{model_name_path}`/ValueInfos`/Func-name-{name}-domain{domain}-overload{overload}-valuesInfo-`{valueInfo_name}`


## General Types

### SimpleValue

&nbsp;&nbsp;&nbsp;&nbsp;Simple Values URIs are the same as show before and have not any more complex structure, just store the value and type (INT,FLOAT,STRING).

- 
    <font size="3">{base_url}{model_name_path}`/SimpleValue`/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}`{attribute_type}`

-  
    <font size="3">{base_url}{model_name_path}`/AttributeType`/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`{attribute_type}-idx{index}`


### Tensor

<html>
    <font size="3">{base_url}{model_name_path}`/Tensor/{resource_id}-{tensor_name}`
</html>


- `tensor_name` in case empty will not be added at the URI 

    <font size="3">{base_url}{model_name_path}`/Tensor/{resource_id}`

- `resource_id` is dependant on where the Tensor is located :
    - Attributes Single Value

        <font size="3">/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`TENSOR-{tensor_name}`
    - Attributes Typed List

        <font size="3">/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`TENSORS-idx{index}-{tensor_name}`
    - Initializers

        <font size="3">/Graph-{graph_name}`Initializer-{tensor_name}`


- A `Tensor` from a SparseTensor (indices and values) would have no name on its URI as the name of the values tensor is already used as name of the sparse_tensor

    - SparseTensor indices

        <font size="3">/Graph-{graph_name}`SparseInitializer-{sparse_tensor_name}-indices`
    - SparseTensor values

        <font size="3">/Graph-{graph_name}`SparseInitializer-{sparse_tensor_name}-values`


- `tensorShape` URIs are created using the `same URI` as the `Tensor` but changing the resource type

    <font size="3">{base_url}{model_name_path}`/TensorShape`/{resource_id}

- `tensorValue` URIs are created using the `same URI` as the `Tensor` but changing the resource type

    <font size="3">{base_url}{model_name_path}`/TensorValue`/{resource_id}

- `tensorSegment` URIs are created using the `same URI` as the `Tensor` but changing the resource type

    <font size="3">{base_url}{model_name_path}`/tensorSegment`/{resource_id}

- `TensorShapeEntry` URIs take the `tensorShape` URI and add the index

    <font size="3">{base_url}{model_name_path}`/TensorShapeEntry`/{resource_id}-idx{idx}`


- `Tensor` possible `DataLocation` URIs are DEFAULT and EXTERNAL its URIs are:

    <font size="3">{base_onnx_url}/`LocationDefault`

    <font size="3">{base_onnx_url}/`LocationExternal`


### Tensor DataTypes

<html>
    <font size="3">Tensor have multiple types the URI follows the scheme`
</html>

<html>
    <font size="3">{base_url}{model_name_path}`/{datatype_id}`
</html>

- `datatype_id` can have the values




    | Name            | URI              | ONNX ID | Description                            | Name             | URI                   | ONNX ID | Description                            |
    |-----------------|------------------|--------|----------------------------------------|------------------|------------------------|--------|----------------------------------------|
    | UNDEFINED       | DataUndefined        | 0      | Unspecified data type                  | FLOAT16          | Float16               | 10     | 16-bit IEEE 754 half-precision         |
    | FLOAT           | DataFloat            | 1      | 32-bit float                           | DOUBLE           | DataDouble                | 11     | 64-bit float (`float64`)               |
    | UINT8           | UInt8            | 2      | 8-bit unsigned integer (`uint8_t`)    | UINT32           | UInt32                | 12     | 32-bit unsigned integer                |
    | INT8            | Int8             | 3      | 8-bit signed integer (`int8_t`)       | UINT64           | UInt64                | 13     | 64-bit unsigned integer                |
    | UINT16          | UInt16           | 4      | 16-bit unsigned integer (`uint16_t`)  | COMPLEX64        | Complex64             | 14     | Complex with `float32` components      |
    | INT16           | Int16            | 5      | 16-bit signed integer (`int16_t`)     | COMPLEX128       | Complex128            | 15     | Complex with `float64` components      |
    | INT32           | Int32            | 6      | 32-bit signed integer (`int32_t`)     | BFLOAT16         | BFloat16              | 16     | Truncated IEEE754 float (8e, 7m bits)  |
    | INT64           | Int64            | 7      | 64-bit signed integer (`int64_t`)     | FLOAT8E4M3FN     | Float8e4m3fn          | 17     | 8-bit float (NaN, no Inf)              |
    | STRING          | DataString           | 8      | UTF-8 string                           | FLOAT8E4M3FNUZ   | Float8e4m3fnuz        | 18     | 8-bit float (NaN, no Inf, no -0)       |
    | BOOL            | DataBool             | 9      | Boolean                                | FLOAT8E5M2       | Float8e5m2            | 19     | 8-bit float (IEEE754, NaN + Inf)       | 
    ||||||||
    | FLOAT8E5M2FNUZ    | Float8e5m2fnuz     | 20    | 8-bit float (IEEE754, NaN, no -0)          | INT4        | Int4        | 22    | 4-bit signed integer                   |
    | UINT4       | Uint4       | 21    | 4-bit unsigned integer           | FLOAT4E2M1        | Float4e2m1         | 23    | 4-bit float (2 exponent, 1 mantissa bits)  |


### SparseTensor

<html>
    <font size="3">{base_url}{model_name_path}`/SparseTensor/{resource_id}-{sparse_tensor_name}`
</html>

- `sparse_tensor_name` in case empty will not be added at the URI 

    <font size="3">{base_url}{model_name_path}`/SparseTensor/{resource_id}`


- `resource_id` is dependant on where the Tensor is located:
    - Attributes Single Value

        <font size="3">/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`SPARSE_TENSOR-{sparse_tensor_name}`
    - Attributes Typed List

        <font size="3">/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`SPARSE_TENSORS-idx{index}-{sparse_tensor_name}`
    - Sparse Initializers

        <font size="3">/Graph-{graph_name}`SparseInitializer-{sparse_tensor_name}`


- `tensorShape` URIs are created using the `same URI` as the `SparseTensor` but changing the resource type

    <font size="3">{base_url}{model_name_path}`/SparseTensor`/{resource_id}

- `TensorShapeEntry` URIs take the `tensorShape` URI and add the index

    <font size="3">{base_url}{model_name_path}`/TensorShapeEntry`/{resource_id}-idx{idx}`



### ValueInfo 

<html>
    <font size="3">{base_url}{model_name_path}`/ValueInfo/{resource_id}`
</html>


- `resource_id` is dependant on where the ValueInfo is:
    - Attributes Single Value

       <font size="3">/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`TYPE_PROTO`
    - Attributes Typed List

       <font size="3">/Graph-{graph_name}-Node-{node_name}-Attribute-{attribute_name}-`TYPE_PROTOS-idx{index}`
    - Inputs

        <font size="3">/Graph-{graph_name}`inputs-{input_name}`
    - Outputs

        <font size="3">/Graph-{graph_name}`outputs-{output_name}`
    - ValueInfos Graph

        <font size="3">/Graph-{graph_name}`valuesInfo-{valueInfo_name}`
    - ValueInfos Function Non Empty Overload

        <font size="3">/Func-name-{name}-domain-{domain}`valuesInfo-{valueInfo_name}`
    - ValueInfos Function Empty Overload

        <font size="3">/Func-name-{name}-domain-{domain}-overload{overload}-valuesInfo-{valueInfo_name}`
- `ValuesInfos` forces a type of one of the possible `OnnxTypes` 


### OnnxTypes


- <font size="3">{base_url}{model_name_path}`/{OnnxType}/{resource_id}`


    - `resource_id` are the same possible values as shown with `ValueInfos`:

    - `OnnxType` can be one of:
        - `SequenceType`, `OptionalType`, `MapType`, `TensorType`, `SparseType`

    - `SequenceType`,`OptionalType` and `MapType` force also
    other OnnxTypes, their URIS will be created appeding `-Seq`, `-Opt`,`-Map`



### Nested GraphType

- When graphs appear inside attributes, recursion applies. There can be unlimited nested graphs using specific Operators like `If`,`Scan`,`Loop`:

    - 
        <font size="3">Graph-{main-graph_name}-{...}-Attribute-{attribute_name}-GRAPH`-Graph-{subgraph_name}`
    - 
        <font size="3">Graph-{main-graph_name}-{...}-Attribute-{attribute_name}-GRAPHS-idx{idx}`-Graph-{subgraph_name}`

---










###
➡️ Refer to the main [README (link)](README.md) for CLI usage and library integration. This file focuses purely on how the URI are design and created.