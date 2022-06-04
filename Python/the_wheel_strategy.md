#! https://zhuanlan.zhihu.com/p/500292278
# 期权权益金收割计划

- CSP: Cash Secured Puts
- CC: Coverd Calls

## 基本原理

这是一个期权权益金收割策略，基本上是收割 theta。持续卖出 OTM Put，直到某一次的期权被行权，买入正股；但是，此时已经收割过多轮 Put 的权益金，正股的买入价格应该已经低于行权价格。买入正股后，开始卖出 OTM Call，此时即为 Coverd Call，这时选择行权价格最好高于正股的成本价；如果无法选择高于成本价也没问题，即可多次卖出 CC，降低成本，直到行权，卖出正股。然后开始新的一轮循环，这也是 Wheel Strategy 名字的由来。过程中，应该记录权益金和正股成本价格。

该策略的核心是收割权益金，虽然可能会短暂持有正股，但是不会长期持有正股。注意，即使如此，该策略的 delta 是正的，即除了 Theta 的收割，还是有 +Delta 暴露，因此在选择正股时应该选择健康稳定的公司，即长期看涨的公司；另外，不应该选择 Gamma 很大的正股，比如 Tesla 一类股价因为CEO发推特而上蹿下跳的公司。

## 选股

**选股非常重要，不要选择会上新闻或者推特的股票：比如特斯拉、推特这种股票；要选择默默无闻但是季度稳定的股票，比如可口可乐。**

- 盈利且现金流稳定
- 长期利好或横盘
- 正股价格可以承受，但是低于10美金的股票不能碰
- 历史数据相对稳定
- 如果有稳定分红就更好，一方面说明公司质量不错，另一方面持有正股可以得到另一笔收益

## 卖出 Put

- 30 ~ 45 天到期的期权
- 0.3 Delta 的期权
- 如果 Put 已经盈利可以提前止盈，然后重新开仓
- 如果 Put 大概率会被行权，可以考虑 roll，前提是 roll 的损失和权益金可以为正；否则，等待行权，买入正股
- 过程中记录自己的交易，以便后续计算正股成本

## 卖出 Cover Call

因为 Put 的权益金高于 Call，当 Put 行权，我们买入正股后，可以选择：

- 直接卖出正股，开始新的一轮
- 卖出 ITM 或者 ITM call，保证行权，赚一点 theta
- 卖出 OTM call 收取权益金，直到行权，卖出正股。特别是当你的成本高于行权价格，需要 CC 不断拉低成本，扭亏为盈。

## 参考

- https://www.reddit.com/r/options/comments/a36k4j/the_wheel_aka_triple_income_strategy_explained/
- [Rolling Short Puts to Avoid Assignment](https://www.reddit.com/r/Optionswheel/comments/lliy8x/rolling_short_puts_to_avoid_assignment/)
