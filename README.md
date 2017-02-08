# OpenCAS Site Deployer

Generate the website with Hexo and npm.

## Deploy & Update

* Add a webhook in `Settings/Webhooks/Add webhook`
* Fill your `Payload URL` with`YourServerAddress:/webhook`(you can change subpath in autoDeploy.js)
* Select `application/json` in content type field
* Rename the `autoDeploy.js.example` to `autoDeploy.js`
* Fill `secret_key` in secret field(you can change secret in autoDeploy.js)
* Clone your repository on the serve you want to deploy 

		git clone https://github.com/opencas/siteDeployer && cd siteDeployer
		npm install
		npm start
* Set your server(e.g. nginx) path to `site\public`
* Clone your repository on your local device, edit contents of the site, each time you commit your changes, your site will update and generate on your server automatically.
* If you change the content of `autoDeploy.js`, you need run `npm restart` on server