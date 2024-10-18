<script setup>
// import { onMounted, onUnmounted } from "vue";

// Example components
import NavbarDefault from "../../examples/navbars/NavbarDefault.vue";
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
// const body = document.getElementsByTagName("body")[0];
// onMounted(() => {
//   body.classList.add("presentation-page");
//   body.classList.add("bg-gray-200");
// });
// onUnmounted(() => {
//   body.classList.remove("presentation-page");
//   body.classList.remove("bg-gray-200");
// });
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
  padding-top: 1.4rem;
  padding-bottom: 0rem;
}

.page-header {
  height: 60vh; /* Ajusta a altura do cabeçalho para 100% da viewport */
  background-size: contain; /* Faz a imagem aparecer completa */
  background-position: top; /* Alinha a imagem no topo */
  background-repeat: no-repeat; /* Impede que a imagem se repita */
  margin-top: 60px; /* Move a imagem um pouco para baixo, alinhando com o Navbar */
  background-color: transparent; /* Fundo transparente */
}

.content-section {
  padding: 0rem 0rem;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 0;
}

@media (max-width: 768px) {
  .page-header {
    height: 100vh; /* Mantém a altura total em telas menores */
    background-size: contain;
  }
}

@media (max-width: 576px) {
  .content-section {
    padding: 1rem;
  }
}
</style>
