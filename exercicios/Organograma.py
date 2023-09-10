# entrada
#   1. Setor mais alto
#   2. nome1 nome2, nome2 é o setor responsavel pelo nome1
#   3. as entradas se encerram ao inserir "fim entrada"
#   4. a ultima entrada é o setor que deseja pesquisar
# saida
#   1. exibir o setor pesquisado
#   2. exibir os setores sob responsabilidade do sertor pesquisado
#   3. antes de exibir o proximo sertor exibir os setores sob responsabilidade do setor
#   5. exibir tudo em ordem alfabetica

def main():
    main_section = input()
    section_dict = get_section_dict()
    search_section = input()
    print(search_section)
    show_sections(section_dict, search_section)


def show_sections(section_dict, section):
    if section in section_dict.keys():
        section_dict[section].sort()
        for i in section_dict[section]:
            print(i)
            if i in section_dict.keys():
                show_sections(section_dict, i)


def get_section_dict():
    section_dict = {}
    while True:
        main_input = input()
        if main_input.lower() == "fim entrada":
            break
        section_tuple = main_input.split(" ")
        if section_tuple[1] in section_dict.keys():
            section_dict[section_tuple[1]].append(section_tuple[0])
        else:
            section_dict[section_tuple[1]] = [section_tuple[0]]
    return section_dict



if __name__ == "__main__":
    main()