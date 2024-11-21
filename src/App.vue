<template>
<div class="balance"><div class="little-button"><a>Balance: $ {{balance}}</a></div></div>
<div class="upgrade-button" @click="openUpgradeModal" id="open-upgrade"><div class="little-button" id="open-upgrade"><a>Upgrade</a></div></div>
<div class="container">
    <div class="button" @click="addMoney"><a>Click Me!</a></div>

</div>
<div class="animation-section">
    <div class="input-container">
        <div class="little-button" @click="openEnemyModal" id="open-enemy"><a>Choose Enemy</a></div>
        <div class="bet-row">
            <span>Win Rate: 75%</span>
            <input type="text" placeholder="Bet Amount">
        </div>
        <div class="little-button "><a>Start Fight</a></div>
    </div>
    <div class="animation-placeholder">
    </div>
</div>

<!-- Enemy Modal -->
<div v-if="isEnemyModalVisible"  class="modal" id="enemy-modal">
    <h2>Choose Your Enemy</h2>
    <div class="modal-content">
        <p>Enemy 1 - Speed: 5, Strength: 8, Durability: 7 </p><div class="super-little-button"><a>Select</a></div>
        <p>Enemy 2 - Speed: 7, Strength: 6, Durability: 5 </p><div class="super-little-button"><a>Select</a></div>
        <p>Enemy 3 - Speed: 4, Strength: 9, Durability: 6 </p><div class="super-little-button"><a>Select</a></div>
    </div>
</div>

<!-- Upgrade Modal -->
<div v-if="isUpgradeModalVisible" class="modal" id="upgrade-modal">
    <h2>Upgrade Your Character</h2>
    <div class="modal-content">
        <p>Speed: 5 </p><div class="super-little-button"><a>Upgrade</a></div>
        <p>Strength: 8 </p><div class="super-little-button"><a>Upgrade</a></div>
        <p>Durability: 7 </p><div class="super-little-button"><a>Upgrade</a></div>
    </div>
</div>

<div v-if="isModalVisible" class="overlay" @click="closeModals" id="overlay"></div>
</template>


<script>
export default {
  data() {
    return{
      balance: 0,
      isEnemyModalVisible: false,
      isUpgradeModalVisible: false,
    }
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
    }
  }

}

</script>

<style>
        /* Общие стили */
        body {
            margin: 0;
            font-family: 'Press Start 2P', sans-serif; /* Явно указываем шрифт */
            //background: transparent; /* Темный фиолетовый */
            background-image: url("assets/background2.png");
            background-repeat: repeat-x;
            background-size: cover;
            background-position: bottom center;
            color: #d6c6dd; /* Светлый пастельный фиолетовый */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            height: 100vh;
            overflow: hidden;
            user-select: none;
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

        /* Центральная секция */
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
          //font-weight:bold;
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
          //font-weight:bold;
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
          //font-weight:bold;
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

                .animation-placeholder {
          width: 240px; /* Размеры контейнера анимации */
          height: 240px;
          bottom: 50px;
          margin: 10px auto;
          background-image: url('assets/Adventurer/adventurer-idle-00.svg'); /* Первый кадр */
          background-size: cover;
          background-position: center;
          animation: loop-animation 1.2s steps(6) infinite; /* Анимация */
        }

        /* Определяем анимацию */
        @keyframes loop-animation {
          0% {
            background-image: url('assets/Adventurer/adventurer-idle-00.svg'); /* Кадр 1 */
          }
          16% {
            background-image: url('assets/Adventurer/adventurer-idle-01.svg'); /* Кадр 2 */
          }
          33% {
            background-image: url('assets/Adventurer/adventurer-idle-02.svg'); /* Кадр 3 */
          }
          50% {
            background-image: url('assets/Adventurer/adventurer-idle-03.svg'); /* Возврат к кадру 1 */
          }
            66%{
                 background-image: url('assets/Adventurer/adventurer-idle-02.svg'); /* Кадр 3 */
            }
            83% {
            background-image: url('assets/Adventurer/adventurer-idle-01.svg'); /* Кадр 2 */
          }
            100%{
                background-image: url('assets/Adventurer/adventurer-idle-00.svg'); /* Кадр 1 */
            }

        }

        /* Ввод и вероятность */
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

        /* Анимация */
        .animation-section {
            background: transparent; /* Темный фиолетовый */
            border: 0px solid #e0c3fc;
            width: 100%;
            height: 50%;
            bottom: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Модальные окна */
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

        .modal h2 {
            font-size: 14px;
            font-family: 'Press Start 2P', sans-serif;
        }

        .modal-content {
            margin-top: 20px;
        }
        .modal-content button {
            font-family: 'Press Start 2P', sans-serif;
        }

        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            display: block;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 5;
        }
    </style>