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
            <!-- Formulário de Caracterização do Egresso -->
            <form class="mt-4">
              <h5>CARACTERIZAÇÃO DO EGRESSO</h5>
              <div class="mb-3">
                <label for="nome" class="form-label">Nome completo*</label>
                <input type="text" class="form-control" id="nome" required />
              </div>
              <div class="mb-3">
                <label class="form-label">Gênero*</label>
                <select class="form-select" required>
                  <option selected disabled>
                    Escolha uma das seguintes respostas...
                  </option>
                  <option>Mulher Cisgênero</option>
                  <option>Mulher Transexual</option>
                  <option>Homem Cisgênero</option>
                  <option>Homem Transexual</option>
                  <option>Não Binário</option>
                  <option>Prefiro não responder</option>
                  <option>Não sei</option>
                  <option>Outro</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="dataNascimento" class="form-label"
                  >Data de nascimento*</label
                >
                <input
                  type="date"
                  class="form-control"
                  id="dataNascimento"
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Nacionalidade</label>
                <select class="form-select" v-model="nacionalidade" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Brasileiro(a)</option>
                  <option>Estrangeiro</option>
                </select>
              </div>
              <div class="mb-3" v-if="nacionalidade === 'Estrangeiro'">
                <label for="pais" class="form-label">Qual País?</label>
                <input type="text" class="form-control" id="pais" />
              </div>
              <div class="mb-3">
                <label class="form-label"
                  >Autoidentificação em termos de cor ou raça, de acordo com o
                  IBGE.*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Preta</option>
                  <option>Parda</option>
                  <option>Amarela</option>
                  <option>Indígena</option>
                  <option>Não sei</option>
                  <option>Prefiro não responder</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Pessoa Com Deficiência?</label>
                <select class="form-select">
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Prefiro não responder</option>
                  <option>Não</option>
                  <option>Sim</option>
                </select>
              </div>
              <!-- Novo campos adicionados -->
              <div class="mb-3">
                <label class="form-label">Estado Civil*</label>
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Solteiro(a)</option>
                  <option>Casado(a)</option>
                  <option>Divorciado(a)</option>
                  <option>União Estável</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Estado Atual de Residência*</label>
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>AC</option>
                  <option>AL</option>
                  <!-- Outras opções de estado -->
                  <option>SP</option>
                  <option>SE</option>
                  <option>TO</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Município de Residência*</label>
                <input
                  type="text"
                  class="form-control"
                  id="municipio"
                  required
                />
              </div>

              <h5>FORMAÇÃO PROFISSIONAL DOS EGRESSOS</h5>
              <div class="mb-3">
                <label class="form-label"
                  >Em qual Instituição cursou sua graduação?*</label
                >
                <select class="form-select" v-model="instituicao" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>UFDPar</option>
                  <option>Outra Instituição</option>
                </select>
              </div>
              <div class="mb-3" v-if="instituicao === 'Outra Instituição'">
                <label for="outraInstituicao" class="form-label"
                  >Especificar:</label
                >
                <input type="text" class="form-control" id="outraInstituicao" />
              </div>
              <div class="mb-3">
                <label class="form-label">Qual sua graduação?*</label>
                <select class="form-select" v-model="graduacao" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Administração</option>
                  <option>Biologia</option>
                  <option>Outro</option>
                </select>
              </div>
              <div class="mb-3" v-if="graduacao === 'Outro'">
                <label for="outraGraduacao" class="form-label"
                  >Especificar:</label
                >
                <input type="text" class="form-control" id="outraGraduacao" />
              </div>
              <div class="mb-3">
                <label for="anoConclusao" class="form-label"
                  >Em que ano você concluiu sua graduação?*</label
                >
                <input
                  type="number"
                  class="form-control"
                  id="anoConclusao"
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Você possui pós-graduação?*</label>
                <select class="form-select" v-model="posGraduacao" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim</option>
                  <option>Não</option>
                </select>
              </div>
              <div class="mb-3" v-if="posGraduacao === 'Sim'">
                <label for="posGraduacao" class="form-label"
                  >Qual sua pós-graduação?</label
                >
                <input type="text" class="form-control" id="posGraduacao" />
              </div>
              <div class="mb-3">
                <label class="form-label"
                  >Você está empregado atualmente?*</label
                >
                <select class="form-select" v-model="empregado" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim</option>
                  <option>Não</option>
                </select>
              </div>
              <div class="mb-3" v-if="empregado === 'Sim'">
                <label for="empregoAtual" class="form-label"
                  >Qual seu emprego atual?</label
                >
                <input type="text" class="form-control" id="empregoAtual" />
              </div>
              <div class="mb-3">
                <label class="form-label">Qual sua área de atuação?*</label>
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Administração</option>
                  <option>Educação</option>
                  <option>Saúde</option>
                  <!-- Outras áreas -->
                </select>
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
      nacionalidade: null,
      instituicao: null,
      graduacao: null,
      posGraduacao: null,
      empregado: null,
    };
  },
};
</script>

<style scoped>
.height-400 {
  height: 400px;
}

.height-500 {
  height: 500px;
}

.height-600 {
  height: 600px;
}
</style>
