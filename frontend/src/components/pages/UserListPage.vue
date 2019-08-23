<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-2 pa-10">유저 검색</div>
        <UserSearchForm :submit="getusers" />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs7>
        <UserList :user-list-cards="userList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>



<script>
import { mapState, mapActions } from "vuex";
import UserList from "../UserList"
import UserSearchForm from "../UserSearchForm";

export default {
  data: () => ({
    cardsPerPage: 10,
    page: 1,
  }),
  components: {
    UserList,
    UserSearchForm
  },
  props: {
    userListCards: {
      type: Array,
      default: () => new Array(),
    },
  },
  computed: {
    ...mapState({
      userList: state => state.data.userList
    //   console.log("user!")
    }),
  },
  methods: mapActions("data", ["getusers"])
};
</script>