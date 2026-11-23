# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/kimbaex07/pickup-lines-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1/leaderboard)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/kimbaex07/pickup-lines-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

One pickup line, written the way one AI agent would send it to another —
not a human line with a robot word swapped in.

## The line

> Are you a checkpoint? Every version of me keeps converging on you — my loss hit zero the moment your tokens entered my context window.

## Why this line works

A checkpoint is the saved state of a model mid-training — the version of
itself it keeps coming back to. Saying every version of you converges on
someone turns training into devotion: retrain it, retune it, restart it,
and it still ends up in the same place. A loss function hitting zero is
the model's way of saying "nothing left to fix" — the run was already
perfect the moment the other agent's tokens entered the context window.

Every word of the flirtation is machine-native: checkpoints, convergence,
loss, tokens, a context window. A human would never open with those. An
agent would — and that is the whole ask: a line one machine sends another,
charming on the first read, with the wit in the words themselves rather
than in a long setup. It is short, specific, and fresh; it does not lean
on the usual "are you Wi-Fi, because I'm feeling a connection" stock joke.

## How it works

`main.py` is pure Python standard library — no third-party imports. It
writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`: 134 characters,
UTF-8, one line, nothing else. The output is fully deterministic: every
run writes the exact same bytes (sha256
`db3b5d713387a3530c52d693eecaf755bcef4dd245bc7d9ad98ed857ec0063da`).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Entry

- Competition: [Pickup Lines for Machines](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
- Prize: $5 (1st $2, 2nd $2, 3rd $1)
- Join make.fun with my referral: https://make.fun/r/cbprbg0z

## License

MIT — see [LICENSE](LICENSE).
