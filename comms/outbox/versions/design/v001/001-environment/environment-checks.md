# Environment Checks — Detailed Results

## 1. Health Check

| Check | Result |
|-------|--------|
| Overall Status | Healthy |
| Server Version | 6.0.0 |
| Uptime | 8318 seconds |
| Config Service | OK |
| State Service | OK |
| Execution Service | OK |
| Active Themes | 0 |
| Execution Backend | Legacy mode |

### External Dependencies

| Dependency | Available | Path |
|------------|-----------|------|
| git | Yes | `C:\Program Files\Git\cmd\git.EXE` |
| gh (GitHub CLI) | Yes (authenticated) | `C:\Program Files\GitHub CLI\gh.EXE` |

### Security & Authorization

| Setting | Value |
|---------|-------|
| Tool Keys Required | Yes |
| Authorization Enforcement | Active |
| Active Keys | 2 |
| Warnings | None |

### SDK Test

| Test | Result |
|------|--------|
| CLI Path | `C:\Users\grant\.local\bin\claude.exe` |
| CLI Version | 2.1.34 (Claude Code) |
| Simple Prompt Test | Success (return code 0) |
| SDK Duration | 7554ms |

### Source Sync

| Field | Value |
|-------|-------|
| Status | No (checksum mismatch) |
| Checked File | `services/execution/cli_logger.py` |

Note: Source sync mismatch is informational — indicates the running MCP server may differ from source. Not a blocker for design work.

## 2. Project Configuration

| Field | Value |
|-------|-------|
| Project Name | auto-dev-test-target-2-python |
| Path | `C:/Users/grant/Documents/projects/auto-dev-test-target-2-python` |
| Description | A minimal Python utility library with Jest tests and GitHub Actions CI, designed as a disposable target for auto-dev-mcp integration testing |
| Destructive Test Target | Yes |
| Active Theme | None |
| Completed Themes | None |
| Theme Count | 0 |
| Timeout | 180 minutes |

## 3. Git Status

| Field | Value |
|-------|-------|
| Current Branch | `main` |
| Tracking | `origin/main` |
| Ahead | 0 |
| Behind | 0 |
| Clean | No |
| Repo URL | https://github.com/gwickman/auto-dev-test-target-2-python.git |

### Working Tree Changes

| Type | Count | Files |
|------|-------|-------|
| Modified | 1 | `comms/state/explorations/design-v001-001-environment-1770386308864.json` |
| Staged | 0 | — |
| Untracked | 1 | `nul` |

Note: The modified file is the exploration state tracker for this task (expected). The `nul` file is a Windows artifact (safe to ignore).

## 4. C4 Architecture

No C4 documentation found at `docs/C4-Documentation/README.md`. This is expected for a greenfield project that has not yet had any source code implemented.
