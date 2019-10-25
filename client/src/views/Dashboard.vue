<template>
  <div class="container bg-light-gray" style="height: calc(100vh - 122px)">
    <div class="text-reset pt-4">Press the <span class="text-red">RESET BUTTON</span> to restart the game.</div>
    <button type="button" class="btn btn-outline-danger btn-lg m-4 login-button" @click="showConfirmation">RESET</button>
    <div class="bg-white mt-4 p-3" v-show="displayCon">
        <div class="row">
            <div class="col-12 col-md-12">
                <div class="title-con pt-2 pb-4">Please confirm if you want to reset.</div>
            </div>
            <div class="col-12 col-md-6" @click="confirmBtn(); onReset();">
                <button type="button" class="btn btn-outline-secondary">
                    <img class="icon-size"
                    src="img/confirm.png" alt="confirmcheck"/>
                    Confirm</button>
            </div>
            <div class="col-12 col-md-6" @click="cancelBtn">
                <button type="button" class="btn btn-outline-secondary" >
                     <img class="icon-size"
                    src="img/cross.png" alt="cancelcross"/>
                    Cancel</button>
            </div>
        </div>
    </div>
    <div class="py-4 text-game" v-show="confirmTrue">Game is restarted!</div>
    <div class="py-4 text-game" v-show="cancelTrue">Cancel!</div>
    <div class="pt-5 mt-5">
      <button type="button" class="btn btn-outline-primary my-5 d-flex ml-auto" @click="onLogout">LOGOUT</button>
    </div>
  </div>
</template>

<script>
import Service from '../services/Service';
export default {
  name: 'Dashboard',
  data() {
    return {
      displayCon: false,
      confirmReset: false,
      confirmTrue: false,
      cancelTrue: false
    };
  },
  methods: {
    showConfirmation() {
      return this.displayCon = true;
    },
    hideConfirmation() {
      return this.displayCon = false;
    },
    confirmBtn() {
      this.displayCon = false;
      return this.confirmReset = true;
    },
    cancelBtn() {
      this.displayCon = false;
      return this.confirmReset = false;
    },
    async onReset(event) {
      if (event) event.preventDefault()
        const confirm = await Service.confirmReset({
          confirmReset: this.confirmReset
        })
        if(confirm.data === 'Confirm'){
          this.confirmTrue = true;
        } else {
          this.cancelTrue = true;
        }
    },
    async onLogout(event) {
    if (event) event.preventDefault()
      const success = await Service.logout({
      })
      if(success.data === 'Success'){
        this.$router.push({ name: 'home' })
      }
    }
  },
};
</script>

<style lang="scss" scoped>
@import "../sass/_variables.scss";

.bg-light-gray {
  background-color: $theme-light-gray-color;
}

.bg-white {
    background-color: white;
    border-radius: 6px;
}

.title-con {
    font-size: 1.625rem;
    color: $theme-blue-color;
    font-weight: $font-weight-bold;
}

.icon-size {
    height: 27px;
    weight: 27px;
}

.btn {
  text-align: center;
}

.text-red {
  color: red;
  font-weight: $font-weight-bold;
}

.text-reset {
    font-size: 1.625rem;
    font-weight: $font-weight-bold;
}

.text-game {
    font-size: 1.125rem;
    font-weight: $font-weight-bold;
}

</style>
