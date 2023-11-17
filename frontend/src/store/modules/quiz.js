/* eslint-disable no-console */
import { defineStore } from "pinia";

export const useQuiz = defineStore("quiz", {
  state: () => {
    return {
      categories: [],
      selectedCategory: null,
      selectedQuiz: null,
      quizStatus: null,
      selectedDifficulty: null,
      initialQuizzes: [],
      quizzes: [],
      users: [],
      correctAnswers: 0,
    }
  },
  getters: {
    
  },
  actions: { 
    setSelectedQuiz(quiz) {
      this.selectedQuiz = quiz;
    },
    setQuizzes(quizzes) {
      this.quizzes = quizzes;
    },
    setInitialQuizzes(initialQuizzes) {
      this.initialQuizzes = initialQuizzes;
    },
    setCategories(categories) {
      this.categories = categories;
    },
    setSelectedCategory(category) {
      this.selectedCategory = category;
    },
    setDifficulty(difficulty) {
      this.selectedDifficulty = difficulty;
    },
    setQuizStatus(status) {
      this.quizStatus = status;
    },
    setUsers(users){
      this.users = users;
    },
  },
})
