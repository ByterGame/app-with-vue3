<script>
export default {
  data() {
    return {
      words: [
        "monster", "dragon", "skeleton", "creepy", "destructive force",
        "vampire", "zombie", "werewolf", "goblin", "phantom",
        "gorgon", "chupacabra", "minotaur", "gremlin", "ogre",
        "bigfoot", "mermaid", "fairy", "demon", "phantom",
        "centaur", "yeti", "slime", "mummy", "sprite",
        "elemental", "banshee", "ghost", "manticore", "wendigo",
        "siren", "imp", "reaper", "kraken", "sasquatch",
        "nymph", "dryad", "kobald", "battler", "hypogryph",
        "cyclops", "ghoul", "selkie", "jotun", "harpy",
        "ghostly", "lurker", "wraith", "succubus", "belphegor",
        "carnivorous", "kinoko", "rakshasa", "dryder", "huldufolk",
        "kappa", "jackalope", "sukubus", "yurei", "hellhound",
        "sphinx", "kuih", "onryo", "phouka", "skinwalker",
        "yeti", "osmanthus", "aswang", "bhoot", "vodyanoy",
        "chimaera", "dracolich", "duergar", "gorgon", "naga",
        "rakshasa", "charybdis", "yuki-onna", "nuckelavee", "dreamwraith",
        "scylla", "mokele-mbembe", "Baba Yaga", "doppelganger", "kraken"
      ],
      currentWordIndex: 0,
      currentWord: "",
      userInput: "",
      selectedWords: [],
      correctCount: 0,
      incorrectCount: 0,
      timeRemaining: 10,
      gameOver: false,
      gameResult: null,
      gameStarted: false,
      gameCountdownVisible: false,
      countdown: 3,
      timer: null,
    };
  },
  methods: {
    startGame() {
      this.gameStarted = false;
      this.gameOver = false;
      this.gameResult = null;
      this.correctCount = 0;
      this.incorrectCount = 0;
      this.currentWordIndex = 0;
      this.userInput = "";
      this.countdown = 3;
      this.gameCountdownVisible = true;

      // Случайным образом выбираем 5 слов
      this.selectRandomWords();

      const countdownInterval = setInterval(() => {
        if (this.countdown > 0) {
          this.countdown--;
        } else {
          clearInterval(countdownInterval);
          this.gameCountdownVisible = false;
          this.startNewGame();
        }
      }, 1000);
    },
    selectRandomWords() {
      const shuffledWords = this.words.sort(() => 0.5 - Math.random());
      this.selectedWords = shuffledWords.slice(0, 5);
      this.currentWordIndex = 0;
    },
    startNewGame() {
      this.timeRemaining = 10;
      this.nextWord();
      this.startTimer();
      this.gameStarted = true;
      this.$nextTick(() => {
        this.$refs.userInput.focus();
      });
    },
    nextWord() {
      if (this.currentWordIndex < this.selectedWords.length) {
        this.currentWord = this.selectedWords[this.currentWordIndex];
        this.userInput = "";
        this.timeRemaining = 10;
        this.startTimer();
      } else {
        this.gameOver = true;
        clearInterval(this.timer);
        this.checkGameResult();
        this.$emit('game-finished', this.gameResult);
      }
    },
    checkWord() {
      if (this.userInput === this.currentWord) {
        this.correctCount++;
      } else {
        this.incorrectCount++;
      }
      this.currentWordIndex++;
      this.nextWord();
    },
    checkGameResult() {
      if (this.correctCount === 5) {
        this.gameResult = true;
      } else {
        this.gameResult = false;
      }
    },
    startTimer() {
      clearInterval(this.timer);
      this.timer = setInterval(() => {
        this.timeRemaining--;
        if (this.timeRemaining <= 0) {
          clearInterval(this.timer);
          this.incorrectCount++;
          this.checkWord();
          this.nextWord();
        }
      }, 1000);
    },
    showMiniGameFalse() {
      this.$emit('close', true);
    },
    closeGame() {
      this.showMiniGameFalse();
    },
    handleKeyDown(event) {
      if (event.key === "Enter" || event.key === "Escape") {
        if (!this.gameStarted && !this.gameOver && event.key === "Enter") {
          this.startGame();
        } else if (this.gameOver) {
          this.closeGame();
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
    <div v-if="!gameStarted && !gameOver">
      <div class="rules-content">
        <h2>Game rules</h2>
        <p>Write down the same words on time!</p>
        <div class="super-little-button" v-if="!gameStarted && !gameOver && !gameCountdownVisible" @click="startGame">
          <a>Start</a>
        </div>
      </div>
    </div>
    <div v-if="gameCountdownVisible && !gameOver">
      <h1 id="countdown-number">{{ countdown }}</h1>
    </div>
    <div v-if="gameStarted && !gameOver">
      <p>Word: <strong>{{ currentWord }}</strong></p>
      <input ref="userInput" v-model="userInput" @keyup.enter="checkWord" placeholder="Enter a word..." />
      <p>time left: {{ timeRemaining }}</p>
    </div>
    <div v-else-if="gameOver">
      <h2>Result</h2>
      <p>Successfully entered words: {{ correctCount }}/5</p>
      <p v-if="gameResult === true">You win!</p>
      <p v-if="gameResult === false">You lose!</p>
      <div class="little-button" @click="showMiniGameFalse"><a>Close</a></div>
    </div>
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