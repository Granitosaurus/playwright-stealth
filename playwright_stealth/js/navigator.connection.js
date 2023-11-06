Object.defineProperty(Object.getPrototypeOf(navigator.connection), 'rtt', {
    get: () => opts.navigator_connection_rtt || '356',
})