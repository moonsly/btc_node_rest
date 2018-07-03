// BTC show wallets component
Vue.component('show-wallets', {
    props: ['item'],
    template: `<tr>
        <td><% item.wallet %> </td>
        <td><% item.created %></td>
    </tr>`,
    delimiters: ['<%', '%>']
})

var show_wallets = new Vue({
    el: '#show_wallets',
    data: {
        wallets: [{"wallet": "loading...", "created": ""}]
    },
    delimiters: ['<%', '%>'],
    methods: {
        fetchWallets: function() {
            axios.get('/api/wallets/')
            .then(response => {
                wallets = response.data
                settings = show_wallets.$data.wallets
                settings.pop()
                settings.push.apply(settings, wallets);
            });
        }
    },
    created: function() {
        this.fetchWallets();
    }
})

// Create wallet component + push new wallet to Wallets list
let ajaxCreateWallet = {
    methods: {
        createWallet(resource) {
            axios('/api/wallets/', {
                method: 'post',
                data: { 
                    method: "create_wallet",
                    csrfmiddlewaretoken: document.forms[0].children[0].value,
                },
                headers: {'X-CSRFToken': document.forms[0].children[0].value},
                withCredentials: true
            }).then(response => {
                wallet = response.data
                create_wallet.$data.item = wallet
                show_wallets.$data.wallets.push({"wallet": wallet["wallet_created"], "created": "just now"})
            });
        }
    },
}
Vue.component('create-wallet', {
    template: '<span><button v-on:click="createWallet">Create</button> <% item.wallet_created %></span>',
    delimiters: ['<%', '%>'],
    mixins: [ajaxCreateWallet],
    props: ['item']
})
var create_wallet = new Vue({
    el: '#create_wallet',
    delimiters: ['<%', '%>'],
    data: function() {
        return { "item": {"wallet_created": ""} }
    }
})

// Balance component
let ajaxBalance = {
    methods: {
        getBalance(resource) {
            axios.get('/api/accounts/balance/')
            .then(response => {
                balance = response.data
                get_balance.$data.item = balance
            });
        }
    },
}
Vue.component('get-balance', {
    template: '<span><button v-on:click="getBalance">Refresh</button> <% item.balance %></span>',
    delimiters: ['<%', '%>'],
    mixins: [ajaxBalance],
    props: ['item']
})
var get_balance = new Vue({
    el: '#get_balance',
    delimiters: ['<%', '%>'],
    data: function() {
        return { "item": {"balance": "unknown"} }
    }
})

// BTC node settings component
Vue.component('show-settings', {
    props: ['item'],
    template: `<tr>
        <td style="text-align: right;"><b><% item.key %></b>: </td>
        <td><% item.value %></td>
    </tr>`,
    delimiters: ['<%', '%>']
})

var creds = new Vue({
    el: '#show_settings',
    data: {
        connectSettings: [{"key": "loading...", "value": ""}]
    },
    delimiters: ['<%', '%>'],
    methods: {
        fetchSettings: function() {
            axios.get('/api/accounts/params/')
            .then(response => {
                resp_settings = response.data.settings
                settings = creds.$data.connectSettings
                settings.pop()
                settings.push.apply(settings, resp_settings);
            });
        }
    },
    created: function(){
        this.fetchSettings();
    }
})