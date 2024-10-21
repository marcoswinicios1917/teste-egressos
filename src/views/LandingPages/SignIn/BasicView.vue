<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import Header from "@/examples/Header.vue";
import setMaterialInput from "@/assets/js/material-input";

const email = ref("");
const password = ref("");
const emailError = ref("");
const passwordError = ref("");
const router = useRouter();

onMounted(() => {
  email.value = localStorage.getItem("savedEmail") || "";
  password.value = localStorage.getItem("savedPassword") || "";
  setMaterialInput();
});

function validateForm() {
  emailError.value = !email.value ? "Email é obrigatório" : "";
  passwordError.value = !password.value ? "Senha é obrigatória" : "";
  return !emailError.value && !passwordError.value;
}

function handleLogin() {
  if (validateForm()) {
    router.push({ name: "dashboard" });
  }
}
</script>

<template>
  <DefaultNavbar transparent />
  <div class="page-wrapper">
    <Header>
      <div class="page-header">
        <div
          class="container my-auto d-flex flex-column align-items-center justify-content-center"
        >
          <div class="login-container">
            <h4 class="portal-title mt-2 mb-0">Portal do Egresso</h4>
            <p class="access-text mb-4 text-center">Acesse sua conta</p>
            <div class="card-body">
              <form
                role="form"
                class="text-start"
                @submit.prevent="handleLogin"
              >
                <div class="input-wrapper">
                  <input
                    v-model="email"
                    type="email"
                    id="email"
                    class="form-control"
                    placeholder=" "
                    required
                    aria-describedby="emailError"
                  />
                  <label for="email">Email</label>
                  <span v-if="emailError" class="error-text" id="emailError">{{
                    emailError
                  }}</span>
                </div>
                <div class="input-wrapper">
                  <input
                    v-model="password"
                    type="password"
                    id="password"
                    class="form-control"
                    placeholder=" "
                    required
                    aria-describedby="passwordError"
                  />
                  <label for="password">Senha</label>
                  <span
                    v-if="passwordError"
                    class="error-text"
                    id="passwordError"
                    >{{ passwordError }}</span
                  >
                </div>
                <div class="text-center">
                  <button type="submit" class="btn btn-primary login-button">
                    Entrar
                  </button>
                </div>
                <p class="mt-4 text-sm text-center">
                  Não tem uma conta?
                  <a href="#" class="text-highlight font-weight-bold"
                    >Cadastrar</a
                  >
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
/* Ajustes gerais da página */
.page-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;
}

.page-header {
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url("@/assets/img/vue-mk-header.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 60vh; /* Ajusta a altura do cabeçalho para 60% da viewport */
  background-size: contain; /* Faz a imagem aparecer completa */
  background-position: center; /* Alinha a imagem no centro */
  background-repeat: no-repeat; /* Impede que a imagem se repita */
  margin-top: 145px; /* Move a imagem um pouco para baixo, alinhando com o Navbar */
  background-color: #e0e0e0; /* Fundo cinza claro e elegante */
}

.container {
  height: 100%;
}

.login-container {
  background-color: rgba(255, 255, 255, 0.92);
  padding: 50px;
  border-radius: 30px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
  max-width: 420px;
  width: 100%;
  text-align: center;
}

.portal-title {
  color: #003366;
  font-weight: bold;
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.access-text {
  color: #666666;
  font-size: 1rem;
  margin-bottom: 1.5rem;
}

.btn-primary.login-button {
  background-color: #00509e;
  color: white;
  padding: 12px 25px;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  transition: all 0.3s ease;
  font-size: 1.1rem;
  width: 100%;
}

.btn-primary.login-button:hover {
  background-color: #004080;
  transform: scale(1.03);
}

/* Estilo dos inputs */
.input-wrapper {
  position: relative;
  margin-bottom: 25px;
}

input {
  width: 100%;
  padding: 14px;
  border: 2px solid #00509e;
  border-radius: 8px;
  background-color: transparent;
  transition: all 0.3s ease;
}

input:focus {
  background-color: #00509e;
  color: white;
}

label {
  position: absolute;
  left: 15px;
  top: -12px;
  color: #00509e;
  background-color: #fff;
  padding: 0 8px;
  font-size: 14px;
  transition: all 0.3s ease;
}

/* Texto de erro */
.error-text {
  color: #ff4c4c;
  font-size: 0.8rem;
  margin-top: 5px;
  text-align: left;
}

/* Rodapé */
.footer-custom {
  background-color: #003366;
  color: white;
  padding: 2rem 0;
}

.footer-image-container {
  max-width: 250px;
  margin: 0 auto;
}

.footer-image {
  max-width: 100%;
}

.line-container {
  margin: 0rem;
}

.elegant-line {
  border: none;
  height: 5px;
  background: linear-gradient(90deg, #ffd700, #ffcc00, #ffd700);
  border-radius: 5px;
}

.footer-text {
  font-size: 0.9rem;
}
</style>
