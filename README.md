EECS4312 Winter26:Lab3

# Name: Mohsen Maoodhah
# Student number: 220153425
# Title: FROM ELICITATION TO CONSTRAINTS, INVARIANTS, AND TESTS

# Medication Dispensing System Documentation

## System Description

The system is a **medication dispensing system** for a pharmacy. Its primary function is to **record each dispensing event**, capturing:

* `patient_id` (who receives the medication)
* `medication` (what is dispensed)
* `dose_mg` (amount per dose)
* `quantity` (number of doses dispensed)

The system operates under **safety, consistency, and policy rules**, ensuring no overdosing or duplicate dispensing occurs within a single day.

---

## Identified Constraints and Invariants

### Constraints (checked during dispensing)

1. `dose_mg` must be **positive**.
2. `quantity` must be a **positive integer**.
3. `dose_mg` must not exceed the **maximum daily dose** for the medication.

### Invariants (system-wide rules that must always hold)

1. A patient may **not receive the same medication more than once per day**.
2. All doses are expressed in **milligrams** (standardized units).

### Functional Requirements

* Record dispensing events.
* Track patient-medication associations.
* Automatically enforce constraints and invariants.

---

## Mapping Tests to Requirements

| Test Case                   | Requirement Validated                                    | Description                                                                                     |
| --------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Test negative or zero dose  | Constraint: dose must be positive                        | Attempt to create a `DispenseEvent` with `dose_mg ≤ 0` → should be rejected                     |
| Test quantity validity      | Constraint: quantity must be positive integer            | Attempt to create a `DispenseEvent` with `quantity ≤ 0` → should be rejected                    |
| Test duplicate dispensing   | Invariant: same medication cannot be dispensed twice/day | Attempt to add a second event for the same patient and medication on the same day → should fail |
| Test exceeding maximum dose | Constraint: max daily dose                               | Attempt to dispense a dose exceeding max daily limit → should be rejected                       |

---

This document links **system rules → constraints/invariants → requirement-driven tests**, ensuring each requirement is directly validated through testing.
