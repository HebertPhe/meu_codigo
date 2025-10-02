import sys
import os
import pytest

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import biblioteca

def test_adicionar_livro_manual():
    biblioteca.livros.clear()
    id_livro = '12345678'
    biblioteca.livros[id_livro] = {
        'titulo': 'Livro de Teste',
        'autor': 'Autor de Teste',
        'disponivel': True
    }

    assert id_livro in biblioteca.livros
    assert biblioteca.livros[id_livro]['titulo'] == 'Livro de Teste'