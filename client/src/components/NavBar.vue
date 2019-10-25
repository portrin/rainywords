<template>
   <nav class="navbar navbar-expand-md bg-blue">
    <img
        src="img/rainywordsicon.png"
        width="150"
        height="50"
        class="d-inline-block mx-4"
        alt
      />
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#myNavbar"
      aria-controls="#myNavbar"
      aria-expanded="false"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="navbar-nav ml-auto align-items-center">
        <li class="nav-item">
          <router-link class="nav-link text-white" to="/about">
          Admin</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style lang="scss" scoped>
@import '../sass/_variables.scss';

.bg-blue {
    background-color: $theme-blue-color;
}

.text-white {
    color: white;
}

</style>