<script setup>
defineProps({
  socials: {
    type: Array,
    default: () => [
      {
        icon: '<i class="fab fa-facebook text-lg opacity-8"></i>',
        link: "https://www.facebook.com/CreativeTim/",
      },
      {
        icon: '<i class="fab fa-twitter text-lg opacity-8"></i>',
        link: "https://twitter.com/creativetim",
      },
      {
        icon: '<i class="fab fa-dribbble text-lg opacity-8"></i>',
        link: "https://dribbble.com/creativetim",
      },
      {
        icon: '<i class="fab fa-github text-lg opacity-8"></i>',
        link: "https://github.com/creativetimofficial",
      },
      {
        icon: '<i class="fab fa-youtube text-lg opacity-8"></i>',
        link: "https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w",
      },
    ],
  },
  links: {
    type: Array,
    default: () => [
      { href: "https://www.creative-tim.com/", name: "Company" },
      { href: "https://www.creative-tim.com/presentation", name: "About Us" },
      { href: "https://www.creative-tim.com/presentation", name: "Team" },
      {
        href: "https://www.creative-tim.com/templates/vuejs",
        name: "Products",
      },
      { href: "https://www.creative-tim.com/blog", name: "Blog" },
      { href: "https://www.creative-tim.com/license", name: "License" },
    ],
  },
});
</script>

<template>
  <footer class="footer py-5">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 mb-4 mx-auto text-center">
          <a
            v-for="{ name, href } of links"
            :key="name"
            :href="href"
            target="_blank"
            class="text-secondary me-xl-5 me-3 mb-sm-0 mb-2"
          >
            {{ name }}
          </a>
        </div>
        <div class="col-lg-8 mx-auto text-center mb-4 mt-2">
          <div class="socials-container">
            <a
              v-for="{ icon, link } of socials"
              :key="link"
              :href="link"
              target="_blank"
              class="social-icon"
              v-html="icon"
            ></a>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-8 mx-auto text-center mt-1">
          <p class="mb-0 text-secondary">
            Copyright © {{ new Date().getFullYear() }} Material by Creative Tim.
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #f8f9fa; /* Cor de fundo do footer */
}

.socials-container {
  display: flex; /* Exibe os ícones em linha */
  justify-content: center; /* Centraliza os ícones */
  flex-wrap: wrap; /* Permite a quebra de linha se necessário */
}

.social-icon {
  display: flex; /* Exibe os ícones como flex items */
  align-items: center; /* Centraliza verticalmente */
  justify-content: center; /* Centraliza horizontalmente */
  width: 40px; /* Largura do quadrado */
  height: 40px; /* Altura do quadrado */
  border-radius: 50%; /* Bordas arredondadas para o quadrado */
  background-color: rgba(
    255,
    255,
    255,
    0.8
  ); /* Fundo branco com transparência */
  margin: 5px; /* Espaçamento entre os ícones */
  transition: background-color 0.3s; /* Transição suave para hover */
}

.social-icon:hover {
  background-color: #007bff; /* Cor ao passar o mouse */
  color: white; /* Cor do ícone ao passar o mouse */
}
</style>
