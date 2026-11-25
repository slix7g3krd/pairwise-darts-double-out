# pairwise-darts-double-out

## 领域

游戏、图形与多媒体

## 主题

飞镖双倍收尾

## 说明

镖尖射线求交、双倍收尾校验、回合服务端计时。

初始状态下 `gameplay/darts_double_out.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
