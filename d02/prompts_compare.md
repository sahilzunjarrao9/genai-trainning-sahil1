# DAY 2 — Task 2.1: Bad Prompt vs. Good Prompt

## Complaint

I visited your MG Road branch on Tuesday to update my mobile number,
waited 45 minutes, was told the system was down, came again Thursday
and was told I need a form nobody gave me. Meanwhile my UPI is failing
since the 3rd and I have an EMI due on the 10th. This is my third
complaint. Ref CMP-88213.

---

## Prompt A — Simple Prompt

### Prompt

Summarize this email.

### Output

The customer visited the MG Road branch twice to update their mobile
number but faced a system outage and was not given the required form.
Their UPI has also been failing since the 3rd, they have an EMI due
on the 10th, and this is their third complaint. The complaint reference
is CMP-88213.

---

## Prompt B — Structured Prompt

### Prompt

You are a complaints triage assistant for a bank.

Analyze the following customer complaint.

Return exactly three fields:

- issue
- severity: low|medium|high
- requested_action

Rules:

- Only use information from the email.
- Do not invent details.
- Severity must be exactly one of: low, medium, high.

### Output

issue: Difficulty updating mobile number and UPI failures

severity: high

requested_action: Resolve the mobile number update issue and restore
UPI functionality.

---

## Observation

The simple prompt produces a general summary without a fixed structure.

The structured prompt produces specific fields for the issue, severity,
and requested action.

This makes the output more consistent and easier for a banking
application to process programmatically.

## Conclusion

Adding role, output structure, and constraints makes the model's response
more predictable and useful for an enterprise banking application.
