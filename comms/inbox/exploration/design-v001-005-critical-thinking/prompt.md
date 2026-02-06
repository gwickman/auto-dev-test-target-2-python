You are executing Task 005: Critical Thinking and Risk Investigation for auto-dev-test-target-2-python version v001.

Read AGENTS.md first and follow all instructions there.

## Objective

Review the logical design from Task 004, investigate all identified risks and unknowns, and produce a refined design with mitigations.

## Context

This is Phase 2 (Logical Design & Critical Thinking) for auto-dev-test-target-2-python version v001.

Task 004 produced a logical design with a "Risks and Unknowns" section. This task investigates each risk, resolves unknowns where possible, and produces an updated design.

**IMPORTANT:** Build EXCLUSIVELY on Task 004's output and the existing design artifact store (001-003). Do NOT re-gather environment context or duplicate work from Tasks 001-003.

## Tasks

### 1. Read the Logical Design

Read from the design artifact store:
- `comms/outbox/versions/design/v001/004-logical-design/logical-design.md`
- `comms/outbox/versions/design/v001/004-logical-design/risks-and-unknowns.md`
- `comms/outbox/versions/design/v001/004-logical-design/test-strategy.md`

### 2. Triage Risks

Categorize each risk/unknown:
- **Investigate now**: Can be resolved with codebase queries or web search
- **Accept with mitigation**: Cannot be fully resolved, but mitigation exists
- **TBD - requires runtime testing**: Cannot be determined pre-implementation

### 3. Investigate Resolvable Risks

For each "Investigate now" item:
- Query the codebase using `request_clarification`
- Search external sources
- Document findings with evidence

### 4. Define Mitigations

For each "Accept with mitigation" item, document the specific mitigation strategy.

### 5. Refine the Logical Design

Based on investigation findings:
- Update theme groupings if risks revealed structural issues
- Adjust feature ordering if dependencies changed
- Update test strategy with new test requirements

### 6. Validate Design Coherence

Review the refined design for:
- ALL backlog items still covered (BL-001 through BL-006)
- No circular dependencies
- Test strategy covers risk mitigations
- Execution order still makes sense

## Output Requirements

Write ALL output files to BOTH locations:

**Primary (design artifact store):** `comms/outbox/versions/design/v001/005-critical-thinking/`
**Exploration output:** `comms/outbox/exploration/design-v001-005-critical-thinking/`

### README.md (required)

First paragraph: Summary of critical thinking review — risks investigated, resolutions found, design changes made.

Then:
- **Risks Investigated**: Count and categories
- **Resolutions**: Key findings that changed the design
- **Design Changes**: What changed from Task 004's proposal
- **Remaining TBDs**: Items requiring runtime testing
- **Confidence Assessment**: Overall confidence in the refined design

### risk-assessment.md

For each risk from Task 004 with original severity, category, investigation, finding, resolution, and affected themes/features.

### refined-logical-design.md

Updated logical design incorporating all findings.

### investigation-log.md

Detailed log of all investigations performed.

## Guidelines

- ALL backlog items from PLAN.md are MANDATORY
- Build exclusively on Task 004's output and the design artifact store
- Document ALL investigation work — even dead ends
- Keep each document under 200 lines
- Do NOT commit — the master prompt handles commits after this task

## When Complete

git add comms/outbox/exploration/design-v001-005-critical-thinking/
git add comms/outbox/versions/design/v001/005-critical-thinking/
git commit -m "exploration: design-v001-005-critical-thinking complete"
