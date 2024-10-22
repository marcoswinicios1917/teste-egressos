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
    <section class="search-form py-5">
      <div class="container">
        <div class="row">
          <div class="col-lg-10 mx-auto">
            <h1 class="text-center mb-4">Busque por Egressos</h1>
            <form
              @submit.prevent="searchEgressos"
              class="rounded shadow p-4 bg-white"
            >
              <div class="row">
                <!-- Nome -->
                <div class="col-md-6 mb-4">
                  <label for="name" class="form-label">
                    <i class="bi bi-person-fill"></i> Nome Completo
                  </label>
                  <input
                    type="text"
                    id="name"
                    class="form-control"
                    placeholder="Digite o nome do egresso"
                  />
                </div>

                <!-- Curso -->
                <div class="col-md-6 mb-4">
                  <label for="course" class="form-label">
                    <i class="bi bi-book-fill"></i> Curso
                  </label>
                  <select id="course" class="form-select">
                    <option value="" disabled selected>
                      Selecione um curso
                    </option>
                    <option v-for="course in courses" :key="course">
                      {{ course }}
                    </option>
                  </select>
                </div>

                <!-- Ano de Conclusão -->
                <div class="col-md-6 mb-4">
                  <label for="year" class="form-label">
                    <i class="bi bi-calendar-fill"></i> Ano de Conclusão
                  </label>
                  <select id="year" class="form-select" v-model="selectedYear">
                    <option value="" disabled selected>Selecione um ano</option>
                    <option v-for="year in years" :key="year" :value="year">
                      {{ year }}
                    </option>
                  </select>
                </div>

                <!-- Área de Atuação -->
                <div class="col-md-6 mb-4">
                  <label for="area" class="form-label">
                    <i class="bi bi-briefcase-fill"></i> Área de Atuação
                  </label>
                  <select id="area" class="form-select">
                    <option value="" disabled selected>
                      Selecione uma área
                    </option>
                    <option v-for="area in areas" :key="area">
                      {{ area }}
                    </option>
                  </select>
                </div>

                <!-- Status no Mercado -->
                <div class="col-md-6 mb-4">
                  <label for="status" class="form-label">
                    <i class="bi bi-people-fill"></i> Status no Mercado
                  </label>
                  <select id="status" class="form-select">
                    <option value="" disabled selected>
                      Selecione o status
                    </option>
                    <option v-for="status in statuses" :key="status">
                      {{ status }}
                    </option>
                  </select>
                </div>

                <!-- Botões -->
                <div class="col-md-12 text-center">
                  <MaterialButton color="primary" class="mt-3 px-5">
                    Pesquisar
                  </MaterialButton>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- Resultados da Pesquisa -->
    <section class="search-results py-5 bg-light">
      <div class="container">
        <h2 class="text-center mb-4">Resultados da Pesquisa</h2>
        <div class="row">
          <!-- Simulação de Resultados -->
          <div class="col-md-4" v-for="n in 6" :key="n">
            <div class="card mb-4 shadow-sm bg-white">
              <img
                src="https://via.placeholder.com/400x300"
                class="card-img-top"
                alt="Foto do Egresso"
              />
              <div class="card-body">
                <h5 class="card-title">Egresso {{ n }}</h5>
                <p class="card-text">
                  <strong>Curso:</strong> {{ courses[n % courses.length]
                  }}<br />
                  <strong>Ano de Conclusão:</strong> 20{{ n + 10 }}<br />
                  <strong>Status:</strong> {{ statuses[n % statuses.length] }}
                </p>
                <a href="#" class="btn btn-primary">Ver Perfil</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.search-page {
  background: linear-gradient(to bottom right, #e3f2fd, #ffffff);
}

.search-form {
  background-color: #ffffff;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
}

.search-form .form-label {
  font-weight: bold;
  color: #1976d2;
}

.form-control,
.form-select {
  border-radius: 8px;
  transition: border-color 0.3s;
}

.form-control:focus,
.form-select:focus {
  border-color: #1976d2;
  box-shadow: 0 0 0 0.2rem rgba(25, 118, 210, 0.25);
}

.search-results .card {
  transition: transform 0.2s;
}

.search-results .card:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

.search-results .card-title {
  font-size: 1.25rem;
  color: #0d47a1;
}

.btn-primary {
  background-color: #1976d2;
  border: none;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #0d47a1;
}

.icon {
  color: #1976d2;
  margin-right: 8px;
}
</style>
