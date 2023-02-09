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