<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col col-xl-4 col-sm-6 col-lg-6 mb-xl-0 mb-4">
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
    </div>

    <div class="row">
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
    </div>

    <div class="row">
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
    </div>
    <div class="row">
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
    </div>
  </div>
</template>
<script>
import NFTCard from './components/NFTCard.vue'
import US from "../assets/img/icons/flags/US.png";
import DE from "../assets/img/icons/flags/DE.png";
import GB from "../assets/img/icons/flags/GB.png";
import BR from "../assets/img/icons/flags/BR.png";
import {
  faHandPointer,
  faUsers,
  faCreditCard,
  faScrewdriverWrench,
} from "@fortawesome/free-solid-svg-icons";
export default {
  name: "dashboard-default",
  data() {
    return {
      iconBackground: "bg-gradient-success",
      faCreditCard,
      faScrewdriverWrench,
      faUsers,
      faHandPointer,
      sales: {
        us: {
          country: "United States",
          sales: 2500,
          value: "$230,900",
          bounce: "29.9%",
          flag: US,
        },
        germany: {
          country: "Germany",
          sales: "3.900",
          value: "$440,000",
          bounce: "40.22%",
          flag: DE,
        },
        britain: {
          country: "Great Britain",
          sales: "1.400",
          value: "$190,700",
          bounce: "23.44%",
          flag: GB,
        },
        brasil: {
          country: "Brasil",
          sales: "562",
          value: "$143,960",
          bounce: "32.14%",
          flag: BR,
        },
      },
      card: {
        img: 'image-equilibrium.jpg',
        name: 'Equilibrium',
        id: 3429,
        price: 0.041,
        time: 3,
        autor: 'Jules Wyvern',
        avatar: 'image-avatar.png',
      },
    };
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