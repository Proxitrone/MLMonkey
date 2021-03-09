#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function

import os
import constants
import git

if not os.path.exists(constants.JOBS_DIR):
    os.makedirs(constants.JOBS_DIR)

if not os.path.exists(constants.SYSTEM_JSON):
    with open(constants.SYSTEM_JSON, 'a') as f:
        f.write('{}')

if not os.path.exists(constants.BANDWIDTH_TXT):
    with open(constants.BANDWIDTH_TXT, 'a') as f:
        pass

if not os.path.exists(constants.TOPOLOGY_TXT):
    with open(constants.TOPOLOGY_TXT, 'a') as f:
        pass
# Create benchmarking repo directory
if not os.path.exists(constants.BENCHMARKS_DIR):
    os.makedirs(constants.BENCHMARKS_DIR)
    # Clone benchmarking repo on startup
    git.Git(constants.BENCHMARKS_DIR).clone(constants.BENCHMARKS_REPO)
