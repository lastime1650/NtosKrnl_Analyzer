# WmipIoControl

- RVA: `0x009DEBD0`–`0x009DF116` (길이 `1,350` bytes)
- VA: `0x00000001409DEBD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A3A90`
- 디코드: `340`개 명령, `1,350/1,350` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009DECCC` → [WmipQueryAllDataMultiple](WmipQueryAllDataMultiple_function_009DF11C.md) (function, `0x009DF11C`)
- `0x009DECFD` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x009DED0B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009DEDA5` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (function, `0x0040DFE0`)
- `0x009DEDD9` → [WmipProbeAndCaptureGuidObjectAttributes](WmipProbeAndCaptureGuidObjectAttributes_function_009DEA00.md) (function, `0x009DEA00`)
- `0x009DEE2D` → [WmipOpenBlock](../9E/WmipOpenBlock_function_009E00D0.md) (function, `0x009E00D0`)
- `0x009DEE64` → [ObOpenObjectByPointer](../8B/ObOpenObjectByPointer_function_008B7420.md) (function, `0x008B7420`)
- `0x009DEE71` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (function, `0x0040DFE0`)
- `0x009DEE8C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DEED2` → [WmipQueryGuidInfo](WmipQueryGuidInfo_function_009DE66C.md) (function, `0x009DE66C`)
- `0x009DEF1D` → [WmipProbeWnodeWorker](WmipProbeWnodeWorker_function_009DE7BC.md) (function, `0x009DE7BC`)
- `0x009DEF75` → [WmipQuerySetExecuteSI](../9E/WmipQuerySetExecuteSI_function_009E0574.md) (function, `0x009E0574`)
- `0x009DEF88` → [WmipProbeWnodeMethodItem](WmipProbeWnodeMethodItem_function_009DE418.md) (function, `0x009DE418`)
- `0x009DEFDC` → [WmipReceiveNotifications](../../text/4E/WmipReceiveNotifications_function_004EC280.md) (function, `0x004EC280`)
- `0x009DF021` → [WmipTranslateFileHandle](../7B/WmipTranslateFileHandle_function_007B3DA4.md) (function, `0x007B3DA4`)
- `0x009DF087` → [WmipQueryAllData](../9E/WmipQueryAllData_function_009E086C.md) (function, `0x009E086C`)
- `0x009DF0A4` → [WmipEnumerateMofResources](../A9/WmipEnumerateMofResources_function_00A94410.md) (function, `0x00A94410`)
- `0x009DF0BE` → [WmipProbeWnodeSingleItem](../7B/WmipProbeWnodeSingleItem_function_007B3D34.md) (function, `0x007B3D34`)
- `0x009DF0E1` → [WmipProbeWnodeSingleInstance](WmipProbeWnodeSingleInstance_function_009DE73C.md) (function, `0x009DE73C`)
- `0x009DF10C` → [WmipEnumerateGuids](../7B/WmipEnumerateGuids_function_007B3560.md) (function, `0x007B3560`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009DEBF3` → RVA `0x00E0A740` (`.data`; read)
- `0x009DEE4E` → RVA `0x00FC6D70` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x009DECFD` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
  - `0x009DED0B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009DEDA5` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (`PAGE` → `.text`)
  - `0x009DEE71` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (`PAGE` → `.text`)
  - `0x009DEE8C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DEFDC` → [WmipReceiveNotifications](../../text/4E/WmipReceiveNotifications_function_004EC280.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x009DEFAC` → [sub_00B2FE0C](../B2/Unknown_function_00B2FE0C.md) (`tail-transfer`)
  - `0x009DF0D0` → [sub_00B2FE0C + 0x78](../B2/Unknown_function_00B2FE0C.md) (`tail-transfer`)
  - `0x009DF0F0` → [sub_00B2FE0C + 0x75](../B2/Unknown_function_00B2FE0C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009DEBD0  48 8B C4                        mov rax, rsp
009DEBD3  48 89 58 08                     mov qword ptr [rax + 8], rbx
009DEBD7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
009DEBDB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
009DEBDF  55                              push rbp
009DEBE0  41 54                           push r12
009DEBE2  41 55                           push r13
009DEBE4  41 56                           push r14
009DEBE6  41 57                           push r15
009DEBE8  48 8D 68 C8                     lea rbp, [rax - 0x38]
009DEBEC  48 81 EC 10 01 00 00            sub rsp, 0x110
009DEBF3  48 8B 05 46 BB 42 00            mov rax, qword ptr [rip + 0x42bb46]
009DEBFA  48 33 C4                        xor rax, rsp
009DEBFD  48 89 45 00                     mov qword ptr [rbp], rax
009DEC01  48 8B 82 B8 00 00 00            mov rax, qword ptr [rdx + 0xb8]
009DEC08  45 33 FF                        xor r15d, r15d
009DEC0B  48 8B 7A 18                     mov rdi, qword ptr [rdx + 0x18]
009DEC0F  4C 8B EA                        mov r13, rdx
009DEC12  8B 70 08                        mov esi, dword ptr [rax + 8]
009DEC15  44 8B 60 18                     mov r12d, dword ptr [rax + 0x18]
009DEC19  44 8B 70 10                     mov r14d, dword ptr [rax + 0x10]
009DEC1D  B8 58 41 22 00                  mov eax, 0x224158
009DEC22  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
009DEC26  44 3B E0                        cmp r12d, eax
009DEC29  0F 86 03 01 00 00               jbe 0x1409ded32
009DEC2F  41 8B C4                        mov eax, r12d
009DEC32  2D 60 41 22 00                  sub eax, 0x224160
009DEC37  0F 84 B8 04 00 00               je 0x1409df0f5
009DEC3D  2D A8 3E 00 00                  sub eax, 0x3ea8
009DEC42  0F 84 8D 04 00 00               je 0x1409df0d5
009DEC48  83 E8 04                        sub eax, 4
009DEC4B  0F 84 67 04 00 00               je 0x1409df0b8
009DEC51  83 E8 18                        sub eax, 0x18
009DEC54  0F 84 25 03 00 00               je 0x1409def7f
009DEC5A  2D F8 00 00 00                  sub eax, 0xf8
009DEC5F  0F 84 AA 03 00 00               je 0x1409df00f
009DEC65  83 E8 10                        sub eax, 0x10
009DEC68  0F 85 3B 03 00 00               jne 0x1409defa9
009DEC6E  83 FE 38                        cmp esi, 0x38
009DEC71  0F 82 8E 03 00 00               jb 0x1409df005
009DEC77  4A 8D 14 37                     lea rdx, [rdi + r14]
009DEC7B  48 8D 47 04                     lea rax, [rdi + 4]
009DEC7F  48 3B C2                        cmp rax, rdx
009DEC82  0F 87 7D 03 00 00               ja 0x1409df005
009DEC88  8B 07                           mov eax, dword ptr [rdi]
009DEC8A  FF C8                           dec eax
009DEC8C  3D FE 0F 00 00                  cmp eax, 0xffe
009DEC91  0F 87 6E 03 00 00               ja 0x1409df005
009DEC97  8B C8                           mov ecx, eax
009DEC99  48 83 C1 02                     add rcx, 2
009DEC9D  48 8D 0C CF                     lea rcx, [rdi + rcx*8]
009DECA1  48 3B CA                        cmp rcx, rdx
009DECA4  0F 87 5B 03 00 00               ja 0x1409df005
009DECAA  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009DECAF  41 B1 01                        mov r9b, 1
009DECB2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009DECB7  4D 8B C5                        mov r8, r13
009DECBA  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
009DECBF  33 D2                           xor edx, edx
009DECC1  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
009DECC5  33 C9                           xor ecx, ecx
009DECC7  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009DECCC  E8 4B 04 00 00                  call 0x1409df11c
009DECD1  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
009DECD5  8B D8                           mov ebx, eax
009DECD7  81 FB 03 01 00 00               cmp ebx, 0x103
009DECDD  74 23                           je 0x1409ded02
009DECDF  81 FB 20 01 00 C0               cmp ebx, 0xc0000120
009DECE5  74 1B                           je 0x1409ded02
009DECE7  85 DB                           test ebx, ebx
009DECE9  41 89 5D 30                     mov dword ptr [r13 + 0x30], ebx
009DECED  49 8B CD                        mov rcx, r13
009DECF0  44 0F 49 FE                     cmovns r15d, esi
009DECF4  33 D2                           xor edx, edx
009DECF6  41 8B C7                        mov eax, r15d
009DECF9  49 89 45 38                     mov qword ptr [r13 + 0x38], rax
009DECFD  E8 BE C8 8B FF                  call 0x14029b5c0
009DED02  8B C3                           mov eax, ebx
009DED04  48 8B 4D 00                     mov rcx, qword ptr [rbp]
009DED08  48 33 CC                        xor rcx, rsp
009DED0B  E8 30 D9 CC FF                  call 0x1406ac640
009DED10  4C 8D 9C 24 10 01 00 00         lea r11, [rsp + 0x110]
009DED18  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
009DED1C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
009DED20  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
009DED24  49 8B E3                        mov rsp, r11
009DED27  41 5F                           pop r15
009DED29  41 5E                           pop r14
009DED2B  41 5D                           pop r13
009DED2D  41 5C                           pop r12
009DED2F  5D                              pop rbp
009DED30  C3                              ret
009DED31  CC                              int3
009DED32  0F 84 59 03 00 00               je 0x1409df091
009DED38  41 8B C4                        mov eax, r12d
009DED3B  2D 00 40 22 00                  sub eax, 0x224000
009DED40  0F 84 50 01 00 00               je 0x1409dee96
009DED46  83 E8 04                        sub eax, 4
009DED49  0F 84 92 01 00 00               je 0x1409deee1
009DED4F  2D 04 01 00 00                  sub eax, 0x104
009DED54  74 29                           je 0x1409ded7f
009DED56  83 E8 1C                        sub eax, 0x1c
009DED59  0F 84 D6 02 00 00               je 0x1409df035
009DED5F  83 E8 10                        sub eax, 0x10
009DED62  0F 84 8D 03 00 00               je 0x1409df0f5
009DED68  83 E8 04                        sub eax, 4
009DED6B  0F 84 55 01 00 00               je 0x1409deec6
009DED71  83 E8 04                        sub eax, 4
009DED74  74 09                           je 0x1409ded7f
009DED76  83 F8 04                        cmp eax, 4
009DED79  0F 85 2F 03 00 00               jne 0x1409df0ae
009DED7F  0F 57 C0                        xorps xmm0, xmm0
009DED82  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
009DED87  33 C0                           xor eax, eax
009DED89  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
009DED8E  33 C9                           xor ecx, ecx
009DED90  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
009DED94  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
009DED99  89 45 88                        mov dword ptr [rbp - 0x78], eax
009DED9C  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
009DEDA1  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
009DEDA5  E8 36 F2 A2 FF                  call 0x14040dfe0
009DEDAA  84 C0                           test al, al
009DEDAC  0F 85 34 02 00 00               jne 0x1409defe6
009DEDB2  41 83 FE 18                     cmp r14d, 0x18
009DEDB6  0F 85 00 01 00 00               jne 0x1409deebc
009DEDBC  41 3B F6                        cmp esi, r14d
009DEDBF  0F 85 F7 00 00 00               jne 0x1409deebc
009DEDC5  4C 8B 0F                        mov r9, qword ptr [rdi]
009DEDC8  44 8B 77 08                     mov r14d, dword ptr [rdi + 8]
009DEDCC  4C 8D 45 A0                     lea r8, [rbp - 0x60]
009DEDD0  48 8D 55 90                     lea rdx, [rbp - 0x70]
009DEDD4  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009DEDD9  E8 22 FC FF FF                  call 0x1409dea00
009DEDDE  8B D8                           mov ebx, eax
009DEDE0  85 C0                           test eax, eax
009DEDE2  78 2A                           js 0x1409dee0e
009DEDE4  4C 39 7C 24 68                  cmp qword ptr [rsp + 0x68], r15
009DEDE9  0F 85 62 02 00 00               jne 0x1409df051
009DEDEF  44 39 7C 24 78                  cmp dword ptr [rsp + 0x78], r15d
009DEDF4  0F 85 57 02 00 00               jne 0x1409df051
009DEDFA  4C 39 7D 80                     cmp qword ptr [rbp - 0x80], r15
009DEDFE  0F 85 4D 02 00 00               jne 0x1409df051
009DEE04  4C 39 7D 88                     cmp qword ptr [rbp - 0x78], r15
009DEE08  0F 85 43 02 00 00               jne 0x1409df051
009DEE0E  85 DB                           test ebx, ebx
009DEE10  0F 88 C1 FE FF FF               js 0x1409decd7
009DEE16  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009DEE1B  45 8B CE                        mov r9d, r14d
009DEE1E  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
009DEE23  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009DEE28  B2 01                           mov dl, 1
009DEE2A  41 8B CC                        mov ecx, r12d
009DEE2D  E8 9E 12 00 00                  call 0x1409e00d0
009DEE32  8B D8                           mov ebx, eax
009DEE34  85 C0                           test eax, eax
009DEE36  0F 88 9B FE FF FF               js 0x1409decd7
009DEE3C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009DEE41  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009DEE46  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009DEE4B  45 8B CE                        mov r9d, r14d
009DEE4E  48 8B 05 1B 7F 5E 00            mov rax, qword ptr [rip + 0x5e7f1b]
009DEE55  45 33 C0                        xor r8d, r8d
009DEE58  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009DEE5D  33 D2                           xor edx, edx
009DEE5F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009DEE64  E8 B7 85 ED FF                  call 0x1408b7420
009DEE69  8B D8                           mov ebx, eax
009DEE6B  85 C0                           test eax, eax
009DEE6D  78 18                           js 0x1409dee87
009DEE6F  33 C9                           xor ecx, ecx
009DEE71  E8 6A F1 A2 FF                  call 0x14040dfe0
009DEE76  84 C0                           test al, al
009DEE78  0F 85 DD 01 00 00               jne 0x1409df05b
009DEE7E  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009DEE83  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
009DEE87  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009DEE8C  E8 BF A4 91 FF                  call 0x1402f9350
009DEE91  E9 41 FE FF FF                  jmp 0x1409decd7
009DEE96  83 FE 48                        cmp esi, 0x48
009DEE99  0F 82 00 01 00 00               jb 0x1409def9f
009DEE9F  41 83 FE 30                     cmp r14d, 0x30
009DEEA3  72 17                           jb 0x1409deebc
009DEEA5  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
009DEEA8  A8 01                           test al, 1
009DEEAA  74 10                           je 0x1409deebc
009DEEAC  44 3B 37                        cmp r14d, dword ptr [rdi]
009DEEAF  75 0B                           jne 0x1409deebc
009DEEB1  A9 7E FF FF FF                  test eax, 0xffffff7e
009DEEB6  0F 84 B5 01 00 00               je 0x1409df071
009DEEBC  BB 01 00 00 C0                  mov ebx, 0xc0000001
009DEEC1  E9 21 FE FF FF                  jmp 0x1409dece7
009DEEC6  83 FE 10                        cmp esi, 0x10
009DEEC9  0F 82 D0 00 00 00               jb 0x1409def9f
009DEECF  48 8B CF                        mov rcx, rdi
009DEED2  E8 95 F7 FF FF                  call 0x1409de66c
009DEED7  BE 10 00 00 00                  mov esi, 0x10
009DEEDC  E9 F4 FD FF FF                  jmp 0x1409decd5
009DEEE1  83 FE 38                        cmp esi, 0x38
009DEEE4  0F 82 B5 00 00 00               jb 0x1409def9f
009DEEEA  BA 40 00 00 00                  mov edx, 0x40
009DEEEF  44 3B F2                        cmp r14d, edx
009DEEF2  72 C8                           jb 0x1409deebc
009DEEF4  3B F2                           cmp esi, edx
009DEEF6  72 C4                           jb 0x1409deebc
009DEEF8  8B 47 3C                        mov eax, dword ptr [rdi + 0x3c]
009DEEFB  48 8B CF                        mov rcx, rdi
009DEEFE  44 8B 4F 38                     mov r9d, dword ptr [rdi + 0x38]
009DEF02  44 8B 47 30                     mov r8d, dword ptr [rdi + 0x30]
009DEF06  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
009DEF0B  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
009DEF10  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
009DEF14  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
009DEF19  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009DEF1D  E8 9A F8 FF FF                  call 0x1409de7bc
009DEF22  8B D8                           mov ebx, eax
009DEF24  85 C0                           test eax, eax
009DEF26  78 22                           js 0x1409def4a
009DEF28  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
009DEF2B  A8 02                           test al, 2
009DEF2D  0F 84 34 01 00 00               je 0x1409df067
009DEF33  44 3B 37                        cmp r14d, dword ptr [rdi]
009DEF36  0F 85 2B 01 00 00               jne 0x1409df067
009DEF3C  41 8B DF                        mov ebx, r15d
009DEF3F  A9 7D FF FF FF                  test eax, 0xffffff7d
009DEF44  0F 85 1D 01 00 00               jne 0x1409df067
009DEF4A  85 DB                           test ebx, ebx
009DEF4C  0F 88 85 FD FF FF               js 0x1409decd7
009DEF52  41 B1 01                        mov r9b, 1
009DEF55  45 8A C1                        mov r8b, r9b
009DEF58  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009DEF5D  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
009DEF62  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009DEF67  49 8B D5                        mov rdx, r13
009DEF6A  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
009DEF6E  33 C9                           xor ecx, ecx
009DEF70  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
009DEF75  E8 FA 15 00 00                  call 0x1409e0574
009DEF7A  E9 52 FD FF FF                  jmp 0x1409decd1
009DEF7F  44 8B C6                        mov r8d, esi
009DEF82  41 8B D6                        mov edx, r14d
009DEF85  48 8B CF                        mov rcx, rdi
009DEF88  E8 8B F4 FF FF                  call 0x1409de418
009DEF8D  8B D8                           mov ebx, eax
009DEF8F  85 C0                           test eax, eax
009DEF91  0F 88 40 FD FF FF               js 0x1409decd7
009DEF97  41 B1 09                        mov r9b, 9
009DEF9A  41 B0 01                        mov r8b, 1
009DEF9D  EB B9                           jmp 0x1409def58
009DEF9F  BB 23 00 00 C0                  mov ebx, 0xc0000023
009DEFA4  E9 3E FD FF FF                  jmp 0x1409dece7
009DEFA9  83 E8 04                        sub eax, 4
009DEFAC  0F 84 5A 0E 15 00               je 0x140b2fe0c
009DEFB2  83 F8 14                        cmp eax, 0x14
009DEFB5  0F 85 F3 00 00 00               jne 0x1409df0ae
009DEFBB  83 FE 38                        cmp esi, 0x38
009DEFBE  72 6B                           jb 0x1409df02b
009DEFC0  41 83 FE 10                     cmp r14d, 0x10
009DEFC4  72 65                           jb 0x1409df02b
009DEFC6  41 8D 46 F8                     lea eax, [r14 - 8]
009DEFCA  C1 E8 03                        shr eax, 3
009DEFCD  39 07                           cmp dword ptr [rdi], eax
009DEFCF  77 5A                           ja 0x1409df02b
009DEFD1  4D 8B C5                        mov r8, r13
009DEFD4  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
009DEFD9  48 8B CF                        mov rcx, rdi
009DEFDC  E8 9F D2 B0 FF                  call 0x1404ec280
009DEFE1  E9 EB FC FF FF                  jmp 0x1409decd1
009DEFE6  41 83 FE 10                     cmp r14d, 0x10
009DEFEA  0F 85 CC FE FF FF               jne 0x1409deebc
009DEFF0  41 3B F6                        cmp esi, r14d
009DEFF3  0F 85 C3 FE FF FF               jne 0x1409deebc
009DEFF9  44 8B 0F                        mov r9d, dword ptr [rdi]
009DEFFC  44 8B 77 04                     mov r14d, dword ptr [rdi + 4]
009DF000  E9 C7 FD FF FF                  jmp 0x1409dedcc
009DF005  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009DF00A  E9 C8 FC FF FF                  jmp 0x1409decd7
009DF00F  41 83 FE 16                     cmp r14d, 0x16
009DF013  0F 85 A3 FE FF FF               jne 0x1409deebc
009DF019  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
009DF01E  48 8B CF                        mov rcx, rdi
009DF021  E8 7E 4D DD FF                  call 0x1407b3da4
009DF026  E9 A6 FC FF FF                  jmp 0x1409decd1
009DF02B  BB 10 00 00 C0                  mov ebx, 0xc0000010
009DF030  E9 A2 FC FF FF                  jmp 0x1409decd7
009DF035  83 FE 04                        cmp esi, 4
009DF038  0F 82 61 FF FF FF               jb 0x1409def9f
009DF03E  C7 07 01 00 00 00               mov dword ptr [rdi], 1
009DF044  BE 04 00 00 00                  mov esi, 4
009DF049  41 8B DF                        mov ebx, r15d
009DF04C  E9 96 FC FF FF                  jmp 0x1409dece7
009DF051  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009DF056  E9 B3 FD FF FF                  jmp 0x1409dee0e
009DF05B  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
009DF05F  89 47 08                        mov dword ptr [rdi + 8], eax
009DF062  E9 20 FE FF FF                  jmp 0x1409dee87
009DF067  BB 01 00 00 C0                  mov ebx, 0xc0000001
009DF06C  E9 D9 FE FF FF                  jmp 0x1409def4a
009DF071  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009DF076  4C 8B CF                        mov r9, rdi
009DF079  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009DF07E  41 B0 01                        mov r8b, 1
009DF081  33 C9                           xor ecx, ecx
009DF083  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
009DF087  E8 E0 17 00 00                  call 0x1409e086c
009DF08C  E9 40 FC FF FF                  jmp 0x1409decd1
009DF091  83 FE 10                        cmp esi, 0x10
009DF094  0F 82 6B FF FF FF               jb 0x1409df005
009DF09A  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
009DF09F  8B D6                           mov edx, esi
009DF0A1  48 8B CF                        mov rcx, rdi
009DF0A4  E8 67 53 0B 00                  call 0x140a94410
009DF0A9  E9 23 FC FF FF                  jmp 0x1409decd1
009DF0AE  BB 10 00 00 C0                  mov ebx, 0xc0000010
009DF0B3  E9 2F FC FF FF                  jmp 0x1409dece7
009DF0B8  41 8B D6                        mov edx, r14d
009DF0BB  48 8B CF                        mov rcx, rdi
009DF0BE  E8 71 4C DD FF                  call 0x1407b3d34
009DF0C3  8B D8                           mov ebx, eax
009DF0C5  85 C0                           test eax, eax
009DF0C7  0F 88 0A FC FF FF               js 0x1409decd7
009DF0CD  41 B1 03                        mov r9b, 3
009DF0D0  E9 AF 0D 15 00                  jmp 0x140b2fe84
009DF0D5  45 33 C9                        xor r9d, r9d
009DF0D8  44 8B C6                        mov r8d, esi
009DF0DB  41 8B D6                        mov edx, r14d
009DF0DE  48 8B CF                        mov rcx, rdi
009DF0E1  E8 56 F6 FF FF                  call 0x1409de73c
009DF0E6  8B D8                           mov ebx, eax
009DF0E8  85 C0                           test eax, eax
009DF0EA  0F 88 E7 FB FF FF               js 0x1409decd7
009DF0F0  E9 8C 0D 15 00                  jmp 0x140b2fe81
009DF0F5  83 FE 08                        cmp esi, 8
009DF0F8  0F 82 A1 FE FF FF               jb 0x1409def9f
009DF0FE  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
009DF103  44 8B C6                        mov r8d, esi
009DF106  48 8B D7                        mov rdx, rdi
009DF109  41 8B CC                        mov ecx, r12d
009DF10C  E8 4F 44 DD FF                  call 0x1407b3560
009DF111  E9 BB FB FF FF                  jmp 0x1409decd1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipIoControl(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mD0;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 4373318)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 56) = result;
    v_r15 = 0;
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 24)))) <= ((unsigned int)((unsigned int)(0x224158ULL)))) goto loc_009DED32;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 24))))) - (0x224160ULL));
    if (condition_is_equal) goto loc_009DF0F5;
    result = (unsigned int)((result) - (0x3EA8ULL));
    if (condition_is_equal) goto loc_009DF0D5;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_009DF0B8;
    result = (unsigned int)((result) - (24));
    if (condition_is_equal) goto loc_009DEF7F;
    result = (unsigned int)((result) - (248));
    if (condition_is_equal) goto loc_009DF00F;
    result = (unsigned int)((result) - (16));
    if (condition_is_not_equal) goto loc_009DEFA9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8)))) < 56) goto loc_009DF005;
    if ((*(unsigned __int64 *)(a2 + 24) + 4) > (*(unsigned __int64 *)(a2 + 24) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 16)) * 1)) goto loc_009DF005;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24)))) - 1);
    if (((unsigned int)(result)) > 0xFFEULL) goto loc_009DF005;
    a1 = ((unsigned int)((unsigned int)(result))) + (2);
    if ((*(unsigned __int64 *)(a2 + 24) + a1 * 8) > (*(unsigned __int64 *)(a2 + 24) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 16)) * 1)) goto loc_009DF005;
    v_stack_m100 = v_stack_mE8;
    v_stack_m108 = *(unsigned __int64 *)(a2 + 24);
    a2 = 0;
    v_stack_m110 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 8)));
    a1 = 0;
    v_stack_m118 = *(unsigned __int64 *)(a2 + 24);
    result = WmipQueryAllDataMultiple(a1, a2, a2, 1);
loc_009DECD1:
loc_009DECD5:
loc_009DECD7:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 259) goto loc_009DED02;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000120ULL) {
        *(unsigned int *)(a2 + 48) = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = 0;
        if (!sign_flag) { v_r15 = (unsigned int)((unsigned int)(v_stack_mE8)); }
        a2 = 0;
        result = (unsigned int)(v_r15);
        *(unsigned __int64 *)(a2 + 56) = result;
        result = IofCompleteRequest(a1, a2, a2, 1);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 56)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a2, 1);
    return result;
loc_009DED32:
    if (condition_is_equal) goto loc_009DF091;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 24))))) - (0x224000ULL));
    if (condition_is_equal) goto loc_009DEE96;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_009DEEE1;
    result = (unsigned int)((result) - (260));
    if (condition_is_equal) goto loc_009DED7F;
    result = (unsigned int)((result) - (28));
    if (condition_is_equal) goto loc_009DF035;
    result = (unsigned int)((result) - (16));
    if (condition_is_equal) goto loc_009DF0F5;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_009DEEC6;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_009DED7F;
    if (((unsigned int)(result)) != 4) goto loc_009DF0AE;
loc_009DED7F:
    v_stack_mC0 = v_r15;
    result = 0;
    v_stack_mB8 = v_r15;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 128) = 0;
    v_stack_mB0 = v_xmm0;
    *(unsigned int *)(v_rsp - 56 - 120) = 0;
    v_stack_mA0 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = v_xmm0;
    result = IoIs32bitProcess(a1, a2, a2, 1);
    if ((unsigned __int8)(result) != 0) goto loc_009DEFE6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 16)))) != 24) goto loc_009DEEBC;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 16))))) goto loc_009DEEBC;
loc_009DEDCC:
    result = WmipProbeAndCaptureGuidObjectAttributes(v_stack_mB0, v_rsp - 56 - 112, v_rsp - 56 - 96, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)));
    if (sign_flag) goto loc_009DEE0E;
    if (v_stack_mA8 != v_r15) goto loc_009DF051;
    if (v_stack_m98 != ((unsigned int)(v_r15))) goto loc_009DF051;
    if ((*(unsigned __int64 *)(v_rsp - 56 - 128)) != v_r15) goto loc_009DF051;
    if ((*(unsigned __int64 *)(v_rsp - 56 - 120)) != v_r15) goto loc_009DF051;
loc_009DEE0E:
    if (sign_flag) goto loc_009DECD7;
    v_stack_mF0 = v_stack_mB8;
    result = WmipOpenBlock((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 24)))), 1, v_stack_mB0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))));
    if (sign_flag) goto loc_009DECD7;
    v_stack_mE0 = v_stack_mC0;
    a3 = 0;
    v_stack_mE8 = 1;
    a2 = 0;
    v_stack_mF0 = *(unsigned __int64 *)(v_rip + 6192923);
    result = ObOpenObjectByPointer(v_stack_mB8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))));
    if (sign_flag) goto loc_009DEE87;
    a1 = 0;
    result = IoIs32bitProcess(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))));
    if ((unsigned __int8)(result) != 0) goto loc_009DF05B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16) = v_stack_mC0;
loc_009DEE87:
    result = ObfDereferenceObject(v_stack_mB8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))));
    goto loc_009DECD7;
loc_009DEE96:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))) < 72) goto loc_009DEF9F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))) < 48) goto loc_009DEEBC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 44)))) & (1)) == 0) goto loc_009DEEBC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))) != (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_009DEEBC;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 44)))) & (0xFFFFFF7EULL)) == 0) goto loc_009DF071;
loc_009DEEBC:
    goto loc_009DECE7;
loc_009DEEC6:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))) < 16) goto loc_009DEF9F;
    result = WmipQueryGuidInfo(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))));
    goto loc_009DECD5;
loc_009DEEE1:
    if (16 < 56) goto loc_009DEF9F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))) < 64) goto loc_009DEEBC;
    if (16 < 64) goto loc_009DEEBC;
    v_stack_mD0 = (unsigned __int8)(v_r15);
    v_stack_mD8 = 1;
    v_stack_mE0 = 16;
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)));
    v_stack_mF0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 60)));
    result = WmipProbeWnodeWorker(*(unsigned __int64 *)(v_stack_m28 + 72), 64, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56)));
    if (sign_flag) goto loc_009DEF4A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 44)))) & (2)) == 0) goto loc_009DF067;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))) != (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_009DF067;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 44)))) & (0xFFFFFF7DULL)) != 0) goto loc_009DF067;
loc_009DEF4A:
    if (sign_flag) goto loc_009DECD7;
loc_009DEF58:
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)));
    v_stack_mE0 = v_stack_mC0;
    v_stack_mE8 = 16;
    a1 = 0;
    v_stack_mF0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = WmipQuerySetExecuteSI(a1, 0, 1, 1);
    goto loc_009DECD1;
loc_009DEF7F:
    result = WmipProbeWnodeMethodItem(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))), 16, 1);
    if (sign_flag) goto loc_009DECD7;
    goto loc_009DEF58;
loc_009DEF9F:
    goto loc_009DECE7;
loc_009DEFA9:
    result = (unsigned int)((result) - (4));
    if (((unsigned int)(result)) != 20) goto loc_009DF0AE;
    if (16 < 56) goto loc_009DF02B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))) < 16) goto loc_009DF02B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)) - 8) >> (3));
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72))) > ((unsigned int)(result))) goto loc_009DF02B;
    result = WmipReceiveNotifications(*(unsigned __int64 *)(v_stack_m28 + 72), v_stack_mC0, 0, 9);
    goto loc_009DECD1;
loc_009DEFE6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)))) != 16) goto loc_009DEEBC;
    if (16 != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8))))) goto loc_009DEEBC;
    goto loc_009DEDCC;
loc_009DF005:
    goto loc_009DECD7;
loc_009DF00F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4)))) != 22) goto loc_009DEEBC;
    result = WmipTranslateFileHandle(*(unsigned __int64 *)(v_stack_m28 + 72), v_stack_mC0, 0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72))));
    goto loc_009DECD1;
loc_009DF02B:
    goto loc_009DECD7;
loc_009DF035:
    if (16 < 4) goto loc_009DEF9F;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72)) = 1;
    goto loc_009DECE7;
loc_009DF051:
    goto loc_009DEE0E;
loc_009DF05B:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8) = (unsigned int)((unsigned int)(v_stack_mC0));
    goto loc_009DEE87;
loc_009DF067:
    goto loc_009DEF4A;
loc_009DF071:
    v_stack_mE8 = v_stack_mC0;
    a1 = 0;
    v_stack_mF0 = 4;
    result = WmipQueryAllData(a1, v_stack_mC0, 1, *(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_009DECD1;
loc_009DF091:
    if (4 < 16) goto loc_009DF005;
    result = WmipEnumerateMofResources(*(unsigned __int64 *)(v_stack_m28 + 72), 4, v_stack_mC0, *(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_009DECD1;
loc_009DF0AE:
    goto loc_009DECE7;
loc_009DF0B8:
    result = WmipProbeWnodeSingleItem(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4)))), v_stack_mC0, *(unsigned __int64 *)(v_stack_m28 + 72));
    if (sign_flag) goto loc_009DECD7;
loc_009DF0D5:
    a4 = 0;
    result = WmipProbeWnodeSingleInstance(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4)))), 4, a4);
    if (sign_flag) goto loc_009DECD7;
loc_009DF0F5:
    if (4 < 8) goto loc_009DEF9F;
    result = WmipEnumerateGuids((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 184) + 24)))), *(unsigned __int64 *)(v_stack_m28 + 72), 4, v_stack_mC0);
    goto loc_009DECD1;
}
```

## 5. (Beta) C Style

```c
int64_t WmipIoControl(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m28;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mD0;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x42BB46)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x38) = result;
    local_r15 = 0;
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x18)))) <= ((uint32_t)((uint32_t)(0x224158ULL)))) goto loc_009DED32;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x18))))) - (0x224160ULL));
    if (condition_is_equal) goto loc_009DF0F5;
    result = (uint32_t)((result) - (0x3EA8ULL));
    if (condition_is_equal) goto loc_009DF0D5;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_009DF0B8;
    result = (uint32_t)((result) - (24));
    if (condition_is_equal) goto loc_009DEF7F;
    result = (uint32_t)((result) - (248));
    if (condition_is_equal) goto loc_009DF00F;
    result = (uint32_t)((result) - (16));
    if (condition_is_not_equal) goto loc_009DEFA9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8)))) < 56) goto loc_009DF005;
    if ((*(uint64_t *)(arg2 + 0x18) + 4) > (*(uint64_t *)(arg2 + 0x18) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10)) * 1)) goto loc_009DF005;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18)))) - 1);
    if (((uint32_t)(result)) > 0xFFEULL) goto loc_009DF005;
    Arg1 = ((uint32_t)((uint32_t)(result))) + (2);
    if ((*(uint64_t *)(arg2 + 0x18) + Arg1 * 8) > (*(uint64_t *)(arg2 + 0x18) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10)) * 1)) goto loc_009DF005;
    v_stack_m100 = v_stack_mE8;
    v_stack_m108 = *(uint64_t *)(arg2 + 0x18);
    Arg2 = 0;
    v_stack_m110 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x8)));
    Arg1 = 0;
    v_stack_m118 = *(uint64_t *)(arg2 + 0x18);
    result = WmipQueryAllDataMultiple(Arg1, Arg2, Arg2, 1);
loc_009DECD1:
loc_009DECD5:
loc_009DECD7:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 259) goto loc_009DED02;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000120ULL) {
        *(uint32_t *)(arg2 + 0x30) = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = 0;
        if (!sign_flag) { local_r15 = (uint32_t)((uint32_t)(v_stack_mE8)); }
        Arg2 = 0;
        result = (uint32_t)(local_r15);
        *(uint64_t *)(arg2 + 0x38) = result;
        result = IofCompleteRequest(Arg1, Arg2, Arg2, 1);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x38)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg2, 1);
    return result;
loc_009DED32:
    if (condition_is_equal) goto loc_009DF091;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x18))))) - (0x224000ULL));
    if (condition_is_equal) goto loc_009DEE96;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_009DEEE1;
    result = (uint32_t)((result) - (260));
    if (condition_is_equal) goto loc_009DED7F;
    result = (uint32_t)((result) - (28));
    if (condition_is_equal) goto loc_009DF035;
    result = (uint32_t)((result) - (16));
    if (condition_is_equal) goto loc_009DF0F5;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_009DEEC6;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_009DED7F;
    if (((uint32_t)(result)) != 4) goto loc_009DF0AE;
loc_009DED7F:
    v_stack_mC0 = local_r15;
    result = 0;
    v_stack_mB8 = local_r15;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x80) = 0;
    v_stack_mB0 = v_xmm0;
    *(uint32_t *)(local_rsp - 0x38 - 0x78) = 0;
    v_stack_mA0 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = v_xmm0;
    result = IoIs32bitProcess(Arg1, Arg2, Arg2, 1);
    if ((uint8_t)(result) != 0) goto loc_009DEFE6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10)))) != 24) goto loc_009DEEBC;
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x10))))) goto loc_009DEEBC;
loc_009DEDCC:
    result = WmipProbeAndCaptureGuidObjectAttributes(v_stack_mB0, local_rsp - 56 - 112, local_rsp - 56 - 96, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)));
    if (sign_flag) goto loc_009DEE0E;
    if (v_stack_mA8 != local_r15) goto loc_009DF051;
    if (v_stack_m98 != ((uint32_t)(local_r15))) goto loc_009DF051;
    if ((*(uint64_t *)(local_rsp - 0x38 - 0x80)) != local_r15) goto loc_009DF051;
    if ((*(uint64_t *)(local_rsp - 0x38 - 0x78)) != local_r15) goto loc_009DF051;
loc_009DEE0E:
    if (sign_flag) goto loc_009DECD7;
    v_stack_mF0 = v_stack_mB8;
    result = WmipOpenBlock((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x18)))), 1, v_stack_mB0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))));
    if (sign_flag) goto loc_009DECD7;
    v_stack_mE0 = v_stack_mC0;
    a3 = 0;
    v_stack_mE8 = 1;
    Arg2 = 0;
    v_stack_mF0 = *(uint64_t *)(v_rip + 0x5E7F1B);
    result = ObOpenObjectByPointer(v_stack_mB8, Arg2, a3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))));
    if (sign_flag) goto loc_009DEE87;
    Arg1 = 0;
    result = IoIs32bitProcess(Arg1, Arg2, a3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))));
    if ((uint8_t)(result) != 0) goto loc_009DF05B;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10) = v_stack_mC0;
loc_009DEE87:
    result = ObfDereferenceObject(v_stack_mB8, Arg2, a3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))));
    goto loc_009DECD7;
loc_009DEE96:
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))) < 72) goto loc_009DEF9F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))) < 48) goto loc_009DEEBC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x2C)))) & (1)) == 0) goto loc_009DEEBC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))) != (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_009DEEBC;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x2C)))) & (0xFFFFFF7EULL)) == 0) goto loc_009DF071;
loc_009DEEBC:
    goto loc_009DECE7;
loc_009DEEC6:
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))) < 16) goto loc_009DEF9F;
    result = WmipQueryGuidInfo(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, a3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))));
    goto loc_009DECD5;
loc_009DEEE1:
    if (16 < 56) goto loc_009DEF9F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))) < 64) goto loc_009DEEBC;
    if (16 < 64) goto loc_009DEEBC;
    v_stack_mD0 = (uint8_t)(local_r15);
    v_stack_mD8 = 1;
    v_stack_mE0 = 16;
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)));
    v_stack_mF0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x3C)));
    result = WmipProbeWnodeWorker(*(uint64_t *)(v_stack_m28 + 0x48), 64, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38)));
    if (sign_flag) goto loc_009DEF4A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x2C)))) & (2)) == 0) goto loc_009DF067;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))) != (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_009DF067;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x2C)))) & (0xFFFFFF7DULL)) != 0) goto loc_009DF067;
loc_009DEF4A:
    if (sign_flag) goto loc_009DECD7;
loc_009DEF58:
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)));
    v_stack_mE0 = v_stack_mC0;
    v_stack_mE8 = 16;
    Arg1 = 0;
    v_stack_mF0 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = WmipQuerySetExecuteSI(Arg1, 0, 1, 1);
    goto loc_009DECD1;
loc_009DEF7F:
    result = WmipProbeWnodeMethodItem(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))), 16, 1);
    if (sign_flag) goto loc_009DECD7;
    goto loc_009DEF58;
loc_009DEF9F:
    goto loc_009DECE7;
loc_009DEFA9:
    result = (uint32_t)((result) - (4));
    if (((uint32_t)(result)) != 20) goto loc_009DF0AE;
    if (16 < 56) goto loc_009DF02B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))) < 16) goto loc_009DF02B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)) - 8) >> (3));
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48))) > ((uint32_t)(result))) goto loc_009DF02B;
    result = WmipReceiveNotifications(*(uint64_t *)(v_stack_m28 + 0x48), v_stack_mC0, 0, 9);
    goto loc_009DECD1;
loc_009DEFE6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)))) != 16) goto loc_009DEEBC;
    if (16 != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8))))) goto loc_009DEEBC;
    goto loc_009DEDCC;
loc_009DF005:
    goto loc_009DECD7;
loc_009DF00F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x4)))) != 22) goto loc_009DEEBC;
    result = WmipTranslateFileHandle(*(uint64_t *)(v_stack_m28 + 0x48), v_stack_mC0, 0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48))));
    goto loc_009DECD1;
loc_009DF02B:
    goto loc_009DECD7;
loc_009DF035:
    if (16 < 4) goto loc_009DEF9F;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48)) = 1;
    goto loc_009DECE7;
loc_009DF051:
    goto loc_009DEE0E;
loc_009DF05B:
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8) = (uint32_t)((uint32_t)(v_stack_mC0));
    goto loc_009DEE87;
loc_009DF067:
    goto loc_009DEF4A;
loc_009DF071:
    v_stack_mE8 = v_stack_mC0;
    Arg1 = 0;
    v_stack_mF0 = 4;
    result = WmipQueryAllData(Arg1, v_stack_mC0, 1, *(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_009DECD1;
loc_009DF091:
    if (4 < 16) goto loc_009DF005;
    result = WmipEnumerateMofResources(*(uint64_t *)(v_stack_m28 + 0x48), 4, v_stack_mC0, *(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_009DECD1;
loc_009DF0AE:
    goto loc_009DECE7;
loc_009DF0B8:
    result = WmipProbeWnodeSingleItem(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x4)))), v_stack_mC0, *(uint64_t *)(v_stack_m28 + 0x48));
    if (sign_flag) goto loc_009DECD7;
loc_009DF0D5:
    a4 = 0;
    result = WmipProbeWnodeSingleInstance(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x4)))), 4, a4);
    if (sign_flag) goto loc_009DECD7;
loc_009DF0F5:
    if (4 < 8) goto loc_009DEF9F;
    result = WmipEnumerateGuids((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x18)))), *(uint64_t *)(v_stack_m28 + 0x48), 4, v_stack_mC0);
    goto loc_009DECD1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x38` | `64` | `W` |
| `Arg2` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009DEBD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
