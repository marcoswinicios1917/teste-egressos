<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
    <div class="container-fluid">
      <!-- Logo do site -->
      <RouterLink to="/" class="navbar-brand ms-3">
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
        <ul class="navbar-nav">
          <!-- Botão Home -->
          <li class="nav-item">
            <RouterLink
              to="/"
              class="nav-link"
              :class="isActive('/') ? 'active' : ''"
            >
              Home
            </RouterLink>
          </li>
          <!-- Pesquisa de Egressos -->
          <li class="nav-item">
            <RouterLink
              to="/egressos"
              class="nav-link"
              :class="isActive('/egressos') ? 'active' : ''"
            >
              Pesquisa de Egressos
            </RouterLink>
          </li>
          <!-- Oportunidades -->
          <li class="nav-item">
            <RouterLink
              to="/oportunidades"
              class="nav-link"
              :class="isActive('/oportunidades') ? 'active' : ''"
            >
              Oportunidades
            </RouterLink>
          </li>
          <!-- Contatos -->
          <li class="nav-item">
            <RouterLink
              to="/contatos"
              class="nav-link"
              :class="isActive('/contatos') ? 'active' : ''"
            >
              Contatos
            </RouterLink>
          </li>
          <!-- Administrativo -->
          <li class="nav-item">
            <RouterLink
              to="/administrativo"
              class="nav-link"
              :class="isActive('/administrativo') ? 'active' : ''"
            >
              Administrativo
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

// Função para verificar se a rota atual está ativa
const isActive = (targetRoute) => {
  return route.path === targetRoute;
};
</script>

<style scoped>
/* Estilo do Navbar */
.navbar {
  background-color: #f8f9fa;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Estilo da logo */
.logo {
  max-height: 80px; /* Aumentei o tamanho da imagem da logo */
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.1);
}

/* Estilo dos links */
.nav-link {
  color: #003366;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 0.5rem 1rem;
  text-transform: uppercase;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #0056b3;
}

.active {
  color: #002244 !important;
  border-bottom: 2px solid #002244;
}

/* Ajuste de espaçamento */
.navbar-nav {
  margin-right: 1rem;
}

.nav-item {
  margin-left: 1rem;
}

/* Tornar o navbar estático e preencher a tela */
.navbar-expand-lg {
  width: 100%;
}

/* Para telas pequenas */
@media (max-width: 992px) {
  .navbar {
    padding: 1rem;
  }

  .nav-link {
    font-size: 1rem;
  }

  .logo {
    max-height: 60px; /* Ajustei também para dispositivos menores */
  }
}
</style>
