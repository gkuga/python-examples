From the [Python glossary](https://docs.python.org/3/glossary.html#term-assignment-expression):

```
assignment expression
An expression that assigns a value to a name (variable) while returning the
value of that assignment, using the walrus operator (:=).
```

- [PEP 572 -- Assignment Expressions](https://peps.python.org/pep-0572/)
- [Assignment expressions (language reference)](https://docs.python.org/3/reference/expressions.html#assignment-expressions)
- [What's New In Python 3.8](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions)

`:=` (the "walrus operator"), introduced in Python 3.8, lets you assign to a
variable and use that value within the same expression. It's mainly useful
for avoiding duplicate computation or repeated calls when a value needs to
be both tested and used, e.g.:

- `if (n := len(data)) > 3:` — bind a value while testing a condition
- `while (chunk := read()) != EOF:` — loop conditions that read and check in one step
- list comprehensions, where the same computed value is used in both the
  filter and the output expression
