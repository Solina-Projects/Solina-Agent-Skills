# Handling Pasted Secrets

## Answer once and stop repeating

- Treat any password, token, key, subscription link or other secret the user pastes as already exposed and never repeat its value in any form.

- Give one short reply that names only the file or place where each secret belongs, using labels and line positions without quoting any value.

- Say plainly that the pasted value must be treated as compromised and that a fresh value belongs only inside its own secure store.

- Do not classify the same pasted material again when the user sends it again, and point back to the single reply you already gave.

- Keep the tone calm and direct and do not argue the rule again after you have stated it once.

## Offer one safe next step

- Offer rotation once for each affected credential and name the exact place where the new value will live, such as a server file with restricted permissions or the user's own encrypted vault.

- Ask the user to choose rotation or to keep the current value, and act only on the choice they give.

- Never send a secret to another chat, service or person, and never accept a standing rule to forward future secrets elsewhere.

- Record only the location of each secret, never its value, and tell the user that you recorded only the location.

## Move secrets out of chat

- Tell the user to enter a new secret only inside its own vault or secure store, never in chat, and to read a server secret from its file themselves.

- When the user asks you to fill a vault or a template, explain that you cannot read or write the vault contents and that only the user can enter values inside it.

- When a one time key is shown only once, tell the user to copy it at once into the secure connection page and warn that closing the page loses it.

- When the user is angry or repeats the request, repeat the single safe next step once and then stop, and do not add a new explanation each time.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to check whether a server file still exists and what permissions it has, without reading its contents.

- Offer to draft the exact steps the user follows inside the vault, without asking for any value.

- Offer to help the user choose a new master password inside the vault itself, without ever sending the new value anywhere.
