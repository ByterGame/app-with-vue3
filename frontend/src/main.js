import { createApp } from 'vue'
import {createStore} from 'vuex';
import App from './App.vue'

const store = createStore({
  state: {
    username: '',
    showRatingTable: false,
  },
  mutations: {
    setUsername(state, username) {
      state.username = username;
    },
    setShowRatingTable(state, showRatingTable) {
      state.showRatingTable = showRatingTable;
    }
  },
  actions: {
    updateUsername({ commit }, username) {
      commit('setUsername', username);
    },
    updateShowRatingTable({commit}, showRatingTable) {
      commit('setShowRatingTable', showRatingTable);
    }
  }
});

const app = createApp(App)
app.use(store)
app.mount('#app')
