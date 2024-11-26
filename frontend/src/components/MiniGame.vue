<script>

export default {
  data() {
    return {
      gameStarted: false,
      gameCountdownVisible: false,
      countdown: 3,
      timeLeft: 30,
      clickCount: 0,
      gameEnded: false,
      resultMessage: ''
    }
    },
    methods: {
        startGame() {
            this.gameStarted = false;
            this.gameEnded = false;
            this.clickCount = 0;
            this.timeLeft = 30;
            this.countdown = 3;
            this.gameCountdownVisible = true;

            const countdownInterval = setInterval(() => {
                if (this.countdown > 0) {
                    this.countdown--;
                } else {
                    clearInterval(countdownInterval);
                    this.gameCountdownVisible = false;
                    this.startTimer();
                }
            }, 1000);
        },
        startTimer() {
            this.gameStarted = true;
            const timerInterval = setInterval(() => {
                if (this.timeLeft > 0) {
                    this.timeLeft--;
                } else {
                    clearInterval(timerInterval);
                    this.endGame();
                }
            }, 1000);
        },
        registerClick() {
            this.clickCount++;
        },
        endGame() {
            this.gameStarted = false;
            this.gameEnded = true;
            if (this.clickCount > 100) {
                this.resultMessage = "Поздравляем! Вы набрали " + this.clickCount + " кликов!";
            } else {
                this.resultMessage = "Вот и все! Вы набрали только " + this.clickCount + " кликов.";
            }
        }
    }
}
</script>

<template>
    <div v-if="!gameStarted && !gameEnded" class="overlay">
            <div class="rules-content">
                <h2>Правила игры</h2>
                <p>Нажмите на кнопку более 100 раз за 30 секунд!</p>
                <button @click="startGame">Старт</button>
            </div>
        </div>

        <div v-if="!gameStarted && gameCountdownVisible" class="overlay">
            <h1 id="countdown-number">{{ countdown }}</h1>
        </div>

        <div v-if="gameStarted" id="game">
            <h2>Время: <span>{{ timeLeft }}</span> секунд</h2>
            <h2>Клики: <span>{{ clickCount }}</span></h2>
            <button @click="registerClick">Нажми меня!</button>
            <h2 v-if="gameEnded">{{ resultMessage }}</h2>
        </div>
</template>

<style scoped>
.little-button {
  text-align: center;
  background-color: transparent;
  font-family: 'Press Start 2P', sans-serif;
  position: relative;
  display: inline-block;
  margin: 20px;
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
  text-shadow: 0px 1px 0px #000;
  filter: dropshadow(color=#000, offx=0px, offy=1px);

  -webkit-box-shadow: inset 0 1px 0 #d6c6dd, 0 5px 0 #601e7c;
  -moz-box-shadow: inset 0 1px 0 #d6c6dd, 0 5px 0 #601e7c;
  box-shadow: inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;

  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}

.little-button a:hover {
  background-color: #601e7c;
}

.little-button a:active {
  top: 8px;
  background-color: #601e7c;

  -webkit-box-shadow: inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
  -moz-box-shadow: inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
  box-shadow: inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
}

.little-button:after {
  content: "";
  height: 100%;
  width: 100%;
  padding: 4px;
  position: absolute;
  bottom: -10px;
  left: -4px;
  z-index: -1;
  background-color: #2F0A3D;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}

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

.modal-content button {
  font-family: 'Press Start 2P', sans-serif;
}

</style>