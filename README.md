#OpenCAS Website

##Deploy&Update
* Fork this repository and add a webhook in `Settings/Webhooks/Add webhook`
* Fill your `Payload URL` with`YourServerAddress:/incoming/site`(you can change subpath in autoDeploy.js)
* Select `application/json` in content type field
* Fill `12345678` in secret field(you can change secret in autoDeploy.js)
* Clone your repository on the serve you want to deploy 

		git clone https://github.com/yourname/site && cd site
		npm install
		npm start
* Set your server(e.g. nginx) path to `site\public`
* clone your repository on your local device, edit contents of the sit, each time you commit your changes, your site will update and generate on your server automatically.
* if you change the content of `autoDeploy.js`, you need run `	npm restart` on server