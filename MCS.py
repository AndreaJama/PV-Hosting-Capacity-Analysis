
# Monte Carlo Simulation

import compile_fluxo as fluxo
import py_dss_interface
import pandas as pd
import time
import gc
import itertools
import multiprocessing


# Função para executar a simulação de um cenário específico
def run_simulation(params):
    location_n, npfv_n, hora_n, dia, dss_file, curvas_file = params

    # Inicializa a interface OpenDSS
    dss = py_dss_interface.DSSDLL()

    num_OV, num_UV, num_SC, num_DT, buses_tensoes, Tensoes_abc_pu, v_max, v_min, total_pv_p, total_pv_q, \
        total_losses_p_kw, total_p_kw, total_q_kvar, total_pv_p_dict, total_pv_q_dict = \
        fluxo.compile_fluxo(dss, dss_file, dia, hora_n, curvas_file, location_n, npfv_n)

    # Coleta os resultados
    result = {
        "Location": location_n,
        "NPFV": npfv_n,
        "Hora": hora_n,
        "V_max": v_max,
        "V_min": v_min,
        "Num_OV": num_OV,
        "Num_UV": num_UV,
        "Num_SC": num_SC,
        "buses_voltages": Tensoes_abc_pu,
        "total_pv_p": total_pv_p,
        "total_pv_q": total_pv_q,
        "feeder_kw": total_p_kw,
        "feeder_kvar": total_q_kvar,
        "pv_kw": total_pv_p_dict,
        "pv_kvar": total_pv_q_dict,
        "perdas": total_losses_p_kw
    }

    # Libera o objeto dss após o uso
    del dss
    # Força a coleta de lixo para liberar memória
    gc.collect()

    return result

# Paralel process in Windows
if __name__ == '__main__':
    # Inputs
    dss_file = r"C:\DSS_Files\Run_IEEE123Bus.DSS"
    curvas_file = "C:\loadShape_Coelba_MT_dia_util.csv"
    dia = 'SOL' # Mude para 'CHUVA' para análise em dia chuvoso

    locations = list(range(1, 101))
    NPFVs = list(range(10, 101, 10))
    horas = list(range(1, 25))

    # Cria lista de parâmetros para cada cenário
    params_list = list(itertools.product(locations, NPFVs, horas, [dia], [dss_file], [curvas_file]))

    # Lista para armazenar os dados de cada cenário

    data_list = []

    start = time.time()

    # Cria um pool de processos

    with multiprocessing.Pool(processes = multiprocessing.cpu_count()) as pool:
        # Executa as simulações em paralelo
        data_list = pool.map(run_simulation, params_list)

    # Cria um dataframe único a partir da lista de dados
    df = pd.DataFrame(data_list)

    # Salva o dataframe em CSV
    #df.to_csv(fr"C:\Resultados\SMC_{dia}.csv", index = False)
