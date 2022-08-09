[glossary](https://docs.python.org/ja/3/glossary.html)より

```
decorator
(デコレータ) 別の関数を返す関数で、通常、 @wrapper 構文で関数変換として適用されます。デコレータの一般的な利用例は、 classmethod() と staticmethod() です。

デコレータの文法はシンタックスシュガーです。次の2つの関数定義は意味的に同じものです:

def f(arg):
    ...
    f = staticmethod(f)

    @staticmethod
    def f(arg):
        ...
        同じ概念がクラスにも存在しますが、あまり使われません。デコレータについて詳しくは、 関数定義 および クラス定義 のドキュメントを参照してください。
```
