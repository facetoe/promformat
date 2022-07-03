# Promformat

Promformat is a PromQL formatter written in Python. It works by building an AST from the CST provided by ANTLR4, and then using that to produce formatted code.

The result should be semantically identical to the unformatted version as promval compares the parse tree of the original and formatted expression and fails if they are not identical.

# Usage

From command line:
```text
# Format a file containing PromQL
promformat <path to file>

# No arguments enters interpreter
promformat
```

As library:
```text
from promformat import format_query
print(format_query("1+1")
```

# Example

Given the PromQL:

```
job:request_latency_seconds:mean5m{job="myjob"} > 0.5
```

it will be formatted:

```
job:request_latency_seconds:mean5m
{
  job="myjob",
}
> 0.5
```

A more complex example:
```text
count by (namespace)(sum by (namespace,pod,container)(kube_pod_container_info{container!=""}) unless sum by (namespace,pod,container)(kube_pod_container_resource_limits{resource="cpu"}))
```

```text
count by (
  namespace,
)
(
  sum by (
    namespace,
    pod,
    container,
  )
  (
    kube_pod_container_info
    {
      container!="",
    }
  )
  unless
  sum by (
    namespace,
    pod,
    container,
  )
  (
    kube_pod_container_resource_limits
    {
      resource="cpu",
    }
  )
)
```