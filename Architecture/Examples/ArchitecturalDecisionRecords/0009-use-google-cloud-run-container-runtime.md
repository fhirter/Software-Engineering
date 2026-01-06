# 9. Use Google Cloud Run Container Runtime

Date: 2023-06-13

## Status

proposed

Superceded by [13. Use Cloud Functions For Backend](0013-use-cloud-functions-for-backend.md)

## Context

Starting development on the backend we need to choose a platform on which to run the application.
The choice is between Container based and Function as a Service.
Both have trade-offs and at the time of writing there is no clear winner.

As a first try we opt for containers because it makes development, especially testing, easier and the choice of platform more flexible.
Having simple backup systems running with limited capabilities or on different providers seems easier.

## Decision

We choose Google Cloud with Cloud Run as a provider over other cloud vendors, as there is experience with their tooling.

## Consequences

Maintaining Container Images is the trade-off of this decision. 
We might switch to a FaaS offering later to get rid of this if it seems beneficial.
