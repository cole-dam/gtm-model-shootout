# Does Jev know when it's wrong?

Each answer's confidence is the lower of its department and seniority confidence.

## Jev (title only)

- **Accuracy:** 19/26
- **Average confidence when right:** 0.88
- **Average confidence when wrong:** 0.80

### If you auto-accepted answers above a confidence threshold

| Threshold | Auto-accepted | Accuracy of auto-accepted | Sent to a human |
|---|---|---|---|
| 0.50 | 23/26 | 17/23 (74%) | 3 |
| 0.70 | 21/26 | 16/21 (76%) | 5 |
| 0.80 | 19/26 | 15/19 (79%) | 7 |
| 0.90 | 18/26 | 14/18 (78%) | 8 |
| 0.95 | 17/26 | 13/17 (76%) | 9 |

### Misses, most confident first

- Lifecycle Marketing Manager (confidence 1.00) → seniority: got "Manager", wanted "IC"
- Demand Gen Manager (confidence 1.00) → seniority: got "Manager", wanted "IC"
- Customer Success Manager (confidence 0.97) → seniority: got "Manager", wanted "IC"
- Marketing Ops Team Lead (confidence 0.97) → function: got "Marketing", wanted "Operations"
- RevOps Manager (confidence 0.71) → seniority: got "Manager", wanted "IC"
- Chief Revenue Officer (confidence 0.54) → function: got "Executive", wanted "Sales"
- Product Manager II (confidence 0.44) → seniority: got "Manager", wanted "IC"

## Jev (with rules)

- **Accuracy:** 26/26
- **Average confidence when right:** 0.88
- **Average confidence when wrong:** n/a

### If you auto-accepted answers above a confidence threshold

| Threshold | Auto-accepted | Accuracy of auto-accepted | Sent to a human |
|---|---|---|---|
| 0.50 | 23/26 | 23/23 (100%) | 3 |
| 0.70 | 22/26 | 22/22 (100%) | 4 |
| 0.80 | 21/26 | 21/21 (100%) | 5 |
| 0.90 | 19/26 | 19/19 (100%) | 7 |
| 0.95 | 18/26 | 18/18 (100%) | 8 |

### Misses, most confident first

- None 🎯

## How to read this
- **Good sign:** confidence is clearly lower when Jev is wrong. Then you can auto-accept the sure answers and route the rest to a person.
- **Bad sign:** a confident miss. That's an error your process would wave straight through.
