<script setup>
import { ref } from "vue";
import BaseLayout from "../../components/BaseLayout.vue";

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
    :breadcrumb="[{ label: 'Home', route: '#' }, { label: 'Contato' }]"
  >
    <div id="contact-page" class="container py-5 bg-light-gray">
      <!-- Formulário e Informações -->
      <div class="row mb-5 bg-gray-box p-4 rounded-3 shadow-sm">
        <!-- Formulário de Contato -->
        <div class="col-lg-6 col-md-12 mb-4">
          <h3 class="text-primary fw-bold mt-3 mb-3">
            Estamos Aqui Para Você!
          </h3>
          <p class="text-muted mb-3">
            Se tiver alguma dúvida ou precisar de assistência, entre em contato
            preenchendo o formulário abaixo.
          </p>
          <form
            @submit.prevent="handleSubmit"
            class="shadow-sm p-4 rounded bg-white mt-3 mb-3"
          >
            <div class="mb-3">
              <label for="name" class="form-label text-primary">Seu Nome</label>
              <input
                type="text"
                class="form-control"
                id="name"
                v-model="name"
                required
                placeholder="Digite seu nome completo"
              />
            </div>
            <div class="mb-3">
              <label for="email" class="form-label text-primary"
                >Seu E-mail</label
              >
              <input
                type="email"
                class="form-control"
                id="email"
                v-model="email"
                required
                placeholder="Digite seu e-mail"
              />
            </div>
            <div class="mb-3">
              <label for="message" class="form-label text-primary"
                >Sua Mensagem</label
              >
              <textarea
                class="form-control"
                id="message"
                v-model="message"
                rows="4"
                required
                placeholder="Digite sua mensagem aqui..."
              ></textarea>
            </div>
            <button type="submit" class="btn btn-primary w-100 mt-3">
              Enviar Mensagem
            </button>
          </form>
        </div>

        <!-- Informações de Contato -->
        <div class="col-lg-6 col-md-12">
          <h3 class="text-primary fw-bold mt-3 mb-3">Informações de Contato</h3>
          <div class="contact-info mb-4">
            <p class="text-muted mb-3">
              <i class="fas fa-envelope me-2 text-primary"></i>Email:
              <a href="mailto:prae@ufdpar.edu.br" class="text-dark fw-semibold"
                >prae@ufdpar.edu.br</a
              >
            </p>
            <p class="text-muted mb-3">
              <i class="fas fa-phone me-2 text-primary"></i>Telefone:
              <a href="tel:+558694369919" class="text-dark fw-semibold"
                >(86) 9 9436-0919</a
              >
            </p>
            <p class="text-muted mb-3">
              <i class="fas fa-map-marker-alt me-2 text-primary"></i>Endereço:
              Nossa Senhora de Fátima, Parnaíba-PI, CEP: 64.202-020
            </p>
          </div>
          <h4 class="text-primary mt-4 mb-3">Redes Sociais</h4>
          <div class="social-links d-flex align-items-center mt-3 mb-3">
            <a
              href="https://www.instagram.com/ufdpar.br/"
              class="text-primary me-3 fs-4"
              target="_blank"
              aria-label="Instagram"
              ><i class="fab fa-instagram"></i
            ></a>
            <a
              href="https://www.facebook.com/ufdpar.edu.br"
              class="text-primary me-3 fs-4"
              target="_blank"
              aria-label="Facebook"
              ><i class="fab fa-facebook"></i
            ></a>
            <a
              href="https://www.youtube.com/c/TVUFDPar"
              class="text-primary me-3 fs-4"
              target="_blank"
              aria-label="YouTube"
              ><i class="fab fa-youtube"></i
            ></a>
            <a
              href="https://twitter.com/ufdpar"
              class="text-primary me-3 fs-4"
              target="_blank"
              aria-label="Twitter"
              ><i class="fab fa-twitter"></i
            ></a>
            <a
              href="https://www.linkedin.com/school/ufdpar/"
              class="text-primary fs-4"
              target="_blank"
              aria-label="LinkedIn"
              ><i class="fab fa-linkedin"></i
            ></a>
          </div>
        </div>
      </div>

      <!-- Localização no Google Maps -->
      <div class="row mt-4 mb-4">
        <div class="col-12">
          <h3 class="text-primary fw-bold mt-3 mb-3">Localização</h3>
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.835434509602!2d-41.7780!3d-2.8860!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6e0f232da146bb9f%3A0xd09175eaa701c74b!2sUniversidade%20Federal%20do%20Delta%20do%20Parna%C3%ADba!5e0!3m2!1spt-BR!2sbr!4v1632863048810!5m2!1spt-BR!2sbr"
            width="100%"
            height="300"
            class="rounded shadow-sm border-0 mt-3 mb-3"
            allowfullscreen=""
            loading="lazy"
          ></iframe>
        </div>
      </div>
    </div>
  </BaseLayout>
</template>
<style scoped>
/* Fundo cinza claro para o container principal */
.bg-light-gray {
  background-color: #f3f3f3; /* Fundo cinza */
  padding: 20px;
  border-radius: 8px;
}

.bg-gray-box {
  background-color: #ffffff; /* Fundo branco */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  margin-top: -50px;
  margin-bottom: 10px;
}

h3,
h4 {
  margin-top: 20px;
  margin-bottom: 10px;
}

.contact-info p {
  font-size: 1.1rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.text-primary {
  color: #007bff !important; /* Azul */
}

.btn-primary {
  background-color: #007bff;
  border: none;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.social-links a {
  font-size: 1.5rem;
  margin-right: 15px;
  color: #007bff;
  transition: color 0.3s ease;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

social-links a:hover {
  color: #0056b3;
}

iframe {
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
