<h1> 5-Generator based automation framework </h1>

## 1. A simple python based generator automation framework, that accomplishes:

1. Less or no usage of flat files.
2. Transactions on the fly sequential or in parallel.
3. Wider scope for expanding use-cases into suites.
4. Transaction suites instead of scripts.
5. All the above, while considering minimal code change and maximum code re-usability.

## 2. Applicable Use-cases:

1. Micro-services
2. Database IO
3. NFS/SMB IO workloads over on-prem VMs.
4. Aggregator APIs
5. Test automation



## 3. Working

![alt text](https://github.com/ippudkippude/ippudkippude/blob/main/5-Gen%20example.PNG)


1. Each oval represents a class holding multiple defs designed as a generator, these generators in-turn could hold any logic, wrapping sequence or clean-up tasks. These generators are best held within classes while the object calls are abstracted in the config_mapper.py
2. The framework begins by reading the user-input and tranforming into a sequence designed in the config_mapper.py. Used eval() to hold and evaluate each object calls respectively.
3. Completes one cycle with all hops among Gen1 to Gen 5 without waiting. Then repeats for all input/injest data from Gen 1 is iterated.
4. Results can be directed to excel, csv, grafana , BigQuery or Google Sheets as per SDKs availablity.

## Example using 3 micro-services API calls using feature transformation.
## Referring to the image above.

Workflow A : Collects data, Builds a query, conducts a MySQL transaction, transforms the fetched records, writes to output.

Workflow B : Collects data, Builds test data for UI automation test case, conducts a get on URL, transforms the fetched target, prepares a report.

Workflow C : Collects raw data, Cleans the data, added feature engineering, trains a smaller set for a ML algorightm, predict and evaluate test data, prepares a report.

## Possible to mix and match the Generator classes ? Yes !

Data cleaning logic for SQL test data could be re-used in Workflow C.

Transformation logic for web scraped response could be re-used in Workflow A.

The config_mapper should be made to re-direct respective hops accordingly.

## 4. Crucial dependencies:

1. Framework config mapper - This script will hold all needed workflows defined with hops between defs/classes.
2. User input transformer - This script will have to ingest user input or pre-def input and convert to a framework specific sequence.
3. The user inputs can then be set into a concurrent calls as each workflow stays independent at runtime. Appropriate async/aiohttp calls could be added.

The End.
