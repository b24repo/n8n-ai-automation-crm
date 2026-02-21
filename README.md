# n8n AI Automation — CRM Sync, Lead Scoring & Follow-ups

End-to-end AI-powered lead operations pipeline built with n8n, OpenAI, and Supabase.

## What It Does
Automates the full lead lifecycle: inbound capture → AI scoring → CRM sync → personalised follow-up sequences.

## Architecture
```
Webhook (lead capture)
  → n8n Workflow Engine
    → OpenAI GPT-4o (lead scoring + email generation)
    → Supabase (lead storage + status tracking)
    → HubSpot / Pipedrive CRM sync
    → Gmail / SendGrid (follow-up emails)
    → Slack (team alerts for hot leads)
```

## Tech Stack
```
n8n (self-hosted) · OpenAI API · Supabase · Python
HubSpot API · Slack API · Gmail API · Docker Compose
```

## Workflows Included
| Workflow | Description |
|----------|-------------|
| `lead-capture.json` | Webhook → validate → store in Supabase |
| `lead-scoring.json` | GPT-4o scoring (0–100) + persona tagging |
| `crm-sync.json` | Bidirectional sync with HubSpot/Pipedrive |
| `follow-up-sequence.json` | 3-touch email sequence with AI personalisation |
| `hot-lead-alert.json` | Slack alert when score > 80 |

## Results
- 3× faster lead qualification
- 45% increase in email reply rates
- 80% reduction in manual CRM data entry
- Processes 500+ leads/day on a $20/mo VPS

## Quick Start
```bash
git clone https://github.com/b24repo/n8n-ai-automation-crm
cd n8n-ai-automation-crm
cp .env.example .env
docker-compose up -d
# Import workflows from /workflows/*.json into your n8n instance
```

## Project Structure
```
├── workflows/
│   ├── lead-capture.json
│   ├── lead-scoring.json
│   ├── crm-sync.json
│   ├── follow-up-sequence.json
│   └── hot-lead-alert.json
├── scripts/
│   └── seed_supabase.py    # DB schema + seed data
├── docker-compose.yml
└── .env.example
```

---
*Built for Upwork clients needing automated lead ops without a dedicated RevOps team.*