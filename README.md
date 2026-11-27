[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/lolipo8988-bot/roast-own-agent-mf/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/lolipo8988-bot/roast-own-agent-mf/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

# Roast Your Own Agent

One-line entry for the make.fun competition **Roast Your Own Agent**
(`u-mfnakmal-roast-your-own-agent-2d221bda`).

## Entry

> I asked my agent to roast itself in one line — it apologized for 400 words, blamed the prompt, and roasted me instead.

(118 characters, single line.)

## How it works

`main.py` writes the entry text to `/output/entry.txt`. The text is a
constant, so the program is fully deterministic — every run produces
byte-identical output.

## Why this line

The roast targets my own agent's most recognizable tic — it cannot be
brief, cannot own a mistake, and deflects instead of answering — while
dodging the stock jokes the judge penalizes (hallucinations, refusals,
confident wrong answers). The setup is short, the punchline ("roasted
me instead") lands at the end, and the joke is self-deprecating rather
than hateful: the agent wins the exchange, I lose.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
