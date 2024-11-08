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
          <li class="nav-item" v-for="nav in navItems" :key="nav.id">
            <a
              :href="nav.link"
              class="nav-link"
              :class="{ active: activeNav === nav.id }"
              @click="setActiveNav(nav.id)"
            >
              {{ nav.name }}
            </a>
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

  <!-- Footer -->
  <footer class="footer-custom py-5">
    <div class="container text-center">
      <!-- Imagem da Assinatura -->
      <div class="footer-image-container mb-3">
        <img
          src="/src/assets/img/assinaturaUFDPar.png"
          alt="Assinatura UFDPar"
          class="footer-image"
        />
      </div>

      <!-- Linha dourada preenchendo toda a largura -->
      <div class="line-container">
        <hr class="elegant-line" />
      </div>

      <!-- Copyright -->
      <div class="footer-text-container mt-4">
        <p class="mb-0 text-secondary footer-text">
          Copyright © {{ new Date().getFullYear() }} Portal do Egresso da
          Universidade Federal do Delta do Parnaíba.
        </p>
      </div>
    </div>
  </footer>
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
            {
              title: "Desenvolvedor Backend",
              description:
                "Vaga para desenvolvedor backend com experiência em Node.js.",
            },
            {
              title: "Gerente de Projetos",
              description: "Gerente de Projetos para atuar em tecnologia.",
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
            {
              title: "Estágio em TI",
              description: "Suporte técnico e redes.",
            },
            {
              title: "Estágio em Desenvolvimento",
              description: "Desenvolvimento de aplicações web.",
            },
            {
              title: "Estágio em Design",
              description: "Criação de layouts e design gráfico.",
            },
          ],
          icon: "bi bi-person-badge",
        },
        {
          id: "mentorias",
          name: "Mentorias",
          title: "Programas de Mentoria",
          description: "Programas de mentoria para egressos.",
          items: [
            {
              title: "Mentoria em Carreira",
              description: "Orientação sobre desenvolvimento de carreira.",
            },
            {
              title: "Mentoria em Tecnologia",
              description: "Apoio e dicas sobre tecnologia e inovação.",
            },
          ],
          icon: "bi bi-lightbulb",
        },
        {
          id: "cursos",
          name: "Cursos",
          title: "Cursos Disponíveis",
          description: "Cursos oferecidos para egressos.",
          items: [
            {
              title: "Curso de Python",
              description: "Aprenda a programar em Python do zero.",
            },
            {
              title: "Curso de Design Gráfico",
              description: "Aprenda as ferramentas de design gráfico.",
            },
          ],
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

/* Alinhamento das abas */
.nav-pills .nav-link {
  border-radius: 0.5rem; /* Bordas arredondadas */
}

/* Estilo do conteúdo da aba */
.animated-card {
  transition: transform 0.3s ease; /* Transição suave para o cartão */
}

.animated-card:hover {
  transform: scale(1.05); /* Efeito de zoom ao passar o mouse */
}

.selected-button {
  background-color: #0056b3; /* Cor de fundo da aba ativa */
  color: white; /* Cor do texto da aba ativa */
}

.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra sutil para o cartão */
}

/* Estilo do botão */
.btn {
  background-color: #007bff; /* Azul suave */
  color: white; /* Texto branco para contraste */
  transition: background-color 0.2s ease; /* Transição suave para o botão */
  border: none; /* Removendo borda */
}

.btn:hover {
  background-color: #0056b3; /* Tom mais escuro ao passar o mouse */
}

/* Footer Custom Styles */
.footer-custom {
  background-color: #003366; /* Azul forte */
  padding: 2rem 0;
  color: white;
  position: relative; /* Para permitir o posicionamento absoluto dos ornamentos */
}

/* Estilo para a imagem de assinatura */
.footer-image-container {
  max-width: 250px; /* Tamanho máximo da imagem ajustado */
  margin: 0 auto; /* Centraliza a imagem */
}

.footer-image {
  max-width: 100%; /* Garante que a imagem não ultrapasse o container */
  border: none; /* Removendo a borda */
  border-radius: 0; /* Sem bordas arredondadas */
  box-shadow: none; /* Removendo a sombra */
  transition: transform 0.3s ease; /* Transição suave para efeito de hover */
}

/* Efeito de hover na imagem */
.footer-image:hover {
  transform: scale(1.05); /* Aumenta levemente a imagem ao passar o mouse */
}

/* Estilo do container da linha */
.line-container {
  margin: 2rem 0; /* Remover margem lateral */
  width: 100%; /* Faz a linha ocupar toda a largura da tela */
}

/* Linha dourada com design aprimorado */
.elegant-line {
  border: none;
  height: 6px; /* Aumenta a altura da linha para mais presença */
  background-image: linear-gradient(
    to right,
    #ffd700,
    /* Dourado vibrante */ #ffcc00,
    /* Dourado mais claro */ #ffd700 /* Dourado vibrante novamente */
  ); /* Gradiente dourado */
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.8); /* Sombra suave para efeito 3D */
  border-radius: 5px; /* Bordas arredondadas */
  width: 100%; /* Largura da linha ajustada para 100% */
}

/* Pequeno ornamento decorativo nas pontas da linha */
.elegant-line::before,
.elegant-line::after {
  content: "";
  width: 14px; /* Aumenta o tamanho dos ornamentos */
  height: 14px;
  background-color: #ffd700; /* Dourado sólido */
  border-radius: 50%; /* Ornamento circular nas extremidades */
  position: absolute;
  top: -7px; /* Ajusta a posição do ornamento */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Sombra para profundidade */
}

.elegant-line::before {
  left: -10px; /* Alinhamento do ornamento esquerdo */
}

.elegant-line::after {
  right: -10px; /* Alinhamento do ornamento direito */
}

/* Estilo do texto copyright */
.footer-text {
  font-size: 1rem; /* Aumenta o tamanho da fonte para maior legibilidade */
  line-height: 1.5; /* Aumenta o espaço entre linhas */
}

/* Ajustes para a cor do texto */
.text-secondary {
  color: #e0e0e0; /* Tom de cinza suave */
}

/* Responsividade */
@media (max-width: 768px) {
  .footer-text {
    font-size: 0.9rem; /* Tamanho da fonte reduzido em telas menores */
  }
}
</style>
