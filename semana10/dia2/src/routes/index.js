const {Router} = require('express');
const router = Router();

router.get('/',(req,res)=>{
    res.json({
        mensaje:'api rest con docker'
    })
})

module.exports = router;