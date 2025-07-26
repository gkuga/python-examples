
以下をやらなくていいようににするための設定

```
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from lib import hello
```

pyproject.tomlを作成
