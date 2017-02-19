#!/bin/bash

ENV_FILE="$1"
RUN_COMMAND=${@:2}

set -a
source $ENV_FILE
set +a

$RUN_COMMAND
