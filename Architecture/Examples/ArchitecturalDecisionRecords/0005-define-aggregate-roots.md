# 5. define aggregate roots

Date: 2022-12-30

## Status

Accepted

## Context

Following the principles of domain driven design [aggregates](https://martinfowler.com/bliki/DDD_Aggregate.html) group
entities together. Access to the grouped entities should only be through the aggregate root.

## Decision

Two aggregates are being identified:

- Board
    - Rows
    - Lanes
- Shipment
    - Parcels
    - Stops
    - Tags

Board and Shipment are the aggregate roots.

Addresses don't belong to the shipment aggregate because they are also used elsewhere.

## Consequences

Access to `row` and `lane` objects is only through `board` objects. No other entities should hold references to
`lane` and `row` objects. The same applies to `shipment`.