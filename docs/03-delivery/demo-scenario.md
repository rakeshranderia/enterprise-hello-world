# Guided GitHub Demonstration Scenario

This scenario creates a **real** project history. Do not manufacture old commits or closed issues.

## Phase 1 — Initial Delivery

1. Create the repository.
2. Commit the initial project files.
3. Create the GitHub Project board.
4. Create the initial backlog issues.
5. Move the implementation issue to **In Progress**.
6. Create a branch:
   `feature/hello-world-service`
7. Make a small legitimate change, such as improving the health response.
8. Push the branch.
9. Open a pull request.
10. Observe CI.
11. Review the PR.
12. Merge it.
13. Move the issue to **Done**.

## Phase 2 — Intentional Defect Demonstration

The defect should be introduced **openly as part of the demonstration**, not disguised.

1. Create issue:
   `Demonstration defect: incorrect Hello World response`
2. Create branch:
   `demo/introduce-known-defect`
3. Temporarily change:
   `Hello World`
   to:
   `Helo World`
4. Update the relevant test to demonstrate how a poor test change could allow the defect.
5. Open a PR clearly labelled as a demonstration.
6. Merge only if you are comfortable showing the deliberately controlled scenario.
7. Create a bug issue noting the UAT failure.
8. Create:
   `bugfix/restore-hello-world`
9. Restore the correct output and test.
10. Open a PR.
11. Confirm CI passes.
12. Merge.
13. Close the bug.

Alternative: if you do not want deliberate broken code on `main`, perform steps 3–6 only on a branch and use the failed UAT evidence without merging it.

**The alternative is recommended.**

## Phase 3 — Release

1. Complete release-readiness checklist.
2. Create a milestone `v1.0.0`.
3. Close release-blocking issues.
4. Tag:
   `v1.0.0`
5. Create a GitHub Release.
6. Use the release notes template.

## Phase 4 — Hypercare Incident

Use the simulated incident in `docs/08-incident/incident-simulation.md`.

Create:
- an incident issue;
- executive update;
- decision log;
- PIR action.

Move the Project item:

**Hypercare → Done**

## Phase 5 — BAU

Complete the operational acceptance and BAU handover documents.

The result is an authentic demonstration of:

**Requirement → Issue → Branch → PR → CI → UAT → Release → Incident → Improvement → BAU**
