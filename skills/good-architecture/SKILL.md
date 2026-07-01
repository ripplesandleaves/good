---
name: good-architecture
description: Use when designing systems, choosing component boundaries, deciding dependency direction, or evaluating whether a system structure is sound
---

# Good Architecture

## Core Principle

**Architecture is about what's hard to change.** Make the right things easy to change, and the wrong things hard to do by accident.

## System Decomposition

Split systems by **responsibility**, not by technical layer.

- Each component answers clearly: what does it do, how do you use it, what does it depend on?
- Components communicate through **well-defined interfaces** — change the internals without breaking consumers
- **Bounded contexts:** name things consistently within a boundary; translate explicitly at boundaries
- Prefer many small components over few large ones — large components are a signal of mixed concerns

**Monolith vs services:** Start with a monolith. Extract services when you have clear, stable boundaries AND a real operational reason (scale, deployment independence, team autonomy). Never as the first move.

## Dependency Direction

```
UI → Application → Domain ← Infrastructure
```

- Domain (core business logic) depends on nothing external
- Application orchestrates; domain decides
- Infrastructure (DB, HTTP, queues) implements interfaces defined by the domain
- Dependencies point inward, never outward

**The test:** can you run domain logic tests with no database, no HTTP, no filesystem? If not, the boundaries are wrong.

## Data Flow & State

- Prefer **immutable data** flowing through the system over shared mutable state
- Locate state as close to where it's used as possible
- Avoid global state; make dependencies explicit
- One source of truth per piece of data — duplication creates sync bugs

## Key Decisions (When Architecture Matters Most)

| Decision | Ask first |
|----------|-----------|
| Adding a service | Do we have a stable boundary AND operational need? |
| Shared database | Can we afford tight coupling between these components? |
| New abstraction | Does this reduce complexity or just add indirection? |
| Caching layer | Have we profiled? Is the source of truth still authoritative? |

## Red Flags
- Circular dependencies between components
- Components that know too much about each other's internals
- "God object" — one class/module that does everything
- Database as integration point between services
- Architecture chosen for résumé, not requirements
