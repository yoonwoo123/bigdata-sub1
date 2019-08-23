<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="card in userListCardsSliced" :key="card.id" pa-2>
        <UserListCard
          :username="card.username"
          :gender="card.gender"
          :age="card.age"
          :occupation="card.occupation"
          :view_users="card.view_users"
        />
      </v-flex>
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import UserListCard from "./UserListCard"

export default {
  data: () => ({
    cardsPerPage: 10,
    page: 1,
  }),
  components: {
    UserListCard
  },
  props: {
    userListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  computed: {
    userListEmpty: function() {
      return this.userListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.userListCards.length + this.cardsPerPage - 1) / this.cardsPerPage)
    },
    userListCardsSliced: function() {
      return this.userListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page)
    },
  },
};
</script>