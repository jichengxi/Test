let vm = new Vue({
   el:'#app',
   directives: {
       focus:function(el,binding) {
           // 当cur==todo 就是true时，获取焦点
           if (binding.value) {
               el.focus();
           }
       }
   },
   data:{
       todos:[
           {IsSelected:false,title:'睡觉'},
           {IsSelected:false,title:'吃饭'},
           {IsSelected:false,title:'喝水'},
       ],
       a:'',
       cur:'',
       hash:'',
   },
   watch:{  // watch 默认只监控一层数据
        todos:{  // 默认写成函数就相当于默认写了handler
            handler() {
                localStorage.setItem('data',JSON.stringify(this.todos))  // localstorage默认存字符串
            },deep:true
        }
   },
   created(){  // ajax获取 初始化数据
        this.todos = JSON.parse(localStorage.getItem('data'))||this.todos

       // 监控hash值的变化
       this.hash = window.location.hash || '#all'
       window.addEventListener('hashchange',()=>{
            this.hash = window.location.hash;
       },false)
   },

   methods: {
        add(a){
            this.todos.push({IsSelected:false,title:this.a}),
            this.a = ''
        },
        remove(b){
            this.todos.splice(b,1)
        },
        remember(c){
            this.cur = c;
        },
        cancel(){
            this.cur = '';
        },
   },
   computed:{
       filtertodos(){
           if(this.hash === '#all') return this.todos
           if(this.hash === '#finish') return this.todos.filter(item=>item.IsSelected)
           if(this.hash === '#unfinish') return this.todos.filter(item=>!item.IsSelected)
           return this.todos
       }
   }


});
