## Flexibility is ideal in uncertain world

- be proud of changing plans
- be proud of changing your mind
- have uncertainty about yourself, the future (think probabilistically)
- always be skeptical and question yourself - this makes long term planning intractable
- don't need to be good at making decisions if you are good at remaking them

https://medium.com/@awjuliani/maximum-entropy-policies-in-reinforcement-learning-everyday-life-f5a1cc18d32d

## Clean architecture

In the book 'Clean Architecture' Robert Martin espouses a philosophy of software design where the ease of making change is as important as the function of the software.

Martin separates the value of software into function and structure.  Function is the behaviour of the system - does it do what we want it to do.  The value of structure is that it is structure that determines how easy or hard it is to make changes to the system.

Imagine software that functions perfectly but is impossible to change, versus software that doesn't work but is easy to change.  As requirements change, it is only the second software that is useful.  The challenge in software design isn't to get it to work - it is to keep it working as requirements change.

A structure that leaves options open allows decisions about details to be delayed until we have more infomation.  Martin's philosophy is to maximize the number of decisions not made.

## Model based rl

The more you replan, the less perfect each individual plan needs to be (see notes for lct 11 CS294) - and vice versa
