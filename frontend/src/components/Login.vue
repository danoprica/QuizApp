<template>
    <div class="card">
        <div class="flex flex-column md:flex-row">
            <div class="w-full flex flex-column align-items-center justify-content-center gap-3 py-5">
              <form @submit.prevent="handleSubmit">
                <div class="flex flex-wrap justify-content-center align-items-center gap-2">
                    <label class="w-6rem">Username</label>
                    <InputText id="username" type="text" v-model="username" class="w-12rem" />
                </div>
              </form>
              <Button label="Login" icon="pi pi-user" @click="login" class="w-10rem mx-auto"></Button>
            </div>
        </div>
    </div>
</template>


<script setup>
import { onMounted, onUpdated } from "vue";
import QuizApi from "../api/quiz";
import { useUser } from "../store/modules/user";
import router from "../router";

const quizApi = new QuizApi();
const userStore = useUser();

let usersResponse = null;

onMounted(async () => {
   usersResponse = await quizApi.getAllUsers();
   usersResponse =  usersResponse.data.value;
   console.log(usersResponse);
});


const login = () => {
  let inputUserName = username.value;
  let checkUser = usersResponse.find((user) => user.username === inputUserName);

  if (checkUser) {
    userStore.setUserName(inputUserName);
    userStore.setUserId(checkUser.id);
    router.push("/");
  }

}

</script>