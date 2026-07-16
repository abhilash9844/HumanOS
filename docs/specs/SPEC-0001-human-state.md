# SPEC-0001 — Human State

**Status:** Draft

**Version:** 0.1

**Author:** Abhilash Anand Y

**Last Updated:** 16 July 2026

---

# Purpose

This specification defines the computational representation of a human within HumanOS.

Every simulation operates on a Human State.

The Human State contains only the minimum set of variables required to simulate learning strategies.

This specification intentionally separates the human's internal state from the policies that decide actions.

---

# Design Principles

The Human State must be:

- Minimal
- Explainable
- Extensible
- Measurable
- Independent of implementation

If a variable is not essential, it does not belong in the Human State.

---

# Core State Variables

## 1. Knowledge

### Definition

The amount of information and concepts a person has learned.

### Represents

- Facts
- Concepts
- Theory
- Understanding

### Does NOT Represent

- Ability to apply knowledge
- Speed
- Experience

---

## 2. Skill

### Definition

The ability to apply knowledge to accomplish a task.

### Represents

- Problem solving
- Programming ability
- Mathematical ability
- Practical execution

### Does NOT Represent

- Memory
- Intelligence
- Motivation

---

## 3. Energy

### Definition

The current capacity available for productive work.

### Represents

- Mental freshness
- Physical readiness

### Changes Due To

- Sleep
- Rest
- Work

---

## 4. Fatigue

### Definition

Accumulated mental and physical exhaustion.

### Represents

The cost paid for sustained effort.

### Increases With

- Deep work
- Long work sessions
- Poor sleep

### Decreases With

- Sleep
- Recovery
- Breaks

---

# Why Only Four Variables?

HumanOS follows the principle of the Minimum Scientific Core.

Adding more variables increases complexity.

Every additional variable must provide enough explanatory power to justify its maintenance cost.

Version 0.1 intentionally remains minimal.

---

# Variables Not Included

The following are intentionally excluded from Version 0.1.

- Motivation
- Intelligence
- IQ
- Personality
- Emotion
- Happiness
- Dopamine
- Hormones
- Attention
- Stress

These may be introduced in future versions if supported by evidence and justified by the simulation.

---

# Separation of Concerns

Human State answers:

> "What is the current condition of the person?"

Policies answer:

> "What action should the person take next?"

The Human State never decides actions.

Policies never directly store state.

---

# Future Extensions

Future versions may introduce optional state variables through the plugin system while maintaining backward compatibility.

---

# Version History

## Version 0.1

- Initial Human State specification.
- Four-variable minimum scientific core.