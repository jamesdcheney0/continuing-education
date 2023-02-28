# Review
## 
- Terraform workspaces: isolate and manage multiple versions of tf state
    - `terraform workspace <name>`
- Variables
    - can be as simple as `<variable> "<var_name>" {}`
- Terraform is stateful - everything is stored in a state file, which is written in JSON
    - By default, stored locally
- providers: registry.terraform.io/providers used to define AWS/GCP/Azure etc
## Credentials
- can define in template (e.g. in main.tf) - not recommended 
- avoid using full admin IAM profile when more granular permissions could be used
- tf will automatically look for AWS credentials in environment variables [AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION]
- can also point main.tf to existing credential file

## Terraform CLI commands
- init/validate/plan/apply/destroy - main commands
- init - initilzie tf in current directory
- TERRAFORM WILL NOT ROLL BACK CONFIGURATIONS IF IT FAILS PARTWAY THROUGH
    - when using git, can step back to working template & reapply
## Terraform Language - HCL syntax

- single line comment: `#`
- multi-line comment: `/* <comment \n comment> */`
- multi-line string: `<<EOF string \n string EOF`
- interpolated variable: `"public-${var.project}"`
- map: defined by {}
    - ```
        variable = "amis" {
            type = map
            default = {
                "us-east-1": "data"
                "us-west-1": "other-data"
            }
        }
        ```
- data sources: obtain information outside of what has been defined by tf

### Variables
- multiple ways to define variables; highest priority to lowest as follows: 
    - CLI flag
    - configuration file as CLI argument 
        - e.g. `terraform apply -var-file="file.tfvars"`
    - environment variable 
        - e.g. `export <variable>` in the CLI before run
    - default config - value in `variables.tf`
    - manual entry - asked in the CLI

### Modules
- combine related resources
- collection of .tf files contained w/n directory 
- tf has a repo of modules

### Expressions
- Functions: transform and combine values
- Count meta argument: makes it so that subnets can be made for all the defined AZs
- element function: wraps around when index is exceeded
- interpolation: when referencing resources, tf can figure out dependencies, so `depends_on` isn't necessary
    - implicit dependencies are stored in state and created by interpolation

# Test Review (random tidbits to remember)
- complex types: groups multiple values into a single value
- core tf workflow: write, plan, apply
- input variable precedence: env vars < .tfvars < .tfvars.json < *.auto.tfvars* < -var, -var-file 
- tf cloud features: remote state management, remote tf execution, provides private module registry
- anyone can publish & share module on the tf registry
- hashicorp sentinel is a policy as code framework
- terraform manages state lock itself
    - State lock can be disabled with -lock (not recommended)
- use the CLI argument `-target={resource}` to only view specific resources in `terraform plan`
- output variables are only run and sent to stdout when `terraform apply` is ran
- setup tf logs to single location: export the environment variable TF_LOG to be INFO, export TF_LOG_PATH environment variable to specified path
- data sources: data to be fetched or computed for use elsewhere in tf
- increase # of operations that are concurrently used: `terraform apply -parallelism={<number of ops>}`. Number of ops is 10 by default
- ensure S3 access by correct team members: specify file path to API key, make sure bucket policy is correct
- correcctly reference PRIVATE registry module source: `hostname/namespace/name/provider`
- syntax for specifying module in public terraform registry: `namespace/name/provider`
- `var.<var_name>` to reference variables. 
- `terraform plan` and etc run on all *.tf in current directory by default
- tf plug-in installations via local or HTTPS
- default provider block configuration has no required default parameters, although its populatr to do region
- an input variable w no type set will accept any type
- `terraform workspace new <workspace-name>` to set up new workspace
- meta arguemnt `provider: aws.west` can be used by resource to change the provider if there are multiple options
- `terraform fmt -diff` to see differences when formatting .tf files
- two types of backends: standard (local) and enhanced (local and remote)
- set `TF_LOG` environment variable to setup detailed tf logs
- by default, tf stored state in direcotry its working in
- `terraform providers lock` to lock a providers file
- empty backend configured in root of tf configuration files is requred when configuring partial backend configuration
- managing state for teams is best done by configuring remote backend
- Cause a resource to run a command when `terraform destroy` is called 
    - ```
        when = destroy
        command = <command>
        ```
- configure backend through the backend block, under the terraform block
- `terraform validate` does NOT Cconnect to remote state/APIs when run
- two configuration variables available to default local backend: path, workspace_dir
- complex types: collection type, structural type (made up of values called element types)
- accepted conditions for provisioners that have `on_failure` key specified: `contine`, `fail`
- get JSON output from validate command: `terraform validate -json` 
- use workspaces to manage small differences b/w different environments
- `local-exec` provisioner executes code in its block on the local machine running tf
- built-in functions tf provides: max(), regex(), alltrue(), and many others, reviewed in ABCC
- tf follows semantic module versioning
- show all resources in state: `terraform state list`
- init a directory with a specific source: `terraform init -from-module={<module_source}` 
- access module attributes through child module by declaring an output value to export values to calling module
- module path and resource specification is required to successfully import tf resources
- tf workspace store state files in `terraform.tfstaste.d`
- when version is able to be defined, set it explicitly, according to tf registry
- reference data source `data.<data_type>.<name>`
- when using `when = destroy` before resource is destroyed, provisioner invokes command
- if injecting secrets into state file, the WILL SHOW UP after `terraform apply` is run
- config file formats allowed: HCL, JSON
- hashicorp sentinel written for integration w Go, can be executed locally & in cloud. NOT open source

# Andrew Brown Exam Pro Review
## Introduction
- tf is a tool that is declarative and agnostic. Automate creation, update, and destruction of cloud infrastructure
    - partly imperative, mostly declarative; allows 'for loops', 'dynamic blocks', locals, complex data structures
- IaC enhances infrastructure lifecycle by being reliable, manageable, sensible 
    - idemopotent: when updating on IaC file, it modifies existing infrastructure instead of adding to it
- configuration drift: 
    - detected by config tool (.e.g AWS config)
    - corrected by refresh & plan w/n tf or manually adding to tf, although manually adding is not recommended (use import instead)
    - prevented by using immutable infrastructure - always destroying & rebuilding, not modifying after deployment
- mutable infrastructure: has stuff set in the configure stage with user data, etc
- immutable infrastructure: set up w baked AMIs in deploy stage
- GitOps: use IaC and git to formally review and process changes through a pipeline
- packer: used to build images (AMIs) for cloud providers
- terraform cloud: remote state storage, version control integration, flexible workflows, collaboration on infrastructure changes in web portal
- terraform lifecycle: write -> init -> plan/validate -> apply [-> write] or [-> destroy -> write]
- visualize execution plans: with graphwiz installed, run `terraform graph`
- locals: kinda like vars, but hard-coded in template
provider: can be added w/n resource to point to specific provider alias
- tf provisioners: install software, edit files, provision machines made w tf, cloud-init (aka user-data in AWS) using YAML or bash, or packer auto-image builder
- provisioners like chef, puppet, salt stack are depreciated and should only be used as a last resort, as they can create changes outside of code
    - cloud-init, then call it w tf is the recommended approach
    - provisioner 
    ```
    "local exec"{
        command = "<required command>"
    }
    ```
    - remote exec: allows commands to be executed on remote resource after it is provisioned
        - useful for simple stuff, but packer & cloud-init are better 
        - inline: specific commands provided
        - script(s): one or multiple scripts to use
    - file provisioner: copy files from local machine to remote
    - connection block: tells provisioner or resource how to establish connection
    - null resources: placeholder for resources that have no specific association to provider resources
- cloud-init example
    - when public key (.pub part) is added to tf, that key will be put on the instance
    - data: can be used to treat a hard coded value, e.g. VPC ID, as a tf resource
    - cloud-init: important for the user data file to start w `# cloud-config`
    - `terraform  apply -refresh-only` only updates new info in template
- tf registry: public portal to browse providers & modules
    - providers: plugin mapped to cloud service provider API
    - modules: group of config files that provide common config functionality
- `terraform providers`: list currently used providers
- can use alias for alternate providers - e.g. using different regions for resources in AWS 
- HCL (Hashicorp Configuration Files): `.tf`, `.tf.json`
- elements
    - block, block label
    - arguments (appear w/n blocks)
    - expression: values for arguments
    - supports JSON w .tf.json file naming
- terraform settings `terraform{...}`
- HCL: open source toolkit for structured configuration languages
    - used in more than just tf; used by most Hashicorp products
- input variables - parameters for tf modules
    - delcared in root or child modules
    - allowable fields: default, type, description, validation, sensitive
- variable definition files: `terraform.tfvars`, `*.tfvars.json`
- environment variables: get w `TF_VAR<variable_name>`
- loading input variables (highest priority to lowest)
    - specify vars via CLI: `-var ec2_type="t2.medium"`
    - specify vars file via CLI: `-var-file my-vars.tfvars`
    - additional var files: `my-var.tfvars` - specified via CLI
    - additional autoloaded var files: `my-var.auto.tfvars` - will load automatically
    - default autoloaded vars file: `terraform.tfvars`
    - env vars: `TF_VAR_<my_var_name>` - common when using CI/CD
- output values: computed after `terraform apply` performed
    - if marked as sensitive, won't show in logs or CLI, but WILL show in state file
    - `terraform output` lists all outputs in state file
    - `terraform output <name>` lists specific outputs
    - add `-json` to see output in JSON
- local values: assigns name to an expression for reuse
    - can reference locals w/n other locals, and can have multiple locals defined
    - when referencing, use `local` - singular
    - best practice to use sparingly
- data sources: use info defined outside tf

## references to named values: built-in expressions to reference values
- resources: `<resource_type>.<name>` 
    - e.g. `aws_instance.my_server`
- input vars: `var.<name>`
- local values: `local.<name>`
- child module outputs: `module.<name>`
- data sources: `data.<data_type>.<name>`
- file system/workspace info
    - path.module: path of the module where expression is placed
    - path.root: path of root module of config
    - path.cwd: path of current working directory
    - terraform workspaces: name of current workspace
- block-local values (optional values w/n blocks)
    - `count.index` 
    - `each.key`/`each.value`
    - `self.<attribute>`
## Resource Meta Arguments
- depends_on: by default, tf implies the order
- count: create multiples based on a count
    - can manage a pool of objects. Requires a number
    - uses count.index that starts at 0
- for_each: iterate over a map of dynamic values
    ```
    for_each = {
        a_group = 'eastus1'
        another_group = 'westus2'
    }
    name = each.key
    location = each.value
    ``` 
    or
    ```
    for_each = toset(["Todd", "James", "Alice", "Dottie"])
    name = each.key
    ```
- resource providers & alias
    - create additional provider + give it an alias. Separate from default
- lifecycle - resource behavior
    - `+`: create
    - `-`: destroy
    - `~`: update in-place
    - `-/+`: destroy then recreate
    - lifecycle blocks allows changing what happens to a resource based on behavior
- provisioner: extra actions after creation

## Expressions
- Types + values: result of an expression is a value. All values have types
    - primitive types: string, number, bool (no type: null; represents absence or omissions)
    - complex structure/collection types: list(typle), map(object)
- strings + string templates
    - must use double quotes - double quotes cna interpret escape sequences
    - `<< EOT ... EOT` before and after to make multi-line string (known as heredoc)
        - Can be EOT, EOF, the term doesn't matter, just has to be the same word immediately after `<<` and at the end
    - strings templates
        - string interpolation, e.g. `"hello, ${var.name}!"`
            - can also use w multi-line strings
- operators: mathematical operations performed on numbers
- conditional: `<condition> ? <true_value>:<false_value>` (supports ternary conditional operators)
    - `<condition>` is the piece that's being brought into be evaluated against the true/false
    - used for if-else statements. The `:` indicates the 'else'
- for: can accept a list, set, typle, map, or object [not related to for_each]
    - []: amend the expression; returns tuple
    - {}: amend the expression; returns an object
    - if statement can be used w/n for statement
    - implicit element ordering: maps, objects, set of strings
        - listed alphabetically; Other types ordered arbitrarily
- splat: provides shorter express for `for` expressions
    - e.g. `var.list[*].id` to return all `.id` in list
    - can work w 0 elements. Helpful dealing w optional values & ignoring if not present 
- dynamic blocks: dynamically construct repeatable nested blocks
    - define objects in locals, then use for_each
- version constrants
    - uses semantic versioning (e.g. `1.2.0`; major.minor.patch)
        - major version: incompatible API changes 
        - minor version: add backwards-compatible functionality
        - patch version: add backwards-compatible bug fixes
    - version constraint is string containing one or more conditions
        - `-`, `!=`, `>`, `>=`, `<`, `<=`: self explanatory
        - `~>`: only last number can change
- progressive versioning: using latest version to keep proactive stance on security is the best practice
    - use `~>` or `>=` to version progressively

## Terraform
- state: particular condition of cloud resources at a specific time
    - state file: `terraform.tfstate` is created when tf is ran
        - JSON data structure w one-to-one mapping from resource instances to remote objects
    - CLI commands
        - `terraform state list|mv|pull|push|replace-provider|rm|show`
            - list resources
            - move item w/n state
                - changes have to be made in main.tf first, then `mv` can be used
                - rename existing resources: `terraform state mv <resource>.<name> <resource>.<new_name>`
                - move a resource into a module: `terraform state mv <resource>.<name> <module>.<resource>.<name>`
                - move a module into a module: `terraform state mv <module>.<resource> <module>.<parent_module>.<resource>`
            - pull from remote
            - push to remote
            - change providers
            - remove resources from state
            - show a resource in state
    - terraform state backups
        - all tf state subcommands that modify state will write a backup file
            - read only commands will not modify
            - tf will take current state and store in `terraform.tfstate.backup`
                - backups can't be disabled
- init
    - downloads plugin dependencies (e.g. providers & modules)
    - creates `.terraform` directory
    - creates dependency lock file to enforce expected versions for plugins & tf
    - must be run again when dependencies are changed or modified
    - `tf init -upgrade|-get-plugsin-false|-plugin-dir=PATH|-lockfile=MODE`
        - upgrade all plugins to latest compliant version
        - skip plugin installation
        - force plugin installation from specific directory
        - set dependency lockfile mode
    - dependency lock file: `.terraform.lock.hcl`
    - state lock file: `.terraform.tfstate.lock.hcl`
- get
    - `terraform get`
    - used to download and update modules in the root modules
- debugging
    - `terraform fmt`: rewrites tf config files to standard format & style
    - `terraform validate`: validates syntax + arguments of tf config files in directory (automatically runs when `terraform plan|apply` are run
    - `terraform console`: interactive shell to evaluate tf expressions
- plan
    - speculative plans: what's show when `terraform plan` or `terraform apply` is run w/o typing yes
    - saved plans: `terraform plan -out=<file>.plan`: save a file of the `terraform apply` that can then be run using `terraform apply <file>.plan`
        - won't ask for confirmation when applying file extension of .plan
        - `<file>.plan` is a binary file that can't be read in code editor
- apply
    - executes actions proposed in execution plan
    - automatic plan mode: `terraform apply` executes plan,validate, apply. Requires manually approval by default
    - saved plan mode: `terraform apply <file>.plan` runs the plan immediately with no approval required
- managing resource drift
    - `terraform apply -replace`: replace resources
        - marks resources for replacement when `terraform apply is ran`
        - replaces taint & prompts for confirmation
        - replaces one resource at a time 
    - `terraform import <resource>.<resource_name> <id-of-resource-from-cloud-provider>`: import existing resources into terraform
        - define a placeholder in config file for imported resources
        - leave the body of the placeholder blank & manually fill after importing [DOES NOT AUTOFILL]
        - ID of resources like vpc-XXXXX or i-XXXXXX
        - can only import one resource at a time
        - not all resources are able to be imported
    - `terraform apply -refresh-only`: refresh state 
        - reads current settings from all managed objects & updates tf state
        - use-case: e.g. instance manually terminated. It should be terminated, but wasn't done in tf. `terraform apply` would want to make a new one. `terraform apply -refresh-only` would update the state file to recognize instance should be gone
    - resource addressing
        - [module path].[resource specification]
        - `<module>.<module_name>[module_index(if applicable)].<resource_type>.<resource_name>[instance_index(if applicable)]`
            - addresses a module w/n tree of modules, then addresses specific resource instance in module
            - `<module>`: namespace for modules
            - `<module_name>`: user-defined name of modules
            - `<resource_type>`: type of resource being addressed
            - `<resource_name>`: user-defined name for resource
- troubleshooting
    - language errors: `fmt`, `validate`, `version`
    - state errors: `refresh`, `apply`, `replace`
        - these two are easier to solve when troubleshooting
    - core errors: `TF_LOG` to find info & report on github
    - provider errors
    - debugging
        - set `TF_LOG` environment variable to `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `JSON`
            - e.g. `TF_LOG=trace`
            - capitalization doesn't actually matter
        - `TF_LOG`s can be enabled separately: `TF_LOG_CORE`, `TF_LOG_PROVIDER`
        - `TF_LOG_PATH=<path>` to choose where to log
    - crash logs: if tf crashes in a panic, it saves a log file w debug logs from session
- modules
    - tf registry (only verified & official modules will show in search bar) - public modules
        - `<namespace>/<name>/<provider>`
        - verified modules - reviewed by hashicorp & actively maintained by contributors 
            - unverified shouldn't necessarily be considered low quality
    - private modules: in tf cloud (need tf login for tf cloud), or from private repos (github, etc)
        - `<hostname>/<namespace>/<name>/<provider>`
    - standard module structure
        - primary entry point is the root module, and should contain `main.tf`, `variables.tf` & `outputs.tf`
        - nested modules are optional, and must be continaed in `modules/<directory>`
            - README w/n directory indicates module can be used on its own
            - no README indicates module is for internal module use only
- team workflows 
    - core tf workflow: write > plan > apply 
    - individual practicitioner
        - write: write tf locally, store in github/git, run `terraform plan|validate` to test - tight feedback loop
        - plan: commit code to local repo
        - apply: run `terraform apply` & wait for provisioning, then commit to github
    - team 
        - write: write local code, stored on branch in remote repo. `terraform plan` for quick feedback loop
            - as team grows, CI/CD process implmeneted
        - plan: when branch is ready, pull request submitted
        - apply: merge must be approved & merged, then code build server runs `terraform apply`
        - team must make CI/CD pipeline, have to figure out state storage, permissions, safely store & inject secrets, and manageing multiple environments requires duplication of code
    - terraform cloud (team workflow)
        - write: use tf cloud as backend. Input variables stored in tf cloud. Tf cloud integrates w git to set up CI/CD; branch/commit strategy remains the same
        - plan: pull request created & tf cloud creates speculative plan
        - apply: after merge, tf cloud will run `terraform apply`. Team member can confirm & apply changes
        - streamlines CI/CD effort, secures credentials, and makes it easier to audit history of multiple runs
- backends: where & how operations are performed
    - standard backends (including S3): only store state. External CLI required to perform tf operations
        - third party options: AWS S3 (with state locking via DynamoDB), Azure, Google Cloud, Alibaba, etc
            - configuring standard backend does not require tf cloud account or workspacef
    - enhanced backends: store state and perform tf operations
        - local backend: stores state on local filesystem (could be an EC2 instance; not necessarily only on personal computer)
            - used by default when no backend defined
            - local backend can be defined to a specific directory under the `terraform` backend block
        - remote backend: uses tf cloud (or tf enterprise)
            - when `terraform apply` performed w CLI, remote backend executes operation
            - provider credentials need to be configured in the remote backend
            - need to set tf cloud workspace & define in backend block. If not defined, tf will ask when operations run
    - backend initialization
        - `terraform init -backend-config=backend.hcl`: used when backend info is sensitive & shouldn't be in config file. `backend.hcl` in this case defines backend
    - `terraform_remote_state` [data source]: retrieves root module output values from another tf config
        - kinda like using outputs b/w stacks in cloudformation
        - uses latest state snapshot from remote backend
            - works w local & remote backend
        - resource data & output values from nested modules NOT accessible
            - it is possible to configure passthrough of those values in the root module
        - user must have access to entire state snapshot, which may include sensitive info
        - it is recommended to explicitly publish data for external consumption to a separate location instead of accessing via remote state (better because it works off live data)
    - state locking: tf will lock state for all operations that can write state
        - prevents other from acquiring lock & corrupting state
        - happens automatically
        - messages on completion or failure aren't published, only if taking too long
        - not recommended: can be disabled
        - not recommended: `force-unlock` can be used to unlock state if unlocking fails
            - `force-unlock` required a unique ID. ID will be outputted if unlocking fails
            - `-force` will skip confirmation
    - protecting sensitive data
        - local state: state is stored in plain-text and may contain AWS credentials
            - don't share file w anyone. Include it on .gitignore; DON'T COMMIT STATE!
        - remote state w tf cloud
            - state file is in memroy & not persisted to disk
            - state file encrypted-at-rest and -in-transit
            - tf enterprise includes detailed audit logging for tamper evidence
        - remote state w third-party
            - review backend capabilities
            - not as secure by default as tf cloud, but can be beefed up to requirements
    - terraform ignore file (`.terraformignore`)
        - works similar to .gitignore but used by tf cloud
        - can only have one in the root directory
- resource: represent infrastructure objects
    - belogs to a provider (can be explicitly set in resource block)
    - can create timeout blocks to timeout how long to give creation and deletion before canceling them

## Complex types
- type that groups multiple values into single value
- collection types (group similar values)
    - allow multiple objects of one type to be grouped together as single value
    - element type: type of the value w/n collection
    - list: like an array, use integer as index
    - map: key:value, access w key
    - set: similar to list, but no secondary index or preserved ordering
        - all values will be the same type as the first element in the set (e.g., if the set is created with a str and a few ints, the ints will be converted to str)
- structural types (group potentially dissimilar values)
    - allows multiple values of distinct types to be grouped as a single value
    - requires schema as an argument
    - object: like a map, with more explicit keying
    - tuple: multiple return types 

# Built-in Functions
## Numeric Functions
- abs(): gives absolute value of given number
- floor(): returns closest whole number that is <= to given value
- log(x,y): returns logarithm of a given number 
- ceil(): rounds up to nearest whole number
- min(): takes one or more numbers & returns the smallest number from the set
- max(): takes one or more numbers & returns the largest number from the set
- parseint(): parses given string as a representation of an int in specified base (e.g. base 2, 10, 16, etc) and returns result
    - e.g. `parseint("100", 10) == 100`: translate 100 in base 10
    - e.g. `parseint("FF", 16) == 255`: translate FF in hex to an int
    - e.g. `parseint("1011111011101111", 2) == 48879`: translate binary string
- pow(x,y): calculates an exponent by raising first argument to the power of the second argument
- signum(): determines sign of a number (e.g. negative, zero, positive) w -1, 0, or 1

## String Functions
- chomp("str"): removes newline characters at end of str
- format("str"): produces string by formatting a number of other values according to specification string
    - e.g. `format("There are %d lights", 4)` returns 'There are 4 lights'
- formatlist("str", list): produces a list of string by formatting other values according to spec string
    - e.g. `formatlist("Hello, %s!", ["Valentina", "Ander", "Olivia", "Sam"])` returns
            [
                "Hello, Valentina"
                "Hello, Ander"
                "Hello, Olivia"
                "Hello, Sam"
            ]
- indent("str"): adds a given number of spaces to beginning of all lines but the first in a multiline string
- join("<operator>", [list]): produces a string by concatenating all elements of a list of string w <operator>
- lower("str"): converts all cased letters in string to lowercase
- upper("str"): converts all cased letters in string to uppercase
- regex("str"): applies regex to a string & returns matching substrings
- regexall("str"): applies regex to a string & returns list of all matches
- replace("str"): replaces given string for another given substring & replaces each occurence w given replacement string
    - e.g `replace("hello world", "/w.*d/", "everybody)` returns `'hello everybody'`
- split("<separator>","string"): produces a list by dividing string with <separator>
- strrev("string"): reverses characters in a string
- substr("str",<offset>,<len>): extract a substring from string by offset & length
    - e.g. `subset("hello world", 1, 4)` returns `ello`
- title("str"): converts first letter in each word in string to uppercase
- trim("str", "<characters>"): removes specified characters from start & end of string
    - e.g. `trim("!?Hello?!", "!?")` returns `Hello`
- trimprefix("str", "<prefix>"): removes specified <prefix> from start of string
- trimsuffix("str", "<suffix>"): removes specified <suffix> from end of string
- trimspace("str"): removes whitespace from start & end of string

## Collection functions
- alltrue([<bool>, <bool>]): returns true if all elements in collection are `true` or `"true"`
- anytrue([<bool>, <bool>]): returns true if any element in collection are `true` or `"true"`
- chunklist([<list>], <chunk>): splits a single list into fixed-size chunks, returning a list of lists
    - e.g. `chunklist(["a", "b", "c", "d", "e"], 2)`
    [ 
        [
            "a",
            "b"
        ]
        ...
    ]
- coalesce(): takes any number of arguments and returns the first one that isn't null or an emptry string
    - e.g. `coalesce("","a","b")` returns `a`
- coalescelist([]): takes any number of list arguments and returns the first one that isn't empty 
- compact([]): takes a list of strings and returns a new list w empty string elements removed
- concat([],[]): takes two or more lists and combines them into a single list
- contains([],<value>): determines whether a given list or set contains a given single <value> as one of it's elements; returns `true` or `false`
- distinct([]): takes a list and returns a new list w any duplicate elements removed 
- element([],<int>): retrieves a single element from a list
    - e.g. `element(["a", "b", "c"], 3)` returns `a` - index value 3 doesn't exist, so it wrapped back around to the beginning
- index([],<value>): finds the element index for a given value in a list
    - e.g. `index(["a", "b", "c"], "b")` returns `1`
- flatten([],[]): takes a list and replaces any elements that are lists with a flattened sequence of the list contents (turns multiple lists into one list)
- keys({}): takes a map and returns a list containing the *keys* from that map
- values({}): takes a map and returns a list containing the *values* of the elements in the map
- length(<value>): determines the length of a given list, map, or string. List counts values within list, map counts number of key:value pairs, string counts number of characters 
- lookup({},<key>, <default-value>): retrieves the value of a single element from a map, given its <key>. If the given <key> does not exist, the given <default-value> is returned
    - e.g. `lookup({a="ay", b="bee"}, "a", "what?")` returns `ay`
    - e.g. `lookup({a="ay", b="bee"}, "c", "what?")` returns `what?`
- matchkeys([],[],[]): constructs a new list by taking a subset of elements from one list whose indexes match the corresponding indexes of values in another list
    - e.g. `matchkeys(["i-123","i-abc","i-def"], ["us-west", "us-east", "us-east"], ["us-east"])` returns `["i-abc", "i-def"]`
- merge({}, {}): takes an arbitrary number of maps or objects, and returns a single map or object that contains a merged set of elements from all arguments. For duplicates, seems to return the value of the last occurence
    - e.g. `merge({a="b", c="d"}, {e="f", c="z"})` returns `{"a" = "b", "c" = "z", "e" = "f"}
- one([]): takes a list, set, or tuple value w either zero or one elements. If collection is empty, one() returns null. Otherwise, one returns the first element. If there are two or more elements, then one will return an error 
- range(<int>): generates a list of numbers using a start value, a limit value, and a step value (not all required)
    - e.g. `range(3)` returns `[0,1,2]`
- reverse([]): takes a sequence and produces a new sequence of the same length with all of the same elements as the given sequence but in reverse order
    - e.g. `reverse([1,2,3])` returns `[3,2,1]`
- setintersection([],[],[]): takes multiple sets and produces a single set containing only the elements that all of the given sets have in common; computes the intersection of the sets 
    - e.g. `setintersection(["a", "b"], ["b", "c"], ["b", "d"])` returns `["b"]`
- setproduct([],[]): finds all possible combinations of elements from given sets by computing the Cartesian product
    - e.g. `setproduct(["development", "staging", "production"], ["app1", "app2"])` returns `[["development","app1"],["development", "app2"]...]`
- setsubtract([],[]): returns a new set containing the elements from the first set that are not present in the second set; computes the relative complement of the first set in the second set 
    - e.g. `setsubtract(["a", "b", "c"], ["a', "c"])` returns `["b"]`
- setunion([],[]): takes multiple sets and produces a single set containing the unique elements from all the given sets
    - e.g `setunion(["a", "b"], ["b", "c"], ["d"])` returns `["d","b","c","a"]`
- slice([],<int>,<int>): extracts some consecutive elements from w/n a list
    - e.g. `slice(["a", "b", "c", "d"], 1, 3)` returns `["b","c"]` 
- sort([]): takes a list of strings and returns a new list with those strings sorted lexicographically (accounts for longer strings and can compare to shorter strings. pretty complicated concept)
    - e.g. `sort(["e", "d", "a", "x"])` returns `["a","b","e","x"]`
- sum([]): takes a list or set of numbers and returns the sum of those numbers. Can be int or float
- transpose({}): takes a map of lists of strings and swaps the keys and values to produce a new map of lists and strings
    - e.g. `transpose({"a" = ["1", "2"], "b" = ["2", "3"]})` returns `{ "1" = ["a"], "2" = ["a", "b"]...}`
- zipmap([],[]): constructs a map from a list of keys and a corresponding list of values
    - e.g. `zipmap(["a", "b"], [1, 2])` returns `{"a" = 1, "b" = 2}`

## Encoding and Decoding Functions
- functions that will encode and decode for various formats 
- base64encode/decode
- textencodebase64/decode
- yamlencode/decode
- jsonencode/decode
- base64gzip
- urlencode: used for making URL links 
- csvdecode 

## Filesystem Functions
- abspath(): converts string containing filesystem path & converts to absolute path
    - e.g. `abspath(path.roo)` might return something like `/home/user/some/terraform/root`
- dirname(): takes string containing filesystem path & removes file name portion from it
- basename(): takes a string containing filesystem path & removes directory path 
- pathexpand(): expands path into an absolute. 
    - e.g., `pathexpand("~/.ssh/id_rsa")`, expands to include the specific name of the home dir 
- file(): reads contents of file at given path & returns as string
- fileexists(): determines file's existence
- fileset(): enumerates a set of regular file names given a path and pattern
    - e.g. `fileset(path.module, "files/*.txt")` returns `["files/hello.txt","files/world.txt",]`
- filebase64(): reads contents of file at given path & returns as base64-encoded string
- templatefile(): reads file at given path & uses it as a template using a supplied set of template vars
    - e.g., 
    ```
    backends.tpl: 
    %{ for addr in ip_addrs ~}
    backend ${addr}:${port}
    %{ endfor ~}
    ```
    `templatefile("${path.module}/backends.tpl, { port = 8080, ip_addrs = ["10.0.0.1","10.0.0.2"]})` 
    returns
    `backend 10.0.0.1:8080`
    `backend 10.0.0.2:8080`

## Date & Time Functions
- formatdate(time format, RFC 3339 time code): converts a timestamp into a different time format; variety of formats available
    - e.g., RFC 3339 format: `2019-10-12T07:20:50.52Z`
- timeadd(RFC 3339, <time to add><m/h/d>), time to add, amount of time; minutes/hours/days
- timestamp(), returns a UTC timestamp string in RFC 3339 format 

## Hash & Crypto Functions
- generates hashes and cryptographic strings
- bcrypt(<string>): hash cannot be reversed 
- bash64sh256, 512
- filebase64sha256, 512
- filemd5
- filesha1, 256, 512
- md5
- rsadecrypt
- sha1, 256, 512
- uuid, uuid v5

## IP Network Functions
- cidrhost(): calculates a full host IP address for a given host number w/n a given IP network address prefix 
    - e.g. `cidrhost("10.12.127.0/20", 268)` returns `10.12.113.12` - basically, split the given address into X parts, and return an IP address of one of those parts
- cidrnetmask(): converts an CIDR-formatted IPv4 address into subnet mask address
    - e.g. `cidrnetmask("172.16.0.0/12")` returns `255.240.0.0`
- cidrsubnet(<address>, <network-segments>, <hosts>): calculates a subnet address w/n given IP network address prefix 
    - e.g. `cidrsubnet('172.16.0.0/12, 4, 2)` returns `182.18.0.0/16`
- cidrsubnets(): calculates a sequence of consecutive IP address ranges w/n define CIDR prefix
    - e.g. `cidrsubnets('10.1.0.0/16, 4, 4, 8, 4)` returns `['10.1.0.0/20','10.1.16.0/20','10.1.32.0/24','10.1.48.0/20]`

## Type Conversion Functions 
- can(): evaluates a given expression & returns boolean indicating whether expression produced a result w/o errors
- defaults(): used w input variables w type contrains of object types or collections of object types that include optional attributes
- nonsensitive(): takes a sensitive value & returns a copy of that value w the sensitive marked removed
- sensitive(): takes any values & returns a copy of it marked so tf will treat as sensitive (same meaning & behavior as for sensitive input variables)
- tobool(): converts its argument to a boolean value
- tomap(): converts its argument to a map value
- toset(): converts its argument to a set value (set: all same type)(unlikely to come across)
- tolist(): converts its argument to a list value (list: all different types allowed)
- tonumber(): converts argument to int
- tostring(): converts argument to a set string value
- try(): evaluates all its argument expressions in turn & returns the result of the first one that does not produce any errors 

# Terraform Cloud
- app that helps teams use tf together 
- available as hosted service at app.terraform.io
- features
    - manage state files
    - history of previous runs
    - history of previous states
    - easy & secure variable injection
    - tagging
    - run ttriggers 
    - specify any version of tf per workspace
    - global state sharing
    - commenting on runs
    - notifications via webhooks, email, slack
    - organization and workspace level permissions (requires paid access to manage)
    - policy as code (via sentinel policy sets)
    - MFA
    - SSO (at business tier)
    - cost estimation (at teams & governance tier)
    - integrations w ServiceNow, splunk, k8s, custom run tasks 
- terminology
    - organization: collection of workspaces
    - workspaces: represents unique environment or stack
    - teams: composed of multiple members & can be assigned to (a) workspace(s)
    - runs: single run of the tf run environment that is operating an execution plan
        - UI, API, or CLI driven
- run workflows
    - version control workflow
        - UI/VCS driven (user interface & version control system)
        - integrated w specific branch in VCS
        - plans generated when pull requests submitted
        - run triggered when merge occurs to branch
    - CLI-driven workflow
        - runs triggered by user running tf CLI commands locally on personal machine
    - API-driven workflow   
        - not directly associated w VCS
        - third-party tool/system triggers runs via config file using tf cloud API
            - config file is bash scripted packaged in archive (.tar.gz)
            - pushing a 'configuration version'
- organization-level permissions 
    - manage resources or settings across organization
    - manage policies: manage org's Sentinel policies
    - manage policy overrides: override soft-mandatory policy checks
    - manage workspaces: create + administer workspaces
    - manage VCS settings: manage VCS providers & SSH keys w/n org
    - organization owners
        - at least one, can have more
        - has every available perm + owner-only
        - owner-only permissions 
            - publish private modules
            - invite users to org
            - manage team membership
            - view secret teams
            - manage org permissions
            - manage all org settings
            - manage org billing
            - delete org
            - manage agent 
- workspace-level permissions 
    - manage resource & settings for specific workspace
    - general workspace permissions
        - granual workspace permissions
        - applied to user via custom workspace perms
            - read runs
            - queue plans
            - apply runs
            - lock + unlock workspaces
            - download sentinel mocks
            - read variable
            - read + write variables
            - read state outputs
            - read state versions
            - read + write state versions 
    - fixed permission sets
        - premade permissions for quick assignment 
            - read
                - read runs
                - read variables
                - read state versions
            - plan
                - queue plans
                - read variables
                - read state versions
            - write
                - apply runs
                - lock + unlock workspaces
                - download sentinel mocks
                - read + write variables
                - read + write state versions 
    - workspace admin
        - role that grants all level of perms and some workspace-admin-only perms:
            - read + write workspace settings
            - set or remove workspace perms of any team
            - delete workspace
- API tokens
    - supports three types: user, team, organization tokens
    - organization API tokens
        - have perms across entire org
        - each org can have one valid API token
        - use when setting up org for first time programmitically; not for general-purpose use
    - team API tokens 
        - allow access to the workspaces that team has access to - not tied to specific user
            - has same access level to workspaces the team has access to 
        - each team can have one valid API token at a time
        - any team member can generate or revoke their team's token
            - when new is generated, old immediately becomes invalid
        - meant for performing API operations on workspaces
    - user API tokens
        - flexible b/c they inherit perms from user they're associate w
        - can be used for real user or service acct 
- API tokens access levels 
    - terraform.io/docs/cloud/users-teams-organizations/api-tokens.html
- Private registry
    - publish private modules for org w/n private registry
    - helps share tf modules across org
        - supports:
            - module versioning
            - searchable + filterable list of available modules
            - config designer
        - all users in org can view private module registry
    - authentication
        - user token or team token for authentication
        - use `terraform login` to obtain user token
        - to use team token, must be set in tf CLI config file
- cost estimation (teams + governance plan & above)
    - provides monthly cost of resources displayed alongside tf runs
    - only available for specific cloud resources w/n AWS, Azure, and GCP
        - ~15 services in AWS, ~20 services in Azure, 3 services in GCP
    - can use sentinel policy to force runs to be under a particular cost 
- workflow options
    - choose any version of tf for a workspace 
    - share state globally across org
    - can choose to auto approve runs 
- migrating default local state
    - to migrate tf project that only uses default workspace
        - create workspace in tf cloud
        - replace tf config w remote backend
        - run `terraform init` and copy existing state by typing `yes`
- VCS integration
    - github, github (oauth), github enterprise, gitlab, gitlab EE/CE, butbucket cloud, bitbucket server & data center, azure devops service, azure devops server 
- run environment
    - when tf cloud executes `terraform plan` it runs them in its own Run Environment
    - single-use linux machine running on x86_64 arch & details of internal implementation not know
    - automatically-injected env vars
        - TFC_RUN_ID
        - TFC_WORKSPACE_NAME
        - TFC_WORKSPACE_SLUG
        - TFC_CONFIGURATION_VERSION_GIT_BRANCH
        - TFC_CONFIGURATION_VERSION_GIT_COMMIT_SHA
        - TFC_CONFIGURATION_VERSION_GIT_TAG
        - can be accessed by defining `variable TFC_RUN_ID {}`
- terraform cloud agents (paid feature of business plan)
    - communicate w isolated, private, or on-prem infrastructure
    - agent arch is pull-based; no inbound connectivity required
        - provisioned agents will poll tf cloud for work & execute that work locally
        - supports only x86_64 linux OS
        - can run agent w/n docker using tf agent docker container
        - support tf version 0.12+
        - requires 4GB free disk space (for temp local copies) and 2 GB memory
        - needs ability to make outbound requests on 443 to:
            - app.terraform.io
            - registry.terraform.io
            - releases.hashicorp.com
            - archivist.terraform.io

# Terraform Enterprise
- self-hosted distribution of tf platform
- benefits
    - no resource limits
    - add'l enterprise-grade architectural features
        - audit logging
        - SAML SSO
- requirements
    - operational mode: how data should be stored 
        - external services
            - postgres
            - cloud blob storage (S3, etc) - not part of the server
        - mounted disk
            - persistent disk mounted to VM
            - postgres
        - demo
            - all data stored on instance, using ephemeral data stores - not recommended for prod use
    - credentials
        - tf enterprise license from hashicorp
        - TLS cert + private key - must prove own TLS cert
    - linux instance
        - debian, ubuntu, RHEL, centos, Amazon linux, oracle linux 
        - hardware requirements
            - 10GB+ disk space on root
            - 40GB+ disk space for docker data dir (default /var/lib/docker)
            - 8GB+ system memory
            - 4+ CPU cores  
- air-gapped environments
    - network security measure to ensure computer network physically isolated from unsecure networks
    - supported by the 'air gap bundle' from hashicorp
- tf cloud features and pricing 
    - Open-Source Software (OSS)
        - IaC, workspaces, variables, runs, resource graph, providers, modules, public module registry
    - Cloud - as the list goes down, the one beneath it has all the things listed above plus the new listing 
        - Free
            - remote state, VCS connection, workspace mgmt, secure var storage, remote runs, private module registry
            - 1 current run
            - $0 up to 5 users
        - Teams
            - team management, cost estimation
            - 2 current runs 
            - $20/user/mo
        - Teams & Governance
            - sentinel policy as code management
            - $70/user/mo
        - Business
            - SSO, audit logging
            - self-hosted agents
            - config designer, servicenow integration
            - unlimited current runs 
            - cost: contact sales
    - Self-hosted
        - enterprise
            - all of the above, although no self-hosted agents 
            - cost: contact sales

# Workspaces 
- manage multiple environments or alternate state files
    - think of them like different branches in git repository
    - workspaces are technically equivalent to renaming state file
- variants
    - CLI workspaces
        - a way of managing alternate state files (locally or via remote backends)
    - tf cloud workspaces 
        - act like completely separate working directories
- by default, there is a single workspace in local backend called default
- internals
    - local state
        - tf stores workspace states in terraform.tfstate.d dir
        - small teams may commit to repos, not best practice
    - remote state
        - workspace files stored directly in backend
- current workspace interpolation
    - reference current workspace name via `terraform.workspace` 
- multiple workspaces
    - tf config has backend that defines how operations are executed & where persistent data (e.g. tf state) is stored 
    - supported by the following backend
        - AzureRM, Consul, COS, GCS, k8s, local, anta, Postgres, Remote, S3
    - certain backends support multiple workspaces
        - allows multiple states to be associated w a single config
- tf cloud workspaces 
    - have to create an organization, then can create workspaces 
    - can see a history of previously held states (aka snapshots)
- tf cloud run triggers
    - connect local workspace to one or more workspaces in tf cloud
    - allows runs to queue automatically in workspace upon successful apply of runs in any of the source workspaces
        - can connect each workspace with up to 20 source workspaces
    - designed for workspaces that rely on info or infra produced by other workspaces
    - if tf config uses data sources to read values that might be changed by other workspaces, run triggers allow explicitly specify external dependency 
        - 'if this workspace runs successfully, then run this other workspace'
- CLI commands
    - only affects local workspaces 
    - `terraform workspace list`: list all existing workspaces
        - current workspace indicated w `*`
    - `terraform workspace show`: show current workspace
    - `terraform workspace select <name>`: switch to target workspace
    - `terraform workspace new <name>`: create and switch to workspace
    - `terraform workspace delete <name>`: delete target workspace 
- differences
    - local
        - tf config stored on disk
        - variables: as .tfvars files, cli arguments, or via shell
        - state: store on disk or in remote backend
        - credentials & secrets entered in shell env or entered at prompts  
    - cloud
        - tf config in VCS or uploaded via CLI
        - variables: set in tf cloud workspace
        - state: stored in tf cloud workspace
        - credentials & secrets stored as sensitive variables

# Sentinel
- embedded policy-as-code framework integrated w tf platform
    - code written to automate regulatory or governance policies
- features
    - embedded
    - fine-grained, condition-based policy
    - multiple enforcement levels
    - external information
    - multi-cloud compatible
- paid service part of Team & Governance upgrade package
- benefits of policy as code
    - sandboxing: able to create guardrails
    - codification
    - version control
    - testing: syntax & behavior can easily be validated
    - automation
- language: all policies written using sentinel language; designed to be non-programmer and programmer friendly
- development: provides CLI for dev & testing
- testing: provides test framework designed for automation
- lots of policy examples for various providers provided by terraform
- have to import policy language functions in main.tf file 
- can be integrated w tf via tf cloud as part of IaC pipeline b/w plan & apply stages 

# Packer
- developer tool to provision build image that will be stored in repo 
- using a build image before deploying provides
    - immutable infrastructure
    - VMs in fleet are all one-to-one in config
    - faster deploys for multiple servers after each built
    - earlier detection and intervention of package changes or depreciation of old technology
- configures machine or container via packer template, using HCL
- template file
    - source - required, e.g. EBS-backed AMI; stored in AWS under EC2 images
    - build: allows config scripts
        - wide range of provisioners supported: chef, puppet, ansible, powershell, bash, salt
    - post-provisioners: run after image is built
        - can be used to upload artificates or re-package 
- integrating w tf
    - two steps
        - build image; packer is not a service, but a development tool; must manually run packer or automate image building w build server running packer 
        - referencing image: once image is built, can be referenced as data source 
            - for AWS AMI, can match on regex & select most recent 

# Consul
- service networking platform
    - useful w micro-service or service-oriented architecture w 100s-1000s of services 
    - provides
        - service discovery - central registry for service in network
            - allows for direct communication w no SPOF via load balancers
        - service mesh - managing network traffic b/w services
            - 'middleware'-type communication layer on top of container apps
        - app config capabilities 
- integrations w tf
    - remote backend
        - consul has key value (KV) store for config storage
    - consul provider

# Hashicorp Vault
- for securely accessing secrets from multiple secrets data stores
- provides unified interface
    - to any secrets
        - includes AWS secrets, consul key value, Google Cloud KMS, etc
    - provide tight access control
        - Just-in-Time (JIT): reduce attack surface based on range of time
        - Just enough Privilege (JeP): reducing attack surface by providing least-permissive permissions
    - records detailed audit log for tamper evidence 
- deployed to VMs in a cluster 
- integration w tf
    - when devs need credentials, e.g. aws credentials, instead of local storage, using JIT credentials injected at the time of `terraform apply` using data sources 
    - injection via data source
        - vault service provisioned
        - vault engine config'd - e.g. AWS secrets engine
        - vault creates a machine user for AWS
        - vault will generate short-lived AWS credentials from machine user
            - new credentials supplied every time `terraform apply` is ran
        - vault will manage & apply AWS policy
        e.g.
        ```
        data "vault_aws_access_credentials" "creds" {
            backend     = data.terraform_remote_state.admin.outputs.backend
            role        = data.terraform_remote_state.admin.outputs.role
        }

        provider "aws" {
            region      = var.region
            access_key  = data.vault_aws_access_credentials.creds.access_key
            secret_key  = data.vault_aws_access_credentials.creds.secret_key
        }
        ```
- tf cloud uses vault behind the scenes, and not bespoke like the comments above 

# Atlantis
- open-source developer tool to automate tf pull requests
- helps automate infrastructure-as-code
- creators of Atlantis now work at HashiCorp & maintains the project, which is something of an alternative to tf cloud

# CDK for tf
- AWS Cloud Development Kit (CDK) imperative IaC tool
    - only intended for AWS cloud; generates CloudFormation templates
- CDK for Terraform is standalone project by HashiCorp that allows use of CDK, and instead of CFN, it creates tf templates
    - allows use of CDK tooling to define IaC resources for any provider

# Gruntwork
- software company that builds DevOps tools that extend/leverages tf
- IaC library: 300k+ lines of reusable, tested IaC code for various tf providers
- terragrunt: thin wrapper that provides extra tools for keeping configs dry (don't repeat yourself), working w multiple tf modules & managing remote state
    - Don't-Repeat-Yourself: programming methodology to abstract repeated code into function, modules, or libraries (often in isolate files) to reduce code complexity effort & errors 
- terratest: testing framework for infrastructure provisioned w tf
    - perform unit test & integration tests on infro
    - test infrastructure by temporarily deploying it, validating results, and tearing down test env 
    - written in GoLang 
- gruntwork landing zone for AWS: collection of baselines for multi-account security on AWS
- gruntwork pipelines: security-first approach to CI/CD pipeline for infrastructure
- gruntwork reference architecture: opinionated, tested, best-practices way to assembly code from the IaC library 
    - paid service 

# Testing in Terraform
- e2e tests > integration tests > unit tests > static analysis (> actually meant to indicate 'greater than')
    - static analysis
        - test code w/o deploying
        - tflint, terraform validate, terraform pan, terraform-compliance, sentinel
    - unit tests
        - testing a single module (need to divide modules into small units of work)
        - terratest, kitchen-terraform, inspec
    - integration tests
        - test multiple IaC modules working together
        - terratest
    - e2e
        - must setup persistent test env
        - gruntwork reference architecture 


# Bhargav Bachina 250 Terraform Questions Review
- `terraform fmt` only works on .tf and .tfvars files
- `terraform show` shows current state of applied infrastructure by reading from terraform.tfstate
- `terraform state list` list all resources from state 
- `terraform state show <resource>` list information about specific resource
- 'resource spec' is essentially the name of the resource defined in tf; e.g. it refers to `<resource_type>.<resource_name>[<resource_index]`