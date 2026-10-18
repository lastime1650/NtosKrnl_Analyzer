# CMFSystemThreadRoutine

- RVA: `0x007D3A70`–`0x007D4087` (길이 `1,559` bytes)
- VA: `0x00000001407D3A70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D5A90`
- 디코드: `396`개 명령, `1,559/1,559` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x007D3B39` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D3B84` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x007D3BC7` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x007D3BE1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007D3C24` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (function, `0x006AD730`)
- `0x007D3C78` → [ZwCreateEvent](../../text/6A/ZwCreateEvent_function_006AD9D0.md) (function, `0x006AD9D0`)
- `0x007D3CB6` → [ZwReadFile](../../text/6A/ZwReadFile_function_006AD190.md) (function, `0x006AD190`)
- `0x007D3CCE` → [ZwWaitForSingleObject](../../text/6A/ZwWaitForSingleObject_function_006AD150.md) (function, `0x006AD150`)
- `0x007D3D59` → [CMFGetFileSizeEx](CMFGetFileSizeEx_function_007D3450.md) (function, `0x007D3450`)
- `0x007D3D7B` → [CMFGetLargePageSectionSize](CMFGetLargePageSectionSize_function_007D34C8.md) (function, `0x007D34C8`)
- `0x007D3DB2` → [CMFCreateSecurityDescriptor](CMFCreateSecurityDescriptor_function_007D2B10.md) (function, `0x007D2B10`)
- `0x007D3E0E` → [ZwCreateSection](../../text/6A/ZwCreateSection_function_006ADA10.md) (function, `0x006ADA10`)
- `0x007D3E69` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x007D3ED2` → [ZwMapViewOfSection](../../text/6A/ZwMapViewOfSection_function_006AD5D0.md) (function, `0x006AD5D0`)
- `0x007D3F2B` → [ZwReadFile](../../text/6A/ZwReadFile_function_006AD190.md) (function, `0x006AD190`)
- `0x007D3F43` → [ZwWaitForSingleObject](../../text/6A/ZwWaitForSingleObject_function_006AD150.md) (function, `0x006AD150`)
- `0x007D3F67` → [CMFReadCompressedSegment](CMFReadCompressedSegment_function_007D3580.md) (function, `0x007D3580`)
- `0x007D3F7F` → [ZwUnmapViewOfSection](../../text/6A/ZwUnmapViewOfSection_function_006AD610.md) (function, `0x006AD610`)
- `0x007D3FDE` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007D3FF1` → [ZwUnmapViewOfSection](../../text/6A/ZwUnmapViewOfSection_function_006AD610.md) (function, `0x006AD610`)
- `0x007D3FFF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007D400E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007D401D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D402A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x007D4039` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D4051` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007D4060` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007D3A96` → RVA `0x00E0A740` (`.data`; read)
- `0x007D3B15` → RVA `0x000395E8` (`.rdata`; read)
- `0x007D3B1C` → RVA `0x00B08CA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007D3B50` → RVA `0x000395D8` (`.rdata`; read)
- `0x007D3B61` → RVA `0x00B08C40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007D3B6B` → RVA `0x00B08C70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007D3B93` → RVA `0x000395E0` (`.rdata`; read)
- `0x007D3B9A` → RVA `0x00B08C10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007D3E42` → RVA `0x00FC6BD8` (`ALMOSTRO`; read)
- `0x007D3FA6` → RVA `0x00E0EC04` (`.data`; read)
- `0x007D3FBC` → RVA `0x00EEEFD0` (`.data`; read/write)
- `0x007D3FC5` → RVA `0x00E0EC04` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x007D3B39` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D3B84` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x007D3BC7` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x007D3BE1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007D3C24` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (`PAGE` → `.text`)
  - `0x007D3C78` → [ZwCreateEvent](../../text/6A/ZwCreateEvent_function_006AD9D0.md) (`PAGE` → `.text`)
  - `0x007D3CB6` → [ZwReadFile](../../text/6A/ZwReadFile_function_006AD190.md) (`PAGE` → `.text`)
  - `0x007D3CCE` → [ZwWaitForSingleObject](../../text/6A/ZwWaitForSingleObject_function_006AD150.md) (`PAGE` → `.text`)
  - `0x007D3E0E` → [ZwCreateSection](../../text/6A/ZwCreateSection_function_006ADA10.md) (`PAGE` → `.text`)
  - `0x007D3ED2` → [ZwMapViewOfSection](../../text/6A/ZwMapViewOfSection_function_006AD5D0.md) (`PAGE` → `.text`)
  - `0x007D3F2B` → [ZwReadFile](../../text/6A/ZwReadFile_function_006AD190.md) (`PAGE` → `.text`)
  - `0x007D3F43` → [ZwWaitForSingleObject](../../text/6A/ZwWaitForSingleObject_function_006AD150.md) (`PAGE` → `.text`)
  - `0x007D3F7F` → [ZwUnmapViewOfSection](../../text/6A/ZwUnmapViewOfSection_function_006AD610.md) (`PAGE` → `.text`)
  - `0x007D3FDE` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007D3FF1` → [ZwUnmapViewOfSection](../../text/6A/ZwUnmapViewOfSection_function_006AD610.md) (`PAGE` → `.text`)
  - `0x007D3FFF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007D400E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007D401D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D402A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x007D4039` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D4051` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007D4060` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D3A70  48 8B C4                        mov rax, rsp
007D3A73  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
007D3A77  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
007D3A7B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
007D3A7F  55                              push rbp
007D3A80  41 54                           push r12
007D3A82  41 55                           push r13
007D3A84  41 56                           push r14
007D3A86  41 57                           push r15
007D3A88  48 8D A8 B8 FD FF FF            lea rbp, [rax - 0x248]
007D3A8F  48 81 EC 20 03 00 00            sub rsp, 0x320
007D3A96  48 8B 05 A3 6C 63 00            mov rax, qword ptr [rip + 0x636ca3]
007D3A9D  48 33 C4                        xor rax, rsp
007D3AA0  48 89 85 10 02 00 00            mov qword ptr [rbp + 0x210], rax
007D3AA7  45 33 E4                        xor r12d, r12d
007D3AAA  0F 57 C0                        xorps xmm0, xmm0
007D3AAD  33 C0                           xor eax, eax
007D3AAF  4C 89 65 98                     mov qword ptr [rbp - 0x68], r12
007D3AB3  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007D3AB7  48 8B F9                        mov rdi, rcx
007D3ABA  89 45 C8                        mov dword ptr [rbp - 0x38], eax
007D3ABD  45 8B FC                        mov r15d, r12d
007D3AC0  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
007D3AC5  45 8B EC                        mov r13d, r12d
007D3AC8  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
007D3ACC  41 8B F4                        mov esi, r12d
007D3ACF  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
007D3AD3  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
007D3AD8  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
007D3ADC  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
007D3AE1  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
007D3AE6  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
007D3AEA  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
007D3AEF  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
007D3AF3  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
007D3AF7  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
007D3AFB  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
007D3AFF  48 85 C9                        test rcx, rcx
007D3B02  0F 84 4E 05 00 00               je 0x1407d4056
007D3B08  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
007D3B0B  B9 00 01 00 00                  mov ecx, 0x100
007D3B10  83 F8 10                        cmp eax, 0x10
007D3B13  75 10                           jne 0x1407d3b25
007D3B15  48 8D 05 CC 5A 86 FF            lea rax, [rip - 0x79a534]
007D3B1C  4C 8D 05 7D 51 33 00            lea r8, [rip + 0x33517d]
007D3B23  EB 7C                           jmp 0x1407d3ba1
007D3B25  83 F8 20                        cmp eax, 0x20
007D3B28  75 61                           jne 0x1407d3b8b
007D3B2A  41 BE 60 10 00 00               mov r14d, 0x1060
007D3B30  41 B8 50 66 6D 63               mov r8d, 0x636d6650
007D3B36  41 8B D6                        mov edx, r14d
007D3B39  E8 B2 E5 3A 00                  call 0x140b820f0
007D3B3E  4C 8B F8                        mov r15, rax
007D3B41  48 85 C0                        test rax, rax
007D3B44  75 0A                           jne 0x1407d3b50
007D3B46  BB 17 00 00 C0                  mov ebx, 0xc0000017
007D3B4B  E9 85 04 00 00                  jmp 0x1407d3fd5
007D3B50  48 8D 05 81 5A 86 FF            lea rax, [rip - 0x79a57f]
007D3B57  BA 04 01 00 00                  mov edx, 0x104
007D3B5C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007D3B61  4C 8D 0D D8 50 33 00            lea r9, [rip + 0x3350d8]
007D3B68  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
007D3B6B  4C 8D 05 FE 50 33 00            lea r8, [rip + 0x3350fe]
007D3B72  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007D3B76  48 8D 4D 00                     lea rcx, [rbp]
007D3B7A  8B 47 04                        mov eax, dword ptr [rdi + 4]
007D3B7D  4D 8B E7                        mov r12, r15
007D3B80  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007D3B84  E8 D3 F1 CA FF                  call 0x140482d5c
007D3B89  EB 41                           jmp 0x1407d3bcc
007D3B8B  3B C1                           cmp eax, ecx
007D3B8D  0F 85 3D 04 00 00               jne 0x1407d3fd0
007D3B93  48 8D 05 46 5A 86 FF            lea rax, [rip - 0x79a5ba]
007D3B9A  4C 8D 05 6F 50 33 00            lea r8, [rip + 0x33506f]
007D3BA1  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
007D3BA6  4C 8D 0D 93 50 33 00            lea r9, [rip + 0x335093]
007D3BAD  8B 47 04                        mov eax, dword ptr [rdi + 4]
007D3BB0  48 8D 4D 00                     lea rcx, [rbp]
007D3BB4  BA 04 01 00 00                  mov edx, 0x104
007D3BB9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007D3BBD  4C 8D 65 F0                     lea r12, [rbp - 0x10]
007D3BC1  41 BE 08 00 00 00               mov r14d, 8
007D3BC7  E8 90 F1 CA FF                  call 0x140482d5c
007D3BCC  BE 00 00 00 C0                  mov esi, 0xc0000000
007D3BD1  8B D8                           mov ebx, eax
007D3BD3  23 C6                           and eax, esi
007D3BD5  3B C6                           cmp eax, esi
007D3BD7  74 60                           je 0x1407d3c39
007D3BD9  48 8D 55 00                     lea rdx, [rbp]
007D3BDD  48 8D 4D E0                     lea rcx, [rbp - 0x20]
007D3BE1  E8 9A 6B C5 FF                  call 0x14042a780
007D3BE6  44 21 6C 24 28                  and dword ptr [rsp + 0x28], r13d
007D3BEB  48 8D 45 E0                     lea rax, [rbp - 0x20]
007D3BEF  4C 21 6D A8                     and qword ptr [rbp - 0x58], r13
007D3BF3  4C 8D 4D D0                     lea r9, [rbp - 0x30]
007D3BF7  0F 57 C0                        xorps xmm0, xmm0
007D3BFA  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
007D3BFE  4C 8D 45 A0                     lea r8, [rbp - 0x60]
007D3C02  C7 45 A0 30 00 00 00            mov dword ptr [rbp - 0x60], 0x30
007D3C09  8B D6                           mov edx, esi
007D3C0B  C7 45 B8 40 02 00 00            mov dword ptr [rbp - 0x48], 0x240
007D3C12  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
007D3C17  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
007D3C1F  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
007D3C24  E8 07 9B ED FF                  call 0x1406ad730
007D3C29  8B D8                           mov ebx, eax
007D3C2B  23 C6                           and eax, esi
007D3C2D  3B C6                           cmp eax, esi
007D3C2F  75 12                           jne 0x1407d3c43
007D3C31  45 33 E4                        xor r12d, r12d
007D3C34  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
007D3C39  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
007D3C3E  E9 92 03 00 00                  jmp 0x1407d3fd5
007D3C43  33 C0                           xor eax, eax
007D3C45  C7 45 A0 30 00 00 00            mov dword ptr [rbp - 0x60], 0x30
007D3C4C  0F 57 C0                        xorps xmm0, xmm0
007D3C4F  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007D3C53  4C 8D 45 A0                     lea r8, [rbp - 0x60]
007D3C57  C7 45 B8 00 02 00 00            mov dword ptr [rbp - 0x48], 0x200
007D3C5E  BA 03 00 1F 00                  mov edx, 0x1f0003
007D3C63  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
007D3C67  44 8D 48 01                     lea r9d, [rax + 1]
007D3C6B  88 44 24 20                     mov byte ptr [rsp + 0x20], al
007D3C6F  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007D3C73  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
007D3C78  E8 53 9D ED FF                  call 0x1406ad9d0
007D3C7D  8B D8                           mov ebx, eax
007D3C7F  23 C6                           and eax, esi
007D3C81  3B C6                           cmp eax, esi
007D3C83  74 B4                           je 0x1407d3c39
007D3C85  4C 21 6C 24 40                  and qword ptr [rsp + 0x40], r13
007D3C8A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
007D3C8F  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
007D3C93  45 33 C9                        xor r9d, r9d
007D3C96  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007D3C9B  45 33 C0                        xor r8d, r8d
007D3C9E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007D3CA3  48 8D 45 D0                     lea rax, [rbp - 0x30]
007D3CA7  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
007D3CAC  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
007D3CB1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007D3CB6  E8 D5 94 ED FF                  call 0x1406ad190
007D3CBB  8B D8                           mov ebx, eax
007D3CBD  85 C0                           test eax, eax
007D3CBF  0F 88 74 FF FF FF               js 0x1407d3c39
007D3CC5  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
007D3CC9  45 33 C0                        xor r8d, r8d
007D3CCC  33 D2                           xor edx, edx
007D3CCE  E8 7D 94 ED FF                  call 0x1406ad150
007D3CD3  8B D8                           mov ebx, eax
007D3CD5  85 C0                           test eax, eax
007D3CD7  74 10                           je 0x1407d3ce9
007D3CD9  0F 88 5A FF FF FF               js 0x1407d3c39
007D3CDF  BB 01 00 00 C0                  mov ebx, 0xc0000001
007D3CE4  E9 50 FF FF FF                  jmp 0x1407d3c39
007D3CE9  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
007D3CEE  48 8B 00                        mov rax, qword ptr [rax]
007D3CF1  49 39 04 24                     cmp qword ptr [r12], rax
007D3CF5  74 0A                           je 0x1407d3d01
007D3CF7  BB 00 A0 00 C0                  mov ebx, 0xc000a000
007D3CFC  E9 38 FF FF FF                  jmp 0x1407d3c39
007D3D01  8B 5F 30                        mov ebx, dword ptr [rdi + 0x30]
007D3D04  83 FB 20                        cmp ebx, 0x20
007D3D07  75 13                           jne 0x1407d3d1c
007D3D09  45 39 6F 4C                     cmp dword ptr [r15 + 0x4c], r13d
007D3D0D  74 0D                           je 0x1407d3d1c
007D3D0F  83 4F 18 04                     or dword ptr [rdi + 0x18], 4
007D3D13  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
007D3D18  C6 47 0C 01                     mov byte ptr [rdi + 0xc], 1
007D3D1C  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007D3D21  45 33 F6                        xor r14d, r14d
007D3D24  45 33 E4                        xor r12d, r12d
007D3D27  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
007D3D2C  44 38 67 0C                     cmp byte ptr [rdi + 0xc], r12b
007D3D30  74 71                           je 0x1407d3da3
007D3D32  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
007D3D37  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
007D3D3C  83 FB 10                        cmp ebx, 0x10
007D3D3F  74 13                           je 0x1407d3d54
007D3D41  81 FB 00 01 00 00               cmp ebx, 0x100
007D3D47  74 0B                           je 0x1407d3d54
007D3D49  45 8B 77 20                     mov r14d, dword ptr [r15 + 0x20]
007D3D4D  44 89 74 24 58                  mov dword ptr [rsp + 0x58], r14d
007D3D52  EB 1E                           jmp 0x1407d3d72
007D3D54  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
007D3D59  E8 F2 F6 FF FF                  call 0x1407d3450
007D3D5E  8B D8                           mov ebx, eax
007D3D60  23 C6                           and eax, esi
007D3D62  3B C6                           cmp eax, esi
007D3D64  0F 84 CF FE FF FF               je 0x1407d3c39
007D3D6A  44 8B 74 24 58                  mov r14d, dword ptr [rsp + 0x58]
007D3D6F  8B 5F 30                        mov ebx, dword ptr [rdi + 0x30]
007D3D72  48 8D 55 98                     lea rdx, [rbp - 0x68]
007D3D76  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
007D3D7B  E8 48 F7 FF FF                  call 0x1407d34c8
007D3D80  85 C0                           test eax, eax
007D3D82  78 12                           js 0x1407d3d96
007D3D84  44 39 27                        cmp dword ptr [rdi], r12d
007D3D87  7D 0D                           jge 0x1407d3d96
007D3D89  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
007D3D8C  4C 8D 65 98                     lea r12, [rbp - 0x68]
007D3D90  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
007D3D94  EB 0D                           jmp 0x1407d3da3
007D3D96  0F BA 37 1F                     btr dword ptr [rdi], 0x1f
007D3D9A  4C 8D 64 24 58                  lea r12, [rsp + 0x58]
007D3D9F  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
007D3DA3  81 FB 00 01 00 00               cmp ebx, 0x100
007D3DA9  74 18                           je 0x1407d3dc3
007D3DAB  33 D2                           xor edx, edx
007D3DAD  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
007D3DB2  E8 59 ED FF FF                  call 0x1407d2b10
007D3DB7  8B D8                           mov ebx, eax
007D3DB9  23 C6                           and eax, esi
007D3DBB  3B C6                           cmp eax, esi
007D3DBD  0F 84 76 FE FF FF               je 0x1407d3c39
007D3DC3  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
007D3DC8  4C 8D 45 A0                     lea r8, [rbp - 0x60]
007D3DCC  33 C9                           xor ecx, ecx
007D3DCE  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007D3DD2  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
007D3DD7  4D 8B CC                        mov r9, r12
007D3DDA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007D3DDF  8B 07                           mov eax, dword ptr [rdi]
007D3DE1  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
007D3DE5  8D 51 06                        lea edx, [rcx + 6]
007D3DE8  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
007D3DEC  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
007D3DF0  48 8D 4D 88                     lea rcx, [rbp - 0x78]
007D3DF4  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007D3DF8  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
007D3E00  C7 45 A0 30 00 00 00            mov dword ptr [rbp - 0x60], 0x30
007D3E07  C7 45 B8 40 02 00 00            mov dword ptr [rbp - 0x48], 0x240
007D3E0E  E8 FD 9B ED FF                  call 0x1406ada10
007D3E13  45 33 E4                        xor r12d, r12d
007D3E16  8B D8                           mov ebx, eax
007D3E18  85 C0                           test eax, eax
007D3E1A  79 26                           jns 0x1407d3e42
007D3E1C  44 38 67 0C                     cmp byte ptr [rdi + 0xc], r12b
007D3E20  74 17                           je 0x1407d3e39
007D3E22  8B 07                           mov eax, dword ptr [rdi]
007D3E24  85 C0                           test eax, eax
007D3E26  79 11                           jns 0x1407d3e39
007D3E28  0F BA F0 1F                     btr eax, 0x1f
007D3E2C  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
007D3E30  89 07                           mov dword ptr [rdi], eax
007D3E32  4C 8D 64 24 58                  lea r12, [rsp + 0x58]
007D3E37  EB 8A                           jmp 0x1407d3dc3
007D3E39  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
007D3E3D  E9 F7 FD FF FF                  jmp 0x1407d3c39
007D3E42  4C 8B 05 8F 2D 7F 00            mov r8, qword ptr [rip + 0x7f2d8f]
007D3E49  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007D3E4E  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
007D3E52  45 33 C9                        xor r9d, r9d
007D3E55  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
007D3E5A  BA 1F 00 0F 00                  mov edx, 0xf001f
007D3E5F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007D3E64  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
007D3E69  E8 42 4F 09 00                  call 0x140868db0
007D3E6E  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
007D3E73  8B D8                           mov ebx, eax
007D3E75  23 C6                           and eax, esi
007D3E77  3B C6                           cmp eax, esi
007D3E79  75 08                           jne 0x1407d3e83
007D3E7B  4D 8B EC                        mov r13, r12
007D3E7E  E9 B6 FD FF FF                  jmp 0x1407d3c39
007D3E83  44 38 67 0C                     cmp byte ptr [rdi + 0xc], r12b
007D3E87  0F 84 FC 00 00 00               je 0x1407d3f89
007D3E8D  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
007D3E91  48 8D 45 90                     lea rax, [rbp - 0x70]
007D3E95  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
007D3E9D  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
007D3EA2  C7 44 24 40 00 00 40 00         mov dword ptr [rsp + 0x40], 0x400000
007D3EAA  45 33 C9                        xor r9d, r9d
007D3EAD  C7 44 24 38 02 00 00 00         mov dword ptr [rsp + 0x38], 2
007D3EB5  48 83 CA FF                     or rdx, 0xffffffffffffffff
007D3EB9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007D3EBE  48 8D 44 24 58                  lea rax, [rsp + 0x58]
007D3EC3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007D3EC8  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
007D3ECD  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
007D3ED2  E8 F9 96 ED FF                  call 0x1406ad5d0
007D3ED7  8B D8                           mov ebx, eax
007D3ED9  23 C6                           and eax, esi
007D3EDB  3B C6                           cmp eax, esi
007D3EDD  75 0A                           jne 0x1407d3ee9
007D3EDF  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
007D3EE4  E9 50 FD FF FF                  jmp 0x1407d3c39
007D3EE9  44 38 64 24 50                  cmp byte ptr [rsp + 0x50], r12b
007D3EEE  75 63                           jne 0x1407d3f53
007D3EF0  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
007D3EF4  48 8D 44 24 58                  lea rax, [rsp + 0x58]
007D3EF9  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007D3EFE  45 33 C9                        xor r9d, r9d
007D3F01  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
007D3F06  45 33 C0                        xor r8d, r8d
007D3F09  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007D3F0E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
007D3F13  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
007D3F18  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007D3F1D  48 8D 45 D0                     lea rax, [rbp - 0x30]
007D3F21  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007D3F26  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
007D3F2B  E8 60 92 ED FF                  call 0x1406ad190
007D3F30  8B D8                           mov ebx, eax
007D3F32  85 C0                           test eax, eax
007D3F34  0F 88 FF FC FF FF               js 0x1407d3c39
007D3F3A  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
007D3F3E  45 33 C0                        xor r8d, r8d
007D3F41  33 D2                           xor edx, edx
007D3F43  E8 08 92 ED FF                  call 0x1406ad150
007D3F48  8B D8                           mov ebx, eax
007D3F4A  85 C0                           test eax, eax
007D3F4C  74 28                           je 0x1407d3f76
007D3F4E  E9 86 FD FF FF                  jmp 0x1407d3cd9
007D3F53  45 89 67 4C                     mov dword ptr [r15 + 0x4c], r12d
007D3F57  4D 8B CF                        mov r9, r15
007D3F5A  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
007D3F5F  45 8B C6                        mov r8d, r14d
007D3F62  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007D3F67  E8 14 F6 FF FF                  call 0x1407d3580
007D3F6C  8B D8                           mov ebx, eax
007D3F6E  85 C0                           test eax, eax
007D3F70  0F 88 C3 FC FF FF               js 0x1407d3c39
007D3F76  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
007D3F7B  48 83 C9 FF                     or rcx, 0xffffffffffffffff
007D3F7F  E8 8C 96 ED FF                  call 0x1406ad610
007D3F84  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
007D3F89  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
007D3F8D  48 85 C0                        test rax, rax
007D3F90  0F 84 A3 FC FF FF               je 0x1407d3c39
007D3F96  4C 89 28                        mov qword ptr [rax], r13
007D3F99  4D 8B EC                        mov r13, r12
007D3F9C  83 7F 30 10                     cmp dword ptr [rdi + 0x30], 0x10
007D3FA0  0F 85 93 FC FF FF               jne 0x1407d3c39
007D3FA6  81 3D 54 AC 63 00 10 27 00 00   cmp dword ptr [rip + 0x63ac54], 0x2710
007D3FB0  0F 85 83 FC FF FF               jne 0x1407d3c39
007D3FB6  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
007D3FB9  83 E0 0F                        and eax, 0xf
007D3FBC  09 05 0E B0 71 00               or dword ptr [rip + 0x71b00e], eax
007D3FC2  8B 47 04                        mov eax, dword ptr [rdi + 4]
007D3FC5  89 05 39 AC 63 00               mov dword ptr [rip + 0x63ac39], eax
007D3FCB  E9 69 FC FF FF                  jmp 0x1407d3c39
007D3FD0  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007D3FD5  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
007D3FD9  48 85 C9                        test rcx, rcx
007D3FDC  74 05                           je 0x1407d3fe3
007D3FDE  E8 CD 92 ED FF                  call 0x1406ad2b0
007D3FE3  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
007D3FE8  48 85 D2                        test rdx, rdx
007D3FEB  74 09                           je 0x1407d3ff6
007D3FED  48 83 C9 FF                     or rcx, 0xffffffffffffffff
007D3FF1  E8 1A 96 ED FF                  call 0x1406ad610
007D3FF6  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
007D3FFA  48 85 C9                        test rcx, rcx
007D3FFD  74 05                           je 0x1407d4004
007D3FFF  E8 AC 92 ED FF                  call 0x1406ad2b0
007D4004  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007D4009  48 85 C9                        test rcx, rcx
007D400C  74 05                           je 0x1407d4013
007D400E  E8 9D 92 ED FF                  call 0x1406ad2b0
007D4013  48 85 F6                        test rsi, rsi
007D4016  74 0A                           je 0x1407d4022
007D4018  33 D2                           xor edx, edx
007D401A  48 8B CE                        mov rcx, rsi
007D401D  E8 4E E8 3A 00                  call 0x140b82870
007D4022  4D 85 ED                        test r13, r13
007D4025  74 08                           je 0x1407d402f
007D4027  49 8B CD                        mov rcx, r13
007D402A  E8 21 53 B2 FF                  call 0x1402f9350
007D402F  4D 85 FF                        test r15, r15
007D4032  74 0A                           je 0x1407d403e
007D4034  33 D2                           xor edx, edx
007D4036  49 8B CF                        mov rcx, r15
007D4039  E8 32 E8 3A 00                  call 0x140b82870
007D403E  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
007D4042  89 5F 24                        mov dword ptr [rdi + 0x24], ebx
007D4045  48 85 C9                        test rcx, rcx
007D4048  74 0C                           je 0x1407d4056
007D404A  45 33 C0                        xor r8d, r8d
007D404D  41 8D 50 01                     lea edx, [r8 + 1]
007D4051  E8 BA B2 B6 FF                  call 0x14033f310
007D4056  48 8B 8D 10 02 00 00            mov rcx, qword ptr [rbp + 0x210]
007D405D  48 33 CC                        xor rcx, rsp
007D4060  E8 DB 85 ED FF                  call 0x1406ac640
007D4065  4C 8D 9C 24 20 03 00 00         lea r11, [rsp + 0x320]
007D406D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
007D4071  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
007D4075  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
007D4079  49 8B E3                        mov rsp, r11
007D407C  41 5F                           pop r15
007D407E  41 5E                           pop r14
007D4080  41 5D                           pop r13
007D4082  41 5C                           pop r12
007D4084  5D                              pop rbp
007D4085  C3                              ret
007D4086  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CMFSystemThreadRoutine(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int8 v_stack_m2F8;
    unsigned int v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned int v_stack_m318;
    unsigned int v_stack_m320;
    unsigned int v_stack_m328;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (800);
    result = (*(unsigned __int64 *)(v_rip + 6515875)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 584 + 528) = result;
    v_r12 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 64) = 0;
    *(unsigned int *)(v_rsp - 584 - 56) = 0;
    v_stack_m2F0 = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 16) = 0;
    v_stack_m2F8 = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 128) = 0;
    v_stack_m2D0 = 0;
    v_stack_m2E8 = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 120) = 0;
    v_stack_m2D8 = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 48) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 584 - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 584 - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 584 - 32) = v_xmm0;
    if (a1 == 0) goto loc_007D4056;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) != 16) goto loc_007D3B25;
    goto loc_007D3BA1;
loc_007D3B25:
    if (((unsigned int)(v_rip - 7972148)) != 32) goto loc_007D3B8B;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(0x1060ULL))), (unsigned int)(0x636D6650ULL), a4);
    if (result != 0) goto loc_007D3B50;
    goto loc_007D3FD5;
loc_007D3B50:
    v_stack_m2E0 = v_rip - 7972223;
    v_stack_m320 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    v_stack_m328 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    result = RtlStringCchPrintfW(v_rsp - 584, 260, v_rip + 3363070, v_rip + 3363032);
    goto loc_007D3BCC;
loc_007D3B8B:
    if (((unsigned int)(result)) != ((unsigned int)(v_rsp - 584))) goto loc_007D3FD0;
loc_007D3BA1:
    v_stack_m2E0 = v_rip - 7972282;
    v_stack_m328 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    result = RtlStringCchPrintfW(v_rsp - 584, 260, v_rip + 3362927, v_rip + 3362963);
loc_007D3BCC:
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D3C39;
    result = RtlInitUnicodeString(v_rsp - 584 - 32, v_rsp - 584, v_rip + 3362927, v_rip + 3362963);
    *(unsigned __int64 *)(v_rsp - 584 - 80) = v_rsp - 584 - 32;
    *(unsigned int *)(v_rsp - 584 - 96) = 48;
    *(unsigned int *)(v_rsp - 584 - 72) = 576;
    v_stack_m328 = 7;
    *(unsigned __int64 *)(v_rsp - 584 - 64) = v_xmm0;
    result = ZwOpenFile(v_stack_m2D0, (unsigned int)((unsigned int)((unsigned int)(0xC0000000ULL))), v_rsp - 584 - 96, v_rsp - 584 - 48);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_007D3C43;
    v_r12 = 0;
    v_stack_m2D0 = 0;
loc_007D3C39:
    goto loc_007D3FD5;
loc_007D3C43:
    result = 0;
    *(unsigned int *)(v_rsp - 584 - 96) = 48;
    *(unsigned __int64 *)(v_rsp - 584 - 88) = 0;
    *(unsigned int *)(v_rsp - 584 - 72) = 512;
    *(unsigned __int64 *)(v_rsp - 584 - 80) = 0;
    v_stack_m328 = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 64) = v_xmm0;
    result = ZwCreateEvent(v_rsp - 584 - 128, (unsigned int)(0x1F0003ULL), v_rsp - 584 - 96, result + 1);
    result = (unsigned int)((result) & ((unsigned int)(v_stack_m2E8)));
    if (((unsigned int)(result)) == ((unsigned int)(v_stack_m2E8))) goto loc_007D3C39;
    a4 = 0;
    a3 = 0;
    v_stack_m310 = v_stack_m2F0;
    v_stack_m318 = 8;
    v_stack_m320 = 0;
    v_stack_m328 = v_rsp - 584 - 48;
    result = ZwReadFile(v_stack_m2D0, *(unsigned __int64 *)(v_rsp - 584 - 128), a3, a4);
    if (sign_flag) goto loc_007D3C39;
    a3 = 0;
    a2 = 0;
    result = ZwWaitForSingleObject(*(unsigned __int64 *)(v_rsp - 584 - 128), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_007D3CE9;
loc_007D3CD9:
    if (sign_flag) goto loc_007D3C39;
    goto loc_007D3C39;
loc_007D3CE9:
    if ((*(unsigned __int64 *)(v_r12)) == (*(unsigned __int64 *)(v_stack_m2E0))) goto loc_007D3D01;
    goto loc_007D3C39;
loc_007D3D01:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) != 32) goto loc_007D3D1C;
    if ((*(unsigned int *)(result + 76)) != 0) {
        v_stack_m2F8 = 1;
        *(unsigned __int8 *)(a1 + 12) = 1;
    }
    v_r14 = 0;
    v_r12 = 0;
    v_stack_m2E0 = v_stack_m2D0;
    if ((*(unsigned __int8 *)(a1 + 12)) == 0) goto loc_007D3DA3;
    v_stack_m2E0 = 0;
    v_stack_m2F0 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) == 16) goto loc_007D3D54;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) == 256) goto loc_007D3D54;
    v_stack_m2F0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)));
    goto loc_007D3D72;
loc_007D3D54:
    result = CMFGetFileSizeEx(v_stack_m2D0, v_stack_m2F0, a3, a4);
    result = (unsigned int)((result) & ((unsigned int)(v_stack_m2E8)));
    if (((unsigned int)(result)) == ((unsigned int)(v_stack_m2E8))) goto loc_007D3C39;
loc_007D3D72:
    result = CMFGetLargePageSectionSize(v_stack_m2F0, v_rsp - 584 - 104, a3, a4);
    if (sign_flag) goto loc_007D3D96;
    if ((*(unsigned int *)(a1)) >= 0) goto loc_007D3D96;
    *(unsigned __int64 *)(v_rsp - 584 - 112) = (unsigned int)(*(unsigned int *)(v_rsp - 584 - 104));
    goto loc_007D3DA3;
loc_007D3D96:
    *(unsigned __int64 *)(v_rsp - 584 - 112) = (unsigned int)(v_stack_m2F0);
loc_007D3DA3:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)))) == 256) goto loc_007D3DC3;
    a2 = 0;
    result = CMFCreateSecurityDescriptor(v_stack_m2E8, a2, a3, a4);
    result = (unsigned int)((result) & ((unsigned int)(v_stack_m2E8)));
    if (((unsigned int)(result)) == ((unsigned int)(v_stack_m2E8))) goto loc_007D3C39;
loc_007D3DC3:
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 64) = v_stack_m2E8;
    v_stack_m318 = v_stack_m2E0;
    *(unsigned __int64 *)(v_rsp - 584 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 584 - 56) = 0;
    v_stack_m320 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m328 = 4;
    *(unsigned int *)(v_rsp - 584 - 96) = 48;
    *(unsigned int *)(v_rsp - 584 - 72) = 576;
    result = ZwCreateSection(v_rsp - 584 - 120, a1 + 6, v_rsp - 584 - 96, v_stack_m2F0);
    v_r12 = 0;
    if (!sign_flag) goto loc_007D3E42;
    if ((*(unsigned __int8 *)(a1 + 12)) == 0) goto loc_007D3E39;
    if (!sign_flag) goto loc_007D3E39;
    *(unsigned __int64 *)(v_rsp - 584 - 112) = (unsigned int)(v_stack_m2F0);
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    goto loc_007D3DC3;
loc_007D3E39:
    *(unsigned __int64 *)(v_rsp - 584 - 120) = v_stack_m2F0;
    goto loc_007D3C39;
loc_007D3E42:
    a4 = 0;
    v_stack_m320 = v_stack_m2F0;
    v_stack_m328 = v_stack_m2E0;
    v_stack_m2E0 = v_stack_m2F0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(v_rsp - 584 - 120), (unsigned int)(0xF001FULL), *(unsigned __int64 *)(v_rip + 8334735), a4);
    result = (unsigned int)((result) & ((unsigned int)(v_stack_m2E8)));
    if (((unsigned int)(result)) != ((unsigned int)(v_stack_m2E8))) goto loc_007D3E83;
    goto loc_007D3C39;
loc_007D3E83:
    if ((*(unsigned __int8 *)(a1 + 12)) == ((unsigned __int8)(v_stack_m2F0))) goto loc_007D3F89;
    v_stack_m300 = 4;
    v_stack_m308 = 0x400000ULL;
    a4 = 0;
    v_stack_m310 = 2;
    a2 = ((unsigned int)(0xF001FULL)) | (-1);
    v_stack_m318 = v_rsp - 584 - 112;
    v_stack_m320 = v_stack_m2F0;
    v_stack_m328 = v_stack_m2F0;
    v_stack_m2F0 = v_stack_m2F0;
    result = ZwMapViewOfSection(*(unsigned __int64 *)(v_rsp - 584 - 120), a2, v_stack_m2D8, a4);
    result = (unsigned int)((result) & ((unsigned int)(v_stack_m2E8)));
    if (((unsigned int)(result)) != ((unsigned int)(v_stack_m2E8))) goto loc_007D3EE9;
    v_stack_m2D8 = v_stack_m2F0;
    goto loc_007D3C39;
loc_007D3EE9:
    if (v_stack_m2F8 != ((unsigned __int8)(v_stack_m2F0))) goto loc_007D3F53;
    a4 = 0;
    v_stack_m308 = v_stack_m2F0;
    a3 = 0;
    v_stack_m310 = v_stack_m2F0;
    v_stack_m318 = (unsigned int)((unsigned int)(v_stack_m2F0));
    v_stack_m320 = v_stack_m2D8;
    v_stack_m328 = v_rsp - 584 - 48;
    v_stack_m2F0 = v_stack_m2F0;
    result = ZwReadFile(v_stack_m2D0, *(unsigned __int64 *)(v_rsp - 584 - 128), a3, a4);
    if (sign_flag) goto loc_007D3C39;
    a3 = 0;
    a2 = 0;
    result = ZwWaitForSingleObject(*(unsigned __int64 *)(v_rsp - 584 - 128), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_007D3F76;
    goto loc_007D3CD9;
loc_007D3F53:
    *(unsigned int *)(result + 76) = (unsigned int)(v_stack_m2F0);
    result = CMFReadCompressedSegment(v_stack_m2D0, v_stack_m2D8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    if (sign_flag) goto loc_007D3C39;
loc_007D3F76:
    a1 = (v_stack_m2D0) | (-1);
    result = ZwUnmapViewOfSection(a1, v_stack_m2D8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    v_stack_m2D8 = v_stack_m2F0;
loc_007D3F89:
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_007D3C39;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40)) = v_stack_m2F0;
    if ((*(unsigned int *)(a1 + 48)) != 16) goto loc_007D3C39;
    if ((*(unsigned int *)(v_rip + 6532180)) != 0x2710ULL) goto loc_007D3C39;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) & (15));
    *(unsigned int *)(v_rip + 6532153) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    goto loc_007D3C39;
loc_007D3FD0:
loc_007D3FD5:
    result = (unsigned int)(*(unsigned int *)(a1 + 4));
    if (*(unsigned __int64 *)(v_rsp - 584 - 128) != 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 584 - 128), v_stack_m2D8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    }
    if (v_stack_m2D8 != 0) {
        a1 = (*(unsigned __int64 *)(v_rsp - 584 - 128)) | (-1);
        result = ZwUnmapViewOfSection(a1, v_stack_m2D8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    }
    if (*(unsigned __int64 *)(v_rsp - 584 - 120) != 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 584 - 120), v_stack_m2D8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    }
    if (v_stack_m2D0 != 0) {
        result = ZwClose(v_stack_m2D0, v_stack_m2D8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    }
    if (v_stack_m2E8 != 0) {
        a2 = 0;
        a1 = v_stack_m2E8;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    }
    if (v_stack_m2F0 != 0) {
        a1 = v_stack_m2F0;
        result = ObfDereferenceObject(a1, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0))), result);
    }
    *(unsigned int *)(a1 + 36) = (unsigned int)((unsigned int)(0xC000000DULL));
    if (*(unsigned __int64 *)(a1 + 16) != 0) {
        a3 = 0;
        a2 = a3 + 1;
        result = KeSetEvent(*(unsigned __int64 *)(a1 + 16), a2, a3, result);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 584 + 528)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, result);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CMFSystemThreadRoutine(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint8_t v_stack_m2F8;
    uint32_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint32_t v_stack_m318;
    uint32_t v_stack_m320;
    uint32_t v_stack_m328;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (800);
    result = (*(uint64_t *)(v_rip + 0x636CA3)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x248 + 0x210) = result;
    local_r12 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x40) = 0;
    *(uint32_t *)(local_rsp - 0x248 - 0x38) = 0;
    v_stack_m2F0 = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x10) = 0;
    v_stack_m2F8 = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x80) = 0;
    v_stack_m2D0 = 0;
    v_stack_m2E8 = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x78) = 0;
    v_stack_m2D8 = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x30) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x248 - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x248 - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x248 - 0x20) = v_xmm0;
    if (Arg1 == NULL) goto loc_007D4056;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) != 16) goto loc_007D3B25;
    goto loc_007D3BA1;
loc_007D3B25:
    if (((uint32_t)(v_rip - 7972148)) != 32) goto loc_007D3B8B;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(0x1060ULL))), (uint32_t)(0x636D6650ULL), a4);
    if (result != 0) goto loc_007D3B50;
    goto loc_007D3FD5;
loc_007D3B50:
    v_stack_m2E0 = v_rip - 7972223;
    v_stack_m320 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    v_stack_m328 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    result = RtlStringCchPrintfW(local_rsp - 584, 260, v_rip + 3363070, v_rip + 3363032);
    goto loc_007D3BCC;
loc_007D3B8B:
    if (((uint32_t)(result)) != ((uint32_t)(local_rsp - 584))) goto loc_007D3FD0;
loc_007D3BA1:
    v_stack_m2E0 = v_rip - 7972282;
    v_stack_m328 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    result = RtlStringCchPrintfW(local_rsp - 584, 260, v_rip + 3362927, v_rip + 3362963);
loc_007D3BCC:
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D3C39;
    result = RtlInitUnicodeString(local_rsp - 584 - 32, local_rsp - 584, v_rip + 3362927, v_rip + 3362963);
    *(uint64_t *)(local_rsp - 0x248 - 0x50) = local_rsp - 584 - 32;
    *(uint32_t *)(local_rsp - 0x248 - 0x60) = 48;
    *(uint32_t *)(local_rsp - 0x248 - 0x48) = 576;
    v_stack_m328 = 7;
    *(uint64_t *)(local_rsp - 0x248 - 0x40) = v_xmm0;
    result = ZwOpenFile(v_stack_m2D0, (uint32_t)((uint32_t)((uint32_t)(0xC0000000ULL))), local_rsp - 584 - 96, local_rsp - 584 - 48);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_007D3C43;
    local_r12 = 0;
    v_stack_m2D0 = 0;
loc_007D3C39:
    goto loc_007D3FD5;
loc_007D3C43:
    result = 0;
    *(uint32_t *)(local_rsp - 0x248 - 0x60) = 48;
    *(uint64_t *)(local_rsp - 0x248 - 0x58) = 0;
    *(uint32_t *)(local_rsp - 0x248 - 0x48) = 512;
    *(uint64_t *)(local_rsp - 0x248 - 0x50) = 0;
    v_stack_m328 = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x40) = v_xmm0;
    result = ZwCreateEvent(local_rsp - 584 - 128, (uint32_t)(0x1F0003ULL), local_rsp - 584 - 96, result + 1);
    result = (uint32_t)((result) & ((uint32_t)(v_stack_m2E8)));
    if (((uint32_t)(result)) == ((uint32_t)(v_stack_m2E8))) goto loc_007D3C39;
    a4 = 0;
    a3 = 0;
    v_stack_m310 = v_stack_m2F0;
    v_stack_m318 = 8;
    v_stack_m320 = 0;
    v_stack_m328 = local_rsp - 584 - 48;
    result = ZwReadFile(v_stack_m2D0, *(uint64_t *)(local_rsp - 0x248 - 0x80), a3, a4);
    if (sign_flag) goto loc_007D3C39;
    a3 = 0;
    a2 = 0;
    result = ZwWaitForSingleObject(*(uint64_t *)(local_rsp - 0x248 - 0x80), a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_007D3CE9;
loc_007D3CD9:
    if (sign_flag) goto loc_007D3C39;
    goto loc_007D3C39;
loc_007D3CE9:
    if ((*(uint64_t *)(local_r12)) == (*(uint64_t *)(v_stack_m2E0))) goto loc_007D3D01;
    goto loc_007D3C39;
loc_007D3D01:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) != 32) goto loc_007D3D1C;
    if ((*(uint32_t *)(result + 0x4C)) != 0) {
        v_stack_m2F8 = 1;
        *(uint8_t *)(arg1 + 0xC) = 1;
    }
    local_r14 = 0;
    local_r12 = 0;
    v_stack_m2E0 = v_stack_m2D0;
    if ((*(uint8_t *)(arg1 + 0xC)) == 0) goto loc_007D3DA3;
    v_stack_m2E0 = 0;
    v_stack_m2F0 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) == 16) goto loc_007D3D54;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) == 256) goto loc_007D3D54;
    v_stack_m2F0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)));
    goto loc_007D3D72;
loc_007D3D54:
    result = CMFGetFileSizeEx(v_stack_m2D0, v_stack_m2F0, a3, a4);
    result = (uint32_t)((result) & ((uint32_t)(v_stack_m2E8)));
    if (((uint32_t)(result)) == ((uint32_t)(v_stack_m2E8))) goto loc_007D3C39;
loc_007D3D72:
    result = CMFGetLargePageSectionSize(v_stack_m2F0, local_rsp - 584 - 104, a3, a4);
    if (sign_flag) goto loc_007D3D96;
    if ((*(uint32_t *)(arg1)) >= 0) goto loc_007D3D96;
    *(uint64_t *)(local_rsp - 0x248 - 0x70) = (uint32_t)(*(uint32_t *)(local_rsp - 0x248 - 0x68));
    goto loc_007D3DA3;
loc_007D3D96:
    *(uint64_t *)(local_rsp - 0x248 - 0x70) = (uint32_t)(v_stack_m2F0);
loc_007D3DA3:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) == 256) goto loc_007D3DC3;
    a2 = 0;
    result = CMFCreateSecurityDescriptor(v_stack_m2E8, a2, a3, a4);
    result = (uint32_t)((result) & ((uint32_t)(v_stack_m2E8)));
    if (((uint32_t)(result)) == ((uint32_t)(v_stack_m2E8))) goto loc_007D3C39;
loc_007D3DC3:
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x40) = v_stack_m2E8;
    v_stack_m318 = v_stack_m2E0;
    *(uint64_t *)(local_rsp - 0x248 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x248 - 0x38) = 0;
    v_stack_m320 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m328 = 4;
    *(uint32_t *)(local_rsp - 0x248 - 0x60) = 48;
    *(uint32_t *)(local_rsp - 0x248 - 0x48) = 576;
    result = ZwCreateSection(local_rsp - 584 - 120, Arg1 + 6, local_rsp - 584 - 96, v_stack_m2F0);
    local_r12 = 0;
    if (!sign_flag) goto loc_007D3E42;
    if ((*(uint8_t *)(arg1 + 0xC)) == 0) goto loc_007D3E39;
    if (!sign_flag) goto loc_007D3E39;
    *(uint64_t *)(local_rsp - 0x248 - 0x70) = (uint32_t)(v_stack_m2F0);
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    goto loc_007D3DC3;
loc_007D3E39:
    *(uint64_t *)(local_rsp - 0x248 - 0x78) = v_stack_m2F0;
    goto loc_007D3C39;
loc_007D3E42:
    a4 = 0;
    v_stack_m320 = v_stack_m2F0;
    v_stack_m328 = v_stack_m2E0;
    v_stack_m2E0 = v_stack_m2F0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(local_rsp - 0x248 - 0x78), (uint32_t)(0xF001FULL), *(uint64_t *)(v_rip + 0x7F2D8F), a4);
    result = (uint32_t)((result) & ((uint32_t)(v_stack_m2E8)));
    if (((uint32_t)(result)) != ((uint32_t)(v_stack_m2E8))) goto loc_007D3E83;
    goto loc_007D3C39;
loc_007D3E83:
    if ((*(uint8_t *)(arg1 + 0xC)) == ((uint8_t)(v_stack_m2F0))) goto loc_007D3F89;
    v_stack_m300 = 4;
    v_stack_m308 = 0x400000ULL;
    a4 = 0;
    v_stack_m310 = 2;
    a2 = ((uint32_t)(0xF001FULL)) | (-1);
    v_stack_m318 = local_rsp - 584 - 112;
    v_stack_m320 = v_stack_m2F0;
    v_stack_m328 = v_stack_m2F0;
    v_stack_m2F0 = v_stack_m2F0;
    result = ZwMapViewOfSection(*(uint64_t *)(local_rsp - 0x248 - 0x78), a2, v_stack_m2D8, a4);
    result = (uint32_t)((result) & ((uint32_t)(v_stack_m2E8)));
    if (((uint32_t)(result)) != ((uint32_t)(v_stack_m2E8))) goto loc_007D3EE9;
    v_stack_m2D8 = v_stack_m2F0;
    goto loc_007D3C39;
loc_007D3EE9:
    if (v_stack_m2F8 != ((uint8_t)(v_stack_m2F0))) goto loc_007D3F53;
    a4 = 0;
    v_stack_m308 = v_stack_m2F0;
    a3 = 0;
    v_stack_m310 = v_stack_m2F0;
    v_stack_m318 = (uint32_t)((uint32_t)(v_stack_m2F0));
    v_stack_m320 = v_stack_m2D8;
    v_stack_m328 = local_rsp - 584 - 48;
    v_stack_m2F0 = v_stack_m2F0;
    result = ZwReadFile(v_stack_m2D0, *(uint64_t *)(local_rsp - 0x248 - 0x80), a3, a4);
    if (sign_flag) goto loc_007D3C39;
    a3 = 0;
    a2 = 0;
    result = ZwWaitForSingleObject(*(uint64_t *)(local_rsp - 0x248 - 0x80), a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_007D3F76;
    goto loc_007D3CD9;
loc_007D3F53:
    *(uint32_t *)(result + 0x4C) = (uint32_t)(v_stack_m2F0);
    result = CMFReadCompressedSegment(v_stack_m2D0, v_stack_m2D8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    if (sign_flag) goto loc_007D3C39;
loc_007D3F76:
    Arg1 = (v_stack_m2D0) | (-1);
    result = ZwUnmapViewOfSection(Arg1, v_stack_m2D8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    v_stack_m2D8 = v_stack_m2F0;
loc_007D3F89:
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_007D3C39;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28)) = v_stack_m2F0;
    if ((*(uint32_t *)(arg1 + 0x30)) != 16) goto loc_007D3C39;
    if ((*(uint32_t *)(v_rip + 0x63AC54)) != 0x2710ULL) goto loc_007D3C39;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) & (15));
    *(uint32_t *)(v_rip + 0x63AC39) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    goto loc_007D3C39;
loc_007D3FD0:
loc_007D3FD5:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x4));
    if (*(uint64_t *)(local_rsp - 0x248 - 0x80) != 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x248 - 0x80), v_stack_m2D8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    }
    if (v_stack_m2D8 != 0) {
        Arg1 = (*(uint64_t *)(local_rsp - 0x248 - 0x80)) | (-1);
        result = ZwUnmapViewOfSection(Arg1, v_stack_m2D8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    }
    if (*(uint64_t *)(local_rsp - 0x248 - 0x78) != 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x248 - 0x78), v_stack_m2D8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    }
    if (v_stack_m2D0 != 0) {
        result = ZwClose(v_stack_m2D0, v_stack_m2D8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    }
    if (v_stack_m2E8 != 0) {
        a2 = 0;
        Arg1 = v_stack_m2E8;
        result = ExFreePoolWithTag(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    }
    if (v_stack_m2F0 != 0) {
        Arg1 = v_stack_m2F0;
        result = ObfDereferenceObject(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    }
    if (result != 0) {
        a2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0))), result);
    }
    *(uint32_t *)(arg1 + 0x24) = (uint32_t)((uint32_t)(0xC000000DULL));
    if (*(uint64_t *)(arg1 + 0x10) != 0) {
        a3 = 0;
        a2 = a3 + 1;
        result = KeSetEvent(*(uint64_t *)(arg1 + 0x10), a2, a3, result);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x248 + 0x210)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, result);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xC` | `8` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R/W` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D3A70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
