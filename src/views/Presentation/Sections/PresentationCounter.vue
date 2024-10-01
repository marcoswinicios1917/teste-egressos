<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router"; // Importa o roteador do Vue
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faGraduationCap,
  faMapMarkedAlt,
  faBriefcase,
} from "@fortawesome/free-solid-svg-icons";

// Inicia o roteador
const router = useRouter();

// Função para lidar com o clique no botão "Egressos"
const navigateToEgressos = (event) => {
  if (event.ctrlKey) {
    window.open("/sections/page-sections/page-headers", "_blank");
  } else {
    router.push("/sections/page-sections/page-headers");
  }
};

// Função para lidar com o clique no botão "Mapa de Egressos"
const navigateToMapaEgressos = (event) => {
  if (event.ctrlKey) {
    window.open("/sections/input-areas/inputs", "_blank");
  } else {
    router.push("/sections/input-areas/inputs");
  }
};

// Função para lidar com o clique no botão "Oportunidades"
const navigateToOportunidades = (event) => {
  if (event.ctrlKey) {
    window.open("/sections/attention-catchers/tooltips-popovers", "_blank");
  } else {
    router.push("/sections/attention-catchers/tooltips-popovers");
  }
};

const buttons = ref([
  { name: "Egressos", icon: faGraduationCap, action: navigateToEgressos },
  {
    name: "Mapa de Egressos",
    icon: faMapMarkedAlt,
    action: navigateToMapaEgressos,
  },
  { name: "Oportunidades", icon: faBriefcase, action: navigateToOportunidades },
]);
</script>

<template>
  <section class="pt-3 pb-4" id="count-stats">
    <div class="container">
      <div class="row">
        <div class="col-lg-9 z-index-2 border-radius-xl mx-auto py-3">
          <div class="d-flex justify-content-between">
            <button
              v-for="button in buttons"
              :key="button.name"
              class="btn btn-dark-blue"
              :style="{
                flex: 1,
                margin: '0 5px',
                height: '150px',
                width: '150px',
                fontSize: '1.2rem',
                fontWeight: 'bold',
              }"
              @click="(event) => button.action(event)"
              @mousedown="(event) => event.preventDefault()"
            >
              <FontAwesomeIcon
                :icon="button.icon"
                class="me-2"
                style="font-size: 2rem"
              />
              <span>{{ button.name }}</span>
            </button>
          </div>
          <div class="text-content mt-4">
            <strong class="highlighted-title"
              >Acompanhamento de Egressos da UFDPar</strong
            >
            <p class="mt-3">
              O Programa de Acompanhamento de Egressos da UFDPar visa manter um
              elo constante entre a universidade e seus ex-alunos, celebrando
              suas conquistas e oferecendo apoio contínuo em sua trajetória
              profissional. Acreditamos que a relação da universidade com seus
              estudantes vai além da graduação, estendendo-se à construção de
              uma comunidade vibrante e interligada, que cresce junto com cada
              conquista pessoal e profissional. Nosso objetivo é entender o
              impacto da formação acadêmica na carreira dos egressos e
              identificar oportunidades para aprimorar ainda mais os cursos
              oferecidos. Dessa forma, o programa busca proporcionar suporte em
              termos de desenvolvimento profissional, networking e acesso a
              oportunidades no mercado de trabalho, criando uma rede de suporte
              mútuo entre a universidade e os ex-alunos. Através de pesquisas,
              eventos e atividades colaborativas, queremos acompanhar a evolução
              dos nossos egressos, ajudando-os a enfrentar os desafios do
              mercado de trabalho, conectar-se com outros profissionais e
              contribuir para a construção de um ambiente acadêmico cada vez
              mais qualificado. Mantendo esse vínculo, fortalecemos o
              compromisso da UFDPar em formar não apenas profissionais
              competentes, mas também cidadãos conscientes e ativos na
              sociedade. Participe de nossa rede e ajude a fortalecer o legado
              da UFDPar, contribuindo com sua experiência e mantendo viva a
              conexão com a universidade que fez parte da sua história. Juntos,
              podemos inspirar as futuras gerações e construir um futuro repleto
              de oportunidades.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-transform: uppercase;
  color: #ffffff; /* Texto em branco para contraste */
  background-color: #003366; /* Azul escuro */
  border: none;
  border-radius: 8px; /* Bordas mais retas para um visual mais moderno */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15); /* Sombra suave para dar profundidade */
  transition: transform 0.2s ease, box-shadow 0.2s ease; /* Transição suave para efeitos de hover */
}

.btn-dark-blue:hover {
  transform: translateY(-5px); /* Eleva levemente o botão ao passar o mouse */
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3); /* Aumenta a sombra para um efeito de elevação */
  background-color: #002244; /* Azul mais escuro ao passar o mouse */
}

.btn-dark-blue:active {
  transform: scale(0.95); /* Efeito de redução ao clicar */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15); /* Restaura a sombra ao clicar */
}

.btn span {
  margin-top: 10px; /* Espaçamento entre o ícone e o texto */
}

.text-content {
  text-align: center; /* Centraliza o texto abaixo dos botões */
}

.highlighted-title {
  font-size: 1.5rem;
  color: #003366; /* Destaque em azul escuro */
  text-transform: uppercase;
}
</style>
