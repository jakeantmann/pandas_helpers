
# %%
import pandas as pd
from dunder_methods_autogen_full_temp import Col as col

# %%
df = pd.DataFrame(dict(a=[1,2,3], b=[10,20,30]))


# %%
(
    df
    .assign(c=[100,200,300])
    .assign(d = (col("b") ** col("a"))/2 + col("c"))
    .assign(e=col("a") + 10000 + col("b") + 10000 + col("c"))
)

# %%
(
    df
    .assign(c=list("abc"))
    .assign(d=list("def"))
    .assign(e=col("c").str.concat("d")) # TODO - StringAccessor has no __init__!
)


# %%
df2 = pd.DataFrame(dict(
    a = [1,2,3,4,5],
    b = [3,1,3,1,3],
))

# %%
df2.loc[col("a") <= col("b")]
# %%
df3 = pd.DataFrame(dict(
    a=[1,pd.NA, pd.NA],
    b=[2,pd.NA,3],
))

(
    df3
    .assign(c = (pd.NA, 4, pd.NA))
    .assign(
        d = col("c").combine_first(col("b")),
        e = col("a").combine_first(col("c")),
        f = col("a").combine_first(col("c")).combine_first(col("b"))
    )
)

# %%
df5 = pd.DataFrame(dict(
    a = [10,20,30,40,50],
    b = [4,3,2,1,0],
)).assign(c=col("b").loc[2:3])

df5
# %%

# %%
df5 = df5.assign(
    d = (col("b") % 2).astype(bool),
)

df5
# %%
df5.assign(e = lambda DF: DF["d"].where(DF["d"]))

# %%
df5.assign(e = col("d").where(col("d"))) # TODO - doesn't match the above
# %%
