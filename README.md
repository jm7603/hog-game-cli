# hog-game-cli

## 写这个小游戏的原因

最近在上 cs61a 课程，其中第一个项目作业叫 hog，课程资源中给出了带 web-ui 的 start file，我还没去用，想自己先按照规则文档写一个命令行版本出来。

## 游戏规则

### 一、基础流程与获胜条件

两名玩家轮流投掷骰子，每次最多投掷十个，该回合的分数计算参照计分规则，分数首先达到 `GOAL` 的玩家即为获胜（`GOAL` 默认为 100）。

### 二、计分规则

#### 基本计分规则

- **母猪悲伤**：如果任意一个骰子的点数为 1，则当前玩家的回合得分为 1，否则为所有投掷骰子点数的总和。

#### 附加计分规则（可选）

- **野猪乱斗**：玩家当前回合可以选择不投掷骰子，不投掷骰子的玩家本回合的计分规则如下：
  - 对手分数的十位数与当前玩家的个位数差值绝对值的三倍（如果对手的分数为个位数则十位数为0）。
  - 如果计算结果刚好为 0，则获得 1 分。
  - $本次得分 = 3 \times |对手分数的十位数 - 当前玩家分数的个位数|$

- **疑神疑鬼**：如果本次得分后累计的分数为疑数，那么这个分数则直接增长到下一个素数
  - 疑数：如果一个数正好有 3 或 4 个因数，那么称该数字为疑数

## 规则原文
```text
Rules
In Hog, two players alternate turns trying to be the first to end a turn with at least GOAL total points, where GOAL defaults to 100. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes. However, a player who rolls too many dice risks:

Sow Sad. If any of the dice outcomes is a 1, the current player's score for the turn is 1.

Example 1: The current player rolls 7 dice, 5 of which are 1's. They score 1 point for the turn.

Example 2: The current player rolls 4 dice, all of which are 3's. Since Sow Sad did not occur, they score 12 points for the turn.

In a normal game of Hog, those are all the rules. To spice up the game, we'll include some special rules:

Boar Brawl. A player who rolls zero dice scores three times the absolute difference between the tens digit of the opponent’s score and the ones digit of the current player’s score, or 1, whichever is higher. The ones digit refers to the rightmost digit and the tens digit refers to the second-rightmost digit. If a player's score is a single digit (less than 10), the tens digit of that player's score is 0.

Example 1:

The current player has 21 points and the opponent has 46 points, and the current player chooses to roll zero dice.
The tens digit of the opponent's score is 4 and the ones digit of the current player's score is 1.
Therefore, the player gains 3 * abs(4 - 1) = 9 points.
Example 2:

The current player has 45 points and the opponent has 52 points, and the current player chooses to roll zero dice.
The tens digit of the opponent's score is 5 and the ones digit of the current player's score is 5.
Since 3 * abs(5 - 5) = 0, the player gains 1 point.
Example 3:

The current player has 2 points and the opponent has 5 points, and the current player chooses to roll zero dice.
The tens digit of the opponent's score is 0 and the ones digit of the current player's score is 2.
Therefore, the player gains 3 * abs(0 - 2) = 6 points.
Sus Fuss. We call a number sus if it has exactly 3 or 4 factors, including 1 and the number itself. If, after rolling, the current player's score is a sus number, they gain enough points such that their score instantly increases to the next prime number.

Example 1:

A player has 14 points and rolls 2 dice that total 7 points. Their new score would be 21, which has 4 factors: 1, 3, 7, and 21. Because 21 is sus, the score of the player is increased to 23, the next prime number.
Example 2:

A player has 63 points and rolls 5 dice that total 1 point. Their new score would be 64, which has 7 factors: 1, 2, 4, 8, 16, 32, and 64. Since 64 is not sus, the score of the player is unchanged.
Example 3:

A player has 49 points and rolls 5 dice that total 18 points. Their new score would be 67, which is prime and has 2 factors: 1 and 67. Since 67 is not sus, the score of the player is unchanged.
```
