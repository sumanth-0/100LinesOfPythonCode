<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Typing Speed Challenge — README</title>
  <style>
    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;line-height:1.6;color:#111;margin:24px}
    pre{background:#f6f8fa;padding:12px;border-radius:6px;overflow:auto}
    code{background:#f1f5f9;padding:2px 6px;border-radius:4px}
    h1,h2{color:#0b69ff}
    .meta{color:#555;font-size:0.95rem}
  </style>
</head>
<body>
  <h1>Typing Speed Challenge</h1>
  <p class="meta">A simple terminal typing speed tester written in Python.</p>

  <h2>What it does</h2>
  <p>Displays a random sentence, times your typing, and shows:</p>
  <ul>
    <li>Time taken (seconds)</li>
    <li>Words per minute (WPM)</li>
    <li>Accuracy (%)</li>
    <li>Errors (mismatches)</li>
    <li>Session stats: best &amp; worst times across rounds</li>
  </ul>

  <h2>Requirements</h2>
  <p>Python 3.7+ (no external libraries required).</p>

  <h2>Usage</h2>
  <ol>
    <li>Navigate to TYPING_SPEED_CHALLENGE folder</li>
    <li>Run in terminal: <pre>python typing_speed_challenge.py</pre></li>
    <li>Follow on-screen prompts. Type the sentence exactly and press Enter.</li>
    <li>After each round you may play again or exit; session stats are shown on exit.</li>
  </ol>

  <h2>Notes & Tips</h2>
  <ul>
    <li>Accuracy is computed by character-by-character comparison (case &amp; punctuation matter).</li>
    <li>WPM is calculated from typed words divided by elapsed minutes (simple approximation).</li>
    <li>ANSI color codes are used for nicer terminal output; run in a modern terminal for best visuals.</li>
  </ul>

</body>
</html>