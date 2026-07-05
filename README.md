# QuietScript

QuietScript is a lightweight AI writing companion designed for literary analysis and creative writing. Running entirely on a local LLM with Ollama and Qwen 2.5, it helps writers explore themes, refine their writing, and overcome creative blocks without relying on external APIs.

## Features

- Analyze literary texts
- Improve writing clarity and flow
- Generate creative writing prompts
- Read text directly from `.txt` files
- Export AI responses as Markdown

## Tech Stack

- Python
- Ollama
- Qwen 2.5 (3B)

## Installation

```bash
pip install -r requirements.txt
ollama pull qwen2.5:3b
python main.py
```

## Project Structure

```
agent.py
main.py
prompts.py
story.txt
requirements.txt
```
