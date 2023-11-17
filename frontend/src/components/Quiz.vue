<template>
  <div>
    <div v-if="quizStore.quizStatus !== 'FINISHED'">
      <h1 class="text-center">Quiz</h1>
      <p class="text-center" v-if="currentQuestionIndex < questions.length">
        {{ currentQuestionIndex + 1 }} / {{ questions.length }}
      </p>

        <ViewQuestion
          v-for="(question, index) in questions"
          :key="index"
          :question="question"
          :onAnswer="handleAnswer"
        />

      <div  class="text-center mt-6">
        <Button
          @click="finishQuiz"
          class="text-2xl"
          raised
          text
          label="Finish!"
        ></Button>
      </div>
    </div>

    <div v-if="quizStore.quizStatus === 'FINISHED'" class="text-center">
      <h2>Quiz Completed!</h2>
      <p>Your Score: {{ score }} / {{ questions.length }}</p>
      <Button
        @click="backToQuizSelection"
        class="text-2xl"
        raised
        text
        label="Back to Quiz Selection"
      ></Button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import ViewQuestion from "./ViewQuestion.vue";
import { useQuiz } from "@/store/modules/quiz";

const quizStore = useQuiz();
const questions = quizStore.selectedQuiz.questions;

const currentQuestionIndex = 0;
let score = 0;

const finishQuiz = () => {
  quizStore.setQuizStatus("FINISHED");
  questions.forEach((question) => { 
    if (question.correct_input === true) {
      score = score +1;
  }});
};

const backToQuizSelection = () => {
  quizStore.setQuizStatus("NOT_STARTED");
  for (let question in questions){
    console.log(question);
  }
};
</script>
