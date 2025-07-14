def is_number_or_error(number):

    try:

        int(number)

    except Exception:
        print("Entrada não é um numero válido !")
        raise

def is_option_invalid(option,available_options_cli=[]):

    try:

        if int(option) not in available_options_cli:

            raise
    
    except Exception:

        print("Opção indisponivel !")
        raise
        
