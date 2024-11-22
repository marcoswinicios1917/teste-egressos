<template>
  <BaseLayout
    :breadcrumb="[
      {
        label: 'Seções da Página',
        route: '/sections/page-sections/page-headers',
      },
      { label: 'Histórias de Egressos' },
    ]"
  >
    <section class="">
      <!-- <h1 class="egress-title">🎓 Formulário de Egressos</h1> -->
      <View :code="header1Code" id="header-1">
        <HeaderOne />
      </View>
    </section>
  </BaseLayout>
</template>

<script setup>
import { onMounted } from "vue";
import BaseLayout from "../../components/BaseLayout.vue";
import View from "../../components/View.vue";
import HeaderOne from "./components/HeaderOne.vue";
import { header1Code } from "./components/codes";
import setNavPills from "@/assets/js/nav-pills.js";

onMounted(() => {
  setNavPills();
});
</script>

<style scoped>
.egress-section {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Alinhado à esquerda */
  padding: 80px 15px;
  background-color: #f7f9fc;
  border-radius: 10px; /* Cantos arredondados para um visual mais suave */
}

.egress-title {
  font-size: 2.4rem; /* Aumentado para destaque */
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 0px; /* Aumentado para espaçamento */
  margin-left: 0; /* Remover margem padrão */
}

.view-container {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Sombra mais sutil */
  padding: 30px;
  transition: box-shadow 0.3s ease; /* Transição mais suave */
  width: 100%; /* Largura total para responsividade */
  max-width: 800px; /* Largura máxima para manter a legibilidade */
}

.view-container:hover {
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2); /* Sombra mais forte ao passar o mouse */
}

@media (max-width: 768px) {
  .egress-section {
    padding: 20px 10px; /* Redução do padding em telas menores */
  }

  .egress-title {
    font-size: 2rem; /* Reduzido para melhor encaixe em telas pequenas */
  }
}
</style>
