<template>
  <el-table :data="mockData" style="width: 100%">
    <el-table-column prop="date" label="Date" />
    <el-table-column prop="close" label="Price" />
    <el-table-column prop="open" label="Open" />
    <el-table-column prop="high" label="High" />
    <el-table-column prop="low" label="Low" />
    <el-table-column prop="volume" label="Vol.">
      <template slot-scope="scope">
        {{ scope.row.volume.toLocaleString() }}
      </template>
    </el-table-column>
    <el-table-column prop="name" label="Change%">
      <template slot-scope="scope">
        <div :class="displayColor(scope.row.prevClose, scope.row.close)">
          {{ displayChange(scope.row.prevClose, scope.row.close) }}
        </div>
      </template>
    </el-table-column>
  </el-table>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Home extends Vue {
  calcChange(prevClose: number, close: number): number {
    return ((close - prevClose) / prevClose) * 100;
  }

  displayChange(prevClose: number, close: number): string {
    const change = this.calcChange(prevClose, close).toFixed(2);
    return `${change}%`;
  }

  displayColor(prevClose: number, close: number): string {
    const change = this.calcChange(prevClose, close);
    return change > 0 ? "up" : "down";
  }
  mockData = [
    {
      date: "01/06/2021",
      open: 125.08,
      high: 125.35,
      low: 123.94,
      prevClose: 124.61,
      close: 124.28,
      volume: 65184000,
      currency: "USD",
    },
    {
      date: "02/06/2021",
      open: 124.2,
      high: 125.22,
      low: 124.05,
      prevClose: 124.28,
      close: 125.06,
      volume: 59278864,
      currency: "USD",
    },
    {
      date: "03/06/2021",
      open: 124.66,
      high: 124.83,
      low: 123.14,
      prevClose: 125.06,
      close: 123.54,
      volume: 76229168,
      currency: "USD",
    },
    {
      date: "04/06/2021",
      open: 124.07,
      high: 126.16,
      low: 123.85,
      prevClose: 123.54,
      close: 125.89,
      volume: 75169000,
      currency: "USD",
    },
    {
      date: "07/06/2021",
      open: 126.05,
      high: 126.24,
      low: 124.85,
      prevClose: 125.89,
      close: 125.9,
      volume: 71057552,
      currency: "USD",
    },
    {
      date: "08/06/2021",
      open: 126.72,
      high: 128.44,
      low: 126.22,
      prevClose: 125.9,
      close: 126.74,
      volume: 74403776,
      currency: "USD",
    },
    {
      date: "09/06/2021",
      open: 127.34,
      high: 127.7,
      low: 126.57,
      prevClose: 126.74,
      close: 127.13,
      volume: 56877936,
      currency: "USD",
    },
    {
      date: "10/06/2021",
      open: 127.01,
      high: 128.16,
      low: 125.94,
      prevClose: 127.13,
      close: 126.11,
      volume: 71186424,
      currency: "USD",
    },
    {
      date: "11/06/2021",
      open: 126.53,
      high: 127.44,
      low: 126.1,
      prevClose: 126.11,
      close: 127.35,
      volume: 53522000,
      currency: "USD",
    },
    {
      date: "14/06/2021",
      open: 127.7,
      high: 130.48,
      low: 127.1,
      prevClose: 127.35,
      close: 130.48,
      volume: 96906488,
      currency: "USD",
    },
  ];
}
</script>

<style lang="scss" scoped>
.up {
  color: #f56c6c;
}

.down {
  color: #67c23a;
}
</style>
