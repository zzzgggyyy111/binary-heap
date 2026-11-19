# 二叉堆：上浮、下沉与弹出

优先队列弹出顺序错乱、堆化后不满足堆序：上浮没有交换父子，下沉没有比较两个孩子，push 没有从末尾上浮，pop 没有把末尾放到根，heapify 没有复用 push，空堆崩，批量插入只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
data/__init__.py
data/heap.py
tests/test_heap.py
```

## 当前状态

`data/heap.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_heap.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 上浮交换父子
2. 下沉比较两个孩子
3. push 末尾上浮
4. pop 末尾放根
5. heapify 复用 push
6. 空堆兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `data/heap.py`
后 15 条用例应全部通过。
