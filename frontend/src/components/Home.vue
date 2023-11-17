<template>
    <!-- <SelectDifficulty v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" /> -->
    <div v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" class="mt-6">
      <SelectCategory />
    </div>
    <div v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED' && quizStore.selectedCategory" class="mt-6">
      <SelectQuiz />
    </div>
    <div v-if="quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED'" class="text-center mt-6">
      <Button @click="startQuiz" raised text label="Start!" :disabled="!quizStore.selectedQuiz"></Button>
    </div>
    <div v-if="quizStore.quizStatus === 'STARTED' || quizStore.quizStatus === 'FINISHED'" class="mt-6">
      <Quiz />
    </div>
    <div v-if="userStore.userName && quizStore.quizStatus !== 'STARTED' && quizStore.quizStatus !== 'FINISHED' " class="text-center mt-6" >
      <Button @click="createQuiz" raised text label="Create quiz" />
    </div>
</template>

<script setup>
  import { onMounted } from "vue";
  import SelectCategory from "./SelectCategory.vue";
  import SelectQuiz from "./SelectQuiz.vue";
  import Quiz from "./Quiz.vue";
  import QuizApi from "../api/quiz";
  import { useQuiz } from "../store/modules/quiz";
  import { useUser } from "../store/modules/user";
  import router from "../router";

  const quizApi = new QuizApi();

  const quizStore = useQuiz();
  const userStore = useUser();

  const startQuiz = () => {
  quizStore.setQuizStatus("STARTED");
  };

  const createQuiz = () => {
    router.push("/create-quiz");
  }

  onMounted(async () => {
  const quizzesResponse = await quizApi.getAllQuizzes();
  const usersResponse = await quizApi.getAllUsers();
  let categories = quizzesResponse.data.value.map((quiz) => quiz.category);

  categories = categories.filter((obj, index) => {
    return index === categories.findIndex(o => obj.id === o.id);
  });

  
  quizStore.setInitialQuizzes(quizzesResponse.data.value);
  console.log(quizStore.initialQuizzes)
  quizStore.setCategories(categories);
  quizStore.setUsers(usersResponse.data.value)

});


</script>