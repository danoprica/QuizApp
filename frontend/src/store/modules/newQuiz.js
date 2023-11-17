import { defineStore } from "pinia";
import axios from "axios";

export const useNewQuiz = defineStore("newQuiz", {
  state: () => {
    return {
      questions: []
    }
  },
  actions: {
    addQuestion(question) {
      this.questions.push(question);
    }
  }
})