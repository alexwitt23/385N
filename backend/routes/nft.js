const express = require("express");
require("@nomiclabs/hardhat-web3");
const router = express.Router();

// Getting One Post by id
router.post("/mint", (req, res) => {
  console.log("MINT");
  task("balance", "Prints an account's balance")
  .addParam("account", "The account's address")
  .setAction(async (taskArgs) => {
    const account = web3.utils.toChecksumAddress(taskArgs.account);
    const balance = await web3.eth.getBalance(account);

    console.log(web3.utils.fromWei(balance, "ether"), "ETH");
  });
});

module.exports = router;