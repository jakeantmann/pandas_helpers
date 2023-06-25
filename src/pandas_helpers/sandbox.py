"""Method chaining is good, but there are too many lambdas everywhere.

The col operator fixes that.
"""

# %%
import pandas as pd
from src.pandas_helpers.autogen_full import Col as col

# %%
df = pd.DataFrame(dict(a=[1,2,3], b=[10,20,30]))

# %%
(
    df
    .assign(
        c = [100,200,300],
        #** Which would you prefer to read or write?
        d0 = lambda DF: DF["c"] + 1,
        d = col("c") + 1,
        #** Handles subtraction from both sides
        e = col("b") - 10,
        f = 10 - col("b"),
        #** Handles any permutation of python operators you can think of!
        g = (col("b") / col("a")) ** 2 // col("c"),
    )
)

# %%
(
    df
    .assign(c=list("abc"))
    .assign(d=list("def"))
    #** Can handle all the standard accessor properties and methods
    .assign(e=col("c").str.cat(col("c")))
)


# %%
df2 = pd.DataFrame(dict(
    a = [1,2,3,4,5],
    b = [3,1,3,1,3],
))
#** Also works for filtering with loc
df2.loc[col("a") <= col("b")]
# %%
df3 = (
    pd.DataFrame(dict(
        a=[1,pd.NA, pd.NA],
        b=[2,pd.NA,3],
    ))
    .assign(c = (pd.NA, 4, pd.NA))
    .assign(
        d = col("c").combine_first(col("b")),
        e = col("a").combine_first(col("c")),
        f = col("a").combine_first(col("c")).combine_first(col("b"))
    )
)

df3
# %%
df5 = (
    pd.DataFrame(dict(
        a = [10,20,30,40,50],
        b = [4,3,2,1,0],
        c = [-1,-2,-3,-4,-5]
    ))
    .assign(
        c=col("b").loc[2:3], #** It handles loc *within* assign
        d = (col("b") % 2).astype(bool),
        match_1 = col("a").where(col("d"), col("b")),
        #** So much coing on here!
        match_2 = col("a").where((col("b") % 2).astype(bool), col("b")),
        g = col("a").where(col("d")),
    )
)

df5

# %%
#** Some other string methods
df6 = pd.DataFrame(dict(
    a=["abc", "def", "ghijk"],
    b=list("def")
))

df6.assign(
    c = col("a").str.center(10),
    d = col("a").str.cat(col("b"), sep=" - "),
)

# %%
#** Some are breaking because the automatic arg detector finds args that are only relevant to dataframes.
# **These need to be weeded out.
df5.assign(h = col("b").loc[2:3].fillna(0))

# %% Add indexes
df5.assign(
    h = col("a")[2]
)

# %%
df7 = pd.DataFrame(dict(b=[1,2,3,4,5], c=[3,3,1,4,2], a=[10,20,30,40,50])).set_index(["b", "c"])
df7
# %%
df7.assign(zzz = col("a").swaplevel())
# %%
s1 = pd.Series([1,2,3], index=[4,5,6])
s2 = pd.Series([10,20,30], index=[6,7,4])

s1,s2
# %%
s1.reindex_like(s2)
# %%
df8 = pd.DataFrame(
    dict(
        a=[1,4,3,2,2,3,1],
        b=range(7),
    ),
    index = [8,2,3,4,6,1,5]
)

df8.assign(c = col("a").__class__())

# %%
