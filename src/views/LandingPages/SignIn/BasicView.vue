<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import Header from "@/examples/Header.vue";
import setMaterialInput from "@/assets/js/material-input";

const email = ref("");
const password = ref("");
const rememberMe = ref(false);
const router = useRouter();

// Recupera email e senha do local storage ao montar
onMounted(() => {
  email.value = localStorage.getItem("savedEmail") || "";
  password.value = localStorage.getItem("savedPassword") || "";
  setMaterialInput();
});

// Função para lidar com o login
function handleLogin() {
  if (rememberMe.value) {
    localStorage.setItem("savedEmail", email.value);
    localStorage.setItem("savedPassword", password.value);
  } else {
    localStorage.removeItem("savedEmail");
    localStorage.removeItem("savedPassword");
  }
  // Redireciona para a página após o login
  router.push({ name: "dashboard" });
}
</script>

<template>
  <DefaultNavbar transparent />
  <div>
    <Header>
      <div class="page-header">
        <div
          class="container my-auto d-flex flex-column align-items-center justify-content-center"
        >
          <div class="login-container">
            <h4 class="font-weight-bolder mt-2 mb-0">Portal do Egresso</h4>
            <p class="mb-4 text-center">Acesse sua conta</p>
            <div class="card-body">
              <form role="form" class="text-start">
                <div class="input-wrapper">
                  <input
                    v-model="email"
                    type="email"
                    id="email"
                    class="form-control"
                    placeholder=" "
                    required
                  />
                  <label for="email">Email</label>
                </div>
                <div class="input-wrapper">
                  <input
                    v-model="password"
                    type="password"
                    id="password"
                    class="form-control"
                    placeholder=" "
                    required
                  />
                  <label for="password">Senha</label>
                </div>
                <div class="d-flex align-items-center mb-4">
                  <input
                    v-model="rememberMe"
                    class="form-check-input"
                    type="checkbox"
                    id="rememberMe"
                  />
                  <label class="form-check-label ms-2" for="rememberMe">
                    <span class="remember-me-text">Mantenha-me conectado</span>
                  </label>
                </div>
                <div class="text-center">
                  <button
                    type="button"
                    @click="handleLogin"
                    class="btn btn-primary"
                  >
                    Entrar
                  </button>
                  <label class="form-check-label ms-2" for="rememberMe">
                    <span class="remember-me-text">Mantenha-me conectado</span>
                  </label>
                </div>
                <p class="mt-4 text-sm text-center">
                  Não tem uma conta?
                  <a href="#" class="text-blue font-weight-bold">Cadastrar</a>
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </Header>
    <footer class="footer-custom py-5">
      <div class="container text-center">
        <div class="footer-image-container mb-3">
          <img
            src="/src/assets/img/assinaturaUFDPar.png"
            alt="Assinatura UFDPar"
            class="footer-image"
          />
        </div>
        <div class="line-container">
          <hr class="elegant-line" />
        </div>
        <div class="footer-text-container mt-4">
          <p class="mb-0 text-secondary footer-text">
            Copyright © {{ new Date().getFullYear() }} Portal do Egresso da
            Universidade Federal do Delta do Parnaíba.
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.page-header {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url("@/assets/img/vue-mk-header.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: #e0e0e0;
}

.container {
  height: 100%;
}

.login-container {
  background-color: rgba(255, 255, 255, 0.9);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 90%;
  position: relative;
  overflow: hidden;
  animation: fadeIn 0.5s ease-in-out;
}

h4 {
  color: #003366;
  margin-bottom: 1rem;
  font-size: 2rem;
  text-align: center;
}

.btn-primary {
  background-color: #00509e;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  transition: background-color 0.3s, transform 0.3s;
  width: 100%;
  font-size: 1.1rem;
}

.btn-primary:hover {
  background-color: #003366;
  transform: scale(1.05);
}

.footer-custom {
  background-color: #003366;
  padding: 2rem 0;
  color: white;
}

.footer-image-container {
  max-width: 250px;
  margin: 0 auto;
}

.footer-image {
  max-width: 100%;
}

.line-container {
  margin: 2rem 0;
  width: 100%;
}

.elegant-line {
  border: none;
  height: 6px;
  background-image: linear-gradient(to right, #ffd700, #ffcc00, #ffd700);
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
  border-radius: 5px;
  width: 100%;
}

.footer-text {
  font-size: 1rem;
  line-height: 1.5;
}

.text-secondary {
  color: #e0e0e0;
}

.text-blue {
  color: #00509e;
}

.input-wrapper {
  position: relative;
  margin-bottom: 20px;
}

input {
  width: 100%;
  padding: 12px; /* Aumentar o padding para melhor espaçamento */
  border: 2px solid #00509e; /* Adiciona borda ao input */
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.9);
  transition: all 0.3s ease;
  outline: none;
}

label {
  position: absolute;
  left: 10px;
  top: -8px; /* Ajuste para cima para que o label fique acima */
  color: #00509e;
  transition: all 0.3s ease;
  pointer-events: none;
  font-weight: bold;
  font-size: 14px; /* Tamanho do texto do label */
}

input:focus {
  background-color: rgba(255, 255, 255, 1);
  border-color: #003366; /* Muda a cor da borda ao focar */
}

input:focus + label,
input:not(:placeholder-shown) + label {
  top: -20px; /* Mantém o label acima do input */
  left: 10px;
  font-size: 12px;
  color: #003366;
}

.remember-me-text {
  font-size: 14px;
  color: #00509e; /* Cor do texto "lembrar de mim" */
  transition: color 0.3s;
}

.remember-me-text:hover {
  color: #003366; /* Muda a cor ao passar o mouse */
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .footer-text {
    font-size: 0.9rem;
  }

  .login-container {
    padding: 30px;
  }

  h4 {
    font-size: 1.5rem;
  }
}
</style>
