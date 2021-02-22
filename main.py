import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Automatização de processos se refere ao uso de equipamentos e sistemas ao executar tarefas repetitivas e operacionais. {os.linesep}Assim sobra para o profissional mais tempo para pensar estrategicamente, utilizando suas competências no crescimento dos resultados da empresa.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Tenha processos que funcionam! Coloque robôs para trabalhar com planilhas, relatórios, sistemas de gestão, para captar, analisar e entender dados!{os.linesep}')
    elif resposta == '3':
        print(
            f'{os.linesep}{nome} Elimine erros e duplicidade de trabalho.{os.linesep}')
        print(
            f'{os.linesep}{nome} Tenha bots operando 24 horas por dia, 7 dias por semana.  {os.linesep}')
        print(f'{os.linesep}{nome} Padronize e aumente a qualidade dos produtos e serviços oferecidos. {os.linesep}')
        print(
            f'{os.linesep}{nome} Reduza custos operacionais e melhore a performance.{os.linesep}')
        print(f'{os.linesep}{nome} Libere funcionários de tarefas repetitivas para que se concentrem naquelas mais estratégicas.{os.linesep}')
        print(f'{os.linesep}{nome} Ganho na Produtividade.{os.linesep}')
        print(f'{os.linesep}{nome} Diminuição das tarefas repetitivas{os.linesep}')
        print(f'{os.linesep}{nome} Padronização dos produtos e serviços.{os.linesep}')
        print(
            f'{os.linesep}{nome} Reduza custos operacionais e melhore a performance.{os.linesep}')

    elif resposta == '4':
        print(f'{os.linesep}{nome} Automatização de processos corresponde à adoção de sistemas ou equipamentos focados na execução de tarefas operacionais e repetitivas. {os.linesep}A automatização de processos envolve o uso de ferramentas para execução das atividades operacionais e de rotina de uma empresa.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome} Algumas pessoas têm dúvida se automatização de processos e automação se referem à mesma coisa. {os.linesep}Ainda que semelhantes, não são conceitos iguais. A automação é quando uma atividade pode ser executada sem interferência ou intervenção humana. {os.linesep}Por exemplo, um sistema de dados analíticos coleta informações, buscando padrões ou tendências, que serão analisadas por um time de marketing em busca de oportunidades. {os.linesep}Já a automatização parte do princípio de que um ser humano precisa programar, gerenciar ou controlar a ação.{os.linesep} No sistema de dados analíticos, por exemplo, você pode criar metas configuradas para avaliação dos resultados.{os.linesep}')
    elif resposta == '7':
        print(f'{os.linesep}{nome} Vivemos na era da informática, o que significa a presença quase absoluta de sistemas computacionais no tratamento da informação. {os.linesep} Grande parte desses sistemas são capazes de controlar praticamente todos os processos empresariais que existem. {os.linesep}O potencial disso tudo é gigantesco. {os.linesep}Inúmeras atividades são simplificadas quando recebem o auxílio de ferramentas automatizadas, como: {os.linesep}pagamento e recebimento de títulos em aberto; {os.linesep}conciliação de contas; análise do fluxo de caixa; criação de pedidos internos; {os.linesep} identificação de baixas no estoque; /{os.linesep}transferência de produtos entre unidades; {os.linesep}contato com clientes; {os.linesep}negociação de débitos. {os.linesep}Portanto, a automatização de processos tem como principal objetivo otimizar o tempo dedicado para tarefas de rotina, permitindo ao profissional ou gestor focar no essencial para o crescimento do negócio: estratégia.{os.linesep}')
    elif resposta == '7':
        print(f'{os.linesep}-Automatização de processos industriais.{os.linesep}')
        print(f'-Automatização de processos de TI.{os.linesep}')
        print(f'-Automatização de processos de compras.{os.linesep}')
        print(
            f'-Automatização de processos contábeis e financeiros.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3, 4, 5, 6 ou 7')


def start():
    # Apresentar o chatbot
    print('Olá! Seja Bem-vindo ')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - O que é automação?{os.linesep}[2] - Vale a pena automatizar processos?{os.linesep}[3] - Quais as vantagens de usar automação?{os.linesep}[4] - O que é automatização de processos?{os.linesep}[5] - Qual a diferença entre automação e automatização?{os.linesep}[6] - Objetivo da automatização de processos?{os.linesep}[7] - Exemplos de automatização de processos?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
