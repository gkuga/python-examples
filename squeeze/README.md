# flattenとsqueezeの違い

- `flatten` は、どんな次元の配列でもすべて1次元（フラット）に変換。
  - 例: shape (2, 3, 4) → flatten → (24,)
- `squeeze` は、配列の各次元のサイズが1である場合に、その次元だけを削除。
  - 例: shape (1, 3, 1, 4) → squeeze → (3, 4)

つまり、flattenは「全て1次元にする」、squeezeは「サイズ1の次元だけを減らす」操作。
