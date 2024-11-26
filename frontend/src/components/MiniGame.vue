<script>

export default {
  data() {
    return {
      /*gameStarted: false,
      gameCountdownVisible: false,
      countdown: 3,
      timeLeft: 30,
      clickCount: 0,
      gameEnded: false,
      resultMessage: ''*/
      words: ["апельсин", "банан", "киви", "груша", "яблоко"],
      currentWordIndex: 0,
      currentWord: "",
      userInput: "",
      correctCount: 0,
      timeRemaining: 10,
      gameOver: false,
      timer: null,
      countdown: 3,
      gameCountdownVisible: false,
    }
    },
    methods: {
        // startGame() {
        //     this.gameStarted = false;
        //     this.gameEnded = false;
        //     this.clickCount = 0;
        //     this.timeLeft = 30;
        //     this.countdown = 3;
        //     this.gameCountdownVisible = true;
        //
        //     const countdownInterval = setInterval(() => {
        //         if (this.countdown > 0) {
        //             this.countdown--;
        //         } else {
        //             clearInterval(countdownInterval);
        //             this.gameCountdownVisible = false;
        //             this.startTimer();
        //         }
        //     }, 1000);
        // },
        // startTimer() {
        //     this.gameStarted = true;
        //     const timerInterval = setInterval(() => {
        //         if (this.timeLeft > 0) {
        //             this.timeLeft--;
        //         } else {
        //             clearInterval(timerInterval);
        //             this.endGame();
        //         }
        //     }, 1000);
        // },
        startGame() {
            this.gameOver = false;
            this.correctCount = 0;
            this.currentWordIndex = 0;
            this.timeRemaining = 10;
            this.userInput = "";
            this.nextWord();
            this.startTimer();
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
          this.timer = setInterval(() => {
            this.timeRemaining--;
            if (this.timeRemaining <= 0) {
              clearInterval(this.timer);
              this.currentWordIndex++; // Переходим к следующему слову
              this.nextWord(); // Загружаем следующее слово
            }
          }, 1000);
        },
        nextWord() {
          if (this.currentWordIndex < this.words.length) {
            this.currentWord = this.words[this.currentWordIndex];
            this.userInput = "";
            this.timeRemaining = 10; // Сбрасываем время
          } else {
            this.gameOver = true; // Игра окончена
            clearInterval(this.timer); // Остановить таймер
          }
        },
        checkWord() {
          if (this.userInput === this.currentWord) {
            this.correctCount++;
          } else {
            this.incorrectCount++;
          }
          this.currentWordIndex++; // Переходим к следующему слову
          this.nextWord(); // Загружаем следующее слово
        },

        // registerClick() {
        //     this.clickCount++;
        // },
        // endGame() {
        //     this.gameStarted = false;
        //     this.gameEnded = true;
        //     let result = false;
        //     if (this.clickCount > 100) {
        //       result = true;
        //       this.resultMessage = "Поздравляем! Вы набрали " + this.clickCount + " кликов!";
        //     } else {
        //       result = false;
        //       this.resultMessage = "Вот и все! Вы набрали только " + this.clickCount + " кликов.";
        //     }
        //     this.$emit('game-finished', result);
        // },
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
                <h2>Правила игры</h2>
<!--                <p>Нажмите на кнопку более 100 раз за 30 секунд!</p>-->
                    <p>Запиши такие же слова на время!</p>
                <div class="super-little-button" v-if="!gameStarted && !gameCountdownVisible" @click="startGame"><a>Старт</a></div>
            </div>
        </div>

<!--        <div v-if="!gameStarted && gameCountdownVisible">-->
<!--            <h1 id="countdown-number">{{ countdown }}</h1>-->
<!--        </div>-->
        <div v-if="!startGame && gameCountdownVisible">
            <h1 id="countdown-number">{{ countdown }}</h1>
        </div>

<!--        <div v-if="gameStarted" id="game">-->
<!--            <h2>Время: <span>{{ timeLeft }}</span> секунд</h2>-->
<!--            <h2>Клики: <span>{{ clickCount }}</span></h2>-->
<!--            <div class="little-button" @click="registerClick"><a>Нажми меня!</a></div>-->
<!--        </div>-->
        <div v-if="!gameOver">
          <p>Слово: <strong>{{ currentWord }}</strong></p>
          <input v-model="userInput" @keyup.enter="checkWord" placeholder="Введите слово..." />
          <p>Осталось времени: {{ timeRemaining }} сек</p>
        </div>
        <div v-else>
          <h2>Результаты</h2>
          <p>Успешно введено слов: {{ correctCount }}/5</p>
          <div class="little-button" @click="showMiniGameFalse"><a>Close</a></div>
        </div>

<!--    <h2 v-if="gameEnded">{{ resultMessage }}<div class="little-button" @click="showMiniGameFalse"><a>Close</a></div></h2>-->
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