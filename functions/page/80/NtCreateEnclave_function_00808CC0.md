# NtCreateEnclave

- RVA: `0x00808CC0`–`0x0080909C` (길이 `988` bytes)
- VA: `0x0000000140808CC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8990`
- 디코드: `241`개 명령, `988/988` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00808E21` → [MiValidateZeroBits](../88/MiValidateZeroBits_function_00884440.md) (function, `0x00884440`)
- `0x00808EA3` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00808EE5` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00808F04` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00808F81` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00808FA6` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00808FED` → [MiCreateEnclave](MiCreateEnclave_function_008083E4.md) (function, `0x008083E4`)
- `0x00809008` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00809015` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00809041` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00809083` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00808CD5` → RVA `0x00E0A740` (`.data`; read)
- `0x00808E02` → RVA `0x00E375B8` (`.data`; read)
- `0x00808F51` → RVA `0x00FC6A98` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00808EA3` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00808F04` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00808FA6` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00809008` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00809015` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00809041` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00809083` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00808CC0  4C 8B DC                        mov r11, rsp
00808CC3  53                              push rbx
00808CC4  56                              push rsi
00808CC5  57                              push rdi
00808CC6  41 54                           push r12
00808CC8  41 55                           push r13
00808CCA  41 56                           push r14
00808CCC  41 57                           push r15
00808CCE  48 81 EC 00 01 00 00            sub rsp, 0x100
00808CD5  48 8B 05 64 1A 60 00            mov rax, qword ptr [rip + 0x601a64]
00808CDC  48 33 C4                        xor rax, rsp
00808CDF  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
00808CE7  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
00808CEF  4C 8B EA                        mov r13, rdx
00808CF2  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00808CF7  4C 8B BC 24 70 01 00 00         mov r15, qword ptr [rsp + 0x170]
00808CFF  4C 8B B4 24 80 01 00 00         mov r14, qword ptr [rsp + 0x180]
00808D07  48 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdx
00808D0F  4D 89 83 60 FF FF FF            mov qword ptr [r11 - 0xa0], r8
00808D16  8B 94 24 78 01 00 00            mov edx, dword ptr [rsp + 0x178]
00808D1D  89 54 24 64                     mov dword ptr [rsp + 0x64], edx
00808D21  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00808D29  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
00808D2F  0F 57 C0                        xorps xmm0, xmm0
00808D32  41 0F 11 43 90                  movups xmmword ptr [r11 - 0x70], xmm0
00808D37  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
00808D3C  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
00808D41  49 83 A3 48 FF FF FF 00         and qword ptr [r11 - 0xb8], 0
00808D49  33 F6                           xor esi, esi
00808D4B  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00808D50  21 74 24 68                     and dword ptr [rsp + 0x68], esi
00808D54  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00808D5D  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00808D63  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00808D67  4D 85 F6                        test r14, r14
00808D6A  74 23                           je 0x140808d8f
00808D6C  3C 01                           cmp al, 1
00808D6E  75 1F                           jne 0x140808d8f
00808D70  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00808D7A  48 8B CB                        mov rcx, rbx
00808D7D  4C 3B F3                        cmp r14, rbx
00808D80  49 0F 42 CE                     cmovb rcx, r14
00808D84  8B 01                           mov eax, dword ptr [rcx]
00808D86  89 01                           mov dword ptr [rcx], eax
00808D88  EB 0F                           jmp 0x140808d99
00808D8A  E9 E9 02 00 00                  jmp 0x140809078
00808D8F  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00808D99  8B 84 24 68 01 00 00            mov eax, dword ptr [rsp + 0x168]
00808DA0  83 E8 01                        sub eax, 1
00808DA3  74 5D                           je 0x140808e02
00808DA5  83 E8 01                        sub eax, 1
00808DA8  74 3D                           je 0x140808de7
00808DAA  83 E8 0E                        sub eax, 0xe
00808DAD  74 05                           je 0x140808db4
00808DAF  83 F8 01                        cmp eax, 1
00808DB2  75 40                           jne 0x140808df4
00808DB4  A1 6C 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff7800000036c]
00808DBD  0F BA E0 08                     bt eax, 8
00808DC1  73 31                           jae 0x140808df4
00808DC3  4C 8B A4 24 60 01 00 00         mov r12, qword ptr [rsp + 0x160]
00808DCB  4D 85 E4                        test r12, r12
00808DCE  74 07                           je 0x140808dd7
00808DD0  BB F3 00 00 C0                  mov ebx, 0xc00000f3
00808DD5  EB 22                           jmp 0x140808df9
00808DD7  83 FA 24                        cmp edx, 0x24
00808DDA  76 07                           jbe 0x140808de3
00808DDC  BB 04 00 00 C0                  mov ebx, 0xc0000004
00808DE1  EB 16                           jmp 0x140808df9
00808DE3  33 FF                           xor edi, edi
00808DE5  EB 32                           jmp 0x140808e19
00808DE7  A1 6C 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff7800000036c]
00808DF0  A8 04                           test al, 4
00808DF2  75 0E                           jne 0x140808e02
00808DF4  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00808DF9  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00808DFD  E9 35 02 00 00                  jmp 0x140809037
00808E02  48 83 3D AE E7 62 00 00         cmp qword ptr [rip + 0x62e7ae], 0
00808E0A  74 E8                           je 0x140808df4
00808E0C  BF 00 10 00 00                  mov edi, 0x1000
00808E11  4C 8B A4 24 60 01 00 00         mov r12, qword ptr [rsp + 0x160]
00808E19  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
00808E21  E8 1A B6 07 00                  call 0x140884440
00808E26  85 C0                           test eax, eax
00808E28  79 07                           jns 0x140808e31
00808E2A  BB F1 00 00 C0                  mov ebx, 0xc00000f1
00808E2F  EB C8                           jmp 0x140808df9
00808E31  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00808E39  48 85 C0                        test rax, rax
00808E3C  75 07                           jne 0x140808e45
00808E3E  BB F2 00 00 C0                  mov ebx, 0xc00000f2
00808E43  EB B4                           jmp 0x140808df9
00808E45  4C 3B E0                        cmp r12, rax
00808E48  77 86                           ja 0x140808dd0
00808E4A  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
00808E4E  80 FA 01                        cmp dl, 1
00808E51  75 10                           jne 0x140808e63
00808E53  48 8B CB                        mov rcx, rbx
00808E56  4C 3B EB                        cmp r13, rbx
00808E59  49 0F 42 CD                     cmovb rcx, r13
00808E5D  48 8B 01                        mov rax, qword ptr [rcx]
00808E60  48 89 01                        mov qword ptr [rcx], rax
00808E63  49 8B 45 00                     mov rax, qword ptr [r13]
00808E67  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00808E6F  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
00808E73  85 C0                           test eax, eax
00808E75  0F 84 B4 00 00 00               je 0x140808f2f
00808E7B  85 FF                           test edi, edi
00808E7D  74 08                           je 0x140808e87
00808E7F  3B C7                           cmp eax, edi
00808E81  0F 85 55 FF FF FF               jne 0x140808ddc
00808E87  48 8B F8                        mov rdi, rax
00808E8A  48 8D 90 FF 0F 00 00            lea rdx, [rax + 0xfff]
00808E91  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00808E98  B9 00 01 00 00                  mov ecx, 0x100
00808E9D  41 B8 4D 6D 45 44               mov r8d, 0x44456d4d
00808EA3  E8 98 26 B5 FF                  call 0x14035b540
00808EA8  48 8B F0                        mov rsi, rax
00808EAB  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00808EB0  48 85 C0                        test rax, rax
00808EB3  75 0A                           jne 0x140808ebf
00808EB5  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00808EBA  E9 3A FF FF FF                  jmp 0x140808df9
00808EBF  80 7C 24 50 01                  cmp byte ptr [rsp + 0x50], 1
00808EC4  75 35                           jne 0x140808efb
00808EC6  48 81 FF 00 00 01 00            cmp rdi, 0x10000
00808ECD  73 10                           jae 0x140808edf
00808ECF  41 F6 C7 03                     test r15b, 3
00808ED3  75 10                           jne 0x140808ee5
00808ED5  4C 3B FB                        cmp r15, rbx
00808ED8  49 0F 42 DF                     cmovb rbx, r15
00808EDC  90                              nop
00808EDD  EB 1A                           jmp 0x140808ef9
00808EDF  41 F6 C7 03                     test r15b, 3
00808EE3  74 06                           je 0x140808eeb
00808EE5  E8 E6 10 09 00                  call 0x140899fd0
00808EEA  CC                              int3
00808EEB  49 8D 04 3F                     lea rax, [r15 + rdi]
00808EEF  48 3B C3                        cmp rax, rbx
00808EF2  77 05                           ja 0x140808ef9
00808EF4  49 3B C7                        cmp rax, r15
00808EF7  73 02                           jae 0x140808efb
00808EF9  8A 03                           mov al, byte ptr [rbx]
00808EFB  4C 8B C7                        mov r8, rdi
00808EFE  49 8B D7                        mov rdx, r15
00808F01  48 8B CE                        mov rcx, rsi
00808F04  E8 37 D9 EB FF                  call 0x1406c6840
00808F09  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
00808F0D  EB 20                           jmp 0x140808f2f
00808F0F  8B D8                           mov ebx, eax
00808F11  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00808F15  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00808F1A  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
00808F22  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00808F2A  E9 08 01 00 00                  jmp 0x140809037
00808F2F  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00808F34  49 83 FF FF                     cmp r15, -1
00808F38  75 17                           jne 0x140808f51
00808F3A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00808F43  48 8B B8 B8 00 00 00            mov rdi, qword ptr [rax + 0xb8]
00808F4A  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00808F4F  EB 5A                           jmp 0x140808fab
00808F51  4C 8B 05 40 DB 7B 00            mov r8, qword ptr [rip + 0x7bdb40]
00808F58  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00808F5E  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00808F64  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00808F69  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00808F6E  C7 44 24 20 4D 6D 56 6D         mov dword ptr [rsp + 0x20], 0x6d566d4d
00808F76  44 8A CA                        mov r9b, dl
00808F79  BA 08 00 00 00                  mov edx, 8
00808F7E  49 8B CF                        mov rcx, r15
00808F81  E8 CA 06 06 00                  call 0x140869650
00808F86  8B D8                           mov ebx, eax
00808F88  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00808F8C  85 C0                           test eax, eax
00808F8E  0F 88 A3 00 00 00               js 0x140809037
00808F94  4C 8D 84 24 C8 00 00 00         lea r8, [rsp + 0xc8]
00808F9C  33 D2                           xor edx, edx
00808F9E  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00808FA3  48 8B CF                        mov rcx, rdi
00808FA6  E8 75 D8 A0 FF                  call 0x140216820
00808FAB  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00808FB0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00808FB5  8B 54 24 64                     mov edx, dword ptr [rsp + 0x64]
00808FB9  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00808FBD  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00808FC2  8B 84 24 68 01 00 00            mov eax, dword ptr [rsp + 0x168]
00808FC9  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00808FCD  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00808FD2  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
00808FDA  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
00808FE2  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
00808FEA  48 8B CF                        mov rcx, rdi
00808FED  E8 F2 F3 FF FF                  call 0x1408083e4
00808FF2  8B D8                           mov ebx, eax
00808FF4  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00808FF8  49 83 FF FF                     cmp r15, -1
00808FFC  74 39                           je 0x140809037
00808FFE  33 D2                           xor edx, edx
00809000  48 8D 8C 24 C8 00 00 00         lea rcx, [rsp + 0xc8]
00809008  E8 23 ED A0 FF                  call 0x140217d30
0080900D  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
00809012  48 8B CF                        mov rcx, rdi
00809015  E8 C6 E8 AE FF                  call 0x1402f78e0
0080901A  EB 1B                           jmp 0x140809037
0080901C  8B D8                           mov ebx, eax
0080901E  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00809022  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00809027  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
0080902F  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00809037  48 85 F6                        test rsi, rsi
0080903A  74 0A                           je 0x140809046
0080903C  33 D2                           xor edx, edx
0080903E  48 8B CE                        mov rcx, rsi
00809041  E8 2A 98 37 00                  call 0x140b82870
00809046  85 DB                           test ebx, ebx
00809048  78 1A                           js 0x140809064
0080904A  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00809052  49 89 45 00                     mov qword ptr [r13], rax
00809056  EB 0C                           jmp 0x140809064
00809058  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
0080905C  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00809064  4D 85 F6                        test r14, r14
00809067  74 0D                           je 0x140809076
00809069  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
0080906D  41 89 06                        mov dword ptr [r14], eax
00809070  EB 04                           jmp 0x140809076
00809072  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
00809076  8B C3                           mov eax, ebx
00809078  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
00809080  48 33 CC                        xor rcx, rsp
00809083  E8 B8 35 EA FF                  call 0x1406ac640
00809088  48 81 C4 00 01 00 00            add rsp, 0x100
0080908F  41 5F                           pop r15
00809091  41 5E                           pop r14
00809093  41 5D                           pop r13
00809095  41 5C                           pop r12
00809097  5F                              pop rdi
00809098  5E                              pop rsi
00809099  5B                              pop rbx
0080909A  C3                              ret
0080909B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateEnclave(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, unsigned int a8, __int64 a9)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 6298212)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mA8 = a4;
    v_stack_mE0 = a1;
    v_stack_m98 = a2;
    *(unsigned __int64 *)(v_rsp - 160) = a3;
    v_stack_mD4 = (unsigned int)((unsigned int)(a8));
    v_stack_mB0 = a9;
    *(unsigned __int64 *)(v_rsp - 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    v_rsi = 0;
    v_stack_mC0 = 0;
    v_stack_mE8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (a9 == 0) goto loc_00808D8F;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) goto loc_00808D8F;
    a1 = v_rbx;
    if (a9 < v_rbx) { a1 = a9; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    goto loc_00808D99;
loc_00808D8F:
loc_00808D99:
    result = (unsigned int)(((unsigned int)(a6)) - (1));
    if (condition_is_equal) goto loc_00808E02;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00808DE7;
    result = (unsigned int)((result) - (14));
    if (condition_is_equal) goto loc_00808DB4;
    if (((unsigned int)(result)) != 1) goto loc_00808DF4;
loc_00808DB4:
    if (((unsigned int)(result)) >= 1) goto loc_00808DF4;
    if (a5 == 0) goto loc_00808DD7;
loc_00808DD0:
    goto loc_00808DF9;
loc_00808DD7:
    if (((unsigned int)((unsigned int)(a8))) <= 36) goto loc_00808DE3;
loc_00808DDC:
    goto loc_00808DF9;
loc_00808DE3:
    v_rdi = 0;
    goto loc_00808E19;
loc_00808DE7:
    if ((((unsigned __int8)(result)) & (4)) != 0) goto loc_00808E02;
loc_00808DF4:
loc_00808DF9:
    v_stack_mE0 = (unsigned int)((unsigned int)(0xC00000BBULL));
    goto loc_00809037;
loc_00808E02:
    if ((*(unsigned __int64 *)(v_rip + 6481838)) == 0) goto loc_00808DF4;
loc_00808E19:
    result = MiValidateZeroBits(v_stack_mA0, (unsigned int)(a8), a3, a4);
    if (!sign_flag) goto loc_00808E31;
    goto loc_00808DF9;
loc_00808E31:
    if (v_stack_mA8 != 0) goto loc_00808E45;
    goto loc_00808DF9;
loc_00808E45:
    if (a5 > v_stack_mA8) goto loc_00808DD0;
    result = v_stack_mA8;
    if (((unsigned __int8)(v_stack_mE8)) == 1) {
        a1 = (unsigned int)(0xC00000F2ULL);
        if (a2 < ((unsigned int)(0xC00000F2ULL))) { a1 = a2; }
        result = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(a1) = result;
    }
    v_stack_mB8 = *(unsigned __int64 *)(a2);
    if ((unsigned int)((unsigned int)(v_stack_mD4)) == 0) goto loc_00808F2F;
    if ((unsigned int)((unsigned int)(0x1000ULL)) == 0) goto loc_00808E87;
    if (((unsigned int)((unsigned int)(v_stack_mD4))) != ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_00808DDC;
loc_00808E87:
    a2 = ((unsigned int)(v_stack_mD4) + 4095) & (0xFFFFFFFFFFFFF000ULL);
    result = MiAllocatePool(256, a2, (unsigned int)(0x44456D4DULL), a4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_00808EBF;
    goto loc_00808DF9;
loc_00808EBF:
    if (v_stack_mE8 != 1) goto loc_00808EFB;
    if (((unsigned int)(v_stack_mD4)) >= 0x10000ULL) goto loc_00808EDF;
    if ((((unsigned __int8)(a7)) & (3)) != 0) goto loc_00808EE5;
    v_rbx = (unsigned int)(0xC000009AULL);
    if (a7 < ((unsigned int)(0xC000009AULL))) { v_rbx = a7; }
    goto loc_00808EF9;
loc_00808EDF:
    if ((((unsigned __int8)(a7)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(256, a2, (unsigned int)(0x44456D4DULL), a4);
    }
    if ((a7 + (unsigned int)(v_stack_mD4) * 1) > v_rbx) goto loc_00808EF9;
    result = a7 + (unsigned int)(v_stack_mD4) * 1;
    if ((a7 + (unsigned int)(v_stack_mD4) * 1) < a7) {
        result = *(unsigned __int8 *)(v_rbx);
    }
    result = memcpy(result, a7, (unsigned int)(v_stack_mD4), a4);
    goto loc_00808F2F;
loc_00808F2F:
    if (v_stack_mE0 != -1) goto loc_00808F51;
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    goto loc_00808FAB;
loc_00808F51:
    v_stack_m110 = v_stack_mC8;
    v_stack_m118 = 0x6D566D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mE0, 8, *(unsigned __int64 *)(v_rip + 8117056), (unsigned __int8)(v_stack_mE8));
    v_stack_mE0 = (unsigned int)(result);
    if (sign_flag) goto loc_00809037;
    a2 = 0;
    result = KiStackAttachProcess(v_stack_mC8, a2, v_stack_m70, (unsigned __int8)(v_stack_mE8));
loc_00808FAB:
    v_stack_mF8 = v_stack_mD0;
    v_stack_m100 = (unsigned int)((unsigned int)(v_stack_mD4));
    v_stack_m108 = result;
    v_stack_m110 = (unsigned int)((unsigned int)(a6));
    v_stack_m118 = a5;
    result = MiCreateEnclave(v_stack_mC8, v_stack_mB8, v_stack_mA0, v_stack_mA8);
    v_stack_mE0 = (unsigned int)(result);
    if (v_stack_mE0 == -1) goto loc_00809037;
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m70, a2, v_stack_mA0, v_stack_mA8);
    result = ObfDereferenceObjectWithTag(v_stack_mC8, (unsigned int)(0x6D566D4DULL), v_stack_mA0, v_stack_mA8);
    goto loc_00809037;
loc_00809037:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_mA0, v_stack_mA8);
    }
    if (sign_flag) goto loc_00809064;
    *(unsigned __int64 *)(a2) = v_stack_mB8;
    goto loc_00809064;
loc_00809064:
    if (a9 == 0) goto loc_00809076;
    *(unsigned int *)(a9) = (unsigned int)((unsigned int)(v_stack_mD0));
    goto loc_00809076;
loc_00809076:
loc_00809078:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_mA0, v_stack_mA8);
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateEnclave(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, uint32_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m40;
    uint64_t v_stack_m70;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x601A64)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mA8 = Arg4;
    v_stack_mE0 = Arg1;
    v_stack_m98 = Arg2;
    *(uint64_t *)(local_rsp - 0xA0) = Arg3;
    v_stack_mD4 = (uint32_t)((uint32_t)(Arg8));
    v_stack_mB0 = Arg9;
    *(uint64_t *)(local_rsp - 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    local_rsi = 0;
    v_stack_mC0 = 0;
    v_stack_mE8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (Arg9 == 0) goto loc_00808D8F;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) goto loc_00808D8F;
    Arg1 = local_rbx;
    if (Arg9 < local_rbx) { Arg1 = Arg9; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    goto loc_00808D99;
loc_00808D8F:
loc_00808D99:
    result = (uint32_t)(((uint32_t)(Arg6)) - (1));
    if (condition_is_equal) goto loc_00808E02;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00808DE7;
    result = (uint32_t)((result) - (14));
    if (condition_is_equal) goto loc_00808DB4;
    if (((uint32_t)(result)) != 1) goto loc_00808DF4;
loc_00808DB4:
    if (((uint32_t)(result)) >= 1) goto loc_00808DF4;
    if (Arg5 == 0) goto loc_00808DD7;
loc_00808DD0:
    goto loc_00808DF9;
loc_00808DD7:
    if (((uint32_t)((uint32_t)(Arg8))) <= 36) goto loc_00808DE3;
loc_00808DDC:
    goto loc_00808DF9;
loc_00808DE3:
    local_rdi = 0;
    goto loc_00808E19;
loc_00808DE7:
    if ((((uint8_t)(result)) & (4)) != 0) goto loc_00808E02;
loc_00808DF4:
loc_00808DF9:
    v_stack_mE0 = (uint32_t)((uint32_t)(0xC00000BBULL));
    goto loc_00809037;
loc_00808E02:
    if ((*(uint64_t *)(v_rip + 0x62E7AE)) == 0) goto loc_00808DF4;
loc_00808E19:
    result = MiValidateZeroBits(v_stack_mA0, (uint32_t)(Arg8), Arg3, Arg4);
    if (!sign_flag) goto loc_00808E31;
    goto loc_00808DF9;
loc_00808E31:
    if (v_stack_mA8 != 0) goto loc_00808E45;
    goto loc_00808DF9;
loc_00808E45:
    if (Arg5 > v_stack_mA8) goto loc_00808DD0;
    result = v_stack_mA8;
    if (((uint8_t)(v_stack_mE8)) == 1) {
        Arg1 = (uint32_t)(0xC00000F2ULL);
        if (Arg2 < ((uint32_t)(0xC00000F2ULL))) { Arg1 = Arg2; }
        result = *(uint64_t *)(Arg1);
        *(uint64_t *)(Arg1) = result;
    }
    v_stack_mB8 = *(uint64_t *)(Arg2);
    if ((uint32_t)((uint32_t)(v_stack_mD4)) == 0) goto loc_00808F2F;
    if ((uint32_t)((uint32_t)(0x1000ULL)) == 0) goto loc_00808E87;
    if (((uint32_t)((uint32_t)(v_stack_mD4))) != ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_00808DDC;
loc_00808E87:
    Arg2 = ((uint32_t)(v_stack_mD4) + 4095) & (0xFFFFFFFFFFFFF000ULL);
    result = MiAllocatePool(256, Arg2, (uint32_t)(0x44456D4DULL), Arg4);
    v_stack_mC0 = result;
    if (result != 0) goto loc_00808EBF;
    goto loc_00808DF9;
loc_00808EBF:
    if (v_stack_mE8 != 1) goto loc_00808EFB;
    if (((uint32_t)(v_stack_mD4)) >= 0x10000ULL) goto loc_00808EDF;
    if ((((uint8_t)(Arg7)) & (3)) != 0) goto loc_00808EE5;
    local_rbx = (uint32_t)(0xC000009AULL);
    if (Arg7 < ((uint32_t)(0xC000009AULL))) { local_rbx = Arg7; }
    goto loc_00808EF9;
loc_00808EDF:
    if ((((uint8_t)(Arg7)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(256, Arg2, (uint32_t)(0x44456D4DULL), Arg4);
    }
    if ((Arg7 + (uint32_t)(v_stack_mD4) * 1) > local_rbx) goto loc_00808EF9;
    result = Arg7 + (uint32_t)(v_stack_mD4) * 1;
    if ((Arg7 + (uint32_t)(v_stack_mD4) * 1) < Arg7) {
        result = *(uint8_t *)(local_rbx);
    }
    result = memcpy(result, Arg7, (uint32_t)(v_stack_mD4), Arg4);
    goto loc_00808F2F;
loc_00808F2F:
    if (v_stack_mE0 != -1) goto loc_00808F51;
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    goto loc_00808FAB;
loc_00808F51:
    v_stack_m110 = v_stack_mC8;
    v_stack_m118 = 0x6D566D4DULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mE0, 8, *(uint64_t *)(v_rip + 0x7BDB40), (uint8_t)(v_stack_mE8));
    v_stack_mE0 = (uint32_t)(result);
    if (sign_flag) goto loc_00809037;
    Arg2 = 0;
    result = KiStackAttachProcess(v_stack_mC8, Arg2, v_stack_m70, (uint8_t)(v_stack_mE8));
loc_00808FAB:
    v_stack_mF8 = v_stack_mD0;
    v_stack_m100 = (uint32_t)((uint32_t)(v_stack_mD4));
    v_stack_m108 = result;
    v_stack_m110 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m118 = Arg5;
    result = MiCreateEnclave(v_stack_mC8, v_stack_mB8, v_stack_mA0, v_stack_mA8);
    v_stack_mE0 = (uint32_t)(result);
    if (v_stack_mE0 == -1) goto loc_00809037;
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m70, Arg2, v_stack_mA0, v_stack_mA8);
    result = ObfDereferenceObjectWithTag(v_stack_mC8, (uint32_t)(0x6D566D4DULL), v_stack_mA0, v_stack_mA8);
    goto loc_00809037;
loc_00809037:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_mA0, v_stack_mA8);
    }
    if (sign_flag) goto loc_00809064;
    *(uint64_t *)(Arg2) = v_stack_mB8;
    goto loc_00809064;
loc_00809064:
    if (Arg9 == 0) goto loc_00809076;
    *(uint32_t *)(Arg9) = (uint32_t)((uint32_t)(v_stack_mD0));
    goto loc_00809076;
loc_00809076:
loc_00809078:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_mA0, v_stack_mA8);
    local_rsp = (local_rsp) + (256);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00808CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
