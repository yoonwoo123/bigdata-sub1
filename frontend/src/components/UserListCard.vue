<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    유저명: {{ username }}
                  </v-list-item-title>
                  <v-list-item-subtitle>성별: {{ gender }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-card-text>
                <v-layout justify-center>
                    <v-list-item> 나이: {{ age }} </v-list-item>
                    <v-list-item> 직업: {{ occupation }} </v-list-item>
                    <v-list-item> 본 영화 : {{ view_users }} </v-list-item>
                </v-layout>
              </v-card-text>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </v-card>
  </v-hover>
</template>

<script>

export default {
  props: {
    username: {
      type: String,
      default: ""
    },
    gender: {
      type: String,
      default: ""
    },
    age: {
      type: Number,
      default: 0
    },
   occupation: {
      type: String,
      default: ""
    },
  view_users: {
      type: Array,
      default: () => new Array()
    },
  },
  computed: {
  }
};
</script>