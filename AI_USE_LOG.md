# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 3
- Student name: Tan Hui Shan
- Matric no: A24CS0197
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 4 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 4 November 2026 10:45AM
- Tool: Google (2026). Gemini. Retrieved 4 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "what alternative key can I press directly to see the "preview" of my qc_design?"
- Output: Explained that pressing `Ctrl+Shift+V` in VS Code opens the Markdown preview tab, allowing me to see exactly how the formatted design document will look.
- Verified by: Pressed `Ctrl+Shift+V` in VS Code to confirm the preview worked.
- My change: Used the shortcut to verify my markdown formatting before finalizing the document.
- Used in: `design/qc_design.md`

## Entry 2

- Date: 4 November 2026 11:10AM
- Tool: Google (2026). Gemini. Retrieved 4 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "what is the meaning of trim loop"
- Output: Explained that the trim loop removes low-quality sequence bases from the tail end one by one until the quality threshold is met.
- Verified by: Read the lab instructions to confirm the trimming logic matched the requirements.
- My change: Used this conceptual understanding to correctly implement the boundary check in the while loop.
- Used in: `src/qc.py` (trim_low_quality)

## Entry 3

- Date: 4 November 2026 11:40AM
- Tool: Google (2026). Gemini. Retrieved 4 November 2026 from https://gemini.google.com
- Purpose: generate-code
- Prompt: "for classify_read can I use if-else condition? what is the use of elif?"
- Output: Confirmed `if-elif-else` is valid, explained that `elif` handles mutually exclusive conditions, and provided a code snippet.
- Verified by: Ran pytest to ensure the classification logic worked identically to early return statements.
- My change: Replaced the separate `if` statements with the provided `if-elif-else` structure for better readability.
- Used in: `src/qc.py` (classify_read)