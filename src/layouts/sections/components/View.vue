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
                <select class="form-select" v-model="deficiencia" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Prefiro não responder</option>
                  <option>Não</option>
                  <option>Sim</option>
                </select>
              </div>
              <div class="mb-3" v-if="deficiencia === 'Sim'">
                <label for="tipoDeficiencia" class="form-label"
                  >Especificar</label
                >
                <input type="text" class="form-control" id="tipoDeficiencia" />
              </div>
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
                  <option>AP</option>
                  <option>AM</option>
                  <option>BA</option>
                  <option>CE</option>
                  <option>DF</option>
                  <option>ES</option>
                  <option>GO</option>
                  <option>MA</option>
                  <option>MT</option>
                  <option>MS</option>
                  <option>MG</option>
                  <option>PA</option>
                  <option>PB</option>
                  <option>PR</option>
                  <option>PE</option>
                  <option>PI</option>
                  <option>RJ</option>
                  <option>RN</option>
                  <option>RS</option>
                  <option>RO</option>
                  <option>RR</option>
                  <option>SC</option>
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
                  <option>Biomedicina</option>
                  <option>Ciências Contábeis</option>
                  <option>Economia</option>
                  <option>Engenharia de Pesca</option>
                  <option>Fisioterapia</option>
                  <option>Matemática</option>
                  <option>Medicina</option>
                  <option>Pedagogia</option>
                  <option>Psicologia</option>
                  <option>Turismo</option>
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
              <!-- Continuação da Pós-Graduação -->
              <div class="mb-3">
                <label class="form-label"
                  >Que cursos de pós-graduação já concluiu na UFDPar?*</label
                >
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Especialização"
                    id="especializacao"
                  />
                  <label class="form-check-label" for="especializacao"
                    >Especialização</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Residência"
                    id="residencia"
                  />
                  <label class="form-check-label" for="residencia"
                    >Residência</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Mestrado"
                    id="mestrado"
                  />
                  <label class="form-check-label" for="mestrado"
                    >Mestrado</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Doutorado"
                    id="doutorado"
                  />
                  <label class="form-check-label" for="doutorado"
                    >Doutorado</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Pós-doutorado"
                    id="posDoutorado"
                  />
                  <label class="form-check-label" for="posDoutorado"
                    >Pós-doutorado</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Não concluí pós-graduação"
                    id="naoPosGraduacao"
                  />
                  <label class="form-check-label" for="naoPosGraduacao"
                    >Não concluí pós-graduação</label
                  >
                </div>
              </div>

              <div class="mb-3">
                <label class="form-label"
                  >Qual o ÚLTIMO curso que concluiu na UFDPar?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Graduação</option>
                  <option>Especialização</option>
                  <option>Residência</option>
                  <option>Mestrado</option>
                  <option>Doutorado</option>
                  <option>Pós-doutorado</option>
                </select>
              </div>

              <div class="mb-3">
                <label class="form-label"
                  >Qual curso você concluiu na UFDPar?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Administração</option>
                  <option>Biologia</option>
                  <option>Biomedicina</option>
                  <option>Ciências Contábeis</option>
                  <option>Economia</option>
                  <option>Engenharia de Pesca</option>
                  <option>Fisioterapia</option>
                  <option>Matemática</option>
                  <option>Medicina</option>
                  <option>Pedagogia</option>
                  <option>Psicologia</option>
                  <option>Turismo</option>
                  <option>Administração Pública</option>
                  <option>Artes, Patrimônio e Museologia</option>
                  <option>Biotecnologia</option>
                  <option>Ciências Biomédicas</option>
                  <option>Saúde da Família</option>
                  <option>Outro</option>
                </select>
              </div>

              <div class="mb-3">
                <label class="form-label"
                  >Em que ano concluiu este curso?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>2021</option>
                  <option>2022</option>
                  <option>2023</option>
                  <option>2024</option>
                </select>
              </div>

              <div class="mb-3">
                <label for="orientador" class="form-label"
                  >Qual o nome do seu(a) orientador(a)/supervisor(a) durante a
                  realização do seu último curso concluído na UFDPar?*</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="orientador"
                  required
                />
              </div>

              <div class="mb-3">
                <label class="form-label"
                  >Qual a principal motivação que o levou a cursar pós-graduação
                  na UFDPar?* (Marque todas que se aplicam)</label
                >
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Aumento salarial através da titulação"
                    id="aumentoSalarial"
                  />
                  <label class="form-check-label" for="aumentoSalarial"
                    >Aumento salarial através da titulação</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Possibilidade de reconhecimento e progressão profissional"
                    id="progressaoProfissional"
                  />
                  <label class="form-check-label" for="progressaoProfissional"
                    >Possibilidade de reconhecimento e progressão
                    profissional</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Recomendação da instituição de vínculo de trabalho"
                    id="recomendacaoInstituicao"
                  />
                  <label class="form-check-label" for="recomendacaoInstituicao"
                    >Recomendação da instituição de vínculo de trabalho</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Interesse em melhor qualificação profissional"
                    id="qualificacaoProfissional"
                  />
                  <label class="form-check-label" for="qualificacaoProfissional"
                    >Interesse em melhor qualificação profissional</label
                  >
                </div>

                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Expansão das atividades para outros campos"
                    id="expansaoCampos"
                  />
                  <label class="form-check-label" for="expansaoCampos"
                    >Expansão das atividades para outros campos</label
                  >
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value="Não se aplica (ensino, pesquisa e extensão)"
                    id="naoAplicaEnsino"
                  />
                  <label class="form-check-label" for="naoAplicaEnsino"
                    >Não se aplica (ensino, pesquisa e extensão)</label
                  >
                </div>
              </div>

              <!-- Seção 3: Participação em Programas -->
              <h5>SOBRE O ÚLTIMO CURSO NO QUAL CONCLUIU NA UFDPAR</h5>
              <div class="mb-3">
                <label class="form-label"
                  >Participou de Programa de Iniciação Científica e/ou
                  Tecnológica e Inovação oferecido pela UFDPar?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim</option>
                  <option>Não</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Você foi bolsista?*</label>
                <select class="form-select" v-model="bolsista" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim</option>
                  <option>Não</option>
                </select>
              </div>
              <div v-if="bolsista === 'Sim'" class="mb-3">
                <label class="form-label">Qual agência fomentadora?</label>
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>CNPq</option>
                  <option>CAPES</option>
                  <option>FAPEPI</option>
                  <option>UFDPar</option>
                  <option>Outra</option>
                </select>
              </div>

              <!-- Additional Evaluation Fields -->
              <div class="mb-3">
                <label class="form-label"
                  >Avaliação geral com o curso (1 a 5)*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>1 (Péssimo)</option>
                  <option>2 (Ruim)</option>
                  <option>3 (Regular)</option>
                  <option>4 (Bom)</option>
                  <option>5 (Ótimo)</option>
                </select>
              </div>

              <!-- Labor Market and Employment Section -->
              <h5>INFORMAÇÕES SOBRE MERCADO DE TRABALHO</h5>
              <div class="mb-3">
                <label class="form-label"
                  >Você entrou no mercado de trabalho em até 12 meses após a
                  conclusão do curso na UFDPar?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim</option>
                  <option>Não</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label"
                  >Qual afirmativa melhor descreve sua situação atual?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Empregado na área de formação</option>
                  <option>Empregado em área distinta</option>
                  <option>Não estou empregado</option>
                </select>
              </div>

              <div class="mb-3">
                <label class="form-label"
                  >Participou de Programa de Extensão oferecido pela
                  UFDPar?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim</option>
                  <option>Não</option>
                </select>
              </div>

              <!-- Seção 4: Contribuições Científicas e Sociais -->
              <h5>CONTRIBUIÇÕES CIENTÍFICAS, PROFISSIONAIS E SOCIAIS</h5>
              <div class="mb-3">
                <label class="form-label"
                  >Após a conclusão do curso, você continuou a publicar com
                  seu(a) orientador(a)?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Não</option>
                  <option>Sim, de 1 a 2 publicações</option>
                  <option>Sim, de 3 a 5 publicações</option>
                  <option>Sim, mais de 5 publicações</option>
                </select>
              </div>

              <!-- Continuação da Seção 5: Mercado de Trabalho -->
              <h5>
                INFORMAÇÕES SOBRE MERCADO DE TRABALHO E VÍNCULO EMPREGATÍCIO
              </h5>
              <div class="mb-3">
                <label class="form-label"
                  >Você entrou no mercado de trabalho em até 12 meses após a
                  conclusão do curso na UFDPar?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim</option>
                  <option>Não</option>
                </select>
              </div>

              <div class="mb-3">
                <label class="form-label"
                  >Qual sua média mensal de rendimentos brutos?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>até 1 salário mínimo</option>
                  <option>entre 1 e 3 salários mínimos</option>
                  <option>entre 4 e 7 salários mínimos</option>
                  <option>mais que 7 salários mínimos</option>
                </select>
              </div>

              <!-- Seção 6: Gestão ou Liderança -->
              <h5>GESTÃO OU LIDERANÇA</h5>
              <div class="mb-3">
                <label class="form-label"
                  >Você ocupa uma posição de gestão ou liderança em sua área de
                  atuação?*</label
                >
                <select class="form-select" required>
                  <option selected disabled>Escolha uma opção...</option>
                  <option>Sim, em instituição pública</option>
                  <option>Sim, em instituição privada</option>
                  <option>Não</option>
                </select>
              </div>

              <div v-if="lideranca === 'Sim'" class="mb-3">
                <label for="funcaoLideranca" class="form-label"
                  >Por favor, detalhe qual a função e Instituição</label
                >
                <input type="text" class="form-control" id="funcaoLideranca" />
              </div>

              <!-- Include all additional sections as seen in the PDF -->

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
      deficiencia: null,
    };
  },
};
</script>
