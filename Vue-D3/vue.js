// https://unpkg.com/vue-d3@0.1.0 --> only adds d3 to Vue.prototype but it wasn't working as expected (d3 is lower case)
Vue.prototype.$d3 = d3;
const URL = 'https://demo5147591.mockable.io/miserables'; // data copied from below link because of jsonp support

//'https://bl.ocks.org/mbostock/raw/4062045/5916d145c8c048a6e3086915a6be464467391c62/miserables.json';
//console.log(window.d3);
const d3ForceGraph = {
    template: `
  <div>
    {{mousePosition}}
    <button @click="reload">reload</button>
    <svg width="960" height="600" 
    	@mousemove="onMouseMove($event)"></svg>
  </div>
  `,
    data() {
        return {
            nodes: [],
            links: [],
            simulation: undefined,
            mousePosition: {
                x: 0,
                y: 0
            }
        }
    },
    mounted() {
        this.loadData(); // initially load json
    },
    methods: {
        // load data
        loadData() {
            this.$svg = $(this.$el).find('svg');
            let svg = this.$d3.select(this.$svg.get(0)), //this.$d3.select("svg"),
                width = +svg.attr("width"),
                height = +svg.attr("height");
            //console.log($(this.$el).find('svg').get(0));

            this.simulation = this.$d3.forceSimulation()
                .force("link", this.$d3.forceLink().id(function(d) {
                    return d.id;
                }))
                .force("charge", this.$d3.forceManyBody())
                .force("center", this.$d3.forceCenter(width / 2, height / 2));
            let color = this.$d3.scaleOrdinal(this.$d3.schemeCategory20);
            $.getJSON(URL, (graph) => {
                //d3.json("miserables.json", function(error, graph) { // already loaded
                //if (error) throw error; // needs to be implemented differently
                let nodes = graph.nodes;
                let links = graph.links;

                let link = svg.append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(links) //graph.links)
                    .enter().append("line")
                    .attr("stroke-width", function(d) {
                        return Math.sqrt(d.value);
                    });

                let node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("circle")
                    .data(nodes) //graph.nodes)
                    .enter().append("circle")
                    .attr("r", 5)
                    .attr("fill", function(d) {
                        return color(d.group);
                    })
                    .call(this.$d3.drag()
                        .on("start", this.dragstarted)
                        .on("drag", this.dragged)
                        .on("end", this.dragended));

                node.append("title")
                    .text(function(d) {
                        return d.id;
                    });

                this.simulation
                    .nodes(graph.nodes)
                    .on("tick", ticked);

                this.simulation.force("link")
                    .links(links); //graph.links);

                function ticked() {
                    link
                        .attr("x1", function(d) {
                            return d.source.x;
                        })
                        .attr("y1", function(d) {
                            return d.source.y;
                        })
                        .attr("x2", function(d) {
                            return d.target.x;
                        })
                        .attr("y2", function(d) {
                            return d.target.y;
                        });

                    node
                        .attr("cx", function(d) {
                            return d.x;
                        })
                        .attr("cy", function(d) {
                            return d.y;
                        });
                }
            })
        },
        reload() {
            //console.log('reloading...');
            this.$svg.empty(); // clear svg --> easiest way to re-create the force graph.
            this.loadData();
        },
        // mouse events
        onMouseMove(evt) {
            //console.log(evt, this)
            this.mousePosition = {
                x: evt.clientX,
                y: evt.clientY
            }
        },
        // drag event handlers
        dragstarted(d) {
            if (!this.$d3.event.active) this.simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        },
        dragged(d) {
            d.fx = this.$d3.event.x;
            d.fy = this.$d3.event.y;
        },
        dragended(d) {
            if (!this.$d3.event.active) this.simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }
    }
};

new Vue({
    el: '#app',
    data() {
        return {}
    },
    components: {
        d3ForceGraph
    }
});
