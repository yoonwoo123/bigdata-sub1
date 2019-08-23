<template>
  <v-form ref="form">
    <v-text-field v-model="title" label="유저 목록" />
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmit">Search</v-btn>
    </v-layout>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    title: "",
    genre: "",
    items: ["Animation", "Children's", "Comedy", "Adventure", "Fantasy", "Romance", "Drama", "Action", "Crime"],
  }),
  methods: {
    onSubmit: function() {
      const params = {
        title: this.title,
      };
      
      this.submit(params);
    },
    Genre: function() {
      const params = {
        genre: this.genre
      };
      
      this.submit(params);
    },
  }
};
</script>