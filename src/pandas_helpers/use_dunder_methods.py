
# %%
import pandas as pd
from dunder_methods_autogen import Col as col

# %%
df = pd.DataFrame(dict(a=[1,2,3], b=[10,20,30]))

# %%
(
    df
    .assign(c=[100,200,300])
    .assign(d=col("a"))
    .assign(e=col("a") + col("b"))
    .assign(f=col("a") + col("b") + col("c"))
    .assign(g=col("a") + 10000)
    .assign(h=col("a") + col("b") + 10000)
    .assign(i=col("a") + col("b") + col("c") + 10000)
    .assign(j=10000 + col("a"))
    .assign(k=10000 + col("a") + col("b"))
    .assign(l=10000 + col("a") + col("b") + col("c"))
    .assign(m=col("a"))
    .assign(n=col("a") + 10000 + col("b"))
    .assign(o=col("a") + 10000 + col("b") + 10000 + col("c"))
)

# %%
(
    df
    .assign(c=[100,200,300])
    .assign(d = (col("b") ** col("a"))/2 + col("c"))
)
# %%
(
    df
    .assign(c=[100,200,300])
    .assign(o=col("a") + 10000 + col("b") + 10000 + col("c"))
)

# %%
# %%
df2 = pd.DataFrame(dict(
    a = [1,2,3,4,5],
    b = [3,1,3,1,3],
))

df2
# %%
df2.loc[lambda DF: DF["a"] <= DF["b"]]
# %%
df2.loc[col("a") <= col("b")]
# %%
