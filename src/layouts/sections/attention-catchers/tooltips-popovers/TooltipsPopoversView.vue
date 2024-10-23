<template>
  <BaseLayout
    title="Oportunidades"
    :breadcrumb="[
      { label: 'Portal do Egresso', route: '#' },
      { label: 'Oportunidades' },
    ]"
  >
    <div class="container mt-5">
      <!-- Navegação por abas para diferentes oportunidades -->
      <ul
        class="nav nav-pills mb-4 justify-content-center"
        id="pills-tab"
        role="tablist"
        style="margin-top: 50px"
      >
        <!-- Ajuste de margem -->
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            :class="{ active: activeTab === 'empregos' }"
            @click="setActiveTab('empregos')"
            role="tab"
            aria-controls="pills-empregos"
            aria-selected="activeTab === 'empregos'"
          >
            <i class="bi bi-briefcase me-1"></i> Empregos
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            :class="{ active: activeTab === 'estagios' }"
            @click="setActiveTab('estagios')"
            role="tab"
            aria-controls="pills-estagios"
            aria-selected="activeTab === 'estagios'"
          >
            <i class="bi bi-person-badge me-1"></i> Estágios
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            :class="{ active: activeTab === 'mentorias' }"
            @click="setActiveTab('mentorias')"
            role="tab"
            aria-controls="pills-mentorias"
            aria-selected="activeTab === 'mentorias'"
          >
            <i class="bi bi-lightbulb me-1"></i> Mentorias
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            :class="{ active: activeTab === 'cursos' }"
            @click="setActiveTab('cursos')"
            role="tab"
            aria-controls="pills-cursos"
            aria-selected="activeTab === 'cursos'"
          >
            <i class="bi bi-book me-1"></i> Cursos
          </button>
        </li>
      </ul>

      <div class="tab-content" id="pills-tabContent">
        <!-- Seção de Empregos -->
        <div
          class="tab-pane fade"
          :class="{
            show: activeTab === 'empregos',
            active: activeTab === 'empregos',
          }"
          id="pills-empregos"
          role="tabpanel"
        >
          <h3 class="text-center my-4">Oportunidades de Emprego</h3>
          <p class="text-center">
            Explore as últimas vagas de emprego disponíveis para egressos.
            Aproveite as oportunidades!
          </p>
          <div class="row">
            <div class="col-md-6 col-lg-4 mb-4">
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">Desenvolvedor Front-end</h5>
                  <p class="card-text">
                    Empresa X procura um desenvolvedor com experiência em Vue.js
                    e JavaScript. Salário competitivo.
                  </p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails('Desenvolvedor Front-end')"
                  >
                    Ver Detalhes
                  </button>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4">
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">Analista de Dados</h5>
                  <p class="card-text">
                    Vaga para Analista de Dados com habilidades em SQL e Python.
                    Ótima equipe!
                  </p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails('Analista de Dados')"
                  >
                    Ver Detalhes
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Seção de Estágios -->
        <div
          class="tab-pane fade"
          :class="{
            show: activeTab === 'estagios',
            active: activeTab === 'estagios',
          }"
          id="pills-estagios"
          role="tabpanel"
        >
          <h3 class="text-center my-4">Oportunidades de Estágio</h3>
          <p class="text-center">
            Aproveite as oportunidades de estágio para ganhar experiência
            prática e se preparar para o mercado.
          </p>
          <div class="row">
            <div class="col-md-6 col-lg-4 mb-4">
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">Estágio em Marketing</h5>
                  <p class="card-text">
                    Empresa Y oferece estágio em Marketing Digital para
                    estudantes de Publicidade.
                  </p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails('Estágio em Marketing')"
                  >
                    Ver Detalhes
                  </button>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4">
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">Estágio em TI</h5>
                  <p class="card-text">
                    Empresa Z busca estagiários de TI com foco em suporte
                    técnico e redes.
                  </p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails('Estágio em TI')"
                  >
                    Ver Detalhes
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Seção de Mentorias -->
        <div
          class="tab-pane fade"
          :class="{
            show: activeTab === 'mentorias',
            active: activeTab === 'mentorias',
          }"
          id="pills-mentorias"
          role="tabpanel"
        >
          <h3 class="text-center my-4">Programas de Mentoria</h3>
          <p class="text-center">
            Participe de programas de mentoria para desenvolver suas habilidades
            e expandir sua rede de contatos.
          </p>
          <div class="row">
            <div class="col-md-6 col-lg-4 mb-4">
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">Mentoria em Carreira</h5>
                  <p class="card-text">
                    Programa de mentoria voltado para direcionamento de carreira
                    em tecnologia.
                  </p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails('Mentoria em Carreira')"
                  >
                    Ver Detalhes
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Seção de Cursos -->
        <div
          class="tab-pane fade"
          :class="{
            show: activeTab === 'cursos',
            active: activeTab === 'cursos',
          }"
          id="pills-cursos"
          role="tabpanel"
        >
          <h3 class="text-center my-4">Cursos e Workshops</h3>
          <p class="text-center">
            Aprimore suas habilidades com cursos e workshops práticos em várias
            áreas de conhecimento.
          </p>
          <div class="row">
            <div class="col-md-6 col-lg-4 mb-4">
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">Curso de JavaScript Avançado</h5>
                  <p class="card-text">
                    Curso intensivo para aprimorar habilidades em JavaScript e
                    frameworks modernos.
                  </p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails('Curso de JavaScript Avançado')"
                  >
                    Ver Detalhes
                  </button>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-4 mb-4">
              <div class="card h-100 animated-card">
                <div class="card-body">
                  <h5 class="card-title">Workshop de UX Design</h5>
                  <p class="card-text">
                    Aprenda sobre UX Design em um workshop prático com
                    especialistas da área.
                  </p>
                  <button
                    class="btn btn-primary animated-button"
                    @click="showDetails('Workshop de UX Design')"
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

<script setup>
import { ref } from "vue";

// Sections components
import BaseLayout from "../../components/BaseLayout.vue";

// Definindo a aba ativa como 'empregos'
const activeTab = ref("empregos");

// Função para definir a aba ativa
function setActiveTab(tab) {
  activeTab.value = tab;
}

// Função para exibir detalhes da oportunidade
function showDetails(opportunity) {
  alert(`Detalhes da oportunidade: ${opportunity}`);
}
</script>

<style scoped>
/* Adicionando animações e estilos personalizados */
.animated-card {
  transition: transform 0.2s;
}
.animated-card:hover {
  transform: scale(1.05);
}
.animated-button {
  transition: background-color 0.2s, color 0.2s;
}
.animated-button:hover {
  background-color: #0056b3;
  color: white;
}
</style>
