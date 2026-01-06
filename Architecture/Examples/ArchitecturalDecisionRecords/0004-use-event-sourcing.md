# 4. Use Event Sourcing

Date: 2022-11-23

## Status

Accepted

## Context

Traceability (when and who) of changes in entities is crucial. Lots of questions could be answered if this information
were available. Only persisting the current state makes this cumbersome, as changes need to be recorded separately.
Event sourcing is the ideal solution for this, as every change is persisted.

## Decision

The backend will be implemented using event sourcing. Events are recorded in a database and on each new event the
current state is updated accordingly.

## Consequences

We make the foundation to display all changes to the users or the ability to bring the entities into a state in the
past. Downsides are increased complexity and the need for a custom backend.