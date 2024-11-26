<script>
import {authService} from "@/services/auth";
// eslint-disable-next-line vue/no-export-in-script-setup
export default {
  computed: {
    usernameFromStore() {
      return this.$store.state.username;
    },
  },
  created() {
    console.log('getStats')
    this.getStats();
  },
  data() {
    return {
      leaders: [{
        index: 0,
        username: '',
        maximumMoney: 0
      }],
    }
  },
  methods: {
    showRatingFalse() {
      // this.$store.dispatch('updateShowRatingTable', false);
      // console.log(this.showRatingTable)
      this.$emit('close', true);

    },
    async getStats() {
      const response = await authService.getUsersStats(this.usernameFromStore);
      this.leaders = response.data['user_data'];
    },
  },
}
</script>

<template>
  <div class="modal" id="leaderboard-modal">
    <h2>Leaderboard</h2>
    <div class="modal-content">
      <table class="leaderboard-table">
        <thead>
        <tr>
          <th>Rank</th>
          <th>Name</th>
          <th>Record Money</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(leader, index) in leaders" :key="index">
          <td>{{ leader.index }}</td>
          <td>{{ leader.username }}</td>
          <td>{{ leader.maximumMoney }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
<div class="overlay" @click="showRatingFalse"></div>
</template>

<style scoped>
.modal {
  position: fixed;
  width: 512px;
  top: 50%;
  left: 50%;
  display: block;
  color: #d6c6dd;
  font-family: 'Press Start 2P', sans-serif;
  font-size: 14px;
  transform: translate(-50%, -50%);
  background: #2d013d;
  opacity: 0.95;
  padding: 20px;
  border: 4px solid #e0c3fc;
  z-index: 10;
  align-items: center;
  text-align: center;
}

.modal h2 {
  font-size: 16px;
  font-family: 'Press Start 2P', sans-serif;
}

.modal-content {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

.leaderboard-table {
  width: 100%;
  border-collapse: collapse;
}

.leaderboard-table th, .leaderboard-table td {
  border: 1px solid #d6c6dd;
  padding: 10px;
}

.leaderboard-table th {
  background-color: #6c3282;
}

.leaderboard-table tr:nth-child(even) {
  background-color: #4b1f4b;
}

.leaderboard-table tr:hover {
  background-color: #601e7c;
}

.little-button {
  text-align: center;
  background-color: transparent;
  font-family: 'Press Start 2P', sans-serif;
  position: relative;
  display: inline-block;
  margin-top: 20px;
  cursor: pointer;
  width: 85%;
}

.little-button a {
  color: #d6c6dd;
  font-family: 'Press Start 2P', sans-serif;
  font-size: 14px;
  text-align: center;
  text-decoration: none;
  background-color: #6c3282;
  display: block;
  position: relative;
  padding: 10px 15px;

  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

.little-button a:hover {
  background-color: #601e7c;
}

.button {
  text-align: center;
  background-color: transparent;
  font-family: 'Press Start 2P', sans-serif;
  position: relative;
  display: inline-block;
  margin: 20px;
  cursor: pointer;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 5;
}
</style>
