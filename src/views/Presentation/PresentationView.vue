<script setup>
import { onMounted, onUnmounted } from "vue";

// Example components
import NavbarDefault from "../..//examples/navbars/NavbarDefault.vue";
import DefaultFooter from "../../examples/footers/FooterDefault.vue";
import Header from "../../examples/Header.vue";
import PresentationCounter from "./Sections/PresentationCounter.vue";
import PresentationPages from "./Sections/PresentationPages.vue";
import PresentationExample from "./Sections/PresentationExample.vue";
import BuiltByDevelopers from "./Components/BuiltByDevelopers.vue";
import PresentationTestimonials from "./Sections/PresentationTestimonials.vue";
import PresentationInformation from "./Sections/PresentationInformation.vue";

// Images
import vueMkHeader from "@/assets/img/vue-mk-header.jpg";

// Hooks
const body = document.getElementsByTagName("body")[0];
onMounted(() => {
  body.classList.add("presentation-page");
  body.classList.add("bg-gray-200");
});
onUnmounted(() => {
  body.classList.remove("presentation-page");
  body.classList.remove("bg-gray-200");
});
</script>

<template>
  <div class="container-fluid position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <NavbarDefault :sticky="true" />
      </div>
    </div>
  </div>
  <Header>
    <div
      class="page-header"
      :style="`background-image: url(${vueMkHeader});`"
      loading="lazy"
    ></div>
  </Header>

  <div class="content-section">
    <PresentationCounter />
    <PresentationInformation />
    <PresentationExample :data="data" />
    <PresentationPages />
    <BuiltByDevelopers />
    <PresentationTestimonials />
  </div>

  <DefaultFooter />
</template>

<style scoped>
.container-fluid {
  padding: 0;
}

.page-header {
  height: 90vh; /* Ajusta a altura do cabeçalho */
  background-size: cover;
  background-position: center;
  margin-top: -20vh; /* Move a imagem para cima */
}

.content-section {
  padding: 2rem 1rem; /* Adiciona um espaçamento interno para a seção de conteúdo */
  background-color: rgba(
    255,
    255,
    255,
    0.9
  ); /* Fundo claro para destacar o conteúdo */
  border-radius: 0; /* Remove bordas arredondadas */
}

@media (max-width: 768px) {
  .page-header {
    height: 70vh; /* Altura do cabeçalho para telas menores */
    margin-top: -10vh; /* Move a imagem para cima em telas menores */
  }
}

@media (max-width: 576px) {
  .content-section {
    padding: 1rem; /* Ajusta o padding em telas menores */
  }
}
</style>
