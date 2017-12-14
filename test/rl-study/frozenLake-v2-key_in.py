class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        # try:
        self.impl = _GetchWindows()
        # except ImportError:
            # self.impl = _GetchUnix()

    def __call__(self): return self.impl()


# class _GetchUnix:
#     def __init__(self):
#         import tty, sys
#
#     def __call__(self):
#         import sys, tty, termios
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

# MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

# Key mapping
arrow_keys = {
    b'H': UP,
    b'P': DOWN,
    b'M': RIGHT,
    b'K': LEFT
}


import gym
from gym.envs.registration import register


register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name':'4x4','is_slippery' : False}
)


env = gym.make("FrozenLake-v3")
env.render()

while True:
    key = getch()

    # skip when special function key pressed
    if key == b'\xe0':
        continue
    elif key not in arrow_keys.keys():
        print("Game aborted!")
        break

    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render()
    print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

    if done:
        print("Finished with reward", reward)
        break