(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[5405,3100],{77838:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return n(50948)}])},88223:function(e,t,n){"use strict";n.d(t,{o:function(){return o}});var s=n(97458),a=n(52983),i=n(89062),l=n(35240),r=n(6552);const o=a.forwardRef(((e,t)=>{let{children:n,contentWrapperCssClasses:a="flex-grow overflow-hidden",headerControl:o,headerWrapperCssClasses:c="bg-white h-16 flex items-center px-6 border-b border-gray-100 flex-shrink-0",id:d}=e;const u=(0,i.useRecoilValue)(l.qx);return(0,s.jsxs)("div",{id:d,ref:t,"data-onboarding-watch":"create_menu_new_button",className:"absolute inset-0 flex flex-col w-full overflow-y-auto",children:[o&&(0,s.jsx)("div",{className:c,children:o}),u?(0,s.jsx)(r.a,{size:"lg"}):(0,s.jsx)("div",{className:a,children:n})]})}));o.displayName="PageScaffold"},69429:function(e,t,n){"use strict";n.d(t,{ph:function(){return o},s8:function(){return c}});var s=n(97458),a=n(83849),i=n.n(a),l=(n(52983),n(4474)),r=n(2142);const o=e=>{let{childClassName:t,children:n,className:a,name:r,onClickViewAll:o}=e;return(0,s.jsxs)("div",{className:i()("flex flex-col items-start justify-start",a),children:[(0,s.jsxs)("div",{className:"flex items-center justify-between w-full",children:[(0,s.jsx)("div",{className:"text-base truncate font-lf-semi-bold",children:r}),(0,s.jsxs)("span",{onClick:o,className:"flex items-center text-sm text-actionPrimary cursor-pointer gap-x-2 font-lf-semi-bold hover:text-actionPrimaryHover",children:["View more ",(0,s.jsx)(l.J,{name:"arrow-right",className:"mt-1",small:!0})]})]}),(0,s.jsx)("div",{className:i()("w-full mt-4 gap-x-6",t),children:n})]})},c=e=>{let{onClick:t,src:n}=e;const{videoRef:a}=(0,r.x)();return(0,s.jsx)("div",{onClick:t,className:"flex items-center justify-center p-2 overflow-hidden bg-white rounded-lg cursor-pointer shadow-default hover:shadow-md",children:(0,s.jsx)("video",{ref:a,playsInline:!0,muted:!0,loop:!0,className:"object-cover w-full rounded-sm aspect-square",children:(0,s.jsx)("source",{src:n,type:"video/MP4"})})})}},12493:function(e,t,n){"use strict";n.d(t,{Z:function(){return l}});var s=n(97458),a=n(52983),i=n(4474);const l=e=>{let{actionIdentifier:t,children:n,className:l,color:r="blue",permanentClose:o=!1}=e;const[c,d]=(0,a.useState)(!1);(0,a.useEffect)((()=>{let e=!1;if(o){e=!("true"===localStorage.getItem("permanently-closed-".concat(t)))}else{const n=localStorage.getItem("closed-time-".concat(t));if(n){e=Date.now()-new Date(n).getTime()>864e5}else e=!0}d(e)}),[t,o]);const u=(0,a.useCallback)((()=>{o?localStorage.setItem("permanently-closed-".concat(t),"true"):localStorage.setItem("closed-time-".concat(t),(new Date).toISOString()),d(!1)}),[t,o]);return c?(0,s.jsxs)("div",{className:"".concat(l," flex items-center justify-between p-2 space-x-3 rounded-lg bg-").concat(r,"-50"),children:[(0,s.jsx)("div",{className:"flex-grow text-teal-800",children:n}),(0,s.jsxs)("button",{onClick:u,type:"button",className:"p-1 text-gray-900 rounded-md dark:bg-gray-800 hover:text-gray-500 dark:text-gray-300 focus:outline-none focus:ring-2 focus:ring-lf-teal",children:[(0,s.jsx)("span",{className:"sr-only",children:"Close message"}),(0,s.jsx)(i.J,{name:"cross",className:"w-6 h-6"})]})]}):(0,s.jsx)(s.Fragment,{})}},25477:function(e,t,n){"use strict";n.d(t,{t:function(){return a}});var s=n(52983);function a(e){let{defaultValue:t,sizeMap:n}=e;const a=e=>{let s={width:Number.POSITIVE_INFINITY,value:t};return n.forEach((t=>{let{value:n,width:a}=t;e<a&&a<s.width&&(s={width:a,value:n})})),s.width===Number.POSITIVE_INFINITY?{width:e,value:t}:s},[i,l]=(0,s.useState)(a(window.innerWidth));return(0,s.useEffect)((()=>{const e=()=>{const e=window.innerWidth;l(a(e))};return window.addEventListener("resize",e),e(),()=>{window.removeEventListener("resize",e)}}),[]),i}},50948:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return K}});var s=n(97458),a=n(96734),i=n(26766),l=n(62295),r=n(83849),o=n.n(r),c=n(49183),d=n.n(c),u=n(56010),m=n.n(u),f=n(76256),x=n.n(f),h=n(52983),p=n(89062),w=n(80794),g=n(88223),b=n(58202),v=n(37276),j=n(6552),N=n(10637),y=n(34605),C=n(46995),_=n(97716),k=n(208),I=n(4474),E=n(12493),S=n(69806);const P=e=>{let{workspaceId:t}=e;const{loading:n,pendingProcessing:a}=(0,S.k)(t);return!n&&a?(0,s.jsx)(E.Z,{className:"px-3 py-2 bg-[#B0E8FD] text-gray-900",actionIdentifier:"wf-payment-processing-banner-".concat(t),children:(0,s.jsxs)("div",{className:"flex items-center space-x-1",children:[(0,s.jsx)(I.J,{name:"info",className:"w-10 text-blue-500"}),(0,s.jsxs)("div",{className:"text-sm flex",children:[(0,s.jsx)("div",{className:"font-semibold mr-1",children:"Payment is being processed."}),(0,s.jsx)("span",{children:"Premium features will be available in up to 24 hours"})]})]})}):(0,s.jsx)(s.Fragment,{})},L=()=>{const e=(0,a.SS)(l.AD.WORKFLOW_MAINTENANCE_BANNER);if(!e.on)return(0,s.jsx)(s.Fragment,{});const t=e.value,n=new Date(t.from),i=new Date(t.to),r=new Date;if(r<n||r>i)return(0,s.jsx)(s.Fragment,{});const o=()=>(0,s.jsxs)("div",{className:"flex items-center space-x-4",children:[(0,s.jsx)("div",{className:"text-xl",children:t.emoji}),(0,s.jsx)("div",{className:"text-sm",dangerouslySetInnerHTML:{__html:t.message}})]});return t.dismissible?(0,s.jsx)(E.Z,{className:"px-3 py-2 bg-[#B0E8FD] text-gray-900",actionIdentifier:"wf-maintenance-banner",children:(0,s.jsx)(o,{})}):(0,s.jsx)("div",{className:"px-3 py-2 bg-[#B0E8FD] text-gray-900 rounded-lg",children:(0,s.jsx)(o,{})})};var O=n(69429),R=n(18447),A=n(26888),D=n(65516),M=n(25477),F=n(17276),T=n(4884),W=n(54742),U=n(67906),V=n(91787),B=n(65447),q=n(83157);const z="https://creator.lottiefiles.com",Z=d()((async()=>n.e(1156).then(n.bind(n,61156))),{loadableGenerated:{webpack:()=>[61156]},ssr:!1}),G=d()((async()=>n.e(1084).then(n.bind(n,61084))),{loadableGenerated:{webpack:()=>[61084]},ssr:!1}),H=d()((async()=>n.e(4963).then(n.bind(n,94963))),{loadableGenerated:{webpack:()=>[94963]},ssr:!1});function K(){const{activeWorkspace:e,workspaces:t}=(0,W.cF)(),{featuredCuratedAnimations:n}=(0,T.l)(),r=(0,V.QU)();var c;const{hasEditorAccess:d}=(0,F.W)({scopes:null!==(c=null==e?void 0:e.permissionScopes)&&void 0!==c?c:[]}),[u,f]=(0,p.useRecoilState)(C.qx),E=(0,p.useSetRecoilState)(_._b),[,S]=(0,p.useRecoilState)(U.x),[K,J]=(0,h.useState)([]),Y=(0,a.SS)(l.AD.ENABLE_PREMIUM_ASSETS),Q=(0,h.useMemo)((()=>{const e=t.some((e=>-1!==e.features.findIndex((e=>e.slug===l.Hh.USE_PREMIUM_ASSETS&&!0===e.isEnabled))));return Y.on||e}),[Y,t]),[X]=(0,w.aM)({query:y.t});(0,h.useEffect)((()=>{if(X.error);else if(X.data&&X.data.filesRecentlyModified){const e=X.data.filesRecentlyModified;J(e)}X.fetching||X.stale?f(!0):f(!1)}),[X,f]);const $=(0,h.useMemo)((()=>(0,s.jsx)(R.z,{keys:["U"],metaKey:!0})),[]),ee=(0,h.useCallback)((e=>{let{slug:t}=e;return()=>{S({slug:t,source:B.hH.DASHBOARD})}}),[S]),te=(0,h.useCallback)((()=>{(0,i.Z9)(new i.Rd("button","create-animation-cta","dashboard-header")),window.open("".concat(z,"/new?workspace=").concat(null==e?void 0:e.id,"&utm_medium=platform&utm_source=dashboard"),"_blank")}),[e]),ne=(0,h.useCallback)(((e,t)=>{let n;if(((0,k.QR)(e)||(0,k.xK)(e))&&(n=e.fileObject.filename.split(".").pop()),"creator"===n)window.open("".concat(z,"?fileId=").concat(e.id,"&utm_medium=platform&utm_source=file-card"),"_blank");else{const n="/animation/".concat(e.id);t?window.open("".concat(n,"?from=dashboard"),"_blank"):x().push({pathname:n,query:{...x().query,from:"dashboard"}})}}),[]),se=(0,D.X)(),ae=(0,h.useCallback)((e=>{(0,i.Z9)(new i.Rd("button","premium asset dashboard"));const t="/premium-assets";(q.Mq?e.metaKey:e.ctrlKey)?window.open(t,"_blank"):x().push({pathname:t,query:x().query})}),[]);(0,h.useEffect)((()=>{r()}),[se,K,r]);const ie=(0,M.t)({sizeMap:[{width:992,value:4},{width:1200,value:6},{width:1536,value:6},{width:1920,value:8},{width:2150,value:8},{width:1e4,value:10}],defaultValue:10}),le=(0,h.useCallback)((()=>{(0,i.Z9)(new i.Rd("button","dashboard-all-tools")),window.open("https://lottiefiles.com/integrations","_blank")}),[]),re=(0,h.useCallback)((()=>{(0,i.Z9)(new i.Rd("button","upload-animation-cta","dashboard")),E(!0)}),[E]);return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(m(),{children:(0,s.jsx)("title",{children:"LottieFiles Platform"})}),(0,s.jsx)(g.o,{headerWrapperCssClasses:"flex items-center px-6 pt-6 pb-6 flex-shrink-0",contentWrapperCssClasses:o()("flex-grow px-6  pb-9",{"pt-6":0===K.length}),headerControl:(0,s.jsxs)("div",{className:"flex flex-col w-full space-y-6",children:[(0,s.jsx)(L,{}),(0,s.jsx)(P,{workspaceId:null==e?void 0:e.id}),K.length>0&&(0,s.jsx)(v.Z,{variant:"heading-1",gutter:!1,lineHeightClass:"leading-8",darkest:!0,children:"Dashboard"})]}),children:u?(0,s.jsx)(j.a,{}):(0,s.jsxs)(s.Fragment,{children:[K.length>0?(0,s.jsxs)("div",{className:"space-y-[10px]",children:[(0,s.jsxs)("div",{className:"flex items-center justify-between",children:[(0,s.jsx)(v.Z,{variant:"heading-3",darkest:!0,children:"Recently modified"}),d()&&(0,s.jsxs)("div",{className:"flex gap-2",children:[se&&(0,s.jsx)("div",{className:"relative","data-onboarding-id":"dashboard-create-animation",children:(0,s.jsx)(A.u,{title:"Create a new animation with Lottie Creator",placement:"bottom",children:(0,s.jsx)(b.z,{onClick:te,text:"Create animation",additionalClass:"h-8 rounded-lg",variant:"tertiary",padding:"px-4 py-1",fontClasses:"font-lf-bold text-sm",icon:"plus",hideTextOnMobile:!0,iconSize:"small"})})}),(0,s.jsx)("div",{className:"relative","data-onboarding-id":"dashboard-anim-upload",children:(0,s.jsx)(A.u,{title:"",shortcut:$,placement:"bottom",children:(0,s.jsx)(b.z,{onClick:re,text:"Upload animations",icon:"upload",fontClasses:"font-lf-semi-bold",additionalClass:"h-8 rounded-lg",padding:"px-4 py-1",hideTextOnMobile:!0,iconSize:"small"})})})]})]}),(0,s.jsx)("div",{className:"mt-4",children:(0,s.jsx)(N.GridView,{onItemClick:ne,workspaceId:null==e?void 0:e.id,files:K,showUpdatedUser:!1})})]}):(0,s.jsx)(s.Fragment,{children:d()&&(0,s.jsx)(H,{})}),(0,s.jsxs)("div",{className:"space-y-[10px] mt-10",children:[(0,s.jsxs)("div",{className:"flex items-center justify-between",children:[(0,s.jsx)(v.Z,{variant:"heading-4",color:"current",lineHeightClass:"leading-6",darkest:!0,children:"Begin your motion design journey with these tools"}),(0,s.jsxs)("span",{onClick:le,className:"flex items-center text-sm cursor-pointer text-actionPrimary gap-x-2 font-lf-semi-bold hover:text-actionPrimaryHover",children:["All tools ",(0,s.jsx)(I.J,{name:"arrow-right",className:"mt-1",small:!0})]})]}),(0,s.jsx)(Z,{})]}),(0,s.jsxs)("div",{className:"mt-10 space-y-10",children:[Q&&(0,s.jsx)(O.ph,{childClassName:"grid grid-cols-4 lg:grid-cols-6 xl:grid-cols-6 2xl:grid-cols-8 3xl:grid-cols-8 4xl:grid-cols-10",name:"Premium animations",onClickViewAll:ae,children:n.slice(0,ie.value).map((e=>(0,s.jsx)(O.s8,{src:e.thumbnailVideoUrl,onClick:ee({slug:e.slug})},e.id)))}),(0,s.jsx)(G,{})]})]})})]})}},98507:function(e,t,n){"use strict";n.d(t,{Y:function(){return s}});const s=(0,n(89062).atom)({key:"selectedAnimationsCount",default:0})},208:function(e,t,n){"use strict";var s,a,i,l,r,o,c;n.d(t,{GN:function(){return s},QR:function(){return u},eL:function(){return l},hF:function(){return i},nT:function(){return o},qR:function(){return f},ws:function(){return c},xK:function(){return m},yx:function(){return x}}),function(e){e.DOWNLOAD="download",e.FULL_ACCESS="full_access",e.PUBLIC_DOWNLOAD="public_download",e.PUBLIC_VIEW="public_view",e.VIEW="view"}(s||(s={})),function(e){e.Loop="Loop",e.PlayOnce="PlayOnce"}(a||(a={})),function(e){e.DotLottie="lottie",e.Gif="gif",e.LottieJson="json",e.Mp4="mp4"}(i||(i={})),function(e){e.GIF="gif",e.MOV="mov",e.MP4="mp4",e.WEBM="webm"}(l||(l={})),function(e){e.DOWNLOAD="download",e.FULL_ACCESS="full_access",e.PUBLIC_DOWNLOAD="public_download",e.PUBLIC_VIEW="public_view",e.VIEW="view"}(r||(r={})),function(e){e.Approved="Approved",e.InProgress="InProgress",e.NeedsReview="NeedsReview",e.Shipped="Shipped"}(o||(o={})),function(e){e.Completed="Completed",e.Failed="Failed",e.InProgress="InProgress",e.Pending="Pending"}(c||(c={}));const d=e=>e.split(".").pop();function u(e){if(!e.fileObject)return!1;const t=e.fileObject.filename,n=d(t);return void 0!==n&&["lottie","json"].includes(n)}function m(e){if(!e.fileObject)return!1;const t=e.fileObject.filename,n=d(t);return void 0!==n&&"creator"===n}function f(e){return e&&"Folder"===e.__typename}var x;!function(e){e.COLOR_PALETTE="color-palette",e.DIRECT="Direct",e.PLAY_SEGMENTS="play-segments",e.PREMIUM_ANIMTIONS="premium-animations",e.URL="URL"}(x||(x={}))}},function(e){e.O(0,[467,449,7152,637,2888,9774,179],(function(){return t=77838,e(e.s=t);var t}));var t=e.O();_N_E=t}]);