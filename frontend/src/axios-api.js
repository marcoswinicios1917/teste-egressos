// src/axios-api.js

import axios from "axios";

const getAPI = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", // URL base para a API do Django
  timeout: 5000, // Timeout aumentado para 5 segundos
  headers: {
    "Content-Type": "application/json", // Cabeçalho para JSON
  },
});

export default getAPI;
