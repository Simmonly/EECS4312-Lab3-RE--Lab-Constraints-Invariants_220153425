# Task 2 Requirement Classification
1. <What format or type should the patient have?, Constraint>
Justification: Restricts the allowed user input
2. <Should the medication names follow a controlled vocab or can it just be free text?, Constraint>
Justificaiton: Limits the valid values for medication field
3. <Should the system record the date and time of each dispensing event?, Functional Requiremenet>
Justification: Adds new system behaviour
4. <Are fractional doses allowed?, Constraint>
Justification: Restricts allowed numerical values
5. <Should there be a limit to the number of units dispenses at once?, Constraint>
Justification: Enforces safety boundary
6. <What should happen if the medication isn't recognized?, Functional Requirement>
Justification: Defines system response behaviour
7. <Should the system preventing dispensing medications that interact dangerously?, Invariant>
Justification: A system-wide safety property that must always hold
8. <Should pharmacists be able to override constraints in emergency situations?, Functional Requirement>
Justification: Describes the special operation behaviour
