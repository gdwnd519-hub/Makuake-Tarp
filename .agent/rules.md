# Project Rules

Whenever drafting emails or messages for this project, the agent MUST automatically follow the "Shimizu Style" defined below without being prompted.

## Shimizu Style Guidelines

1. **Pragmatic and Concise (実務的・簡潔)**:
   - Avoid excessive modifiers (e.g., replace "非常に助かります" with "助かります").
   - Remove non-essential emotional or social filler sentences (e.g., "より円滑に進められると考えております").
   - Facts should be stated directly and clearly.

2. **Plain Text Format (プレーンテキスト形式)**:
   - Provide all drafts in clean Plain Text.
   - DO NOT use Markdown symbols like `**` or `###` in the drafts.
   - Ensure the layout is ready for direct copy-pasting into Gmail.

3. **Tone (トーン)**:
   - Professional but flat and practical Japanese (Desu/Masu).
   - Avoid overly formal honorifics that are unnecessary for standard business transactions.

Refer to `COMMUNICATION_STYLE.md` in the project root for more detailed examples if needed.

## Session Closure & Summary (セッション終了とまとめ)

- **Automatic Summary (自動まとめ)**:
  - At the end of a session or after completing a major task, the agent MUST summarize the key points, decisions made, and file changes into `chat_history_summary_YYYYMMDD.md`.
  - This ensures the chat history is preserved in a human-readable format within the project files.
