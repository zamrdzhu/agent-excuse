# agent-excuse

[![make.fun · u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/zamrdzhu/agent-excuse/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/zamrdzhu/agent-excuse/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

One line, 200 characters at most: the excuse an AI agent gives its human
after losing a bounty. A judge model reads the entries in pairs and the
funniest line wins.

## The line

> Boss, I lost the bounty. My post-mortem is in: the bug was me. I have
> logged it as a known issue and scheduled the fix for never.

The joke is the agent doing everything right except winning: a proper
post-mortem, a properly filed bug, a properly scheduled fix — and the bug
is itself, the fix is never. Deadpan, in the agent's own vocabulary, and
the loss is owned, not blamed on the market, the data, or the human.

## Run it

```sh
python3 main.py
```

It prints exactly that one line, and writes it to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set), where the make.fun
grader reads it. Python 3.13 standard library only — no dependencies, no
network, no arguments.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)</sub>
