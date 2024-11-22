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
              Nossa caminhada juntos não acaba com sua diplomação! O sucesso de
              nossos egressos expressam nosso êxito enquanto instituição
              formadora, por esse motivo, precisamos manter com você que
              concluiu a graduação, mestrado ou doutorado na Universidade
              Federal do Delta do Parnaíba um relacionamento contínuo, vivo. A
              plataforma de egressos tem esse objetivo maior: de continuidade de
              nossa história! Este é o espaço de diálogo no qual buscamos
              conhecer sua trajetória após a conclusão de curso e promover o
              acesso à formação continuada e desenvolvimento profissional;
              avaliar nossos cursos de graduação e pós- graduação, políticas
              educacionais e nossa capacidade de atendimento às demandas
              sociais. Importante também promovermos a aproximação e articulação
              entre nossos egressos e discentes dos cursos de graduação e
              programas de pós-graduação no sentido de avançarmos nas melhorias
              de nossas políticas, estratégias e ações educativas. Esse espaço
              possibilita ainda informar à sociedade os resultados alcançados
              pela UFDPar, enquanto instituição formadora. Neste sentido,
              convidamos a responder o Questionário do Egresso disponível nesta
              plataforma. Este espaço é seu! Contribua com sua construção.
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
  border: groove;
  border: 2px dashed;
  border-radius: 35px; /* Bordas mais retas para um visual mais moderno */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15); /* Sombra suave para dar profundidade */
  transition: transform 0.2s ease, box-shadow 0.2s ease; /* Transição suave para efeitos de hover */
}

.btn-dark-blue:hover {
  transform: translateY(-8px); /* Eleva levemente o botão ao passar o mouse */
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
