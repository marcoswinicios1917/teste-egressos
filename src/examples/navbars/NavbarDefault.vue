<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
    <div class="container-fluid">
      <RouterLink to="/" class="navbar-brand">
        <img
          src="@/assets/img/egressosufdpar.png"
          alt="Logo Egressos UFDPar"
          class="img-fluid logo"
        />
      </RouterLink>

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

      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <!-- Adicionado 'ms-auto' para alinhar à direita -->
          <li class="nav-item">
            <RouterLink
              to="/"
              class="nav-link"
              :class="isActive('/') ? 'active' : ''"
            >
              Home
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/page-sections/page-headers"
              class="nav-link"
              :class="
                isActive('/sections/page-sections/page-headers') ? 'active' : ''
              "
            >
              Pesquisa de Egressos
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/attention-catchers/tooltips-popovers"
              class="nav-link"
              :class="
                isActive('/sections/attention-catchers/tooltips-popovers')
                  ? 'active'
                  : ''
              "
            >
              Oportunidades
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/navigation/navbars"
              class="nav-link"
              :class="isActive('/sections/navigation/navbars') ? 'active' : ''"
            >
              Contatos
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/page-sections/features"
              class="nav-link"
              :class="
                isActive('/sections/page-sections/features') ? 'active' : ''
              "
            >
              Administrativo
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/pages/landing-pages/basic"
              class="nav-link"
              :class="isActive('/pages/landing-pages/basic') ? 'active' : ''"
            >
              Entrar
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRoute } from "vue-router";

const route = useRoute();

const isActive = (targetRoute) => {
  return route.path === targetRoute;
};
</script>

<style scoped>
/* Estilo do Navbar */
.navbar {
  background-color: #ffffff; /* Fundo branco */
  padding: 0.5rem 1rem; /* Padding fino */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra sutil */
}

/* Estilo da logo */
.logo {
  max-height: 150px; /* Altura máxima da logo */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.logo:hover {
  transform: scale(1.05); /* Leve aumento ao passar o mouse */
}

/* Estilo dos links */
.nav-link {
  color: #007bff; /* Azul suave */
  font-weight: 500;
  font-size: 1.3rem !important; /* Aumenta o tamanho da fonte */
  padding: 1rem 1.8rem !important; /* Aumenta o padding para tornar os botões maiores */
  text-transform: uppercase; /* Texto em maiúsculas */
  transition: color 0.1s ease, transform 0.1s ease; /* Suavização de transições */
  text-decoration: none; /* Removendo sublinhado */
}

.nav-link:hover {
  color: #0056b3; /* Tom mais escuro ao passar o mouse */
  transform: translateY(-3px); /* Efeito de levitar ao passar o mouse */
}

.active {
  color: #0056b3 !important; /* Cor ativa */
  font-weight: bold; /* Destaque para o link ativo */
}

/* Alinhamento e espaçamento */
.navbar-nav {
  margin-right: 0rem; /* Espaçamento no final da lista */
  margin-left: auto; /* Empurrar para a direita */
}

.nav-item {
  margin-left: -1.5rem; /* Espaçamento entre os itens */
}

/* Para telas pequenas */
@media (max-width: 992px) {
  .navbar {
    padding: 0.5rem; /* Ajustando o padding em telas pequenas */
  }

  .nav-link {
    font-size: 0.9rem; /* Tamanho da fonte em telas pequenas */
  }

  .logo {
    max-height: 40px; /* Reduzindo a logo em telas pequenas */
  }
}
</style>
