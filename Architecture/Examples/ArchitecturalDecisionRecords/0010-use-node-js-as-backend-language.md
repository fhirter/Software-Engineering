# 10. Use Node.js as Backend Language

Date: 2023-06-13

## Status

Accepted

Supercedes [3. Use Go as Backend Language](0003-use-go-as-backend-language.md)

## Context

Working with Go was more challenging than expected and hindering the progress of the product.
Because big parts of the code base are in JavaScript it makes a lot of sense to also build the backend with JavaScript, because a lot of the code can be reused thanks to the modular architecture.

The performance gain of Go seems not remotely worth the overhead.

## Decision

We switch the backend language from go to JavaScript with Node.js.

## Consequences

Development on the backend will be way faster.