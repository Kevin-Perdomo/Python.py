import pandas as pd

# Dados dos Stakeholders
data = {
    "Nome": [
        "Maria Santos", "Pedro Oliveira", "Ana Paula Lima", "João Silva", 
        "Carla Ferreira", "Roberto Costa", "Daniela Souza", "Felipe Andrade", 
        "Lucas Mendes", "Fernanda Lima"
    ],
    "Telefone": [
        "(11) 98765-4321", "(11) 98888-1234", "(11) 98989-5678", "(11) 99777-4567", 
        "(11) 99666-7890", "(11) 99555-1234", "(11) 99444-5678", "(11) 99333-6789", 
        "(11) 99222-2345", "(11) 99111-3456"
    ],
    "Email": [
        "maria.santos@prefeitura.vilanova.gov.br", "pedro.oliveira@transportes.sp.gov.br", 
        "ana.lima@ambiental.gov.br", "joao.silva@engenharia.com", 
        "carla.ferreira@construtora.com", "roberto.costa@infraestrutura.com", 
        "daniela.souza@municipio.saopedro.gov.br", "felipe.andrade@comercio.vilanova.com", 
        "lucas.mendes@consultoria.com", "fernanda.lima@moradores.saopedro.com"
    ],
    "Interesse no Projeto": [
        "Garantir que o projeto atenda às necessidades dos cidadãos de Vila Nova", 
        "Garantir que a ponte melhore a logística e o transporte na região", 
        "Assegurar que o projeto cumpra com as regulamentações ambientais", 
        "Garantir a execução bem-sucedida do projeto", 
        "Assegurar que o projeto seja executado conforme o contrato", 
        "Supervisionar a qualidade da construção", 
        "Assegurar que a ponte atenda às necessidades dos cidadãos de São Pedro", 
        "Garantir que a ponte beneficie o comércio local", 
        "Oferecer consultoria técnica e garantir a viabilidade do projeto", 
        "Garantir que a construção não afete negativamente os moradores"
    ],
    "Por que do Interesse": [
        "Prefeita de Vila Nova, objetivo é melhorar a infraestrutura da cidade", 
        "Diretor da Agência Nacional de Transportes Terrestres", 
        "Representante da agência ambiental", 
        "Gerente do projeto", 
        "Diretora da empresa construtora", 
        "Engenheiro de qualidade", 
        "Prefeita de São Pedro", 
        "Presidente da Associação Comercial de Vila Nova", 
        "Consultor técnico do projeto", 
        "Presidente da Associação de Moradores de São Pedro"
    ],
    "Poder no Projeto": [
        "Alto", "Médio", "Médio", "Alto", "Médio", "Médio", 
        "Alto", "Médio", "Médio", "Baixo"
    ],
    "Forma de Apresentação": [
        "Reuniões presenciais e relatórios", "Relatórios e e-mails", 
        "Relatórios e reuniões", "Reuniões e relatórios", 
        "Relatórios e e-mails", "Relatórios e reuniões", 
        "Reuniões presenciais e relatórios", "E-mails e reuniões", 
        "Relatórios e reuniões", "E-mails e reuniões comunitárias"
    ],
    "Frequência": [
        "Mensal", "Bimestral", "Trimestral", "Semanal", 
        "Quinzenal", "Semanal", "Mensal", "Bimestral", 
        "Mensal", "Trimestral"
    ]
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Salvar para Excel
file_path = r'C:\Users\kevin\Desktop\Gerencia de Projetos\Stakeholders.xlsx'
df.to_excel(file_path, index=False)