# MmBuildMdlForNonPagedPool

- RVA: `0x0023A870`–`0x0023AD9C` (길이 `1,324` bytes)
- VA: `0x000000014023A870`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060D2C`
- 디코드: `302`개 명령, `1,324/1,324` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0023AA80` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0023AD23` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0023AD92` → [MiQueuePinDriverAddressLog](MiQueuePinDriverAddressLog_function_0023ADA4.md) (function, `0x0023ADA4`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressCtxCompleteEntry](../26/SMKM_STORE_MGR_SM_TRAITS_SmCompressCtxCompleteEntry_function_002685C0.md) at `0x00268757`
- [VslpLockPagesForTransfer](../29/VslpLockPagesForTransfer_function_0029E0FC.md) at `0x0029E2FB`
- [VslpLockMdlForTransfer](../29/VslpLockMdlForTransfer_function_0029E3FC.md) at `0x0029E489`
- [HalpFlushMapBuffers](../55/HalpFlushMapBuffers_function_00551358.md) at `0x005514C3`
- [HalpFlushMapBuffers](../55/HalpFlushMapBuffers_function_00551358.md) at `0x005515C6`
- [IoWriteCapturedPristineTriageDumpToDedicatedDumpFile](../59/IoWriteCapturedPristineTriageDumpToDedicatedDumpFile_function_005934C0.md) at `0x005935D7`
- [SmKmIssueVolumeIo](../60/SmKmIssueVolumeIo_function_0060F9BC.md) at `0x0060FA68`
- [DifMmBuildMdlForNonPagedPoolWrapper](../63/DifMmBuildMdlForNonPagedPoolWrapper_function_00634BD0.md) at `0x00634C96`
- [HvlpDynamicUpdateMicrocode](../../page/71/HvlpDynamicUpdateMicrocode_function_007185E8.md) at `0x00718634`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9E5D`
- [EtwpBuildMdlForTraceBuffer](../../page/7B/EtwpBuildMdlForTraceBuffer_function_007BEB50.md) at `0x007BEBAC`
- [MiCreateMdl](../../page/98/MiCreateMdl_function_009883A8.md) at `0x009884D2`
- [MiReplaceRotateWithDemandZero](../../page/A7/MiReplaceRotateWithDemandZero_function_00A7C010.md) at `0x00A7C145`
- [PopAllocateHiberContext](../../page/AD/PopAllocateHiberContext_function_00ADC05C.md) at `0x00ADC251`
- [PopAllocateHiberContext](../../page/AD/PopAllocateHiberContext_function_00ADC05C.md) at `0x00ADC2B1`

### Static image references
- `0x0023AA12` → RVA `0x00E38AA8` (`.data`; read)
- `0x0023AAAA` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0023A870  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0023A875  53                              push rbx
0023A876  55                              push rbp
0023A877  56                              push rsi
0023A878  57                              push rdi
0023A879  41 55                           push r13
0023A87B  41 56                           push r14
0023A87D  48 81 EC 88 00 00 00            sub rsp, 0x88
0023A884  48 8B 71 20                     mov rsi, qword ptr [rcx + 0x20]
0023A888  4C 8D 41 30                     lea r8, [rcx + 0x30]
0023A88C  8B 51 2C                        mov edx, dword ptr [rcx + 0x2c]
0023A88F  49 BD F8 FF FF FF 7F 00 00 00   movabs r13, 0x7ffffffff8
0023A899  48 03 D6                        add rdx, rsi
0023A89C  4C 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r8
0023A8A4  48 C1 EE 09                     shr rsi, 9
0023A8A8  4C 8B F1                        mov r14, rcx
0023A8AB  49 23 F5                        and rsi, r13
0023A8AE  48 C7 41 10 00 00 00 00         mov qword ptr [rcx + 0x10], 0
0023A8B6  48 89 51 18                     mov qword ptr [rcx + 0x18], rdx
0023A8BA  48 C7 C7 FF FF FF FF            mov rdi, 0xffffffffffffffff
0023A8C1  33 DB                           xor ebx, ebx
0023A8C3  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0023A8CD  33 ED                           xor ebp, ebp
0023A8CF  49 8B C1                        mov rax, r9
0023A8D2  8B 49 28                        mov ecx, dword ptr [rcx + 0x28]
0023A8D5  81 E2 FF 0F 00 00               and edx, 0xfff
0023A8DB  48 81 C1 FF 0F 00 00            add rcx, 0xfff
0023A8E2  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
0023A8EA  48 03 CA                        add rcx, rdx
0023A8ED  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
0023A8F2  48 C1 E9 0C                     shr rcx, 0xc
0023A8F6  48 03 F0                        add rsi, rax
0023A8F9  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
0023A903  48 8D 04 CE                     lea rax, [rsi + rcx*8]
0023A907  33 C9                           xor ecx, ecx
0023A909  89 8C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ecx
0023A910  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0023A918  48 BA F8 D7 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed7f8
0023A922  48 3B F0                        cmp rsi, rax
0023A925  0F 83 5B 01 00 00               jae 0x14023aa86
0023A92B  85 ED                           test ebp, ebp
0023A92D  0F 85 B6 03 00 00               jne 0x14023ace9
0023A933  4C 8B DE                        mov r11, rsi
0023A936  49 C1 E3 19                     shl r11, 0x19
0023A93A  49 8B C1                        mov rax, r9
0023A93D  48 C1 E0 19                     shl rax, 0x19
0023A941  BF 04 00 00 00                  mov edi, 4
0023A946  4C 2B D8                        sub r11, rax
0023A949  44 8B D7                        mov r10d, edi
0023A94C  49 C1 FB 10                     sar r11, 0x10
0023A950  49 8B EB                        mov rbp, r11
0023A953  48 C1 ED 09                     shr rbp, 9
0023A957  49 23 ED                        and rbp, r13
0023A95A  49 8B C1                        mov rax, r9
0023A95D  48 03 E8                        add rbp, rax
0023A960  4C 8B FD                        mov r15, rbp
0023A963  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
0023A968  49 C1 EF 09                     shr r15, 9
0023A96C  4D 23 FD                        and r15, r13
0023A96F  49 8B C1                        mov rax, r9
0023A972  4C 03 F8                        add r15, rax
0023A975  4D 8B E7                        mov r12, r15
0023A978  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
0023A97D  49 C1 EC 09                     shr r12, 9
0023A981  4D 23 E5                        and r12, r13
0023A984  49 8B C1                        mov rax, r9
0023A987  4C 03 E0                        add r12, rax
0023A98A  49 8B CC                        mov rcx, r12
0023A98D  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0023A992  48 C1 E9 09                     shr rcx, 9
0023A996  4C 23 E9                        and r13, rcx
0023A999  49 8B C1                        mov rax, r9
0023A99C  4C 03 E8                        add r13, rax
0023A99F  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
0023A9A4  4E 8B 4C D4 28                  mov r9, qword ptr [rsp + r10*8 + 0x28]
0023A9A9  49 FF CA                        dec r10
0023A9AC  FF CF                           dec edi
0023A9AE  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
0023A9B8  49 8B 01                        mov rax, qword ptr [r9]
0023A9BB  48 8B C9                        mov rcx, rcx
0023A9BE  4C 3B C9                        cmp r9, rcx
0023A9C1  72 2D                           jb 0x14023a9f0
0023A9C3  48 8B CA                        mov rcx, rdx
0023A9C6  4C 3B C9                        cmp r9, rcx
0023A9C9  77 25                           ja 0x14023a9f0
0023A9CB  48 8B C8                        mov rcx, rax
0023A9CE  A8 01                           test al, 1
0023A9D0  74 26                           je 0x14023a9f8
0023A9D2  A8 42                           test al, 0x42
0023A9D4  41 0F 95 C0                     setne r8b
0023A9D8  A8 20                           test al, 0x20
0023A9DA  0F 95 C2                        setne dl
0023A9DD  44 84 C2                        test dl, r8b
0023A9E0  0F 84 C4 00 00 00               je 0x14023aaaa
0023A9E6  48 BA F8 D7 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed7f8
0023A9F0  A8 01                           test al, 1
0023A9F2  0F 85 1C 01 00 00               jne 0x14023ab14
0023A9F8  48 8B 1E                        mov rbx, qword ptr [rsi]
0023A9FB  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0023AA05  4C 3B D8                        cmp r11, rax
0023AA08  0F 82 19 01 00 00               jb 0x14023ab27
0023AA0E  49 C1 EB 27                     shr r11, 0x27
0023AA12  48 8D 0D 8F E0 BF 00            lea rcx, [rip + 0xbfe08f]
0023AA19  41 81 E3 FF 01 00 00            and r11d, 0x1ff
0023AA20  41 81 EB 00 01 00 00            sub r11d, 0x100
0023AA27  41 0F B6 0C 0B                  movzx ecx, byte ptr [r11 + rcx]
0023AA2C  89 8C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ecx
0023AA33  83 F9 04                        cmp ecx, 4
0023AA36  0F 85 F4 00 00 00               jne 0x14023ab30
0023AA3C  8D 69 FF                        lea ebp, [rcx - 1]
0023AA3F  89 8C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ecx
0023AA46  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
0023AA4E  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
0023AA58  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0023AA62  F6 C3 01                        test bl, 1
0023AA65  0F 85 8C 02 00 00               jne 0x14023acf7
0023AA6B  4C 8B CE                        mov r9, rsi
0023AA6E  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0023AA73  4D 8B C6                        mov r8, r14
0023AA76  BA 40 12 00 00                  mov edx, 0x1240
0023AA7B  B9 1A 00 00 00                  mov ecx, 0x1a
0023AA80  E8 DB 2B 2C 00                  call 0x1404fd660
0023AA85  CC                              int3
0023AA86  66 41 83 4E 0A 04               or word ptr [r14 + 0xa], 4
0023AA8C  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0023AA91  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
0023AA99  48 81 C4 88 00 00 00            add rsp, 0x88
0023AAA0  41 5E                           pop r14
0023AAA2  41 5D                           pop r13
0023AAA4  5F                              pop rdi
0023AAA5  5E                              pop rsi
0023AAA6  5D                              pop rbp
0023AAA7  5B                              pop rbx
0023AAA8  C3                              ret
0023AAA9  CC                              int3
0023AAAA  48 F7 05 D3 BF D8 00 00 00 60 00  test qword ptr [rip + 0xd8bfd3], 0x600000
0023AAB5  0F 84 2B FF FF FF               je 0x14023a9e6
0023AABB  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
0023AAC4  4C 8B 82 B8 00 00 00            mov r8, qword ptr [rdx + 0xb8]
0023AACB  41 80 B8 60 01 00 00 01         cmp byte ptr [r8 + 0x160], 1
0023AAD3  0F 84 0D FF FF FF               je 0x14023a9e6
0023AAD9  49 8B 90 08 05 00 00            mov rdx, qword ptr [r8 + 0x508]
0023AAE0  48 85 D2                        test rdx, rdx
0023AAE3  0F 84 FD FE FF FF               je 0x14023a9e6
0023AAE9  49 C1 E9 03                     shr r9, 3
0023AAED  41 81 E1 FF 01 00 00            and r9d, 0x1ff
0023AAF4  4A 8B 14 CA                     mov rdx, qword ptr [rdx + r9*8]
0023AAF8  F6 C2 20                        test dl, 0x20
0023AAFB  74 04                           je 0x14023ab01
0023AAFD  48 83 C9 20                     or rcx, 0x20
0023AB01  48 8B C1                        mov rax, rcx
0023AB04  48 83 C8 42                     or rax, 0x42
0023AB08  F6 C2 42                        test dl, 0x42
0023AB0B  48 0F 44 C1                     cmove rax, rcx
0023AB0F  E9 D2 FE FF FF                  jmp 0x14023a9e6
0023AB14  84 C0                           test al, al
0023AB16  78 22                           js 0x14023ab3a
0023AB18  49 83 FA 01                     cmp r10, 1
0023AB1C  0F 84 D6 FE FF FF               je 0x14023a9f8
0023AB22  E9 7D FE FF FF                  jmp 0x14023a9a4
0023AB27  33 C9                           xor ecx, ecx
0023AB29  89 8C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ecx
0023AB30  BD 02 00 00 00                  mov ebp, 2
0023AB35  E9 0C FF FF FF                  jmp 0x14023aa46
0023AB3A  85 FF                           test edi, edi
0023AB3C  0F 84 B6 FE FF FF               je 0x14023a9f8
0023AB42  41 BA 04 00 00 00               mov r10d, 4
0023AB48  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
0023AB4D  45 8B C2                        mov r8d, r10d
0023AB50  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0023AB55  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
0023AB5A  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
0023AB5F  49 BE 00 D0 BE 7D FB F6 FF FF   movabs r14, 0xfffff6fb7dbed000
0023AB69  4E 8B 4C C4 48                  mov r9, qword ptr [rsp + r8*8 + 0x48]
0023AB6E  49 FF C8                        dec r8
0023AB71  41 FF CA                        dec r10d
0023AB74  49 8B 39                        mov rdi, qword ptr [r9]
0023AB77  49 8B C6                        mov rax, r14
0023AB7A  4C 3B C8                        cmp r9, rax
0023AB7D  72 31                           jb 0x14023abb0
0023AB7F  48 8B C2                        mov rax, rdx
0023AB82  4C 3B C8                        cmp r9, rax
0023AB85  77 29                           ja 0x14023abb0
0023AB87  48 8B C7                        mov rax, rdi
0023AB8A  40 F6 C7 01                     test dil, 1
0023AB8E  74 20                           je 0x14023abb0
0023AB90  40 F6 C7 42                     test dil, 0x42
0023AB94  0F 95 C2                        setne dl
0023AB97  40 F6 C7 20                     test dil, 0x20
0023AB9B  0F 95 C1                        setne cl
0023AB9E  84 D1                           test cl, dl
0023ABA0  0F 84 D3 00 00 00               je 0x14023ac79
0023ABA6  48 BA F8 D7 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed7f8
0023ABB0  4D 85 C0                        test r8, r8
0023ABB3  74 0A                           je 0x14023abbf
0023ABB5  40 84 FF                        test dil, dil
0023ABB8  78 05                           js 0x14023abbf
0023ABBA  4D 85 C0                        test r8, r8
0023ABBD  75 AA                           jne 0x14023ab69
0023ABBF  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
0023ABC7  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0023ABD1  48 C1 EF 0C                     shr rdi, 0xc
0023ABD5  48 23 F8                        and rdi, rax
0023ABD8  4D 85 C0                        test r8, r8
0023ABDB  74 2B                           je 0x14023ac08
0023ABDD  49 C1 EB 0C                     shr r11, 0xc
0023ABE1  B9 01 00 00 00                  mov ecx, 1
0023ABE6  45 85 D2                        test r10d, r10d
0023ABE9  74 1D                           je 0x14023ac08
0023ABEB  49 8B C3                        mov rax, r11
0023ABEE  49 C1 EB 09                     shr r11, 9
0023ABF2  25 FF 01 00 00                  and eax, 0x1ff
0023ABF7  48 0F AF C1                     imul rax, rcx
0023ABFB  48 C1 E1 09                     shl rcx, 9
0023ABFF  48 03 F8                        add rdi, rax
0023AC02  41 83 EA 01                     sub r10d, 1
0023AC06  75 E3                           jne 0x14023abeb
0023AC08  BD 01 00 00 00                  mov ebp, 1
0023AC0D  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
0023AC14  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
0023AC1E  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
0023AC26  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0023AC2E  49 89 38                        mov qword ptr [r8], rdi
0023AC31  48 83 C6 08                     add rsi, 8
0023AC35  49 83 C0 08                     add r8, 8
0023AC39  48 BA F8 D7 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed7f8
0023AC43  4C 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r8
0023AC4B  49 BD F8 FF FF FF 7F 00 00 00   movabs r13, 0x7ffffffff8
0023AC55  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0023AC5F  48 F7 C6 FF 0F 00 00            test rsi, 0xfff
0023AC66  74 7A                           je 0x14023ace2
0023AC68  83 FD 01                        cmp ebp, 1
0023AC6B  0F 85 B1 FC FF FF               jne 0x14023a922
0023AC71  48 FF C7                        inc rdi
0023AC74  E9 9F FC FF FF                  jmp 0x14023a918
0023AC79  48 F7 05 04 BE D8 00 00 00 60 00  test qword ptr [rip + 0xd8be04], 0x600000
0023AC84  0F 84 1C FF FF FF               je 0x14023aba6
0023AC8A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0023AC93  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0023AC9A  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
0023ACA1  0F 84 FF FE FF FF               je 0x14023aba6
0023ACA7  48 8B 8A 08 05 00 00            mov rcx, qword ptr [rdx + 0x508]
0023ACAE  48 85 C9                        test rcx, rcx
0023ACB1  0F 84 EF FE FF FF               je 0x14023aba6
0023ACB7  49 C1 E9 03                     shr r9, 3
0023ACBB  41 81 E1 FF 01 00 00            and r9d, 0x1ff
0023ACC2  4A 8B 0C C9                     mov rcx, qword ptr [rcx + r9*8]
0023ACC6  F6 C1 20                        test cl, 0x20
0023ACC9  74 04                           je 0x14023accf
0023ACCB  48 83 C8 20                     or rax, 0x20
0023ACCF  48 8B F8                        mov rdi, rax
0023ACD2  48 83 CF 42                     or rdi, 0x42
0023ACD6  F6 C1 42                        test cl, 0x42
0023ACD9  48 0F 44 F8                     cmove rdi, rax
0023ACDD  E9 C4 FE FF FF                  jmp 0x14023aba6
0023ACE2  33 ED                           xor ebp, ebp
0023ACE4  E9 39 FC FF FF                  jmp 0x14023a922
0023ACE9  83 FD 02                        cmp ebp, 2
0023ACEC  0F 8D 70 FD FF FF               jge 0x14023aa62
0023ACF2  E9 37 FF FF FF                  jmp 0x14023ac2e
0023ACF7  83 FD 03                        cmp ebp, 3
0023ACFA  75 0A                           jne 0x14023ad06
0023ACFC  48 8B 06                        mov rax, qword ptr [rsi]
0023ACFF  48 0F BA E0 09                  bt rax, 9
0023AD04  73 2A                           jae 0x14023ad30
0023AD06  48 8B 1E                        mov rbx, qword ptr [rsi]
0023AD09  F6 C3 01                        test bl, 1
0023AD0C  75 53                           jne 0x14023ad61
0023AD0E  4C 8B CE                        mov r9, rsi
0023AD11  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0023AD16  4D 8B C6                        mov r8, r14
0023AD19  BA 40 12 00 00                  mov edx, 0x1240
0023AD1E  B9 1A 00 00 00                  mov ecx, 0x1a
0023AD23  E8 38 29 2C 00                  call 0x1404fd660
0023AD28  CC                              int3
0023AD29  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0023AD30  48 8B C8                        mov rcx, rax
0023AD33  48 81 C9 20 02 00 00            or rcx, 0x220
0023AD3A  48 F7 05 43 BD D8 00 00 00 00 02  test qword ptr [rip + 0xd8bd43], 0x2000000
0023AD45  74 03                           je 0x14023ad4a
0023AD47  0F AE E8                        lfence
0023AD4A  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
0023AD4F  74 07                           je 0x14023ad58
0023AD51  48 0F BA E0 09                  bt rax, 9
0023AD56  73 D8                           jae 0x14023ad30
0023AD58  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
0023AD5F  EB A5                           jmp 0x14023ad06
0023AD61  48 8B FB                        mov rdi, rbx
0023AD64  48 C1 EF 0C                     shr rdi, 0xc
0023AD68  49 23 FA                        and rdi, r10
0023AD6B  83 F9 0B                        cmp ecx, 0xb
0023AD6E  0F 85 B2 FE FF FF               jne 0x14023ac26
0023AD74  48 8B CE                        mov rcx, rsi
0023AD77  48 C1 E1 19                     shl rcx, 0x19
0023AD7B  49 8B C1                        mov rax, r9
0023AD7E  48 C1 E0 19                     shl rax, 0x19
0023AD82  41 B8 01 00 00 00               mov r8d, 1
0023AD88  48 2B C8                        sub rcx, rax
0023AD8B  48 8B D3                        mov rdx, rbx
0023AD8E  48 C1 F9 10                     sar rcx, 0x10
0023AD92  E8 0D 00 00 00                  call 0x14023ada4
0023AD97  E9 71 FE FF FF                  jmp 0x14023ac0d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmBuildMdlForNonPagedPool(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned int v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (136);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 44))) + (*(unsigned __int64 *)(a1 + 32));
    v_stack_p18 = a1 + 48;
    v_rsi = (*(unsigned __int64 *)(a1 + 32)) >> (9);
    v_rsi = (v_rsi) & (v_r13);
    *(unsigned __int64 *)(a1 + 16) = 0;
    *(unsigned __int64 *)(a1 + 24) = a2;
    v_rbx = 0;
    v_rbp = 0;
    a2 = (unsigned int)((a2) & (0xFFFULL));
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 40))) + (0xFFFULL);
    v_stack_m38 = v_r12;
    a1 = (a1) + (a2);
    v_stack_m40 = v_r15;
    a1 = (a1) >> (12);
    v_rsi = (v_rsi) + (a4);
    a1 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = v_rsi + a1 * 8;
loc_0023A918:
loc_0023A922:
    if (v_rsi >= (v_rsi + a1 * 8)) goto loc_0023AA86;
    if (0 != 0) goto loc_0023ACE9;
    v_r11 = (v_rsi) << (25);
    result = (a4) << (25);
    v_r11 = (v_r11) - (result);
    v_r11 = (v_r11) >> (16);
    v_rbp = (v_r11) >> (9);
    v_rbp = (v_rbp) & (v_r13);
    v_rbp = (v_rbp) + (a4);
    v_stack_m88 = v_rbp;
    v_r15 = (v_rbp) >> (9);
    v_r15 = (v_r15) & (v_r13);
    v_r15 = (v_r15) + (a4);
    v_stack_m80 = v_r15;
    v_r12 = (v_r15) >> (9);
    v_r12 = (v_r12) & (v_r13);
    v_r12 = (v_r12) + (a4);
    v_stack_m78 = v_r12;
    a1 = (v_r12) >> (9);
    v_r13 = (v_r13) & (a1);
    v_r13 = (v_r13) + (a4);
    v_stack_m70 = v_r13;
loc_0023A9A4:
    v_r10 = (4) - 1;
    v_rdi = (unsigned int)((4) - 1);
    if ((*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)) < a1) goto loc_0023A9F0;
    if ((*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)) > a2) goto loc_0023A9F0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (1)) == 0) goto loc_0023A9F8;
    a3 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (66)) != 0) ? 1 : 0;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a2)) & ((unsigned __int8)(a3))) == 0) goto loc_0023AAAA;
loc_0023A9E6:
loc_0023A9F0:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (1)) != 0) goto loc_0023AB14;
loc_0023A9F8:
    if (v_r11 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) goto loc_0023AB27;
    v_r11 = (v_r11) >> (39);
    v_r11 = (unsigned int)((v_r11) & (511));
    v_r11 = (unsigned int)((v_r11) - (256));
    v_stack_p10 = (unsigned int)(*(unsigned __int8 *)(v_r11 + v_rip + 12574863 * 1));
    if (((unsigned int)(*(unsigned __int8 *)(v_r11 + v_rip + 12574863 * 1))) != 4) goto loc_0023AB30;
    v_stack_p10 = (unsigned int)(*(unsigned __int8 *)(v_r11 + v_rip + 12574863 * 1));
loc_0023AA46:
loc_0023AA62:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsi))) & (1)) != 0) goto loc_0023ACF7;
    v_stack_m98 = *(unsigned __int64 *)(v_rsi);
    result = KeBugCheckEx(26, (unsigned int)(0x1240ULL), a1, v_rsi);
loc_0023AA86:
    v_rsp = (v_rsp) + (136);
    return result;
loc_0023AAAA:
    if (((*(unsigned __int64 *)(v_rip + 14204883)) & (0x600000ULL)) == 0) goto loc_0023A9E6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0023A9E6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0023A9E6;
    a4 = (v_rsi) >> (3);
    a4 = (unsigned int)((a4) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (32)) != 0) {
        a1 = (26) | (32);
    }
    result = (a1) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (66)) == 0) { result = a1; }
    goto loc_0023A9E6;
loc_0023AB14:
    if (sign_flag) goto loc_0023AB3A;
    if (v_r10 == 1) goto loc_0023A9F8;
    goto loc_0023A9A4;
loc_0023AB27:
    a1 = 0;
    v_stack_pC8 = 0;
loc_0023AB30:
    goto loc_0023AA46;
loc_0023AB3A:
    if ((unsigned int)(v_rdi) == 0) goto loc_0023A9F8;
    v_stack_p50 = 2;
    v_stack_p58 = v_stack_m40;
    v_stack_p60 = v_stack_m38;
    v_stack_p68 = v_r13;
loc_0023AB69:
    a3 = (4) - 1;
    v_r10 = (unsigned int)((4) - 1);
    if ((*(unsigned __int64 *)(v_rsp + 4 * 8 + 72)) < 0) goto loc_0023ABB0;
    if ((*(unsigned __int64 *)(v_rsp + 4 * 8 + 72)) > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) goto loc_0023ABB0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 72)))) & (1)) == 0) goto loc_0023ABB0;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 72)))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 72)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_0023AC79;
loc_0023ABA6:
loc_0023ABB0:
    if (a3 == 0) goto loc_0023ABBF;
    if (sign_flag) goto loc_0023ABBF;
    if (a3 != 0) goto loc_0023AB69;
loc_0023ABBF:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 72))) >> (12);
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 72)));
    if (a3 == 0) goto loc_0023AC08;
    v_r11 = (v_r11) >> (12);
    if ((unsigned int)(v_r10) == 0) goto loc_0023AC08;
loc_0023ABEB:
    v_r11 = (v_r11) >> (9);
    result = (unsigned int)((v_r11) & (511));
    result = (result) * (1);
    a1 = (1) << (9);
    v_rdi = (v_rdi) + (result);
    v_r10 = (unsigned int)((v_r10) - (1));
    if (condition_is_not_equal) goto loc_0023ABEB;
loc_0023AC08:
loc_0023AC0D:
loc_0023AC26:
loc_0023AC2E:
    *(unsigned __int64 *)(v_stack_pD0) = v_rdi;
    v_rsi = (v_rsi) + (8);
    a3 = (v_stack_pD0) + (8);
    v_stack_pD0 = a3;
    if (((v_rsi) & (0xFFFULL)) == 0) goto loc_0023ACE2;
    if (1 != 1) goto loc_0023A922;
    v_rdi = (v_rdi) + 1;
    goto loc_0023A918;
loc_0023AC79:
    if (((*(unsigned __int64 *)(v_rip + 14204420)) & (0x600000ULL)) == 0) goto loc_0023ABA6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0023ABA6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0023ABA6;
    a4 = (*(unsigned __int64 *)(v_rsp + 4 * 8 + 72)) >> (3);
    a4 = (unsigned int)((a4) & (511));
    result = v_stack_pD8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (32)) != 0) {
        result = (v_stack_pD8) | (32);
    }
    v_rdi = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (66)) == 0) { v_rdi = result; }
    goto loc_0023ABA6;
loc_0023ACE2:
    v_rbp = 0;
    goto loc_0023A922;
loc_0023ACE9:
    if (0 >= 2) goto loc_0023AA62;
    goto loc_0023AC2E;
loc_0023ACF7:
    if (0 != 3) goto loc_0023AD06;
    if (0 >= 3) goto loc_0023AD30;
loc_0023AD06:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsi))) & (1)) != 0) goto loc_0023AD61;
    v_stack_p20 = *(unsigned __int64 *)(v_rsi);
    result = KeBugCheckEx(26, (unsigned int)(0x1240ULL), v_stack_pC0, v_rsi);
loc_0023AD30:
    a1 = (result) | (544);
    if (((*(unsigned __int64 *)(v_rip + 14204227)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 14204227)) & (0x2000000ULL)) == 0) goto loc_0023AD58;
    if (condition_is_above_or_equal) goto loc_0023AD30;
loc_0023AD58:
    goto loc_0023AD06;
loc_0023AD61:
    v_rdi = (*(unsigned __int64 *)(v_rsi)) >> (12);
    v_rdi = (v_rdi) & (v_r10);
    if (((unsigned int)((unsigned int)(v_stack_pC8))) != 11) goto loc_0023AC26;
    a1 = (v_rsi) << (25);
    result = (v_rsi) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    result = MiQueuePinDriverAddressLog(a1, *(unsigned __int64 *)(v_rsi), 1, v_rsi);
    goto loc_0023AC0D;
}
```

## 5. (Beta) C Style

```c
int64_t MmBuildMdlForNonPagedPool(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint32_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (136);
    a2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x2C))) + (*(uint64_t *)(arg1 + 0x20));
    v_stack_p18 = Arg1 + 48;
    local_rsi = (*(uint64_t *)(arg1 + 0x20)) >> (9);
    local_rsi = (local_rsi) & (local_r13);
    *(uint64_t *)(arg1 + 0x10) = 0;
    *(uint64_t *)(arg1 + 0x18) = a2;
    local_rbx = 0;
    local_rbp = 0;
    a2 = (uint32_t)((a2) & (0xFFFULL));
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) + (0xFFFULL);
    v_stack_m38 = local_r12;
    Arg1 = (Arg1) + (a2);
    v_stack_m40 = local_r15;
    Arg1 = (Arg1) >> (12);
    local_rsi = (local_rsi) + (a4);
    Arg1 = 0;
    v_stack_p10 = 0;
    v_stack_p20 = local_rsi + Arg1 * 8;
loc_0023A918:
loc_0023A922:
    if (local_rsi >= (local_rsi + Arg1 * 8)) goto loc_0023AA86;
    if (0 != 0) goto loc_0023ACE9;
    local_r11 = (local_rsi) << (25);
    result = (a4) << (25);
    local_r11 = (local_r11) - (result);
    local_r11 = (local_r11) >> (16);
    local_rbp = (local_r11) >> (9);
    local_rbp = (local_rbp) & (local_r13);
    local_rbp = (local_rbp) + (a4);
    v_stack_m88 = local_rbp;
    local_r15 = (local_rbp) >> (9);
    local_r15 = (local_r15) & (local_r13);
    local_r15 = (local_r15) + (a4);
    v_stack_m80 = local_r15;
    local_r12 = (local_r15) >> (9);
    local_r12 = (local_r12) & (local_r13);
    local_r12 = (local_r12) + (a4);
    v_stack_m78 = local_r12;
    Arg1 = (local_r12) >> (9);
    local_r13 = (local_r13) & (Arg1);
    local_r13 = (local_r13) + (a4);
    v_stack_m70 = local_r13;
loc_0023A9A4:
    local_r10 = (4) - 1;
    local_rdi = (uint32_t)((4) - 1);
    if ((*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)) < Arg1) goto loc_0023A9F0;
    if ((*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)) > a2) goto loc_0023A9F0;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (1)) == 0) goto loc_0023A9F8;
    a3 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (66)) != 0) ? 1 : 0;
    a2 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(a2)) & ((uint8_t)(a3))) == 0) goto loc_0023AAAA;
loc_0023A9E6:
loc_0023A9F0:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (1)) != 0) goto loc_0023AB14;
loc_0023A9F8:
    if (local_r11 < (*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) goto loc_0023AB27;
    local_r11 = (local_r11) >> (39);
    local_r11 = (uint32_t)((local_r11) & (511));
    local_r11 = (uint32_t)((local_r11) - (256));
    v_stack_p10 = (uint32_t)(*(uint8_t *)(local_r11 + v_rip + 0xBFE08F * 1));
    if (((uint32_t)(*(uint8_t *)(local_r11 + v_rip + 0xBFE08F * 1))) != 4) goto loc_0023AB30;
    v_stack_p10 = (uint32_t)(*(uint8_t *)(local_r11 + v_rip + 0xBFE08F * 1));
loc_0023AA46:
loc_0023AA62:
    if ((((uint8_t)(*(uint64_t *)(local_rsi))) & (1)) != 0) goto loc_0023ACF7;
    v_stack_m98 = *(uint64_t *)(local_rsi);
    result = KeBugCheckEx(26, (uint32_t)(0x1240ULL), Arg1, local_rsi);
loc_0023AA86:
    local_rsp = (local_rsp) + (136);
    return result;
loc_0023AAAA:
    if (((*(uint64_t *)(v_rip + 0xD8BFD3)) & (0x600000ULL)) == 0) goto loc_0023A9E6;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0023A9E6;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0023A9E6;
    a4 = (local_rsi) >> (3);
    a4 = (uint32_t)((a4) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a4 * 8))) & (32)) != 0) {
        Arg1 = (26) | (32);
    }
    result = (Arg1) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a4 * 8))) & (66)) == 0) { result = Arg1; }
    goto loc_0023A9E6;
loc_0023AB14:
    if (sign_flag) goto loc_0023AB3A;
    if (local_r10 == 1) goto loc_0023A9F8;
    goto loc_0023A9A4;
loc_0023AB27:
    Arg1 = 0;
    v_stack_pC8 = 0;
loc_0023AB30:
    goto loc_0023AA46;
loc_0023AB3A:
    if ((uint32_t)(local_rdi) == 0) goto loc_0023A9F8;
    v_stack_p50 = 2;
    v_stack_p58 = v_stack_m40;
    v_stack_p60 = v_stack_m38;
    v_stack_p68 = local_r13;
loc_0023AB69:
    a3 = (4) - 1;
    local_r10 = (uint32_t)((4) - 1);
    if ((*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48)) < 0) goto loc_0023ABB0;
    if ((*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48)) > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a4 * 8))) goto loc_0023ABB0;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48)))) & (1)) == 0) goto loc_0023ABB0;
    a2 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48)))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(a2))) == 0) goto loc_0023AC79;
loc_0023ABA6:
loc_0023ABB0:
    if (a3 == 0) goto loc_0023ABBF;
    if (sign_flag) goto loc_0023ABBF;
    if (a3 != 0) goto loc_0023AB69;
loc_0023ABBF:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48))) >> (12);
    local_rdi = (local_rdi) & (*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48)));
    if (a3 == 0) goto loc_0023AC08;
    local_r11 = (local_r11) >> (12);
    if ((uint32_t)(local_r10) == 0) goto loc_0023AC08;
loc_0023ABEB:
    local_r11 = (local_r11) >> (9);
    result = (uint32_t)((local_r11) & (511));
    result = (result) * (1);
    Arg1 = (1) << (9);
    local_rdi = (local_rdi) + (result);
    local_r10 = (uint32_t)((local_r10) - (1));
    if (condition_is_not_equal) goto loc_0023ABEB;
loc_0023AC08:
loc_0023AC0D:
loc_0023AC26:
loc_0023AC2E:
    *(uint64_t *)(v_stack_pD0) = local_rdi;
    local_rsi = (local_rsi) + (8);
    a3 = (v_stack_pD0) + (8);
    v_stack_pD0 = a3;
    if (((local_rsi) & (0xFFFULL)) == 0) goto loc_0023ACE2;
    if (1 != 1) goto loc_0023A922;
    local_rdi = (local_rdi) + 1;
    goto loc_0023A918;
loc_0023AC79:
    if (((*(uint64_t *)(v_rip + 0xD8BE04)) & (0x600000ULL)) == 0) goto loc_0023ABA6;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0023ABA6;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0023ABA6;
    a4 = (*(uint64_t *)(local_rsp + 0x4 * 8 + 0x48)) >> (3);
    a4 = (uint32_t)((a4) & (511));
    result = v_stack_pD8;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a4 * 8))) & (32)) != 0) {
        result = (v_stack_pD8) | (32);
    }
    local_rdi = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a4 * 8))) & (66)) == 0) { local_rdi = result; }
    goto loc_0023ABA6;
loc_0023ACE2:
    local_rbp = 0;
    goto loc_0023A922;
loc_0023ACE9:
    if (0 >= 2) goto loc_0023AA62;
    goto loc_0023AC2E;
loc_0023ACF7:
    if (0 != 3) goto loc_0023AD06;
    if (0 >= 3) goto loc_0023AD30;
loc_0023AD06:
    if ((((uint8_t)(*(uint64_t *)(local_rsi))) & (1)) != 0) goto loc_0023AD61;
    v_stack_p20 = *(uint64_t *)(local_rsi);
    result = KeBugCheckEx(26, (uint32_t)(0x1240ULL), v_stack_pC0, local_rsi);
loc_0023AD30:
    Arg1 = (result) | (544);
    if (((*(uint64_t *)(v_rip + 0xD8BD43)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD8BD43)) & (0x2000000ULL)) == 0) goto loc_0023AD58;
    if (condition_is_above_or_equal) goto loc_0023AD30;
loc_0023AD58:
    goto loc_0023AD06;
loc_0023AD61:
    local_rdi = (*(uint64_t *)(local_rsi)) >> (12);
    local_rdi = (local_rdi) & (local_r10);
    if (((uint32_t)((uint32_t)(v_stack_pC8))) != 11) goto loc_0023AC26;
    Arg1 = (local_rsi) << (25);
    result = (local_rsi) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    result = MiQueuePinDriverAddressLog(Arg1, *(uint64_t *)(local_rsi), 1, local_rsi);
    goto loc_0023AC0D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0023A870&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
