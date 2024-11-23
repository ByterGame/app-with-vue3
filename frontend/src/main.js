import { createApp } from 'vue'
import {createStore} from 'vuex';
import App from './App.vue'

const store = createStore({
  state: {
    username: ''
  },
  mutations: {
    setUsername(state, username) {
      state.username = username;
    }
  },
  actions: {
    updateUsername({ commit }, username) {
      commit('setUsername', username);
    }
  }
});

const app = createApp(App)
app.use(store)
app.mount('#app')
