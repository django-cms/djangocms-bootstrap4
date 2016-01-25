// #DROPZONE#
// This script implements the dropzone settings
'use strict';

/* globals Dropzone */
(function ($) {
    $(function () {
        var dropzoneSelector = '.js-filer-dropzone';
        var dropzones;
        var infoMessageClass = 'js-filer-dropzone-info-message';
        var infoMessage = '.' + infoMessageClass;
        var uploadInfo = '.js-filer-dropzone-upload-info';
        var uploadWelcome = '.js-filer-dropzone-upload-welcome';
        var uploadFileName = '.js-filer-dropzone-file-name';
        var uploadProgress = '.js-filer-dropzone-progress';
        var uploadSuccess = '.js-filer-dropzone-upload-success';
        var uploadAccept = '.js-filer-dropzone-upload-accept';
        var dragHoverClass = 'dz-drag-hover';
        var originalImage = '.js-original-image img';
        var hiddenClass = 'hidden';
        var hideMessageTimeout;

        dropzones = $(dropzoneSelector);
        if (dropzones.length && Dropzone) {
            Dropzone.autoDiscover = false;
            dropzones.each(function () {
                var dropzone = $(this);
                var dropzoneUrl = $(this).data('url');
                new Dropzone(this, {
                    url: dropzoneUrl,
                    paramName: 'file',
                    uploadMultiple: false,
                    previewTemplate: '<div></div>',
                    clickable: false,
                    addRemoveLinks: false,
                    //acceptedFiles: 'image/*',
                    accept: function (file, done) {
                        console.log(file.type);
                        if (!file.type.match('image.*')) {
                            console.log('no image');
                            console.log(dropzone.find(infoMessage).removeClass(hiddenClass));
                            dropzone.find(infoMessage).removeClass(hiddenClass);
                            dropzone.find(uploadAccept).removeClass(hiddenClass);
                            dropzone.find(uploadWelcome).addClass(hiddenClass);
                            done('Error');
                        }
                    },
                    maxfilesexceeded: function (file) {
                        this.removeAllFiles();
                        this.addFile(file);
                    },
                    dragover: function () {
                        dropzone.find(uploadSuccess).addClass(hiddenClass);
                        dropzone.find(infoMessage).removeClass(hiddenClass);
                        dropzone.addClass(dragHoverClass);
                    },
                    dragleave: function () {
                        clearTimeout(hideMessageTimeout);
                        hideMessageTimeout = setTimeout(function () {
                            dropzone.find(infoMessage).addClass(hiddenClass);
                        }, 100);

                        dropzone.find(infoMessage).removeClass(hiddenClass);
                        dropzone.removeClass(dragHoverClass);
                    },
                    drop: function () {
                        clearTimeout(hideMessageTimeout);
                        dropzone.find(infoMessage).removeClass(hiddenClass);
                        dropzone.removeClass(dragHoverClass);
                    },
                    sending: function (file) {
                        dropzone.find(uploadWelcome).addClass(hiddenClass);
                        dropzone.find(uploadFileName).text(file.name);
                        dropzone.find(uploadProgress).width(0);
                        dropzone.find(uploadInfo).removeClass(hiddenClass);
                    },
                    uploadprogress: function (file, progress) {
                        dropzone.find(uploadProgress).width(progress + '%');
                    },
                    success: function (file, response) {
                        dropzone.find(uploadInfo).addClass(hiddenClass);
                        dropzone.find(uploadSuccess).removeClass(hiddenClass);
                        if (file && file.status === 'success' && response) {
                            if (response.original_image) {
                                console.log(dropzone.find(originalImage));
                                dropzone.find(originalImage).attr('src', response.original_image)
                            }
                        }
                    },
                    queuecomplete: function () {
                        dropzone.find(infoMessage).addClass(hiddenClass);
                        dropzone.find(uploadSuccess).addClass(hiddenClass);
                        dropzone.find(uploadWelcome).removeClass(hiddenClass);
                    }
                });
            });
        }
    });
})(jQuery);
