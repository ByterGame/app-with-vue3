<template>
  <RegistrationModal :userLoggedIn="userLoggedIn"
      v-if="!userLoggedIn"  @login="handleLogin"/>
<div v-if="!userLoggedIn" class="overlay"></div>
  <div class="clicker-section">
<p class="balance">Balance: $ {{balance.toFixed(0)}}</p>
<div class="upgrade-button" @click="openUpgradeModal" id="open-upgrade"><div class="little-button" id="open-upgrade"><a>Upgrade</a></div></div>
<div class="container">
    <div class="button" @click="addMoney"><a>Click Me!</a></div>
</div>
</div>
<div class="animation-section">
    <div class="input-container">
        <div class="little-button" @click="openEnemyModal" id="open-enemy" :class="{'disabled': fightIsOn}"
  :style="{ pointerEvents: fightIsOn ? 'none' : 'auto' }"><a>Choose Enemy</a></div>
        <div class="bet-row">
            <span>Win Rate: {{(winRate * 100).toFixed(1)}}%</span>
            <input type="number" v-model="bet" min="10" v-bind:max="balance">
          <span>Win Odds: {{winOdd.toFixed(1)}}</span>
        </div>
        <div class="little-button" @click="makeBet" :class="{'disabled': fightIsOn}"
  :style="{ pointerEvents: fightIsOn ? 'none' : 'auto' }"><a>Start Fight</a></div>
    </div>
  <div class="fight-row">
    <div class="animation-placeholder" :class="{'protagonist-death': protagonistStatus.dead, 'protagonist-run': protagonistStatus.run, 'protagonist-attack1': protagonistStatus.attack1 }" id="protagonist"></div>
    <div :id="'enemy-' + chosenEnemyId" :class="'animation-placeholder ' + getAnimationClass(chosenEnemyId)"></div>
  </div>
</div>

<div v-if="isEnemyModalVisible"  class="modal" id="enemy-modal"
     style="width: 600px;
     height: 80%;
     overflow-y: auto;">
    <h2>Choose Your Enemy</h2>
      <div class="modal-content" v-for="enemy in enemies" :key="enemy.id">
          <div class="enemy-container" style= "width: 600px; height: 200px; overflow: hidden;">
            <div :id="'enemy-' + enemy.id" :class="'animation-placeholder ' + getAnimationClass(enemy.id)" style=" height: 100% "></div>
            <p class="enemy-text-container" style=" width: 500px ">
              <span class="enemy-text">Enemy: {{ enemy.name }}</span>
              <span class="enemy-text">Speed: {{ enemy.speed }}</span>
              <span class="enemy-text">Strength: {{ enemy.strength }}</span>
              <span class="enemy-text">Durability: {{ enemy.durability }}</span>
          </p>
        </div>
        <div class="super-little-button" @click="changeEnemy(enemy.id)" style="position: relative; left: 50%; transform: translate(-50%, 0);"><a>Select</a></div>
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
      bet: 10,
      userLoggedIn: false,
      isEnemyModalVisible: false,
      isUpgradeModalVisible: false,
      protagonistIsDead: false,
      fightIsOn: false,
      chosenEnemyId: 1,
      winRate: 0,
      winOdd: 1,
      protagonistStatus: {
        dead: false,
        attack1: false,
        attack2: false,
        attack3: false,
        defence: false,
        run: false,
      },
      enemyStatus:{
        dead: false,
        attack: false,
        defence: false,
      },
      priceList:{
        speed: 50,
        strength: 75,
        durability: 60,
      },
      enemies:[
        {id: 1, name: 'Goblin', speed: 3, strength: 8, durability: 7,},
        {id: 2, name: 'Dead', speed: 7, strength: 5, durability: 5},
        {id: 3, name: 'Flying eye', speed: 4, strength: 9, durability: 6},
        {id: 4, name: 'Mushroom', speed: 4, strength: 7, durability: 5},
        {id: 5, name: 'Skeleton', speed: 9, strength: 5, durability: 5}
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
        const winNumber = Math.random();
        this.balance -= this.bet;
        //let winner = "";
        if(winNumber <= this.winRate){
          //winner = "You";
          this.balance += this.bet * this.winOdd;
        }
        else{
          //winner = "Enemy";
          this.fightIsOn = true;
          this.protagonistStatus.dead = true;
          setTimeout(() => {this.protagonistStatus.dead = false;
            this.fightIsOn = false;}, 1500*2);
        }
        this.bet = 10;
        // winner += " win";
        // alert(winner);
      }
      else if(this.bet > this.balance){
        alert("You don`t have enough money :(")
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
          return 'mushroom-animation';
        case 5:
          return 'skeleton-animation';
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
      this.winOdd = Math.max(4-this.winRate*3.95, 1.4);
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

        .little-button.disabled a{
          cursor: not-allowed;
          top:8px;
          background-color: #4b1363;

          -webkit-box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
          -moz-box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
          box-shadow:inset 0 1px 0 #d6c6dd, inset 0 -3px 0 #2F0A3D;
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

        .dop{
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
          width: 240px;
          height: 240px;
          bottom: 50px;
          background-image: url('assets/Adventurer/adventurer-idle-00.svg'); /* Первый кадр */
          background-size: cover;
          background-position: center;
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

        .protagonist-death{
          animation: protagonist-death-animation 1.5s steps(6) 2;
        }

        @keyframes protagonist-death-animation {
          0% {background-image: url('assets/Adventurer/adventurer-die-00.svg'); }
          16% {background-image: url('assets/Adventurer/adventurer-die-01.svg'); }
          33% {background-image: url('assets/Adventurer/adventurer-die-02.svg');}
          50% {background-image: url('assets/Adventurer/adventurer-die-03.svg');}
          66%{background-image: url('assets/Adventurer/adventurer-die-04.svg');}
          83% {background-image: url('assets/Adventurer/adventurer-die-05.svg');}
          100%{background-image: url('assets/Adventurer/adventurer-die-06.svg');}
        }

        .protagonist-run{
          animation: protagonist-run-animation 0.7s steps(11) 1;
          transform: translate(40px,0);
        }

        @keyframes protagonist-run-animation {
          0% {background-image: url('assets/Adventurer/adventurer-run-00.svg'); }
          16% {background-image: url('assets/Adventurer/adventurer-run-01.svg'); }
          33% {background-image: url('assets/Adventurer/adventurer-run-02.svg');}
          50% {background-image: url('assets/Adventurer/adventurer-run-03.svg');}
          66%{background-image: url('assets/Adventurer/adventurer-run-04.svg');}
          83% {background-image: url('assets/Adventurer/adventurer-run-05.svg');}
          100%{background-image: url('assets/Adventurer/adventurer-run-00.svg');}
        }

        .protagonist-attack1{
          animation: protagonist-attack1-animation 2.5s steps(11) 1;
        }

        @keyframes protagonist-attack1-animation {
          0% {background-image: url('assets/Adventurer/adventurer-attack1-00.svg'); }
          9% {background-image: url('assets/Adventurer/adventurer-attack1-01.svg'); }
          18% {background-image: url('assets/Adventurer/adventurer-attack1-02.svg');}
          27% {background-image: url('assets/Adventurer/adventurer-attack1-03.svg');}
          36%{background-image: url('assets/Adventurer/adventurer-attack1-04.svg');}
          45% {background-image: url('assets/Adventurer/adventurer-attack2-00.svg');}
          54%{background-image: url('assets/Adventurer/adventurer-attack2-01.svg');}
          63% {background-image: url('assets/Adventurer/adventurer-attack2-02.svg');}
          72%{background-image: url('assets/Adventurer/adventurer-attack2-03.svg');}
          81% {background-image: url('assets/Adventurer/adventurer-attack2-04.svg');}
          90% {background-image: url('assets/Adventurer/adventurer-attack2-05.svg');}
          100% {background-image: url('assets/Adventurer/adventurer-attack1-00.svg'); }
        }

        .goblin-animation {
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

          .dead-animation {
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

          .flying-eye-animation {
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
          .mushroom-animation {
            bottom: 50px;
            margin: 10px auto;
            background-image: url('assets/Enemies/Mushroom/mushroom1.svg');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            animation: mushroom-loop-animation 0.9s steps(7) infinite;
          }

          @keyframes mushroom-loop-animation {
            0% { background-image: url('assets/Enemies/Mushroom/mushroom1.svg'); }
            9.09% { background-image: url('assets/Enemies/Mushroom/mushroom2.svg'); }
            18.18% { background-image: url('assets/Enemies/Mushroom/mushroom3.svg'); }
            27.27% { background-image: url('assets/Enemies/Mushroom/mushroom4.svg'); }
            36.36% { background-image: url('assets/Enemies/Mushroom/mushroom5.svg'); }
            45.45% { background-image: url('assets/Enemies/Mushroom/mushroom6.svg'); }
            54.54% { background-image: url('assets/Enemies/Mushroom/mushroom7.svg'); }
            63.63% { background-image: url('assets/Enemies/Mushroom/mushroom8.svg'); }
            72.72% { background-image: url('assets/Enemies/Mushroom/mushroom9.svg'); }
            81.81% { background-image: url('assets/Enemies/Mushroom/mushroom10.svg'); }
            90% { background-image: url('assets/Enemies/Mushroom/mushroom11.svg'); }
            100% { background-image: url('assets/Enemies/Mushroom/mushroom1.svg'); }
        }
          .skeleton-animation {
              bottom: 50px;
              margin: 10px auto;
              background-image: url('assets/Enemies/Skeleton/skeleton_new1.svg'); /* Первый кадр */
              background-size: contain;
              background-position: center;
              background-repeat: no-repeat;
              animation: skeleton-loop-animation 1.8s steps(7) infinite; /* Анимация */
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