# criptografia-de-JulioCesar
repositório para o desafio de criptografia de Julio Cesar do Codenation

#passo 1
Gerei mensagem encriptada por requisicão HTTP [https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN] conforme orientado no desafio

#passo 2
Fiz o programa para desencriptar a mensagem encriptada pela criptografia de Julio Cesar em Python com número de casas = 5
No código, a mensagem encriptada foi trazida do arquivo answer.json, desencriptada e atualizada no arquivo.

#passo 3
Gerei o resumo criptográfico da mensagem desencriptada usando algorítimo SHA-1 e atualizei resumo no arquivo answer.json.
Conferi resumo criptográfico no https://www.browserling.com/tools/all-hashes e está correto o/

#passo 5
Tentei submeter o arquivo answer.json via POST para a API, porém não estava conseguindo.
No final, acabei submentendo pelo Postman.
Conheci esse site para testar post em API -> Test your front-end against a real API: https://reqres.in/ 
    Requisitos de envio do desafio:
    1 - A API espera um arquivo sendo enviado como multipart/form-data, como se fosse enviado por um formulário HTML, com um campo do tipo file com o nome answer.
    2 - Enviar código para [https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN]

