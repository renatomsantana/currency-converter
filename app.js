const express = require('express');
const app = express();
const port = 3000;

// Middleware para lidar com requisições JSON
app.use(express.json());

// Roteamento
const userRoutes = require('./routes/userRoutes');
app.use('/users', userRoutes);

// Endpoint de teste
app.get('/', (req, res) => {
  res.send('Olá, mundo!');
});

// Inicia o servidor
app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
