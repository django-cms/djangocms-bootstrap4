// #DROPZONE#
// This script implements the dropzone settings
'use strict';

/* globals Dropzone */
(function ($) {
    $(function () {
        var dropzoneSelector = '.js-dropzone';
        var dropzones;
        var infoMessageClass = 'js-dropzone-info-message';
        var infoMessage = $('.' + infoMessageClass);
        var uploadInfo = $('.js-dropzone-upload-info');
        var uploadWelcome = $('.js-dropzone-upload-welcome');
        var uploadFileName = $('.js-dropzone-file-name');
        var uploadProgress = $('.js-dropzone-progress');
        var uploadSuccess = $('.js-dropzone-upload-success');
        var uploadAccept = $('.js-dropzone-upload-accept');
        var dragHoverClass = 'dz-drag-hover';
        var originalImage = $('.js-original-image').find('img');
        var hiddenClass = 'hidden';
        var hideMessageTimeout;
        var hasErrors = false;

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
                    acceptedFiles: 'image/*',
                    maxfilesexceeded: function (file) {
                        this.removeAllFiles();
                        this.addFile(file);
                    },
                    dragover: function () {

                        uploadSuccess.addClass(hiddenClass);
                        infoMessage.removeClass(hiddenClass);
                        dropzone.addClass(dragHoverClass);
                    },
                    dragleave: function () {
                        clearTimeout(hideMessageTimeout);
                        hideMessageTimeout = setTimeout(function () {
                            infoMessage.addClass(hiddenClass);
                        }, 1000);

                        infoMessage.removeClass(hiddenClass);
                        dropzones.removeClass(dragHoverClass);
                    },
                    drop: function () {
                        clearTimeout(hideMessageTimeout);
                        infoMessage.removeClass(hiddenClass);
                        dropzones.removeClass(dragHoverClass);
                    },
                    sending: function (file) {
                        uploadWelcome.addClass(hiddenClass);
                        uploadFileName.text(file.name);
                        uploadProgress.width(0);
                        uploadInfo.removeClass(hiddenClass);
                    },
                    uploadprogress: function (file, progress) {
                        uploadProgress.width(progress + '%');
                    },
                    success: function (file, response) {
                        uploadInfo.addClass(hiddenClass);
                        uploadSuccess.removeClass(hiddenClass);
                        if (file && file.status === 'success' && response) {
                            if (response.original_image) {
                                originalImage.attr('src', response.original_image)
                            }
                        }
                    },
                    queuecomplete: function () {
                        infoMessage.addClass(hiddenClass);
                        uploadSuccess.addClass(hiddenClass);
                        uploadWelcome.removeClass(hiddenClass);
                    },
                    accept: function (file, done) {
                        hasErrors = true;
                        if (file.type != 'image/*') {
                            console.log(file.type);
                            infoMessage.removeClass(hiddenClass);
                            uploadAccept.removeClass(hiddenClass);
                            uploadWelcome.addClass(hiddenClass);
                        }
                        else { done(); }
                    }
                });
            });
        }
    });
})(jQuery);
