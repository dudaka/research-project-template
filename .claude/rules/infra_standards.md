# Infrastructure Standards

## Provider Stack

{{Describe your providers and how they are used. Example below.}}

| Provider | Purpose | Cost |
| :--- | :--- | :--- |
| **Local** (e.g., Ollama on local GPU/CPU) | Development, testing, bulk runs | $0 |
| **Cloud API 1** (e.g., Cerebras, Together AI) | Speed runs, specific model access | ~$X |
| **Cloud API 2** (e.g., OpenRouter, Google AI Studio) | Multi-model access, evaluation | ~$X |

## Experiment Protocol

{{Key protocol decisions that affect all experiments.}}

- **Context management:** {{e.g., last-round-only, full history, sliding window}}
- **Response length:** {{e.g., max_tokens=200}}
- **Evaluation:** {{e.g., judge model differs from subject model, offline scoring on saved transcripts}}

## MCP Usage

- **Context7:** Check latest library docs before writing infrastructure code.
- **Sequential Thinking:** Use for complex experimental design or architectural decisions.
- **GitHub MCP:** Use experiment branches (e.g., `exp/{{experiment-name}}`) for experiment variants.

## Python Standards

- Use `uv` as package manager (`uv run`, `uv add`)
- Python 3.13+
- Keep modules and functions short and clearly named

## Data Standards

- All experiment outputs: JSONL to `data/processed/`
- Metadata per record: model_name, config params, timestamp, random_seed, token counts
- Transcripts include per-step intermediate outputs where applicable
