# 8. A Shipment Must Be Completed During One Day

Date: 2023-03-17

## Status

Superceded by [21. use only one board](0021-use-only-one-board.md)

## Context

This is a follow up of the previous adr and a logical consequence.

## Decision

A shipment cannot span multiple days.

## Consequences

Shipments should enforce that from and to date-times are on the same day.
