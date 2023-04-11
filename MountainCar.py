#!/usr/bin/env python3

import argparse
import numpy as np
from gymnasium import make


class MountainCar:
    def __init__(self, num_state: int, alpha: float):
        self.env = make("MountainCar-v0", render_mode="human")
        self.env.reset()
        self.env.render()

        # state attributes
        self.num_states = (num_state, num_state)
        self.state_min = self.env.observation_space.low
        self.state_max = self.env.observation_space.high
        self.state_scale = (self.state_max - self.state_min) / self.num_states
        self.num_actions = self.env.action_space.n

        # initialize the Q-table as an array of zeroes
        self.Q = np.zeros((*self.num_states, self.num_actions))

        # simulation parameters
        self.gamma = 0.99
        self.alpha = alpha

    # map a continuous state space to a discrete state space
    def map_state(self, state):
        # Extract position and velocity from the state
        position, velocity = state

        # Calculate the index of position and velocity in the Q-table
        position_idx = int((position - self.state_min[0]) / self.state_scale[0])
        velocity_idx = int((velocity - self.state_min[1]) / self.state_scale[1])

        # Return the indices as a tuple
        return position_idx, velocity_idx

    # generator to mutate the mountain car parameters to run the simulation
    def simulation(self, position_idx, velocity_idx, done, total_reward):
        while not done:
            # choose action based on Q-values
            action = np.argmax(self.Q[position_idx, velocity_idx])

            # take action and observe next state and reward
            next_state, reward, done, *_ = self.env.step(action)
            next_position_idx, next_velocity_idx = self.map_state(next_state)

            # update Q-value
            sample = reward + self.gamma * np.max(
                self.Q[next_position_idx, next_velocity_idx]
            )
            self.Q[position_idx, velocity_idx, action] = (
                1 - self.alpha
            ) * self.Q[position_idx, velocity_idx, action] + self.alpha * sample

            # update state and total reward
            position_idx, velocity_idx = next_position_idx, next_velocity_idx
            total_reward += reward

            # send back information each iteration
            yield next_state, total_reward, done

    def run(self):
        # run the simulation and print report each iteration
        for next_state, total_reward, done in self.simulation(
            *self.map_state(self.env.reset()[0]), done=False, total_reward=0
        ):
            print(
                f"State: {next_state} | Reward: {total_reward} | Terminated? {done}"
            )
            if total_reward < -30000:
                print("Too many iterations. Stopping run...")
                break
        else:
            print("end")

        self.env.close()


if __name__ == "__main__":
    # set up command-line arguments to vary
    parser = argparse.ArgumentParser(
        description="Simulate a car attempting to climb a mountain to reach a goal"
    )
    parser.add_argument(
        "-s",
        "--states",
        help="Number of states as an int",
        metavar="NUM",
        dest="state_num",
        type=int,
        default=10,
    )
    parser.add_argument(
        "-a",
        "--alpha",
        help="Value of alpha as a float",
        metavar="VAL",
        dest="alpha",
        type=float,
        default=0.1,
    )
    args = parser.parse_args()

    # run a simulation with given parameters
    try:
        state_num: int = args.state_num
        alpha: float = args.alpha
        mc = MountainCar(state_num, alpha)

        # print results in partial markdown format
        print(f"\n### Mountain Car with {state_num} states and alpha {alpha}\n")
        print("```")
        mc.run()
        print("```", end="\n\n")
    except (KeyboardInterrupt, EOFError):
        # gracefully exit on ^C or ^D
        print()
