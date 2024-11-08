<template>
  <div class="container mt-5">
    <div
      class="position-relative border-radius-xl overflow-hidden shadow-lg mb-7"
    >
      <div class="container border-bottom">
        <div class="row justify-content-between py-2">
          <div class="col-lg-3 me-auto">
            <p class="lead text-dark pt-1 mb-0">{{ title }}</p>
          </div>
          <div class="col-lg-3">
            <div class="nav-wrapper position-relative end-0">
              <ul
                class="nav nav-pills nav-fill d-flex justify-content-between p-1"
                role="tablist"
              >
                <li class="nav-item">
                  <a
                    class="nav-link mb-0 px-0 py-1 active"
                    data-bs-toggle="tab"
                    :href="'#preview-' + id"
                    role="tab"
                    aria-selected="true"
                  >
                    <i class="fas fa-search text-sm me-2"></i> Pesquisar
                  </a>
                </li>
                <li class="nav-item">
                  <a
                    class="nav-link mb-0 px-0 py-1"
                    data-bs-toggle="tab"
                    :href="'#code-' + id"
                    role="tab"
                    aria-selected="false"
                  >
                    <i class="fas fa-edit text-sm me-2"></i> Cadastrar
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-content tab-space">
        <div class="tab-pane active p-2" :id="'preview-' + id">
          <div class="overflow-auto" :class="height ? 'height-' + height : ''">
            <slot />
          </div>
        </div>
        <div class="tab-pane" :id="'code-' + id">
          <div class="position-relative p-4 pb-2">
            <!-- Formulário Completo de Caracterização do Egresso -->
            <form class="mt-4" @submit.prevent="submitForm">
              <h5>CARACTERIZAÇÃO DO EGRESSO</h5>

              <div
                v-for="(field, index) in formFields"
                :key="index"
                class="mb-3"
              >
                <label :for="field.id" class="form-label"
                  >{{ field.label }}*</label
                >
                <component
                  :is="field.type === 'input' ? 'input' : 'select'"
                  :id="field.id"
                  class="form-control"
                  v-model="formData[field.model]"
                  :type="field.inputType"
                  required
                >
                  <option
                    v-if="field.type === 'select'"
                    v-for="option in field.options"
                    :key="option"
                    :value="option"
                  >
                    {{ option }}
                  </option>
                </component>
              </div>

              <button type="submit" class="btn btn-primary mt-3">Enviar</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    id: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      default: "",
    },
    height: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      formData: {
        nome_completo: "",
        genero: "",
        data_nascimento: "",
        nacionalidade: "",
        pais: "",
        cor_raca: "",
        pessoa_com_deficiencia: false,
        tipo_deficiencia: "",
        estado_civil: "",
        estado_residencia: "",
        residencia_municipal: "",
        instituicao_graduacao: "",
        curso_graduacao: "",
        ano_conclusao_graduacao: "",
        possui_pos_graduacao: false,
        pos_graduacao: "",
        curso_ufdpar: "",
        ano_conclusao_curso_ufdpar: "",
        orientador: "",
        motivacao: "",
        participacao_programa: "",
        foi_bolsista: false,
        agencia_fomentadora: "",
        avaliacao_geral: "",
        entrou_mercado_trabalho: "",
        situacao_atual: "",
        salario_medio: "",
        posicao_gestao: "",
        funcao_gestao: "",
        instituicao_gestao: "",
        publicacoes_orientador: "",
      },
      formFields: [
        {
          id: "nome",
          label: "Nome completo",
          type: "input",
          inputType: "text",
          model: "nome_completo",
        },
        {
          id: "genero",
          label: "Gênero",
          type: "select",
          model: "genero",
          options: [
            "Mulher Cisgênero",
            "Mulher Transexual",
            "Homem Cisgênero",
            "Homem Transexual",
            "Não Binário",
            "Prefiro não responder",
            "Outro",
          ],
        },
        {
          id: "dataNascimento",
          label: "Data de nascimento",
          type: "input",
          inputType: "date",
          model: "data_nascimento",
        },
        {
          id: "nacionalidade",
          label: "Nacionalidade",
          type: "select",
          model: "nacionalidade",
          options: ["Brasileiro(a)", "Estrangeiro"],
        },
        {
          id: "pais",
          label: "País",
          type: "input",
          inputType: "text",
          model: "pais",
        },
        {
          id: "corRaca",
          label: "Cor ou raça",
          type: "select",
          model: "cor_raca",
          options: [
            "Preta",
            "Parda",
            "Amarela",
            "Indígena",
            "Não sei",
            "Prefiro não responder",
          ],
        },
        {
          id: "deficiencia",
          label: "Pessoa com deficiência",
          type: "select",
          model: "pessoa_com_deficiencia",
          options: ["Sim", "Não"],
        },
        {
          id: "tipoDeficiencia",
          label: "Tipo de deficiência",
          type: "input",
          inputType: "text",
          model: "tipo_deficiencia",
        },
        {
          id: "estadoCivil",
          label: "Estado civil",
          type: "select",
          model: "estado_civil",
          options: [
            "Solteiro(a)",
            "Casado(a)",
            "Divorciado(a)",
            "União Estável",
          ],
        },
        {
          id: "estadoResidencia",
          label: "Estado de residência",
          type: "select",
          model: "estado_residencia",
          options: [
            "AC",
            "AL",
            "AP",
            "AM",
            "BA",
            "CE",
            "DF",
            "ES",
            "GO",
            "MA",
            "MT",
            "MS",
            "MG",
            "PA",
            "PB",
            "PR",
            "PE",
            "PI",
            "RJ",
            "RN",
            "RS",
            "RO",
            "RR",
            "SC",
            "SP",
            "SE",
            "TO",
          ],
        },
        {
          id: "municipio",
          label: "Município de residência",
          type: "input",
          inputType: "text",
          model: "residencia_municipal",
        },
        // Outros campos foram omitidos para brevidade
      ],
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/egressos/",
          this.formData
        );
        console.log("Formulário enviado com sucesso:", response.data);
        alert("Formulário enviado com sucesso!");
      } catch (error) {
        if (error.response) {
          console.error("Erro ao enviar o formulário:", error.response.data);
          alert(`Erro: ${JSON.stringify(error.response.data)}`);
        } else {
          console.error("Erro ao enviar o formulário:", error.message);
          alert("Erro de rede ou CORS. Verifique as configurações.");
        }
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 1300px;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}

h5 {
  color: #495057;
  font-weight: bold;
  margin-bottom: 1rem;
}

.form-label {
  font-weight: 500;
  color: #6c757d;
}

.form-control,
.form-select {
  border-radius: 6px;
  border: 1px solid #ced4da;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.075);
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.form-control:focus,
.form-select:focus {
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
}

button[type="submit"] {
  background-color: #007bff;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease, box-shadow 0.3s ease,
    transform 0.2s ease;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

button[type="submit"]:hover {
  background-color: #0056b3;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

button[type="submit"]:focus {
  outline: none;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
}

button[type="submit"]:active {
  transform: translateY(1px);
  background-color: #004085;
}
</style>
