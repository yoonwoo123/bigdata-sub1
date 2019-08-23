<template>
  <v-form ref="form">
    <v-menu offset-y
        transition="slide-x-transition"
        bottom
        right>
        <template v-slot:activator="{ on }">
        <v-btn  v-on="on" color="#FF9800" dark class>
          {{type}}
        </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in types"
            :key="index"
            @click="click_genre(item)"
          >
          <v-list-item-title>{{item}}</v-list-item-title>
        </v-list-item>
      </v-list>
     </v-menu>
     <template>
      <v-btn  @click="click_rating" color="#FF9800" dark class>
        평점 순 정렬
      </v-btn>
    </template>
      <template>
        <v-btn  @click="click_views" color="#FF9800" dark class>
          조회 순 정렬
        </v-btn>
      </template>
    <v-text-field v-model="title" label="영화 제목" />
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
    types : {1:"Action", 2:"Adventure" ,3:"Animation", 4:"Children's" , 5:"Comedy" , 6:"Crime" , 7:"Documentary"
	    ,8:"Drama", 9:"Fantasy" , 10:"Film-Noir" , 11:"Horror" , 12:"Musical" , 13:"Mystery" , 14:"Romance" , 
      15:"Sci-Fi" , 16:"Thriller" , 17:"War" , 18: "Western"},
    type: "장르 순 정렬",
    flag: false,
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
        click_genre: function(item){
      
      this.type = item
      const params = {
        genre : item
      };
      this.submit(params);
      
      
    },
    click_rating: function(){
      this.type ='장르 순 정렬'
      this.submit('rating');
    },
    click_views: function(){
      this.type = '장르 순 정렬'
      this.submit('views')
    }
  }
};
</script>