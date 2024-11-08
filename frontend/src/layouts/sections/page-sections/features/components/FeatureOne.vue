<template>
  <div class="admin-dashboard">
    <div class="container">
      <section class="dashboard-overview">
        <h2>Visão Geral</h2>
        <div class="stats">
          <div class="stat">
            <h3>Total de Egressos</h3>
            <p>{{ totalEgressos }}</p>
          </div>
          <div class="stat">
            <h3>Eventos Realizados</h3>
            <p>{{ totalEventos }}</p>
          </div>
          <div class="stat">
            <h3>Taxa de Participação</h3>
            <p>{{ taxaParticipacao }}%</p>
          </div>
        </div>
      </section>

      <section class="gerenciamento">
        <h2>Gerenciamento de Egressos</h2>
        <div class="filter">
          <input
            type="text"
            placeholder="Buscar Egressos"
            v-model="egressoSearch"
            aria-label="Buscar Egressos"
          />
          <button @click="addEgresso">Adicionar Egresso</button>
        </div>
        <table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Status</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="egresso in filteredEgressos" :key="egresso.id">
              <td>{{ egresso.name }}</td>
              <td>{{ egresso.status }}</td>
              <td>
                <button @click="editEgresso(egresso)">Editar</button>
                <button @click="removeEgresso(egresso.id)">Remover</button>
              </td>
            </tr>
          </tbody>
        </table>
      </section>

      <section class="relatorios">
        <h2>Relatórios</h2>
        <button @click="generateReport">Gerar Relatório</button>
      </section>

      <section class="historico">
        <h2>Histórico de Eventos</h2>
        <ul>
          <li v-for="evento in eventosHistorico" :key="evento.id">
            {{ evento.name }} - {{ evento.date }}
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

// Estado reativo para os egressos e eventos
const egressoSearch = ref("");

const egressos = ref([
  { id: 1, name: "Maria Oliveira", status: "Ativo" },
  { id: 2, name: "João Silva", status: "Inativo" },
  // Adicione mais egressos conforme necessário
]);

const eventosHistorico = ref([
  { id: 1, name: "Reunião de Egressos", date: "01/01/2024" },
  { id: 2, name: "Workshop de Carreira", date: "15/02/2024" },
  // Adicione mais eventos conforme necessário
]);

// Computed properties para os totais e filtragem
const totalEgressos = computed(() => egressos.value.length);
const totalEventos = computed(() => eventosHistorico.value.length);
const taxaParticipacao = computed(() => {
  return Math.round(Math.random() * 100); // Simulação
});

const filteredEgressos = computed(() => {
  return egressos.value.filter((egresso) =>
    egresso.name.toLowerCase().includes(egressoSearch.value.toLowerCase())
  );
});

// Métodos para manipular os egressos e gerar relatórios
const addEgresso = () => {
  alert("Adicionar novo egresso.");
};

const editEgresso = (egresso) => {
  alert(`Editar egresso: ${egresso.name}`);
};

const removeEgresso = (id) => {
  egressos.value = egressos.value.filter((egresso) => egresso.id !== id);
};

const generateReport = () => {
  alert("Relatório gerado com sucesso!");
};
</script>

<style scoped>
.admin-dashboard {
  font-family: Arial, sans-serif;
  background-color: #f8f9fa;
  padding: 20px;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
}

section {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  border-bottom: 2px solid #007bff;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.stats {
  display: flex;
  gap: 20px;
}

.stat {
  background-color: #f0f4f8;
  padding: 20px;
  border-radius: 8px;
  flex: 1;
  text-align: center;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.filter {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

input[type="text"] {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}
</style>
