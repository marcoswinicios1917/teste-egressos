<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
    <div class="container-fluid">
      <!-- Logo -->
      <a href="/" class="navbar-brand">
        <img
          src="/src/assets/img/egressosufdpar.png"
          alt="Logo Egressos UFDPar"
          class="img-fluid logo"
        />
      </a>

      <!-- Botão de colapso para telas menores -->
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

      <!-- Links do Navbar -->
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item" v-for="nav in navItems" :key="nav.name">
            <a
              :href="nav.link"
              class="nav-link"
              :class="{ active: activeNav === nav.id }"
              @click="setActiveNav(nav.id)"
              >{{ nav.name }}</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <BaseLayout
    title="Oportunidades"
    :breadcrumb="[
      { label: 'Portal do Egresso', route: '#' },
      { label: 'Oportunidades' },
    ]"
  >
    <div class="container mt-5">
      <!-- Navegação por abas -->
      <ul
        class="nav nav-pills mb-4 justify-content-center"
        id="pills-tab"
        role="tablist"
        style="margin-top: 150px"
      >
        <li
          class="nav-item"
          role="presentation"
          v-for="tab in tabs"
          :key="tab.id"
        >
          <button
            class="nav-link"
            :class="{
              active: activeTab === tab.id,
              'selected-button': activeTab === tab.id,
            }"
            @click="setActiveTab(tab.id)"
            role="tab"
            :aria-controls="`pills-${tab.id}`"
            :aria-selected="activeTab === tab.id"
          >
            <i :class="tab.icon" class="me-1"></i> {{ tab.name }}
          </button>
        </li>
      </ul>

      <div class="tab-content" id="pills-tabContent">
        <div
          v-for="tab in tabs"
          :key="tab.id"
          class="tab-pane fade"
          :class="{
            show: activeTab === tab.id,
            active: activeTab === tab.id,
          }"
          :id="`pills-${tab.id}`"
          role="tabpanel"
        >
          <h3 class="text-center my-4">{{ tab.title }}</h3>
          <p class="text-center">{{ tab.description }}</p>
          <div class="row">
            <div
              v-for="item in tab.items"
              :key="item.title"
              class="col-md-6 col-lg-4 mb-4"
            >
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">{{ item.title }}</h5>
                  <p class="card-text">{{ item.description }}</p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails(item.title)"
                  >
                    Ver Detalhes
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </BaseLayout>
</template>

<script>
export default {
  data() {
    return {
      activeNav: "oportunidades",
      activeTab: "empregos",
      navItems: [
        { id: "home", name: "Home", link: "/" },
        {
          id: "pesquisa",
          name: "Pesquisa de Egressos",
          link: "/sections/page-sections/page-headers",
        },
        {
          id: "oportunidades",
          name: "Oportunidades",
          link: "/sections/attention-catchers/tooltips-popovers",
        },
        {
          id: "contatos",
          name: "Contatos",
          link: "/sections/navigation/navbars",
        },
        {
          id: "administrativo",
          name: "Administrativo",
          link: "/sections/page-sections/features",
        },
        { id: "entrar", name: "Entrar", link: "/pages/landing-pages/basic" },
      ],
      tabs: [
        {
          id: "empregos",
          name: "Empregos",
          title: "Oportunidades de Emprego",
          description:
            "Explore as últimas vagas de emprego disponíveis para egressos.",
          items: [
            {
              title: "Desenvolvedor Front-end",
              description: "Vaga para desenvolvedor com experiência em Vue.js.",
            },
            {
              title: "Analista de Dados",
              description: "Analista de Dados com habilidades em SQL e Python.",
            },
          ],
          icon: "bi bi-briefcase",
        },
        {
          id: "estagios",
          name: "Estágios",
          title: "Oportunidades de Estágio",
          description: "Vagas de estágio disponíveis.",
          items: [
            {
              title: "Estágio em Marketing",
              description: "Estágio em Marketing Digital.",
            },
            { title: "Estágio em TI", description: "Suporte técnico e redes." },
          ],
          icon: "bi bi-person-badge",
        },
        {
          id: "mentorias",
          name: "Mentorias",
          title: "Programas de Mentoria",
          description: "Programas de mentoria para egressos.",
          items: [],
          icon: "bi bi-lightbulb",
        },
        {
          id: "cursos",
          name: "Cursos",
          title: "Cursos Disponíveis",
          description: "Cursos oferecidos para egressos.",
          items: [],
          icon: "bi bi-book",
        },
      ],
    };
  },
  methods: {
    setActiveTab(tab) {
      this.activeTab = tab;
    },
    setActiveNav(nav) {
      this.activeNav = nav;
    },
    showDetails(title) {
      alert(`Exibindo detalhes para: ${title}`);
    },
  },
};
</script>

<style scoped>
/* Variáveis de cores */
navbar {
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

/* Botão de navegação ativo */
.selected-button {
  background-color: var(--primary-color);
  color: var(--white-color) !important;
}

/* Cartões */
.animated-card {
  transition: transform 0.2s;
}
.animated-card:hover {
  transform: scale(var(--card-hover-scale));
}

/* Botões */
.animated-button {
  transition: background-color 0.3s, transform 0.3s;
}
.animated-button:hover {
  background-color: var(--hover-color);
  transform: scale(var(--card-hover-scale));
}

/* Responsividade */
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
