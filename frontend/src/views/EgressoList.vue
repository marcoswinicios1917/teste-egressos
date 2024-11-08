<!-- src/views/EgressoList.vue -->
<template>
  <div class="container mt-5">
    <h1>Lista de Egressos</h1>
    <p>Aqui será exibida a lista de egressos.</p>
    <!-- Adicione o código necessário para listar egressos aqui -->
  </div>
</template>

<script>
export default {
  name: "EgressoList",
  data() {
    return {
      egressos: [], // array para armazenar a lista de egressos
    };
  },
  created() {
    // Aqui você pode adicionar a lógica para buscar a lista de egressos da API
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
