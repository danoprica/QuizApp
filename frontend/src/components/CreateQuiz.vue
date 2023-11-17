<template>
  <h1>Create a quiz</h1>
  <h3>Title</h3>
  <div class="flex flex-column gap-2">
    <InputText id="title" v-model="title"/>
  </div>
  <h3>Description</h3>
  <div class="flex flex-column gap-2">
    <InputText id="description" v-model="description"/>
  </div>
  <br>
  <div class="flex flex-column gap-2">
    <Dropdown v-model="selectedCategory" :options="categories" optionLabel="name" placeholder="Select a Category" class="w-full md:w-14rem" />
  </div>
  <CreateQuestion />
  <div class="text-center mt-6">
    <Button @click="createQuiz">Create quiz</Button>
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import QuizApi from "../api/quiz";
  import { useQuiz } from "../store/modules/quiz";
  import { useUser } from "../store/modules/user";
  import { useNewQuiz } from "../store/modules/newQuiz";
  import router from "../router";
  import CreateQuestion from './CreateQuestion.vue';

  const quizStore = useQuiz();
  const userStore = useUser();
  const newQuizStore = useNewQuiz();

  const quizApi = new QuizApi();

  let categories = quizStore.categories.map(c => c.name);

  categories = categories.map((category) => ({name: category}));

  categories = ref(categories);
  const selectedCategory = ref();
  
  const availableCategories = quizStore.categories;  

  const createQuiz = () => {
    const selectedCategoryName = selectedCategory._rawValue.name;
    const selectedCategoryObj =  availableCategories.find(category => category.name === selectedCategoryName );
    const selectedCategoryId = selectedCategoryObj.id;

    const newQuiz = {
      "title": title.value,
      "description": description.value,
      "difficulty": "string",
      "category_id": selectedCategoryId,
      "owner_id": userStore.userId
    }
    
    const quizzes = quizStore.initialQuizzes;

    const lastQuiz = quizzes[quizzes.length - 1];
    const newQuizId = lastQuiz.id + 1;

    quizApi.createQuiz(newQuiz);

    newQuizStore.questions.forEach(function (question) {
      question.quiz_id = newQuizId;
      console.log(question);
      quizApi.createQuestion(question);
    })

    newQuizStore.questions = [];
    router.push("/");
  }
</script>