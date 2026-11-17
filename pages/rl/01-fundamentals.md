# RL Fundamentals

> Status: 🔴 not started

## Concept

Reinforcement learning algorithm mechanics: how an agent learns a policy that maps observations to actions by
maximizing cumulative reward, through trial and error against an environment. This page covers the mechanics
themselves — PPO vs SAC, reward shaping, what actually goes wrong — before any simulator-specific tooling
enters the picture.

## Why it matters

PPO/SAC tradeoffs, reward hacking, and "why did training plateau" stop being interview talking points you
memorized and become things you've actually debugged, the moment you've trained something yourself, even on a
toy task.

## Must-knows for interviews

- **MDP framing**: state, action, reward, transition dynamics, discount factor. Know that most robotics RL
  problems are actually POMDPs (partially observable) in disguise — the agent doesn't get true state, only
  noisy/partial observations (camera images, joint encoders) — this is *why* recurrent policies or stacked
  observations show up so often.
- **On-policy vs off-policy**: PPO is on-policy (learns from data collected by the current policy, discards it
  after each update — more stable, less sample-efficient). SAC is off-policy (learns from a replay buffer of
  past experience, including from older policy versions — more sample-efficient, more hyperparameter-sensitive
  via the entropy temperature term). Know *when* each wins: PPO for environments cheap to simulate in parallel
  (exactly what Isaac Lab gives you), SAC when environment interaction itself is expensive (closer to
  real-world sample efficiency constraints).
- **Reward shaping pitfalls**: reward hacking (the agent finds a technically-correct-but-useless way to
  maximize reward that you didn't intend — a classic, almost guaranteed interview discussion point), sparse vs
  dense rewards (sparse is easier to specify correctly but harder to learn from; dense is easier to learn from
  but easy to shape incorrectly and bias behavior). Know a real example of reward hacking, not just the term.
- **Why training plateaus or diverges**: learning rate too high (divergence), value function not tracking
  reward well (actor gets bad advantage estimates), insufficient exploration (entropy coefficient too low in
  SAC, or clip range too tight in PPO), or the task itself being under-specified by the reward function.

## Project

- [ ] Train PPO and SAC on the same classic task, compare sample efficiency and final performance
- [ ] Deliberately misspecify a reward (e.g. reward distance-traveled instead of reward goal-reached) and
      observe the reward-hacking behavior that results
- [ ] Plot training curves (reward, episode length, value loss) and practice explaining what each one tells you

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(training curves, demo GIFs go here once started)_

## Resources

- [OpenAI Spinning Up](https://spinningup.openai.com/)
- [Sutton & Barto (free)](http://incompleteideas.net/book/the-book.html)
