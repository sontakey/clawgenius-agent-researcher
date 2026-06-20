# clawgenius-agent-researcher

Source-heavy research and analysis agent.

## Install

```bash
hermes profile install github.com/sontakey/clawgenius-agent-researcher --alias --name researcher
```

## Update

```bash
hermes profile update researcher
```

## What ships

- `SOUL.md` — profile persona and operating contract
- `skills/` — bundled ClawGenius operating skills
- `mcp.json` — MCP placeholder, intentionally empty until integrations are picked
- `cron/` — cron placeholder, intentionally empty by default
- `distribution.yaml` — manifest and update ownership

## What never ships

No credentials, memories, sessions, logs, workspaces, or local user customization.

## Recommended toolsets

`web, search, file, session_search, skills`

Configure locally after install with:

```bash
hermes -p researcher tools
hermes -p researcher model
```
