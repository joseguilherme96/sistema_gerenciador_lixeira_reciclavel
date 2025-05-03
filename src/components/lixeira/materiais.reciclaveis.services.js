import { ref } from 'vue'

export const materiaisReciclaveisComChaveValor = ref([

    { mat_colet_id: 1, nome: "Plástico" },
    { mat_colet_id: 2, nome: "Vidro" },
    { mat_colet_id: 3, nome: "Papel" },
    { mat_colet_id: 4, nome: "Metal" },
    { mat_colet_id: 5, nome: "Organico" },
    { mat_colet_id: 6, nome: "Outros" }

])

export const materiaisReciclaveis = ref(materiaisReciclaveisComChaveValor.value.map((material) => material.nome));
