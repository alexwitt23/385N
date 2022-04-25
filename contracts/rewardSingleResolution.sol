// SPDX-License-Identifier: GPL-3.0
// TODO: Switch to SafeMath.
// TODO: Interface with Minting.
// TODO: Interface with MultiLevel.
// TODO: Batch Compute Reward with Batch Minting.

pragma solidity ^0.8.4;

import "@openzeppelin/contracts/access/Ownable.sol";

contract rewardSingleResolution is Ownable{

    uint96 private resolution;
    uint256 private maxTokensPerCell; // Assumes in Lowest Denomination Unit
    uint256 private firstImageValue; // Assumes in Lowest Denomination Unit
    // TODO: Change the folowing to constant.
    uint256 private qualityDenominator;

    mapping (string => uint256) private num_images;
    mapping (string => uint256) private next_reward;
    mapping (string => uint256) private remaining_total;

    // Event for EVM logging
    event reducedAmount(
        uint256 resolution,
        string hexID,
        uint256 next_reward,
        uint256 remaining_total
    );

    constructor(uint96 _resolution, uint256 _max_tokens_per_cell, uint256 _first_image_value) {
        assert (_first_image_value <= _max_tokens_per_cell);
        resolution = _resolution;
        maxTokensPerCell = _max_tokens_per_cell;
        firstImageValue = _first_image_value;
        qualityDenominator = 100000;
    }

    // Compute Reward
    // Quality is between 1 and 100000
    function computeReward(uint256 quality, string memory hexID) public onlyOwner returns (uint256) {
        assert(quality <= 100000);
        assert(quality != 0);
        if (num_images[hexID] == 0){
            next_reward[hexID] = firstImageValue;
            remaining_total[hexID] = maxTokensPerCell;
        }

        uint256 quality_weighted_reward = (quality * next_reward[hexID])/qualityDenominator;

        num_images[hexID] += 1;
        uint256 t = remaining_total[hexID];
        remaining_total[hexID] -= quality_weighted_reward;
        next_reward[hexID] = (remaining_total[hexID] * next_reward[hexID]) / t;

        emit reducedAmount(resolution, hexID, next_reward[hexID], remaining_total[hexID]);
        return quality_weighted_reward;
    }

}