<script setup>
import { onMounted, ref } from "vue";
import Chart from "chart.js/auto"; // Certifique-se de instalar o Chart.js com `npm install chart.js`

// Dados simulados para os gráficos
const egressosData = ref({
  total: 1500,
  employed: 1200,
  unemployed: 300,
  byYear: [
    { year: 2020, graduates: 200 },
    { year: 2021, graduates: 300 },
    { year: 2022, graduates: 500 },
    { year: 2023, graduates: 500 },
  ],
  byCourse: [
    { course: "Engenharia Pesca", employed: 400 },
    { course: "Medicina", employed: 300 },
    { course: "Economia", employed: 200 },
    { course: "Fisioterapia", employed: 150 },
    { course: "Psicologia", employed: 150 },
  ],
  byRegion: [
    { region: "Brasil", count: 1000 },
    { region: "EUA", count: 300 },
    { region: "Europa", count: 150 },
    { region: "Ásia", count: 50 },
  ],
  byQuotaDetailed: [
    { group: "PCD", count: 200 },
    { group: "Hipossuficientes", count: 300 },
    { group: "Preto/Pardo", count: 400 },
    { group: "Mescla", count: 100 },
    { group: "Não Cotistas", count: 500 },
  ],
  salaryByCourse: [
    { course: "Engenharia", avgSalary: 8000 },
    { course: "Medicina", avgSalary: 10000 },
    { course: "Direito", avgSalary: 6000 },
    { course: "Ciência da Computação", avgSalary: 7500 },
    { course: "Psicologia", avgSalary: 4500 },
  ],
});

// Criar gráficos ao montar o componente
onMounted(() => {
  const createCharts = () => {
    const chartConfigs = [
      {
        id: "totalChart",
        type: "pie",
        data: {
          labels: ["Empregados", "Desempregados"],
          datasets: [
            {
              data: [
                egressosData.value.employed,
                egressosData.value.unemployed,
              ],
              backgroundColor: ["#007bff", "#dc3545"],
            },
          ],
        },
      },
      {
        id: "byRegionChart",
        type: "doughnut",
        data: {
          labels: egressosData.value.byRegion.map((item) => item.region),
          datasets: [
            {
              data: egressosData.value.byRegion.map((item) => item.count),
              backgroundColor: ["#007bff", "#17a2b8", "#ffc107", "#6c757d"],
            },
          ],
        },
      },
      {
        id: "byYearChart",
        type: "line",
        data: {
          labels: egressosData.value.byYear.map((item) => item.year),
          datasets: [
            {
              label: "Formados",
              data: egressosData.value.byYear.map((item) => item.graduates),
              borderColor: "#28a745",
              fill: false,
            },
          ],
        },
      },
      {
        id: "byCourseChart",
        type: "bar",
        data: {
          labels: egressosData.value.byCourse.map((item) => item.course),
          datasets: [
            {
              label: "Empregados",
              data: egressosData.value.byCourse.map((item) => item.employed),
              backgroundColor: "#ffc107",
            },
          ],
        },
      },
      {
        id: "byQuotaDetailedChart",
        type: "bar",
        data: {
          labels: egressosData.value.byQuotaDetailed.map((item) => item.group),
          datasets: [
            {
              label: "Egressos",
              data: egressosData.value.byQuotaDetailed.map(
                (item) => item.count
              ),
              backgroundColor: [
                "#6f42c1",
                "#fd7e14",
                "#28a745",
                "#17a2b8",
                "#007bff",
              ],
            },
          ],
        },
      },
      {
        id: "salaryChart",
        type: "line",
        data: {
          labels: egressosData.value.salaryByCourse.map((item) => item.course),
          datasets: [
            {
              label: "Salário Médio (R$)",
              data: egressosData.value.salaryByCourse.map(
                (item) => item.avgSalary
              ),
              borderColor: "#dc3545",
              fill: false,
            },
          ],
        },
      },
    ];

    // Criar cada gráfico
    chartConfigs.forEach((config) => {
      const ctx = document.getElementById(config.id)?.getContext("2d");
      if (ctx) new Chart(ctx, config);
    });
  };

  createCharts();
});
</script>

<template>
  <div class="container mt-5">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container-fluid">
        <a href="/" class="navbar-brand">
          <img
            src="/src/assets/img/egressosufdpar.png"
            alt="Logo Egressos UFDPar"
            class="img-fluid logo"
          />
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div
          class="collapse navbar-collapse justify-content-end"
          id="navbarNav"
        >
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a href="/" class="nav-link">Home</a></li>
            <li class="nav-item">
              <a href="/sections/page-sections/page-headers" class="nav-link"
                >Pesquisa de Egressos</a
              >
            </li>
            <li class="nav-item">
              <a
                href="/sections/attention-catchers/tooltips-popovers"
                class="nav-link"
                >Oportunidades</a
              >
            </li>
            <li class="nav-item">
              <a href="/sections/navigation/navbars" class="nav-link"
                >Contatos</a
              >
            </li>
            <li class="nav-item">
              <a href="/sections/page-sections/features" class="nav-link active"
                >Administrativo</a
              >
            </li>
            <li class="nav-item">
              <a href="/pages/landing-pages/basic" class="nav-link">Entrar</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Filtros -->
    <div class="filters py-4">
      <div class="row">
        <div class="col-md-3">
          <label for="yearFilter">Ano de Graduação</label>
          <select id="yearFilter" class="form-select">
            <option>Todos</option>
            <option>2020</option>
            <option>2021</option>
            <option>2022</option>
            <option>2023</option>
          </select>
        </div>
        <div class="col-md-3">
          <label for="courseFilter">Curso</label>
          <select id="courseFilter" class="form-select">
            <option>Todos</option>
            <option>Engenharia</option>
            <option>Medicina</option>
            <option>Direito</option>
            <option>Ciência da Computação</option>
            <option>Psicologia</option>
          </select>
        </div>
        <div class="col-md-3">
          <label for="regionFilter">Região</label>
          <select id="regionFilter" class="form-select">
            <option>Todos</option>
            <option>Brasil</option>
            <option>EUA</option>
            <option>Europa</option>
            <option>Ásia</option>
          </select>
        </div>
        <div class="col-md-3">
          <label for="quotaFilter">Cotistas</label>
          <select id="quotaFilter" class="form-select">
            <option>Todos</option>
            <option>PCD</option>
            <option>Hipossuficientes</option>
            <option>Preto/Pardo</option>
            <option>Mescla</option>
            <option>Não Cotistas</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Gráficos -->
    <div class="chart-grid">
      <div class="card">
        <h5>Empregados x Desempregados</h5>
        <canvas id="totalChart"></canvas>
      </div>
      <div class="card">
        <h5>Egressos por Região</h5>
        <canvas id="byRegionChart"></canvas>
      </div>
      <div class="card">
        <h5>Formados por Ano</h5>
        <canvas id="byYearChart"></canvas>
      </div>
      <div class="card">
        <h5>Empregabilidade por Curso</h5>
        <canvas id="byCourseChart"></canvas>
      </div>
      <div class="card">
        <h5>Cotistas</h5>
        <canvas id="byQuotaDetailedChart"></canvas>
      </div>
      <div class="card">
        <h5>Salário Médio por Curso</h5>
        <canvas id="salaryChart"></canvas>
      </div>
    </div>
  </div>
</template>
<style>
/* Estilo global para o corpo */
body {
  background: url("/egressufundo.png") no-repeat center center fixed;
  background-size: 100%;
  margin: 0;
  padding: 0;
  font-family: "Roboto", Arial, sans-serif;
  color: #343a40;
}

/* Configuração da caixa principal */
.container {
  max-width: 1200px;
  margin-top: 100px;
  background: rgba(255, 255, 255, 0.95); /* Transparência sobre a imagem */
  padding: 25px;
  border-radius: 20px;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
}

/* Layout flexível e organização */
.chart-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.card {
  background: #ffffff;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.15);
}

.card h5 {
  font-size: 1.5rem;
  color: #495057;
  margin-bottom: 20px;
}

canvas {
  max-height: 300px;
  max-width: 100%;
  transition: transform 0.3s ease;
}

canvas:hover {
  transform: scale(1.05);
}

/* Filtros */
.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  background: linear-gradient(135deg, #ffffff, #f8f9fa);
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.15);
  margin-bottom: 30px;
  margin-top: 100px;
  border: 1px solid #dcdfe3;
}
.filters:hover {
  transform: translateY(-3px);
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
}

.filter-item {
  flex: 1;
  min-width: 220px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.filter-item label {
  font-weight: 600;
  font-size: 1rem;
  color: #495057;
}

.filter-item select {
  border: 1px solid #ced4da;
  border-radius: 8px;
  padding: 10px;
  font-size: 1rem;
  color: #495057;
  box-shadow: inset 0px 2px 6px rgba(0, 0, 0, 0.05);
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.filter-item select:hover,
.filter-item select:focus {
  border-color: #007bff;
  box-shadow: 0px 0px 8px rgba(0, 123, 255, 0.5);
  outline: none;
}

/* Botões */
.btn-filter {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 10px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn-filter:hover {
  background-color: #0056b3;
  transform: translateY(-3px);
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
}

/* Ajustes para dispositivos menores */
@media (max-width: 768px) {
  .filters {
    flex-direction: column;
    gap: 15px;
    padding: 20px;
  }

  .filter-item {
    width: 100%;
  }

  .chart-grid {
    grid-template-columns: 1fr; /* Um gráfico por linha em telas pequenas */
  }
}

.navbar {
  background-color: #ffffff;
  padding: 0.5rem 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Estilo da logo */
.logo {
  max-height: 150px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

/* Estilo dos links */
.nav-link {
  color: #007bff;
  font-weight: 500;
  font-size: 1.3rem !important;
  padding: 1rem 1.8rem !important;
  text-transform: uppercase;
  transition: color 0.1s ease, transform 0.1s ease;
  text-decoration: none;
}

.nav-link:hover {
  color: #0056b3;
  transform: translateY(-3px);
}

.active {
  color: #0056b3 !important;
  font-weight: bold;
}

/* Alinhamento e espaçamento */
.navbar-nav {
  margin-right: 0;
  margin-left: auto;
}

.nav-item {
  margin-left: -1.5rem;
}
</style>
