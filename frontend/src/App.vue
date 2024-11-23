<template>
  <RegistrationModal :userLoggedIn="userLoggedIn"
      v-if="!userLoggedIn"  @login="handleLogin"/>
<div v-if="!userLoggedIn" class="overlay"></div>
  <div class="clicker-section">
<p class="balance">Balance: $ {{balance}}</p>
<div class="upgrade-button" @click="openUpgradeModal" id="open-upgrade"><div class="little-button" id="open-upgrade"><a>Upgrade</a></div></div>
<div class="container">
    <div class="button" @click="addMoney"><a>Click Me!</a></div>
</div>
</div>
<div class="animation-section">
    <div class="input-container">
        <div class="little-button" @click="openEnemyModal" id="open-enemy"><a>Choose Enemy</a></div>
        <div class="bet-row">
            <span>Win Rate: {{(winRate * 100).toFixed(1)}}%</span>
            <input type="number" v-model="bet" min="0" v-bind:max="balance">
          <span>Win Odds: {{(winOdd).toFixed(1)}}</span>
        </div>
        <div class="little-button" @click="makeBet"><a>Start Fight</a></div>
    </div>
  <div class="fight-row">
    <div class="animation-placeholder" style=" width: 300px;  height: 300px; margin-top: 80px; "></div>
    <div :id="'enemy-' + chosenEnemyId" :class="'animation-placeholder ' + getReverseStaticAnimationClass(chosenEnemyId)"
         style=" margin-top: 80px; "></div>
  </div>
</div>

<div v-if="isEnemyModalVisible"  class="modal" id="enemy-modal"
     style="width: 600px;
     height: 80%;
     overflow-y: auto;">
    <h2>Choose Your Enemy</h2>
      <div class="modal-content" v-for="enemy in enemies" :key="enemy.id">
          <div class="enemy-container" style= "width: 600px; height: 200px; overflow: hidden;">
            <div :id="'enemy-' + enemy.id" :class="'animation-placeholder ' + getAnimationClass(enemy.id)" style=" width: 300px;  height: 100%; "></div>
            <p class="enemy-text-container" style=" width: 500px ">
              <span class="enemy-text">Enemy: {{ enemy.name }}</span>
              <span class="enemy-text">Speed: {{ enemy.speed }}</span>
              <span class="enemy-text">Strength: {{ enemy.strength }}</span>
              <span class="enemy-text">Durability: {{ enemy.durability }}</span>
          </p>
        </div>
        <div class="super-little-button" @click="changeEnemy(enemy.id)"  style="position: relative; left: 50%; transform: translate(-50%, 0);"><a>Select</a></div>
      </div>
</div>

<div v-if="isUpgradeModalVisible" class="modal" id="upgrade-modal">
    <h2>Upgrade Your Character</h2>
    <div class="modal-content">
        <div class="column">
          <p>Speed: {{character.speed}} </p><div class="super-little-button" @click="upgrade('speed')"><div class="row"><a>Upgrade</a><p>{{character.speed * priceList.speed}}$</p></div></div></div>
        <p>Strength: {{character.strength}} </p><div class="super-little-button"><div class="row"><a @click="upgrade('strength')">Upgrade</a><p>{{character.strength * priceList.strength}}$</p></div></div>
        <p>Durability: {{character.durability}} </p><div class="super-little-button"><div class="row"><a @click="upgrade('durability')">Upgrade</a><p>{{character.durability * priceList.durability}}$</p></div></div>
    </div>
</div>
<div v-if="isModalVisible" class="overlay" @click="closeModals" id="overlay"></div>
</template>


<script>
import RegistrationModal from "@/components/RegistrationModal.vue";
export default {
  data() {
    return{
      balance: 10000,
      bet: 0,
      userLoggedIn: true,
      isEnemyModalVisible: false,
      isUpgradeModalVisible: false,
      chosenEnemyId: 1,
      winRate: 0,
      winOdd: 1,
      priceList:{
        speed: 50,
        strength: 75,
        durability: 60,
      },
      enemies:[
        {id: 1, name: 'Goblin', speed: 3, strength: 8, durability: 7,},
        {id: 2, name: 'Dead', speed: 7, strength: 5, durability: 5},
        {id: 3, name: 'Flying eye', speed: 4, strength: 9, durability: 6},
        {id: 4, name: 'Skeleton', speed: 9, strength: 5, durability: 5},
        {id: 5, name: 'Demon', speed: 5, strength: 11, durability: 3},
        {id: 6, name: 'Kobold', speed: 7, strength: 3, durability: 9}
      ],
      character:{
          speed: 1,
          strength: 1,
          durability: 1,
        }
      }
    },
  mounted(){
    this.calculateWinRate();
    this.calculateWinOdd();
  },

  computed: {
    isModalVisible() {
      return this.isEnemyModalVisible || this.isUpgradeModalVisible;
    }
  },

  methods: {
    addMoney(){
      this.balance++;
    },

    openEnemyModal() {
      this.isEnemyModalVisible = true;
    },

    openUpgradeModal() {
      this.isUpgradeModalVisible = true;
    },

    closeModals() {
      this.isEnemyModalVisible = false;
      this.isUpgradeModalVisible = false;
    },

    makeBet(){
      if(this.bet > 0 && this.bet <= this.balance){
        this.balance -= this.bet;
        this.bet = 0;
      }
      else if(this.bet > this.balance){
        this.bet = this.balance;
      }
    },
    getAnimationClass(enemyId) {
      switch (enemyId) {
        case 1:
          return 'goblin-animation';
        case 3:
          return 'flying-eye-animation';
        case 2:
          return 'dead-animation';
        case 4:
          return 'skeleton-animation';
        case 5:
          return 'demon-animation';
        case 6:
          return 'kobold-animation';
        default:
          return '';
      }
    },
    getAttackAnimationClass(enemyId) {
      switch (enemyId) {
        case 1:
          return 'goblin_reverse-animation';
        case 3:
          return 'flying-eye-reverse-static-animation';
        case 2:
          return 'dead-reverse-animation';
        case 4:
          return 'skeleton-reverse-animation';
        case 5:
          return 'demon-animation';
        case 6:
          return 'kobold-reverse-animation';
        default:
          return '';
      }
    },
    getStaticAnimationClass(enemyId) {
      switch (enemyId) {
        case 1:
          return 'goblin_static-animation';
        case 3:
          return 'flying-eye-static-animation';
        case 2:
          return 'dead-animation';
        case 4:
          return 'skeleton-animation';
        case 5:
          return 'demon-animation';
        default:
          return '';
      }
    },
    getReverseStaticAnimationClass(enemyId) {
      switch (enemyId) {
        case 1:
          return 'goblin_reverse_static-animation';
        case 3:
          return 'flying-eye-reverse-static-animation';
        case 2:
          return 'dead-reverse-static-animation';
        case 4:
          return 'skeleton-reverse-static-animation';
        case 5:
          return 'demon-animation';
        case 6:
          return 'kobold-static-animation';
        default:
          return '';
      }
    },
    handleLogin(value) {
      this.userLoggedIn = value;
    },

    upgrade(characteristic){
      const sum = this.character[characteristic] * this.priceList[characteristic];
      if(this.balance >= sum){
        this.balance -= sum;
        this.character[characteristic] ++;
      }
      this.calculateWinRate();
    },

    calculateWinRate() {
    const enemy = this.enemies.find(e => e.id === this.chosenEnemyId);

    if (!enemy) return 0;
    let score = 0;

    const characterSum = this.character.speed * 0.4 + this.character.strength * 0.8 + this.character.durability * 0.5;
    const enemySum = enemy.speed * 0.4 + enemy.durability * 0.5 + enemy.strength * 0.8;
    score = 0.5 * (characterSum / enemySum);

    this.winRate = Math.min(score, 0.8);
    this.calculateWinOdd();
  },
    calculateWinOdd(){
      this.winOdd = Math.max(3-this.winRate*3.95, 1.1);
    },

  changeEnemy(id) {
    this.chosenEnemyId = id;
    this.calculateWinRate();
  },
  },
  components: {
    RegistrationModal
  },
}

</script>

<style>
        body {
            margin: 0;
            font-family: 'Press Start 2P', sans-serif;
            background-image: url("assets/background2.png");
            background-repeat: repeat-x;
            background-size: cover;
            background-position: bottom center;
            color: #d6c6dd;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            height: 100vh;
            overflow: hidden;
            user-select: none;
        }
        .clicker-section{
          top: 0;
          left: 0;
          width: 100%;
          height: 40%;
          align-content: center;
          justify-content: space-between;
        }

        .balance {
            text-align: center;
            position: absolute;
            top: 20px;
            right: 20px;
        }

        .upgrade-button {
            text-align: center;
            position: absolute;
            top: 20px;
            left: 20px;
        }

        .container {
            text-align: center;
            width: 100%;
            margin-top: 70px;
        }


          .button{
              text-align:center;
          background-color: transparent;
            font-family: 'Press Start 2P', sans-serif;
          position:relative;
          display:inline-block;
          margin:20px;
              cursor: pointer;
        }

        .button a{
          color: #d6c6dd;
          font-family: 'Press Start 2P', sans-serif;
          /*font-weight:bold;*/
          font-size:24px;
          text-align: center;
          text-decoration:none;
          background-color:#6c3282;
          display:block;
          position:relative;
          padding:25px 30px;

          -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
          text-shadow: 0px 1px 0px #000;
          filter: dropshadow(color=#000, offx=0px, offy=1px);

          -webkit-box-shadow:inset 0 1px 0 #d6c6dd, 0 10px 0 #601e7c;
          -moz-box-shadow:inset 0 1px 0 #d6c6dd, 0 10px 0 #601e7c;
          box-shadow:inset 0 1px 0 #d6c6dd, 0 10px 0 #2F0A3D;

          -webkit-border-radius: 5px;
          -moz-border-radius: 5px;
          border-radius: 5px;
        }

        .button a:hover{
            background-color: #601e7c;
        }

        .button a:active{
          top:10px;
          background-color:#601e7c;

          -webkit-box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
          -moz-box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
          box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
        }

        .button:after{
          content:"";
          height:100%;
          width:100%;
          padding:4px;
          position: absolute;
          bottom:-15px;
          left:-4px;
          z-index:-1;
          background-color:#2F0A3D;
          -webkit-border-radius: 5px;
          -moz-border-radius: 5px;
          border-radius: 5px;
        }


                .little-button{
              text-align:center;
          background-color: transparent;
            font-family: 'Press Start 2P', sans-serif;
          position:relative;
          display:inline-block;
          margin:20px;
              cursor: pointer;
        }

        .little-button a{
          color: #d6c6dd;
          font-family: 'Press Start 2P', sans-serif;
          /* font-weight:bold; */
          font-size:14px;
          text-align: center;
          text-decoration:none;
          background-color:#6c3282;
          display:block;
            position:relative;
          padding:10px 15px;

          -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
          text-shadow: 0px 1px 0px #000;
          filter: dropshadow(color=#000, offx=0px, offy=1px);

          -webkit-box-shadow:inset 0 1px 0 #d6c6dd, 0 5px 0 #601e7c;
          -moz-box-shadow:inset 0 1px 0 #d6c6dd, 0 5px 0 #601e7c;
          box-shadow:inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;

          -webkit-border-radius: 3px;
          -moz-border-radius: 3px;
          border-radius: 3px;
        }

        .little-button a:hover{
            background-color: #601e7c;
        }

        .little-button a:active{
          top:8px;
          background-color:#601e7c;

          -webkit-box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
          -moz-box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
          box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
        }

        .little-button:after{
          content:"";
          height:100%;
          width:100%;
          padding:4px;
          position: absolute;
          bottom:-10px;
          left:-4px;
          z-index:-1;
          background-color:#2F0A3D;
          -webkit-border-radius: 3px;
          -moz-border-radius: 3px;
          border-radius: 3px;
        }

        .super-little-button{
              text-align:center;
          background-color: transparent;
            font-family: 'Press Start 2P', sans-serif;
          position:relative;
          display:inline-block;
          margin:5px;
              cursor: pointer;
        }

        .super-little-button a{
          color: #6c3282;
          font-family: 'Press Start 2P', sans-serif;
          /* font-weight:bold; */
          font-size:10px;
          text-align: center;
          text-decoration:none;
          background-color:#d6c6dd;
          display:block;
          position:relative;
          padding: 10px 12px;

          -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
          text-shadow: 0px 0px 0px #000;
          filter: dropshadow(color=#000, offx=0px, offy=1px);

          -webkit-box-shadow:inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;
          -moz-box-shadow:inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;
          box-shadow:inset 0 1px 0 #d6c6dd, 0 5px 0 #2F0A3D;

          -webkit-border-radius: 3px;
          -moz-border-radius: 3px;
          border-radius: 3px;
        }

        .super-little-button a:hover{
            background-color: #601e7c;
            color: #d6c6dd;
        }

        .super-little-button a:active{
          top:8px;
          background-color:#2F0A3D;

          -webkit-box-shadow:inset 0 1px 0 #2F0A3D, inset 0 -2px 0 #d6c6dd;
          -moz-box-shadow:inset 0 1px 0 #2F0A3D, inset 0 -2px 0 #d6c6dd;
          box-shadow:inset 0 1px 0 #2F0A3D, inset 0 -2px 0 #d6c6dd;
        }

        .super-little-button:after{
          content:"";
          height:100%;
          width:100%;
          padding:2px;
          position: absolute;
          bottom:-5px;
          left:-2px;
          z-index:-1;
          background-color:#2F0A3D;
          -webkit-border-radius: 2px;
          -moz-border-radius: 2px;
          border-radius: 2px;
        }

        .fight-row{
          display: flex;
          flex-direction: row;
          gap: 20px;
          align-items: center;
          justify-content: center;
        }

        .animation-placeholder {
          bottom: 50px;
          background-image: url('assets/Adventurer/adventurer-idle-00.svg'); /* Первый кадр */
          background-size: contain;
          background-position: center;
          background-repeat: no-repeat;
          animation: loop-animation 1.2s steps(6) infinite;
        }

        @keyframes loop-animation {
          0% {background-image: url('assets/Adventurer/adventurer-idle-00.svg'); }
          16% {background-image: url('assets/Adventurer/adventurer-idle-01.svg'); }
          33% {background-image: url('assets/Adventurer/adventurer-idle-02.svg');}
          50% {background-image: url('assets/Adventurer/adventurer-idle-03.svg');}
          66%{background-image: url('assets/Adventurer/adventurer-idle-02.svg');}
          83% {background-image: url('assets/Adventurer/adventurer-idle-01.svg');}
          100%{background-image: url('assets/Adventurer/adventurer-idle-00.svg');}
        }

        .goblin-animation {
            width: 300px;
            height: 300px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Goblin/goblin_animation/goblin1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: goblin-loop-animation 1.5s steps(13) infinite;
          }

          @keyframes goblin-loop-animation {
            0% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin1.svg'); }
            8.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin2.svg'); }
            16.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin3.svg'); }
            25% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin4.svg'); }
            33.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin5.svg'); }
            41.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin6.svg'); }
            50% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin7.svg'); }
            58.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin8.svg'); }
            66.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin9.svg'); }
            75% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin10.svg'); }
            83.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin11.svg'); }
            91.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin12.svg'); }
            100% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin1.svg'); }
          }
          .goblin_static-animation {
            width: 300px;
            height: 300px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Goblin/goblin_animation/goblin1.svg'); /* Первый кадр */
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: goblin_static-loop-animation 1.1s steps(7) infinite; /* Анимация */
          }

          @keyframes goblin_static-loop-animation {
            0% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin1.svg'); }
            16.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin2.svg'); }
            33.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin3.svg'); }
            50% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin4.svg'); }
            66.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin5.svg'); }
            83.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin6.svg'); }
            100% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin1.svg'); } /* Возврат к первому кадру */
          }
          .goblin_reverse-animation {
            width: 300px;
            height: 300px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse1.svg'); /* Первый кадр */
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: goblin_reverse-loop-animation 1.5s steps(13) infinite; /* Анимация */
          }

          @keyframes goblin_reverse-loop-animation {
            0% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse1.svg'); }
            8.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse2.svg'); }
            16.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse3.svg'); }
            25% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse4.svg'); }
            33.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse5.svg'); }
            41.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse6.svg'); }
            50% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse7.svg'); }
            58.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse8.svg'); }
            66.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse9.svg'); }
            75% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse10.svg'); }
            83.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse11.svg'); }
            91.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse12.svg'); }
            100% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse1.svg'); }
          }
          .goblin_reverse_static-animation {
            width: 300px;
            height: 300px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static1.svg'); /* Первый кадр */
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: goblin_reverse_static-loop-animation 1.1s steps(7) infinite; /* Анимация */
          }

          @keyframes goblin_reverse_static-loop-animation {
            0% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static1.svg'); }
            16.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static2.svg'); }
            33.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static3.svg'); }
            50% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static4.svg'); }
            66.67% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static5.svg'); }
            83.33% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static6.svg'); }
            100% { background-image: url('assets/Enemies/Goblin/goblin_animation/goblin_reverse_static1.svg'); } /* Возврат к первому кадру */
          }

          .dead-animation {
            width: 300px;
            height: 300px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Dead/dead_animation/dead1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: dead-loop-animation 1.2s steps(9) infinite;
          }

          @keyframes dead-loop-animation {
            0% { background-image: url('assets/Enemies/Dead/dead_animation/dead1.svg'); }
            12.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead2.svg'); }
            25% { background-image: url('assets/Enemies/Dead/dead_animation/dead3.svg'); }
            37.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead4.svg'); }
            50% { background-image: url('assets/Enemies/Dead/dead_animation/dead5.svg'); }
            62.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead6.svg'); }
            75% { background-image: url('assets/Enemies/Dead/dead_animation/dead7.svg'); }
            87.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead8.svg'); }
            100% { background-image: url('assets/Enemies/Dead/dead_animation/dead1.svg'); }
          }
          .dead-reverse-animation {
            width: 300px;
            height: 300px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: dead-reverse-loop-animation 1.2s steps(9) infinite;
          }

          @keyframes dead-reverse-loop-animation {
            0% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse1.svg'); }
            12.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse2.svg'); }
            25% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse3.svg'); }
            37.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse4.svg'); }
            50% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse5.svg'); }
            62.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse6.svg'); }
            75% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse7.svg'); }
            87.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse8.svg'); }
            100% { background-image: url('assets/Enemies/Dead/dead_animation/dead-reverse1.svg'); }
          }
          .dead-reverse-static-animation {
            width: 300px;
            height: 300px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: dead-reverse-static-animation-loop-animation 1.2s steps(9) infinite;
          }

          @keyframes dead-reverse-static-animation-loop-animation {
            0% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse1.svg'); }
            12.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse2.svg'); }
            25% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse3.svg'); }
            37.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse4.svg'); }
            50% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse5.svg'); }
            62.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse6.svg'); }
            75% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse7.svg'); }
            87.5% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse8.svg'); }
            100% { background-image: url('assets/Enemies/Dead/dead_animation/dead-static-reverse1.svg'); }
          }
          .demon-animation {
            width: 250px;
            height: 250px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Demon/demon1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: demon-loop-animation 1.2s steps(9) infinite;
          }

          @keyframes demon-loop-animation {
            0% { background-image: url('assets/Enemies/Demon/demon1.svg'); }
            12.5% { background-image: url('assets/Enemies/Demon/demon2.svg'); }
            25% { background-image: url('assets/Enemies/Demon/demon3.svg'); }
            37.5% { background-image: url('assets/Enemies/Demon/demon4.svg'); }
            50% { background-image: url('assets/Enemies/Demon/demon5.svg'); }
            62.5% { background-image: url('assets/Enemies/Demon/demon6.svg'); }
            75% { background-image: url('assets/Enemies/Demon/demon7.svg'); }
            87.5% { background-image: url('assets/Enemies/Demon/demon8.svg'); }
            100% { background-image: url('assets/Enemies/Demon/demon1.svg'); }
          }
          .flying-eye-animation {
            width: 200px;
            height: 200px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Flying eye/eye1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: flying-eye-loop-animation 1.1s steps(7) infinite;
          }

          @keyframes flying-eye-loop-animation {
            0% { background-image: url('assets/Enemies/Flying eye/eye1.svg'); }
            16.67% { background-image: url('assets/Enemies/Flying eye/eye2.svg'); }
            33.33% { background-image: url('assets/Enemies/Flying eye/eye3.svg'); }
            50% { background-image: url('assets/Enemies/Flying eye/eye4.svg'); }
            66.67% { background-image: url('assets/Enemies/Flying eye/eye5.svg'); }
            83.33% { background-image: url('assets/Enemies/Flying eye/eye6.svg'); }
            100% { background-image: url('assets/Enemies/Flying eye/eye1.svg'); }
          }
          .flying-eye-static-animation {
            width: 200px;
            height: 200px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Flying eye/eye5.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: flying-eye-static-loop-animation 1.1s steps(7) infinite;
          }

          @keyframes flying-eye-static-loop-animation {
            0% { background-image: url('assets/Enemies/Flying eye/eye5.svg'); }
            25% { background-image: url('assets/Enemies/Flying eye/eye6.svg'); transform: translate(0, 5%);}
            50% { background-image: url('assets/Enemies/Flying eye/eye5.svg'); transform: translate(0, 10%);}
            75% { background-image: url('assets/Enemies/Flying eye/eye6.svg'); transform: translate(0, 5%);}
            100% { background-image: url('assets/Enemies/Flying eye/eye5.svg'); transform: translate(0, 0%);}
          }
          .flying-eye-reverse-static-animation {
            width: 200px;
            height: 200px;
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Flying eye/eye-reverse-stat1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: flying-eye-reverse-static-animation 1.1s steps(7) infinite;
          }

          @keyframes flying-eye-reverse-static-animation {
            0% { background-image: url('assets/Enemies/Flying eye/eye-reverse-stat2.svg'); }
            25% { background-image: url('assets/Enemies/Flying eye/eye-reverse-stat1.svg'); transform: translate(0, 5%);}
            50% { background-image: url('assets/Enemies/Flying eye/eye-reverse-stat2.svg'); transform: translate(0, 10%);}
            75% { background-image: url('assets/Enemies/Flying eye/eye-reverse-stat1.svg'); transform: translate(0, 5%);}
            100% { background-image: url('assets/Enemies/Flying eye/eye-reverse-stat2.svg'); transform: translate(0, 0%);}
          }
          .skeleton-animation {
              width: 250px;
              height: 250px;
              bottom: 50px;
              margin: 10px auto;
              background-image: url('assets/Enemies/Skeleton/skeleton_new1.svg');
              background-size: contain;
              background-position: center;
              background-repeat: no-repeat;
              animation: skeleton-loop-animation 1.8s steps(7) infinite;
            }

          @keyframes skeleton-loop-animation {
              0% { background-image: url('assets/Enemies/Skeleton/skeleton_new1.svg'); }
              5.56% { background-image: url('assets/Enemies/Skeleton/skeleton_new2.svg'); }
              11.11% { background-image: url('assets/Enemies/Skeleton/skeleton_new3.svg'); }
              16.67% { background-image: url('assets/Enemies/Skeleton/skeleton_new4.svg'); }
              22.22% { background-image: url('assets/Enemies/Skeleton/skeleton_new5.svg'); }
              27.78% { background-image: url('assets/Enemies/Skeleton/skeleton_new6.svg'); }
              33.33% { background-image: url('assets/Enemies/Skeleton/skeleton_new7.svg'); }
              38.89% { background-image: url('assets/Enemies/Skeleton/skeleton_new8.svg'); }
              44.44% { background-image: url('assets/Enemies/Skeleton/skeleton_new9.svg'); }
              50% { background-image: url('assets/Enemies/Skeleton/skeleton_new10.svg'); }
              55.56% { background-image: url('assets/Enemies/Skeleton/skeleton_new11.svg'); }
              61.11% { background-image: url('assets/Enemies/Skeleton/skeleton_new12.svg'); }
              66.67% { background-image: url('assets/Enemies/Skeleton/skeleton_new13.svg'); }
              72.22% { background-image: url('assets/Enemies/Skeleton/skeleton_new14.svg'); }
              77.78% { background-image: url('assets/Enemies/Skeleton/skeleton_new15.svg'); }
              83.33% { background-image: url('assets/Enemies/Skeleton/skeleton_new16.svg'); }
              88.89% { background-image: url('assets/Enemies/Skeleton/skeleton_new17.svg'); }
              94.44% { background-image: url('assets/Enemies/Skeleton/skeleton_new18.svg'); }
              100% { background-image: url('assets/Enemies/Skeleton/skeleton_new1.svg'); }
          }
          .skeleton-reverse-animation {
              width: 250px;
              height: 250px;
              bottom: 50px;
              margin: 10px auto;
              background-image: url('assets/Enemies/Skeleton/skeleton-reverse1.svg');
              background-size: contain;
              background-position: center;
              background-repeat: no-repeat;
              animation: skeleton-reverse-loop-animation 1.8s steps(7) infinite;
            }

          @keyframes skeleton-reverse-loop-animation {
              0% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse1.svg'); }
              5.56% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse2.svg'); }
              11.11% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse3.svg'); }
              16.67% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse4.svg'); }
              22.22% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse5.svg'); }
              27.78% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse6.svg'); }
              33.33% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse7.svg'); }
              38.89% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse8.svg'); }
              44.44% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse9.svg'); }
              50% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse10.svg'); }
              55.56% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse11.svg'); }
              61.11% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse12.svg'); }
              66.67% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse13.svg'); }
              72.22% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse14.svg'); }
              77.78% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse15.svg'); }
              83.33% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse16.svg'); }
              88.89% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse17.svg'); }
              94.44% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse18.svg'); }
              100% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse1.svg'); }
          }
          .skeleton-reverse-static-animation {
              width: 230px;
              height: 230px;
              bottom: 50px;
              margin: 10px auto;
              background-image: url('assets/Enemies/Skeleton/skeleton-reverse-static1.svg');
              background-size: contain;
              background-position: center;
              background-repeat: no-repeat;
              animation: skeleton-reverse-static-animation-loop-animation 0.7s steps(7) infinite;
            }

          @keyframes skeleton-reverse-static-animation-loop-animation {
            0% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse-static1.svg'); }
            20% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse-static2.svg'); }
            40% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse-static3.svg'); }
            60% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse-static4.svg'); }
            80% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse-static5.svg'); }
            100% { background-image: url('assets/Enemies/Skeleton/skeleton-reverse-static1.svg'); }
        }
        .kobold-animation {
              width: 230px;
              height: 230px;
              bottom: 50px;
              margin: 10px auto;
              background-image: url('assets/Enemies/Kobold/kobold-attack1.svg');
              background-size: contain;
              background-position: center;
              background-repeat: no-repeat;
              animation: kobold-animation-loop-animation 0.8s steps(7) infinite;
            }

          @keyframes kobold-animation-loop-animation {
            0% { background-image: url('assets/Enemies/Kobold/kobold-attack1.svg'); }
            20% { background-image: url('assets/Enemies/Kobold/kobold-attack2.svg'); }
            40% { background-image: url('assets/Enemies/Kobold/kobold-attack3.svg'); }
            60% { background-image: url('assets/Enemies/Kobold/kobold-attack4.svg'); }
            80% { background-image: url('assets/Enemies/Kobold/kobold-attack5.svg'); }
            100% { background-image: url('assets/Enemies/Kobold/kobold-attack1.svg'); }
        }
          .kobold-reverse-animation {
              width: 300px;
              height: 300px;
              bottom: 50px;
              margin: 10px auto;
              background-image: url('assets/Enemies/Kobold/kobold-attack-reverse1.svg');
              background-size: contain;
              background-position: center;
              background-repeat: no-repeat;
              animation: kobold-reverse-animation-loop-animation 0.8s steps(7) infinite;
            }

          @keyframes kobold-reverse-animation-loop-animation {
            0% { background-image: url('assets/Enemies/Kobold/kobold-attack-reverse1.svg'); }
            20% { background-image: url('assets/Enemies/Kobold/kobold-attack-reverse2.svg'); }
            40% { background-image: url('assets/Enemies/Kobold/kobold-attack-reverse3.svg'); }
            60% { background-image: url('assets/Enemies/Kobold/kobold-attack-reverse4.svg'); }
            80% { background-image: url('assets/Enemies/Kobold/kobold-attack-reverse5.svg'); }
            100% { background-image: url('assets/Enemies/Kobold/kobold-attack-reverse1.svg'); }
        }
          .kobold-static-animation {
              width: 300px;
              height: 300px;
              bottom: 50px;
              margin: 10px auto;
              background-image: url('assets/Enemies/Kobold/kobold-static1.svg');
              background-size: contain;
              background-position: center;
              background-repeat: no-repeat;
              animation: kobold-static-animation-loop-animation 1.2s steps(7) infinite;
            }

          @keyframes kobold-static-animation-loop-animation {
            0% { background-image: url('assets/Enemies/Kobold/kobold-static1.svg'); }
            20% { background-image: url('assets/Enemies/Kobold/kobold-static2.svg'); }
            40% { background-image: url('assets/Enemies/Kobold/kobold-static3.svg'); }
            60% { background-image: url('assets/Enemies/Kobold/kobold-static4.svg'); }
            80% { background-image: url('assets/Enemies/Kobold/kobold-static5.svg'); }
            100% { background-image: url('assets/Enemies/Kobold/kobold-static1.svg'); }
        }
        .bomb-animation {
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Goblin/bomb_animation/bomb1.svg');
            background-size: cover;
            background-position: center;
            animation: bomb-animation 1.2s steps(17) infinite;
          }

          @keyframes bomb-animation {
            0% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb1.svg'); }
            6.25% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb2.svg'); }
            12.5% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb3.svg'); }
            18.75% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb4.svg'); }
            25% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb5.svg'); }
            31.25% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb6.svg'); }
            37.5% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb7.svg'); }
            43.75% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb8.svg'); }
            50% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb9.svg'); }
            56.25% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb10.svg'); }
            62.5% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb11.svg'); }
            68.75% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb12.svg'); }
            75% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb13.svg'); }
            81.25% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb14.svg'); }
            87.5% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb15.svg'); }
            93.75% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb16.svg'); }
            100% { background-image: url('assets/Enemies/Goblin/bomb_animation/bomb17.svg'); }
          }

        .input-container {
            top: 10px;
            margin: 30px auto;
            text-align: center;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            width: 90%;
            align-items: center;
            color: #d6c6dd;
        }

        .input-container span {
            display: block;
            margin-bottom: 10px;

        }

        .input-container input {
            width: 120px;
            padding: 15px;
            border: 2px solid #d6c6dd;
            background: #6c3282;
            color: #d6c6dd;
            font-family: 'Press Start 2P', sans-serif;
            font-size: 14px;
            text-align: center;
            -webkit-border-radius: 5px;
            -moz-border-radius: 5px;
            border-radius: 5px;
        }

        .bet-row{
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            gap: 20px;
        }

        .animation-section {
            background: transparent;
            border: 0px solid #e0c3fc;
            width: 100%;
            height: 60%;
            bottom: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .modal {
          position: fixed;
          top: 50%;
          left: 50%;
          display: block;
          transform: translate(-50%, -50%);
          background: #2d013d;
          opacity: 0.95;
          padding: 20px;
          border: 4px solid #e0c3fc;
          z-index: 10;
      }
        .enemy-container {
          display: flex;
          align-items: center;
          justify-content: center;
      }

        .modal h2 {
            font-size: 14px;
            font-family: 'Press Start 2P', sans-serif;
            text-align: center
        }

        .animation-placeholder {
            margin-left: 45px;
        }

        .enemy-text {
            display: block;
            margin-bottom: 10px;
            margin-left: 150px;
        }
        .enemy-text-container{
          text-align: left;
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

        .column{
          display: flex;
          flex-direction: column;
        }

        .row{
          display: flex;
          flex-direction: row;
          gap: 20px;
          height: 30px;
          align-items: center;
        }
    </style>