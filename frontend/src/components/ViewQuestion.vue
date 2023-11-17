<template>
  <h2 class="text-center">{{ question.question_text }}</h2>
  <div
    v-for="(choice, index) in props.question.options.split(',')"
    :key="index"
    class="flex justify-content-center mt-3"
    isCorrect
  >
    <RadioButton
      @click="incrementAnswer"
      v-model="state.selectedChoice"
      :inputId="index"
      name="dynamic"
      :value="choice"
    />
    <label :for="index" class="ml-2 text-xl text-center">{{ choice }}</label>
  </div>
</template>

<script setup>
import { reactive, watch } from "vue";
import { useQuiz } from "../store/modules/quiz";

const quizStore = useQuiz();

const props = defineProps({
  question: {
    type: String,
    required: true,
  },
  choices: {
    type: Array,
    required: true,
  },
  onAnswer: {
    type: Function,
    required: true,
  },
});

const state = reactive({
  selectedChoice: null,
});

// const optionsArray = props.question.options.split(',');
// let selectedIndex = optionsArray.findIndex(o => o == state.selectedChoice) + 1;

// const incrementAnswer = () => {
//   console.log(selectedIndex);
  // if(selectedIndex == props.question.correct_answer){
  //    quizStore.correctAnswers = quizStore.correctAnswers + 1;
  // }
//}

watch(
  () => state.selectedChoice, 
  async (value) => {
    const optionsArray = props.question.options.split(',');
    let selectedIndex = optionsArray.findIndex(o => o == value) + 1;
    console.log(selectedIndex);
    console.log(props.question.correct_answer);
    if(selectedIndex == props.question.correct_answer){
      props.question.correct_input = true;
    } else {
      props.question.correct_input = false;
    }
  }
);

</script>
