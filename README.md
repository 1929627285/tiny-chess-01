# {repo}

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/{owner}/{repo}/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/{owner}/{repo}/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB chess engine in pure Python, standard library only: a 0x88 board, negamax with alpha-beta, quiescence search with check evasions, piece-square tables, MVV-LVA plus killer move ordering, and iterative deepening to a fixed 60,000-node budget per move, so every game replays move for move. It plays through the make.fun env over HTTP and makes no model calls.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=797zmkyh&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
