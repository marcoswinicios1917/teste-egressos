import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";

// Certifique-se de que o arquivo "router/index.js" exista e esteja configurado corretamente.
import router from "./router/index.js";

// Ícones do Núcleo e CSS
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";

// Importando o Material Kit
import materialKit from "./material-kit";

const app = createApp(App);

// Configura o Pinia (estado global)
app.use(createPinia());

// Configura o roteador para navegação entre as páginas
app.use(router);

// Configura o Material Kit para UI/UX melhorados
app.use(materialKit);

// Monta o aplicativo na div com o id "app"
app.mount("#app");
