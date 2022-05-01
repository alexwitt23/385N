const express = require('express');
// require("@nomiclabs/hardhat-web3");

const router = express.Router();

const PORT = 3000;

const app = express();
app.use(express.json());


const nftRouter = require("./routes/nft");
app.use("/nft", nftRouter);

app.listen(PORT, () => console.log("API is Running on PORT " + PORT));