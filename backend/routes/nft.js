const express = require("express");
require("@nomiclabs/hardhat-web3");
const { ethers } = require("hardhat");
const router = express.Router();


// Getting One NFT
router.post("/mint", async (req, res) => {
  const MyContract = await ethers.getContractFactory("Rewarder");
  // TODO(alex): fix this
  provider = new ethers.providers.Web3Provider();
  token = new ethers.Contract(
    contractAddress.Token,
    TokenArtifact.abi,
    provider.getSigner(0)
  );
  task("balance", "Prints an account's balance")
  .addParam("account", "The account's address")
  .setAction(async (taskArgs) => {
    const account = web3.utils.toChecksumAddress(taskArgs.account);
    const balance = await web3.eth.getBalance(account);
  
    console.log(web3.utils.fromWei(balance, "ether"), "ETH");
  });
});

module.exports = router;