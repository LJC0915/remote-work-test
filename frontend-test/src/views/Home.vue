<template>
  <el-tabs v-model="tab">
    <el-tab-pane label="表格" name="form">
      <test-form />
    </el-tab-pane>
    <el-tab-pane label="股價資訊" name="dataTable"><Table /></el-tab-pane>
  </el-tabs>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Table from "@/components/Table.vue";
import TestForm from "@/components/TestForm.vue";
@Component({
  components: { TestForm, Table },
})
export default class Home extends Vue {
  tab = "form";
}
</script>

<style></style>
