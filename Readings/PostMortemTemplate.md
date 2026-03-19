# Post Mortem Template

Source: https://www.atlassian.com/incident-management/handbook/postmortems#postmortem-issue-fields

## Incident summary

Summarize the incident in a few sentences. Include what the severity was, why, and how long impact lasted.

## Leadup

Describe the circumstances that led to this incident, for example, prior changes that introduced latent bugs.

## Fault

Describe what didn't work as expected. Attach screenshots of relevant graphs or data showing the fault.

## Detection

How and when did we detect the incident?

How could time to detection be improved? As a thought exercise, how would you have cut the time in half?

## Response

Who responded, when and how? Were there any delays or barriers to our response?

## Recovery

Describe how and when service was restored. How did you reach the point where you knew how to mitigate the impact?

## Timeline

Provide a detailed incident timeline, in chronological order, timestamped with timezone(s).

Include any lead-up; start of impact; detection time; escalations, decisions, and changes; and end of impact.

## Five whys

Use the root cause identification technique.

Start with the impact and ask why it happened and why it had the impact it did. Continue asking why until you arrive at
the root cause.

Document your "whys" as a list here or in a diagram attached to the issue.

## Root cause

What was the root cause? This is the thing that needs to change in order to stop this class of incident from recurring.

## Backlog check

Is there anything on your backlog that would have prevented this or greatly reduced its impact? If so, why wasn't it
done?

An honest assessment here helps clarify past decisions around priority and risk.

## Recurrence

Has this incident (with the same root cause) occurred before? If so, why did it happen again?

## Lessons learned

What have we learned?

Discuss what went well, what could have gone better, and where did we get lucky to find improvement opportunities.

## Corrective actions

What are we going to do to make sure this class of incident doesn't happen again? Who will take the actions and by when?

Create "Priority action" issue links to issues tracking each action.