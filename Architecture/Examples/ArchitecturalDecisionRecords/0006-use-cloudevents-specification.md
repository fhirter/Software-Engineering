# 6. use cloudevents specification

Date: 2023-02-24

## Status

Accepted

## Context

Unlike REST APIs there are few resources on how to structure events. 

Cloudevents.io seems to be the exact solution we are looking for.

## Decision

We use the [structure](https://github.com/cloudevents/spec) proposed by [cloudevents.io](https://cloudevents.io/) for our events.

## Consequences

We adhere to a common specification and might use some libraries for creating or receiving events. 
We can profit from the thoughts other have made about this topic.