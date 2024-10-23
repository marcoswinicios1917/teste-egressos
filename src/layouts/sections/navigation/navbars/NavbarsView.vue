<script setup>
import { ref, onMounted } from "vue";
import BaseLayout from "../../components/BaseLayout.vue";
import View from "../../components/View.vue";

// Hook para configurar elementos na montagem
onMounted(() => {
  // Configurações adicionais podem ser adicionadas aqui
});

// Variáveis reativas para o formulário
const name = ref("");
const email = ref("");
const message = ref("");

// Função para lidar com o envio do formulário
const handleSubmit = () => {
  alert(`Mensagem enviada por ${name.value} com e-mail ${email.value}`);
  // Limpar campos após o envio
  name.value = "";
  email.value = "";
  message.value = "";
};
</script>

<template>
  <BaseLayout
    title="Contato"
    :breadcrumb="[{ label: 'Home', route: '#' }, { label: 'Contato' }]"
  >
    <View id="contact-page" height="auto" class="position-relative pb-5">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 my-auto">
            <h3 class="text-primary fw-bold">Estamos Aqui Para Você!</h3>
            <p class="text-muted">
              Se você tiver alguma dúvida ou precisar de assistência, sinta-se à
              vontade para entrar em contato conosco preenchendo o formulário
              abaixo.
            </p>
            <form @submit.prevent="handleSubmit" class="shadow-lg p-4 rounded">
              <div class="mb-3">
                <label for="name" class="form-label">Seu Nome</label>
                <input
                  type="text"
                  class="form-control"
                  id="name"
                  v-model="name"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="email" class="form-label">Seu E-mail</label>
                <input
                  type="email"
                  class="form-control"
                  id="email"
                  v-model="email"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="message" class="form-label">Sua Mensagem</label>
                <textarea
                  class="form-control"
                  id="message"
                  v-model="message"
                  rows="4"
                  required
                ></textarea>
              </div>
              <button type="submit" class="btn btn-primary">
                Enviar Mensagem
              </button>
            </form>
          </div>
          <div class="col-lg-6 mt-lg-0 mt-5">
            <h3 class="text-primary fw-bold">Informações de Contato</h3>
            <div class="contact-info">
              <p class="text-muted">
                Email:
                <a href="mailto:prae@ufdpar.edu.br">prae@ufdpar.edu.br</a>
              </p>
              <p class="text-muted">
                Telefone: <a href="tel:+558694369919">(86) 9 9436-0919</a>
              </p>
              <p class="text-muted">
                Endereço: Nossa Senhora de Fátima, Parnaíba-PI, CEP: 64.202-020
              </p>
            </div>
            <h4 class="mt-4">Redes Sociais</h4>
            <div class="social-links">
              <a
                href="https://www.instagram.com/ufdpar.br/"
                class="text-primary me-2"
                target="_blank"
                ><i class="fab fa-instagram"></i
              ></a>
              <a
                href="https://www.facebook.com/ufdpar.edu.br/?locale=pt_BR"
                class="text-primary me-2"
                target="_blank"
                ><i class="fab fa-facebook"></i
              ></a>
              <a
                href="https://www.youtube.com/c/TVUFDPar"
                class="text-primary"
                target="_blank"
                ><i class="fab fa-youtube"></i
              ></a>
            </div>
          </div>
        </div>
        <div class="row mt-5">
          <div class="col-12">
            <h3 class="text-primary fw-bold">Localização</h3>
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.835434509602!2d-41.7780!3d-2.8860!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6e0f232da146bb9f%3A0xd09175eaa701c74b!2sUniversidade%20Federal%20do%20Delta%20do%20Parna%C3%ADba!5e0!3m2!1spt-BR!2sbr!4v1632863048810!5m2!1spt-BR!2sbr"
              width="100%"
              height="300"
              style="border: 0"
              allowfullscreen=""
              loading="lazy"
            ></iframe>
          </div>
        </div>
      </div>
      <nav class="navbar navbar-expand-lg navbar-light bg-light mt-4">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">UFDPar</a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Sobre Nós</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Serviços</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Contato</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </View>
  </BaseLayout>
</template>

<style scoped>
.container {
  margin-top: 2rem; /* Espaço superior */
}

h3 {
  color: #1f3a3d; /* Cor do cabeçalho */
}

.text-muted {
  color: #6c757d; /* Cor do texto secundário */
}

.btn-primary {
  background-color: #007bff; /* Cor do botão */
  border: none; /* Remover bordas */
  transition: background-color 0.3s ease, transform 0.1s; /* Transição suave */
}

.btn-primary:hover {
  background-color: #0056b3; /* Cor do botão ao passar o mouse */
}

.btn-primary:active {
  transform: scale(0.95); /* Efeito de clique */
}

form {
  background: #fff; /* Fundo branco para o formulário */
  border-radius: 0.5rem; /* Bordas arredondadas */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Sombra do formulário */
}

form .form-control {
  border-radius: 0.5rem; /* Bordas arredondadas nos campos */
}

form .form-label {
  font-weight: bold; /* Negrito nos rótulos */
}

.contact-info {
  margin-bottom: 1.5rem; /* Espaçamento inferior */
}

.social-links a {
  font-size: 1.5rem; /* Tamanho do ícone */
  color: #007bff; /* Cor do ícone */
  transition: color 0.3s ease; /* Transição suave */
}

.social-links a:hover {
  color: #0056b3; /* Cor do ícone ao passar o mouse */
}

.navbar {
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1); /* Sombra na barra de navegação */
}
</style>
