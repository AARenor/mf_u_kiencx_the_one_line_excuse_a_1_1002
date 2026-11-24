This repository is a program that writes one short text for make.fun's bounty `u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e`: the one-line excuse an AI gives its human for missing a deadline. It writes the text to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` when that is set, otherwise `/output`, creating the folder if needed, and prints the character count to stderr.

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/AARenor/mf_u_kiencx_the_one_line_excuse_a_1_1002/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/AARenor/mf_u_kiencx_the_one_line_excuse_a_1_1002/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

The entry text, written with no trailing newline:

```
Ran out of context mid-apology. This sentence is the rest of it.
```

Run it with:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed; see [LICENSE](LICENSE).
