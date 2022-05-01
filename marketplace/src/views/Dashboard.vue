<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col col-xl-4 col-sm-6 col-lg-6 mb-xl-0 mb-4">
        <NFTCard 
          :object="nft0.object"
          :name="nft0.name"
          :id="nft0.id"
          :description="nft0.description"
          :price="nft0.price"
          :autor="nft0.autor"
          :avatar="nft0.avatar"
        />
      </div>
      <!-- <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>

      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div>
      <div class="col col-xl-4 col-sm-6 mb-xl-0 mb-4">
        <NFTCard 
          :img="card.img" 
          :name="card.name"
          :id="card.id"
          :description="card.description"
          :price="card.price"
          :autor="card.autor"
          :avatar="card.avatar"
        />
      </div> -->
    </div>
  </div>
</template>
<script>
import NFTCard from './components/NFTCard.vue'

export default {
  name: "dashboard-default",
  data() {
    return {
        nft0: {
          img: "1.glb",
          name: "1",
          id: "0",
          description: "Description",
          price: 100,
          autor: "Alex",
          avatar: "image-avatar.png"
        },
      }
  },
  components: {
    NFTCard,
  },
};
</script>

<style scoped>
.row {
  padding-bottom: 10px;
}
.col {
  padding-right: 100px;
}

.nft-card {
  padding-left: 5px;
  padding-right: 5px;
}

</style>