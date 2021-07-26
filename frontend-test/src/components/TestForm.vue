<template>
  <el-form
    id="test-form"
    ref="form"
    :model="form"
    label-width="80px"
    :rules="rules"
  >
    <el-form-item label="姓名" prop="name">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="電話" prop="phone">
      <el-input v-model="form.phone" type="tel" />
    </el-form-item>
    <el-form-item label="聯絡地址" prop="address">
      <el-input v-model="form.address" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit"> Submit </el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { FormProps } from "@/types/FormProps";

@Component
export default class TestForm extends Vue {
  form: FormProps = {
    name: "",
    phone: "",
    address: "",
  };

  rules = {
    phone: [{ validator: this.checkPhone, trigger: ["blur", "change"] }],
  };

  checkPhone(rule, value: string, cb): void {
    const phoneReg = /\d+$/;
    if (value === "") {
      cb();
    } else if (Number.isNaN(Number(value))) {
      cb(new Error("請輸入數字"));
    } else if (!phoneReg.test(value)) {
      cb(new Error("請輸入數字"));
    } else {
      cb();
    }
  }
  onSubmit(): void {
    // TODO: validate
    this.$swal({ icon: "success", text: "Submit Success" });
  }
}
</script>

<style></style>
