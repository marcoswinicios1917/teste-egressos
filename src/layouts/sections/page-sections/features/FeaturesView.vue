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
        <div class="feature-icon">
          <i class="fas fa-cogs"></i>
          <!-- Exemplo de ícone, ajuste conforme necessário -->
        </div>
        <h3 class="feature-title">Sistema Administrativo de Egressos</h3>
        <p class="feature-description">
          Este sistema tem como objetivo gerenciar as informações dos egressos,
          facilitando o acesso a dados importantes e oferecendo suporte contínuo
          aos ex-alunos.
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
}

.feature-icon {
  font-size: 3rem; /* Tamanho do ícone */
  color: #007bff; /* Cor do ícone */
  text-align: center; /* Centralizar ícone */
  margin-bottom: 1rem; /* Espaçamento inferior */
}

.feature-title {
  text-align: center; /* Centralizar título */
  color: #343a40; /* Cor do título */
  margin-bottom: 0.5rem; /* Margem inferior */
}

.feature-description {
  text-align: center; /* Centralizar descrição */
  color: #6c757d; /* Cor da descrição */
  margin-bottom: 1rem; /* Margem inferior */
}
</style>
