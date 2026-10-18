# CmGetDeviceRegKeyPath

- RVA: `0x00990CC0`–`0x0099107D` (길이 `957` bytes)
- VA: `0x0000000140990CC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098C78`
- 디코드: `237`개 명령, `957/957` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00990DFE` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00990E4B` → [_CmGetDeviceSoftwareKeyPath](_CmGetDeviceSoftwareKeyPath_function_00991090.md) (function, `0x00991090`)
- `0x00990E9B` → [CmGetDeviceLogConfKeyPath](CmGetDeviceLogConfKeyPath_function_009913B8.md) (function, `0x009913B8`)
- `0x00990ED4` → [CmGetDeviceControlKeyPath](CmGetDeviceControlKeyPath_function_00991470.md) (function, `0x00991470`)
- `0x00990F0D` → [_CmGetDeviceHardwareKeyPath](_CmGetDeviceHardwareKeyPath_function_00991528.md) (function, `0x00991528`)
- `0x00990FC8` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x0099106C` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)

### Direct callers
- [PiDqGetRelativeObjectRegPath](PiDqGetRelativeObjectRegPath_function_00990B6C.md) at `0x00990BD1`
- [sub_00B47098](../B4/Unknown_function_00B47098.md) at `0x00B470BF`

### Static image references
- `0x00990DCE` → RVA `0x00B0D550` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00990DE4` → RVA `0x00AFD430` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00990FA2` → RVA `0x00B0D590` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00990FB1` → RVA `0x00AFDE50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00991041` → RVA `0x00B0D620` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00991058` → RVA `0x00B0D700` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00990DFE` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x00990FC8` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x0099106C` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00990CC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00990CC5  57                              push rdi
00990CC6  48 83 EC 50                     sub rsp, 0x50
00990CCA  4C 8B DA                        mov r11, rdx
00990CCD  48 8B F9                        mov rdi, rcx
00990CD0  45 85 C0                        test r8d, r8d
00990CD3  0F 84 56 02 00 00               je 0x140990f2f
00990CD9  41 F7 C0 E8 FC FF FF            test r8d, 0xfffffce8
00990CE0  0F 85 49 02 00 00               jne 0x140990f2f
00990CE6  45 33 D2                        xor r10d, r10d
00990CE9  41 8D 5A 01                     lea ebx, [r10 + 1]
00990CED  48 85 D2                        test rdx, rdx
00990CF0  0F 84 39 02 00 00               je 0x140990f2f
00990CF6  B9 C8 00 00 00                  mov ecx, 0xc8
00990CFB  48 8B C2                        mov rax, rdx
00990CFE  66 90                           nop
00990D00  66 44 39 10                     cmp word ptr [rax], r10w
00990D04  74 0B                           je 0x140990d11
00990D06  48 83 C0 02                     add rax, 2
00990D0A  48 2B CB                        sub rcx, rbx
00990D0D  75 F1                           jne 0x140990d00
00990D0F  EB 40                           jmp 0x140990d51
00990D11  0F B7 02                        movzx eax, word ptr [rdx]
00990D14  66 85 C0                        test ax, ax
00990D17  74 2E                           je 0x140990d47
00990D19  8D 48 DF                        lea ecx, [rax - 0x21]
00990D1C  66 83 F9 5E                     cmp cx, 0x5e
00990D20  77 2F                           ja 0x140990d51
00990D22  66 83 F8 2C                     cmp ax, 0x2c
00990D26  74 29                           je 0x140990d51
00990D28  66 83 F8 5C                     cmp ax, 0x5c
00990D2C  74 09                           je 0x140990d37
00990D2E  41 FF C2                        inc r10d
00990D31  48 83 C2 02                     add rdx, 2
00990D35  EB DA                           jmp 0x140990d11
00990D37  45 85 D2                        test r10d, r10d
00990D3A  74 15                           je 0x140990d51
00990D3C  45 33 D2                        xor r10d, r10d
00990D3F  FF C3                           inc ebx
00990D41  48 83 C2 02                     add rdx, 2
00990D45  EB CA                           jmp 0x140990d11
00990D47  45 85 D2                        test r10d, r10d
00990D4A  74 05                           je 0x140990d51
00990D4C  83 FB 03                        cmp ebx, 3
00990D4F  74 11                           je 0x140990d62
00990D51  B8 33 00 00 C0                  mov eax, 0xc0000033
00990D56  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990D5B  48 83 C4 50                     add rsp, 0x50
00990D5F  5F                              pop rdi
00990D60  C3                              ret
00990D61  CC                              int3
00990D62  41 0F B6 C0                     movzx eax, r8b
00990D66  83 F8 10                        cmp eax, 0x10
00990D69  0F 85 A0 00 00 00               jne 0x140990e0f
00990D6F  41 0F BA E0 09                  bt r8d, 9
00990D74  0F 82 BF 01 00 00               jb 0x140990f39
00990D7A  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00990D81  48 FF C0                        inc rax
00990D84  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
00990D8A  75 F5                           jne 0x140990d81
00990D8C  48 83 C0 1F                     add rax, 0x1f
00990D90  B9 FF FF FF FF                  mov ecx, 0xffffffff
00990D95  48 3B C1                        cmp rax, rcx
00990D98  76 11                           jbe 0x140990dab
00990D9A  B8 95 00 00 C0                  mov eax, 0xc0000095
00990D9F  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990DA4  48 83 C4 50                     add rsp, 0x50
00990DA8  5F                              pop rdi
00990DA9  C3                              ret
00990DAA  CC                              int3
00990DAB  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00990DB3  48 85 C9                        test rcx, rcx
00990DB6  74 02                           je 0x140990dba
00990DB8  89 01                           mov dword ptr [rcx], eax
00990DBA  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
00990DC1  3B C1                           cmp eax, ecx
00990DC3  0F 87 55 01 00 00               ja 0x140990f1e
00990DC9  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
00990DCE  48 8D 05 7B C7 17 00            lea rax, [rip + 0x17c77b]
00990DD5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00990DDA  8B D1                           mov edx, ecx
00990DDC  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00990DE4  48 8D 05 45 C6 16 00            lea rax, [rip + 0x16c645]
00990DEB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00990DF0  45 33 C9                        xor r9d, r9d
00990DF3  45 33 C0                        xor r8d, r8d
00990DF6  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
00990DFE  E8 8D A5 A9 FF                  call 0x14042b390
00990E03  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990E08  48 83 C4 50                     add rsp, 0x50
00990E0C  5F                              pop rdi
00990E0D  C3                              ret
00990E0E  CC                              int3
00990E0F  83 F8 12                        cmp eax, 0x12
00990E12  75 48                           jne 0x140990e5c
00990E14  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00990E1C  49 8B D3                        mov rdx, r11
00990E1F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00990E24  48 8B CF                        mov rcx, rdi
00990E27  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00990E2E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00990E32  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00990E3A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00990E3F  0F B6 84 24 80 00 00 00         movzx eax, byte ptr [rsp + 0x80]
00990E47  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00990E4B  E8 40 02 00 00                  call 0x140991090
00990E50  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990E55  48 83 C4 50                     add rsp, 0x50
00990E59  5F                              pop rdi
00990E5A  C3                              ret
00990E5B  CC                              int3
00990E5C  83 F8 11                        cmp eax, 0x11
00990E5F  0F 84 80 00 00 00               je 0x140990ee5
00990E65  83 F8 13                        cmp eax, 0x13
00990E68  74 42                           je 0x140990eac
00990E6A  83 F8 14                        cmp eax, 0x14
00990E6D  0F 85 BC 00 00 00               jne 0x140990f2f
00990E73  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00990E7B  49 8B D3                        mov rdx, r11
00990E7E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00990E83  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00990E8A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00990E8E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00990E96  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00990E9B  E8 18 05 00 00                  call 0x1409913b8
00990EA0  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990EA5  48 83 C4 50                     add rsp, 0x50
00990EA9  5F                              pop rdi
00990EAA  C3                              ret
00990EAB  CC                              int3
00990EAC  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00990EB4  49 8B D3                        mov rdx, r11
00990EB7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00990EBC  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00990EC3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00990EC7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00990ECF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00990ED4  E8 97 05 00 00                  call 0x140991470
00990ED9  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990EDE  48 83 C4 50                     add rsp, 0x50
00990EE2  5F                              pop rdi
00990EE3  C3                              ret
00990EE4  CC                              int3
00990EE5  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00990EED  49 8B D3                        mov rdx, r11
00990EF0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00990EF5  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00990EFC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00990F00  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00990F08  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00990F0D  E8 16 06 00 00                  call 0x140991528
00990F12  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990F17  48 83 C4 50                     add rsp, 0x50
00990F1B  5F                              pop rdi
00990F1C  C3                              ret
00990F1D  CC                              int3
00990F1E  B8 23 00 00 C0                  mov eax, 0xc0000023
00990F23  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990F28  48 83 C4 50                     add rsp, 0x50
00990F2C  5F                              pop rdi
00990F2D  C3                              ret
00990F2E  CC                              int3
00990F2F  B8 0D 00 00 C0                  mov eax, 0xc000000d
00990F34  E9 1D FE FF FF                  jmp 0x140990d56
00990F39  45 85 C9                        test r9d, r9d
00990F3C  0F 85 97 00 00 00               jne 0x140990fd9
00990F42  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00990F49  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00990F50  48 FF C0                        inc rax
00990F53  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
00990F59  75 F5                           jne 0x140990f50
00990F5B  48 83 C0 52                     add rax, 0x52
00990F5F  B9 FF FF FF FF                  mov ecx, 0xffffffff
00990F64  48 3B C1                        cmp rax, rcx
00990F67  0F 87 2D FE FF FF               ja 0x140990d9a
00990F6D  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00990F75  48 85 C9                        test rcx, rcx
00990F78  74 02                           je 0x140990f7c
00990F7A  89 01                           mov dword ptr [rcx], eax
00990F7C  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
00990F83  3B C1                           cmp eax, ecx
00990F85  77 97                           ja 0x140990f1e
00990F87  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
00990F8C  48 8D 05 BD C5 17 00            lea rax, [rip + 0x17c5bd]
00990F93  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00990F98  8B D1                           mov edx, ecx
00990F9A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00990FA2  48 8D 05 E7 C5 17 00            lea rax, [rip + 0x17c5e7]
00990FA9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00990FAE  45 33 C9                        xor r9d, r9d
00990FB1  48 8D 05 98 CE 16 00            lea rax, [rip + 0x16ce98]
00990FB8  45 33 C0                        xor r8d, r8d
00990FBB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00990FC0  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
00990FC8  E8 C3 A3 A9 FF                  call 0x14042b390
00990FCD  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00990FD2  48 83 C4 50                     add rsp, 0x50
00990FD6  5F                              pop rdi
00990FD7  C3                              ret
00990FD8  CC                              int3
00990FD9  B9 FF FF FF FF                  mov ecx, 0xffffffff
00990FDE  44 3B C9                        cmp r9d, ecx
00990FE1  0F 84 48 FF FF FF               je 0x140990f2f
00990FE7  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00990FEE  66 90                           nop
00990FF0  48 FF C0                        inc rax
00990FF3  66 41 83 3C 43 00               cmp word ptr [r11 + rax*2], 0
00990FF9  75 F5                           jne 0x140990ff0
00990FFB  48 83 C0 4F                     add rax, 0x4f
00990FFF  48 3B C1                        cmp rax, rcx
00991002  0F 87 92 FD FF FF               ja 0x140990d9a
00991008  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00991010  48 85 C9                        test rcx, rcx
00991013  74 02                           je 0x140991017
00991015  89 01                           mov dword ptr [rcx], eax
00991017  8B 8C 24 90 00 00 00            mov ecx, dword ptr [rsp + 0x90]
0099101E  3B C1                           cmp eax, ecx
00991020  0F 87 F8 FE FF FF               ja 0x140990f1e
00991026  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
0099102B  48 8D 05 1E C5 17 00            lea rax, [rip + 0x17c51e]
00991032  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00991037  8B D1                           mov edx, ecx
00991039  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00991041  48 8D 05 D8 C5 17 00            lea rax, [rip + 0x17c5d8]
00991048  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
0099104D  45 33 C0                        xor r8d, r8d
00991050  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00991055  45 33 C9                        xor r9d, r9d
00991058  48 8D 05 A1 C6 17 00            lea rax, [rip + 0x17c6a1]
0099105F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00991064  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
0099106C  E8 1F A3 A9 FF                  call 0x14042b390
00991071  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00991076  48 83 C4 50                     add rsp, 0x50
0099107A  5F                              pop rdi
0099107B  C3                              ret
0099107C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmGetDeviceRegKeyPath(__int64 a1, __int64 a2, int a3, int a4, unsigned __int8 a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p130;
    unsigned int v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p188;
    unsigned int v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned __int64 v_stack_p1C0;
    unsigned __int64 v_stack_p1E0;
    unsigned int v_stack_p1E8;
    unsigned __int64 v_stack_p1F0;
    unsigned __int64 v_stack_p218;
    unsigned __int64 v_stack_p270;
    unsigned int v_stack_p288;
    unsigned __int64 v_stack_p290;
    unsigned __int64 v_stack_p298;
    unsigned __int64 v_stack_p2A0;
    unsigned __int64 v_stack_p2A8;
    unsigned __int64 v_stack_p2C8;
    unsigned int v_stack_p2E0;
    unsigned __int64 v_stack_p2E8;
    unsigned __int64 v_stack_p2F0;
    unsigned int v_stack_p2F8;
    unsigned __int64 v_stack_p300;
    unsigned __int64 v_stack_p308;
    unsigned __int64 v_stack_p320;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pB8;
    unsigned __int8 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned int v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    if (a3 == 0) goto loc_00990F2F;
    if (((a3) & (0xFFFFFCE8ULL)) != 0) goto loc_00990F2F;
    v_r10 = 0;
    if (a2 == 0) goto loc_00990F2F;
loc_00990D00:
    if ((*(unsigned __int16 *)(a2)) == 0) goto loc_00990D11;
    result = (a2) + (2);
    a1 = (200) - (v_r10 + 1);
    if (condition_is_not_equal) goto loc_00990D00;
    goto loc_00990D51;
loc_00990D11:
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_00990D47;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2) - 33)) > 94) goto loc_00990D51;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) == 44) goto loc_00990D51;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) == 92) goto loc_00990D37;
    v_r10 = (unsigned int)((v_r10) + 1);
    a2 = (a2) + (2);
    goto loc_00990D11;
loc_00990D37:
    if ((unsigned int)(v_r10) == 0) goto loc_00990D51;
    v_r10 = 0;
    v_rbx = (unsigned int)((v_r10 + 1) + 1);
    a2 = (a2) + (2);
    goto loc_00990D11;
loc_00990D47:
    if (0 == 0) goto loc_00990D51;
    if (((unsigned int)(v_rbx)) == 3) goto loc_00990D62;
loc_00990D51:
loc_00990D56:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(0xC0000033ULL);
loc_00990D62:
    if (((unsigned int)((unsigned __int8)(a3))) != 16) goto loc_00990E0F;
    if (((unsigned int)((unsigned __int8)(a3))) < 16) goto loc_00990F39;
loc_00990D81:
    result = (-1) + 1;
    if ((*(unsigned __int16 *)(a2 + result * 2)) != 0) goto loc_00990D81;
    result = (result) + (31);
    if (result <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_00990DAB;
loc_00990D9A:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(0xC0000095ULL);
loc_00990DAB:
    if (a8 != 0) {
        *(unsigned int *)(a8) = (unsigned int)((unsigned int)(0xC0000095ULL));
    }
    if (((unsigned int)((unsigned int)(0xC0000095ULL))) > ((unsigned int)((unsigned int)(a7)))) goto loc_00990F1E;
    v_stack_p90 = a2;
    v_stack_p88 = v_rip + 1558395;
    v_stack_p80 = v_rip + 1492549;
    a4 = 0;
    a3 = 0;
    v_stack_p78 = 0x800ULL;
    result = RtlStringCchPrintfExW(a6, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
loc_00990E0F:
    if (((unsigned int)(result)) != 18) goto loc_00990E5C;
    v_stack_pE8 = a8;
    v_stack_pE0 = (unsigned int)((unsigned int)(a7));
    v_stack_pD8 = a6;
    v_stack_pD0 = a5;
    result = _CmGetDeviceSoftwareKeyPath(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
loc_00990E5C:
    if (((unsigned int)(result)) == 17) goto loc_00990EE5;
    if (((unsigned int)(result)) == 19) goto loc_00990EAC;
    if (((unsigned int)(result)) != 20) goto loc_00990F2F;
    v_stack_p140 = a8;
    v_stack_p138 = (unsigned int)((unsigned int)(a7));
    v_stack_p130 = a6;
    result = CmGetDeviceLogConfKeyPath(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
loc_00990EAC:
    v_stack_p198 = a8;
    v_stack_p190 = (unsigned int)((unsigned int)(a7));
    v_stack_p188 = a6;
    result = CmGetDeviceControlKeyPath(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
loc_00990EE5:
    v_stack_p1F0 = a8;
    v_stack_p1E8 = (unsigned int)((unsigned int)(a7));
    v_stack_p1E0 = a6;
    result = _CmGetDeviceHardwareKeyPath(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
loc_00990F1E:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(0xC0000023ULL);
loc_00990F2F:
    goto loc_00990D56;
loc_00990F39:
    if (0 != 0) goto loc_00990FD9;
loc_00990F50:
    result = (-1) + 1;
    if ((*(unsigned __int16 *)(a2 + result * 2)) != 0) goto loc_00990F50;
    result = (result) + (82);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00990D9A;
    if (a8 != 0) {
        *(unsigned int *)(a8) = (unsigned int)(result);
    }
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(a7)))) goto loc_00990F1E;
    v_stack_p2A8 = a2;
    v_stack_p2A0 = v_rip + 1557949;
    v_stack_p298 = v_rip + 1557991;
    a4 = 0;
    a3 = 0;
    v_stack_p290 = v_rip + 1494680;
    v_stack_p288 = 0x800ULL;
    result = RtlStringCchPrintfExW(a6, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
loc_00990FD9:
    if (0 == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00990F2F;
loc_00990FF0:
    result = (-1) + 1;
    if ((*(unsigned __int16 *)(a2 + result * 2)) != 0) goto loc_00990FF0;
    result = (result) + (79);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00990D9A;
    if (a8 != 0) {
        *(unsigned int *)(a8) = (unsigned int)(result);
    }
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(a7)))) goto loc_00990F1E;
    v_stack_p308 = a2;
    v_stack_p300 = v_rip + 1557790;
    v_stack_p2F8 = 0;
    a3 = 0;
    v_stack_p2F0 = v_rip + 1557976;
    a4 = 0;
    v_stack_p2E8 = v_rip + 1558177;
    v_stack_p2E0 = 0x800ULL;
    result = RtlStringCchPrintfExW(a6, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmGetDeviceRegKeyPath(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p110;
    uint64_t v_stack_p130;
    uint32_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p168;
    uint64_t v_stack_p188;
    uint32_t v_stack_p190;
    uint64_t v_stack_p198;
    uint64_t v_stack_p1C0;
    uint64_t v_stack_p1E0;
    uint32_t v_stack_p1E8;
    uint64_t v_stack_p1F0;
    uint64_t v_stack_p218;
    uint64_t v_stack_p270;
    uint32_t v_stack_p288;
    uint64_t v_stack_p290;
    uint64_t v_stack_p298;
    uint64_t v_stack_p2A0;
    uint64_t v_stack_p2A8;
    uint64_t v_stack_p2C8;
    uint32_t v_stack_p2E0;
    uint64_t v_stack_p2E8;
    uint64_t v_stack_p2F0;
    uint32_t v_stack_p2F8;
    uint64_t v_stack_p300;
    uint64_t v_stack_p308;
    uint64_t v_stack_p320;
    uint64_t v_stack_p60;
    uint32_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_pB8;
    uint8_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint32_t v_stack_pE0;
    uint64_t v_stack_pE8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    if (Arg3 == 0) goto loc_00990F2F;
    if (((Arg3) & (0xFFFFFCE8ULL)) != 0) goto loc_00990F2F;
    local_r10 = 0;
    if (Arg2 == NULL) goto loc_00990F2F;
loc_00990D00:
    if ((*(uint16_t *)(arg2)) == 0) goto loc_00990D11;
    result = (Arg2) + (2);
    Arg1 = (200) - (local_r10 + 1);
    if (condition_is_not_equal) goto loc_00990D00;
    goto loc_00990D51;
loc_00990D11:
    if ((uint16_t)(*(uint16_t *)(arg2)) == 0) goto loc_00990D47;
    if (((uint16_t)(*(uint16_t *)(arg2) - 33)) > 94) goto loc_00990D51;
    if (((uint16_t)(*(uint16_t *)(arg2))) == 44) goto loc_00990D51;
    if (((uint16_t)(*(uint16_t *)(arg2))) == 92) goto loc_00990D37;
    local_r10 = (uint32_t)((local_r10) + 1);
    Arg2 = (Arg2) + (2);
    goto loc_00990D11;
loc_00990D37:
    if ((uint32_t)(local_r10) == 0) goto loc_00990D51;
    local_r10 = 0;
    local_rbx = (uint32_t)((local_r10 + 1) + 1);
    Arg2 = (Arg2) + (2);
    goto loc_00990D11;
loc_00990D47:
    if (0 == 0) goto loc_00990D51;
    if (((uint32_t)(local_rbx)) == 3) goto loc_00990D62;
loc_00990D51:
loc_00990D56:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(0xC0000033ULL);
loc_00990D62:
    if (((uint32_t)((uint8_t)(Arg3))) != 16) goto loc_00990E0F;
    if (((uint32_t)((uint8_t)(Arg3))) < 16) goto loc_00990F39;
loc_00990D81:
    result = (-1) + 1;
    if ((*(uint16_t *)(arg2 + result * 2)) != 0) goto loc_00990D81;
    result = (result) + (31);
    if (result <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_00990DAB;
loc_00990D9A:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(0xC0000095ULL);
loc_00990DAB:
    if (Arg8 != 0) {
        *(uint32_t *)(Arg8) = (uint32_t)((uint32_t)(0xC0000095ULL));
    }
    if (((uint32_t)((uint32_t)(0xC0000095ULL))) > ((uint32_t)((uint32_t)(Arg7)))) goto loc_00990F1E;
    v_stack_p90 = Arg2;
    v_stack_p88 = v_rip + 1558395;
    v_stack_p80 = v_rip + 1492549;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p78 = 0x800ULL;
    result = RtlStringCchPrintfExW(Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
loc_00990E0F:
    if (((uint32_t)(result)) != 18) goto loc_00990E5C;
    v_stack_pE8 = Arg8;
    v_stack_pE0 = (uint32_t)((uint32_t)(Arg7));
    v_stack_pD8 = Arg6;
    v_stack_pD0 = Arg5;
    result = _CmGetDeviceSoftwareKeyPath(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
loc_00990E5C:
    if (((uint32_t)(result)) == 17) goto loc_00990EE5;
    if (((uint32_t)(result)) == 19) goto loc_00990EAC;
    if (((uint32_t)(result)) != 20) goto loc_00990F2F;
    v_stack_p140 = Arg8;
    v_stack_p138 = (uint32_t)((uint32_t)(Arg7));
    v_stack_p130 = Arg6;
    result = CmGetDeviceLogConfKeyPath(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
loc_00990EAC:
    v_stack_p198 = Arg8;
    v_stack_p190 = (uint32_t)((uint32_t)(Arg7));
    v_stack_p188 = Arg6;
    result = CmGetDeviceControlKeyPath(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
loc_00990EE5:
    v_stack_p1F0 = Arg8;
    v_stack_p1E8 = (uint32_t)((uint32_t)(Arg7));
    v_stack_p1E0 = Arg6;
    result = _CmGetDeviceHardwareKeyPath(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
loc_00990F1E:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(0xC0000023ULL);
loc_00990F2F:
    goto loc_00990D56;
loc_00990F39:
    if (0 != 0) goto loc_00990FD9;
loc_00990F50:
    result = (-1) + 1;
    if ((*(uint16_t *)(arg2 + result * 2)) != 0) goto loc_00990F50;
    result = (result) + (82);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00990D9A;
    if (Arg8 != 0) {
        *(uint32_t *)(Arg8) = (uint32_t)(result);
    }
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(Arg7)))) goto loc_00990F1E;
    v_stack_p2A8 = Arg2;
    v_stack_p2A0 = v_rip + 1557949;
    v_stack_p298 = v_rip + 1557991;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p290 = v_rip + 1494680;
    v_stack_p288 = 0x800ULL;
    result = RtlStringCchPrintfExW(Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
loc_00990FD9:
    if (0 == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00990F2F;
loc_00990FF0:
    result = (-1) + 1;
    if ((*(uint16_t *)(arg2 + result * 2)) != 0) goto loc_00990FF0;
    result = (result) + (79);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00990D9A;
    if (Arg8 != 0) {
        *(uint32_t *)(Arg8) = (uint32_t)(result);
    }
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(Arg7)))) goto loc_00990F1E;
    v_stack_p308 = Arg2;
    v_stack_p300 = v_rip + 1557790;
    v_stack_p2F8 = 0;
    Arg3 = 0;
    v_stack_p2F0 = v_rip + 1557976;
    Arg4 = 0;
    v_stack_p2E8 = v_rip + 1558177;
    v_stack_p2E0 = 0x800ULL;
    result = RtlStringCchPrintfExW(Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rax*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00990CC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
