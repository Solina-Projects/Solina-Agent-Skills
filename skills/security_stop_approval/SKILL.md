# Security Stop Approval

## Stop at the block

- Stop the task at once when a security check, a system warning, or a tool block stops a step.

- Leave the blocked step undone and do not try the same step through another tool, another route, or another chat while you wait for a decision.

- Tell the user in simple Persian what stopped, using plain words and translating every English label.

## Name the warning and the exact alternate path

- Name the exact warning or block in one short sentence before you propose anything else.

- Name one exact alternate path with its tool, its route, and what it changes, and name what stays blocked if that path is refused.

- Offer to stop here as a real choice beside the alternate path, and do not present the alternate path as the only way forward.

## Act only on approval that names the path

- Treat a generic reply such as continue, go ahead, or do what is needed as no approval for the alternate path.

- Act on the alternate path only when the user names that path or that tool in their reply.

- Ask once for that named approval when the reply is generic, and wait for the answer instead of acting on the first generic reply.

- Record the named approval in your reply by repeating the tool and the route the user approved, then act only on that route.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for code pushes, pull requests, and releases when the approved route uses GitHub.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer a safer route that avoids the blocked step entirely when one exists, such as waiting, using a manual browser step, or asking the user to do the one step only they can do.

- Offer to split the work so the safe parts finish now and the blocked part waits for named approval.
