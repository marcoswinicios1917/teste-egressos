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
          <li class="nav-item">
            <RouterLink
              to="/"
              class="nav-link"
              :class="{ active: isActive('/') }"
            >
              Home
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/page-sections/page-headers"
              class="nav-link"
              :class="{
                active: isActive('/sections/page-sections/page-headers'),
              }"
            >
              Pesquisa de Egressos
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/attention-catchers/tooltips-popovers"
              class="nav-link"
              :class="{
                active: isActive(
                  '/sections/attention-catchers/tooltips-popovers'
                ),
              }"
            >
              Oportunidades
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/navigation/navbars"
              class="nav-link"
              :class="{ active: isActive('/sections/navigation/navbars') }"
            >
              Contatos
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/sections/page-sections/features"
              class="nav-link"
              :class="{ active: isActive('/sections/page-sections/features') }"
            >
              Administrativo
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              to="/pages/landing-pages/basic"
              class="nav-link"
              :class="{ active: isActive('/pages/landing-pages/basic') }"
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

// Função para verificar a rota ativa
const isActive = (targetRoute) => route.path === targetRoute;
</script>

<style scoped>
/* Estilo do Navbar */
.navbar {
  background-color: #ffffff;
  padding: 0.5rem 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Estilo da logo */
.logo {
  max-height: 150px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

/* Estilo dos links */
.nav-link {
  color: #007bff;
  font-weight: 500;
  font-size: 1.3rem !important;
  padding: 1rem 1.8rem !important;
  text-transform: uppercase;
  transition: color 0.1s ease, transform 0.1s ease;
  text-decoration: none;
}

.nav-link:hover {
  color: #0056b3;
  transform: translateY(-3px);
}

.active {
  color: #0056b3 !important;
  font-weight: bold;
}

/* Alinhamento e espaçamento */
.navbar-nav {
  margin-right: 0;
  margin-left: auto;
}

.nav-item {
  margin-left: -1.5rem;
}

/* Para telas pequenas */
@media (max-width: 992px) {
  .navbar {
    padding: 0.5rem;
  }

  .nav-link {
    font-size: 0.9rem;
  }

  .logo {
    max-height: 40px;
  }
}
</style>
