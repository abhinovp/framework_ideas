A simple python based generator automation framework, that accomplishes:

Less or no usage of flat files.
Transactions on the fly sequential or in parallel.
Wider scope for expanding use-cases into suites.
Transaction suites instead of scripts.
All the above, while considering minimal code change and maximum code re-usability.

Applicable Use-cases:

1. Micro-services
2. Database IO
3. NFS/SMB IO workloads over on-prem VMs.
4. Aggregator APIs
5. Test automation


Crucial dependencies:
1. Framework config mapper - This script will hold all needed workflows defined with hops between defs/classes.
2. User input transformer - This script will have to ingest user input or pre-def input and convert to a framework specific sequence.
