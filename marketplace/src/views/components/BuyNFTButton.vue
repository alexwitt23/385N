<template>
     <button @click="buy_nft">Buy</button>
</template>

<script>
export default {
    methods: {
        buy_nft() {
            console.log("Buying NFT");
        }
    }
}
</script>

<style scoped>
button {
  font-weight: bold;
}
</style>