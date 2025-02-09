import { ref } from 'vue'

export const materiaisReciclaveisComChaveValor = ref([

    { id: 1, nome: "Plástico" },
    { id: 2, nome: "Vidro" },
    { id: 3, nome: "Papel" },
    { id: 4, nome: "Metal" },
    { id: 5, nome: "Organico" },
    { id: 6, nome: "Outros" }

])

export const materiaisReciclaveis = ref(materiaisReciclaveisComChaveValor.value.map((material) => material.nome));
