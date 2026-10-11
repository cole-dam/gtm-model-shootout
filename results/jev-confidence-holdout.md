# Does Jev know when it's wrong?

Each answer's confidence is the lower of its department and seniority confidence.

## Jev (title only)

- **Accuracy:** 16/25
- **Average confidence when right:** 0.94
- **Average confidence when wrong:** 0.94

### If you auto-accepted answers above a confidence threshold

| Threshold | Auto-accepted | Accuracy of auto-accepted | Sent to a human |
|---|---|---|---|
| 0.50 | 25/25 | 16/25 (64%) | 0 |
| 0.70 | 24/25 | 15/24 (62%) | 1 |
| 0.80 | 23/25 | 14/23 (61%) | 2 |
| 0.90 | 19/25 | 13/19 (68%) | 6 |
| 0.95 | 18/25 | 12/18 (67%) | 7 |

### Misses, most confident first

- Content Marketing Manager (confidence 1.00) → seniority: got "Manager", wanted "IC"
- Partner Marketing Manager (confidence 1.00) → seniority: got "Manager", wanted "IC"
- Customer Onboarding Manager (confidence 1.00) → seniority: got "Manager", wanted "IC"
- Product Marketing Manager (confidence 0.99) → seniority: got "Manager", wanted "IC"
- Marketing Operations Specialist (confidence 0.99) → function: got "Marketing", wanted "Operations"
- Key Account Manager (confidence 0.97) → seniority: got "Manager", wanted "IC"
- Director of Sales Operations (confidence 0.86) → function: got "Sales", wanted "Operations"
- Senior Product Manager (confidence 0.85) → seniority: got "Manager", wanted "IC"
- Sales Operations Manager (confidence 0.83) → function: got "Sales", wanted "Operations"; seniority: got "Manager", wanted "IC"

## Jev (with rules)

- **Accuracy:** 24/25
- **Average confidence when right:** 0.92
- **Average confidence when wrong:** 0.45

### If you auto-accepted answers above a confidence threshold

| Threshold | Auto-accepted | Accuracy of auto-accepted | Sent to a human |
|---|---|---|---|
| 0.50 | 24/25 | 24/24 (100%) | 1 |
| 0.70 | 21/25 | 21/21 (100%) | 4 |
| 0.80 | 21/25 | 21/21 (100%) | 4 |
| 0.90 | 19/25 | 19/19 (100%) | 6 |
| 0.95 | 17/25 | 17/17 (100%) | 8 |

### Misses, most confident first

- Sales Operations Manager (confidence 0.45) → seniority: got "Manager", wanted "IC"

## How to read this
- **Good sign:** confidence is clearly lower when Jev is wrong. Then you can auto-accept the sure answers and route the rest to a person.
- **Bad sign:** a confident miss. That's an error your process would wave straight through.
