# MiFindEmptyAddressRange

- RVA: `0x00886050`–`0x0088656B` (길이 `1,307` bytes)
- VA: `0x0000000140886050`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007CA24`
- 디코드: `291`개 명령, `1,307/1,307` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008861AE` → [RtlFindClearBitsEx](../../text/3F/RtlFindClearBitsEx_function_003FAF30.md) (function, `0x003FAF30`)
- `0x008862A9` → [MiExpandVadBitMap](MiExpandVadBitMap_function_00886574.md) (function, `0x00886574`)
- `0x00886300` → [MiFindClearVadBitsAligned](MiFindClearVadBitsAligned_function_00887770.md) (function, `0x00887770`)
- `0x008863C7` → [MiFindEmptyAddressRangeInTree](../A2/MiFindEmptyAddressRangeInTree_function_00A26328.md) (function, `0x00A26328`)
- `0x00886420` → [MiFindEmptyAddressRangeInTree](../A2/MiFindEmptyAddressRangeInTree_function_00A26328.md) (function, `0x00A26328`)

### Direct callers
- [MiSelectUserAddress](MiSelectUserAddress_function_00885C40.md) at `0x00885DA5`

### Static image references
- `0x00886135` → RVA `0x00E2F388` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008861AE` → [RtlFindClearBitsEx](../../text/3F/RtlFindClearBitsEx_function_003FAF30.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00886050  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00886055  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0088605A  55                              push rbp
0088605B  56                              push rsi
0088605C  57                              push rdi
0088605D  41 54                           push r12
0088605F  41 55                           push r13
00886061  41 56                           push r14
00886063  41 57                           push r15
00886065  48 83 EC 60                     sub rsp, 0x60
00886069  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00886071  4D 8B E0                        mov r12, r8
00886074  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
0088607C  48 8B C3                        mov rax, rbx
0088607F  49 2B C6                        sub rax, r14
00886082  4C 8B EA                        mov r13, rdx
00886085  48 FF C0                        inc rax
00886088  48 8B E9                        mov rbp, rcx
0088608B  48 3B C2                        cmp rax, rdx
0088608E  0F 82 F7 01 00 00               jb 0x14088628b
00886094  F6 84 24 D0 00 00 00 02         test byte ptr [rsp + 0xd0], 2
0088609C  41 BA 01 00 00 00               mov r10d, 1
008860A2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008860AB  48 8B BC 24 E0 00 00 00         mov rdi, qword ptr [rsp + 0xe0]
008860B3  4C 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r10
008860BB  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
008860C2  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
008860CA  44 89 17                        mov dword ptr [rdi], r10d
008860CD  0F 85 37 02 00 00               jne 0x14088630a
008860D3  45 33 D2                        xor r10d, r10d
008860D6  45 33 C0                        xor r8d, r8d
008860D9  33 D2                           xor edx, edx
008860DB  4C 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r10
008860E3  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
008860E8  4C 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r8
008860F0  41 BB 00 00 01 00               mov r11d, 0x10000
008860F6  4D 85 C9                        test r9, r9
008860F9  0F 85 50 01 00 00               jne 0x14088624f
008860FF  4D 3B E3                        cmp r12, r11
00886102  0F 85 5F 02 00 00               jne 0x140886367
00886108  49 8D B5 FF FF 00 00            lea rsi, [r13 + 0xffff]
0088610F  48 C1 EE 10                     shr rsi, 0x10
00886113  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
00886117  0F 10 45 00                     movups xmm0, xmmword ptr [rbp]
0088611B  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00886120  48 83 FE 01                     cmp rsi, 1
00886124  74 0A                           je 0x140886130
00886126  48 3B 75 18                     cmp rsi, qword ptr [rbp + 0x18]
0088612A  72 04                           jb 0x140886130
0088612C  4C 8B 4D 20                     mov r9, qword ptr [rbp + 0x20]
00886130  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00886135  4C 8B 05 4C 92 5A 00            mov r8, qword ptr [rip + 0x5a924c]
0088613C  49 8B C7                        mov rax, r15
0088613F  49 2B C0                        sub rax, r8
00886142  48 C1 E0 13                     shl rax, 0x13
00886146  48 3B D8                        cmp rbx, rax
00886149  0F 86 F0 00 00 00               jbe 0x14088623f
0088614F  4D 85 F6                        test r14, r14
00886152  0F 85 86 01 00 00               jne 0x1408862de
00886158  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0088615D  48 85 DB                        test rbx, rbx
00886160  74 11                           je 0x140886173
00886162  48 8B CB                        mov rcx, rbx
00886165  48 C1 E9 10                     shr rcx, 0x10
00886169  48 3B 4D 28                     cmp rcx, qword ptr [rbp + 0x28]
0088616D  0F 82 79 03 00 00               jb 0x1408864ec
00886173  48 3B F2                        cmp rsi, rdx
00886176  0F 87 C3 00 00 00               ja 0x14088623f
0088617C  49 69 C0 00 00 F8 FF            imul rax, r8, -0x80000
00886183  49 8B FF                        mov rdi, r15
00886186  48 C1 E7 13                     shl rdi, 0x13
0088618A  48 03 F8                        add rdi, rax
0088618D  48 C1 EF 10                     shr rdi, 0x10
00886191  45 85 D2                        test r10d, r10d
00886194  0F 85 90 02 00 00               jne 0x14088642a
0088619A  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0088619F  4D 3B E3                        cmp r12, r11
008861A2  0F 85 52 01 00 00               jne 0x1408862fa
008861A8  4D 8B C1                        mov r8, r9
008861AB  48 8B D6                        mov rdx, rsi
008861AE  E8 7D 4D B7 FF                  call 0x1403faf30
008861B3  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
008861B8  48 8B C8                        mov rcx, rax
008861BB  48 83 F8 FF                     cmp rax, -1
008861BF  0F 84 D0 00 00 00               je 0x140886295
008861C5  4C 2B 3D BC 91 5A 00            sub r15, qword ptr [rip + 0x5a91bc]
008861CC  4A 8D 14 F8                     lea rdx, [rax + r15*8]
008861D0  48 C1 E2 10                     shl rdx, 0x10
008861D4  49 3B D6                        cmp rdx, r14
008861D7  0F 82 73 03 00 00               jb 0x140886550
008861DD  48 8B C6                        mov rax, rsi
008861E0  48 C1 E0 10                     shl rax, 0x10
008861E4  48 FF C8                        dec rax
008861E7  48 03 C2                        add rax, rdx
008861EA  48 3B C3                        cmp rax, rbx
008861ED  0F 87 5D 03 00 00               ja 0x140886550
008861F3  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
008861FB  45 85 FF                        test r15d, r15d
008861FE  0F 85 58 02 00 00               jne 0x14088645c
00886204  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0088620C  48 89 10                        mov qword ptr [rax], rdx
0088620F  33 C0                           xor eax, eax
00886211  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00886219  48 83 C4 60                     add rsp, 0x60
0088621D  41 5F                           pop r15
0088621F  41 5E                           pop r14
00886221  41 5D                           pop r13
00886223  41 5C                           pop r12
00886225  5F                              pop rdi
00886226  5E                              pop rsi
00886227  5D                              pop rbp
00886228  C3                              ret
00886229  CC                              int3
0088622A  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0088622F  48 2B C8                        sub rcx, rax
00886232  48 C1 E9 10                     shr rcx, 0x10
00886236  48 3B D1                        cmp rdx, rcx
00886239  0F 87 D7 02 00 00               ja 0x140886516
0088623F  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
00886247  48 8B B4 24 C8 00 00 00         mov rsi, qword ptr [rsp + 0xc8]
0088624F  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00886257  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0088625F  C7 00 00 00 00 00               mov dword ptr [rax], 0
00886265  45 85 FF                        test r15d, r15d
00886268  0F 85 5D 02 00 00               jne 0x1408864cb
0088626E  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
00886272  49 8B FE                        mov rdi, r14
00886275  49 3B CE                        cmp rcx, r14
00886278  48 0F 47 F9                     cmova rdi, rcx
0088627C  48 3B FB                        cmp rdi, rbx
0088627F  0F 87 F9 01 00 00               ja 0x14088647e
00886285  0F 82 06 01 00 00               jb 0x140886391
0088628B  B8 17 00 00 C0                  mov eax, 0xc0000017
00886290  E9 7C FF FF FF                  jmp 0x140886211
00886295  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0088629D  4C 8B CB                        mov r9, rbx
008862A0  4D 8B C6                        mov r8, r14
008862A3  48 8B D6                        mov rdx, rsi
008862A6  48 8B CD                        mov rcx, rbp
008862A9  E8 C6 02 00 00                  call 0x140886574
008862AE  85 C0                           test eax, eax
008862B0  0F 85 7F 02 00 00               jne 0x140886535
008862B6  45 85 FF                        test r15d, r15d
008862B9  75 D0                           jne 0x14088628b
008862BB  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008862C3  41 BB 00 00 01 00               mov r11d, 0x10000
008862C9  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
008862D1  48 8B B4 24 C8 00 00 00         mov rsi, qword ptr [rsp + 0xc8]
008862D9  44 89 38                        mov dword ptr [rax], r15d
008862DC  EB 90                           jmp 0x14088626e
008862DE  49 8D 8E FF FF 3F 00            lea rcx, [r14 + 0x3fffff]
008862E5  48 81 E1 00 00 C0 FF            and rcx, 0xffffffffffc00000
008862EC  48 3B C8                        cmp rcx, rax
008862EF  0F 86 63 FE FF FF               jbe 0x140886158
008862F5  E9 30 FF FF FF                  jmp 0x14088622a
008862FA  4C 8B C6                        mov r8, rsi
008862FD  49 8B D4                        mov rdx, r12
00886300  E8 6B 14 00 00                  call 0x140887770
00886305  E9 AE FE FF FF                  jmp 0x1408861b8
0088630A  8B 41 40                        mov eax, dword ptr [rcx + 0x40]
0088630D  48 8B 51 30                     mov rdx, qword ptr [rcx + 0x30]
00886311  48 8B 8E 68 03 00 00            mov rcx, qword ptr [rsi + 0x368]
00886318  44 0F B6 C0                     movzx r8d, al
0088631C  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
00886326  48 C1 EA 10                     shr rdx, 0x10
0088632A  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0088632F  4C 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r8
00886337  48 3B C8                        cmp rcx, rax
0088633A  76 15                           jbe 0x140886351
0088633C  0F B6 C2                        movzx eax, dl
0088633F  48 C1 E9 10                     shr rcx, 0x10
00886343  48 8B D1                        mov rdx, rcx
00886346  48 2B D0                        sub rdx, rax
00886349  48 FF CA                        dec rdx
0088634C  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00886351  4D 85 C0                        test r8, r8
00886354  0F 85 96 FD FF FF               jne 0x1408860f0
0088635A  4C 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r10
00886362  E9 89 FD FF FF                  jmp 0x1408860f0
00886367  49 8D 84 24 00 00 E0 FF         lea rax, [r12 - 0x200000]
0088636F  48 3D 00 00 E0 7F               cmp rax, 0x7fe00000
00886375  0F 87 D4 FE FF FF               ja 0x14088624f
0088637B  49 8D 44 24 FF                  lea rax, [r12 - 1]
00886380  49 85 C5                        test r13, rax
00886383  0F 85 C6 FE FF FF               jne 0x14088624f
00886389  49 8B F5                        mov rsi, r13
0088638C  E9 7E FD FF FF                  jmp 0x14088610f
00886391  48 8B C3                        mov rax, rbx
00886394  48 2B C7                        sub rax, rdi
00886397  48 FF C0                        inc rax
0088639A  49 3B C5                        cmp rax, r13
0088639D  0F 82 E8 FE FF FF               jb 0x14088628b
008863A3  48 8B AC 24 D8 00 00 00         mov rbp, qword ptr [rsp + 0xd8]
008863AB  48 8D 8E 58 05 00 00            lea rcx, [rsi + 0x558]
008863B2  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
008863B7  4D 8B C4                        mov r8, r12
008863BA  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
008863BF  49 8B D5                        mov rdx, r13
008863C2  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008863C7  E8 5C FF 19 00                  call 0x140a26328
008863CC  85 C0                           test eax, eax
008863CE  0F 89 3D FE FF FF               jns 0x140886211
008863D4  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
008863DC  B9 00 00 01 00                  mov ecx, 0x10000
008863E1  48 C1 E2 10                     shl rdx, 0x10
008863E5  45 85 FF                        test r15d, r15d
008863E8  48 0F 44 D1                     cmove rdx, rcx
008863EC  49 3B D6                        cmp rdx, r14
008863EF  49 0F 42 D6                     cmovb rdx, r14
008863F3  48 3B D7                        cmp rdx, rdi
008863F6  0F 83 15 FE FF FF               jae 0x140886211
008863FC  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
00886404  48 8D 8E 58 05 00 00            lea rcx, [rsi + 0x558]
0088640B  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
00886410  4D 8B C4                        mov r8, r12
00886413  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00886418  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0088641D  49 8B D5                        mov rdx, r13
00886420  E8 03 FF 19 00                  call 0x140a26328
00886425  E9 E7 FD FF FF                  jmp 0x140886211
0088642A  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00886432  4A 8D 04 0F                     lea rax, [rdi + r9]
00886436  48 3B 44 24 40                  cmp rax, qword ptr [rsp + 0x40]
0088643B  73 09                           jae 0x140886446
0088643D  48 3B C1                        cmp rax, rcx
00886440  0F 83 54 FD FF FF               jae 0x14088619a
00886446  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
0088644E  4C 8B C9                        mov r9, rcx
00886451  C7 00 00 00 00 00               mov dword ptr [rax], 0
00886457  E9 3E FD FF FF                  jmp 0x14088619a
0088645C  48 8D 04 0F                     lea rax, [rdi + rcx]
00886460  48 3B 84 24 C0 00 00 00         cmp rax, qword ptr [rsp + 0xc0]
00886468  0F 82 2F FE FF FF               jb 0x14088629d
0088646E  48 3B 44 24 40                  cmp rax, qword ptr [rsp + 0x40]
00886473  0F 82 8B FD FF FF               jb 0x140886204
00886479  E9 1F FE FF FF                  jmp 0x14088629d
0088647E  8B 86 50 07 00 00               mov eax, dword ptr [rsi + 0x750]
00886484  A8 20                           test al, 0x20
00886486  74 5D                           je 0x1408864e5
00886488  B8 FF FF FF 3F                  mov eax, 0x3fffffff
0088648D  48 3B D8                        cmp rbx, rax
00886490  76 53                           jbe 0x1408864e5
00886492  48 23 F8                        and rdi, rax
00886495  0F 84 C0 00 00 00               je 0x14088655b
0088649B  48 3B FB                        cmp rdi, rbx
0088649E  0F 87 B7 00 00 00               ja 0x14088655b
008864A4  48 3B F9                        cmp rdi, rcx
008864A7  73 11                           jae 0x1408864ba
008864A9  45 85 FF                        test r15d, r15d
008864AC  74 0C                           je 0x1408864ba
008864AE  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
008864B6  48 C1 E7 10                     shl rdi, 0x10
008864BA  49 3B FE                        cmp rdi, r14
008864BD  0F 82 A0 00 00 00               jb 0x140886563
008864C3  48 3B FB                        cmp rdi, rbx
008864C6  E9 BA FD FF FF                  jmp 0x140886285
008864CB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
008864D0  48 C1 E0 10                     shl rax, 0x10
008864D4  48 3B D8                        cmp rbx, rax
008864D7  0F 86 91 FD FF FF               jbe 0x14088626e
008864DD  48 8B D8                        mov rbx, rax
008864E0  E9 89 FD FF FF                  jmp 0x14088626e
008864E5  B8 FF FF FF 00                  mov eax, 0xffffff
008864EA  EB A6                           jmp 0x140886492
008864EC  48 8D 4B 01                     lea rcx, [rbx + 1]
008864F0  48 3B C8                        cmp rcx, rax
008864F3  0F 86 7A FC FF FF               jbe 0x140886173
008864F9  48 2B C8                        sub rcx, rax
008864FC  48 C1 E9 10                     shr rcx, 0x10
00886500  48 3B D1                        cmp rdx, rcx
00886503  0F 86 6A FC FF FF               jbe 0x140886173
00886509  48 8B D1                        mov rdx, rcx
0088650C  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00886511  E9 5D FC FF FF                  jmp 0x140886173
00886516  48 2B D1                        sub rdx, rcx
00886519  C7 07 00 00 00 00               mov dword ptr [rdi], 0
0088651F  48 C1 E9 03                     shr rcx, 3
00886523  4C 03 F9                        add r15, rcx
00886526  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0088652B  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00886530  E9 28 FC FF FF                  jmp 0x14088615d
00886535  4C 8B 94 24 A8 00 00 00         mov r10, qword ptr [rsp + 0xa8]
0088653D  41 BB 00 00 01 00               mov r11d, 0x10000
00886543  48 8B BC 24 E0 00 00 00         mov rdi, qword ptr [rsp + 0xe0]
0088654B  E9 C3 FB FF FF                  jmp 0x140886113
00886550  41 BB 00 00 01 00               mov r11d, 0x10000
00886556  E9 E4 FC FF FF                  jmp 0x14088623f
0088655B  49 8B FB                        mov rdi, r11
0088655E  E9 41 FF FF FF                  jmp 0x1408864a4
00886563  49 8B FE                        mov rdi, r14
00886566  E9 58 FF FF FF                  jmp 0x1408864c3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFindEmptyAddressRange(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned __int8 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;

    v_stack_p8 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (96);
    result = (a6) - (a5);
    result = (result) + 1;
    if (result < a2) goto loc_0088628B;
    v_stack_p10 = 1;
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    *(unsigned int *)(a9) = 1;
    if (((a7) & (2)) != 0) goto loc_0088630A;
    v_r10 = 0;
    a3 = 0;
    a2 = 0;
    v_stack_p10 = 0;
    v_stack_m58 = 0;
    v_stack_p28 = 0;
loc_008860F0:
    if (a4 != 0) goto loc_0088624F;
    if (0 != ((unsigned int)(0x10000ULL))) goto loc_00886367;
loc_0088610F:
    v_rsi = (a2 + 65535) >> (16);
loc_00886113:
    v_stack_m50 = v_xmm0;
    if (v_rsi == 1) goto loc_00886130;
    if (v_rsi >= (*(unsigned __int64 *)(a1 + 24))) {
        a4 = *(unsigned __int64 *)(a1 + 32);
    }
    result = (v_stack_m48) - (*(unsigned __int64 *)(v_rip + 5935692));
    result = (result) << (19);
    if (a6 <= result) goto loc_0088623F;
    if (a5 != 0) goto loc_008862DE;
loc_00886158:
loc_0088615D:
    if (a6 == 0) goto loc_00886173;
    a1 = (a6) >> (16);
    if (a1 < (*(unsigned __int64 *)(a1 + 40))) goto loc_008864EC;
loc_00886173:
    if (v_rsi > v_stack_m50) goto loc_0088623F;
    result = (result) * (*(unsigned __int64 *)(v_rip + 5935692));
    v_rdi = (v_stack_m48) << (19);
    v_rdi = (v_rdi) + (result);
    v_rdi = (v_rdi) >> (16);
    if (0 != 0) goto loc_0088642A;
loc_0088619A:
    if (0 != ((unsigned int)(0x10000ULL))) goto loc_008862FA;
    result = RtlFindClearBitsEx(v_stack_m50, v_rsi, a4, a4);
loc_008861B8:
    if (result == -1) goto loc_00886295;
    v_r15 = (v_stack_m48) - (*(unsigned __int64 *)(v_rip + 5935548));
    a2 = (result + v_r15 * 8) << (16);
    if (a2 < a5) goto loc_00886550;
    result = (v_rsi) << (16);
    result = (result) - 1;
    result = (result) + (a2);
    if (result > a6) goto loc_00886550;
    if ((unsigned int)(v_stack_p10) != 0) goto loc_0088645C;
loc_00886204:
    *(unsigned __int64 *)(a8) = a2;
    result = 0;
loc_00886211:
    v_rsp = (v_rsp) + (96);
    return result;
loc_0088622A:
    a1 = (result) - (0);
    a1 = (a1) >> (16);
    if (v_stack_p48 > a1) goto loc_00886516;
loc_0088623F:
loc_0088624F:
    *(unsigned int *)(a9) = 0;
    if ((unsigned int)(v_stack_pA8) != 0) goto loc_008864CB;
loc_0088626E:
    if ((*(unsigned __int64 *)(a1 + 56)) > a5) { a5 = *(unsigned __int64 *)(a1 + 56); }
    if (a5 > v_stack_p8) goto loc_0088647E;
loc_00886285:
    if (a5 < v_stack_p8) goto loc_00886391;
loc_0088628B:
    goto loc_00886211;
loc_00886295:
loc_0088629D:
    result = MiExpandVadBitMap(a1, a6, a5, v_stack_p8);
    if ((unsigned int)(result) != 0) goto loc_00886535;
    if ((unsigned int)(v_stack_pA8) != 0) goto loc_0088628B;
    *(unsigned int *)(a9) = (unsigned int)(v_stack_pA8);
    goto loc_0088626E;
loc_008862DE:
    a1 = (a5 + 4194303) & (0xFFFFFFFFFFC00000ULL);
    if (a1 <= a9) goto loc_00886158;
    goto loc_0088622A;
loc_008862FA:
    result = MiFindClearVadBitsAligned(a1, 0, a6, v_stack_pB8);
    goto loc_008861B8;
loc_0088630A:
    a2 = (*(unsigned __int64 *)(a1 + 48)) >> (16);
    v_stack_p40 = a2;
    v_stack_pC0 = (unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 64)));
    result = (unsigned int)(*(unsigned int *)(a1 + 64));
    if ((*(unsigned __int64 *)(a6 + 872)) >= = ((unsigned int)(*(unsigned int *)(a1 + 64)))) {
        result = (unsigned __int8)(a2);
        a1 = (*(unsigned __int64 *)(a6 + 872)) >> (16);
        a2 = a1;
        a2 = (a2) - (result);
        a2 = (a2) - 1;
        v_stack_p40 = a2;
    }
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 64))) != 0) goto loc_008860F0;
    v_stack_pC0 = 0;
    goto loc_008860F0;
loc_00886367:
    if ((a3 - 2097152) > 0x7FE00000ULL) goto loc_0088624F;
    if (((a2) & (a3 - 1)) != 0) goto loc_0088624F;
    goto loc_0088610F;
loc_00886391:
    result = (v_stack_p8) - (a5);
    result = (result) + 1;
    if (result < a2) goto loc_0088628B;
    v_stack_p30 = a8;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = a5;
    result = MiFindEmptyAddressRangeInTree(a2 + 1368, a2, 0, v_stack_pB8);
    if (!sign_flag) goto loc_00886211;
    a2 = (a5) << (16);
    if ((unsigned int)(v_stack_pA8) == 0) { a2 = (unsigned int)(0x10000ULL); }
    if (a2 < a5) { a2 = a5; }
    if (a2 >= a5) goto loc_00886211;
    v_stack_p30 = a8;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = a2;
    result = MiFindEmptyAddressRangeInTree(a2 + 1368, a2, 0, v_stack_pB8);
    goto loc_00886211;
loc_0088642A:
    if ((a5 + v_stack_pB8 * 1) >= v_stack_p40) goto loc_00886446;
    if ((a5 + v_stack_pB8 * 1) >= a5) goto loc_0088619A;
loc_00886446:
    *(unsigned int *)(a9) = 0;
    goto loc_0088619A;
loc_0088645C:
    if ((a5 + a5 * 1) < a5) goto loc_0088629D;
    if ((a5 + a5 * 1) < v_stack_p40) goto loc_00886204;
    goto loc_0088629D;
loc_0088647E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 1872)))) & (32)) == 0) goto loc_008864E5;
    if (v_stack_p8 <= ((unsigned int)(0x3FFFFFFFULL))) goto loc_008864E5;
loc_00886492:
    v_rdi = (a5) & ((unsigned int)(0x3FFFFFFFULL));
    if (condition_is_equal) goto loc_0088655B;
    if (v_rdi > v_stack_p8) goto loc_0088655B;
loc_008864A4:
    if (v_rdi >= a5) goto loc_008864BA;
    if ((unsigned int)(v_stack_pA8) != 0) {
        v_rdi = a5;
        v_rdi = (v_rdi) << (16);
    }
    if (v_rdi < a5) goto loc_00886563;
loc_008864C3:
    goto loc_00886285;
loc_008864CB:
    result = (v_stack_p40) << (16);
    if (v_stack_p8 <= result) goto loc_0088626E;
    goto loc_0088626E;
loc_008864E5:
    goto loc_00886492;
loc_008864EC:
    if ((result + 1) <= ((unsigned int)(0xFFFFFFULL))) goto loc_00886173;
    a1 = (result + 1) - ((unsigned int)(0xFFFFFFULL));
    a1 = (a1) >> (16);
    if (a2 <= a1) goto loc_00886173;
    v_stack_p48 = a1;
    goto loc_00886173;
loc_00886516:
    a2 = (a1) - (a1);
    *(unsigned int *)(v_rdi) = 0;
    a1 = (a1) >> (3);
    v_r15 = (v_stack_pA8) + (a1);
    v_stack_p48 = a2;
    v_stack_p50 = v_r15;
    goto loc_0088615D;
loc_00886535:
    goto loc_00886113;
loc_00886550:
    goto loc_0088623F;
loc_0088655B:
    goto loc_008864A4;
loc_00886563:
    goto loc_008864C3;
}
```

## 5. (Beta) C Style

```c
int64_t MiFindEmptyAddressRange(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint8_t Arg7, void *Arg8, void *Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;

    v_stack_p8 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (96);
    result = (Arg6) - (Arg5);
    result = (result) + 1;
    if (result < Arg2) goto loc_0088628B;
    v_stack_p10 = 1;
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    *(uint32_t *)(arg9) = 1;
    if (((Arg7) & (2)) != 0) goto loc_0088630A;
    local_r10 = 0;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_p10 = 0;
    v_stack_m58 = 0;
    v_stack_p28 = 0;
loc_008860F0:
    if (Arg4 != 0) goto loc_0088624F;
    if (0 != ((uint32_t)(0x10000ULL))) goto loc_00886367;
loc_0088610F:
    local_rsi = (Arg2 + 65535) >> (16);
loc_00886113:
    v_stack_m50 = v_xmm0;
    if (local_rsi == 1) goto loc_00886130;
    if (local_rsi >= (*(uint64_t *)(arg1 + 0x18))) {
        Arg4 = *(uint64_t *)(arg1 + 0x20);
    }
    result = (v_stack_m48) - (*(uint64_t *)(v_rip + 0x5A924C));
    result = (result) << (19);
    if (Arg6 <= result) goto loc_0088623F;
    if (Arg5 != 0) goto loc_008862DE;
loc_00886158:
loc_0088615D:
    if (Arg6 == 0) goto loc_00886173;
    Arg1 = (Arg6) >> (16);
    if (Arg1 < (*(uint64_t *)(arg1 + 0x28))) goto loc_008864EC;
loc_00886173:
    if (local_rsi > v_stack_m50) goto loc_0088623F;
    result = (result) * (*(uint64_t *)(v_rip + 0x5A924C));
    local_rdi = (v_stack_m48) << (19);
    local_rdi = (local_rdi) + (result);
    local_rdi = (local_rdi) >> (16);
    if (0 != 0) goto loc_0088642A;
loc_0088619A:
    if (0 != ((uint32_t)(0x10000ULL))) goto loc_008862FA;
    result = RtlFindClearBitsEx(v_stack_m50, local_rsi, Arg4, Arg4);
loc_008861B8:
    if (result == -1) goto loc_00886295;
    local_r15 = (v_stack_m48) - (*(uint64_t *)(v_rip + 0x5A91BC));
    Arg2 = (result + local_r15 * 8) << (16);
    if (Arg2 < Arg5) goto loc_00886550;
    result = (local_rsi) << (16);
    result = (result) - 1;
    result = (result) + (Arg2);
    if (result > Arg6) goto loc_00886550;
    if ((uint32_t)(v_stack_p10) != 0) goto loc_0088645C;
loc_00886204:
    *(void **)(arg8) = Arg2;
    result = 0;
loc_00886211:
    local_rsp = (local_rsp) + (96);
    return result;
loc_0088622A:
    Arg1 = (result) - (0);
    Arg1 = (Arg1) >> (16);
    if (v_stack_p48 > Arg1) goto loc_00886516;
loc_0088623F:
loc_0088624F:
    *(uint32_t *)(arg9) = 0;
    if ((uint32_t)(v_stack_pA8) != 0) goto loc_008864CB;
loc_0088626E:
    if ((*(uint64_t *)(arg1 + 0x38)) > Arg5) { Arg5 = *(uint64_t *)(arg1 + 0x38); }
    if (Arg5 > v_stack_p8) goto loc_0088647E;
loc_00886285:
    if (Arg5 < v_stack_p8) goto loc_00886391;
loc_0088628B:
    goto loc_00886211;
loc_00886295:
loc_0088629D:
    result = MiExpandVadBitMap(Arg1, Arg6, Arg5, v_stack_p8);
    if ((uint32_t)(result) != 0) goto loc_00886535;
    if ((uint32_t)(v_stack_pA8) != 0) goto loc_0088628B;
    *(uint32_t *)(arg9) = (uint32_t)(v_stack_pA8);
    goto loc_0088626E;
loc_008862DE:
    Arg1 = (Arg5 + 4194303) & (0xFFFFFFFFFFC00000ULL);
    if (Arg1 <= Arg9) goto loc_00886158;
    goto loc_0088622A;
loc_008862FA:
    result = MiFindClearVadBitsAligned(Arg1, 0, Arg6, v_stack_pB8);
    goto loc_008861B8;
loc_0088630A:
    Arg2 = (*(uint64_t *)(arg1 + 0x30)) >> (16);
    v_stack_p40 = Arg2;
    v_stack_pC0 = (uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x40));
    if ((*(uint64_t *)(Arg6 + 0x368)) >= = ((uint32_t)(*(uint32_t *)(arg1 + 0x40)))) {
        result = (uint8_t)(Arg2);
        Arg1 = (*(uint64_t *)(Arg6 + 0x368)) >> (16);
        Arg2 = Arg1;
        Arg2 = (Arg2) - (result);
        Arg2 = (Arg2) - 1;
        v_stack_p40 = Arg2;
    }
    if ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))) != 0) goto loc_008860F0;
    v_stack_pC0 = 0;
    goto loc_008860F0;
loc_00886367:
    if ((Arg3 - 2097152) > 0x7FE00000ULL) goto loc_0088624F;
    if (((Arg2) & (Arg3 - 1)) != 0) goto loc_0088624F;
    goto loc_0088610F;
loc_00886391:
    result = (v_stack_p8) - (Arg5);
    result = (result) + 1;
    if (result < Arg2) goto loc_0088628B;
    v_stack_p30 = Arg8;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = Arg5;
    result = MiFindEmptyAddressRangeInTree(Arg2 + 1368, Arg2, 0, v_stack_pB8);
    if (!sign_flag) goto loc_00886211;
    Arg2 = (Arg5) << (16);
    if ((uint32_t)(v_stack_pA8) == 0) { Arg2 = (uint32_t)(0x10000ULL); }
    if (Arg2 < Arg5) { Arg2 = Arg5; }
    if (Arg2 >= Arg5) goto loc_00886211;
    v_stack_p30 = Arg8;
    v_stack_p28 = v_stack_p8;
    v_stack_p20 = Arg2;
    result = MiFindEmptyAddressRangeInTree(Arg2 + 1368, Arg2, 0, v_stack_pB8);
    goto loc_00886211;
loc_0088642A:
    if ((Arg5 + v_stack_pB8 * 1) >= v_stack_p40) goto loc_00886446;
    if ((Arg5 + v_stack_pB8 * 1) >= Arg5) goto loc_0088619A;
loc_00886446:
    *(uint32_t *)(arg9) = 0;
    goto loc_0088619A;
loc_0088645C:
    if ((Arg5 + Arg5 * 1) < Arg5) goto loc_0088629D;
    if ((Arg5 + Arg5 * 1) < v_stack_p40) goto loc_00886204;
    goto loc_0088629D;
loc_0088647E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x750)))) & (32)) == 0) goto loc_008864E5;
    if (v_stack_p8 <= ((uint32_t)(0x3FFFFFFFULL))) goto loc_008864E5;
loc_00886492:
    local_rdi = (Arg5) & ((uint32_t)(0x3FFFFFFFULL));
    if (condition_is_equal) goto loc_0088655B;
    if (local_rdi > v_stack_p8) goto loc_0088655B;
loc_008864A4:
    if (local_rdi >= Arg5) goto loc_008864BA;
    if ((uint32_t)(v_stack_pA8) != 0) {
        local_rdi = Arg5;
        local_rdi = (local_rdi) << (16);
    }
    if (local_rdi < Arg5) goto loc_00886563;
loc_008864C3:
    goto loc_00886285;
loc_008864CB:
    result = (v_stack_p40) << (16);
    if (v_stack_p8 <= result) goto loc_0088626E;
    goto loc_0088626E;
loc_008864E5:
    goto loc_00886492;
loc_008864EC:
    if ((result + 1) <= ((uint32_t)(0xFFFFFFULL))) goto loc_00886173;
    Arg1 = (result + 1) - ((uint32_t)(0xFFFFFFULL));
    Arg1 = (Arg1) >> (16);
    if (Arg2 <= Arg1) goto loc_00886173;
    v_stack_p48 = Arg1;
    goto loc_00886173;
loc_00886516:
    Arg2 = (Arg1) - (Arg1);
    *(uint32_t *)(local_rdi) = 0;
    Arg1 = (Arg1) >> (3);
    local_r15 = (v_stack_pA8) + (Arg1);
    v_stack_p48 = Arg2;
    v_stack_p50 = local_r15;
    goto loc_0088615D;
loc_00886535:
    goto loc_00886113;
loc_00886550:
    goto loc_0088623F;
loc_0088655B:
    goto loc_008864A4;
loc_00886563:
    goto loc_008864C3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0xFFFF` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `W` |
| `Arg9` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00886050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
