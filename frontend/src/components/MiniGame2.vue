<script>
export default {
    data() {
        return {
            gameStarted: false,
            gameCountdownVisible: false,
            countdown: 3,
            timeLeft: 7,
            sequence: [1, 2, 3, 4, 5],
            shuffledSequence: [],
            userClicks: [],
            currentIndex: 0,
            gameEnded: false,
            resultMessage: ''
        }
    },
    methods: {
        startGame() {
            this.gameStarted = false;
            this.gameEnded = false;
            this.userClicks = [];
            this.currentIndex = 0;
            this.countdown = 3;
            this.gameCountdownVisible = true;

            this.shuffledSequence = this.shuffleArray([...this.sequence]);

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
                } else if(!this.gameEnded) {
                  clearInterval(timerInterval);
                  this.endGame(false);
                } else{
                  clearInterval(timerInterval);
                }
            }, 1000);
        },
        shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
          // for(let i = 0; i < array.length; i++){
          //   let n = Math.floor(Math.random() * 100);
          //   while(n in array){
          //     n = Math.floor(Math.random() * 100);
          //   }
          //   array[i] = n;
          //     this.sequence[i] = n;
          // }
          // this.sequence.sort();
            return array;
        },

        registerClick(number) {
            if (this.gameEnded) return;
            if (number === this.sequence[this.currentIndex]) {
                this.userClicks.push(number);
                this.currentIndex++;
                if (this.currentIndex === this.sequence.length) {
                  this.gameEnded = true;
                    this.endGame(true);
                }
            } else {
                this.endGame(false);
            }
        },
        endGame(success) {
            this.gameStarted = false;
            this.gameEnded = true;
            if (success) {
                this.resultMessage = "You win! Congratulations! You completed the sequence!";
            } else {
                this.resultMessage = "Wrong sequence or time limit reached! Game over!";
            }
            this.$emit('game-finished', success);
        },
        showMiniGameFalse() {
            this.$emit('close', true);
        },
        handleKeyDown(event) {
              if (event.key === "Enter" || event.key === "Escape") {
                  if (!this.gameStarted && !this.gameEnded && event.key === "Enter") {
                      this.startGame();
                  } else if (this.gameEnded) {
                      this.endGame(false);
                      this.showMiniGameFalse();
                  }
              }
          }
    },
  mounted() {
        window.addEventListener('keydown', this.handleKeyDown);
    },
    beforeUnmount() {
        window.removeEventListener('keydown', this.handleKeyDown);
    }
  }
</script>

<template>
  <div class="modal">
    <div v-if="!gameStarted && !gameEnded">
        <div class="rules-content">
            <h2>Game rules</h2>
            <p>Click the numbers in the correct order!</p>
            <div class="super-little-button" v-if="!gameStarted && !gameCountdownVisible" @click="startGame"><a>Start</a></div>
        </div>
    </div>

    <div v-if="!gameStarted && gameCountdownVisible">
        <h1 id="countdown-number">{{ countdown }}</h1>
    </div>

    <div v-if="gameStarted" id="game">
        <h2>Time: <span>{{ timeLeft }}</span> </h2>
        <div class="number-buttons">
            <div class="little-button" v-for="num in shuffledSequence" :key="num" @click="registerClick(num)"><a>{{ num }}</a></div>
        </div>

    </div>

    <h2 v-if="gameEnded">{{ resultMessage }}<div class="little-button" @click="showMiniGameFalse"><a>Close</a></div></h2>
  </div>
  <div class="overlay"></div>
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


.super-little-button {
  text-align: center;
  background-color: transparent;
  font-family: 'Press Start 2P', sans-serif;
  position: relative;
  display: inline-block;
  margin: 5px;
  cursor: pointer;
}

.super-little-button a {
  color: #6c3282;
  font-family: 'Press Start 2P', sans-serif;
  /* font-weight:bold; */
  font-size: 10px;
  text-align: center;
  text-decoration: none;
  background-color: #d6c6dd;
  display: block;
  position: relative;
  padding: 10px 12px;

  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  text-shadow: 0px 0px 0px #000;
  filter: dropshadow(color=#000, offx=0px, offy=1px);

  -webkit-box-shadow: inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;
  -moz-box-shadow: inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;
  box-shadow: inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;

  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}

.super-little-button a:hover {
  background-color: #601e7c;
  color: #d6c6dd;
}

.super-little-button a:active {
  top: 8px;
  background-color: #2F0A3D;

  -webkit-box-shadow: inset 0 1px 0 #2F0A3D, inset 0 -2px 0 #d6c6dd;
  -moz-box-shadow: inset 0 1px 0 #2F0A3D, inset 0 -2px 0 #d6c6dd;
  box-shadow: inset 0 1px 0 #2F0A3D, inset 0 -2px 0 #d6c6dd;
}

.super-little-button:after {
  content: "";
  height: 100%;
  width: 100%;
  padding: 2px;
  position: absolute;
  bottom: -5px;
  left: -2px;
  z-index: -1;
  background-color: #2F0A3D;
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  border-radius: 2px;
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
input {
  width: 80%;
  padding: 15px;
  border: 2px solid #d6c6dd;
  margin: 15px;
  background: #6c3282;
  color: #d6c6dd;
  font-family: 'Press Start 2P', sans-serif;
  font-size: 14px;
  text-align: center;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
}

</style>