const imagemin = require('imagemin');
const imageminJpegtran = require('imagemin-jpegtran');
const imageminPngquant = require('imagemin-pngquant');
const imageminGifsicle = require('imagemin-gifsicle');

(async () => {
	const files = await imagemin(['src/**/*.{jpeg}', 'imgs/**/*.{jpeg}'], {
		destination: 'jpeg',
		plugins: [
			imageminJpegtran({
        progressive: true,
      }),
			imageminPngquant({
				quality: [0.4, 0.6],
      }),
      imageminGifsicle({
        optimizationLevel: 3,
      }),
		]
	});
  console.log(files);
})();
