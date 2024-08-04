# 981. Time base key value store
## Notes
This is a binary search question, since it is timebased every new timestamp will be greater than the previous hence sorted in ascending order
## Code
```python
class TimeMap:

    def __init__(self):
        self.kv = {} # {key : (value, t)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        self.kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        list_keys = self.kv.get(key, [])
        l, r = 0, len(list_keys) - 1
        while l <= r:
            m = (l + r) // 2
            if list_keys[m][1] <= timestamp:
               res = list_keys[m][0]
               l = m + 1
            else:
                r = m - 1 

        return res
```