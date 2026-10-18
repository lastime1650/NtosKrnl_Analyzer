# MiResolveImageReferences

- RVA: `0x00A23BE4`–`0x00A23FFE` (길이 `1,050` bytes)
- VA: `0x0000000140A23BE4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AB748`
- 디코드: `276`개 명령, `1,050/1,050` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A23C73` → [RtlImageDirectoryEntryToData](../../text/43/RtlImageDirectoryEntryToData_function_004328D0.md) (function, `0x004328D0`)
- `0x00A23CC9` → [MiAllocateImportList](MiAllocateImportList_function_00A243F4.md) (function, `0x00A243F4`)
- `0x00A23D09` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (function, `0x00470F40`)
- `0x00A23D19` → [RtlAnsiStringToUnicodeString](../90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (function, `0x0090BEA0`)
- `0x00A23D37` → [PsQueryCurrentApiSetSchema](PsQueryCurrentApiSetSchema_function_00A24300.md) (function, `0x00A24300`)
- `0x00A23D55` → [ApiSetResolveToHost](../../text/4C/ApiSetResolveToHost_function_004C8AA8.md) (function, `0x004C8AA8`)
- `0x00A23DB9` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00A23DDA` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (function, `0x004D9D34`)
- `0x00A23E24` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00A23E53` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00A23E98` → [MiCompressImportList](MiCompressImportList_function_00A24344.md) (function, `0x00A24344`)
- `0x00A23EF1` → [MiSnapThunk](MiSnapThunk_function_00A24004.md) (function, `0x00A24004`)
- `0x00A23F17` → [MiSnapUnresolvedImport](MiSnapUnresolvedImport_function_00A24438.md) (function, `0x00A24438`)
- `0x00A23F32` → [MiLogFailedDriverLoad](MiLogFailedDriverLoad_function_00A24ACC.md) (function, `0x00A24ACC`)
- `0x00A23F4D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00A23F86` → [RtlDuplicateUnicodeString](../93/RtlDuplicateUnicodeString_function_009321F0.md) (function, `0x009321F0`)
- `0x00A23FA2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A23FDF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiResolveImageImports](../7F/MiResolveImageImports_function_007F8144.md) at `0x007F81B5`

### Static image references
- `0x00A23C1B` → RVA `0x00B09CC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A23D8B` → RVA `0x00EF54C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00A23C73` → [RtlImageDirectoryEntryToData](../../text/43/RtlImageDirectoryEntryToData_function_004328D0.md) (`PAGE` → `.text`)
  - `0x00A23D09` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (`PAGE` → `.text`)
  - `0x00A23D55` → [ApiSetResolveToHost](../../text/4C/ApiSetResolveToHost_function_004C8AA8.md) (`PAGE` → `.text`)
  - `0x00A23DDA` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (`PAGE` → `.text`)
  - `0x00A23E24` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00A23E53` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00A23F4D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00A23FA2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A23FDF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00A23D77` → [sub_00B37A8C](../B3/Unknown_function_00B37A8C.md) (`tail-transfer`)
  - `0x00A23DA8` → [sub_00B37A8C + 0xC4](../B3/Unknown_function_00B37A8C.md) (`tail-transfer`)
  - `0x00A23DD1` → [sub_00B37A8C + 0xC4](../B3/Unknown_function_00B37A8C.md) (`tail-transfer`)
  - `0x00A23FC6` → [sub_00B37A8C + 0x1D2](../B3/Unknown_function_00B37A8C.md) (`tail-transfer`)
  - `0x00A23FEF` → [sub_00B37A8C + 0x1F5](../B3/Unknown_function_00B37A8C.md) (`tail-transfer`)
  - `0x00A23FF9` → [sub_00B37A8C + 0x1F5](../B3/Unknown_function_00B37A8C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A23BE4  48 8B C4                        mov rax, rsp
00A23BE7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00A23BEB  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00A23BEF  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00A23BF3  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A23BF7  55                              push rbp
00A23BF8  53                              push rbx
00A23BF9  56                              push rsi
00A23BFA  57                              push rdi
00A23BFB  41 54                           push r12
00A23BFD  41 55                           push r13
00A23BFF  41 56                           push r14
00A23C01  41 57                           push r15
00A23C03  48 8D 68 A9                     lea rbp, [rax - 0x57]
00A23C07  48 81 EC E8 00 00 00            sub rsp, 0xe8
00A23C0E  48 8B F1                        mov rsi, rcx
00A23C11  48 C7 45 DF 3A 00 3C 00         mov qword ptr [rbp - 0x21], 0x3c003a
00A23C19  33 C9                           xor ecx, ecx
00A23C1B  48 8D 05 9E 60 0E 00            lea rax, [rip + 0xe609e]
00A23C22  0F 57 C0                        xorps xmm0, xmm0
00A23C25  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00A23C29  33 C0                           xor eax, eax
00A23C2B  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
00A23C2F  48 8B 5E 30                     mov rbx, qword ptr [rsi + 0x30]
00A23C33  4C 8D 4D 87                     lea r9, [rbp - 0x79]
00A23C37  48 C7 86 88 00 00 00 FE FF FF FF  mov qword ptr [rsi + 0x88], 0xfffffffffffffffe
00A23C42  4D 8B F0                        mov r14, r8
00A23C45  8D 71 01                        lea esi, [rcx + 1]
00A23C48  89 45 F3                        mov dword ptr [rbp - 0xd], eax
00A23C4B  0F 57 C9                        xorps xmm1, xmm1
00A23C4E  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
00A23C52  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
00A23C56  44 8B C6                        mov r8d, esi
00A23C59  88 4C 24 41                     mov byte ptr [rsp + 0x41], cl
00A23C5D  40 8A D6                        mov dl, sil
00A23C60  48 8B CB                        mov rcx, rbx
00A23C63  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
00A23C67  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00A23C6B  0F 11 4D 8F                     movups xmmword ptr [rbp - 0x71], xmm1
00A23C6F  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
00A23C73  E8 58 EC A0 FF                  call 0x1404328d0
00A23C78  45 33 C0                        xor r8d, r8d
00A23C7B  4C 8B E0                        mov r12, rax
00A23C7E  48 85 C0                        test rax, rax
00A23C81  0F 84 21 02 00 00               je 0x140a23ea8
00A23C87  45 8B F8                        mov r15d, r8d
00A23C8A  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
00A23C8F  41 8B F8                        mov edi, r8d
00A23C92  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
00A23C97  45 8B E8                        mov r13d, r8d
00A23C9A  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
00A23C9F  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
00A23CA3  41 8B C8                        mov ecx, r8d
00A23CA6  44 39 40 0C                     cmp dword ptr [rax + 0xc], r8d
00A23CAA  0F 84 0F 02 00 00               je 0x140a23ebf
00A23CB0  44 39 00                        cmp dword ptr [rax], r8d
00A23CB3  74 0C                           je 0x140a23cc1
00A23CB5  48 83 C0 14                     add rax, 0x14
00A23CB9  03 CE                           add ecx, esi
00A23CBB  44 39 40 0C                     cmp dword ptr [rax + 0xc], r8d
00A23CBF  75 EF                           jne 0x140a23cb0
00A23CC1  85 C9                           test ecx, ecx
00A23CC3  0F 84 F6 01 00 00               je 0x140a23ebf
00A23CC9  E8 26 07 00 00                  call 0x140a243f4
00A23CCE  45 33 C0                        xor r8d, r8d
00A23CD1  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00A23CD5  48 8B C8                        mov rcx, rax
00A23CD8  48 85 C0                        test rax, rax
00A23CDB  0F 84 81 02 00 00               je 0x140a23f62
00A23CE1  4C 8B E9                        mov r13, rcx
00A23CE4  41 8B 44 24 0C                  mov eax, dword ptr [r12 + 0xc]
00A23CE9  85 C0                           test eax, eax
00A23CEB  0F 84 A3 01 00 00               je 0x140a23e94
00A23CF1  45 39 04 24                     cmp dword ptr [r12], r8d
00A23CF5  0F 84 99 01 00 00               je 0x140a23e94
00A23CFB  48 8D 3C 03                     lea rdi, [rbx + rax]
00A23CFF  4D 8B F8                        mov r15, r8
00A23D02  48 8B D7                        mov rdx, rdi
00A23D05  48 8D 4D FF                     lea rcx, [rbp - 1]
00A23D09  E8 32 D2 A4 FF                  call 0x140470f40
00A23D0E  44 8A C6                        mov r8b, sil
00A23D11  48 8D 55 FF                     lea rdx, [rbp - 1]
00A23D15  48 8D 4D 8F                     lea rcx, [rbp - 0x71]
00A23D19  E8 82 81 EE FF                  call 0x14090bea0
00A23D1E  33 C9                           xor ecx, ecx
00A23D20  8B D8                           mov ebx, eax
00A23D22  85 C0                           test eax, eax
00A23D24  0F 88 A1 02 00 00               js 0x140a23fcb
00A23D2A  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
00A23D2E  48 85 F6                        test rsi, rsi
00A23D31  0F 84 7D 02 00 00               je 0x140a23fb4
00A23D37  E8 C4 05 00 00                  call 0x140a24300
00A23D3C  4C 8B 45 67                     mov r8, qword ptr [rbp + 0x67]
00A23D40  4C 8D 4C 24 41                  lea r9, [rsp + 0x41]
00A23D45  48 8B C8                        mov rcx, rax
00A23D48  48 8D 55 8F                     lea rdx, [rbp - 0x71]
00A23D4C  48 8D 45 BF                     lea rax, [rbp - 0x41]
00A23D50  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A23D55  E8 4E 4D AA FF                  call 0x1404c8aa8
00A23D5A  33 C9                           xor ecx, ecx
00A23D5C  8B D8                           mov ebx, eax
00A23D5E  85 C0                           test eax, eax
00A23D60  0F 88 53 02 00 00               js 0x140a23fb9
00A23D66  38 4C 24 41                     cmp byte ptr [rsp + 0x41], cl
00A23D6A  0F 85 E0 00 00 00               jne 0x140a23e50
00A23D70  89 4D 87                        mov dword ptr [rbp - 0x79], ecx
00A23D73  48 39 4D 77                     cmp qword ptr [rbp + 0x77], rcx
00A23D77  0F 85 0F 3D 11 00               jne 0x140b37a8c
00A23D7D  BF 01 00 00 00                  mov edi, 1
00A23D82  0F 28 45 8F                     movaps xmm0, xmmword ptr [rbp - 0x71]
00A23D86  66 0F 7F 45 AF                  movdqa xmmword ptr [rbp - 0x51], xmm0
00A23D8B  48 8B 1D 2E 17 4D 00            mov rbx, qword ptr [rip + 0x4d172e]
00A23D92  48 8D 45 AF                     lea rax, [rbp - 0x51]
00A23D96  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A23D9B  45 33 C0                        xor r8d, r8d
00A23D9E  48 8D 05 1B 17 4D 00            lea rax, [rip + 0x4d171b]
00A23DA5  48 3B D8                        cmp rbx, rax
00A23DA8  0F 84 A2 3D 11 00               je 0x140b37b50
00A23DAE  48 8D 53 58                     lea rdx, [rbx + 0x58]
00A23DB2  44 8A C7                        mov r8b, dil
00A23DB5  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00A23DB9  E8 62 EC F0 FF                  call 0x140932a20
00A23DBE  45 33 C0                        xor r8d, r8d
00A23DC1  84 C0                           test al, al
00A23DC3  75 05                           jne 0x140a23dca
00A23DC5  48 8B 1B                        mov rbx, qword ptr [rbx]
00A23DC8  EB D4                           jmp 0x140a23d9e
00A23DCA  4C 8B 7B 30                     mov r15, qword ptr [rbx + 0x30]
00A23DCE  4D 85 FF                        test r15, r15
00A23DD1  0F 84 79 3D 11 00               je 0x140b37b50
00A23DD7  48 8B CB                        mov rcx, rbx
00A23DDA  E8 55 5F AB FF                  call 0x1404d9d34
00A23DDF  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
00A23DE5  84 C9                           test cl, cl
00A23DE7  0F 88 D4 01 00 00               js 0x140a23fc1
00A23DED  F7 43 68 00 10 00 00            test dword ptr [rbx + 0x68], 0x1000
00A23DF4  75 0D                           jne 0x140a23e03
00A23DF6  48 39 BB 88 00 00 00            cmp qword ptr [rbx + 0x88], rdi
00A23DFD  74 0D                           je 0x140a23e0c
00A23DFF  66 01 7B 6C                     add word ptr [rbx + 0x6c], di
00A23E03  48 39 BB 88 00 00 00            cmp qword ptr [rbx + 0x88], rdi
00A23E0A  75 67                           jne 0x140a23e73
00A23E0C  41 8B 04 24                     mov eax, dword ptr [r12]
00A23E10  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00A23E14  85 C0                           test eax, eax
00A23E16  0F 85 AF 00 00 00               jne 0x140a23ecb
00A23E1C  48 85 F6                        test rsi, rsi
00A23E1F  74 12                           je 0x140a23e33
00A23E21  48 8B CE                        mov rcx, rsi
00A23E24  E8 27 EA 15 00                  call 0x140b82850
00A23E29  0F 57 C0                        xorps xmm0, xmm0
00A23E2C  45 33 C0                        xor r8d, r8d
00A23E2F  0F 11 45 8F                     movups xmmword ptr [rbp - 0x71], xmm0
00A23E33  44 38 44 24 40                  cmp byte ptr [rsp + 0x40], r8b
00A23E38  0F 85 5E 01 00 00               jne 0x140a23f9c
00A23E3E  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
00A23E42  49 83 C4 14                     add r12, 0x14
00A23E46  BE 01 00 00 00                  mov esi, 1
00A23E4B  E9 94 FE FF FF                  jmp 0x140a23ce4
00A23E50  48 8B CE                        mov rcx, rsi
00A23E53  E8 F8 E9 15 00                  call 0x140b82850
00A23E58  45 33 C0                        xor r8d, r8d
00A23E5B  0F 57 C0                        xorps xmm0, xmm0
00A23E5E  0F 11 45 8F                     movups xmmword ptr [rbp - 0x71], xmm0
00A23E62  66 44 39 45 BF                  cmp word ptr [rbp - 0x41], r8w
00A23E67  0F 85 03 01 00 00               jne 0x140a23f70
00A23E6D  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00A23E71  EB CF                           jmp 0x140a23e42
00A23E73  F7 43 68 00 10 00 00            test dword ptr [rbx + 0x68], 0x1000
00A23E7A  75 90                           jne 0x140a23e0c
00A23E7C  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
00A23E80  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00A23E84  48 89 5C D1 08                  mov qword ptr [rcx + rdx*8 + 8], rbx
00A23E89  03 D7                           add edx, edi
00A23E8B  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
00A23E8F  E9 78 FF FF FF                  jmp 0x140a23e0c
00A23E94  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00A23E98  E8 A7 04 00 00                  call 0x140a24344
00A23E9D  48 8B 4D 5F                     mov rcx, qword ptr [rbp + 0x5f]
00A23EA1  48 89 81 88 00 00 00            mov qword ptr [rcx + 0x88], rax
00A23EA8  33 C0                           xor eax, eax
00A23EAA  48 81 C4 E8 00 00 00            add rsp, 0xe8
00A23EB1  41 5F                           pop r15
00A23EB3  41 5E                           pop r14
00A23EB5  41 5D                           pop r13
00A23EB7  41 5C                           pop r12
00A23EB9  5F                              pop rdi
00A23EBA  5E                              pop rsi
00A23EBB  5B                              pop rbx
00A23EBC  5D                              pop rbp
00A23EBD  C3                              ret
00A23EBE  CC                              int3
00A23EBF  49 8B C8                        mov rcx, r8
00A23EC2  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
00A23EC6  E9 16 FE FF FF                  jmp 0x140a23ce1
00A23ECB  45 8B 74 24 10                  mov r14d, dword ptr [r12 + 0x10]
00A23ED0  48 8D 3C 03                     lea rdi, [rbx + rax]
00A23ED4  4C 03 F3                        add r14, rbx
00A23ED7  4C 39 07                        cmp qword ptr [rdi], r8
00A23EDA  0F 84 3C FF FF FF               je 0x140a23e1c
00A23EE0  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00A23EE5  4D 8B CE                        mov r9, r14
00A23EE8  4C 8B C7                        mov r8, rdi
00A23EEB  48 8B D3                        mov rdx, rbx
00A23EEE  49 8B CF                        mov rcx, r15
00A23EF1  E8 0E 01 00 00                  call 0x140a24004
00A23EF6  45 33 C0                        xor r8d, r8d
00A23EF9  8B D8                           mov ebx, eax
00A23EFB  85 C0                           test eax, eax
00A23EFD  78 0E                           js 0x140a23f0d
00A23EFF  48 8B 5D 9F                     mov rbx, qword ptr [rbp - 0x61]
00A23F03  48 83 C7 08                     add rdi, 8
00A23F07  49 83 C6 08                     add r14, 8
00A23F0B  EB CA                           jmp 0x140a23ed7
00A23F0D  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00A23F11  4D 8B C7                        mov r8, r15
00A23F14  48 8B D7                        mov rdx, rdi
00A23F17  E8 1C 05 00 00                  call 0x140a24438
00A23F1C  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00A23F21  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
00A23F25  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
00A23F29  44 8B CB                        mov r9d, ebx
00A23F2C  4C 8B C0                        mov r8, rax
00A23F2F  49 8B D7                        mov rdx, r15
00A23F32  E8 95 0B 00 00                  call 0x140a24acc
00A23F37  45 33 FF                        xor r15d, r15d
00A23F3A  44 38 7C 24 40                  cmp byte ptr [rsp + 0x40], r15b
00A23F3F  0F 85 94 00 00 00               jne 0x140a23fd9
00A23F45  48 85 F6                        test rsi, rsi
00A23F48  74 08                           je 0x140a23f52
00A23F4A  48 8B CE                        mov rcx, rsi
00A23F4D  E8 FE E8 15 00                  call 0x140b82850
00A23F52  4D 85 ED                        test r13, r13
00A23F55  0F 85 8E 00 00 00               jne 0x140a23fe9
00A23F5B  8B C3                           mov eax, ebx
00A23F5D  E9 48 FF FF FF                  jmp 0x140a23eaa
00A23F62  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
00A23F66  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A23F6B  48 8B C7                        mov rax, rdi
00A23F6E  EB B5                           jmp 0x140a23f25
00A23F70  B8 00 00 00 80                  mov eax, 0x80000000
00A23F75  4C 8D 45 8F                     lea r8, [rbp - 0x71]
00A23F79  48 8D 55 BF                     lea rdx, [rbp - 0x41]
00A23F7D  89 45 87                        mov dword ptr [rbp - 0x79], eax
00A23F80  33 C9                           xor ecx, ecx
00A23F82  4C 8D 75 DF                     lea r14, [rbp - 0x21]
00A23F86  E8 65 E2 F0 FF                  call 0x1409321f0
00A23F8B  33 C9                           xor ecx, ecx
00A23F8D  8B D8                           mov ebx, eax
00A23F8F  85 C0                           test eax, eax
00A23F91  78 38                           js 0x140a23fcb
00A23F93  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
00A23F97  E9 D7 FD FF FF                  jmp 0x140a23d73
00A23F9C  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00A23FA0  33 D2                           xor edx, edx
00A23FA2  E8 C9 E8 15 00                  call 0x140b82870
00A23FA7  45 33 C0                        xor r8d, r8d
00A23FAA  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
00A23FAF  E9 8A FE FF FF                  jmp 0x140a23e3e
00A23FB4  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A23FB9  48 8B C1                        mov rax, rcx
00A23FBC  E9 60 FF FF FF                  jmp 0x140a23f21
00A23FC1  BB C0 04 00 C0                  mov ebx, 0xc00004c0
00A23FC6  E9 93 3C 11 00                  jmp 0x140b37c5e
00A23FCB  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
00A23FCF  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00A23FD4  E9 48 FF FF FF                  jmp 0x140a23f21
00A23FD9  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00A23FDD  33 D2                           xor edx, edx
00A23FDF  E8 8C E8 15 00                  call 0x140b82870
00A23FE4  E9 5C FF FF FF                  jmp 0x140a23f45
00A23FE9  8B C7                           mov eax, edi
00A23FEB  49 3B 45 00                     cmp rax, qword ptr [r13]
00A23FEF  0F 84 8C 3C 11 00               je 0x140b37c81
00A23FF5  49 89 45 00                     mov qword ptr [r13], rax
00A23FF9  E9 83 3C 11 00                  jmp 0x140b37c81
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiResolveImageReferences(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (232);
    *(unsigned __int64 *)(v_rsp - 87 - 33) = 0x3C003AULL;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 25) = v_rip + 942238;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 81) = 0;
    *(unsigned __int64 *)(a1 + 136) = -2;
    *(unsigned int *)(v_rsp - 87 - 13) = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 49) = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 17) = 0;
    v_stack_mE7 = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 97) = *(unsigned __int64 *)(a1 + 48);
    *(unsigned __int64 *)(v_rsp - 87 - 1) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 87 - 113) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 87 - 65) = v_xmm0;
    result = RtlImageDirectoryEntryToData(*(unsigned __int64 *)(a1 + 48), (unsigned __int8)(a1 + 1), (unsigned int)((unsigned int)(a1 + 1)), v_rsp - 87 - 121);
    a3 = 0;
    if (result == 0) goto loc_00A23EA8;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mE4 = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 73) = 0;
    if ((*(unsigned int *)(result + 12)) == 0) goto loc_00A23EBF;
loc_00A23CB0:
    if ((*(unsigned int *)(result)) == 0) goto loc_00A23CC1;
    result = (result) + (20);
    a1 = (unsigned int)((0) + ((unsigned int)(a1 + 1)));
    if ((*(unsigned int *)(result + 12)) != 0) goto loc_00A23CB0;
loc_00A23CC1:
    if ((unsigned int)(a1) == 0) goto loc_00A23EBF;
    result = MiAllocateImportList(a1, (unsigned __int8)(a1 + 1), a3, v_rsp - 87 - 121);
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 41) = result;
    if (result == 0) goto loc_00A23F62;
loc_00A23CE1:
loc_00A23CE4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 12))) == 0) goto loc_00A23E94;
    if ((*(unsigned int *)(result)) == 0) goto loc_00A23E94;
    result = RtlInitAnsiString(v_rsp - 87 - 1, *(unsigned __int64 *)(a1 + 48) + (unsigned int)(*(unsigned int *)(result + 12)) * 1, a3, v_rsp - 87 - 121);
    result = RtlAnsiStringToUnicodeString(v_rsp - 87 - 113, v_rsp - 87 - 1, (unsigned __int8)(a1 + 1), v_rsp - 87 - 121);
    a1 = 0;
    if (sign_flag) goto loc_00A23FCB;
    if (*(unsigned __int64 *)(v_rsp - 87 - 105) == 0) goto loc_00A23FB4;
    result = PsQueryCurrentApiSetSchema(a1, v_rsp - 87 - 1, (unsigned __int8)(a1 + 1), v_rsp - 87 - 121);
    v_stack_m108 = v_rsp - 87 - 65;
    result = ApiSetResolveToHost(result, v_rsp - 87 - 113, *(unsigned __int64 *)(v_rsp - 87 + 103), v_stack_mE7);
    a1 = 0;
    if (sign_flag) goto loc_00A23FB9;
    if (v_stack_mE7 != 0) goto loc_00A23E50;
    *(unsigned int *)(v_rsp - 87 - 121) = 0;
loc_00A23D73:
    *(unsigned __int64 *)(v_rsp - 87 - 81) = v_xmm0;
    v_stack_mD8 = v_rsp - 87 - 81;
    a3 = 0;
loc_00A23D9E:
    result = RtlEqualUnicodeString(v_rsp - 87 - 81, *(unsigned __int64 *)(v_rip + 5052206) + 88, 1, v_stack_mE7);
    a3 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00A23DCA;
    goto loc_00A23D9E;
loc_00A23DCA:
    result = MiGetBaseLoaderPortion(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5052206)), *(unsigned __int64 *)(v_rip + 5052206) + 88, a3, v_stack_mE7);
    if (sign_flag) goto loc_00A23FC1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5052206)) + 104)) & (0x1000ULL)) != 0) goto loc_00A23E03;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5052206)) + 136)) == 1) goto loc_00A23E0C;
loc_00A23E03:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5052206)) + 136)) != 1) goto loc_00A23E73;
loc_00A23E0C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) != 0) goto loc_00A23ECB;
loc_00A23E1C:
    result = (unsigned int)(*(unsigned int *)(result));
    if (*(unsigned __int64 *)(v_rsp - 87 - 105) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 87 - 105);
        result = ExFreePool(a1, *(unsigned __int64 *)(v_rip + 5052206) + 88, a3, v_stack_mE7);
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 87 - 113) = v_xmm0;
    }
    if (v_stack_mE8 != 0) goto loc_00A23F9C;
loc_00A23E3E:
loc_00A23E42:
    v_r12 = (result) + (20);
    goto loc_00A23CE4;
loc_00A23E50:
    result = ExFreePool(1, *(unsigned __int64 *)(v_rip + 5052206) + 88, a3, v_stack_mE7);
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 87 - 113) = v_xmm0;
    if ((*(unsigned __int16 *)(v_rsp - 87 - 65)) != 0) goto loc_00A23F70;
    goto loc_00A23E42;
loc_00A23E73:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 87 - 97) + 104)) & (0x1000ULL)) != 0) goto loc_00A23E0C;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 - 41) + (unsigned int)(v_stack_mE4) * 8 + 8) = *(unsigned __int64 *)(v_rsp - 87 - 97);
    a2 = (unsigned int)(((unsigned int)(v_stack_mE4)) + (1));
    v_stack_mE4 = (unsigned int)(a2);
    goto loc_00A23E0C;
loc_00A23E94:
    result = MiCompressImportList(*(unsigned __int64 *)(v_rsp - 87 - 41), a2, a3, v_stack_mE7);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 + 95) + 136) = result;
loc_00A23EA8:
    result = 0;
loc_00A23EAA:
    v_rsp = (v_rsp) + (232);
    return result;
loc_00A23EBF:
    *(unsigned __int64 *)(v_rsp - 87 - 41) = 0;
    goto loc_00A23CE1;
loc_00A23ECB:
    v_r14 = ((unsigned int)(*(unsigned int *)(v_r12 + 16))) + (*(unsigned __int64 *)(v_rsp - 87 - 97));
loc_00A23ED7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 87 - 97) + result * 1)) == 0) goto loc_00A23E1C;
    v_stack_p20 = 0;
    result = MiSnapThunk(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5052206)) + 48), *(unsigned __int64 *)(v_rsp - 87 - 97), *(unsigned __int64 *)(v_rsp - 87 - 97) + result * 1, v_r14);
    a3 = 0;
    if (sign_flag) goto loc_00A23F0D;
    v_rdi = (*(unsigned __int64 *)(v_rsp - 87 - 97) + result * 1) + (8);
    v_r14 = (v_r14) + (8);
    goto loc_00A23ED7;
loc_00A23F0D:
    result = MiSnapUnresolvedImport(*(unsigned __int64 *)(v_rsp - 87 - 97), v_rdi, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5052206)) + 48), v_r14);
loc_00A23F21:
loc_00A23F25:
    result = MiLogFailedDriverLoad(*(unsigned __int64 *)(v_rsp - 87 + 103), v_stack_p50, result, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 87 - 97))));
    v_r15 = 0;
    if (v_stack_p40 != 0) goto loc_00A23FD9;
loc_00A23F45:
    if (1 != 0) {
        a1 = 1;
        result = ExFreePool(a1, v_stack_p50, result, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 87 - 97))));
    }
    if (result != 0) goto loc_00A23FE9;
    goto loc_00A23EAA;
loc_00A23F62:
    goto loc_00A23F25;
loc_00A23F70:
    *(unsigned int *)(v_rsp - 87 - 121) = (unsigned int)((unsigned int)(0x80000000ULL));
    a1 = 0;
    result = RtlDuplicateUnicodeString(a1, v_rsp - 87 - 65, v_rsp - 87 - 113, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 87 - 97))));
    a1 = 0;
    if (sign_flag) goto loc_00A23FCB;
    goto loc_00A23D73;
loc_00A23F9C:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 87 - 73), a2, v_rsp - 87 - 113, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 87 - 97))));
    a3 = 0;
    v_stack_p40 = 0;
    goto loc_00A23E3E;
loc_00A23FB4:
loc_00A23FB9:
    goto loc_00A23F21;
loc_00A23FC1:
loc_00A23FCB:
    goto loc_00A23F21;
loc_00A23FD9:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 87 - 73), a2, a3, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 87 - 97))));
    goto loc_00A23F45;
loc_00A23FE9:
    *(unsigned __int64 *)(result) = (unsigned int)((unsigned int)((unsigned int)(v_stack_p44)));
}
```

## 5. (Beta) C Style

```c
int64_t MiResolveImageReferences(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint64_t v_stack_p20;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (232);
    *(uint64_t *)(local_rsp - 0x57 - 0x21) = 0x3C003AULL;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x19) = v_rip + 942238;
    result = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x51) = 0;
    *(uint64_t *)(arg1 + 0x88) = -2;
    *(uint32_t *)(local_rsp - 0x57 - 0xD) = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x31) = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x11) = 0;
    v_stack_mE7 = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x61) = *(uint64_t *)(arg1 + 0x30);
    *(uint64_t *)(local_rsp - 0x57 - 0x1) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x57 - 0x71) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x57 - 0x41) = v_xmm0;
    result = RtlImageDirectoryEntryToData(*(uint64_t *)(arg1 + 0x30), (uint8_t)(Arg1 + 1), (uint32_t)((uint32_t)(Arg1 + 1)), local_rsp - 87 - 121);
    Arg3 = 0;
    if (result == 0) goto loc_00A23EA8;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mE4 = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x49) = 0;
    if ((*(uint32_t *)(result + 0xC)) == 0) goto loc_00A23EBF;
loc_00A23CB0:
    if ((*(uint32_t *)(result)) == 0) goto loc_00A23CC1;
    result = (result) + (20);
    Arg1 = (uint32_t)((0) + ((uint32_t)(Arg1 + 1)));
    if ((*(uint32_t *)(result + 0xC)) != 0) goto loc_00A23CB0;
loc_00A23CC1:
    if ((uint32_t)(Arg1) == 0) goto loc_00A23EBF;
    result = MiAllocateImportList(Arg1, (uint8_t)(Arg1 + 1), Arg3, local_rsp - 87 - 121);
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x29) = result;
    if (result == 0) goto loc_00A23F62;
loc_00A23CE1:
loc_00A23CE4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC))) == 0) goto loc_00A23E94;
    if ((*(uint32_t *)(result)) == 0) goto loc_00A23E94;
    result = RtlInitAnsiString(local_rsp - 87 - 1, *(uint64_t *)(arg1 + 0x30) + (uint32_t)(*(uint32_t *)(result + 0xC)) * 1, Arg3, local_rsp - 87 - 121);
    result = RtlAnsiStringToUnicodeString(local_rsp - 87 - 113, local_rsp - 87 - 1, (uint8_t)(Arg1 + 1), local_rsp - 87 - 121);
    Arg1 = 0;
    if (sign_flag) goto loc_00A23FCB;
    if (*(uint64_t *)(local_rsp - 0x57 - 0x69) == 0) goto loc_00A23FB4;
    result = PsQueryCurrentApiSetSchema(Arg1, local_rsp - 87 - 1, (uint8_t)(Arg1 + 1), local_rsp - 87 - 121);
    v_stack_m108 = local_rsp - 87 - 65;
    result = ApiSetResolveToHost(result, local_rsp - 87 - 113, *(uint64_t *)(local_rsp - 0x57 + 0x67), v_stack_mE7);
    Arg1 = 0;
    if (sign_flag) goto loc_00A23FB9;
    if (v_stack_mE7 != 0) goto loc_00A23E50;
    *(uint32_t *)(local_rsp - 0x57 - 0x79) = 0;
loc_00A23D73:
    *(uint64_t *)(local_rsp - 0x57 - 0x51) = v_xmm0;
    v_stack_mD8 = local_rsp - 87 - 81;
    Arg3 = 0;
loc_00A23D9E:
    result = RtlEqualUnicodeString(local_rsp - 87 - 81, *(uint64_t *)(v_rip + 0x4D172E) + 88, 1, v_stack_mE7);
    Arg3 = 0;
    if ((uint8_t)(result) != 0) goto loc_00A23DCA;
    goto loc_00A23D9E;
loc_00A23DCA:
    result = MiGetBaseLoaderPortion(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4D172E)), *(uint64_t *)(v_rip + 0x4D172E) + 88, Arg3, v_stack_mE7);
    if (sign_flag) goto loc_00A23FC1;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4D172E)) + 0x68)) & (0x1000ULL)) != 0) goto loc_00A23E03;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4D172E)) + 0x88)) == 1) goto loc_00A23E0C;
loc_00A23E03:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4D172E)) + 0x88)) != 1) goto loc_00A23E73;
loc_00A23E0C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) != 0) goto loc_00A23ECB;
loc_00A23E1C:
    result = (uint32_t)(*(uint32_t *)(result));
    if (*(uint64_t *)(local_rsp - 0x57 - 0x69) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x57 - 0x69);
        result = ExFreePool(Arg1, *(uint64_t *)(v_rip + 0x4D172E) + 88, Arg3, v_stack_mE7);
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x57 - 0x71) = v_xmm0;
    }
    if (v_stack_mE8 != 0) goto loc_00A23F9C;
loc_00A23E3E:
loc_00A23E42:
    local_r12 = (result) + (20);
    goto loc_00A23CE4;
loc_00A23E50:
    result = ExFreePool(1, *(uint64_t *)(v_rip + 0x4D172E) + 88, Arg3, v_stack_mE7);
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x57 - 0x71) = v_xmm0;
    if ((*(uint16_t *)(local_rsp - 0x57 - 0x41)) != 0) goto loc_00A23F70;
    goto loc_00A23E42;
loc_00A23E73:
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x57 - 0x61) + 0x68)) & (0x1000ULL)) != 0) goto loc_00A23E0C;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 - 0x29) + (uint32_t)(v_stack_mE4) * 8 + 0x8) = *(uint64_t *)(local_rsp - 0x57 - 0x61);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mE4)) + (1));
    v_stack_mE4 = (uint32_t)(Arg2);
    goto loc_00A23E0C;
loc_00A23E94:
    result = MiCompressImportList(*(uint64_t *)(local_rsp - 0x57 - 0x29), Arg2, Arg3, v_stack_mE7);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 + 0x5F) + 0x88) = result;
loc_00A23EA8:
    result = 0;
loc_00A23EAA:
    local_rsp = (local_rsp) + (232);
    return result;
loc_00A23EBF:
    *(uint64_t *)(local_rsp - 0x57 - 0x29) = 0;
    goto loc_00A23CE1;
loc_00A23ECB:
    local_r14 = ((uint32_t)(*(uint32_t *)(local_r12 + 0x10))) + (*(uint64_t *)(local_rsp - 0x57 - 0x61));
loc_00A23ED7:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x57 - 0x61) + result * 1)) == 0) goto loc_00A23E1C;
    v_stack_p20 = 0;
    result = MiSnapThunk(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4D172E)) + 0x30), *(uint64_t *)(local_rsp - 0x57 - 0x61), *(uint64_t *)(local_rsp - 0x57 - 0x61) + result * 1, local_r14);
    Arg3 = 0;
    if (sign_flag) goto loc_00A23F0D;
    local_rdi = (*(uint64_t *)(local_rsp - 0x57 - 0x61) + result * 1) + (8);
    local_r14 = (local_r14) + (8);
    goto loc_00A23ED7;
loc_00A23F0D:
    result = MiSnapUnresolvedImport(*(uint64_t *)(local_rsp - 0x57 - 0x61), local_rdi, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4D172E)) + 0x30), local_r14);
loc_00A23F21:
loc_00A23F25:
    result = MiLogFailedDriverLoad(*(uint64_t *)(local_rsp - 0x57 + 0x67), v_stack_p50, result, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x57 - 0x61))));
    local_r15 = 0;
    if (v_stack_p40 != 0) goto loc_00A23FD9;
loc_00A23F45:
    if (1 != 0) {
        Arg1 = 1;
        result = ExFreePool(Arg1, v_stack_p50, result, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x57 - 0x61))));
    }
    if (result != 0) goto loc_00A23FE9;
    goto loc_00A23EAA;
loc_00A23F62:
    goto loc_00A23F25;
loc_00A23F70:
    *(uint32_t *)(local_rsp - 0x57 - 0x79) = (uint32_t)((uint32_t)(0x80000000ULL));
    Arg1 = 0;
    result = RtlDuplicateUnicodeString(Arg1, local_rsp - 87 - 65, local_rsp - 87 - 113, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x57 - 0x61))));
    Arg1 = 0;
    if (sign_flag) goto loc_00A23FCB;
    goto loc_00A23D73;
loc_00A23F9C:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x57 - 0x49), Arg2, local_rsp - 87 - 113, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x57 - 0x61))));
    Arg3 = 0;
    v_stack_p40 = 0;
    goto loc_00A23E3E;
loc_00A23FB4:
loc_00A23FB9:
    goto loc_00A23F21;
loc_00A23FC1:
loc_00A23FCB:
    goto loc_00A23F21;
loc_00A23FD9:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x57 - 0x49), Arg2, Arg3, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x57 - 0x61))));
    goto loc_00A23F45;
loc_00A23FE9:
    *(uint64_t *)(result) = (uint32_t)((uint32_t)((uint32_t)(v_stack_p44)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A23BE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
