(window.webpackJsonp=window.webpackJsonp||[]).push([["chunk-4fba"],{aIQd:function(t,e,a){"use strict";a.r(e);var r=a("d5rn"),l={name:"Table",props:{worklist:{type:Array,require:!0,default:function(){return[]}}},data:function(){return{gridData:[],listQuery:{work_id:0},sqldetail:"",dialogSqlDetail:!1,dialogExecResVisible:!1,activeName:"1",list:null,flag:!0}},methods:{formatter:function(t){var e=t.work_id,a=new Date(1e3*e),r=a.getFullYear(),l=a.getMonth()+1,n=a.getDate(),i=a.getHours(),o=a.getMinutes(),s=a.getSeconds();return o<10?r+"-"+l+"-"+n+" "+i+":"+("0"+o)+":"+s:i<10?r+"-"+l+"-"+n+" "+("0"+i)+":"+o+":"+s:s<10?r+"-"+l+"-"+n+" "+i+":"+o+":"+("0"+s):r+"-"+l+"-"+n+" "+i+":"+o+":"+s},handleSqlDetail:function(t){this.dialogSqlDetail=!0,this.sqldetail=t.replace(/\n/g,"<br/>")},handleExecResDetail:function(t){var e=this;this.dialogExecResVisible=!0,this.listQuery.work_id=t,Object(r.b)(this.listQuery).then(function(t){e.gridData=t})}}},n=a("KHd+"),i=Object(n.a)(l,function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.worklist,"default-sort":{prop:"work_id",order:"descending"},"element-loading-text":"Loading",border:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{formatter:t.formatter,label:"DateTime",prop:"work_id",align:"center",sortable:""}}),t._v(" "),a("el-table-column",{attrs:{label:"工单标题",prop:"workname",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{label:"数据库名",prop:"db_name",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{label:"执行语句",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-button",{attrs:{size:"small",type:"text",icon:"el-icon-info"},on:{click:function(a){t.handleSqlDetail(e.row.db_sql)}}},[t._v("详细")])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"审批人",width:"150",align:"center",prop:"auditor"}}),t._v(" "),a("el-table-column",{attrs:{label:"执行人",width:"150",align:"center",prop:"dba"}}),t._v(" "),a("el-table-column",{attrs:{label:"工单状态",width:"150",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[0===e.row.work_status?a("el-tag",{attrs:{type:"info"}},[t._v("等待审核")]):t._e(),t._v(" "),1===e.row.work_status?a("el-tag",{attrs:{type:"warning"}},[t._v("等待执行")]):t._e(),t._v(" "),2===e.row.work_status?a("el-tag",{attrs:{type:"success"}},[t._v("后台操作中")]):t._e(),t._v(" "),3===e.row.work_status?a("el-tag",{attrs:{type:"success"}},[t._v("工单完成")]):t._e(),t._v(" "),-1===e.row.work_status?a("el-tag",{attrs:{type:"danger"}},[t._v("已被驳回")]):t._e()]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"详情",width:"150",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[e.row.work_status<=-1?a("el-popover",{attrs:{placement:"right",width:"300",trigger:"click"}},[a("div",{attrs:{align:"left"},domProps:{innerHTML:t._s(e.row.rejected_note)}},[t._v(".")]),t._v(" "),a("el-button",{attrs:{slot:"reference",size:"mini",type:"text",icon:"el-icon-info"},slot:"reference"},[t._v("驳回原因")])],1):t._e(),t._v(" "),3===e.row.work_status?a("el-button",{attrs:{size:"small",type:"text",icon:"el-icon-info"},on:{click:function(a){t.handleExecResDetail(e.row.work_id)}}},[t._v("执行结果")]):t._e()]}}])}),t._v(" "),a("el-dialog",{attrs:{"append-to-body":!0,visible:t.dialogExecResVisible,title:"执行结果",width:"70%"},on:{"update:visible":function(e){t.dialogExecResVisible=e}}},[a("el-table",{attrs:{data:t.gridData}},[a("el-table-column",{attrs:{property:"c_time",label:"执行完成时间",width:"150"}}),t._v(" "),a("el-table-column",{attrs:{label:"执行状态",width:"150"},scopedSlots:t._u([{key:"default",fn:function(e){return[1===e.row.exec_status?a("el-tag",{attrs:{type:"success"}},[t._v("执行成功")]):t._e(),t._v(" "),-1===e.row.exec_status?a("el-tag",{attrs:{type:"danger"}},[t._v("执行失败")]):t._e()]}}])}),t._v(" "),a("el-table-column",{attrs:{property:"errormessage",label:"错误信息",width:"200"}}),t._v(" "),a("el-table-column",{attrs:{property:"SQL",label:"SQL内容"}})],1)],1),t._v(" "),a("el-dialog",{attrs:{"append-to-body":!0,visible:t.dialogSqlDetail,title:"SQL详情",width:"70%"},on:{"update:visible":function(e){t.dialogSqlDetail=e}}},[a("div",{attrs:{align:"left"},domProps:{innerHTML:t._s(t.sqldetail)}},[t._v(".")])])],1)},[],!1,null,null,null);i.options.__file="table.vue";var o=i.exports,s=a("fe1z"),c={components:{TableDetail:o},data:function(){return{username:"",currentPage1:1,pagesizes:[10,20,30,40],totalrows:0,listQuery:{page:1,page_size:10,author:"",workname:""},workers:[],flag:!0}},created:function(){this.fetchData()},methods:{fetchData:function(t){var e=this;Object(s.a)().then(function(a){e.listQuery.author=a.name,e.listQuery.work_status=t,Object(r.c)(e.listQuery).then(function(t){e.workers=t.results,e.totalrows=t.count})})},handleCurrentChange:function(t){this.listQuery.page=t,this.fetchData()},handleSizeChange:function(t){this.listQuery.page_size=t,this.fetchData()}}},u=Object(n.a)(c,function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-container"},[a("div",{staticClass:"filter-container"},[a("el-input",{staticClass:"filter-item",staticStyle:{width:"200px"},attrs:{size:"small",placeholder:"工单标题"},nativeOn:{keyup:function(e){if(!("button"in e)&&t._k(e.keyCode,"enter",13,e.key,"Enter"))return null;t.fetchData()}},model:{value:t.listQuery.workname,callback:function(e){t.$set(t.listQuery,"workname",e)},expression:"listQuery.workname"}}),t._v(" "),a("el-button",{staticClass:"filter-item",attrs:{size:"small",type:"primary",icon:"el-icon-search"},on:{click:function(e){t.fetchData()}}},[t._v("搜&刷")]),t._v(" "),a("router-link",{attrs:{to:"/task/create/"}},[a("el-button",{attrs:{size:"small",type:"primary",icon:"el-icon-edit"}},[t._v("填写工单")])],1),t._v(" "),a("el-button",{staticClass:"filter-item",staticStyle:{"margin-left":"10px"},attrs:{size:"small",type:"primary",icon:"el-icon-check"},on:{click:function(e){t.fetchData(0)}}},[t._v("未审核")])],1),t._v(" "),a("br"),t._v(" "),a("table-detail",{attrs:{worklist:t.workers}}),t._v(" "),a("div",{staticClass:"block"},[a("el-pagination",{attrs:{"current-page":t.currentPage1,total:t.totalrows,"page-sizes":t.pagesizes,"page-size":t.listQuery.page_size,layout:"total, sizes, prev, pager, next,  jumper"},on:{"current-change":t.handleCurrentChange,"size-change":t.handleSizeChange}})],1)],1)},[],!1,null,null,null);u.options.__file="tasklist.vue";e.default=u.exports},d5rn:function(t,e,a){"use strict";a.d(e,"c",function(){return l}),a.d(e,"a",function(){return n}),a.d(e,"d",function(){return i}),a.d(e,"b",function(){return o});var r=a("t3Un");function l(t,e){return Object(r.a)({url:"/workorder/workinfo/",method:"get",params:t})}function n(t){return Object(r.a)({url:"/workorder/workinfo/",method:"post",data:t})}function i(t,e){return Object(r.a)({url:"/workorder/workinfo/"+t+"/",method:"put",data:e})}function o(t,e){return Object(r.a)({url:"/workorder/executeres/",method:"get",params:t})}}}]);