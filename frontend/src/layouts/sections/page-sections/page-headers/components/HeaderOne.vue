<script setup>
import { ref } from "vue";
import MaterialButton from "@/components/MaterialButton.vue"; // Botões reutilizáveis

// Dados simulados
const courses = [
  "Engenharia",
  "Medicina",
  "Direito",
  "Ciência da Computação",
  "Administração",
];
const statuses = [
  "Empregado",
  "Empreendendo",
  "Estudando",
  "Disponível para contratação",
];
const areas = [
  "Tecnologia",
  "Saúde",
  "Engenharia",
  "Direito",
  "Negócios",
  "Educação",
];

// Gera os anos disponíveis para o seletor
const currentYear = new Date().getFullYear();
const years = Array.from({ length: 30 }, (_, i) => currentYear - i);
const selectedYear = ref(null);
</script>

<template>
  <div class="search-page">
    <!-- Formulário de Pesquisa -->
    <section class="search-form">
      <h1 class="form-title">Busque por Egressos</h1>
      <form
        @submit.prevent="searchEgressos"
        class="rounded shadow bg-white p-4"
      >
        <div class="form-grid">
          <!-- Nome -->
          <div>
            <label for="name" class="form-label">Nome Completo</label>
            <input
              type="text"
              id="name"
              class="form-control"
              placeholder="Digite o nome do egresso"
            />
          </div>

          <!-- Curso -->
          <div>
            <label for="course" class="form-label">Curso</label>
            <select id="course" class="form-select">
              <option value="" disabled selected>Selecione um curso</option>
              <option v-for="course in courses" :key="course">
                {{ course }}
              </option>
            </select>
          </div>

          <!-- Ano de Conclusão -->
          <div>
            <label for="year" class="form-label">Ano de Conclusão</label>
            <select id="year" class="form-select" v-model="selectedYear">
              <option value="" disabled selected>Selecione um ano</option>
              <option v-for="year in years" :key="year" :value="year">
                {{ year }}
              </option>
            </select>
          </div>

          <!-- Área de Atuação -->
          <div>
            <label for="area" class="form-label">Área de Atuação</label>
            <select id="area" class="form-select">
              <option value="" disabled selected>Selecione uma área</option>
              <option v-for="area in areas" :key="area">{{ area }}</option>
            </select>
          </div>

          <!-- Status no Mercado -->
          <div>
            <label for="status" class="form-label">Status no Mercado</label>
            <select id="status" class="form-select">
              <option value="" disabled selected>Selecione o status</option>
              <option v-for="status in statuses" :key="status">
                {{ status }}
              </option>
            </select>
          </div>
        </div>
        <div class="text-center mt-4">
          <MaterialButton color="primary">Pesquisar</MaterialButton>
        </div>
      </form>
    </section>

    <!-- Resultados da Pesquisa -->
    <section class="search-results">
      <h2 class="results-title">Resultados da Pesquisa</h2>
      <div class="results-grid">
        <!-- Simulação de Resultados -->
        <div class="card" v-for="n in 12" :key="n">
          <div class="card-body">
            <h6 class="card-title">Egresso {{ n }}</h6>
            <p class="card-text">
              <strong>Curso:</strong> {{ courses[n % courses.length] }}<br />
              <strong>Ano de Conclusão:</strong> 20{{ n + 10 }}<br />
              <strong>Status:</strong> {{ statuses[n % statuses.length] }}
            </p>
            <a href="#" class="btn btn-primary btn-sm">Ver Perfil</a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Página Principal */
.search-page {
  background: linear-gradient(to bottom right, #f0f4f9, #ffffff);
  padding: 40px;
  font-family: "Arial", sans-serif;
}

/* Formulário */
.search-form {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  padding: 30px;
  margin-bottom: 40px;
}

.form-title {
  font-size: 2rem;
  color: #343a40;
  margin-bottom: 20px;
  text-align: center;
}

/* Grid do Formulário */
.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.form-label {
  font-weight: 600;
  margin-bottom: 5px;
  color: #495057;
}

.form-control,
.form-select {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
  background: #f8f9fa;
}

.form-control:focus,
.form-select:focus {
  border-color: #1976d2;
  box-shadow: 0px 4px 8px rgba(25, 118, 210, 0.2);
}

/* Resultados */
.search-results {
  padding: 20px 0;
}

.results-title {
  font-size: 1.8rem;
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}

/* Cards */
.card {
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.card-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #1976d2;
  margin-bottom: 10px;
}

.card-text {
  font-size: 0.95rem;
  color: #555;
}

.btn-primary {
  background-color: #1976d2;
  border: none;
  border-radius: 5px;
  padding: 8px 15px;
  font-size: 0.85rem;
  transition: background-color 0.3s;
  color: white;
}

.btn-primary:hover {
  background-color: #0d47a1;
}
</style>
