<template>
  <div class="container bg-light-gray" style="height: calc(100vh - 122px)">
    <div
      class="col-12"
    >
      <img
        src="img/rainywordsicon.png"
        class="mt-5 px-5 pt-5"
        alt
      />
      <form
        class="py-5 mx-5 d-inline-block"
      >
        <div class="form-row justify-content-center">
          <div class="form-group px-5 pb-1 col-12 col-md-8">
          <label for="emailInput">Email:</label>
            <input
              type="email"
              class="form-control"
              id="emailInput"
              placeholder="Please enter your email"
              name="email"
              v-model="email"
            />
        </div>
        <div class="form-group px-5 col-12 col-md-8">
          <label for="emailPassword">Password:</label>
            <input
              type="password"
              class="form-control"
              id="emailPassword"
              aria-describedby="passwordHelp"
              placeholder="Password"
              name="password"
              v-model="password"
            />
            <small id="passwordHelp" class="form-text text-light">Forgot your password?</small>
            <button
              type="submit"
              class="btn btn-outline-secondary d-flex ml-auto"
              @click="onSubmit($event)"
            >
              Login
            </button>
        </div>
        </div>
      </form>
    </div>
    <div class="py-4" v-show="notMatch">Username or password is incorrect.</div>
  </div>
</template>

<script> 
import Service from '../services/Service';
export default {
  name: "Home",
  data() {
    return {
      notMatch: false,
      email: '',
      password: '',
    }
  },
  methods: {
    async onSubmit(event) {
    if (event) event.preventDefault()
      const success = await Service.login({
        email: this.email,
        password: this.password
      })
      if(success.data === 'Success'){
        this.$router.push({ name: 'dashboard' })
      } else {
        this.notMatch = true;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../sass/_variables.scss";

.bg-light-gray {
  background-color: $theme-light-gray-color;
}
</style>
