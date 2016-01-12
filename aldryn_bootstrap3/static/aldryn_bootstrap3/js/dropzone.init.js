// #DROPZONE#
// This script implements the dropzone settings
'use strict';

/* globals Dropzone */
(function ($) {
    $(function () {
        var submitNum = 0;
        var maxSubmitNum = 1;
        var dropzoneSelector = '.js-dropzone';
        var dropzones;
        var infoMessageClass = 'js-dropzone-info-message';
        var infoMessage = $('.' + infoMessageClass);
        var uploadInfo = $('.js-dropzone-upload-info');
        var uploadWelcome = $('.js-dropzone-upload-welcome');
        var uploadNumber = $('.js-dropzone-upload-number');
        var uploadFileName = $('.js-dropzone-file-name');
        var uploadProgress = $('.js-dropzone-progress');
        var uploadSuccess = $('.js-dropzone-upload-success');
        var dragHoverClass = 'dz-drag-hover';
        var originalImage = $('.js-original-image');
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
                    maxFiles: 100,
                    previewTemplate: '<div></div>',
                    clickable: false,
                    addRemoveLinks: false,
                    addedfile: function () {
                        submitNum++;

                        if (maxSubmitNum < submitNum) {
                            maxSubmitNum = submitNum;
                        }
                    },
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
                        uploadNumber.text(maxSubmitNum - submitNum + 1 + '/' + maxSubmitNum);
                    },
                    //complete: function () {
                    //    submitNum--;
                    //    uploadInfo.addClass(hiddenClass);
                    //    uploadSuccess.removeClass(hiddenClass);
                    //    console.log('complete');
                    //},
                    success: function (file, response) {
                        console.log('success');
                        maxSubmitNum = 1;

                        uploadInfo.addClass(hiddenClass);
                        uploadSuccess.removeClass(hiddenClass);
                        console.log(response.label);
                        if (file && file.status === 'success' && response) {
                            console.log(originalImage);
                            if (response.thumbnail_180) {
                                originalImage.attr('src', response.thumbnail_180)
                            }
                        }
                    },
                    queuecomplete: function () {
                        infoMessage.addClass(hiddenClass);
                    },
                    error: function (file) {
                        hasErrors = true;
                        window.showError(file.name + ': ' + file.xhr.statusText);
                    }
                });
            });
        }
    });
})(jQuery);
