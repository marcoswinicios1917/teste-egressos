<template>
  <div class="main-container">
    <!-- Cabeçalho com Navegação -->
    <div class="nav-header">
      <h5 class="page-title"></h5>
      <div class="nav-tabs">
        <a
          class="nav-tab"
          :class="{ active: activeTab === 'pesquisar' }"
          @click="activeTab = 'pesquisar'"
        >
          Pesquisar
        </a>
        <a
          class="nav-tab"
          :class="{ active: activeTab === 'cadastrar' }"
          @click="activeTab = 'cadastrar'"
        >
          Cadastrar
        </a>
      </div>
    </div>

    <!-- Aba de Pesquisar -->
    <div v-if="activeTab === 'pesquisar'" class="tab-content">
      <h6 class="tab-title">Buscar Egressos</h6>
      <form class="form-container">
        <div class="form-grid">
          <div>
            <label for="name" class="form-label">Nome do Egresso</label>
            <input
              id="name"
              type="text"
              v-model="searchQuery.name"
              placeholder="Digite o nome"
              class="form-control"
              @input="filterResults"
            />
          </div>
          <div>
            <label for="enrollment" class="form-label">Matrícula</label>
            <input
              id="enrollment"
              type="text"
              v-model="searchQuery.enrollment"
              placeholder="Digite a matrícula"
              class="form-control"
              @input="filterResults"
            />
          </div>
          <div>
            <label for="course" class="form-label">Curso</label>
            <select
              id="course"
              v-model="searchQuery.course"
              class="form-control"
              @change="filterResults"
            >
              <option value="">Selecione um curso</option>
              <option v-for="course in courses" :key="course" :value="course">
                {{ course }}
              </option>
            </select>
          </div>
          <div>
            <label for="year" class="form-label">Ano de Conclusão</label>
            <select
              id="year"
              v-model="searchQuery.year"
              class="form-control"
              @change="filterResults"
            >
              <option value="">Selecione um ano</option>
              <option v-for="year in years" :key="year" :value="year">
                {{ year }}
              </option>
            </select>
          </div>
          <div>
            <label for="status" class="form-label">Status no Mercado</label>
            <select
              id="status"
              v-model="searchQuery.status"
              class="form-control"
              @change="filterResults"
            >
              <option value="">Selecione o status</option>
              <option v-for="status in statuses" :key="status" :value="status">
                {{ status }}
              </option>
            </select>
          </div>
        </div>
      </form>

      <!-- Resultados da Pesquisa -->
      <div v-if="filteredResults.length" class="results-container">
        <h6 class="tab-title mt-4">Resultados da Pesquisa</h6>
        <ul class="egressos-list">
          <li
            v-for="(egresso, index) in filteredResults"
            :key="index"
            class="egresso-item"
          >
            <h6 class="egresso-name">{{ egresso.name }}</h6>
            <p><strong>Matrícula:</strong> {{ egresso.enrollment }}</p>
            <p><strong>Curso:</strong> {{ egresso.course }}</p>
            <p><strong>Ano de Conclusão:</strong> {{ egresso.year }}</p>
            <p><strong>Status:</strong> {{ egresso.status }}</p>
            <p>
              <strong>Ocupação Atual:</strong> {{ egresso.currentActivity }}
            </p>
          </li>
        </ul>
      </div>

      <div v-else-if="searchPerformed" class="no-results">
        <p>Nenhum egresso encontrado para os critérios informados.</p>
      </div>
    </div>

    <!-- Aba de Cadastrar -->
    <div v-else class="tab-content">
      <h6 class="tab-title">Formulário de Cadastro</h6>
      <form class="form-container" @submit.prevent="submitForm">
        <!-- Caracterização do Egresso -->

        <fieldset>
          <legend>1. Caracterização do Egresso</legend>
          <div class="form-grid">
            <div>
              <label for="nome" class="form-label">Nome completo *</label>
              <input
                id="nome"
                type="text"
                v-model="formData.nome"
                class="form-control"
                required
              />
            </div>
            <div>
              <label for="genero" class="form-label">Gênero *</label>
              <select
                id="genero"
                v-model="formData.genero"
                class="form-control"
                required
              >
                <option value="" disabled>Selecione</option>
                <option>Mulher Cisgênero</option>
                <option>Mulher Transexual</option>
                <option>Homem Cisgênero</option>
                <option>Homem Transexual</option>
                <option>Não Binário</option>
                <option>Prefiro não responder</option>
                <option>Outro</option>
              </select>
            </div>
            <div>
              <label for="dataNascimento" class="form-label"
                >Data de nascimento *</label
              >
              <input
                id="dataNascimento"
                type="date"
                v-model="formData.dataNascimento"
                class="form-control"
                required
              />
            </div>
            <div>
              <label for="nacionalidade" class="form-label"
                >Nacionalidade</label
              >
              <select
                id="nacionalidade"
                v-model="formData.nacionalidade"
                class="form-control"
              >
                <option value="" disabled>Selecione</option>
                <option>Brasileiro(a)</option>
                <option>Estrangeiro</option>
              </select>
            </div>
            <div v-if="formData.nacionalidade === 'Estrangeiro'">
              <label for="pais" class="form-label">Qual País?</label>
              <input
                id="pais"
                type="text"
                v-model="formData.pais"
                class="form-control"
              />
            </div>
            <div>
              <label for="estadoCivil" class="form-label">Estado Civil *</label>
              <select
                id="estadoCivil"
                v-model="formData.estadoCivil"
                class="form-control"
                required
              >
                <option value="" disabled>Selecione</option>
                <option>Solteiro(a)</option>
                <option>Casado(a)</option>
                <option>Divorciado(a)</option>
                <option>União Estável</option>
              </select>
            </div>
            <div>
              <label for="estadoResidencia" class="form-label"
                >Estado atual de residência *</label
              >
              <select
                id="estadoResidencia"
                v-model="formData.estadoResidencia"
                class="form-control"
                required
              >
                <option value="" disabled>Selecione</option>
                <option v-for="estado in estados" :key="estado" :value="estado">
                  {{ estado }}
                </option>
              </select>
            </div>

            <div>
              <label for="municipioResidencia" class="form-label"
                >Município de residência *</label
              >
              <input
                id="municipioResidencia"
                type="text"
                v-model="formData.municipioResidencia"
                class="form-control"
                required
              />
            </div>
          </div>
        </fieldset>

        <!-- Formação Profissional -->
        <fieldset>
          <legend>2. Formação Profissional dos Egressos</legend>
          <div class="form-grid">
            <div>
              <label for="instituicaoGraduacao" class="form-label">
                Instituição da Graduação *
              </label>
              <select
                id="instituicaoGraduacao"
                v-model="formData.instituicaoGraduacao"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>UFDPar</option>
                <option>Outra Instituição</option>
              </select>
            </div>
            <div v-if="formData.instituicaoGraduacao === 'Outra Instituição'">
              <label for="outraInstituicao" class="form-label">
                Especificar Instituição
              </label>
              <input
                id="outraInstituicao"
                type="text"
                v-model="formData.outraInstituicao"
                class="form-control"
              />
            </div>
            <div>
              <label for="cursoGraduacao" class="form-label">
                Qual sua Graduação? *
              </label>
              <select
                id="cursoGraduacao"
                v-model="formData.cursoGraduacao"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
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
            <div v-if="formData.cursoGraduacao === 'Outro'">
              <label for="especificarCurso" class="form-label">
                Especificar Curso
              </label>
              <input
                id="especificarCurso"
                type="text"
                v-model="formData.especificarCurso"
                class="form-control"
              />
            </div>
            <div>
              <label for="anoConclusao" class="form-label">
                Em que ano você concluiu sua graduação? *
              </label>
              <input
                id="dataNascimento"
                type="date"
                v-model="formData.dataNascimento"
                class="form-control"
                required
              />
            </div>
            <div>
              <label for="temPosGraduacao" class="form-label">
                Tem pós-graduação? *
              </label>
              <select
                id="temPosGraduacao"
                v-model="formData.temPosGraduacao"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>Sim</option>
                <option>Não</option>
              </select>
            </div>
            <div v-if="formData.temPosGraduacao === 'Sim'">
              <label for="tipoPosGraduacao" class="form-label">
                Que cursos de pós-graduação já concluiu na UFDPar? *
              </label>
              <div>
                <label>
                  <input
                    type="checkbox"
                    value="Especialização"
                    v-model="formData.tipoPosGraduacao"
                  />
                  Especialização
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Residência"
                    v-model="formData.tipoPosGraduacao"
                  />
                  Residência
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Mestrado"
                    v-model="formData.tipoPosGraduacao"
                  />
                  Mestrado
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Doutorado"
                    v-model="formData.tipoPosGraduacao"
                  />
                  Doutorado
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Pós-doutorado"
                    v-model="formData.tipoPosGraduacao"
                  />
                  Pós-doutorado
                </label>
              </div>
            </div>
            <div>
              <label for="motivacoes" class="form-label">
                Qual a principal motivação que o levou a cursar pós-graduação na
                UFDPar? *
              </label>
              <div>
                <label>
                  <input
                    type="checkbox"
                    value="Aumento salarial através da titulação"
                    v-model="formData.motivacoes"
                  />
                  Aumento salarial através da titulação
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Possibilidade de reconhecimento e progressão profissional"
                    v-model="formData.motivacoes"
                  />
                  Possibilidade de reconhecimento e progressão profissional
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Recomendação da instituição de vínculo de trabalho"
                    v-model="formData.motivacoes"
                  />
                  Recomendação da instituição de vínculo de trabalho
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Mudança de local de trabalho e ocupação"
                    v-model="formData.motivacoes"
                  />
                  Mudança de local de trabalho e ocupação
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Interesse em uma melhor qualificação e aprimoramento profissional na área de atuação"
                    v-model="formData.motivacoes"
                  />
                  Interesse em uma melhor qualificação e aprimoramento
                  profissional na área de atuação
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Expansão das atividades profissionais para outros campos"
                    v-model="formData.motivacoes"
                  />
                  Expansão das atividades profissionais para outros campos
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Não se aplica (ensino, pesquisa e extensão)"
                    v-model="formData.motivacoes"
                  />
                  Não se aplica (ensino, pesquisa e extensão)
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Prefiro não responder"
                    v-model="formData.motivacoes"
                  />
                  Prefiro não responder
                </label>
              </div>
            </div>

            <div>
              <label for="curriculoLattes" class="form-label">
                Você atualiza seu Currículo Lattes anualmente? *
              </label>
              <select
                id="curriculoLattes"
                v-model="formData.curriculoLattes"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>Sim</option>
                <option>Não</option>
              </select>
            </div>
          </div>
        </fieldset>

        <fieldset>
          <legend>3. Sobre o Último Curso Concluído na UFDPar</legend>
          <div class="form-grid">
            <div>
              <label class="form-label">
                Participou de Programa de Iniciação Científica e/ou Tecnológica
                e Inovação oferecido pela UFDPar? *
              </label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim"
                    v-model="formData.participacaoCientifica"
                  />
                  Sim
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.participacaoCientifica"
                  />
                  Não
                </label>
              </div>
            </div>
            <div>
              <label class="form-label">
                Participou de Programa de Extensão oferecido pela UFDPar? *
              </label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim"
                    v-model="formData.participacaoExtensao"
                  />
                  Sim
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.participacaoExtensao"
                  />
                  Não
                </label>
              </div>
            </div>
            <div>
              <label class="form-label">
                Participou de Programa de Ensino oferecido pela UFDPar? *
              </label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim"
                    v-model="formData.participacaoEnsino"
                  />
                  Sim
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.participacaoEnsino"
                  />
                  Não
                </label>
              </div>
            </div>
            <div>
              <label class="form-label">
                Analise os itens abaixo em uma escala de 1 (Péssimo) a 5
                (Ótimo): *
              </label>
              <table class="evaluation-table">
                <thead>
                  <tr>
                    <th>Itens</th>
                    <th>1 (Péssimo)</th>
                    <th>2 (Ruim)</th>
                    <th>3 (Regular)</th>
                    <th>4 (Bom)</th>
                    <th>5 (Ótimo)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(item, index) in formData.avaliacaoItems"
                    :key="index"
                  >
                    <td>{{ item.label }}</td>
                    <td>
                      <input
                        type="radio"
                        :name="`avaliacao-${index}`"
                        value="1"
                        v-model="item.value"
                      />
                    </td>
                    <td>
                      <input
                        type="radio"
                        :name="`avaliacao-${index}`"
                        value="2"
                        v-model="item.value"
                      />
                    </td>
                    <td>
                      <input
                        type="radio"
                        :name="`avaliacao-${index}`"
                        value="3"
                        v-model="item.value"
                      />
                    </td>
                    <td>
                      <input
                        type="radio"
                        :name="`avaliacao-${index}`"
                        value="4"
                        v-model="item.value"
                      />
                    </td>
                    <td>
                      <input
                        type="radio"
                        :name="`avaliacao-${index}`"
                        value="5"
                        v-model="item.value"
                      />
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div>
              <label class="form-label">Você foi bolsista? *</label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim"
                    v-model="formData.foiBolsista"
                  />
                  Sim
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.foiBolsista"
                  />
                  Não
                </label>
              </div>
            </div>
            <div v-if="formData.foiBolsista === 'Sim'">
              <label class="form-label">Qual agência fomentadora? *</label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="CNPq"
                    v-model="formData.agenciaFomentadora"
                  />
                  CNPq
                </label>
                <label>
                  <input
                    type="radio"
                    value="CAPES"
                    v-model="formData.agenciaFomentadora"
                  />
                  CAPES
                </label>
                <label>
                  <input
                    type="radio"
                    value="FAPEPI"
                    v-model="formData.agenciaFomentadora"
                  />
                  FAPEPI
                </label>
                <label>
                  <input
                    type="radio"
                    value="UFDPar"
                    v-model="formData.agenciaFomentadora"
                  />
                  UFDPar
                </label>
                <label>
                  <input
                    type="radio"
                    value="Outro"
                    v-model="formData.agenciaFomentadora"
                  />
                  Outro
                </label>
              </div>
              <div v-if="formData.agenciaFomentadora === 'Outro'">
                <label class="form-label">Especificar:</label>
                <input
                  type="text"
                  v-model="formData.agenciaOutro"
                  class="form-control"
                />
              </div>
            </div>
            <div>
              <label class="form-label">
                Participou de Programa de Monitoria oferecido pela UFDPar? *
              </label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim"
                    v-model="formData.participacaoMonitoria"
                  />
                  Sim
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.participacaoMonitoria"
                  />
                  Não
                </label>
              </div>
            </div>

            <div>
              <label class="form-label">
                Apresente observações que deseja fazer em relação ao último
                curso que concluiu (opcional):
              </label>
              <textarea
                v-model="formData.observacoesUltimoCurso"
                class="form-control"
                rows="4"
                maxlength="800"
              ></textarea>
            </div>
          </div>
        </fieldset>

        <fieldset>
          <legend>4. Contribuições Científicas, Profissionais e Sociais</legend>
          <div class="form-grid">
            <div>
              <label class="form-label"
                >Após a conclusão do curso, você continuou a publicar com
                seu/sua orientador/a? *</label
              >
              <div>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.publicacoesOrientador"
                  />
                  Não
                </label>
                <label>
                  <input
                    type="radio"
                    value="Sim, de 1 a 2 publicações"
                    v-model="formData.publicacoesOrientador"
                  />
                  Sim, de 1 a 2 publicações
                </label>
                <label>
                  <input
                    type="radio"
                    value="Sim, de 3 a 5 publicações"
                    v-model="formData.publicacoesOrientador"
                  />
                  Sim, de 3 a 5 publicações
                </label>
                <label>
                  <input
                    type="radio"
                    value="Sim, mais de 5 publicações"
                    v-model="formData.publicacoesOrientador"
                  />
                  Sim, mais de 5 publicações
                </label>
              </div>
            </div>

            <div>
              <label class="form-label"
                >Após a conclusão do curso, você:*</label
              >
              <div>
                <label>
                  <input
                    type="checkbox"
                    value="Participou de eventos científicos"
                    v-model="formData.atividadesContribuicoes"
                  />
                  Participou de eventos científicos
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Publicou Livro(s) e/ou Capítulos de Livro(s)"
                    v-model="formData.atividadesContribuicoes"
                  />
                  Publicou Livro(s) e/ou Capítulos de Livro(s)
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Desenvolveu patente ou registro de software"
                    v-model="formData.atividadesContribuicoes"
                  />
                  Desenvolveu patente ou registro de software
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Recebeu Prêmio científico ou profissional"
                    v-model="formData.atividadesContribuicoes"
                  />
                  Recebeu Prêmio científico ou profissional
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Colaborou em Rede de Pesquisa"
                    v-model="formData.atividadesContribuicoes"
                  />
                  Colaborou em Rede de Pesquisa
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Contribuiu para Políticas e Práticas relevantes na área de formação"
                    v-model="formData.atividadesContribuicoes"
                  />
                  Contribuiu para Políticas e Práticas relevantes na área de
                  formação
                </label>
                <label>
                  <input
                    type="checkbox"
                    value="Não realizei nenhuma das atividades acima descritas"
                    v-model="formData.atividadesContribuicoes"
                  />
                  Não realizei nenhuma das atividades acima descritas
                </label>
              </div>
            </div>

            <div>
              <label class="form-label"
                >Como você avalia a contribuição da sua pesquisa desenvolvida
                durante o curso no avanço do conhecimento em sua área? *</label
              >
              <div>
                <label>
                  <input
                    type="radio"
                    value="Contribuiu substancialmente"
                    v-model="formData.impactoPesquisa"
                  />
                  Contribuiu substancialmente
                </label>
                <label>
                  <input
                    type="radio"
                    value="Contribuiu moderadamente"
                    v-model="formData.impactoPesquisa"
                  />
                  Contribuiu moderadamente
                </label>
                <label>
                  <input
                    type="radio"
                    value="Contribuiu pouco"
                    v-model="formData.impactoPesquisa"
                  />
                  Contribuiu pouco
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não contribuiu"
                    v-model="formData.impactoPesquisa"
                  />
                  Não contribuiu
                </label>
              </div>
            </div>

            <div>
              <label class="form-label"
                >O curso influenciou na melhoria dos processos de gestão e
                tomada de decisões em sua área? *</label
              >
              <div>
                <label>
                  <input
                    type="radio"
                    value="Concordo totalmente"
                    v-model="formData.melhoriaProcessos"
                  />
                  Concordo totalmente
                </label>
                <label>
                  <input
                    type="radio"
                    value="Concordo parcialmente"
                    v-model="formData.melhoriaProcessos"
                  />
                  Concordo parcialmente
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não concordo nem discordo"
                    v-model="formData.melhoriaProcessos"
                  />
                  Não concordo nem discordo
                </label>
                <label>
                  <input
                    type="radio"
                    value="Discordo parcialmente"
                    v-model="formData.melhoriaProcessos"
                  />
                  Discordo parcialmente
                </label>
                <label>
                  <input
                    type="radio"
                    value="Discordo totalmente"
                    v-model="formData.melhoriaProcessos"
                  />
                  Discordo totalmente
                </label>
              </div>
            </div>

            <div>
              <label class="form-label">
                Você está ou esteve envolvido na criação ou gestão de algum novo
                negócio ou startup após a conclusão do curso? *
              </label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim, relacionado à área do curso de pós-graduação"
                    v-model="formData.inovacaoEmpreendedorismo"
                  />
                  Sim, relacionado à área do curso de pós-graduação
                </label>
                <label>
                  <input
                    type="radio"
                    value="Sim, não relacionado à área do curso de pós-graduação"
                    v-model="formData.inovacaoEmpreendedorismo"
                  />
                  Sim, não relacionado à área do curso de pós-graduação
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.inovacaoEmpreendedorismo"
                  />
                  Não
                </label>
              </div>
            </div>

            <div v-if="formData.inovacaoEmpreendedorismo.includes('Sim')">
              <label class="form-label"
                >Informar novo(s) negócio(s) ou startup(s) que está ou esteve
                envolvido *</label
              >
              <textarea
                v-model="formData.startupNegocios"
                class="form-control"
                rows="3"
              ></textarea>
            </div>

            <div>
              <label class="form-label">
                Desde a conclusão do curso, você esteve envolvido em atividades
                que promovem a responsabilidade social corporativa e
                sustentabilidade? *
              </label>
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim, em várias atividades"
                    v-model="formData.responsabilidadeSocial"
                  />
                  Sim, em várias atividades
                </label>
                <label>
                  <input
                    type="radio"
                    value="Sim, em algumas atividades"
                    v-model="formData.responsabilidadeSocial"
                  />
                  Sim, em algumas atividades
                </label>
                <label>
                  <input
                    type="radio"
                    value="Nenhuma atividade"
                    v-model="formData.responsabilidadeSocial"
                  />
                  Nenhuma atividade
                </label>
              </div>
            </div>

            <div v-if="formData.responsabilidadeSocial.includes('Sim')">
              <label class="form-label"
                >Informar a(s) atividade(s) de responsabilidade social
                corporativa e sustentabilidade na qual esteve envolvido *</label
              >
              <textarea
                v-model="formData.atividadesResponsabilidade"
                class="form-control"
                rows="3"
              ></textarea>
            </div>
          </div>
        </fieldset>

        <fieldset>
          <legend>5. Informações de Vínculo Empregatício</legend>
          <div class="form-grid">
            <div>
              <label for="mercadoTrabalho12Meses" class="form-label">
                Você entrou no mercado de trabalho em até 12 meses após a
                conclusão do curso? *
              </label>
              <select
                id="mercadoTrabalho12Meses"
                v-model="formData.vinculoEmpregaticio.mercadoTrabalho12Meses"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>Sim</option>
                <option>Não</option>
              </select>
            </div>
            <div>
              <label for="situacaoAtual" class="form-label">
                Situação atual *
              </label>
              <select
                id="situacaoAtual"
                v-model="formData.vinculoEmpregaticio.situacaoAtual"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>
                  Estou empregado na área de formação do curso concluído na
                  UFDPar
                </option>
                <option>
                  Estou empregado em área distinta à área de formação do curso
                  concluído na UFDPar
                </option>
                <option>Não estou empregado</option>
              </select>
            </div>
            <div>
              <label for="setorAtuacao" class="form-label">
                Setor de atuação *
              </label>
              <select
                id="setorAtuacao"
                v-model="formData.vinculoEmpregaticio.setorAtuacao"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>Empresário/autônomo/profissional liberal</option>
                <option>
                  Docente e/ou pesquisador de Instituição pública (Ensino apenas
                  em graduação)
                </option>
                <option>
                  Docente e/ou pesquisador de Instituição pública (Ensino em
                  graduação e pós-graduação)
                </option>
                <option>
                  Docente e/ou pesquisador de Instituição privada (Ensino apenas
                  em graduação)
                </option>
                <option>
                  Docente e/ou pesquisador de Instituição privada (Ensino em
                  graduação e pós-graduação)
                </option>
                <option>
                  Profissional de Instituição pública (exceto docência/pesquisa)
                </option>
                <option>
                  Profissional de Instituição privada (exceto docência/pesquisa)
                </option>
                <option>
                  Terceiro Setor (ONGs, organizações sem fins lucrativos)
                </option>
                <option>Estagiário</option>
              </select>
            </div>
            <div>
              <label for="jornadaTrabalho" class="form-label">
                Jornada de Trabalho (horas semanais) *
              </label>
              <select
                id="jornadaTrabalho"
                v-model="formData.vinculoEmpregaticio.jornadaTrabalho"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>20h</option>
                <option>20 - 30h</option>
                <option>30 - 40h</option>
                <option>Mais que 40h</option>
              </select>
            </div>
            <div>
              <label for="instituicaoAtual" class="form-label">
                Instituição que trabalha atualmente? *
              </label>
              <input
                id="instituicaoAtual"
                type="text"
                v-model="formData.vinculoEmpregaticio.instituicaoAtual"
                class="form-control"
                required
              />
            </div>
            <div>
              <label for="salarioMedio" class="form-label">
                Qual a sua média mensal de rendimentos brutos? *
              </label>
              <select
                id="salarioMedio"
                v-model="formData.vinculoEmpregaticio.salarioMedio"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>até 1 salário mínimo</option>
                <option>entre 1 e 3 salários mínimos</option>
                <option>entre 4 e 7 salários mínimos</option>
                <option>mais que 7 salários mínimos</option>
              </select>
            </div>
            <div>
              <label for="impactoRenda" class="form-label">
                Qual o impacto do curso, concluído na UFDPar, na sua renda? *
              </label>
              <select
                id="impactoRenda"
                v-model="formData.vinculoEmpregaticio.impactoRenda"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>Aumentou consideravelmente</option>
                <option>Aumentou um pouco</option>
                <option>Não houve mudança</option>
              </select>
            </div>
            <div>
              <label for="qualificacaoMercado" class="form-label">
                Você concorda que o curso lhe qualificou para o mercado de
                trabalho? *
              </label>
              <select
                id="qualificacaoMercado"
                v-model="formData.vinculoEmpregaticio.qualificacaoMercado"
                class="form-control"
                required
              >
                <option value="" disabled selected>Selecione</option>
                <option>Concordo totalmente</option>
                <option>Concordo parcialmente</option>
                <option>Não concordo nem discordo</option>
                <option>Discordo parcialmente</option>
                <option>Discordo totalmente</option>
              </select>
            </div>
          </div>
        </fieldset>

        <fieldset>
          <legend>6. Gestão ou Liderança</legend>
          <div class="form-grid">
            <div>
              <label class="form-label"
                >Você ocupa uma posição de gestão ou liderança em sua área de
                atuação? *</label
              >
              <div>
                <label>
                  <input
                    type="radio"
                    value="Sim, em instituição pública"
                    v-model="formData.posicaoGestao.ocupaPosicao"
                  />
                  Sim, em instituição pública
                </label>
                <label>
                  <input
                    type="radio"
                    value="Sim, em instituição privada"
                    v-model="formData.posicaoGestao.ocupaPosicao"
                  />
                  Sim, em instituição privada
                </label>
                <label>
                  <input
                    type="radio"
                    value="Não"
                    v-model="formData.posicaoGestao.ocupaPosicao"
                  />
                  Não
                </label>
              </div>
            </div>

            <div v-if="formData.posicaoGestao.ocupaPosicao.startsWith('Sim')">
              <label for="detalhesPosicao" class="form-label"
                >Por favor, detalhe qual a função e Instituição:</label
              >
              <textarea
                id="detalhesPosicao"
                v-model="formData.posicaoGestao.detalhesPosicao"
                class="form-control"
                rows="3"
              ></textarea>
            </div>
          </div>
        </fieldset>

        <!-- Botão de Envio -->
        <div class="button-container">
          <button type="submit" class="btn btn-primary">Enviar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: "pesquisar",
      searchQuery: {
        name: "",
        enrollment: "",
        course: "",
        year: "",
        status: "",
      },
      formData: {
        nome: "",
        genero: "",
        dataNascimento: "",
        nacionalidade: "",
        pais: "",
        corRaca: "",
        deficiencia: "",
        tipoDeficiencia: "",
        estadoCivil: "",
        estadoResidencia: "", // Estado selecionado será armazenado aqui
        municipioResidencia: "",
        instituicaoGraduacao: "",
        outraInstituicao: "",
        cursoGraduacao: "",
        anoConclusao: "",
        temPosGraduacao: "",
        tipoPosGraduacao: [],
        ultimoCursoConcluido: "",
        motivacoes: [],
        curriculoLattes: "",
        publicacoesOrientador: "",
        atividadesContribuicoes: [],
        impactoPesquisa: "",
        melhoriaProcessos: "",
        inovacaoEmpreendedorismo: "",
        startupNegocios: "",
        responsabilidadeSocial: "",
        atividadesResponsabilidade: "",
        avaliacaoItems: [
          { label: "Avaliação geral com o curso", value: "" },
          { label: "Salas de aula", value: "" },
          { label: "Bibliotecas", value: "" },
          { label: "Laboratórios de ensino", value: "" },
          { label: "Laboratórios de pesquisa", value: "" },
          { label: "Currículo do curso", value: "" },
          { label: "Professores do curso", value: "" },
          { label: "Materiais e métodos de ensino", value: "" },
          { label: "Coordenação do curso", value: "" },
          { label: "Secretaria do curso", value: "" },
          { label: "Flexibilidade de horários", value: "" },
          { label: "Espaços de convivência", value: "" },
        ],
        programasParticipados: {
          cientifico: "",
          extensao: "",
          ensino: "",
          monitoria: "",
          foiBolsista: "",
          agenciaFomentadora: "",
        },
        observacoesUltimoCurso: "",

        motivacoesOptions: [
          "Aumento salarial através da titulação",
          "Possibilidade de reconhecimento e progressão profissional",
          "Recomendação da instituição de vínculo de trabalho",
          "Mudança de local de trabalho e ocupação",
          "Interesse em uma melhor qualificação e aprimoramento profissional na área de atuação",
          "Expansão das atividades profissionais para outros campos",
          "Não se aplica (ensino, pesquisa e extensão)",
          "Prefiro não responder",
        ],
        vinculoEmpregaticio: {
          mercadoTrabalho12Meses: "",
          situacaoAtual: "",
          setorAtuacao: "",
          jornadaTrabalho: "",
          instituicaoAtual: "",
          salarioMedio: "",
          impactoRenda: "",
          qualificacaoMercado: "",
        },
        posicaoGestao: {
          ocupaPosicao: "",
          detalhesPosicao: "",
        },
        contribuicoes: {
          publicacoesOrientador: "",
          atividadesContribuicoes: [],
          impactoPesquisa: "",
          melhoriaProcessos: "",
          inovacaoEmpreendedorismo: "",
          responsabilidadeSocial: "",
        },
      },
      estados: [
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
      ], // Lista de estados aqui
      courses: [
        "Ciência da Computação",
        "Engenharia Civil",
        "Administração",
        "Medicina",
        "Direito",
      ],
      statuses: [
        "Empregado",
        "Empreendendo",
        "Estudando",
        "Disponível para Contratação",
      ],
      years: Array.from({ length: 30 }, (_, i) => new Date().getFullYear() - i),
      egressos: [
        {
          name: "João Silva",
          enrollment: "2020001",
          course: "Ciência da Computação",
          year: 2020,
          status: "Empregado",
          currentActivity: "Desenvolvedor Full Stack na Empresa X",
        },
        {
          name: "Ana Oliveira",
          enrollment: "2018012",
          course: "Administração",
          year: 2018,
          status: "Empreendendo",
          currentActivity: "Dona de uma startup de tecnologia",
        },
        {
          name: "Carlos Pereira",
          enrollment: "2015015",
          course: "Engenharia Civil",
          year: 2015,
          status: "Disponível para Contratação",
          currentActivity: "Buscando oportunidades em grandes obras",
        },
        {
          name: "Maria Santos",
          enrollment: "2019007",
          course: "Medicina",
          year: 2019,
          status: "Estudando",
          currentActivity: "Residência Médica em Pediatria",
        },
        {
          name: "Rafael Souza",
          enrollment: "2021023",
          course: "Direito",
          year: 2021,
          status: "Empregado",
          currentActivity: "Advogado Júnior em um escritório de renome",
        },
        {
          name: "Isabela Lima",
          enrollment: "2022005",
          course: "Engenharia Civil",
          year: 2022,
          status: "Empreendendo",
          currentActivity: "Proprietária de uma consultoria de obras",
        },
        {
          name: "Pedro Mendes",
          enrollment: "2021003",
          course: "Administração",
          year: 2021,
          status: "Estudando",
          currentActivity: "MBA em Gestão Empresarial",
        },
        {
          name: "Larissa Alves",
          enrollment: "2016011",
          course: "Medicina",
          year: 2016,
          status: "Empregado",
          currentActivity: "Médica especialista em Clínica Geral",
        },
        {
          name: "Felipe Costa",
          enrollment: "2014014",
          course: "Ciência da Computação",
          year: 2014,
          status: "Disponível para Contratação",
          currentActivity:
            "Buscando oportunidades em desenvolvimento de software",
        },
        {
          name: "Julia Fernandes",
          enrollment: "2023002",
          course: "Direito",
          year: 2023,
          status: "Estudando",
          currentActivity: "Preparação para a OAB",
        },
      ],
      filteredResults: [],
      searchPerformed: false,
    };
  },
  methods: {
    filterResults() {
      const query = this.searchQuery;
      this.filteredResults = this.egressos.filter(
        (egresso) =>
          (!query.name ||
            egresso.name.toLowerCase().includes(query.name.toLowerCase())) &&
          (!query.enrollment ||
            egresso.enrollment.includes(query.enrollment)) &&
          (!query.course || egresso.course === query.course) &&
          (!query.year || egresso.year.toString() === query.year) &&
          (!query.status || egresso.status === query.status)
      );
      this.searchPerformed = true;
    },
    submitForm() {
      console.log("Dados enviados:", this.formData);
      alert("Cadastro enviado com sucesso!");
    },
  },
  mounted() {
    this.filteredResults = this.egressos;
  },
};
</script>

<style scoped>
/* Layout Principal */
/* Layout Principal */
.main-container {
  margin: 60px;
  padding: 0px;
  background: #ffffff;
  border-radius: 15px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
  font-family: "Roboto", sans-serif;
  color: #333;
}

/* Cabeçalho e Navegação */
.nav-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.page-title {
  font-size: 2rem;
  font-weight: bold;
  color: #4a4a4a;
}

.nav-tabs {
  display: flex;
  gap: 15px;
}

.nav-tab {
  padding: 12px 25px;
  margin-top: 20px;
  font-size: 1rem;
  font-weight: 500;
  color: #0078d7;
  background-color: #f9f9f9;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  transition: background-color 0.3s, transform 0.2s, color 0.3s;
  cursor: pointer;
  text-align: center;
  text-transform: uppercase;
}

.nav-tab.active {
  background-color: #0078d7;
  color: white;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.nav-tab:hover {
  background-color: #005bb5;
  color: #ffffff;
  transform: scale(1.02);
}

/* Conteúdo das Abas */
.tab-content {
  background: white;
  padding: 50px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.tab-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: #4a4a4a;
  text-align: center;
}

/* Formulário */
.form-container {
  width: 100%;
  margin: 0 auto;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.form-label {
  font-weight: 600;
  margin-bottom: 8px;
  color: #495057;
  font-size: 1rem;
  display: block;
}

.form-control {
  border: 1px solid #ced4da;
  border-radius: 8px;
  padding: 10px 15px;
  font-size: 1rem;
  color: #495057;
  transition: border-color 0.3s, box-shadow 0.3s;
  outline: none;
  width: 100%;
  box-sizing: border-box;
}

.form-control:focus {
  border-color: #0078d7;
  box-shadow: 0px 0px 5px rgba(0, 120, 215, 0.5);
}

textarea.form-control {
  resize: vertical;
  min-height: 100px;
}

/* Botões */
.btn {
  display: inline-block;
  padding: 12px 20px;
  font-size: 1rem;
  font-weight: 600;
  text-align: center;
  color: #ffffff;
  background-color: #0078d7;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s, box-shadow 0.3s;
}

.btn-primary:hover {
  background-color: #005bb5;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
  transform: scale(1.02);
}

.btn-primary:active {
  background-color: #004494;
}

/* Resultados */
.results-container {
  margin-top: 20px;
}

.egressos-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.egresso-item {
  background: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s, box-shadow 0.3s;
}

.egresso-item:hover {
  transform: translateY(-2px);
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
}

.egresso-name {
  font-size: 1.2rem;
  font-weight: bold;
  color: #333333;
}

.egresso-item p {
  margin: 5px 0;
  color: #666666;
  font-size: 0.95rem;
}

/* Tabela de Avaliação */
.evaluation-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  text-align: center;
  font-size: 0.9rem;
}

.evaluation-table th,
.evaluation-table td {
  border: 1px solid #e0e0e0;
  padding: 10px;
}

.evaluation-table th {
  background: #f4f4f4;
  font-weight: 600;
  text-transform: uppercase;
  color: #333333;
}

.evaluation-table td input[type="radio"] {
  transform: scale(1.2);
  cursor: pointer;
}

/* Responsividade */
@media (max-width: 768px) {
  .form-grid {
    grid-template-columns: 1fr;
  }

  .nav-tab {
    font-size: 0.9rem;
    padding: 8px 15px;
  }

  .page-title {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .main-container {
    padding: 15px;
  }

  .form-control {
    padding: 8px;
  }

  .btn {
    padding: 10px 15px;
    font-size: 0.9rem;
  }
}
</style>
