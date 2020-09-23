import cupom;

# nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
# logradouro = "Av. Projetada Leste"
# numero = 500
# complemento = "EUC F32/33/34"
# bairro = "Br. Sta Genebra"
# municipio = "Campinas"
# estado = "SP"
# cep = "13080-395"
# telefone = "(19) 3756-7408"
# observacao = "Loja 1317 (PDP)"
# cnpj = "42.591.651/0797-34"
# inscricao_estadual = "244.898.500.113"

def test_loja_completa():
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_nome_vazio():
    # global nome_loja
    cupom.nome_loja = ""
    assert cupom.imprime_dados_loja() == '''O campo nome da loja é obrigatório'''
    cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
    # global logradouro
    cupom.logradouro = ""
    assert cupom.imprime_dados_loja() == '''O campo logradouro do endereço é obrigatório'''
    cupom.logradouro = "Av. Projetada Leste"

def test_numero_zero():
    # global numero
    cupom.numero = 0
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, s/n EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
    cupom.numero = 500

def test_municipio_vazio():
    # global municipio
    cupom.municipio = ""
    assert cupom.imprime_dados_loja() == '''O campo município do endereço é obrigatório'''
    cupom.municipio = "Campinas"

def test_estado_vazio():
    # global estado
    cupom.estado = ""
    assert cupom.imprime_dados_loja() == '''O campo estado do endereço é obrigatório'''
    cupom.estado = "SP"

def test_cnpj_vazio():
    # global cnpj
    cupom.cnpj = ""
    assert cupom.imprime_dados_loja() == '''O campo CNPJ da loja é obrigatório'''
    cupom.cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazia():
    # global inscricao_estadual
    cupom.inscricao_estadual = ""
    assert cupom.imprime_dados_loja() == '''O campo inscrição estadual da loja é obrigatório'''
    cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
#     global nome_loja
#     global logradouro
#     global numero
#     global complemento
#     global bairro
#     global municipio
#     global estado
#     global cep
#     global telefone
#     global observacao
#     global cnpj
#     global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "LOJAS AMERICANAS S.A."
    cupom.logradouro = "R SACADURA CABRAL"
    cupom.numero = 102
    cupom.complemento = ""
    cupom.bairro = "GAMBOA"
    cupom.municipio = "RIO DE JANEIRO"
    cupom.estado = "RJ"
    cupom.cep = "20.221-160"
    cupom.telefone = "(21) 2206-6708"
    cupom.observacao = "47.11-3-02 Comercio varejista de mercadorias em geral"
    cupom.cnpj = "33.014.556/0001-96"
    cupom.inscricao_estadual = "85.687.08-5"

    #E atualize o texto esperado abaixo
    assert cupom.imprime_dados_loja() == '''LOJAS AMERICANAS S.A.
R SACADURA CABRAL, 102 
GAMBOA - RIO DE JANEIRO - RJ
CEP:20.221-160 Tel (21) 2206-6708
47.11-3-02 Comercio varejista de mercadorias em geral
CNPJ: 33.014.556/0001-96
IE: 85.687.08-5
'''
