# VrpPostOpenOrCreate

- RVA: `0x00936510`–`0x009368C7` (길이 `951` bytes)
- VA: `0x0000000140936510`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008F35C`
- 디코드: `253`개 명령, `951/951` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00936550` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (function, `0x0041E720`)
- `0x009365C2` → [VrpAllocateKeyContext](VrpAllocateKeyContext_function_00937204.md) (function, `0x00937204`)
- `0x009365E0` → [VrpBuildKeyPath](VrpBuildKeyPath_function_00934650.md) (function, `0x00934650`)
- `0x009365FD` → [VrpCountPathComponents](VrpCountPathComponents_function_009358F0.md) (function, `0x009358F0`)
- `0x0093661D` → [CmSetCallbackObjectContext](CmSetCallbackObjectContext_function_009368D0.md) (function, `0x009368D0`)
- `0x00936646` → [CmAllocateExtraParameter](CmAllocateExtraParameter_function_009370D8.md) (function, `0x009370D8`)
- `0x00936664` → [VrpBuildKeyPath](VrpBuildKeyPath_function_00934650.md) (function, `0x00934650`)
- `0x00936683` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x009366C5` → [VrpAllocateKeyContext](VrpAllocateKeyContext_function_00937204.md) (function, `0x00937204`)
- `0x009366E3` → [VrpBuildKeyPath](VrpBuildKeyPath_function_00934650.md) (function, `0x00934650`)
- `0x00936727` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00936761` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00936772` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0093677D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00936793` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009367F0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0093689B` → [CmpFreeExtraParameter](../87/CmpFreeExtraParameter_function_00876894.md) (function, `0x00876894`)

### Direct callers
- [VrpRegistryCallback](../86/VrpRegistryCallback_function_00867450.md) at `0x00867527`

### Static image references
- `0x0093652C` → RVA `0x00E0A740` (`.data`; read)
- `0x00936610` → RVA `0x00EF02C8` (`.data`; read)
- `0x00936748` → RVA `0x00E0A630` (`.data`; read)
- `0x009367FE` → RVA `0x00011F68` (`.rdata`; read)
- `0x0093680B` → RVA `0x00011F70` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00936550` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (`PAGE` → `.text`)
  - `0x00936683` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00936727` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00936761` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00936772` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0093677D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00936793` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009367F0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x009365EC` → [sub_00B24D7E](../B2/Unknown_function_00B24D7E.md) (`tail-transfer`)
  - `0x0093662F` → [sub_00B24D7E](../B2/Unknown_function_00B24D7E.md) (`tail-transfer`)
  - `0x00936670` → [sub_00B24D7E](../B2/Unknown_function_00B24D7E.md) (`tail-transfer`)
  - `0x009366EF` → [sub_00B24D7E](../B2/Unknown_function_00B24D7E.md) (`tail-transfer`)
  - `0x0093674F` → [sub_00B24D7E + 0xA9](../B2/Unknown_function_00B24D7E.md) (`tail-transfer`)
  - `0x00936851` → [sub_00B24D7E](../B2/Unknown_function_00B24D7E.md) (`tail-transfer`)
  - `0x009368B5` → [sub_00B24D7E](../B2/Unknown_function_00B24D7E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00936510  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00936515  55                              push rbp
00936516  56                              push rsi
00936517  57                              push rdi
00936518  41 54                           push r12
0093651A  41 55                           push r13
0093651C  41 56                           push r14
0093651E  41 57                           push r15
00936520  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00936525  48 81 EC B0 00 00 00            sub rsp, 0xb0
0093652C  48 8B 05 0D 42 4D 00            mov rax, qword ptr [rip + 0x4d420d]
00936533  48 33 C4                        xor rax, rsp
00936536  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0093653A  4C 8B EA                        mov r13, rdx
0093653D  48 8B D9                        mov rbx, rcx
00936540  0F 57 C0                        xorps xmm0, xmm0
00936543  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00936547  B9 03 00 00 00                  mov ecx, 3
0093654C  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
00936550  E8 CB 81 AE FF                  call 0x14041e720
00936555  48 8B 33                        mov rsi, qword ptr [rbx]
00936558  45 33 C9                        xor r9d, r9d
0093655B  48 89 75 AF                     mov qword ptr [rbp - 0x51], rsi
0093655F  45 8B F1                        mov r14d, r9d
00936562  45 8B F9                        mov r15d, r9d
00936565  8B 56 08                        mov edx, dword ptr [rsi + 8]
00936568  48 8B 7E 20                     mov rdi, qword ptr [rsi + 0x20]
0093656C  4C 8B 66 10                     mov r12, qword ptr [rsi + 0x10]
00936570  85 D2                           test edx, edx
00936572  0F 88 85 01 00 00               js 0x1409366fd
00936578  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0093657C  41 8B F1                        mov esi, r9d
0093657F  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00936583  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
00936587  49 8B 00                        mov rax, qword ptr [r8]
0093658A  49 3B C0                        cmp rax, r8
0093658D  0F 85 67 02 00 00               jne 0x1409367fa
00936593  B8 34 00 00 C0                  mov eax, 0xc0000034
00936598  48 83 C6 30                     add rsi, 0x30
0093659C  85 C0                           test eax, eax
0093659E  49 0F 48 F1                     cmovs rsi, r9
009365A2  81 FA 04 01 00 00               cmp edx, 0x104
009365A8  0F 84 54 01 00 00               je 0x140936702
009365AE  81 FA 68 03 00 00               cmp edx, 0x368
009365B4  74 7E                           je 0x140936634
009365B6  48 85 F6                        test rsi, rsi
009365B9  0F 84 03 01 00 00               je 0x1409366c2
009365BF  48 8B 0E                        mov rcx, qword ptr [rsi]
009365C2  E8 3D 0C 00 00                  call 0x140937204
009365C7  45 33 C9                        xor r9d, r9d
009365CA  4C 8B F0                        mov r14, rax
009365CD  48 85 C0                        test rax, rax
009365D0  0F 84 DA 02 00 00               je 0x1409368b0
009365D6  4C 8D 40 10                     lea r8, [rax + 0x10]
009365DA  33 C9                           xor ecx, ecx
009365DC  48 8D 56 10                     lea rdx, [rsi + 0x10]
009365E0  E8 6B E0 FF FF                  call 0x140934650
009365E5  45 33 C9                        xor r9d, r9d
009365E8  8B D8                           mov ebx, eax
009365EA  85 C0                           test eax, eax
009365EC  0F 88 8C E7 1E 00               js 0x140b24d7e
009365F2  8B 46 08                        mov eax, dword ptr [rsi + 8]
009365F5  49 8D 4E 10                     lea rcx, [r14 + 0x10]
009365F9  41 89 46 24                     mov dword ptr [r14 + 0x24], eax
009365FD  E8 EE F2 FF FF                  call 0x1409358f0
00936602  66 41 89 46 20                  mov word ptr [r14 + 0x20], ax
00936607  4C 8D 4D A7                     lea r9, [rbp - 0x59]
0093660B  49 8B 4C 24 48                  mov rcx, qword ptr [r12 + 0x48]
00936610  48 8D 15 B1 9C 5B 00            lea rdx, [rip + 0x5b9cb1]
00936617  4D 8B C6                        mov r8, r14
0093661A  48 8B 09                        mov rcx, qword ptr [rcx]
0093661D  E8 AE 02 00 00                  call 0x1409368d0
00936622  45 33 C9                        xor r9d, r9d
00936625  8B D8                           mov ebx, eax
00936627  85 C0                           test eax, eax
00936629  0F 89 DF 00 00 00               jns 0x14093670e
0093662F  E9 4A E7 1E 00                  jmp 0x140b24d7e
00936634  48 85 F6                        test rsi, rsi
00936637  0F 85 CE 00 00 00               jne 0x14093670b
0093663D  48 85 FF                        test rdi, rdi
00936640  0F 84 62 02 00 00               je 0x1409368a8
00936646  E8 8D 0A 00 00                  call 0x1409370d8
0093664B  45 33 C9                        xor r9d, r9d
0093664E  4C 8B F8                        mov r15, rax
00936651  48 85 C0                        test rax, rax
00936654  0F 84 56 02 00 00               je 0x1409368b0
0093665A  4C 8D 40 10                     lea r8, [rax + 0x10]
0093665E  33 C9                           xor ecx, ecx
00936660  48 8D 57 30                     lea rdx, [rdi + 0x30]
00936664  E8 E7 DF FF FF                  call 0x140934650
00936669  45 33 C9                        xor r9d, r9d
0093666C  8B D8                           mov ebx, eax
0093666E  85 C0                           test eax, eax
00936670  0F 88 08 E7 1E 00               js 0x140b24d7e
00936676  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0093667A  41 BD 56 52 65 67               mov r13d, 0x67655256
00936680  41 8B D5                        mov edx, r13d
00936683  E8 88 A0 8D FF                  call 0x140210710
00936688  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0093668C  49 8D 4F D0                     lea rcx, [r15 - 0x30]
00936690  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00936694  49 89 07                        mov qword ptr [r15], rax
00936697  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
0093669A  41 89 47 08                     mov dword ptr [r15 + 8], eax
0093669E  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
009366A2  4C 8B 0A                        mov r9, qword ptr [rdx]
009366A5  4C 3B CA                        cmp r9, rdx
009366A8  0F 85 7C 01 00 00               jne 0x14093682a
009366AE  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
009366B2  48 39 10                        cmp qword ptr [rax], rdx
009366B5  0F 84 9B 01 00 00               je 0x140936856
009366BB  B9 03 00 00 00                  mov ecx, 3
009366C0  CD 29                           int 0x29
009366C2  49 8B CD                        mov rcx, r13
009366C5  E8 3A 0B 00 00                  call 0x140937204
009366CA  45 33 C9                        xor r9d, r9d
009366CD  4C 8B F0                        mov r14, rax
009366D0  48 85 C0                        test rax, rax
009366D3  0F 84 D7 01 00 00               je 0x1409368b0
009366D9  4C 8D 40 10                     lea r8, [rax + 0x10]
009366DD  33 C9                           xor ecx, ecx
009366DF  48 8D 57 30                     lea rdx, [rdi + 0x30]
009366E3  E8 68 DF FF FF                  call 0x140934650
009366E8  45 33 C9                        xor r9d, r9d
009366EB  8B D8                           mov ebx, eax
009366ED  85 C0                           test eax, eax
009366EF  0F 88 89 E6 1E 00               js 0x140b24d7e
009366F5  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
009366F8  E9 F8 FE FF FF                  jmp 0x1409365f5
009366FD  41 8B D9                        mov ebx, r9d
00936700  EB 10                           jmp 0x140936712
00936702  48 85 F6                        test rsi, rsi
00936705  0F 85 64 01 00 00               jne 0x14093686f
0093670B  41 8B D9                        mov ebx, r9d
0093670E  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
00936712  48 85 FF                        test rdi, rdi
00936715  74 6B                           je 0x140936782
00936717  41 BD 56 52 65 67               mov r13d, 0x67655256
0093671D  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
00936722  48 85 C9                        test rcx, rcx
00936725  74 08                           je 0x14093672f
00936727  E8 24 2C 9C FF                  call 0x1402f9350
0093672C  45 33 C9                        xor r9d, r9d
0093672F  48 8B 07                        mov rax, qword ptr [rdi]
00936732  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
00936736  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
0093673B  4C 89 0F                        mov qword ptr [rdi], r9
0093673E  8B 46 08                        mov eax, dword ptr [rsi + 8]
00936741  3D 04 01 00 00                  cmp eax, 0x104
00936746  75 6C                           jne 0x1409367b4
00936748  83 3D E1 3E 4D 00 05            cmp dword ptr [rip + 0x4d3ee1], 5
0093674F  0F 87 D2 E6 1E 00               ja 0x140b24e27
00936755  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
00936759  48 85 C9                        test rcx, rcx
0093675C  74 08                           je 0x140936766
0093675E  41 8B D5                        mov edx, r13d
00936761  E8 0A C1 24 00                  call 0x140b82870
00936766  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0093676A  48 85 C9                        test rcx, rcx
0093676D  74 08                           je 0x140936777
0093676F  41 8B D5                        mov edx, r13d
00936772  E8 F9 C0 24 00                  call 0x140b82870
00936777  41 8B D5                        mov edx, r13d
0093677A  48 8B CF                        mov rcx, rdi
0093677D  E8 EE C0 24 00                  call 0x140b82870
00936782  85 DB                           test ebx, ebx
00936784  0F 88 30 01 00 00               js 0x1409368ba
0093678A  8B C3                           mov eax, ebx
0093678C  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00936790  48 33 CC                        xor rcx, rsp
00936793  E8 A8 5E D7 FF                  call 0x1406ac640
00936798  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
009367A0  48 81 C4 B0 00 00 00            add rsp, 0xb0
009367A7  41 5F                           pop r15
009367A9  41 5E                           pop r14
009367AB  41 5D                           pop r13
009367AD  41 5C                           pop r12
009367AF  5F                              pop rdi
009367B0  5E                              pop rsi
009367B1  5D                              pop rbp
009367B2  C3                              ret
009367B3  CC                              int3
009367B4  3D 68 03 00 00                  cmp eax, 0x368
009367B9  74 8D                           je 0x140936748
009367BB  49 8B 04 24                     mov rax, qword ptr [r12]
009367BF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009367C3  48 85 C9                        test rcx, rcx
009367C6  75 26                           jne 0x1409367ee
009367C8  49 8B 04 24                     mov rax, qword ptr [r12]
009367CC  0F 10 47 10                     movups xmm0, xmmword ptr [rdi + 0x10]
009367D0  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
009367D4  49 8B 44 24 70                  mov rax, qword ptr [r12 + 0x70]
009367D9  0F 10 4F 20                     movups xmm1, xmmword ptr [rdi + 0x20]
009367DD  F3 0F 7F 08                     movdqu xmmword ptr [rax], xmm1
009367E1  4C 89 4F 18                     mov qword ptr [rdi + 0x18], r9
009367E5  4C 89 4F 28                     mov qword ptr [rdi + 0x28], r9
009367E9  E9 67 FF FF FF                  jmp 0x140936755
009367EE  33 D2                           xor edx, edx
009367F0  E8 7B C0 24 00                  call 0x140b82870
009367F5  45 33 C9                        xor r9d, r9d
009367F8  EB CE                           jmp 0x1409367c8
009367FA  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
009367FE  48 2B 0D 63 B7 6D FF            sub rcx, qword ptr [rip - 0x92489d]
00936805  75 0B                           jne 0x140936812
00936807  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
0093680B  48 2B 0D 5E B7 6D FF            sub rcx, qword ptr [rip - 0x9248a2]
00936812  48 85 C9                        test rcx, rcx
00936815  74 08                           je 0x14093681f
00936817  48 8B 00                        mov rax, qword ptr [rax]
0093681A  E9 6B FD FF FF                  jmp 0x14093658a
0093681F  48 8B F0                        mov rsi, rax
00936822  41 8B C1                        mov eax, r9d
00936825  E9 6E FD FF FF                  jmp 0x140936598
0093682A  4D 8B 41 10                     mov r8, qword ptr [r9 + 0x10]
0093682E  4C 2B 41 10                     sub r8, qword ptr [rcx + 0x10]
00936832  75 08                           jne 0x14093683c
00936834  4D 8B 41 18                     mov r8, qword ptr [r9 + 0x18]
00936838  4C 2B 41 18                     sub r8, qword ptr [rcx + 0x18]
0093683C  4D 85 C0                        test r8, r8
0093683F  74 08                           je 0x140936849
00936841  4D 8B 09                        mov r9, qword ptr [r9]
00936844  E9 5C FE FF FF                  jmp 0x1409366a5
00936849  BB 35 00 00 C0                  mov ebx, 0xc0000035
0093684E  45 33 C9                        xor r9d, r9d
00936851  E9 28 E5 1E 00                  jmp 0x140b24d7e
00936856  48 89 11                        mov qword ptr [rcx], rdx
00936859  45 33 C9                        xor r9d, r9d
0093685C  48 89 41 08                     mov qword ptr [rcx + 8], rax
00936860  41 8B D9                        mov ebx, r9d
00936863  48 89 08                        mov qword ptr [rax], rcx
00936866  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0093686A  E9 AE FE FF FF                  jmp 0x14093671d
0093686F  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00936873  48 8B 11                        mov rdx, qword ptr [rcx]
00936876  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
0093687A  0F 85 3B FE FF FF               jne 0x1409366bb
00936880  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00936884  48 39 08                        cmp qword ptr [rax], rcx
00936887  0F 85 2E FE FF FF               jne 0x1409366bb
0093688D  48 89 10                        mov qword ptr [rax], rdx
00936890  48 89 42 08                     mov qword ptr [rdx + 8], rax
00936894  4C 89 09                        mov qword ptr [rcx], r9
00936897  4C 89 49 08                     mov qword ptr [rcx + 8], r9
0093689B  E8 F4 FF F3 FF                  call 0x140876894
009368A0  45 33 C9                        xor r9d, r9d
009368A3  E9 63 FE FF FF                  jmp 0x14093670b
009368A8  41 8B D9                        mov ebx, r9d
009368AB  E9 DA FE FF FF                  jmp 0x14093678a
009368B0  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009368B5  E9 C4 E4 1E 00                  jmp 0x140b24d7e
009368BA  89 5E 18                        mov dword ptr [rsi + 0x18], ebx
009368BD  BB 03 05 00 C0                  mov ebx, 0xc0000503
009368C2  E9 C3 FE FF FF                  jmp 0x14093678a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpPostOpenOrCreate(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 5063181)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mA8 = v_xmm0;
    result = EtwActivityIdControl(3, v_stack_mA8, a3, a4);
    a4 = 0;
    v_stack_mB0 = *(unsigned __int64 *)(a1);
    if (sign_flag) goto loc_009366FD;
    v_stack_mB8 = *(unsigned __int64 *)(a1 + 8);
loc_0093658A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 16))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 16))) goto loc_009367FA;
loc_00936598:
    v_rsi = (0) + (48);
    if (sign_flag) { v_rsi = 0; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)))) == 260) goto loc_00936702;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)))) == 872) goto loc_00936634;
    if (v_rsi == 0) goto loc_009366C2;
    result = VrpAllocateKeyContext(*(unsigned __int64 *)(v_rsi), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 16), a4);
    a4 = 0;
    if (result == 0) goto loc_009368B0;
    a1 = 0;
    result = VrpBuildKeyPath(a1, v_rsi + 16, result + 16, a4);
    a4 = 0;
loc_009365F5:
    *(unsigned int *)(result + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 8)));
    result = VrpCountPathComponents(result + 16, v_rsi + 16, result + 16, a4);
    *(unsigned __int16 *)(result + 32) = (unsigned __int16)(result);
    result = CmSetCallbackObjectContext(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) + 72)), v_rip + 6003889, result, v_stack_mB8);
    a4 = 0;
    if (!sign_flag) goto loc_0093670E;
loc_00936634:
    if (v_rsi != 0) goto loc_0093670B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) == 0) goto loc_009368A8;
    result = CmAllocateExtraParameter(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) + 72)), v_rip + 6003889, result, a4);
    a4 = 0;
    if (result == 0) goto loc_009368B0;
    a1 = 0;
    result = VrpBuildKeyPath(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 48, result + 16, a4);
    a4 = 0;
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 8), (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), result + 16, a4);
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 8);
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 64)));
loc_009366A5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 16))) != (*(unsigned __int64 *)(v_stack_mB8 + 16))) goto loc_0093682A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 16) + 8))) == (*(unsigned __int64 *)(v_stack_mB8 + 16))) goto loc_00936856;
loc_009366BB:
loc_009366C2:
    result = VrpAllocateKeyContext((unsigned int)(0x67655256ULL), *(unsigned __int64 *)(v_stack_mB8 + 16), result + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 16)));
    a4 = 0;
    if (result == 0) goto loc_009368B0;
    a1 = 0;
    result = VrpBuildKeyPath(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 48, result + 16, a4);
    a4 = 0;
    goto loc_009365F5;
loc_009366FD:
    goto loc_00936712;
loc_00936702:
    if (v_rsi != 0) goto loc_0093686F;
loc_0093670B:
loc_0093670E:
loc_00936712:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) == 0) goto loc_00936782;
loc_0093671D:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 64));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) + 8) != 0) {
        result = ObfDereferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 48, result + 16, a4);
        a4 = 0;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32)) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 8)))) != 260) goto loc_009367B4;
loc_00936748:
loc_00936755:
    result = (unsigned int)(*(unsigned int *)(v_stack_mB0 + 8));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 56) != 0) {
        a2 = (unsigned int)((unsigned int)(0x67655256ULL));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 56), a2, result + 16, a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 24) != 0) {
        a2 = (unsigned int)((unsigned int)(0x67655256ULL));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 24), a2, result + 16, a4);
    }
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32), (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), result + 16, a4);
loc_00936782:
    if (sign_flag) goto loc_009368BA;
loc_0093678A:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), result + 16, a4);
    v_rsp = (v_rsp) + (176);
    return result;
loc_009367B4:
    if (((unsigned int)(result)) == 872) goto loc_00936748;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16)) + 8) != 0) goto loc_009367EE;
loc_009367C8:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16))) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) + 112)) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 24) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32) + 40) = 0;
    goto loc_00936755;
loc_009367EE:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16)) + 8), a2, result + 16, a4);
    a4 = 0;
    goto loc_009367C8;
loc_009367FA:
    a1 = (*(unsigned __int64 *)(result + 16)) - (*(unsigned __int64 *)(v_rip - 9586845));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(result + 24);
        a1 = (a1) - (*(unsigned __int64 *)(v_rip - 9586850));
    }
    if (a1 == 0) goto loc_0093681F;
    goto loc_0093658A;
loc_0093681F:
    goto loc_00936598;
loc_0093682A:
    a3 = (*(unsigned __int64 *)(a4 + 16)) - (*(unsigned __int64 *)(a1 + 16));
    if (!(condition_is_not_equal)) {
        a3 = *(unsigned __int64 *)(a4 + 24);
        a3 = (a3) - (*(unsigned __int64 *)(a1 + 24));
    }
    if (a3 == 0) goto loc_00936849;
    goto loc_009366A5;
loc_00936849:
    a4 = 0;
loc_00936856:
    *(unsigned __int64 *)(a1) = 0;
    a4 = 0;
    *(unsigned __int64 *)(a1 + 8) = 0;
    *(unsigned __int64 *)(0) = a1;
    *(unsigned __int64 *)(a2 + 8) = a1;
    goto loc_0093671D;
loc_0093686F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48) + 8)) != (*(unsigned __int64 *)(result) - 48)) goto loc_009366BB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48 + 8))) != (*(unsigned __int64 *)(result) - 48)) goto loc_009366BB;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48 + 8) = 0;
    result = CmpFreeExtraParameter(*(unsigned __int64 *)(result) - 48, *(unsigned __int64 *)(*(unsigned __int64 *)(result) - 48), a3, a4);
    a4 = 0;
    goto loc_0093670B;
loc_009368A8:
    goto loc_0093678A;
loc_009368B0:
loc_009368BA:
    *(unsigned int *)(*(unsigned __int64 *)(result) + 24) = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_0093678A;
}
```

## 5. (Beta) C Style

```c
int64_t VrpPostOpenOrCreate(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m5F;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x4D420D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mA8 = v_xmm0;
    result = EtwActivityIdControl(3, v_stack_mA8, Arg3, Arg4);
    Arg4 = 0;
    v_stack_mB0 = *(uint64_t *)(arg1);
    if (sign_flag) goto loc_009366FD;
    v_stack_mB8 = *(uint64_t *)(arg1 + 0x8);
loc_0093658A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10))) goto loc_009367FA;
loc_00936598:
    local_rsi = (0) + (48);
    if (sign_flag) { local_rsi = 0; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)))) == 260) goto loc_00936702;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)))) == 872) goto loc_00936634;
    if (local_rsi == 0) goto loc_009366C2;
    result = VrpAllocateKeyContext(*(uint64_t *)(local_rsi), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10), Arg4);
    Arg4 = 0;
    if (result == 0) goto loc_009368B0;
    Arg1 = 0;
    result = VrpBuildKeyPath(Arg1, local_rsi + 16, result + 16, Arg4);
    Arg4 = 0;
loc_009365F5:
    *(uint32_t *)(result + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8)));
    result = VrpCountPathComponents(result + 16, local_rsi + 16, result + 16, Arg4);
    *(uint16_t *)(result + 0x20) = (uint16_t)(result);
    result = CmSetCallbackObjectContext(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) + 0x48)), v_rip + 6003889, result, v_stack_mB8);
    Arg4 = 0;
    if (!sign_flag) goto loc_0093670E;
loc_00936634:
    if (local_rsi != 0) goto loc_0093670B;
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) == 0) goto loc_009368A8;
    result = CmAllocateExtraParameter(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) + 0x48)), v_rip + 6003889, result, Arg4);
    Arg4 = 0;
    if (result == 0) goto loc_009368B0;
    Arg1 = 0;
    result = VrpBuildKeyPath(Arg1, *(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 48, result + 16, Arg4);
    Arg4 = 0;
    result = ObfReferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x8), (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), result + 16, Arg4);
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x8);
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x40)));
loc_009366A5:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x10))) != (*(uint64_t *)(v_stack_mB8 + 0x10))) goto loc_0093682A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x10) + 0x8))) == (*(uint64_t *)(v_stack_mB8 + 0x10))) goto loc_00936856;
loc_009366BB:
loc_009366C2:
    result = VrpAllocateKeyContext((uint32_t)(0x67655256ULL), *(uint64_t *)(v_stack_mB8 + 0x10), result + 16, *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x10)));
    Arg4 = 0;
    if (result == 0) goto loc_009368B0;
    Arg1 = 0;
    result = VrpBuildKeyPath(Arg1, *(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 48, result + 16, Arg4);
    Arg4 = 0;
    goto loc_009365F5;
loc_009366FD:
    goto loc_00936712;
loc_00936702:
    if (local_rsi != 0) goto loc_0093686F;
loc_0093670B:
loc_0093670E:
loc_00936712:
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) == 0) goto loc_00936782;
loc_0093671D:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x40));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) + 0x8) != 0) {
        result = ObfDereferenceObject(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) + 0x8), *(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 48, result + 16, Arg4);
        Arg4 = 0;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20)) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x8)))) != 260) goto loc_009367B4;
loc_00936748:
loc_00936755:
    result = (uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x8));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x38) != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x67655256ULL));
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x38), Arg2, result + 16, Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x18) != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x67655256ULL));
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x18), Arg2, result + 16, Arg4);
    }
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20), (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), result + 16, Arg4);
loc_00936782:
    if (sign_flag) goto loc_009368BA;
loc_0093678A:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), result + 16, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
loc_009367B4:
    if (((uint32_t)(result)) == 872) goto loc_00936748;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10)) + 0x8) != 0) goto loc_009367EE;
loc_009367C8:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10))) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) + 0x70)) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x18) = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x20) + 0x28) = 0;
    goto loc_00936755;
loc_009367EE:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10)) + 0x8), Arg2, result + 16, Arg4);
    Arg4 = 0;
    goto loc_009367C8;
loc_009367FA:
    Arg1 = (*(uint64_t *)(result + 0x10)) - (*(uint64_t *)(v_rip - 0x92489D));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(result + 0x18);
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip - 0x9248A2));
    }
    if (Arg1 == NULL) goto loc_0093681F;
    goto loc_0093658A;
loc_0093681F:
    goto loc_00936598;
loc_0093682A:
    Arg3 = (*(uint64_t *)(Arg4 + 0x10)) - (*(uint64_t *)(arg1 + 0x10));
    if (!(condition_is_not_equal)) {
        Arg3 = *(uint64_t *)(Arg4 + 0x18);
        Arg3 = (Arg3) - (*(uint64_t *)(arg1 + 0x18));
    }
    if (Arg3 == 0) goto loc_00936849;
    goto loc_009366A5;
loc_00936849:
    Arg4 = 0;
loc_00936856:
    *(uint64_t *)(arg1) = 0;
    Arg4 = 0;
    *(uint64_t *)(arg1 + 0x8) = 0;
    *(void **)(0) = Arg1;
    *(void **)(Arg2 + 0x8) = Arg1;
    goto loc_0093671D;
loc_0093686F:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result) - 0x30) + 0x8)) != (*(uint64_t *)(result) - 48)) goto loc_009366BB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result) - 0x30 + 0x8))) != (*(uint64_t *)(result) - 48)) goto loc_009366BB;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result) - 0x30 + 0x8)) = *(uint64_t *)(*(uint64_t *)(result) - 0x30);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result) - 0x30) + 0x8) = *(uint64_t *)(*(uint64_t *)(result) - 0x30 + 0x8);
    *(uint64_t *)(*(uint64_t *)(result) - 0x30) = 0;
    *(uint64_t *)(*(uint64_t *)(result) - 0x30 + 0x8) = 0;
    result = CmpFreeExtraParameter(*(uint64_t *)(result) - 48, *(uint64_t *)(*(uint64_t *)(result) - 0x30), Arg3, Arg4);
    Arg4 = 0;
    goto loc_0093670B;
loc_009368A8:
    goto loc_0093678A;
loc_009368B0:
loc_009368BA:
    *(uint32_t *)(*(uint64_t *)(result) + 0x18) = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_0093678A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00936510&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
