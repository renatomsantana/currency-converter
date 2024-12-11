# usa uma imagem base do Node.js
FROM node:18

# define o diretório de trabalho no container
WORKDIR /app

# copia os arquivos package.json e package-lock.json para dentro do container
COPY package*.json ./

# instala as dependências da aplicação
RUN npm install

# copia o restante dos arquivos da aplicação para dentro do container
COPY . .

# expõe a porta em que a aplicação estará rodando (se necessário)
EXPOSE 3000

# comando para rodar a aplicação (modifique conforme seu arquivo principal)
CMD ["npm", "start"]
const port = process.env.PORT || 3000; // Porta fornecida pelo Railway ou 3000 local
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
