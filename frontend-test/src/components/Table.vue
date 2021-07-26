<template>
  <el-tabs v-model="tab">
    <el-tab-pane label="表格" name="form">表格</el-tab-pane>
    <el-tab-pane label="股價資訊" name="dataTable">股價資訊</el-tab-pane>
  </el-tabs>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component
export default class Home extends Vue {
  tab = "form";
}
</script>

<style></style>
