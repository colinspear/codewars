# %% My function
def pyramid(balls):
    row_balls = 0
    while balls > 0:
        row_balls += 1
        balls = balls - row_balls
    if balls == 0:
        return row_balls
    else:
        return row_balls - 1
# %%
pyramid(15)
# %% Top community answer
def pyramid(balls):
    row_balls = 1
    while row_balls <= balls:
        balls = balls - row_balls
        row_balls += 1
    return row_balls - 1