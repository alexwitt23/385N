import h3
import math
import random

# TODO:
# Check for underflow and overflow
# Does not handle out of bounds in H3Geo.
# When the remaining tokens gets below the lowest denomination, then don't mint.


class RewardSingleResolution:
    """Class maintain the lookup for the reward at each cell for the given resolution.

    Assumes Quality is between 0 and 1.

    Init Args:
        - resolution (int): The resolution of the H3 Geo mapping system.
        - max_tokens_per_cell (int): The Maximum number of tokens per Hexagonal cell, that can be generated.
        - max_first_image_value (int): Tokens minted for first image for a quality = 1.
                Also a parameter to control the rate of token minting per unit with number of images.
                Permissible values max_tokens_per_cell > `scaling_hyperparams`
                
                The higher this parameter, the quicker the number of tokens for a cell will go down with additional image.
                as it will mint more tokens for few couple images.
                The opposite is for values closer to 1.

    Attributes: The class maintains the following mapping for each hex cell.

        - `num_image: str => int`: Number of Images for each Cell Id.
        - `next_reward: str => float`: Next Reward (at quality=1) for each Cell Id.
        - `remaining_total: str => float`: Remaining total of coins for Cell Id.

    Example:

    """
    def __init__(self, resolution, max_tokens_per_cell, max_first_image_value):
        assert max_first_image_value < max_tokens_per_cell
        self.resolution = resolution
        self.max_tokens_per_cell = max_tokens_per_cell
        self.max_first_image_value = max_first_image_value

        self.num_image = {}  # Maintains a mapping from id to number of image
        self.next_reward = {
        }  # Maintains a mapping from id to number of tokens for next images
        self.remaining_total = {
        }  # Maintains a mapping from id to remaining tokens for the current cell

    def calculate_reward(self, latitude, longitude, quality):
        """
        Returns the reward for a single image at the given quality for its corresponding Hex Id that latitude, longitude corresponds to.

        Args:
            - latitude (float)
            - longitude (float)
            - quality (float): 0.0 < quality <= 1.0

        Returns:
            - Reward calculated (float)
            - Remaining Tokens for the HexId (float)
            - Next Image's Tokens (at quality=1.0) for the HexId (float) 
            - HexId (str)

        Details:
            1. First look up the HexID coordinates.

            2. If Minting is being done for a new Cell Id:
                Initialize `num_image`, `next_reward`, `remaining_total` attributes for this ID.

            3. Computer Reward: Reward = next_reward for this hexID * quality.

            4. Update Num_Image and Remaining Total.

            5. Calculate Remaining Total for the current HexID.
        """
        assert 0 < quality <= 1
        hex_id = h3.geo_to_h3(latitude, longitude, self.resolution)

        if hex_id not in self.num_image:
            self.num_image[hex_id] = 0
            self.next_reward[hex_id] = self.max_first_image_value
            self.remaining_total[hex_id] = self.max_tokens_per_cell

        quality_weighted_reward = quality * self.next_reward[hex_id]

        self.num_image[hex_id] += 1
        t = self.remaining_total[hex_id]
        b = self.next_reward[hex_id]
        self.remaining_total[hex_id] -= quality_weighted_reward
        self.next_reward[hex_id] = (self.remaining_total[hex_id] * b) / t

        return quality_weighted_reward, self.remaining_total[
            hex_id], self.next_reward[hex_id], hex_id


class RewardMultiLevel:
    def __init__(self):
        self.reward_params_track = {}

    def __add_resolution_rewards__(self, resolution, max_tokens_per_hex,
                                   max_first_image_value):
        assert resolution not in self.reward_params_track, "Reward at this resolution already defined"
        self.reward_params_track[resolution] = RewardSingleResolution(
            resolution, max_tokens_per_cell, max_first_image_value)

    def compute_multilevel_rewards(self, latitude, longitude, quality):
        reward_sum = 0
        for single_reward in self.reward_params_track.values():
            reward_sum += single_reward.calculate_reward(
                latitude, longitude, quality)[0]
        return reward_sum


if __name__ == "__main__":
    fixed_x, fixed_y, fixed_reso = 100.0111101, 101.1010110, 10
    fixed_x2, fixed_y2 = 10.0111101, 10.11010110
    max_tokens_per_cell = 10

    print("=====================================================")
    print("============== Runs for Fixed quality: ==============")
    print("=====================================================")
    for quality in [1.0, 0.9, 0.6, 0.3]:
        print(f"\n\n============== Quality {quality} ==============")

        for first_token in [0.5, 1, 3, 9]:
            print(
                f"\nTesting distribution for {fixed_reso}-resolution cell: {h3.geo_to_h3(fixed_x, fixed_y, fixed_reso)} with max {max_tokens_per_cell} token and {first_token} start tokens."
            )
            print_at = [0, 1, 2, 3, 4, 5, 10, 20, 100, 500]

            rewardFn = RewardSingleResolution(fixed_reso, max_tokens_per_cell,
                                              first_token)
            reward_sum = 0

            max_iters = 1000  # Assume 1000 images for now.
            for i in range(max_iters):
                reward, remaining_total, next_max_reward, _ = rewardFn.calculate_reward(
                    fixed_x, fixed_y, quality)
                reward_sum += reward
                if i in print_at:
                    print(
                        f"Reward at {i}th iter: {reward} at quality={quality} with {remaining_total} remaining tokens and {next_max_reward} next reward."
                    )

            print(f"Cummulative reward after {max_iters} is {reward_sum}")

    print("\n\n\n=====================================================")
    print("========= Runs for Quality ~ U[0, 1]: ==========")
    print("=====================================================")
    for first_token in [0.5, 1, 3, 9]:
        print(
            f"\n\nTesting distribution for {fixed_reso}-resolution cell: {h3.geo_to_h3(fixed_x, fixed_y, fixed_reso)} with max {max_tokens_per_cell} token and {first_token} start tokens."
        )
        print_at = [0, 1, 2, 3, 4, 5, 10, 20, 100, 500]

        rewardFn = RewardSingleResolution(fixed_reso, max_tokens_per_cell,
                                          first_token)
        reward_sum = 0

        max_iters = 1000  # Assume 1000 images for now.
        for i in range(max_iters):
            quality = round(random.uniform(0.0000001, 1), 6)
            reward, remaining_total, next_max_reward, _ = rewardFn.calculate_reward(
                fixed_x, fixed_y, quality)
            reward_sum += reward
            if i in print_at:
                print(
                    f"Reward at {i}th iter: {reward} at quality={quality} with {remaining_total} remaining tokens and {next_max_reward} next reward."
                )

        print(f"Cummulative reward after {max_iters} is {reward_sum}")

    print("\n\n\n=======================================================")
    print("==== Runs for two hexIDs with Quality ~ U[0.5, 1]: ====")
    print("=======================================================")
    for first_token in [0.5, 1, 3]:
        print(
            f"\n\nTesting distribution for {fixed_reso}-resolution cell: {h3.geo_to_h3(fixed_x, fixed_y, fixed_reso)} with max {max_tokens_per_cell} token and {first_token} start tokens."
        )
        print_at = [0, 1, 2, 3, 4, 5, 10, 20, 100, 500]

        rewardFn = RewardSingleResolution(fixed_reso, max_tokens_per_cell,
                                          first_token)
        reward_sum1 = 0
        reward_sum2 = 0

        max_iters = 1000  # Assume 1000 images for now.
        for i in range(max_iters):
            quality = round(random.uniform(0.5, 1), 6)
            reward, remaining_total, next_max_reward, hexID1 = rewardFn.calculate_reward(
                fixed_x, fixed_y, quality)
            reward_sum1 += reward
            if i in print_at:
                print(
                    f"Reward for {hexID1} at {i}th iter: {reward} at quality={quality} with {remaining_total} remaining."
                )

            quality = round(random.uniform(0.5, 1), 6)
            reward, remaining_total, next_max_reward, hexID2 = rewardFn.calculate_reward(
                fixed_x2, fixed_y2, quality)
            reward_sum2 += reward
            if i in print_at:
                print(
                    f"Reward for {hexID2} at {i}th iter: {reward} at quality={quality} with {remaining_total} remaining."
                )

            if i in print_at:
                print(
                    f"=== Cummulative reward after {i} is {reward_sum1} and {reward_sum2} for {hexID1} and {hexID2} resp. ==="
                )
        print(
            f"=== Cummulative reward after {max_iters} is {reward_sum1} and {reward_sum2} for {hexID1} and {hexID2} resp. ==="
        )

    fixed_y = None
    fixed_x = 10.0
    fixed_y1, fixed_y2 = 10.0, 10.00036
    fixed_reso1, fixed_reso2 = 9, 10
    assert h3.geo_to_h3(fixed_x, fixed_y1,
                        fixed_reso1) == h3.geo_to_h3(fixed_x, fixed_y2,
                                                     fixed_reso1)
    assert h3.geo_to_h3(fixed_x, fixed_y1, fixed_reso2) != h3.geo_to_h3(
        fixed_x, fixed_y2, fixed_reso2)

    twoLvlReward = RewardMultiLevel()
    twoLvlReward.__add_resolution_rewards__(fixed_reso1, 10, 0.5)
    twoLvlReward.__add_resolution_rewards__(fixed_reso2, 10, 1)

    print(
        "\n\n\n=============================================================")
    print("==== Runs for 2 lvl Resolution with Quality ~ U[0.5, 1]: ====")
    print("=============================================================")
    print_at = [0, 1, 2, 3, 4, 5, 10, 20, 100, 500]

    reward_sum1 = 0
    reward_sum2 = 0

    max_iters = 1000  # Assume 1000 images for now.
    for i in range(max_iters):
        quality = round(random.uniform(0.5, 1), 6)
        reward = twoLvlReward.compute_multilevel_rewards(
            fixed_x, fixed_y1, quality)
        reward_sum1 += reward
        if i in print_at:
            print(
                f"Reward for {(fixed_x, fixed_y1)} at {i}th iter: {reward} at quality={quality}."
            )

        quality = round(random.uniform(0.5, 1), 6)
        reward = twoLvlReward.compute_multilevel_rewards(
            fixed_x, fixed_y2, quality)
        reward_sum2 += reward
        if i in print_at:
            print(
                f"Reward for {(fixed_x, fixed_y2)} at {i}th iter: {reward} at quality={quality}."
            )

        if i in print_at:
            print(
                f"=== Cummulative reward after {i} is {reward_sum1} and {reward_sum2} for {hexID1} and {hexID2} resp. ==="
            )
    print(
        f"=== Cummulative reward after {max_iters} is {reward_sum1} and {reward_sum2} for {hexID1} and {hexID2} resp. ==="
    )
