<template>
  <form v-on:submit.prevent="addQuestion">
    <h3>Question</h3>
    <div class="flex flex-column gap-2">
      <label>Question text</label>
      <InputText id="question" v-model="question" :class="{'p-invalid': question.length === 0 && state.success === false }"/>
    </div>
    <h3>Answers</h3>
    <div class="flex flex-column gap-2">
      <label>Answer 1</label>
      <InputText id="answer1" v-model="answer1" :class="{'p-invalid': answer1.length === 0 && state.success === false }"/>
    </div>
    <div class="flex flex-column gap-2">
      <label>Answer 2</label>
      <InputText id="answer2" v-model="answer2" :class="{'p-invalid': answer2.length === 0 && state.success === false }"/>
    </div>
    <div class="flex flex-column gap-2">
      <label>Answer 3</label>
      <InputText id="answer3" v-model="answer3" :class="{'p-invalid':answer3.length === 0 && state.success === false }"/>
    </div>
    <div class="flex flex-column gap-2">
      <label>Answer 4</label>
      <InputText id="answer4" v-model="answer4" :class="{'p-invalid':answer4.length === 0 && state.success === false }"/>
    </div>
    <h3>Correct answer</h3>
    <div class="card flex">
      <div class="flex flex-column gap-3">
        <div v-for="category in categories" :key="category.key" class="flex align-items-center">
            <RadioButton v-model="selectedCategory" :inputId="category.key" name="dynamic" :value="category.name" />
            <label :for="category.key" class="ml-2">{{ category.name }}</label>
        </div>
        <div v-if="selectedCategory === ''  && state.success === false" class="p-error">Answer is required.</div>
      </div>
    </div>
    <div class="mt-4">
      <Button type="submit">Add question</Button>
    </div>
  </form>
</template>

<script setup>
import { reactive } from 'vue';
import { ref, computed } from 'vue';
import { useNewQuiz } from "../store/modules/newQuiz";
import { useVuelidate } from '@vuelidate/core'
import { required, minLength } from '@vuelidate/validators'

const newQuizStore = useNewQuiz();

const question = ref('');
const answer1 = ref('');
const answer2 = ref('');
const answer3 = ref('');
const answer4 = ref('');
const selectedCategory = ref('');
const categories = ref([
    { name: '1', key: '1' },
    { name: '2', key: '2' },
    { name: '3', key: '3' },
    { name: '4', key: '4' }
]);

const rules = computed(() => (
  {
    question: {
      required
    },
    answer1: {
      required
    },
    answer2: {
      required
    },
    answer3: {
      required
    },
    answer4: {
      required
    },
    selectedCategory: {
      required
    }
  }
));

const state = reactive({
    success: true,
});

const $v = useVuelidate(rules, { question, answer1, answer2, answer3, answer4, selectedCategory });

const addQuestion = () => {
  console.log(state.success);

  state.success = false;

  console.log(state.success);

  const result = $v.value.$validate();
  result.then((res) => {
    if(res) {
      let correct_answer = selectedCategory.value;
      correct_answer = correct_answer.toString();
      console.log(correct_answer);
      let newQuestion = {
      "question_text": question.value,
      "options": answer1.value + ',' + answer2.value + ',' + answer3.value + ',' + answer4.value,
      "correct_answer": correct_answer
      }
      newQuizStore.addQuestion(newQuestion);
      state.success=true;
      alert('Question added');
    }
  }).catch((err) => {
    console.log(err);
  })
}

</script>