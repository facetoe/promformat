# Promformat

Promformat is a PromQL formatter written in Python. It works by building an AST from the CST provided by ANTLR4, and then using that to produce formatted code.

The result should be semantically identical to the unformatted version as promval compares the parse tree of the original and formatted expression and fails if they are not identical.

### Example

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