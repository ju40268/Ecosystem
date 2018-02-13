<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <body>
    <div id="app">
      <div class="title">
        <h1> <a href="https://github.com/emiliorizzo/vue-d3-network">vue-d3-network</a> </h1>
        <!-- example control -->
        <ul class="menu">
          <li>
            <label> Node size  </label>
            <input type="range" min="1" max="100" v-model='nodeSize' /> {{ options.nodeSize }}
          </li>
          <li>
            <label>Render as  </label>
            <input type="radio" :value='false' v-model='canvas' />
            <label>SVG</label>
            <input type="radio" :value='true' v-model='canvas' />
            <label>Canvas</label>
          </li>
        </ul>
      </div>
      <d3-network ref='net' :net-nodes="nodes" :net-links="links" :options="options" />
    </div>
    </body>
  </div>
</template>

<script>

  import D3Network from 'vue-d3-network'
  export default {
    name: 'HelloWorld',
    components: {
      D3Network
    },
    data() {
    return {
        msg: 'Welcome to Your Vue.js App',
        nodes: [
          {id: 1, name: 'my awesome node 1'},
          {id: 2, name: 'my node 2'},
          {id: 3, name: 'orange node', _color: 'orange'},
          {id: 4, _color: '#0022ff'},
          {id: 5},
          {id: 6},
          {id: 7},
          {id: 8},
          {id: 9}
        ],
        links: [
          {sid: 1, tid: 2, _color: '#0022ff'},
          {sid: 2, tid: 8, _color: '#0022ff'},
          {sid: 3, tid: 4},
          {sid: 4, tid: 5},
          {sid: 5, tid: 6},
          {sid: 7, tid: 8},
          {sid: 5, tid: 8},
          {sid: 3, tid: 8},
          {sid: 7, tid: 9}
        ],
        nodeSize: 20,
        canvas: false

      }
    },
    computed: {
      options() {
        return {
          force: 3000,
          size: {w: 600, h: 600},
          nodeSize: this.nodeSize,
          linkWidth: 5,
          nodeLabels: true,
          canvas: this.canvas
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
