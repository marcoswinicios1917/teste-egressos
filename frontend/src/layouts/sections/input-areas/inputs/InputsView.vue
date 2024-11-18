<script setup>
import { onMounted, ref } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet.markercluster";
import "leaflet.markercluster/dist/MarkerCluster.Default.css";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

const isActive = (targetRoute) => route.path === targetRoute;

const generateEgressosData = () => {
  // Generate sample data for the map markers
  const cursos = [
    "Engenharia",
    "Medicina",
    "Direito",
    "Ciência da Computação",
    "Psicologia",
    "Administração",
    "Arquitetura",
    "Pedagogia",
    "Biomedicina",
    "Química",
    "Física",
    "Matemática",
    "Letras",
    "História",
  ];
  const statusList = [
    "Trabalhando em empresa",
    "Pesquisador(a)",
    "Empreendedor(a)",
    "Consultor(a)",
    "Professor(a)",
    "Desenvolvedor(a)",
    "Freelancer",
    "Gestor(a)",
  ];
  const nomesFicticios = [
    "Ana",
    "Carlos",
    "Fernanda",
    "Gabriel",
    "Juliana",
    "Lucas",
    "Mariana",
    "Pedro",
    "Rafael",
    "Sofia",
    "Thiago",
    "Vitoria",
    "Bruno",
    "Camila",
    "Ricardo",
    "Larissa",
    "Mateus",
    "Bianca",
    "Felipe",
    "Renata",
  ];
  const locaisBrasil = [
    [-23.5505, -46.6333],
    [-22.9068, -43.1729],
    [-15.7942, -47.8822],
    [-19.9167, -43.9345],
    [-12.9714, -38.5014],
    [-8.0476, -34.877],
    [-25.4296, -49.2713],
    [-3.119, -60.0217],
    [-16.6869, -49.2648],
    [-2.5297, -44.3028],
  ];
  const locaisMundo = [
    [40.7128, -74.006],
    [51.5074, -0.1278],
    [48.8566, 2.3522],
    [35.6895, 139.6917],
    [55.7558, 37.6176],
    [-33.8688, 151.2093],
    [1.3521, 103.8198],
    [39.9042, 116.4074],
    [37.7749, -122.4194],
    [19.4326, -99.1332],
  ];

  const egressos = [];
  for (let i = 1; i <= 150; i++) {
    const randomLocation =
      i <= 120
        ? locaisBrasil[Math.floor(Math.random() * locaisBrasil.length)]
        : locaisMundo[Math.floor(Math.random() * locaisMundo.length)];
    const randomName = `${
      nomesFicticios[Math.floor(Math.random() * nomesFicticios.length)]
    } ${nomesFicticios[Math.floor(Math.random() * nomesFicticios.length)]}`;
    const randomCourse = cursos[Math.floor(Math.random() * cursos.length)];
    const randomStatus =
      statusList[Math.floor(Math.random() * statusList.length)];
    const randomYear = Math.floor(Math.random() * 15) + 2005;
    const matricula = `UF${Math.floor(1000 + Math.random() * 9000)}`;

    egressos.push({
      id: i,
      matricula,
      name: randomName,
      course: randomCourse,
      year: randomYear,
      location: randomLocation,
      status: randomStatus,
    });
  }
  return egressos;
};

const egressosData = ref(generateEgressosData());
const map = ref(null);
const markersCluster = ref(null);
const selectedEgresso = ref(null);

onMounted(() => {
  map.value = L.map("map").setView([0, 0], 2);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap contributors",
  }).addTo(map.value);

  markersCluster.value = L.markerClusterGroup();
  egressosData.value.forEach((egresso) => {
    const marker = L.marker(egresso.location);
    marker.bindPopup(
      `<strong>${egresso.name}</strong><br>Curso: ${egresso.course}<br>Ano: ${egresso.year}<br>Status: ${egresso.status}`
    );
    marker.on("click", () => {
      selectedEgresso.value = egresso;
    });
    markersCluster.value.addLayer(marker);
  });
  map.value.addLayer(markersCluster.value);
});
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">
        <img
          src="@/assets/img/egressosufdpar.png"
          alt="Logo Egressos UFDPar"
          class="logo"
        />
      </router-link>
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
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link
              to="/"
              class="nav-link"
              :class="{ active: isActive('/') }"
              >Home</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              to="/sections/page-sections/page-headers"
              class="nav-link"
              :class="{
                active: isActive('/sections/page-sections/page-headers'),
              }"
              >Pesquisa de Egressos</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              to="/sections/input-areas/inputs"
              class="nav-link"
              :class="{ active: isActive('/sections/input-areas/inputs') }"
              >Mapa de Egressos</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              to="/sections/attention-catchers/tooltips-popovers"
              class="nav-link"
              :class="{
                active: isActive(
                  '/sections/attention-catchers/tooltips-popovers'
                ),
              }"
              >Oportunidades</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              to="/sections/navigation/navbars"
              class="nav-link"
              :class="{ active: isActive('/sections/navigation/navbars') }"
              >Contatos</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              to="/pages/landing-pages/basic"
              class="nav-link"
              :class="{ active: isActive('/pages/landing-pages/basic') }"
              >Entrar</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="content-wrapper">
    <div class="sidebar">
      <h5>Filtrar Egressos</h5>
      <label>Matrícula:</label>
      <input
        type="text"
        placeholder="Digite a matrícula"
        class="form-control mb-2"
      />
      <label>Nome:</label>
      <input
        type="text"
        placeholder="Digite o nome"
        class="form-control mb-2"
      />
      <label>Curso:</label>
      <select class="form-select mb-2">
        <option>Todos</option>
        <option>Engenharia</option>
        <option>Medicina</option>
        <option>Direito</option>
        <option>Ciência da Computação</option>
        <option>Psicologia</option>
      </select>
      <label>Ano de Graduação:</label>
      <select class="form-select mb-2">
        <option>Todos</option>
        <option>2020</option>
        <option>2019</option>
        <option>2018</option>
      </select>
      <label>Status:</label>
      <select class="form-select mb-2">
        <option>Todos</option>
        <option>Trabalhando em empresa</option>
        <option>Pesquisador(a)</option>
        <option>Empreendedor(a)</option>
      </select>
      <div class="stats mt-3">
        <h6>Total de Egressos: 150</h6>
        <h6>Brasil: 120</h6>
        <h6>Internacional: 30</h6>
      </div>
      <button class="btn btn-primary mt-3 w-100">Aplicar Filtros</button>
      <button class="btn btn-secondary mt-2 w-100">Limpar Filtros</button>
    </div>

    <div id="map-container">
      <div id="map"></div>
      <div v-if="selectedEgresso" class="details-panel">
        <h5>Detalhes do Egresso</h5>
        <p><strong>Matrícula:</strong> {{ selectedEgresso.matricula }}</p>
        <p><strong>Nome:</strong> {{ selectedEgresso.name }}</p>
        <p><strong>Curso:</strong> {{ selectedEgresso.course }}</p>
        <p><strong>Ano:</strong> {{ selectedEgresso.year }}</p>
        <p><strong>Status:</strong> {{ selectedEgresso.status }}</p>
        <button class="btn btn-primary btn-sm mt-2">Ver Mais</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
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

.active {
  color: #0056b3 !important;
  font-weight: bold;
}

.content-wrapper {
  display: flex;
  margin-top: 7rem; /* Ajuste para espaço do navbar */
  padding: 2rem 3rem; /* Espaçamento mais generoso */
  gap: 2rem; /* Espaço entre o filtro e o mapa */
  height: calc(100vh - 120px); /* Ajuste de altura */
  background-color: #f4f6f8; /* Fundo sutil */
}

/* Estilo para a barra lateral (filtro de egressos) */
.sidebar {
  width: 330px;
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  gap: -2rem;
  transition: all 0.3s ease;
}

.sidebar h5 {
  font-size: 1.6rem;
  font-weight: 600;
  color: #343a40;
  text-align: center;
  margin-bottom: 1.5rem;
  letter-spacing: 0.5px;
}

.sidebar label {
  font-weight: 500;
  color: #495057;
  margin-bottom: 0.4rem;
  font-size: 0.9rem;
  letter-spacing: 0.3px;
}

.sidebar input,
.sidebar select {
  background-color: #f9fafc;
  border-radius: 8px;
  border: 1px solid #ced4da;
  padding: 0.75rem;
  font-size: 1rem;
  color: #495057;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  outline: none;
}

.sidebar input:focus,
.sidebar select:focus {
  border-color: #007bff;
  box-shadow: 0 4px 12px rgba(0, 123, 255, 0.15);
}

.sidebar input::placeholder {
  color: #adb5bd;
  font-size: 0.9rem;
}

.stats {
  background-color: #f1f3f5;
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
  font-weight: 500;
  color: #212529;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  font-size: 0.9rem;
}

.stats h6 {
  font-weight: 600;
  color: #495057;
}

.btn-primary {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 0.8rem;
  font-size: 1rem;
  font-weight: 600;
  text-align: center;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
}

.btn-primary:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

.btn-secondary {
  background-color: #6c757d;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 0.8rem;
  font-size: 1rem;
  font-weight: 600;
  text-align: center;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
}

.btn-secondary:hover {
  background-color: #5a6268;
  transform: translateY(-2px);
}

.sidebar input,
.sidebar select,
.btn-primary,
.btn-secondary {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

.stats {
  text-align: center;
  font-weight: 500;
  color: #212529;
  background-color: #f1f3f5;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

.btn-primary {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 0.75rem;
  font-size: 1rem;
  font-weight: 600;
  transition: background-color 0.3s, transform 0.3s;
  box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
}

.btn-primary:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

.btn-secondary {
  background-color: #6c757d;
  color: #ffffff;
  border: none;
  border-radius: 8px;
  padding: 0.75rem;
  font-size: 1rem;
  font-weight: 600;
  transition: background-color 0.3s, transform 0.3s;
  box-shadow: 0 4px 8px rgba(108, 117, 125, 0.2);
}

.btn-secondary:hover {
  background-color: #5a6268;
  transform: translateY(-2px);
}

#map-container {
  flex: 1;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 10px 20px;
}

#map {
  height: 80vh;
  width: 100%;
  max-width: 1200px;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Painel de detalhes do egresso */
.details-panel {
  position: relative;
  top: -15px; /* Ajustado para alinhar com o mapa */
  left: 0;
  width: 100%;
  max-width: 320px;
  background-color: #ffffff;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  margin-top: 1.5rem;
}

.details-panel h5 {
  font-size: 1.4rem;
  font-weight: 600;
  color: #343a40;
  margin-bottom: 1rem;
}

.details-panel p {
  font-size: 1rem;
  color: #495057;
  margin-bottom: 0.8rem;
}

.details-panel button {
  width: 100%;
  padding: 0.6rem;
  background-color: #007bff;
  color: #fff;
  font-size: 0.9rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  transition: background-color 0.3s;
}

.details-panel button:hover {
  background-color: #0056b3;
}
</style>
