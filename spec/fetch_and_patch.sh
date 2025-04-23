#!/bin/bash

set -euox pipefail
wget https://nightlies.apache.org/flink/flink-docs-master/generated/rest_v1_dispatcher.yml -O rest_v1_dispatcher.yml

# ## Patching the session handle to be string
# for file in rest*job_manager*.yml; do
#     yq e '
#         .components.schemas.SessionHandle = {"type": "string"} |
#         .components.schemas.OperationHandle = {"type": "string"}
#     ' -i "$file"
# done
