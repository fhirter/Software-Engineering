# 7. There Can Only Be One Board at a Time

Date: 2023-03-17

## Status

Superceded by [21. use only one board](0021-use-only-one-board.md)

## Context

The business is very fast-paced and most orders are completed within a few hours. Orders that span multiple days are
rare and are, from a business perspective, two separate shipments, one from the pickup location to the overnight
location, another from the overnight location to the delivery location.

Shipments any shipments not happening on the current day are mostly irrelevant form the dispatch perspective.
Therefore, the board, that is the dispatchers most important tool, should only show shipments of the current day.

To avoid confusion there should not multiple boards for any given day.

## Decision

Boards can only contain shipments of the same day.

There should only be one shipment per day.

## Consequences

These rules need to be enforced in the board. It should be very clear, which day the current board belongs to.

For the event replay it will be easier, because the events being replayed can be limited quite easily.
