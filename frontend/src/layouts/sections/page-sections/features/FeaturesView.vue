<script setup>
import { onMounted } from "vue";

// Sections components
import BaseLayout from "../../components/BaseLayout.vue";
import View from "../../components/View.vue";

// Features page components
import FeatureOne from "./components/FeatureOne.vue";

// Features page components codes
import { feature1Code } from "./components/codes";

// Nav pills
import setNavPills from "@/assets/js/nav-pills";

// Hook
onMounted(() => {
  setNavPills();
});
</script>

<template>
  <BaseLayout
    title="Features"
    :breadcrumb="[
      { label: 'Page Sections', route: '/sections/page-sections/page-headers' },
      { label: 'Features' },
    ]"
  >
    <View :code="feature1Code" id="feature-1">
      <div class="feature-container">
        <h3 class="feature-title">
          <i class="fas fa-cogs feature-icon"></i>
          Sistema Administrativo de Egressos
        </h3>
        <p class="feature-description">
          Gerencie as informações dos egressos de forma eficiente, facilitando o
          acesso a dados importantes e oferecendo suporte contínuo aos
          ex-alunos.
        </p>
        <FeatureOne />
      </div>
    </View>
  </BaseLayout>
</template>

<style scoped>
.feature-container {
  background: #f8f9fa; /* Fundo claro */
  border-radius: 0.5rem; /* Bordas arredondadas */
  padding: 2rem; /* Espaçamento interno */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Sombra */
  margin-top: 2rem; /* Margem superior */
  text-align: center; /* Centralizar todo o texto */
}

.feature-title {
  font-size: 1.75rem; /* Tamanho do título */
  color: #343a40; /* Cor do título */
  margin-bottom: 1rem; /* Margem inferior */
}

.feature-icon {
  font-size: 3rem; /* Tamanho do ícone */
  color: #007bff; /* Cor do ícone */
  display: inline-block; /* Permite centralizar o ícone com o título */
  margin-bottom: 0.5rem; /* Margem inferior */
}

.feature-description {
  color: #6c757d; /* Cor da descrição */
  margin-bottom: 1rem; /* Margem inferior */
  font-size: 1.1rem; /* Tamanho da fonte da descrição */
}
</style>
