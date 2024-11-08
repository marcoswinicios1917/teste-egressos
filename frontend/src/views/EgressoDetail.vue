<!-- src/views/EgressoDetail.vue -->

<template>
  <div class="container mt-5">
    <h1>Detalhes do Egresso</h1>
    <div v-if="egressoData">
      <p><strong>Nome Completo:</strong> {{ egressoData.nome_completo }}</p>
      <p><strong>Gênero:</strong> {{ egressoData.genero }}</p>
      <p>
        <strong>Data de Nascimento:</strong> {{ egressoData.data_nascimento }}
      </p>
      <p><strong>Nacionalidade:</strong> {{ egressoData.nacionalidade }}</p>
      <p><strong>Cor/Raça:</strong> {{ egressoData.cor_raca }}</p>
      <p>
        <strong>Pessoa com Deficiência:</strong>
        {{ egressoData.pessoa_com_deficiencia ? "Sim" : "Não" }}
      </p>
      <p><strong>Estado Civil:</strong> {{ egressoData.estado_civil }}</p>
      <p>
        <strong>Estado de Residência:</strong>
        {{ egressoData.estado_residencia }}
      </p>
      <p>
        <strong>Curso de Graduação:</strong> {{ egressoData.curso_graduacao }}
      </p>
      <p>
        <strong>Ano de Conclusão da Graduação:</strong>
        {{ egressoData.ano_conclusao_graduacao }}
      </p>
      <!-- Adicione outros campos conforme necessário -->
    </div>
    <div v-else>
      <p>Carregando dados do egresso...</p>
    </div>
  </div>
</template>

<script>
import getAPI from "@/axios-api.js";

export default {
  props: ["id"], // Recebe o ID do egresso pela URL
  data() {
    return {
      egressoData: null,
    };
  },
  async created() {
    try {
      // Faz a requisição à API para obter os dados do egresso com o ID passado
      const response = await getAPI.get(`egressos/${this.id}/`);
      this.egressoData = response.data;
    } catch (error) {
      console.error("Erro ao buscar os detalhes do egresso:", error);
    }
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
