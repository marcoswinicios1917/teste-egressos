<template>
  <footer class="footer-custom py-5">
    <div class="container text-center">
      <!-- Imagem da Assinatura -->
      <div class="footer-image-container mb-3">
        <img
          src="/src/assets/img/assinaturaUFDPar.png"
          alt="Assinatura UFDPar"
          class="footer-image"
        />
      </div>

      <!-- Linha dourada preenchendo toda a largura -->
      <div class="line-container">
        <hr class="elegant-line" />
      </div>

      <!-- Copyright -->
      <div class="footer-text-container mt-4">
        <p class="mb-0 text-secondary footer-text">
          Copyright © {{ new Date().getFullYear() }} Portal do Egresso da
          Universidade Federal do Delta do Parnaíba.
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
// Nenhuma lógica JavaScript necessária.
</script>

<style scoped>
.footer-custom {
  background-color: #003366; /* Azul forte */
  padding: 2rem 0;
  color: white;
  position: relative; /* Para permitir o posicionamento absoluto dos ornamentos */
}

/* Estilo para a imagem de assinatura */
.footer-image-container {
  max-width: 250px; /* Tamanho máximo da imagem ajustado */
  margin: 0 auto; /* Centraliza a imagem */
}

.footer-image {
  max-width: 100%; /* Garante que a imagem não ultrapasse o container */
  border: none; /* Removendo a borda */
  border-radius: 0; /* Sem bordas arredondadas */
  box-shadow: none; /* Removendo a sombra */
  transition: transform 0.3s ease; /* Transição suave para efeito de hover */
}

/* Efeito de hover na imagem */
.footer-image:hover {
  transform: scale(1.05); /* Aumenta levemente a imagem ao passar o mouse */
}

/* Estilo do container da linha */
.line-container {
  margin: 2rem 0; /* Remover margem lateral */
  width: 100%; /* Faz a linha ocupar toda a largura da tela */
}

/* Linha dourada com design aprimorado */
.elegant-line {
  border: none;
  height: 6px; /* Aumenta a altura da linha para mais presença */
  background-image: linear-gradient(
    to right,
    #ffd700,
    /* Dourado vibrante */ #ffcc00,
    /* Dourado mais claro */ #ffd700 /* Dourado vibrante novamente */
  ); /* Gradiente dourado */
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.8); /* Sombra suave para efeito 3D */
  border-radius: 5px; /* Bordas arredondadas */
  width: 100%; /* Largura da linha ajustada para 100% */
}

/* Pequeno ornamento decorativo nas pontas da linha */
.elegant-line::before,
.elegant-line::after {
  content: "";
  width: 14px; /* Aumenta o tamanho dos ornamentos */
  height: 14px;
  background-color: #ffd700; /* Dourado sólido */
  border-radius: 50%; /* Ornamento circular nas extremidades */
  position: absolute;
  top: -7px; /* Ajusta a posição do ornamento */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Sombra para profundidade */
}

.elegant-line::before {
  left: -10px; /* Alinhamento do ornamento esquerdo */
}

.elegant-line::after {
  right: -10px; /* Alinhamento do ornamento direito */
}

/* Estilo do texto copyright */
.footer-text {
  font-size: 1rem; /* Aumenta o tamanho da fonte para maior legibilidade */
  line-height: 1.5; /* Aumenta o espaço entre linhas */
}

/* Ajustes para a cor do texto */
.text-secondary {
  color: #e0e0e0; /* Tom de cinza suave */
}

/* Responsividade */
@media (max-width: 768px) {
  .footer-text {
    font-size: 0.9rem; /* Tamanho da fonte reduzido em telas menores */
  }
}
</style>
