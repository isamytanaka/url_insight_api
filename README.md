# URL Insight API

[![URL Insight API](https://img.shields.io/badge/URL_Insight_API-Data_Scanner-4B0082?style=flat&logo=search&logoColor=white&labelColor=4B0082&color=6A5ACD)](https://github.com/seuusuario/url-insight-api)
![Versão](https://img.shields.io/badge/Version-1.1.0-00CED1?style=flat&logo=semantic-release&logoColor=white&labelColor=008B8B&color=20B2AA)
![Licença](https://img.shields.io/badge/License-MIT-DAA520?style=flat&logo=open-source-initiative&logoColor=white&labelColor=B8860B&color=FFD700)
![Construído com Python](https://img.shields.io/badge/Built_with-Python-306998?style=flat&logo=python&logoColor=white&labelColor=2B4A78&color=4682B4)
![Framework Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat&logo=flask&logoColor=white&labelColor=2F4F4F&color=708090)
![Open Source](https://img.shields.io/badge/Open_Source-Yes-228B22?style=flat&logo=github&logoColor=white&labelColor=006400&color=32CD32)
![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-FF8C00?style=flat&logo=git&logoColor=white&labelColor=CD6600&color=FFA500)
![Documentação](https://img.shields.io/badge/Documentação-Disponível-1E90FF?style=flat&logo=readthedocs&logoColor=white&labelColor=104E8B&color=4682B4)
![Estrelas](https://img.shields.io/badge/Stars-GitHub-6A5ACD?style=flat&logo=github&logoColor=white&labelColor=483D8B&color=9370DB)
![Contribuições](https://img.shields.io/badge/Contribuidores-Bem_vindos-9932CC?style=flat&logo=git&logoColor=white&labelColor=800080&color=BA55D3)
![Tecnologias](https://img.shields.io/badge/Tecnologias-Python_Flask_API-2E8B57?style=flat&logo=code&logoColor=white&labelColor=006400&color=3CB371)


---

## Sobre o Projeto

A **URL Insight API** fornece dados abrangentes sobre uma URL fornecida, incluindo:

### Funcionalidades

1. **Informações de Domínio**  
   Recupera dados Whois como data de registro, registrador, país, DNS e status do domínio.

2. **Informações HTTP**  
   Retorna código de status HTTP, tempo de resposta, tamanho da página e cabeçalhos.

3. **Informações HTTPS**  
   Extrai detalhes do certificado SSL (sujeito, emissor, validade).

4. **Informações Gerais**  
   Tipo de conteúdo, tamanho total da resposta e tempo de carregamento.

5. **Cabeçalhos de Segurança**  
   Detecta configurações como HSTS e Content Security Policy.

6. **Verificação de Vulnerabilidades**  
   Realiza varredura nos ports 80 e 443 em busca de vulnerabilidades conhecidas.

---

## Como Usar

Envie uma requisição `GET` com o parâmetro `URL` para o endpoint:

```http
GET http://127.0.0.1:5000/get_info?URL=example.com
