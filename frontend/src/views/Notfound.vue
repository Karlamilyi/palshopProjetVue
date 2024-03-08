<template>
    <h1>404: Page Not Found</h1>

    <p>Sorry, the page you are looking for does not exist.</p>

    <p>
      You can always visit the
      <strong><router-link to="/">home page</router-link></strong>
      to get a fresh start.
    </p>
  </template>
  
  <script>
  export default {
    name: "Notfound",
  };
  </script>
  
  <style scoped>
  h1 {
    text-align: center;
  }
  </style>