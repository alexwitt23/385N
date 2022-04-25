// SPDX-License-Identifier: GPL-3.0
// TODO: Switch to SafeMath.
// TODO: Interface with Minting.
// TODO: Interface with MultiLevel.
// TODO: Batch Compute Reward with Batch Minting.

pragma solidity ^0.8.4;

import "@openzeppelin/contracts/access/Ownable.sol";
import "./rewardSingleResolution.sol";

contract rewardMultiResolution is Ownable{
    // TODO: Change the folowing to constant.
    uint256 private qualityDenominator;
    bool private mintingAllowed;
    uint256[] private resolutionsArray;

    struct singleResolution{
        uint256 resolution;
        uint256 maxTokensPerCell; // Assumes in Lowest Denomination Unit
        uint256 firstImageValue; // Assumes in Lowest Denomination Unit
        mapping (string => uint256) num_images;
        mapping (string => uint256) next_reward;
        mapping (string => uint256) remaining_total;
    }

    mapping(uint256 => singleResolution) private levelledRewards;

    // Event for EVM logging
    event reducedAmount(
        uint256 resolution,
        string hexID,
        uint256 next_reward,
        uint256 remaining_total
    );


    constructor() {
        mintingAllowed = false;
    }


    function enableMinting() public onlyOwner {
        mintingAllowed = true;
    }

    function addRewardLevel(uint256 resolution, uint256 max_tokens_per_hex, uint256 max_first_image_value) public onlyOwner {
        assert(mintingAllowed == false);
        singleResolution storage rewardStruct = levelledRewards[resolution];
        rewardStruct.resolution = resolution;
        rewardStruct.maxTokensPerCell = max_tokens_per_hex;
        rewardStruct.firstImageValue = max_first_image_value;
        resolutionsArray.push(resolution);
    }

    // Compute Reward
    // Quality is between 1 and 100000
    function computeReward(uint256 quality, string [] memory hexIDs) public onlyOwner returns (uint256) {
        assert(quality <= 100000);
        assert(quality != 0);
        assert(mintingAllowed == true);
        uint256 total_reward = 0;
        for (uint j = 0; j < resolutionsArray.length; j++) {
            string memory hexID = hexIDs[j];
            singleResolution storage tempRewardStruct = levelledRewards[resolutionsArray[j]];
            if (tempRewardStruct.num_images[hexID] == 0){
                tempRewardStruct.next_reward[hexID] = tempRewardStruct.firstImageValue;
                tempRewardStruct.remaining_total[hexID] = tempRewardStruct.maxTokensPerCell;
            }
            uint256 quality_weighted_reward = (quality * tempRewardStruct.next_reward[hexID])/qualityDenominator;

            tempRewardStruct.num_images[hexID] += 1;
            uint256 t = tempRewardStruct.remaining_total[hexID];
            tempRewardStruct.remaining_total[hexID] -= quality_weighted_reward;
            tempRewardStruct.next_reward[hexID] = (tempRewardStruct.remaining_total[hexID] * tempRewardStruct.next_reward[hexID]) / t;

            emit reducedAmount(tempRewardStruct.resolution, hexID, tempRewardStruct.next_reward[hexID], tempRewardStruct.remaining_total[hexID]);

            total_reward += quality_weighted_reward;
        }

        return total_reward;
    }

}