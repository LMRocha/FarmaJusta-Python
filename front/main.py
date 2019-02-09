#coding: utf-8

from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
import requests as req
import json

import urllib


class EnviarDenuncia(Screen):
    pass


class VisualizacaoConsulta(Screen):
    _info = None

    def set_medicamento_info(self,info):
        self._info = info

    def get_medicamento_info(self):
        return self._info

    def popula_campos(self):
        self.ids.label_resultado.text = self.get_medicamento_info();


class ConsultaRegistro(Screen):

    _numeroGREM = None
    _valorMedicamento = None
    _info = None


    def get_info_medicamento(self):
        return self._info

    def clicar_consultar(self):
        self.recupera_valor_medicamento()
        self.manager.get_screen('visualizar_consulta').set_medicamento_info(self._info)
        self.manager.current = 'visualizar_consulta'



    def recupera_valor_medicamento(self):
        self._numeroGREM = self.ids.num_germ.text
        self._valorMedicamento = self.ids.vlr_medicamento.text

        print("REGISTRO: " + self._numeroGREM)

        url_consulta_registro = "http://127.0.0.1:5000/consultaRegistro/?cod_registro=" + self._numeroGREM
        jsonObj = req.get(url_consulta_registro).json()
        print(jsonObj['meds'][0]['pmc20'])
        self.valida_valor_medicamento(preco = self._valorMedicamento,valorPMC=jsonObj['meds'][0]['pmc20'])


    def valida_valor_medicamento(self,preco,valorPMC):
        print(preco)

        if float(preco) >= float(valorPMC.replace(",", ".")):
            self._info = "ACIMA DO VALOR DECRETADO"

        else:
            self._info = "VALOR PADRÃO RECOMENDADO"



    def clica_cod_barras(self):
        cod_barras_fake = "123456789012"
        self.ids.cod_barras.text = cod_barras_fake
        pass

    def clica_encerrar(self):
        self.manager.current = 'auth'


    def chama_servico_consulta_registro(self):
        pass

class Auth(Screen):

    def clica_logar(self):
        login = self.ids.usr.text
        pwd = self.ids.pwd.text
        print("USR: "+login, "PWD: "+pwd)
        self.manager.current = 'consulta_grem'


class Main(App):

    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(Auth())
        sm.add_widget(ConsultaRegistro())
        sm.add_widget(VisualizacaoConsulta())
        return sm


if __name__ == '__main__':
    Main().run()