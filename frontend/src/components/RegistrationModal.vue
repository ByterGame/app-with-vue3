<script>
// eslint-disable-next-line vue/no-export-in-script-setup
export default{
  data(){
    return{
      isRegistrationModalVisible: true,
      isLoginModalVisible: false,
    }
  },
  props: {
    userLoggedIn: {
      type: Boolean
    }
  },
  methods: {
    openLogin(){
      this.isRegistrationModalVisible = false;
      this.isLoginModalVisible = true;
    },
    openRegistration(){
      this.isRegistrationModalVisible = true;
      this.isLoginModalVisible = false;
    },
    login() {
      this.$emit('login', true);
    }
  },
}
</script>

<template>
<div v-if="isRegistrationModalVisible" class="modal" id="registration-modal">
    <h2>Sign up or log in!</h2>
    <div class="modal-content">
        <input class="name-input" type="text" placeholder="Enter Your Name">
      <input class="password-input" type="password" placeholder="Enter Your Password">
      <input class="password-input" type="password" placeholder="Repeat Your Password">
      <div class="little-button"><a>Create account</a></div>
<div class="little-button" @click="openLogin"><a>I already have an account</a></div>
    </div>
</div>

  <div v-if="isLoginModalVisible" class="modal" id="registration-modal">
    <h2>Sign up or log in!</h2>
    <div class="modal-content">
        <input class="name-input" type="text" placeholder="Enter Your Name">
      <input class="password-input" type="password" placeholder="Enter Your Password">
      <div class="little-button" @click="login"><a>Log in</a></div>
<div class="little-button" @click="openRegistration"><a>I don`t have an account</a></div>
    </div>
</div>
</template>

<style scoped>
        .little-button{
          text-align:center;
          background-color: transparent;
          font-family: 'Press Start 2P', sans-serif;
          position:relative;
          display:inline-block;
          margin:20px;
              cursor: pointer;
          width: 85%;
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
        .modal {
            position: fixed;
          width: 512px;
            top: 50%;
            left: 50%;
            display: block;
          color: #d6c6dd;
          font-family: 'Press Start 2P', sans-serif;
          font-size:14px;
            transform: translate(-50%, -50%);
            background: #2d013d;
            opacity: 0.95;
            padding: 20px;
            border: 4px solid #e0c3fc;
            z-index: 10;
          align-items: center;
          text-align:center;
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
        .modal-content button {
            font-family: 'Press Start 2P', sans-serif;
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