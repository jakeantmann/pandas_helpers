
# %%
v = "hello"
# %%
def add(x, y):
    return x + y

def add_3(x):
    return add(x, 3)
# %%
# add_3(5)
# %%
add_3(v)
# %%
d = {
    "a": {"width": 2, "index":4},
    "b": {"width": 6, "index":8, "boop": 1},
}
# %%
for key, value in d.values():
    print(key)
    print(value)
# %%
