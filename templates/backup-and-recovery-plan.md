# Backup and recovery plan

*Template by Adekunle Akeju. CC BY-SA 4.0.*

**Company:** [Name] | **Owner:** [Role] | **Last reviewed:** [Date]

## The 3-2-1 rule

Keep **3** copies of important data, on **2** different kinds of storage, with **1** copy off-site. At least one copy must be offline or immutable, because ransomware attacks connected backups too.

## What we back up

| Data | Where it lives | Backup method | How often | Most we can afford to lose | How fast we need it back |
|---|---|---|---|---|---|
| Email | [Service] | [Method] | [Daily] | [1 day] | [4 hours] |
| Files | [Service] | [Method] | [Daily] | [1 day] | [1 day] |
| Accounting | [Service] | [Method] | [Daily] | [1 day] | [2 days] |
| Website | [Host] | [Method] | [Weekly] | [1 week] | [1 day] |

Cloud services are not automatically backups. A deleted or encrypted file can sync everywhere.

## Protect the backups

- [ ] Backup accounts use a unique password and two-step verification
- [ ] Backup access is separate from everyday admin accounts
- [ ] Backups are encrypted, and the key is stored separately
- [ ] Backup failures alert [Name]

## Test the restore

A backup you have not restored is only a hope.

| Every | Test |
|---|---|
| Month | Restore one file and open it |
| Quarter | Restore a full mailbox or folder |
| Year | Rebuild one critical system from backup and time it |

## Restore log

| Date | What was tested | Worked? | Time taken | Tested by |
|---|---|---|---|---|
| [Date] | [Test] | [Yes/No] | [Time] | [Name] |

## Restoring after an attack

Confirm the attacker is gone first. Restore from a backup made before the incident, onto clean systems.
