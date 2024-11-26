<script>
export default {
  data() {
    return {
      gameStarted: false,
      gameCountdownVisible: false,
      countdown: 3,
      timeLeft: 40,
      clickCount: 0,
      gameEnded: false,
      resultMessage: '',
      randomX: 0,
      randomY: 0,
      enemyImage: 'goblin',
    }
    },
    methods: {
    getAnimationClass(enemyId) {
      switch (enemyId) {
        case 1:
          return 'goblin';
        case 3:
          return 'flying-eye';
        case 2:
          return 'dead';
        case 4:
          return 'skeleton';
        case 5:
          return 'demon';
        case 6:
          return 'kobold';
        default:
          return 'goblin';
      }
    },
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
                  this.enemyImage = this.getAnimationClass(Math.floor((Math.random() * 6)));
                  this.randomY = Math.floor((Math.random() * 390)) + 80;
                  this.randomX = Math.floor((Math.random() * 340)) + 40;
                    clearInterval(countdownInterval);
                    this.gameCountdownVisible = false;
                    this.startTimer();
                    this.generatePoints();
                }
            }, 1000);
        },

        startTimer() {
            this.gameStarted = true;
            const timerInterval = setInterval(() => {
                if (this.timeLeft > 0) {
                    this.timeLeft--;
                    // this.randomX = Math.floor((Math.random() * 400));
                    // this.randomY = Math.floor((Math.random() * 400));
                } else {
                    clearInterval(timerInterval);
                    this.endGame();
                }
            }, 1000);
        },

      generatePoints() {
          const pointTimerInterval = setInterval(() => {
            this.enemyImage = this.getAnimationClass(Math.floor((Math.random() * 6)));
            this.randomY = Math.floor((Math.random() * 390)) + 80;
            this.randomX = Math.floor((Math.random() * 340)) + 40;
            }, 1500);
      },

        registerClick() {
          this.clickCount++;
          // this.randomX = Math.floor((Math.random() * 1000) % 400);
          // this.randomY = Math.floor((Math.random() * 1000) % 400);
          if(this.clickCount >= 10)
            this.endGame();
        },

        endGame() {
            this.gameStarted = false;
            this.gameEnded = true;
            let result = false;
            if (this.clickCount >= 10) {
              result = true;
              this.resultMessage = "Congratulations! You reached " + this.clickCount + " clicks!";
            } else {
              result = false;
              this.resultMessage = "Unfortunately! You got only " + this.clickCount + " clicks.";
            }
            this.$emit('game-finished', result);
        },
      showMiniGameFalse(){
          this.$emit('close', true);
      }
    }
}
</script>

<template>
  <div class="modal">
    <div v-if="!gameStarted && !gameEnded">
            <div class="rules-content">
                <h2>Game rules</h2>
                <p>Catch 10 points in 40 seconds by tapping on them</p>
                <div class="super-little-button" v-if="!gameStarted && !gameCountdownVisible" @click="startGame"><a>Start</a></div>
            </div>
        </div>

        <div v-if="!gameStarted && gameCountdownVisible">
            <h1 id="countdown-number">{{ countdown }}</h1>
        </div>

        <div v-if="gameStarted" id="game" style="height: 400px;">
            <h2>Time left: <span>{{ timeLeft }}</span> sec</h2>
            <h2>Points: <span>{{ clickCount }}/10</span></h2>
            <div :class="enemyImage"
                :style="{position: 'absolute', top: randomX + 'px', left: randomY + 'px'}"
                @click="registerClick"></div>
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

.goblin {
  background-repeat: no-repeat;
  background-size: contain;
            width: 60px;
            height: 60px;
            background-image: url('../assets/Enemies/Goblin/goblin_animation/goblin1.svg');
          }

.dead {
  background-repeat: no-repeat;
  background-size: contain;
            width: 60px;
            height: 60px;
            background-image: url('../assets/Enemies/Dead/dead_animation/dead1.svg');
          }

.demon {
  background-repeat: no-repeat;
  background-size: contain;
            width: 60px;
            height: 60px;
            background-image: url('../assets/Enemies/Demon/demon1.svg');
          }

.flying-eye {
  background-repeat: no-repeat;
  background-size: contain;
            width: 60px;
            height: 60px;
            background-image: url('../assets/Enemies/Flying eye/eye1.svg');
          }

.skeleton {
  background-repeat: no-repeat;
  background-size: contain;
              width: 60px;
              height: 60px;
              background-image: url('../assets/Enemies/Skeleton/skeleton_new1.svg');
            }

.kobold {
  background-repeat: no-repeat;
  background-size: contain;
              width: 60px;
              height: 60px;
              background-image: url('../assets/Enemies/Kobold/kobold-attack1.svg');
            }


</style>