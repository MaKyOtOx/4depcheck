#
# Licensed to 4depcheck under one or more contributor
# license agreements. See the NOTICE file distributed with
# this work for additional information regarding copyright
# ownership. 4depcheck licenses this file to you under
# the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import tempfile

from cli.dep_check_cli_parser import DepCheckCLIParser
from tool.orchestrator import run_tools


# -- Main function
def main(parsed_args):
    # -- Run analysis
    full_report = run_tools(path_to_analyze=parsed_args.get_dir())

    # -- Print full report (STDOUT and file)
    print(full_report)
    with open(tempfile.gettempdir() + "/4depcheck/" +
              parsed_args.get_project_name().replace(' ', '_') + ".json", "w") as report_file:
        report_file.write(full_report)


if __name__ == "__main__":
    main(DepCheckCLIParser())
