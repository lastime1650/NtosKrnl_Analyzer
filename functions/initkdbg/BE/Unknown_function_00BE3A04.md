# sub_00BE3A04

- RVA: `0x00BE3A04`–`0x00BE60AA` (길이 `9,894` bytes)
- VA: `0x0000000140BE3A04`
- 실행 섹션: `INITKDBG`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2B68`
- 디코드: `2,478`개 명령, `9,894/9,894` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **50**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BE3A49` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE3CA9` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE3F18` → [sub_00BE8D30](Unknown_function_00BE8D30.md) (function, `0x00BE8D30`)
- `0x00BE3F3C` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE3F59` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE3F81` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE3FD3` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE3FE9` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4039` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE404C` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4058` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4074` → [sub_00BEFF8C](../../init/BE/Unknown_function_00BEFF8C.md) (function, `0x00BEFF8C`)
- `0x00BE409D` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE40D3` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4116` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE413E` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4262` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE427F` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE42BC` → [sub_00BE7AF8](Unknown_function_00BE7AF8.md) (function, `0x00BE7AF8`)
- `0x00BE4355` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE436F` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4560` → [sub_00BE8D30](Unknown_function_00BE8D30.md) (function, `0x00BE8D30`)
- `0x00BE45A5` → [sub_00BE60B0](Unknown_function_00BE60B0.md) (function, `0x00BE60B0`)
- `0x00BE4765` → [sub_00BE7AF8](Unknown_function_00BE7AF8.md) (function, `0x00BE7AF8`)
- `0x00BE4800` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE481A` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE49C4` → [sub_0051AF4C](../../text/51/Unknown_function_0051AF4C.md) (function, `0x0051AF4C`)
- `0x00BE4A1C` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4AC6` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4C2C` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE4D2D` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4E6A` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE4E86` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE4FC1` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE53BD` → [sub_00BE7AF8](Unknown_function_00BE7AF8.md) (function, `0x00BE7AF8`)
- `0x00BE5486` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE54A0` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE5AB7` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE5E87` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE5EC8` → [sub_00BE3A04](Unknown_function_00BE3A04.md) (function, `0x00BE3A04`)
- `0x00BE5F2A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE5F55` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE5F7F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE5FA7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE5FD2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE5FFB` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE6021` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE604C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE6077` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00BE60A4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [sub_00BE3A04](Unknown_function_00BE3A04.md) at `0x00BE5EC8`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BFCC9B`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C13657`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00BE4074` → [sub_00BEFF8C](../../init/BE/Unknown_function_00BEFF8C.md) (`INITKDBG` → `INIT`)
  - `0x00BE49C4` → [sub_0051AF4C](../../text/51/Unknown_function_0051AF4C.md) (`INITKDBG` → `.text`)
  - `0x00BE5F2A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE5F55` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE5F7F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE5FA7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE5FD2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE5FFB` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE6021` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE604C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE6077` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
  - `0x00BE60A4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INITKDBG` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BE3A04  48 8B C4                        mov rax, rsp
00BE3A07  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00BE3A0B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00BE3A0F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00BE3A13  55                              push rbp
00BE3A14  53                              push rbx
00BE3A15  56                              push rsi
00BE3A16  57                              push rdi
00BE3A17  41 54                           push r12
00BE3A19  41 55                           push r13
00BE3A1B  41 56                           push r14
00BE3A1D  41 57                           push r15
00BE3A1F  48 8D A8 28 FF FF FF            lea rbp, [rax - 0xd8]
00BE3A26  48 81 EC 98 01 00 00            sub rsp, 0x198
00BE3A2D  48 8B 01                        mov rax, qword ptr [rcx]
00BE3A30  48 8B F2                        mov rsi, rdx
00BE3A33  48 8B F9                        mov rdi, rcx
00BE3A36  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BE3A3B  48 8D 55 30                     lea rdx, [rbp + 0x30]
00BE3A3F  48 8B CE                        mov rcx, rsi
00BE3A42  48 8B 80 10 02 00 00            mov rax, qword ptr [rax + 0x210]
00BE3A49  E8 12 70 00 00                  call 0x140beaa60
00BE3A4E  4C 8B E0                        mov r12, rax
00BE3A51  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
00BE3A58  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
00BE3A5C  45 33 C0                        xor r8d, r8d
00BE3A5F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00BE3A63  48 85 C0                        test rax, rax
00BE3A66  75 1F                           jne 0x140be3a87
00BE3A68  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00BE3A6D  F7 80 D8 09 00 00 00 00 10 00   test dword ptr [rax + 0x9d8], 0x100000
00BE3A77  0F 84 88 24 00 00               je 0x140be5f05
00BE3A7D  B8 7B 00 00 C0                  mov eax, 0xc000007b
00BE3A82  E9 69 24 00 00                  jmp 0x140be5ef0
00BE3A87  B9 04 00 00 00                  mov ecx, 4
00BE3A8C  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
00BE3A90  48 8D 45 B8                     lea rax, [rbp - 0x48]
00BE3A94  8D 51 FD                        lea edx, [rcx - 3]
00BE3A97  44 88 00                        mov byte ptr [rax], r8b
00BE3A9A  48 03 C2                        add rax, rdx
00BE3A9D  83 C1 FF                        add ecx, -1
00BE3AA0  75 F5                           jne 0x140be3a97
00BE3AA2  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00BE3AA7  44 8D 69 30                     lea r13d, [rcx + 0x30]
00BE3AAB  45 8B C8                        mov r9d, r8d
00BE3AAE  44 8B B3 2C 08 00 00            mov r14d, dword ptr [rbx + 0x82c]
00BE3AB5  45 85 F6                        test r14d, r14d
00BE3AB8  0F 84 CB 01 00 00               je 0x140be3c89
00BE3ABE  4C 8B BB C0 0A 00 00            mov r15, qword ptr [rbx + 0xac0]
00BE3AC5  44 8B 6D 44                     mov r13d, dword ptr [rbp + 0x44]
00BE3AC9  8B 4D B8                        mov ecx, dword ptr [rbp - 0x48]
00BE3ACC  8B 55 B4                        mov edx, dword ptr [rbp - 0x4c]
00BE3ACF  8B 7D B0                        mov edi, dword ptr [rbp - 0x50]
00BE3AD2  4D 85 FF                        test r15, r15
00BE3AD5  45 8B D8                        mov r11d, r8d
00BE3AD8  4C 8B D3                        mov r10, rbx
00BE3ADB  4D 0F 45 D7                     cmovne r10, r15
00BE3ADF  45 8B 82 28 08 00 00            mov r8d, dword ptr [r10 + 0x828]
00BE3AE6  4D 03 C2                        add r8, r10
00BE3AE9  85 FF                           test edi, edi
00BE3AEB  74 0E                           je 0x140be3afb
00BE3AED  41 3B D1                        cmp edx, r9d
00BE3AF0  77 09                           ja 0x140be3afb
00BE3AF2  44 8B C1                        mov r8d, ecx
00BE3AF5  44 8B DA                        mov r11d, edx
00BE3AF8  4D 03 C2                        add r8, r10
00BE3AFB  45 3B D9                        cmp r11d, r9d
00BE3AFE  0F 84 12 01 00 00               je 0x140be3c16
00BE3B04  41 8B F9                        mov edi, r9d
00BE3B07  BE 01 00 00 00                  mov esi, 1
00BE3B0C  41 2B FB                        sub edi, r11d
00BE3B0F  49 BC AB AA AA AA AA AA AA AA   movabs r12, 0xaaaaaaaaaaaaaaab
00BE3B19  45 8B D9                        mov r11d, r9d
00BE3B1C  41 8B 08                        mov ecx, dword ptr [r8]
00BE3B1F  2B CE                           sub ecx, esi
00BE3B21  0F 84 BC 00 00 00               je 0x140be3be3
00BE3B27  83 E9 06                        sub ecx, 6
00BE3B2A  0F 84 A4 00 00 00               je 0x140be3bd4
00BE3B30  2B CE                           sub ecx, esi
00BE3B32  0F 84 8F 00 00 00               je 0x140be3bc7
00BE3B38  83 E9 02                        sub ecx, 2
00BE3B3B  74 7E                           je 0x140be3bbb
00BE3B3D  83 E9 12                        sub ecx, 0x12
00BE3B40  74 72                           je 0x140be3bb4
00BE3B42  83 E9 02                        sub ecx, 2
00BE3B45  74 40                           je 0x140be3b87
00BE3B47  83 E9 03                        sub ecx, 3
00BE3B4A  74 13                           je 0x140be3b5f
00BE3B4C  83 F9 0A                        cmp ecx, 0xa
00BE3B4F  0F 84 8E 00 00 00               je 0x140be3be3
00BE3B55  B8 30 00 00 00                  mov eax, 0x30
00BE3B5A  E9 99 00 00 00                  jmp 0x140be3bf8
00BE3B5F  41 8B 48 20                     mov ecx, dword ptr [r8 + 0x20]
00BE3B63  41 8B 50 28                     mov edx, dword ptr [r8 + 0x28]
00BE3B67  81 E1 FF 0F 00 00               and ecx, 0xfff
00BE3B6D  48 81 C2 FF 0F 00 00            add rdx, 0xfff
00BE3B74  48 03 D1                        add rdx, rcx
00BE3B77  48 C1 EA 0C                     shr rdx, 0xc
00BE3B7B  8D 04 92                        lea eax, [rdx + rdx*4]
00BE3B7E  8D 04 85 30 00 00 00            lea eax, [rax*4 + 0x30]
00BE3B85  EB 71                           jmp 0x140be3bf8
00BE3B87  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
00BE3B8B  8D 48 FF                        lea ecx, [rax - 1]
00BE3B8E  F7 D8                           neg eax
00BE3B90  1B C0                           sbb eax, eax
00BE3B92  23 C8                           and ecx, eax
00BE3B94  49 8B C4                        mov rax, r12
00BE3B97  48 F7 E1                        mul rcx
00BE3B9A  41 0F B7 40 28                  movzx eax, word ptr [r8 + 0x28]
00BE3B9F  48 C1 EA 03                     shr rdx, 3
00BE3BA3  83 C2 07                        add edx, 7
00BE3BA6  83 E2 F8                        and edx, 0xfffffff8
00BE3BA9  83 C0 02                        add eax, 2
00BE3BAC  8D 04 40                        lea eax, [rax + rax*2]
00BE3BAF  8D 04 C2                        lea eax, [rdx + rax*8]
00BE3BB2  EB 44                           jmp 0x140be3bf8
00BE3BB4  41 0F B7 40 28                  movzx eax, word ptr [r8 + 0x28]
00BE3BB9  EB 11                           jmp 0x140be3bcc
00BE3BBB  41 8B 40 1C                     mov eax, dword ptr [r8 + 0x1c]
00BE3BBF  83 C0 03                        add eax, 3
00BE3BC2  C1 E0 04                        shl eax, 4
00BE3BC5  EB 31                           jmp 0x140be3bf8
00BE3BC7  41 0F B7 40 20                  movzx eax, word ptr [r8 + 0x20]
00BE3BCC  83 C0 37                        add eax, 0x37
00BE3BCF  83 E0 F8                        and eax, 0xfffffff8
00BE3BD2  EB 24                           jmp 0x140be3bf8
00BE3BD4  41 8B 40 18                     mov eax, dword ptr [r8 + 0x18]
00BE3BD8  83 C0 02                        add eax, 2
00BE3BDB  8D 04 40                        lea eax, [rax + rax*2]
00BE3BDE  C1 E0 03                        shl eax, 3
00BE3BE1  EB 15                           jmp 0x140be3bf8
00BE3BE3  41 8B 48 10                     mov ecx, dword ptr [r8 + 0x10]
00BE3BE7  49 8B C4                        mov rax, r12
00BE3BEA  48 F7 E1                        mul rcx
00BE3BED  48 C1 EA 03                     shr rdx, 3
00BE3BF1  8D 04 95 30 00 00 00            lea eax, [rdx*4 + 0x30]
00BE3BF8  4C 03 C0                        add r8, rax
00BE3BFB  48 2B FE                        sub rdi, rsi
00BE3BFE  0F 85 18 FF FF FF               jne 0x140be3b1c
00BE3C04  48 8B B5 E8 00 00 00            mov rsi, qword ptr [rbp + 0xe8]
00BE3C0B  4C 8B A5 F8 00 00 00            mov r12, qword ptr [rbp + 0xf8]
00BE3C12  44 8B 6D 44                     mov r13d, dword ptr [rbp + 0x44]
00BE3C16  B8 01 00 00 00                  mov eax, 1
00BE3C1B  41 8B C8                        mov ecx, r8d
00BE3C1E  8B F8                           mov edi, eax
00BE3C20  89 45 B0                        mov dword ptr [rbp - 0x50], eax
00BE3C23  41 8B 00                        mov eax, dword ptr [r8]
00BE3C26  41 2B CA                        sub ecx, r10d
00BE3C29  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
00BE3C2C  41 8B D3                        mov edx, r11d
00BE3C2F  89 55 B4                        mov dword ptr [rbp - 0x4c], edx
00BE3C32  3B C7                           cmp eax, edi
00BE3C34  74 0A                           je 0x140be3c40
00BE3C36  83 F8 0C                        cmp eax, 0xc
00BE3C39  74 05                           je 0x140be3c40
00BE3C3B  83 F8 2B                        cmp eax, 0x2b
00BE3C3E  75 0C                           jne 0x140be3c4c
00BE3C40  4D 39 60 08                     cmp qword ptr [r8 + 8], r12
00BE3C44  75 06                           jne 0x140be3c4c
00BE3C46  45 39 68 10                     cmp dword ptr [r8 + 0x10], r13d
00BE3C4A  74 21                           je 0x140be3c6d
00BE3C4C  83 C0 DF                        add eax, -0x21
00BE3C4F  3B C7                           cmp eax, edi
00BE3C51  77 0A                           ja 0x140be3c5d
00BE3C53  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00BE3C57  49 39 40 20                     cmp qword ptr [r8 + 0x20], rax
00BE3C5B  74 10                           je 0x140be3c6d
00BE3C5D  44 03 CF                        add r9d, edi
00BE3C60  45 3B CE                        cmp r9d, r14d
00BE3C63  73 17                           jae 0x140be3c7c
00BE3C65  45 33 C0                        xor r8d, r8d
00BE3C68  E9 65 FE FF FF                  jmp 0x140be3ad2
00BE3C6D  4D 85 C0                        test r8, r8
00BE3C70  74 0A                           je 0x140be3c7c
00BE3C72  B8 0E 01 00 C0                  mov eax, 0xc000010e
00BE3C77  E9 74 22 00 00                  jmp 0x140be5ef0
00BE3C7C  48 8B BD E0 00 00 00            mov rdi, qword ptr [rbp + 0xe0]
00BE3C83  41 BD 30 00 00 00               mov r13d, 0x30
00BE3C89  44 8B B5 F0 00 00 00            mov r14d, dword ptr [rbp + 0xf0]
00BE3C90  48 8D 55 78                     lea rdx, [rbp + 0x78]
00BE3C94  48 8B 83 10 02 00 00            mov rax, qword ptr [rbx + 0x210]
00BE3C9B  48 8B CE                        mov rcx, rsi
00BE3C9E  44 89 B5 F8 00 00 00            mov dword ptr [rbp + 0xf8], r14d
00BE3CA5  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00BE3CA9  E8 B2 6D 00 00                  call 0x140beaa60
00BE3CAE  4C 8B BD 80 00 00 00            mov r15, qword ptr [rbp + 0x80]
00BE3CB5  45 33 C0                        xor r8d, r8d
00BE3CB8  44 8B A5 8C 00 00 00            mov r12d, dword ptr [rbp + 0x8c]
00BE3CBF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00BE3CC4  44 89 64 24 78                  mov dword ptr [rsp + 0x78], r12d
00BE3CC9  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00BE3CCE  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00BE3CD3  4D 85 FF                        test r15, r15
00BE3CD6  75 22                           jne 0x140be3cfa
00BE3CD8  F7 83 D8 09 00 00 00 00 10 00   test dword ptr [rbx + 0x9d8], 0x100000
00BE3CE2  0F 84 48 22 00 00               je 0x140be5f30
00BE3CE8  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00BE3CED  B9 7B 00 00 C0                  mov ecx, 0xc000007b
00BE3CF2  48 89 07                        mov qword ptr [rdi], rax
00BE3CF5  E9 FC 16 00 00                  jmp 0x140be53f6
00BE3CFA  4C 89 45 C0                     mov qword ptr [rbp - 0x40], r8
00BE3CFE  48 8D 45 C8                     lea rax, [rbp - 0x38]
00BE3D02  B9 04 00 00 00                  mov ecx, 4
00BE3D07  44 88 00                        mov byte ptr [rax], r8b
00BE3D0A  48 FF C0                        inc rax
00BE3D0D  83 C1 FF                        add ecx, -1
00BE3D10  75 F5                           jne 0x140be3d07
00BE3D12  8B B3 2C 08 00 00               mov esi, dword ptr [rbx + 0x82c]
00BE3D18  45 8B C8                        mov r9d, r8d
00BE3D1B  85 F6                           test esi, esi
00BE3D1D  0F 84 C1 01 00 00               je 0x140be3ee4
00BE3D23  4C 8B B3 C0 0A 00 00            mov r14, qword ptr [rbx + 0xac0]
00BE3D2A  8B 4D C8                        mov ecx, dword ptr [rbp - 0x38]
00BE3D2D  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
00BE3D30  8B 7D C0                        mov edi, dword ptr [rbp - 0x40]
00BE3D33  4D 85 F6                        test r14, r14
00BE3D36  45 8B D8                        mov r11d, r8d
00BE3D39  4C 8B D3                        mov r10, rbx
00BE3D3C  4D 0F 45 D6                     cmovne r10, r14
00BE3D40  45 8B 82 28 08 00 00            mov r8d, dword ptr [r10 + 0x828]
00BE3D47  4D 03 C2                        add r8, r10
00BE3D4A  85 FF                           test edi, edi
00BE3D4C  74 0E                           je 0x140be3d5c
00BE3D4E  41 3B D1                        cmp edx, r9d
00BE3D51  77 09                           ja 0x140be3d5c
00BE3D53  44 8B C1                        mov r8d, ecx
00BE3D56  44 8B DA                        mov r11d, edx
00BE3D59  4D 03 C2                        add r8, r10
00BE3D5C  45 3B D9                        cmp r11d, r9d
00BE3D5F  0F 84 0B 01 00 00               je 0x140be3e70
00BE3D65  41 8B F9                        mov edi, r9d
00BE3D68  41 BF 01 00 00 00               mov r15d, 1
00BE3D6E  41 2B FB                        sub edi, r11d
00BE3D71  49 BC AB AA AA AA AA AA AA AA   movabs r12, 0xaaaaaaaaaaaaaaab
00BE3D7B  45 8B D9                        mov r11d, r9d
00BE3D7E  41 8B 08                        mov ecx, dword ptr [r8]
00BE3D81  41 2B CF                        sub ecx, r15d
00BE3D84  0F 84 BB 00 00 00               je 0x140be3e45
00BE3D8A  83 E9 06                        sub ecx, 6
00BE3D8D  0F 84 A3 00 00 00               je 0x140be3e36
00BE3D93  41 2B CF                        sub ecx, r15d
00BE3D96  0F 84 8D 00 00 00               je 0x140be3e29
00BE3D9C  83 E9 02                        sub ecx, 2
00BE3D9F  74 7C                           je 0x140be3e1d
00BE3DA1  83 E9 12                        sub ecx, 0x12
00BE3DA4  74 70                           je 0x140be3e16
00BE3DA6  83 E9 02                        sub ecx, 2
00BE3DA9  74 3E                           je 0x140be3de9
00BE3DAB  83 E9 03                        sub ecx, 3
00BE3DAE  74 11                           je 0x140be3dc1
00BE3DB0  83 F9 0A                        cmp ecx, 0xa
00BE3DB3  0F 84 8C 00 00 00               je 0x140be3e45
00BE3DB9  41 8B C5                        mov eax, r13d
00BE3DBC  E9 99 00 00 00                  jmp 0x140be3e5a
00BE3DC1  41 8B 48 20                     mov ecx, dword ptr [r8 + 0x20]
00BE3DC5  41 8B 50 28                     mov edx, dword ptr [r8 + 0x28]
00BE3DC9  81 E1 FF 0F 00 00               and ecx, 0xfff
00BE3DCF  48 81 C2 FF 0F 00 00            add rdx, 0xfff
00BE3DD6  48 03 D1                        add rdx, rcx
00BE3DD9  48 C1 EA 0C                     shr rdx, 0xc
00BE3DDD  8D 04 92                        lea eax, [rdx + rdx*4]
00BE3DE0  8D 04 85 30 00 00 00            lea eax, [rax*4 + 0x30]
00BE3DE7  EB 71                           jmp 0x140be3e5a
00BE3DE9  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
00BE3DED  8D 48 FF                        lea ecx, [rax - 1]
00BE3DF0  F7 D8                           neg eax
00BE3DF2  1B C0                           sbb eax, eax
00BE3DF4  23 C8                           and ecx, eax
00BE3DF6  49 8B C4                        mov rax, r12
00BE3DF9  48 F7 E1                        mul rcx
00BE3DFC  41 0F B7 40 28                  movzx eax, word ptr [r8 + 0x28]
00BE3E01  48 C1 EA 03                     shr rdx, 3
00BE3E05  83 C2 07                        add edx, 7
00BE3E08  83 E2 F8                        and edx, 0xfffffff8
00BE3E0B  83 C0 02                        add eax, 2
00BE3E0E  8D 04 40                        lea eax, [rax + rax*2]
00BE3E11  8D 04 C2                        lea eax, [rdx + rax*8]
00BE3E14  EB 44                           jmp 0x140be3e5a
00BE3E16  41 0F B7 40 28                  movzx eax, word ptr [r8 + 0x28]
00BE3E1B  EB 11                           jmp 0x140be3e2e
00BE3E1D  41 8B 40 1C                     mov eax, dword ptr [r8 + 0x1c]
00BE3E21  83 C0 03                        add eax, 3
00BE3E24  C1 E0 04                        shl eax, 4
00BE3E27  EB 31                           jmp 0x140be3e5a
00BE3E29  41 0F B7 40 20                  movzx eax, word ptr [r8 + 0x20]
00BE3E2E  83 C0 37                        add eax, 0x37
00BE3E31  83 E0 F8                        and eax, 0xfffffff8
00BE3E34  EB 24                           jmp 0x140be3e5a
00BE3E36  41 8B 40 18                     mov eax, dword ptr [r8 + 0x18]
00BE3E3A  83 C0 02                        add eax, 2
00BE3E3D  8D 04 40                        lea eax, [rax + rax*2]
00BE3E40  C1 E0 03                        shl eax, 3
00BE3E43  EB 15                           jmp 0x140be3e5a
00BE3E45  41 8B 48 10                     mov ecx, dword ptr [r8 + 0x10]
00BE3E49  49 8B C4                        mov rax, r12
00BE3E4C  48 F7 E1                        mul rcx
00BE3E4F  48 C1 EA 03                     shr rdx, 3
00BE3E53  8D 04 95 30 00 00 00            lea eax, [rdx*4 + 0x30]
00BE3E5A  4C 03 C0                        add r8, rax
00BE3E5D  49 2B FF                        sub rdi, r15
00BE3E60  0F 85 18 FF FF FF               jne 0x140be3d7e
00BE3E66  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00BE3E6B  44 8B 64 24 78                  mov r12d, dword ptr [rsp + 0x78]
00BE3E70  B8 01 00 00 00                  mov eax, 1
00BE3E75  41 8B C8                        mov ecx, r8d
00BE3E78  8B F8                           mov edi, eax
00BE3E7A  89 45 C0                        mov dword ptr [rbp - 0x40], eax
00BE3E7D  41 8B 00                        mov eax, dword ptr [r8]
00BE3E80  41 2B CA                        sub ecx, r10d
00BE3E83  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
00BE3E86  41 8B D3                        mov edx, r11d
00BE3E89  89 55 C4                        mov dword ptr [rbp - 0x3c], edx
00BE3E8C  3B C7                           cmp eax, edi
00BE3E8E  74 0A                           je 0x140be3e9a
00BE3E90  83 F8 0C                        cmp eax, 0xc
00BE3E93  74 05                           je 0x140be3e9a
00BE3E95  83 F8 2B                        cmp eax, 0x2b
00BE3E98  75 11                           jne 0x140be3eab
00BE3E9A  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
00BE3E9F  4D 39 50 08                     cmp qword ptr [r8 + 8], r10
00BE3EA3  75 06                           jne 0x140be3eab
00BE3EA5  45 39 60 10                     cmp dword ptr [r8 + 0x10], r12d
00BE3EA9  74 1D                           je 0x140be3ec8
00BE3EAB  83 C0 DF                        add eax, -0x21
00BE3EAE  3B C7                           cmp eax, edi
00BE3EB0  77 06                           ja 0x140be3eb8
00BE3EB2  4D 39 78 20                     cmp qword ptr [r8 + 0x20], r15
00BE3EB6  74 10                           je 0x140be3ec8
00BE3EB8  44 03 CF                        add r9d, edi
00BE3EBB  44 3B CE                        cmp r9d, esi
00BE3EBE  73 1D                           jae 0x140be3edd
00BE3EC0  45 33 C0                        xor r8d, r8d
00BE3EC3  E9 6B FE FF FF                  jmp 0x140be3d33
00BE3EC8  45 33 E4                        xor r12d, r12d
00BE3ECB  4D 85 C0                        test r8, r8
00BE3ECE  0F 85 B6 00 00 00               jne 0x140be3f8a
00BE3ED4  44 8B B5 F8 00 00 00            mov r14d, dword ptr [rbp + 0xf8]
00BE3EDB  EB 0A                           jmp 0x140be3ee7
00BE3EDD  44 8B B5 F8 00 00 00            mov r14d, dword ptr [rbp + 0xf8]
00BE3EE4  45 33 E4                        xor r12d, r12d
00BE3EE7  8B 8D F0 00 00 00               mov ecx, dword ptr [rbp + 0xf0]
00BE3EED  F6 C1 10                        test cl, 0x10
00BE3EF0  74 1A                           je 0x140be3f0c
00BE3EF2  F7 83 DC 09 00 00 00 04 00 00   test dword ptr [rbx + 0x9dc], 0x400
00BE3EFC  75 0E                           jne 0x140be3f0c
00BE3EFE  44 8B F1                        mov r14d, ecx
00BE3F01  41 83 E6 EF                     and r14d, 0xffffffef
00BE3F05  44 89 B5 F8 00 00 00            mov dword ptr [rbp + 0xf8], r14d
00BE3F0C  41 F6 C6 10                     test r14b, 0x10
00BE3F10  74 1A                           je 0x140be3f2c
00BE3F12  49 8B D7                        mov rdx, r15
00BE3F15  48 8B CB                        mov rcx, rbx
00BE3F18  E8 13 4E 00 00                  call 0x140be8d30
00BE3F1D  85 C0                           test eax, eax
00BE3F1F  75 0B                           jne 0x140be3f2c
00BE3F21  41 83 E6 EF                     and r14d, 0xffffffef
00BE3F25  44 89 B5 F8 00 00 00            mov dword ptr [rbp + 0xf8], r14d
00BE3F2C  41 F6 C6 02                     test r14b, 2
00BE3F30  74 62                           je 0x140be3f94
00BE3F32  48 8B 83 08 02 00 00            mov rax, qword ptr [rbx + 0x208]
00BE3F39  49 8B CF                        mov rcx, r15
00BE3F3C  E8 1F 6B 00 00                  call 0x140beaa60
00BE3F41  48 8B 83 00 02 00 00            mov rax, qword ptr [rbx + 0x200]
00BE3F48  4C 8D 4D D0                     lea r9, [rbp - 0x30]
00BE3F4C  45 33 C0                        xor r8d, r8d
00BE3F4F  49 8B CF                        mov rcx, r15
00BE3F52  45 8D 68 01                     lea r13d, [r8 + 1]
00BE3F56  41 8A D5                        mov dl, r13b
00BE3F59  E8 02 6B 00 00                  call 0x140beaa60
00BE3F5E  48 85 C0                        test rax, rax
00BE3F61  74 27                           je 0x140be3f8a
00BE3F63  83 7D D0 28                     cmp dword ptr [rbp - 0x30], 0x28
00BE3F67  72 21                           jb 0x140be3f8a
00BE3F69  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00BE3F6C  48 8D 93 70 09 00 00            lea rdx, [rbx + 0x970]
00BE3F73  48 8B 83 E0 00 00 00            mov rax, qword ptr [rbx + 0xe0]
00BE3F7A  45 8D 45 04                     lea r8d, [r13 + 4]
00BE3F7E  49 03 CF                        add rcx, r15
00BE3F81  E8 DA 6A 00 00                  call 0x140beaa60
00BE3F86  85 C0                           test eax, eax
00BE3F88  74 10                           je 0x140be3f9a
00BE3F8A  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00BE3F8F  E9 B9 1E 00 00                  jmp 0x140be5e4d
00BE3F94  41 BD 01 00 00 00               mov r13d, 1
00BE3F9A  48 8B B3 28 05 00 00            mov rsi, qword ptr [rbx + 0x528]
00BE3FA1  41 8B C6                        mov eax, r14d
00BE3FA4  41 23 C5                        and eax, r13d
00BE3FA7  8B F8                           mov edi, eax
00BE3FA9  89 45 80                        mov dword ptr [rbp - 0x80], eax
00BE3FAC  41 33 FD                        xor edi, r13d
00BE3FAF  41 03 FD                        add edi, r13d
00BE3FB2  FA                              cli
00BE3FB3  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00BE3FBC  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
00BE3FC0  48 8B 83 58 06 00 00            mov rax, qword ptr [rbx + 0x658]
00BE3FC7  48 8B 0C 01                     mov rcx, qword ptr [rcx + rax]
00BE3FCB  FB                              sti
00BE3FCC  48 8B 83 78 01 00 00            mov rax, qword ptr [rbx + 0x178]
00BE3FD3  E8 88 6A 00 00                  call 0x140beaa60
00BE3FD8  48 8B 8B 30 05 00 00            mov rcx, qword ptr [rbx + 0x530]
00BE3FDF  41 8A D5                        mov dl, r13b
00BE3FE2  48 8B 83 F8 00 00 00            mov rax, qword ptr [rbx + 0xf8]
00BE3FE9  E8 72 6A 00 00                  call 0x140beaa60
00BE3FEE  48 8B 16                        mov rdx, qword ptr [rsi]
00BE3FF1  48 3B D6                        cmp rdx, rsi
00BE3FF4  74 48                           je 0x140be403e
00BE3FF6  4C 8B 8B 58 07 00 00            mov r9, qword ptr [rbx + 0x758]
00BE3FFD  4C 8B 93 60 07 00 00            mov r10, qword ptr [rbx + 0x760]
00BE4004  4C 8B 9B 68 07 00 00            mov r11, qword ptr [rbx + 0x768]
00BE400B  48 8B CA                        mov rcx, rdx
00BE400E  49 2B C9                        sub rcx, r9
00BE4011  49 8B 04 0A                     mov rax, qword ptr [r10 + rcx]
00BE4015  46 8B 04 19                     mov r8d, dword ptr [rcx + r11]
00BE4019  4C 03 C0                        add r8, rax
00BE401C  4C 3B F8                        cmp r15, rax
00BE401F  72 05                           jb 0x140be4026
00BE4021  4D 3B F8                        cmp r15, r8
00BE4024  72 0A                           jb 0x140be4030
00BE4026  48 8B 12                        mov rdx, qword ptr [rdx]
00BE4029  48 3B D6                        cmp rdx, rsi
00BE402C  75 DD                           jne 0x140be400b
00BE402E  EB 0E                           jmp 0x140be403e
00BE4030  48 8B 83 E8 00 00 00            mov rax, qword ptr [rbx + 0xe8]
00BE4037  8B D7                           mov edx, edi
00BE4039  E8 22 6A 00 00                  call 0x140beaa60
00BE403E  48 8B 8B 30 05 00 00            mov rcx, qword ptr [rbx + 0x530]
00BE4045  48 8B 83 28 01 00 00            mov rax, qword ptr [rbx + 0x128]
00BE404C  E8 0F 6A 00 00                  call 0x140beaa60
00BE4051  48 8B 83 80 01 00 00            mov rax, qword ptr [rbx + 0x180]
00BE4058  E8 03 6A 00 00                  call 0x140beaa60
00BE405D  F7 83 D8 09 00 00 00 00 00 20   test dword ptr [rbx + 0x9d8], 0x20000000
00BE4067  74 17                           je 0x140be4080
00BE4069  45 8B C6                        mov r8d, r14d
00BE406C  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00BE4071  49 8B D7                        mov rdx, r15
00BE4074  E8 13 BF 00 00                  call 0x140beff8c
00BE4079  8B C8                           mov ecx, eax
00BE407B  E9 53 13 00 00                  jmp 0x140be53d3
00BE4080  48 8B 83 00 02 00 00            mov rax, qword ptr [rbx + 0x200]
00BE4087  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00BE408C  45 33 C0                        xor r8d, r8d
00BE408F  4C 89 65 20                     mov qword ptr [rbp + 0x20], r12
00BE4093  41 8A D5                        mov dl, r13b
00BE4096  44 89 65 E8                     mov dword ptr [rbp - 0x18], r12d
00BE409A  49 8B CF                        mov rcx, r15
00BE409D  E8 BE 69 00 00                  call 0x140beaa60
00BE40A2  48 85 C0                        test rax, rax
00BE40A5  75 09                           jne 0x140be40b0
00BE40A7  41 8B CC                        mov ecx, r12d
00BE40AA  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00BE40AE  EB 04                           jmp 0x140be40b4
00BE40B0  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00BE40B4  48 89 45 08                     mov qword ptr [rbp + 8], rax
00BE40B8  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00BE40BD  48 8B 83 00 02 00 00            mov rax, qword ptr [rbx + 0x200]
00BE40C4  41 B8 0C 00 00 00               mov r8d, 0xc
00BE40CA  89 4D DC                        mov dword ptr [rbp - 0x24], ecx
00BE40CD  41 8A D5                        mov dl, r13b
00BE40D0  49 8B CF                        mov rcx, r15
00BE40D3  E8 88 69 00 00                  call 0x140beaa60
00BE40D8  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00BE40DC  48 8B C8                        mov rcx, rax
00BE40DF  48 85 C0                        test rax, rax
00BE40E2  75 09                           jne 0x140be40ed
00BE40E4  41 8B C4                        mov eax, r12d
00BE40E7  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00BE40EB  EB 04                           jmp 0x140be40f1
00BE40ED  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00BE40F1  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00BE40F5  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00BE40FA  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
00BE40FE  BE 0A 00 00 00                  mov esi, 0xa
00BE4103  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00BE4106  44 8B C6                        mov r8d, esi
00BE4109  48 8B 83 00 02 00 00            mov rax, qword ptr [rbx + 0x200]
00BE4110  41 8A D5                        mov dl, r13b
00BE4113  49 8B CF                        mov rcx, r15
00BE4116  E8 45 69 00 00                  call 0x140beaa60
00BE411B  48 85 C0                        test rax, rax
00BE411E  75 09                           jne 0x140be4129
00BE4120  41 8B CC                        mov ecx, r12d
00BE4123  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00BE4127  EB 04                           jmp 0x140be412d
00BE4129  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00BE412D  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00BE4131  48 8B 83 08 02 00 00            mov rax, qword ptr [rbx + 0x208]
00BE4138  89 4D E4                        mov dword ptr [rbp - 0x1c], ecx
00BE413B  49 8B CF                        mov rcx, r15
00BE413E  E8 1D 69 00 00                  call 0x140beaa60
00BE4143  48 8B F8                        mov rdi, rax
00BE4146  48 85 C0                        test rax, rax
00BE4149  0F 85 22 01 00 00               jne 0x140be4271
00BE414F  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE4155  0F BA E1 14                     bt ecx, 0x14
00BE4159  0F 83 FC 1D 00 00               jae 0x140be5f5b
00BE415F  44 39 A3 18 09 00 00            cmp dword ptr [rbx + 0x918], r12d
00BE4166  0F 85 FB 00 00 00               jne 0x140be4267
00BE416C  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE4176  4C 89 A3 28 09 00 00            mov qword ptr [rbx + 0x928], r12
00BE417D  48 03 C3                        add rax, rbx
00BE4180  48 C7 83 30 09 00 00 0F 01 00 00  mov qword ptr [rbx + 0x930], 0x10f
00BE418B  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
00BE4192  4C 89 BB 38 09 00 00            mov qword ptr [rbx + 0x938], r15
00BE4199  44 89 AB 18 09 00 00            mov dword ptr [rbx + 0x918], r13d
00BE41A0  0F BA E1 1D                     bt ecx, 0x1d
00BE41A4  0F 82 BD 00 00 00               jb 0x140be4267
00BE41AA  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
00BE41B4  0F 84 AD 00 00 00               je 0x140be4267
00BE41BA  41 84 CD                        test r13b, cl
00BE41BD  0F 84 A4 00 00 00               je 0x140be4267
00BE41C3  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
00BE41C9  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE41CF  4C 8B 9B 38 08 00 00            mov r11, qword ptr [rbx + 0x838]
00BE41D6  2B C1                           sub eax, ecx
00BE41D8  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
00BE41DF  4C 8D 0C 19                     lea r9, [rcx + rbx]
00BE41E3  8B C8                           mov ecx, eax
00BE41E5  48 C1 E9 03                     shr rcx, 3
00BE41E9  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
00BE41ED  EB 21                           jmp 0x140be4210
00BE41EF  4D 31 01                        xor qword ptr [r9], r8
00BE41F2  49 8B C3                        mov rax, r11
00BE41F5  49 33 01                        xor rax, qword ptr [r9]
00BE41F8  41 0F B6 C8                     movzx ecx, r8b
00BE41FC  83 E1 3F                        and ecx, 0x3f
00BE41FF  49 D3 C8                        ror r8, cl
00BE4202  4C 03 C0                        add r8, rax
00BE4205  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE420C  49 83 C1 08                     add r9, 8
00BE4210  4D 3B CA                        cmp r9, r10
00BE4213  75 DA                           jne 0x140be41ef
00BE4215  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
00BE421D  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
00BE4224  74 41                           je 0x140be4267
00BE4226  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
00BE422C  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE4233  48 89 18                        mov qword ptr [rax], rbx
00BE4236  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE4239  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
00BE4240  44 39 A3 18 09 00 00            cmp dword ptr [rbx + 0x918], r12d
00BE4247  75 0E                           jne 0x140be4257
00BE4249  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE4250  49 33 C8                        xor rcx, r8
00BE4253  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE4257  33 D2                           xor edx, edx
00BE4259  41 B9 00 01 00 00               mov r9d, 0x100
00BE425F  48 8B CB                        mov rcx, rbx
00BE4262  E8 1D 41 00 00                  call 0x140be8384
00BE4267  B9 7B 00 00 C0                  mov ecx, 0xc000007b
00BE426C  E9 BA 07 00 00                  jmp 0x140be4a2b
00BE4271  48 8B 83 98 04 00 00            mov rax, qword ptr [rbx + 0x498]
00BE4278  48 8D 55 F8                     lea rdx, [rbp - 8]
00BE427C  49 8B CF                        mov rcx, r15
00BE427F  E8 DC 67 00 00                  call 0x140beaa60
00BE4284  8B B3 04 08 00 00               mov esi, dword ptr [rbx + 0x804]
00BE428A  44 8B 83 44 09 00 00            mov r8d, dword ptr [rbx + 0x944]
00BE4291  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
00BE4295  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00BE4298  89 45 EC                        mov dword ptr [rbp - 0x14], eax
00BE429B  8B 47 54                        mov eax, dword ptr [rdi + 0x54]
00BE429E  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00BE42A1  8D 86 20 01 00 00               lea eax, [rsi + 0x120]
00BE42A7  4C 89 7D 00                     mov qword ptr [rbp], r15
00BE42AB  3B 83 64 0A 00 00               cmp eax, dword ptr [rbx + 0xa64]
00BE42B1  0F 86 CC 00 00 00               jbe 0x140be4383
00BE42B7  8B D0                           mov edx, eax
00BE42B9  48 8B CB                        mov rcx, rbx
00BE42BC  E8 37 38 00 00                  call 0x140be7af8
00BE42C1  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00BE42C5  48 8B F8                        mov rdi, rax
00BE42C8  48 85 C0                        test rax, rax
00BE42CB  0F 84 55 07 00 00               je 0x140be4a26
00BE42D1  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE42D7  F6 C1 02                        test cl, 2
00BE42DA  0F 85 9A 00 00 00               jne 0x140be437a
00BE42E0  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE42E6  81 E1 00 00 00 10               and ecx, 0x10000000
00BE42EC  4C 8B 83 E8 07 00 00            mov r8, qword ptr [rbx + 0x7e8]
00BE42F3  F7 D9                           neg ecx
00BE42F5  1B D2                           sbb edx, edx
00BE42F7  23 93 44 09 00 00               and edx, dword ptr [rbx + 0x944]
00BE42FD  83 F8 08                        cmp eax, 8
00BE4300  72 15                           jb 0x140be4317
00BE4302  8B C8                           mov ecx, eax
00BE4304  48 C1 E9 03                     shr rcx, 3
00BE4308  4C 89 23                        mov qword ptr [rbx], r12
00BE430B  83 C0 F8                        add eax, -8
00BE430E  48 83 C3 08                     add rbx, 8
00BE4312  49 2B CD                        sub rcx, r13
00BE4315  75 F1                           jne 0x140be4308
00BE4317  85 C0                           test eax, eax
00BE4319  74 0B                           je 0x140be4326
00BE431B  44 88 23                        mov byte ptr [rbx], r12b
00BE431E  49 03 DD                        add rbx, r13
00BE4321  83 C0 FF                        add eax, -1
00BE4324  75 F5                           jne 0x140be431b
00BE4326  8B 9F 44 09 00 00               mov ebx, dword ptr [rdi + 0x944]
00BE432C  89 97 44 09 00 00               mov dword ptr [rdi + 0x944], edx
00BE4332  83 FA 03                        cmp edx, 3
00BE4335  74 2E                           je 0x140be4365
00BE4337  F7 87 D8 09 00 00 00 00 00 08   test dword ptr [rdi + 0x9d8], 0x8000000
00BE4341  75 19                           jne 0x140be435c
00BE4343  85 D2                           test edx, edx
00BE4345  74 15                           je 0x140be435c
00BE4347  48 8B 87 38 02 00 00            mov rax, qword ptr [rdi + 0x238]
00BE434E  49 8D 48 F8                     lea rcx, [r8 - 8]
00BE4352  48 8B 11                        mov rdx, qword ptr [rcx]
00BE4355  E8 06 67 00 00                  call 0x140beaa60
00BE435A  EB 18                           jmp 0x140be4374
00BE435C  48 8B 87 08 01 00 00            mov rax, qword ptr [rdi + 0x108]
00BE4363  EB 07                           jmp 0x140be436c
00BE4365  48 8B 87 68 03 00 00            mov rax, qword ptr [rdi + 0x368]
00BE436C  49 8B C8                        mov rcx, r8
00BE436F  E8 EC 66 00 00                  call 0x140beaa60
00BE4374  89 9F 44 09 00 00               mov dword ptr [rdi + 0x944], ebx
00BE437A  83 A7 D8 09 00 00 FD            and dword ptr [rdi + 0x9d8], 0xfffffffd
00BE4381  EB 0D                           jmp 0x140be4390
00BE4383  48 8B FB                        mov rdi, rbx
00BE4386  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
00BE438A  89 83 04 08 00 00               mov dword ptr [rbx + 0x804], eax
00BE4390  83 87 2C 08 00 00 06            add dword ptr [rdi + 0x82c], 6
00BE4397  4C 8D 14 37                     lea r10, [rdi + rsi]
00BE439B  33 DB                           xor ebx, ebx
00BE439D  4C 89 55 88                     mov qword ptr [rbp - 0x78], r10
00BE43A1  4C 8D 6D 00                     lea r13, [rbp]
00BE43A5  48 C7 44 24 68 06 00 00 00      mov qword ptr [rsp + 0x68], 6
00BE43AE  4C 8D 65 D8                     lea r12, [rbp - 0x28]
00BE43B2  44 8D 73 30                     lea r14d, [rbx + 0x30]
00BE43B6  44 8D 5B 01                     lea r11d, [rbx + 1]
00BE43BA  45 8B 3C 24                     mov r15d, dword ptr [r12]
00BE43BE  41 8B CE                        mov ecx, r14d
00BE43C1  49 8B 75 00                     mov rsi, qword ptr [r13]
00BE43C5  49 8B C2                        mov rax, r10
00BE43C8  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
00BE43CD  BA 06 00 00 00                  mov edx, 6
00BE43D2  48 89 18                        mov qword ptr [rax], rbx
00BE43D5  83 C1 F8                        add ecx, -8
00BE43D8  48 83 C0 08                     add rax, 8
00BE43DC  49 2B D3                        sub rdx, r11
00BE43DF  75 F1                           jne 0x140be43d2
00BE43E1  85 C9                           test ecx, ecx
00BE43E3  74 0A                           je 0x140be43ef
00BE43E5  88 18                           mov byte ptr [rax], bl
00BE43E7  49 03 C3                        add rax, r11
00BE43EA  83 C1 FF                        add ecx, -1
00BE43ED  75 F6                           jne 0x140be43e5
00BE43EF  41 89 1A                        mov dword ptr [r10], ebx
00BE43F2  4A 8D 0C 3E                     lea rcx, [rsi + r15]
00BE43F6  49 89 72 08                     mov qword ptr [r10 + 8], rsi
00BE43FA  4C 8B CE                        mov r9, rsi
00BE43FD  45 89 7A 10                     mov dword ptr [r10 + 0x10], r15d
00BE4401  48 8B C6                        mov rax, rsi
00BE4404  44 01 BF 48 08 00 00            add dword ptr [rdi + 0x848], r15d
00BE440B  8B 9F 34 08 00 00               mov ebx, dword ptr [rdi + 0x834]
00BE4411  4C 8B B7 38 08 00 00            mov r14, qword ptr [rdi + 0x838]
00BE4418  48 3B F1                        cmp rsi, rcx
00BE441B  73 0C                           jae 0x140be4429
00BE441D  0F 18 00                        prefetchnta byte ptr [rax]
00BE4420  48 83 C0 40                     add rax, 0x40
00BE4424  48 3B C1                        cmp rax, rcx
00BE4427  72 F4                           jb 0x140be441d
00BE4429  45 8B DF                        mov r11d, r15d
00BE442C  4D 8B C6                        mov r8, r14
00BE442F  41 C1 EB 07                     shr r11d, 7
00BE4433  45 85 DB                        test r11d, r11d
00BE4436  74 62                           je 0x140be449a
00BE4438  BF 01 00 00 00                  mov edi, 1
00BE443D  49 BF 01 20 00 04 80 00 10 70   movabs r15, 0x7010008004002001
00BE4447  B8 08 00 00 00                  mov eax, 8
00BE444C  4D 33 01                        xor r8, qword ptr [r9]
00BE444F  8B CB                           mov ecx, ebx
00BE4451  49 D3 C0                        rol r8, cl
00BE4454  4D 33 41 08                     xor r8, qword ptr [r9 + 8]
00BE4458  49 83 C1 10                     add r9, 0x10
00BE445C  49 D3 C0                        rol r8, cl
00BE445F  48 2B C7                        sub rax, rdi
00BE4462  75 E8                           jne 0x140be444c
00BE4464  49 8B C9                        mov rcx, r9
00BE4467  48 2B CE                        sub rcx, rsi
00BE446A  49 33 CE                        xor rcx, r14
00BE446D  48 8B C1                        mov rax, rcx
00BE4470  48 C1 C0 11                     rol rax, 0x11
00BE4474  48 33 C8                        xor rcx, rax
00BE4477  49 8B C7                        mov rax, r15
00BE447A  48 F7 E1                        mul rcx
00BE447D  33 D8                           xor ebx, eax
00BE447F  48 89 55 48                     mov qword ptr [rbp + 0x48], rdx
00BE4483  33 DA                           xor ebx, edx
00BE4485  83 E3 3F                        and ebx, 0x3f
00BE4488  0F 44 DF                        cmove ebx, edi
00BE448B  41 83 C3 FF                     add r11d, -1
00BE448F  75 B6                           jne 0x140be4447
00BE4491  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
00BE4495  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
00BE449A  41 8B D7                        mov edx, r15d
00BE449D  41 BB 01 00 00 00               mov r11d, 1
00BE44A3  83 E2 7F                        and edx, 0x7f
00BE44A6  83 FA 08                        cmp edx, 8
00BE44A9  72 1A                           jb 0x140be44c5
00BE44AB  8B C2                           mov eax, edx
00BE44AD  48 C1 E8 03                     shr rax, 3
00BE44B1  4D 33 01                        xor r8, qword ptr [r9]
00BE44B4  8B CB                           mov ecx, ebx
00BE44B6  49 D3 C0                        rol r8, cl
00BE44B9  49 83 C1 08                     add r9, 8
00BE44BD  83 C2 F8                        add edx, -8
00BE44C0  49 2B C3                        sub rax, r11
00BE44C3  75 EC                           jne 0x140be44b1
00BE44C5  85 D2                           test edx, edx
00BE44C7  74 14                           je 0x140be44dd
00BE44C9  41 0F B6 01                     movzx eax, byte ptr [r9]
00BE44CD  8B CB                           mov ecx, ebx
00BE44CF  4C 33 C0                        xor r8, rax
00BE44D2  4D 03 CB                        add r9, r11
00BE44D5  49 D3 C0                        rol r8, cl
00BE44D8  83 C2 FF                        add edx, -1
00BE44DB  75 EC                           jne 0x140be44c9
00BE44DD  49 8B C0                        mov rax, r8
00BE44E0  48 C1 E8 1F                     shr rax, 0x1f
00BE44E4  33 DB                           xor ebx, ebx
00BE44E6  EB 07                           jmp 0x140be44ef
00BE44E8  44 33 C0                        xor r8d, eax
00BE44EB  48 C1 E8 1F                     shr rax, 0x1f
00BE44EF  48 85 C0                        test rax, rax
00BE44F2  75 F4                           jne 0x140be44e8
00BE44F4  41 0F BA F0 1F                  btr r8d, 0x1f
00BE44F9  44 8D 70 30                     lea r14d, [rax + 0x30]
00BE44FD  45 89 42 14                     mov dword ptr [r10 + 0x14], r8d
00BE4501  49 83 C4 04                     add r12, 4
00BE4505  44 01 BF 48 08 00 00            add dword ptr [rdi + 0x848], r15d
00BE450C  4D 03 D6                        add r10, r14
00BE450F  49 83 C5 08                     add r13, 8
00BE4513  4C 29 5C 24 68                  sub qword ptr [rsp + 0x68], r11
00BE4518  0F 85 9C FE FF FF               jne 0x140be43ba
00BE451E  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
00BE4522  48 85 FF                        test rdi, rdi
00BE4525  0F 84 FB 04 00 00               je 0x140be4a26
00BE452B  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00BE4530  49 89 74 24 18                  mov qword ptr [r12 + 0x18], rsi
00BE4535  41 C7 04 24 2C 00 00 00         mov dword ptr [r12], 0x2c
00BE453D  F7 87 D8 09 00 00 00 00 10 08   test dword ptr [rdi + 0x9d8], 0x8100000
00BE4547  75 26                           jne 0x140be456f
00BE4549  F7 87 DC 09 00 00 00 80 00 00   test dword ptr [rdi + 0x9dc], 0x8000
00BE4553  74 1A                           je 0x140be456f
00BE4555  45 09 5C 24 20                  or dword ptr [r12 + 0x20], r11d
00BE455A  48 8B D6                        mov rdx, rsi
00BE455D  48 8B CF                        mov rcx, rdi
00BE4560  E8 CB 47 00 00                  call 0x140be8d30
00BE4565  85 C0                           test eax, eax
00BE4567  74 06                           je 0x140be456f
00BE4569  41 83 4C 24 20 04               or dword ptr [r12 + 0x20], 4
00BE456F  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
00BE4574  48 8D 45 D4                     lea rax, [rbp - 0x2c]
00BE4578  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00BE457D  48 8D 4D 98                     lea rcx, [rbp - 0x68]
00BE4581  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BE4586  4C 8B CE                        mov r9, rsi
00BE4589  48 8D 45 A8                     lea rax, [rbp - 0x58]
00BE458D  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00BE4591  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BE4596  8B 85 F8 00 00 00               mov eax, dword ptr [rbp + 0xf8]
00BE459C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00BE45A0  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00BE45A5  E8 06 1B 00 00                  call 0x140be60b0
00BE45AA  8B C8                           mov ecx, eax
00BE45AC  85 C0                           test eax, eax
00BE45AE  79 17                           jns 0x140be45c7
00BE45B0  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
00BE45B7  45 33 E4                        xor r12d, r12d
00BE45BA  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00BE45BF  48 89 3E                        mov qword ptr [rsi], rdi
00BE45C2  E9 23 0E 00 00                  jmp 0x140be53ea
00BE45C7  4C 2B 64 24 48                  sub r12, qword ptr [rsp + 0x48]
00BE45CC  BA 06 00 00 00                  mov edx, 6
00BE45D1  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
00BE45D5  41 8B CE                        mov ecx, r14d
00BE45D8  44 8B 4D D4                     mov r9d, dword ptr [rbp - 0x2c]
00BE45DC  4C 03 E3                        add r12, rbx
00BE45DF  44 2B 4D A8                     sub r9d, dword ptr [rbp - 0x58]
00BE45E3  44 8B 5D A8                     mov r11d, dword ptr [rbp - 0x58]
00BE45E7  44 8D 6A 02                     lea r13d, [rdx + 2]
00BE45EB  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
00BE45EF  44 8D 42 FB                     lea r8d, [rdx - 5]
00BE45F3  4D 8D BC 24 C0 00 00 00         lea r15, [r12 + 0xc0]
00BE45FB  4C 03 DE                        add r11, rsi
00BE45FE  49 8B C7                        mov rax, r15
00BE4601  48 C7 00 00 00 00 00            mov qword ptr [rax], 0
00BE4608  83 C1 F8                        add ecx, -8
00BE460B  49 03 C5                        add rax, r13
00BE460E  49 2B D0                        sub rdx, r8
00BE4611  75 EE                           jne 0x140be4601
00BE4613  85 C9                           test ecx, ecx
00BE4615  74 0A                           je 0x140be4621
00BE4617  88 10                           mov byte ptr [rax], dl
00BE4619  49 03 C0                        add rax, r8
00BE461C  83 C1 FF                        add ecx, -1
00BE461F  75 F6                           jne 0x140be4617
00BE4621  41 89 17                        mov dword ptr [r15], edx
00BE4624  4D 8B D3                        mov r10, r11
00BE4627  4D 89 5F 08                     mov qword ptr [r15 + 8], r11
00BE462B  49 8B C3                        mov rax, r11
00BE462E  45 89 4F 10                     mov dword ptr [r15 + 0x10], r9d
00BE4632  44 01 8B 48 08 00 00            add dword ptr [rbx + 0x848], r9d
00BE4639  8B BB 34 08 00 00               mov edi, dword ptr [rbx + 0x834]
00BE463F  4C 8B B3 38 08 00 00            mov r14, qword ptr [rbx + 0x838]
00BE4646  41 8B C9                        mov ecx, r9d
00BE4649  49 03 CB                        add rcx, r11
00BE464C  4C 3B D9                        cmp r11, rcx
00BE464F  73 0C                           jae 0x140be465d
00BE4651  0F 18 00                        prefetchnta byte ptr [rax]
00BE4654  48 83 C0 40                     add rax, 0x40
00BE4658  48 3B C1                        cmp rax, rcx
00BE465B  72 F4                           jb 0x140be4651
00BE465D  41 8B F1                        mov esi, r9d
00BE4660  4D 8B C6                        mov r8, r14
00BE4663  C1 EE 07                        shr esi, 7
00BE4666  BA 01 00 00 00                  mov edx, 1
00BE466B  85 F6                           test esi, esi
00BE466D  74 5B                           je 0x140be46ca
00BE466F  49 BC 01 20 00 04 80 00 10 70   movabs r12, 0x7010008004002001
00BE4679  49 8B C5                        mov rax, r13
00BE467C  4D 33 02                        xor r8, qword ptr [r10]
00BE467F  8B CF                           mov ecx, edi
00BE4681  4D 03 D5                        add r10, r13
00BE4684  49 D3 C0                        rol r8, cl
00BE4687  4D 33 02                        xor r8, qword ptr [r10]
00BE468A  4D 03 D5                        add r10, r13
00BE468D  49 D3 C0                        rol r8, cl
00BE4690  48 2B C2                        sub rax, rdx
00BE4693  75 E7                           jne 0x140be467c
00BE4695  49 8B CA                        mov rcx, r10
00BE4698  49 2B CB                        sub rcx, r11
00BE469B  49 33 CE                        xor rcx, r14
00BE469E  48 8B C1                        mov rax, rcx
00BE46A1  48 C1 C0 11                     rol rax, 0x11
00BE46A5  48 33 C8                        xor rcx, rax
00BE46A8  49 8B C4                        mov rax, r12
00BE46AB  48 F7 E1                        mul rcx
00BE46AE  48 89 55 50                     mov qword ptr [rbp + 0x50], rdx
00BE46B2  33 D0                           xor edx, eax
00BE46B4  33 FA                           xor edi, edx
00BE46B6  BA 01 00 00 00                  mov edx, 1
00BE46BB  83 E7 3F                        and edi, 0x3f
00BE46BE  0F 44 FA                        cmove edi, edx
00BE46C1  83 C6 FF                        add esi, -1
00BE46C4  75 B3                           jne 0x140be4679
00BE46C6  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
00BE46CA  41 83 E1 7F                     and r9d, 0x7f
00BE46CE  45 3B CD                        cmp r9d, r13d
00BE46D1  72 1B                           jb 0x140be46ee
00BE46D3  41 8B C1                        mov eax, r9d
00BE46D6  48 C1 E8 03                     shr rax, 3
00BE46DA  4D 33 02                        xor r8, qword ptr [r10]
00BE46DD  8B CF                           mov ecx, edi
00BE46DF  49 D3 C0                        rol r8, cl
00BE46E2  4D 03 D5                        add r10, r13
00BE46E5  41 83 C1 F8                     add r9d, -8
00BE46E9  48 2B C2                        sub rax, rdx
00BE46EC  75 EC                           jne 0x140be46da
00BE46EE  45 33 DB                        xor r11d, r11d
00BE46F1  45 85 C9                        test r9d, r9d
00BE46F4  74 15                           je 0x140be470b
00BE46F6  41 0F B6 02                     movzx eax, byte ptr [r10]
00BE46FA  8B CF                           mov ecx, edi
00BE46FC  4C 33 C0                        xor r8, rax
00BE46FF  4C 03 D2                        add r10, rdx
00BE4702  49 D3 C0                        rol r8, cl
00BE4705  41 83 C1 FF                     add r9d, -1
00BE4709  75 EB                           jne 0x140be46f6
00BE470B  49 8B C0                        mov rax, r8
00BE470E  EB 03                           jmp 0x140be4713
00BE4710  44 33 C0                        xor r8d, eax
00BE4713  48 C1 E8 1F                     shr rax, 0x1f
00BE4717  48 85 C0                        test rax, rax
00BE471A  75 F4                           jne 0x140be4710
00BE471C  41 0F BA F0 1F                  btr r8d, 0x1f
00BE4721  44 8D 70 30                     lea r14d, [rax + 0x30]
00BE4725  45 89 47 14                     mov dword ptr [r15 + 0x14], r8d
00BE4729  49 8D 74 24 60                  lea rsi, [r12 + 0x60]
00BE472E  45 89 B4 24 F0 00 00 00         mov dword ptr [r12 + 0xf0], r14d
00BE4736  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00BE473B  48 85 F6                        test rsi, rsi
00BE473E  0F 85 50 02 00 00               jne 0x140be4994
00BE4744  8B B3 04 08 00 00               mov esi, dword ptr [rbx + 0x804]
00BE474A  44 8B 83 44 09 00 00            mov r8d, dword ptr [rbx + 0x944]
00BE4751  8D 46 30                        lea eax, [rsi + 0x30]
00BE4754  3B 83 64 0A 00 00               cmp eax, dword ptr [rbx + 0xa64]
00BE475A  0F 86 D1 00 00 00               jbe 0x140be4831
00BE4760  8B D0                           mov edx, eax
00BE4762  48 8B CB                        mov rcx, rbx
00BE4765  E8 8E 33 00 00                  call 0x140be7af8
00BE476A  45 33 DB                        xor r11d, r11d
00BE476D  48 8B F8                        mov rdi, rax
00BE4770  48 85 C0                        test rax, rax
00BE4773  0F 84 AD 02 00 00               je 0x140be4a26
00BE4779  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE477F  F6 C1 02                        test cl, 2
00BE4782  0F 85 A0 00 00 00               jne 0x140be4828
00BE4788  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE478E  45 8D 4E D1                     lea r9d, [r14 - 0x2f]
00BE4792  4C 8B 83 E8 07 00 00            mov r8, qword ptr [rbx + 0x7e8]
00BE4799  81 E1 00 00 00 10               and ecx, 0x10000000
00BE479F  F7 D9                           neg ecx
00BE47A1  1B D2                           sbb edx, edx
00BE47A3  23 93 44 09 00 00               and edx, dword ptr [rbx + 0x944]
00BE47A9  41 3B C5                        cmp eax, r13d
00BE47AC  72 14                           jb 0x140be47c2
00BE47AE  8B C8                           mov ecx, eax
00BE47B0  48 C1 E9 03                     shr rcx, 3
00BE47B4  4C 89 1B                        mov qword ptr [rbx], r11
00BE47B7  83 C0 F8                        add eax, -8
00BE47BA  49 03 DD                        add rbx, r13
00BE47BD  49 2B C9                        sub rcx, r9
00BE47C0  75 F2                           jne 0x140be47b4
00BE47C2  85 C0                           test eax, eax
00BE47C4  74 0B                           je 0x140be47d1
00BE47C6  44 88 1B                        mov byte ptr [rbx], r11b
00BE47C9  49 03 D9                        add rbx, r9
00BE47CC  83 C0 FF                        add eax, -1
00BE47CF  75 F5                           jne 0x140be47c6
00BE47D1  8B 9F 44 09 00 00               mov ebx, dword ptr [rdi + 0x944]
00BE47D7  89 97 44 09 00 00               mov dword ptr [rdi + 0x944], edx
00BE47DD  83 FA 03                        cmp edx, 3
00BE47E0  74 2E                           je 0x140be4810
00BE47E2  F7 87 D8 09 00 00 00 00 00 08   test dword ptr [rdi + 0x9d8], 0x8000000
00BE47EC  75 19                           jne 0x140be4807
00BE47EE  85 D2                           test edx, edx
00BE47F0  74 15                           je 0x140be4807
00BE47F2  48 8B 87 38 02 00 00            mov rax, qword ptr [rdi + 0x238]
00BE47F9  49 8D 48 F8                     lea rcx, [r8 - 8]
00BE47FD  48 8B 11                        mov rdx, qword ptr [rcx]
00BE4800  E8 5B 62 00 00                  call 0x140beaa60
00BE4805  EB 18                           jmp 0x140be481f
00BE4807  48 8B 87 08 01 00 00            mov rax, qword ptr [rdi + 0x108]
00BE480E  EB 07                           jmp 0x140be4817
00BE4810  48 8B 87 68 03 00 00            mov rax, qword ptr [rdi + 0x368]
00BE4817  49 8B C8                        mov rcx, r8
00BE481A  E8 41 62 00 00                  call 0x140beaa60
00BE481F  89 9F 44 09 00 00               mov dword ptr [rdi + 0x944], ebx
00BE4825  45 33 DB                        xor r11d, r11d
00BE4828  83 A7 D8 09 00 00 FD            and dword ptr [rdi + 0x9d8], 0xfffffffd
00BE482F  EB 09                           jmp 0x140be483a
00BE4831  48 8B FB                        mov rdi, rbx
00BE4834  89 83 04 08 00 00               mov dword ptr [rbx + 0x804], eax
00BE483A  41 B8 01 00 00 00               mov r8d, 1
00BE4840  41 8B CE                        mov ecx, r14d
00BE4843  44 01 87 2C 08 00 00            add dword ptr [rdi + 0x82c], r8d
00BE484A  48 03 F7                        add rsi, rdi
00BE484D  48 8B C6                        mov rax, rsi
00BE4850  41 8D 50 05                     lea edx, [r8 + 5]
00BE4854  4C 89 18                        mov qword ptr [rax], r11
00BE4857  83 C1 F8                        add ecx, -8
00BE485A  49 03 C5                        add rax, r13
00BE485D  49 2B D0                        sub rdx, r8
00BE4860  75 F2                           jne 0x140be4854
00BE4862  85 C9                           test ecx, ecx
00BE4864  74 0B                           je 0x140be4871
00BE4866  44 88 18                        mov byte ptr [rax], r11b
00BE4869  49 03 C0                        add rax, r8
00BE486C  83 C1 FF                        add ecx, -1
00BE486F  75 F5                           jne 0x140be4866
00BE4871  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
00BE4875  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
00BE487A  4D 8B CF                        mov r9, r15
00BE487D  C7 06 0D 00 00 00               mov dword ptr [rsi], 0xd
00BE4883  4C 89 7E 08                     mov qword ptr [rsi + 8], r15
00BE4887  44 89 76 10                     mov dword ptr [rsi + 0x10], r14d
00BE488B  44 01 B7 48 08 00 00            add dword ptr [rdi + 0x848], r14d
00BE4892  4B 8D 0C 37                     lea rcx, [r15 + r14]
00BE4896  44 8B 97 34 08 00 00            mov r10d, dword ptr [rdi + 0x834]
00BE489D  48 8B 9F 38 08 00 00            mov rbx, qword ptr [rdi + 0x838]
00BE48A4  4C 3B F9                        cmp r15, rcx
00BE48A7  73 0F                           jae 0x140be48b8
00BE48A9  49 8B C7                        mov rax, r15
00BE48AC  0F 18 00                        prefetchnta byte ptr [rax]
00BE48AF  48 83 C0 40                     add rax, 0x40
00BE48B3  48 3B C1                        cmp rax, rcx
00BE48B6  72 F4                           jb 0x140be48ac
00BE48B8  45 8B DE                        mov r11d, r14d
00BE48BB  4C 8B C3                        mov r8, rbx
00BE48BE  41 C1 EB 07                     shr r11d, 7
00BE48C2  45 85 DB                        test r11d, r11d
00BE48C5  74 67                           je 0x140be492e
00BE48C7  41 BE 01 00 00 00               mov r14d, 1
00BE48CD  49 BC 01 20 00 04 80 00 10 70   movabs r12, 0x7010008004002001
00BE48D7  49 8B C5                        mov rax, r13
00BE48DA  4D 33 01                        xor r8, qword ptr [r9]
00BE48DD  41 8B CA                        mov ecx, r10d
00BE48E0  4D 03 CD                        add r9, r13
00BE48E3  49 D3 C0                        rol r8, cl
00BE48E6  4D 33 01                        xor r8, qword ptr [r9]
00BE48E9  4D 03 CD                        add r9, r13
00BE48EC  49 D3 C0                        rol r8, cl
00BE48EF  49 2B C6                        sub rax, r14
00BE48F2  75 E6                           jne 0x140be48da
00BE48F4  49 8B C9                        mov rcx, r9
00BE48F7  49 2B CF                        sub rcx, r15
00BE48FA  48 33 CB                        xor rcx, rbx
00BE48FD  48 8B C1                        mov rax, rcx
00BE4900  48 C1 C0 11                     rol rax, 0x11
00BE4904  48 33 C8                        xor rcx, rax
00BE4907  49 8B C4                        mov rax, r12
00BE490A  48 F7 E1                        mul rcx
00BE490D  44 33 D0                        xor r10d, eax
00BE4910  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
00BE4914  44 33 D2                        xor r10d, edx
00BE4917  41 83 E2 3F                     and r10d, 0x3f
00BE491B  45 0F 44 D6                     cmove r10d, r14d
00BE491F  41 83 C3 FF                     add r11d, -1
00BE4923  75 B2                           jne 0x140be48d7
00BE4925  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
00BE4929  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
00BE492E  41 8B D6                        mov edx, r14d
00BE4931  BB 01 00 00 00                  mov ebx, 1
00BE4936  83 E2 7F                        and edx, 0x7f
00BE4939  41 3B D5                        cmp edx, r13d
00BE493C  72 1A                           jb 0x140be4958
00BE493E  8B C2                           mov eax, edx
00BE4940  48 C1 E8 03                     shr rax, 3
00BE4944  4D 33 01                        xor r8, qword ptr [r9]
00BE4947  41 8B CA                        mov ecx, r10d
00BE494A  49 D3 C0                        rol r8, cl
00BE494D  4D 03 CD                        add r9, r13
00BE4950  83 C2 F8                        add edx, -8
00BE4953  48 2B C3                        sub rax, rbx
00BE4956  75 EC                           jne 0x140be4944
00BE4958  85 D2                           test edx, edx
00BE495A  74 15                           je 0x140be4971
00BE495C  41 0F B6 01                     movzx eax, byte ptr [r9]
00BE4960  41 8B CA                        mov ecx, r10d
00BE4963  4C 33 C0                        xor r8, rax
00BE4966  4C 03 CB                        add r9, rbx
00BE4969  49 D3 C0                        rol r8, cl
00BE496C  83 C2 FF                        add edx, -1
00BE496F  75 EB                           jne 0x140be495c
00BE4971  49 8B C0                        mov rax, r8
00BE4974  EB 03                           jmp 0x140be4979
00BE4976  44 33 C0                        xor r8d, eax
00BE4979  48 C1 E8 1F                     shr rax, 0x1f
00BE497D  48 85 C0                        test rax, rax
00BE4980  75 F4                           jne 0x140be4976
00BE4982  41 0F BA F0 1F                  btr r8d, 0x1f
00BE4987  44 89 46 14                     mov dword ptr [rsi + 0x14], r8d
00BE498B  44 01 B7 48 08 00 00            add dword ptr [rdi + 0x848], r14d
00BE4992  EB 12                           jmp 0x140be49a6
00BE4994  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
00BE4999  48 8B FB                        mov rdi, rbx
00BE499C  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
00BE49A0  C7 06 0D 00 00 00               mov dword ptr [rsi], 0xd
00BE49A6  F7 87 D8 09 00 00 00 00 00 20   test dword ptr [rdi + 0x9d8], 0x20000000
00BE49B0  74 17                           je 0x140be49c9
00BE49B2  45 85 F6                        test r14d, r14d
00BE49B5  74 12                           je 0x140be49c9
00BE49B7  4C 8D 4E 1C                     lea r9, [rsi + 0x1c]
00BE49BB  45 8B C6                        mov r8d, r14d
00BE49BE  49 8B D7                        mov rdx, r15
00BE49C1  48 8B CF                        mov rcx, rdi
00BE49C4  E8 83 65 93 FF                  call 0x14051af4c
00BE49C9  45 33 F6                        xor r14d, r14d
00BE49CC  44 89 76 18                     mov dword ptr [rsi + 0x18], r14d
00BE49D0  44 39 75 80                     cmp dword ptr [rbp - 0x80], r14d
00BE49D4  74 07                           je 0x140be49dd
00BE49D6  C7 46 18 01 00 00 00            mov dword ptr [rsi + 0x18], 1
00BE49DD  48 85 FF                        test rdi, rdi
00BE49E0  74 44                           je 0x140be4a26
00BE49E2  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00BE49E7  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00BE49EC  41 81 BC 24 A0 00 00 00 94 00 00 00  cmp dword ptr [r12 + 0xa0], 0x94
00BE49F8  41 C7 84 24 90 00 00 00 23 00 00 00  mov dword ptr [r12 + 0x90], 0x23
00BE4A04  0F 82 99 00 00 00               jb 0x140be4aa3
00BE4A0A  48 8B 87 08 02 00 00            mov rax, qword ptr [rdi + 0x208]
00BE4A11  49 8B CF                        mov rcx, r15
00BE4A14  49 8B 9C 24 98 00 00 00         mov rbx, qword ptr [r12 + 0x98]
00BE4A1C  E8 3F 60 00 00                  call 0x140beaa60
00BE4A21  48 85 C0                        test rax, rax
00BE4A24  75 19                           jne 0x140be4a3f
00BE4A26  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00BE4A2B  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
00BE4A32  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00BE4A37  48 89 06                        mov qword ptr [rsi], rax
00BE4A3A  E9 B7 09 00 00                  jmp 0x140be53f6
00BE4A3F  44 8B 40 50                     mov r8d, dword ptr [rax + 0x50]
00BE4A43  41 8B 94 24 B8 00 00 00         mov edx, dword ptr [r12 + 0xb8]
00BE4A4B  4D 03 C7                        add r8, r15
00BE4A4E  83 CA 02                        or edx, 2
00BE4A51  41 89 94 24 B8 00 00 00         mov dword ptr [r12 + 0xb8], edx
00BE4A59  8B CA                           mov ecx, edx
00BE4A5B  48 8B 43 70                     mov rax, qword ptr [rbx + 0x70]
00BE4A5F  49 3B C7                        cmp rax, r15
00BE4A62  72 1B                           jb 0x140be4a7f
00BE4A64  49 3B C0                        cmp rax, r8
00BE4A67  73 16                           jae 0x140be4a7f
00BE4A69  48 8B 00                        mov rax, qword ptr [rax]
00BE4A6C  83 C9 04                        or ecx, 4
00BE4A6F  49 89 84 24 A8 00 00 00         mov qword ptr [r12 + 0xa8], rax
00BE4A77  41 89 8C 24 B8 00 00 00         mov dword ptr [r12 + 0xb8], ecx
00BE4A7F  48 8B 43 78                     mov rax, qword ptr [rbx + 0x78]
00BE4A83  49 3B C7                        cmp rax, r15
00BE4A86  72 1B                           jb 0x140be4aa3
00BE4A88  49 3B C0                        cmp rax, r8
00BE4A8B  73 16                           jae 0x140be4aa3
00BE4A8D  48 8B 00                        mov rax, qword ptr [rax]
00BE4A90  41 0B CD                        or ecx, r13d
00BE4A93  49 89 84 24 B0 00 00 00         mov qword ptr [r12 + 0xb0], rax
00BE4A9B  41 89 8C 24 B8 00 00 00         mov dword ptr [r12 + 0xb8], ecx
00BE4AA3  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00BE4AA8  F7 87 D8 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9d8], 0x200000
00BE4AB2  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00BE4AB6  0F 84 89 13 00 00               je 0x140be5e45
00BE4ABC  48 8B 87 08 02 00 00            mov rax, qword ptr [rdi + 0x208]
00BE4AC3  49 8B CF                        mov rcx, r15
00BE4AC6  E8 95 5F 00 00                  call 0x140beaa60
00BE4ACB  45 33 E4                        xor r12d, r12d
00BE4ACE  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00BE4AD2  4C 8B F0                        mov r14, rax
00BE4AD5  48 85 C0                        test rax, rax
00BE4AD8  75 0A                           jne 0x140be4ae4
00BE4ADA  B9 7B 00 00 C0                  mov ecx, 0xc000007b
00BE4ADF  E9 EF 08 00 00                  jmp 0x140be53d3
00BE4AE4  45 0F B7 56 06                  movzx r10d, word ptr [r14 + 6]
00BE4AE9  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00BE4AF3  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
00BE4AF7  48 F7 E1                        mul rcx
00BE4AFA  66 44 89 95 F8 00 00 00         mov word ptr [rbp + 0xf8], r10w
00BE4B02  4C 8B CA                        mov r9, rdx
00BE4B05  49 C1 E9 03                     shr r9, 3
00BE4B09  4C 89 4D A0                     mov qword ptr [rbp - 0x60], r9
00BE4B0D  66 45 85 D2                     test r10w, r10w
00BE4B11  0F 85 1F 01 00 00               jne 0x140be4c36
00BE4B17  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE4B1D  0F BA E1 14                     bt ecx, 0x14
00BE4B21  0F 83 5E 14 00 00               jae 0x140be5f85
00BE4B27  44 39 A7 18 09 00 00            cmp dword ptr [rdi + 0x918], r12d
00BE4B2E  75 AA                           jne 0x140be4ada
00BE4B30  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE4B3A  4C 89 A7 28 09 00 00            mov qword ptr [rdi + 0x928], r12
00BE4B41  48 03 C7                        add rax, rdi
00BE4B44  48 C7 87 30 09 00 00 0F 01 00 00  mov qword ptr [rdi + 0x930], 0x10f
00BE4B4F  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE4B56  BA 01 00 00 00                  mov edx, 1
00BE4B5B  4C 89 BF 38 09 00 00            mov qword ptr [rdi + 0x938], r15
00BE4B62  89 97 18 09 00 00               mov dword ptr [rdi + 0x918], edx
00BE4B68  0F BA E1 1D                     bt ecx, 0x1d
00BE4B6C  0F 82 68 FF FF FF               jb 0x140be4ada
00BE4B72  F7 87 DC 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9dc], 0x200000
00BE4B7C  0F 84 58 FF FF FF               je 0x140be4ada
00BE4B82  84 CA                           test dl, cl
00BE4B84  0F 84 50 FF FF FF               je 0x140be4ada
00BE4B8A  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE4B90  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE4B96  4C 8B 97 38 08 00 00            mov r10, qword ptr [rdi + 0x838]
00BE4B9D  2B C1                           sub eax, ecx
00BE4B9F  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE4BA6  48 8D 14 39                     lea rdx, [rcx + rdi]
00BE4BAA  8B C8                           mov ecx, eax
00BE4BAC  48 C1 E9 03                     shr rcx, 3
00BE4BB0  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BE4BB4  EB 20                           jmp 0x140be4bd6
00BE4BB6  4C 31 02                        xor qword ptr [rdx], r8
00BE4BB9  48 8B 02                        mov rax, qword ptr [rdx]
00BE4BBC  41 0F B6 C8                     movzx ecx, r8b
00BE4BC0  49 33 C2                        xor rax, r10
00BE4BC3  83 E1 3F                        and ecx, 0x3f
00BE4BC6  49 D3 C8                        ror r8, cl
00BE4BC9  4C 03 C0                        add r8, rax
00BE4BCC  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE4BD3  49 03 D5                        add rdx, r13
00BE4BD6  49 3B D1                        cmp rdx, r9
00BE4BD9  75 DB                           jne 0x140be4bb6
00BE4BDB  0F BA B7 DC 09 00 00 15         btr dword ptr [rdi + 0x9dc], 0x15
00BE4BE3  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE4BEA  0F 84 EA FE FF FF               je 0x140be4ada
00BE4BF0  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE4BF6  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE4BFD  48 89 38                        mov qword ptr [rax], rdi
00BE4C00  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE4C03  48 8B 8F 80 0A 00 00            mov rcx, qword ptr [rdi + 0xa80]
00BE4C0A  44 39 A7 18 09 00 00            cmp dword ptr [rdi + 0x918], r12d
00BE4C11  75 0E                           jne 0x140be4c21
00BE4C13  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE4C1A  49 33 C8                        xor rcx, r8
00BE4C1D  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE4C21  48 8B CF                        mov rcx, rdi
00BE4C24  41 B9 00 01 00 00               mov r9d, 0x100
00BE4C2A  33 D2                           xor edx, edx
00BE4C2C  E8 53 37 00 00                  call 0x140be8384
00BE4C31  E9 A4 FE FF FF                  jmp 0x140be4ada
00BE4C36  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00BE4C3B  48 8B DF                        mov rbx, rdi
00BE4C3E  45 0F B7 5E 14                  movzx r11d, word ptr [r14 + 0x14]
00BE4C43  4C 8B E2                        mov r12, rdx
00BE4C46  41 8B C1                        mov eax, r9d
00BE4C49  49 83 C3 18                     add r11, 0x18
00BE4C4D  4D 03 DE                        add r11, r14
00BE4C50  48 BE E8 B4 C8 91 58 3F A0 A3   movabs rsi, 0xa3a03f5891c8b4e8
00BE4C5A  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
00BE4C5E  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BE4C62  48 8D 04 8A                     lea rax, [rdx + rcx*4]
00BE4C66  33 D2                           xor edx, edx
00BE4C68  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00BE4C6D  8B CA                           mov ecx, edx
00BE4C6F  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00BE4C73  66 45 85 D2                     test r10w, r10w
00BE4C77  0F 84 E4 05 00 00               je 0x140be5261
00BE4C7D  49 8D 53 08                     lea rdx, [r11 + 8]
00BE4C81  4C 8B C8                        mov r9, rax
00BE4C84  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
00BE4C88  45 33 F6                        xor r14d, r14d
00BE4C8B  44 8B 6A 08                     mov r13d, dword ptr [rdx + 8]
00BE4C8F  8B 02                           mov eax, dword ptr [rdx]
00BE4C91  44 3B E8                        cmp r13d, eax
00BE4C94  44 8B 42 04                     mov r8d, dword ptr [rdx + 4]
00BE4C98  44 0F 46 E8                     cmovbe r13d, eax
00BE4C9C  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00BE4CA1  45 03 E8                        add r13d, r8d
00BE4CA4  85 C9                           test ecx, ecx
00BE4CA6  74 16                           je 0x140be4cbe
00BE4CA8  8D 41 FF                        lea eax, [rcx - 1]
00BE4CAB  48 8D 04 80                     lea rax, [rax + rax*4]
00BE4CAF  45 3B 6C C3 0C                  cmp r13d, dword ptr [r11 + rax*8 + 0xc]
00BE4CB4  0F 82 81 03 00 00               jb 0x140be503b
00BE4CBA  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00BE4CBE  4D 3B E1                        cmp r12, r9
00BE4CC1  0F 84 40 03 00 00               je 0x140be5007
00BE4CC7  41 8B 0C 24                     mov ecx, dword ptr [r12]
00BE4CCB  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00BE4CD0  41 3B CD                        cmp ecx, r13d
00BE4CD3  0F 83 19 03 00 00               jae 0x140be4ff2
00BE4CD9  41 3B C0                        cmp eax, r8d
00BE4CDC  0F 86 10 03 00 00               jbe 0x140be4ff2
00BE4CE2  41 3B C8                        cmp ecx, r8d
00BE4CE5  0F 82 64 04 00 00               jb 0x140be514f
00BE4CEB  41 3B C5                        cmp eax, r13d
00BE4CEE  0F 87 5B 04 00 00               ja 0x140be514f
00BE4CF4  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00BE4CF9  B9 01 00 00 00                  mov ecx, 1
00BE4CFE  84 C1                           test cl, al
00BE4D00  75 0B                           jne 0x140be4d0d
00BE4D02  42 F6 04 38 20                  test byte ptr [rax + r15], 0x20
00BE4D07  0F 84 D6 02 00 00               je 0x140be4fe3
00BE4D0D  8B 02                           mov eax, dword ptr [rdx]
00BE4D0F  49 8B CC                        mov rcx, r12
00BE4D12  8B 72 08                        mov esi, dword ptr [rdx + 8]
00BE4D15  3B F0                           cmp esi, eax
00BE4D17  44 8B 7A 04                     mov r15d, dword ptr [rdx + 4]
00BE4D1B  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00BE4D20  0F 46 F0                        cmovbe esi, eax
00BE4D23  48 8B 87 18 04 00 00            mov rax, qword ptr [rdi + 0x418]
00BE4D2A  41 03 F7                        add esi, r15d
00BE4D2D  E8 2E 5D 00 00                  call 0x140beaa60
00BE4D32  4C 8B F0                        mov r14, rax
00BE4D35  44 39 38                        cmp dword ptr [rax], r15d
00BE4D38  72 09                           jb 0x140be4d43
00BE4D3A  39 70 04                        cmp dword ptr [rax + 4], esi
00BE4D3D  0F 86 2C 01 00 00               jbe 0x140be4e6f
00BE4D43  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00BE4D48  B9 00 00 00 80                  mov ecx, 0x80000000
00BE4D4D  41 2B C0                        sub eax, r8d
00BE4D50  0B C1                           or eax, ecx
00BE4D52  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE4D58  0F BA E1 14                     bt ecx, 0x14
00BE4D5C  0F 83 9F 12 00 00               jae 0x140be6001
00BE4D62  45 33 DB                        xor r11d, r11d
00BE4D65  44 39 9F 18 09 00 00            cmp dword ptr [rdi + 0x918], r11d
00BE4D6C  0F 85 FD 00 00 00               jne 0x140be4e6f
00BE4D72  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE4D7C  4C 89 9F 28 09 00 00            mov qword ptr [rdi + 0x928], r11
00BE4D83  48 03 C3                        add rax, rbx
00BE4D86  48 C7 87 30 09 00 00 0F 01 00 00  mov qword ptr [rdi + 0x930], 0x10f
00BE4D91  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE4D98  41 8D 53 01                     lea edx, [r11 + 1]
00BE4D9C  4C 89 87 38 09 00 00            mov qword ptr [rdi + 0x938], r8
00BE4DA3  89 97 18 09 00 00               mov dword ptr [rdi + 0x918], edx
00BE4DA9  0F BA E1 1D                     bt ecx, 0x1d
00BE4DAD  0F 82 BC 00 00 00               jb 0x140be4e6f
00BE4DB3  F7 87 DC 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9dc], 0x200000
00BE4DBD  0F 84 AC 00 00 00               je 0x140be4e6f
00BE4DC3  84 CA                           test dl, cl
00BE4DC5  0F 84 A4 00 00 00               je 0x140be4e6f
00BE4DCB  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE4DD1  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE4DD7  4C 8B 97 38 08 00 00            mov r10, qword ptr [rdi + 0x838]
00BE4DDE  2B C1                           sub eax, ecx
00BE4DE0  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE4DE7  48 8D 14 39                     lea rdx, [rcx + rdi]
00BE4DEB  8B C8                           mov ecx, eax
00BE4DED  48 C1 E9 03                     shr rcx, 3
00BE4DF1  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BE4DF5  EB 21                           jmp 0x140be4e18
00BE4DF7  4C 31 02                        xor qword ptr [rdx], r8
00BE4DFA  48 8B 02                        mov rax, qword ptr [rdx]
00BE4DFD  41 0F B6 C8                     movzx ecx, r8b
00BE4E01  49 33 C2                        xor rax, r10
00BE4E04  83 E1 3F                        and ecx, 0x3f
00BE4E07  49 D3 C8                        ror r8, cl
00BE4E0A  4C 03 C0                        add r8, rax
00BE4E0D  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE4E14  48 83 C2 08                     add rdx, 8
00BE4E18  49 3B D1                        cmp rdx, r9
00BE4E1B  75 DA                           jne 0x140be4df7
00BE4E1D  0F BA B7 DC 09 00 00 15         btr dword ptr [rdi + 0x9dc], 0x15
00BE4E25  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE4E2C  74 41                           je 0x140be4e6f
00BE4E2E  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE4E34  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE4E3B  48 89 18                        mov qword ptr [rax], rbx
00BE4E3E  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE4E41  48 8B 8F 80 0A 00 00            mov rcx, qword ptr [rdi + 0xa80]
00BE4E48  44 39 9F 18 09 00 00            cmp dword ptr [rdi + 0x918], r11d
00BE4E4F  75 0E                           jne 0x140be4e5f
00BE4E51  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE4E58  49 33 C8                        xor rcx, r8
00BE4E5B  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE4E5F  33 D2                           xor edx, edx
00BE4E61  41 B9 00 01 00 00               mov r9d, 0x100
00BE4E67  48 8B CB                        mov rcx, rbx
00BE4E6A  E8 15 35 00 00                  call 0x140be8384
00BE4E6F  45 8B 06                        mov r8d, dword ptr [r14]
00BE4E72  49 8B CE                        mov rcx, r14
00BE4E75  4C 03 44 24 58                  add r8, qword ptr [rsp + 0x58]
00BE4E7A  48 8B 87 20 04 00 00            mov rax, qword ptr [rdi + 0x420]
00BE4E81  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00BE4E86  E8 D5 5B 00 00                  call 0x140beaa60
00BE4E8B  44 39 38                        cmp dword ptr [rax], r15d
00BE4E8E  72 09                           jb 0x140be4e99
00BE4E90  39 70 04                        cmp dword ptr [rax + 4], esi
00BE4E93  0F 86 2F 01 00 00               jbe 0x140be4fc8
00BE4E99  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00BE4E9E  B9 00 00 00 80                  mov ecx, 0x80000000
00BE4EA3  41 2B C7                        sub eax, r15d
00BE4EA6  0B C1                           or eax, ecx
00BE4EA8  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE4EAE  0F BA E1 14                     bt ecx, 0x14
00BE4EB2  0F 83 20 11 00 00               jae 0x140be5fd8
00BE4EB8  45 33 F6                        xor r14d, r14d
00BE4EBB  48 BE E8 B4 C8 91 58 3F A0 A3   movabs rsi, 0xa3a03f5891c8b4e8
00BE4EC5  44 39 B7 18 09 00 00            cmp dword ptr [rdi + 0x918], r14d
00BE4ECC  0F 85 08 01 00 00               jne 0x140be4fda
00BE4ED2  4C 89 B7 28 09 00 00            mov qword ptr [rdi + 0x928], r14
00BE4ED9  48 8D 04 37                     lea rax, [rdi + rsi]
00BE4EDD  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE4EE4  41 8D 56 01                     lea edx, [r14 + 1]
00BE4EE8  89 97 18 09 00 00               mov dword ptr [rdi + 0x918], edx
00BE4EEE  48 C7 87 30 09 00 00 0F 01 00 00  mov qword ptr [rdi + 0x930], 0x10f
00BE4EF9  4C 89 BF 38 09 00 00            mov qword ptr [rdi + 0x938], r15
00BE4F00  0F BA E1 1D                     bt ecx, 0x1d
00BE4F04  0F 82 D0 00 00 00               jb 0x140be4fda
00BE4F0A  F7 87 DC 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9dc], 0x200000
00BE4F14  0F 84 C0 00 00 00               je 0x140be4fda
00BE4F1A  84 CA                           test dl, cl
00BE4F1C  0F 84 B8 00 00 00               je 0x140be4fda
00BE4F22  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE4F28  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE4F2E  4C 8B 97 38 08 00 00            mov r10, qword ptr [rdi + 0x838]
00BE4F35  2B C1                           sub eax, ecx
00BE4F37  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE4F3E  48 8D 14 39                     lea rdx, [rcx + rdi]
00BE4F42  8B C8                           mov ecx, eax
00BE4F44  48 C1 E9 03                     shr rcx, 3
00BE4F48  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BE4F4C  EB 21                           jmp 0x140be4f6f
00BE4F4E  4C 31 02                        xor qword ptr [rdx], r8
00BE4F51  48 8B 02                        mov rax, qword ptr [rdx]
00BE4F54  41 0F B6 C8                     movzx ecx, r8b
00BE4F58  49 33 C2                        xor rax, r10
00BE4F5B  83 E1 3F                        and ecx, 0x3f
00BE4F5E  49 D3 C8                        ror r8, cl
00BE4F61  4C 03 C0                        add r8, rax
00BE4F64  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE4F6B  48 83 C2 08                     add rdx, 8
00BE4F6F  49 3B D1                        cmp rdx, r9
00BE4F72  75 DA                           jne 0x140be4f4e
00BE4F74  0F BA B7 DC 09 00 00 15         btr dword ptr [rdi + 0x9dc], 0x15
00BE4F7C  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE4F83  74 55                           je 0x140be4fda
00BE4F85  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE4F8B  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE4F92  48 89 18                        mov qword ptr [rax], rbx
00BE4F95  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE4F98  48 8B 8F 80 0A 00 00            mov rcx, qword ptr [rdi + 0xa80]
00BE4F9F  44 39 B7 18 09 00 00            cmp dword ptr [rdi + 0x918], r14d
00BE4FA6  75 0E                           jne 0x140be4fb6
00BE4FA8  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE4FAF  49 33 C8                        xor rcx, r8
00BE4FB2  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE4FB6  33 D2                           xor edx, edx
00BE4FB8  41 B9 00 01 00 00               mov r9d, 0x100
00BE4FBE  48 8B CB                        mov rcx, rbx
00BE4FC1  E8 BE 33 00 00                  call 0x140be8384
00BE4FC6  EB 12                           jmp 0x140be4fda
00BE4FC8  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00BE4FCD  48 BE E8 B4 C8 91 58 3F A0 A3   movabs rsi, 0xa3a03f5891c8b4e8
00BE4FD7  45 33 F6                        xor r14d, r14d
00BE4FDA  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00BE4FDE  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
00BE4FE3  49 83 C4 0C                     add r12, 0xc
00BE4FE7  4C 3B 64 24 68                  cmp r12, qword ptr [rsp + 0x68]
00BE4FEC  0F 85 D5 FC FF FF               jne 0x140be4cc7
00BE4FF2  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00BE4FF6  44 0F B7 95 F8 00 00 00         movzx r10d, word ptr [rbp + 0xf8]
00BE4FFE  4C 8B 5D 88                     mov r11, qword ptr [rbp - 0x78]
00BE5002  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00BE5007  48 83 C2 28                     add rdx, 0x28
00BE500B  41 0F B7 C2                     movzx eax, r10w
00BE500F  41 B8 01 00 00 00               mov r8d, 1
00BE5015  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
00BE5019  41 03 C8                        add ecx, r8d
00BE501C  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00BE5020  3B C8                           cmp ecx, eax
00BE5022  0F 82 63 FC FF FF               jb 0x140be4c8b
00BE5028  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
00BE502C  45 8D 68 07                     lea r13d, [r8 + 7]
00BE5030  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
00BE5034  33 D2                           xor edx, edx
00BE5036  E9 2C 02 00 00                  jmp 0x140be5267
00BE503B  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE5041  0F BA E1 14                     bt ecx, 0x14
00BE5045  0F 83 62 0F 00 00               jae 0x140be5fad
00BE504B  45 33 E4                        xor r12d, r12d
00BE504E  44 39 A7 18 09 00 00            cmp dword ptr [rdi + 0x918], r12d
00BE5055  0F 85 7F FA FF FF               jne 0x140be4ada
00BE505B  4C 89 A7 28 09 00 00            mov qword ptr [rdi + 0x928], r12
00BE5062  48 8D 04 37                     lea rax, [rdi + rsi]
00BE5066  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE506D  41 8D 54 24 01                  lea edx, [r12 + 1]
00BE5072  89 97 18 09 00 00               mov dword ptr [rdi + 0x918], edx
00BE5078  48 C7 87 30 09 00 00 0F 01 00 00  mov qword ptr [rdi + 0x930], 0x10f
00BE5083  4C 89 BF 38 09 00 00            mov qword ptr [rdi + 0x938], r15
00BE508A  0F BA E1 1D                     bt ecx, 0x1d
00BE508E  0F 82 46 FA FF FF               jb 0x140be4ada
00BE5094  F7 87 DC 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9dc], 0x200000
00BE509E  0F 84 36 FA FF FF               je 0x140be4ada
00BE50A4  84 CA                           test dl, cl
00BE50A6  0F 84 2E FA FF FF               je 0x140be4ada
00BE50AC  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE50B2  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE50B8  4C 8B 9F 38 08 00 00            mov r11, qword ptr [rdi + 0x838]
00BE50BF  2B C1                           sub eax, ecx
00BE50C1  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE50C8  4C 8D 0C 39                     lea r9, [rcx + rdi]
00BE50CC  8B C8                           mov ecx, eax
00BE50CE  48 C1 E9 03                     shr rcx, 3
00BE50D2  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
00BE50D6  EB 21                           jmp 0x140be50f9
00BE50D8  4D 31 01                        xor qword ptr [r9], r8
00BE50DB  49 8B C3                        mov rax, r11
00BE50DE  49 33 01                        xor rax, qword ptr [r9]
00BE50E1  41 0F B6 C8                     movzx ecx, r8b
00BE50E5  83 E1 3F                        and ecx, 0x3f
00BE50E8  49 D3 C8                        ror r8, cl
00BE50EB  4C 03 C0                        add r8, rax
00BE50EE  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE50F5  49 83 C1 08                     add r9, 8
00BE50F9  4D 3B CA                        cmp r9, r10
00BE50FC  75 DA                           jne 0x140be50d8
00BE50FE  0F BA B7 DC 09 00 00 15         btr dword ptr [rdi + 0x9dc], 0x15
00BE5106  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE510D  0F 84 C7 F9 FF FF               je 0x140be4ada
00BE5113  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE511A  8B 97 04 08 00 00               mov edx, dword ptr [rdi + 0x804]
00BE5120  48 89 18                        mov qword ptr [rax], rbx
00BE5123  89 50 10                        mov dword ptr [rax + 0x10], edx
00BE5126  48 8B 87 80 0A 00 00            mov rax, qword ptr [rdi + 0xa80]
00BE512D  44 39 A7 18 09 00 00            cmp dword ptr [rdi + 0x918], r12d
00BE5134  75 11                           jne 0x140be5147
00BE5136  49 8B D0                        mov rdx, r8
00BE5139  48 33 D0                        xor rdx, rax
00BE513C  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE5143  48 89 50 18                     mov qword ptr [rax + 0x18], rdx
00BE5147  48 8B CB                        mov rcx, rbx
00BE514A  E9 D5 FA FF FF                  jmp 0x140be4c24
00BE514F  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE5155  0F BA E1 14                     bt ecx, 0x14
00BE5159  0F 83 C8 0E 00 00               jae 0x140be6027
00BE515F  45 33 E4                        xor r12d, r12d
00BE5162  44 39 A7 18 09 00 00            cmp dword ptr [rdi + 0x918], r12d
00BE5169  0F 85 6B F9 FF FF               jne 0x140be4ada
00BE516F  4C 89 A7 28 09 00 00            mov qword ptr [rdi + 0x928], r12
00BE5176  48 8D 04 37                     lea rax, [rdi + rsi]
00BE517A  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE5181  41 8D 54 24 01                  lea edx, [r12 + 1]
00BE5186  89 97 18 09 00 00               mov dword ptr [rdi + 0x918], edx
00BE518C  48 C7 87 30 09 00 00 0F 01 00 00  mov qword ptr [rdi + 0x930], 0x10f
00BE5197  4C 89 BF 38 09 00 00            mov qword ptr [rdi + 0x938], r15
00BE519E  0F BA E1 1D                     bt ecx, 0x1d
00BE51A2  0F 82 32 F9 FF FF               jb 0x140be4ada
00BE51A8  F7 87 DC 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9dc], 0x200000
00BE51B2  0F 84 22 F9 FF FF               je 0x140be4ada
00BE51B8  84 CA                           test dl, cl
00BE51BA  0F 84 1A F9 FF FF               je 0x140be4ada
00BE51C0  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE51C6  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE51CC  4C 8B 9F 38 08 00 00            mov r11, qword ptr [rdi + 0x838]
00BE51D3  2B C1                           sub eax, ecx
00BE51D5  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE51DC  4C 8D 0C 39                     lea r9, [rcx + rdi]
00BE51E0  8B C8                           mov ecx, eax
00BE51E2  48 C1 E9 03                     shr rcx, 3
00BE51E6  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
00BE51EA  EB 21                           jmp 0x140be520d
00BE51EC  4D 31 01                        xor qword ptr [r9], r8
00BE51EF  49 8B C3                        mov rax, r11
00BE51F2  49 33 01                        xor rax, qword ptr [r9]
00BE51F5  41 0F B6 C8                     movzx ecx, r8b
00BE51F9  83 E1 3F                        and ecx, 0x3f
00BE51FC  49 D3 C8                        ror r8, cl
00BE51FF  4C 03 C0                        add r8, rax
00BE5202  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE5209  49 83 C1 08                     add r9, 8
00BE520D  4D 3B CA                        cmp r9, r10
00BE5210  75 DA                           jne 0x140be51ec
00BE5212  0F BA B7 DC 09 00 00 15         btr dword ptr [rdi + 0x9dc], 0x15
00BE521A  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE5221  0F 84 B3 F8 FF FF               je 0x140be4ada
00BE5227  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE522D  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE5234  48 89 18                        mov qword ptr [rax], rbx
00BE5237  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE523A  48 8B 8F 80 0A 00 00            mov rcx, qword ptr [rdi + 0xa80]
00BE5241  44 39 A7 18 09 00 00            cmp dword ptr [rdi + 0x918], r12d
00BE5248  0F 85 F9 FE FF FF               jne 0x140be5147
00BE524E  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE5255  49 33 C8                        xor rcx, r8
00BE5258  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE525C  E9 E6 FE FF FF                  jmp 0x140be5147
00BE5261  41 B8 01 00 00 00               mov r8d, 1
00BE5267  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
00BE526C  4D 3B E3                        cmp r12, r11
00BE526F  0F 84 07 01 00 00               je 0x140be537c
00BE5275  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE527B  0F BA E1 14                     bt ecx, 0x14
00BE527F  0F 83 CD 0D 00 00               jae 0x140be6052
00BE5285  45 33 E4                        xor r12d, r12d
00BE5288  44 39 A3 18 09 00 00            cmp dword ptr [rbx + 0x918], r12d
00BE528F  0F 85 45 F8 FF FF               jne 0x140be4ada
00BE5295  4C 89 A3 28 09 00 00            mov qword ptr [rbx + 0x928], r12
00BE529C  48 8D 04 33                     lea rax, [rbx + rsi]
00BE52A0  48 89 83 20 09 00 00            mov qword ptr [rbx + 0x920], rax
00BE52A7  48 C7 83 30 09 00 00 0F 01 00 00  mov qword ptr [rbx + 0x930], 0x10f
00BE52B2  4C 89 BB 38 09 00 00            mov qword ptr [rbx + 0x938], r15
00BE52B9  44 89 83 18 09 00 00            mov dword ptr [rbx + 0x918], r8d
00BE52C0  0F BA E1 1D                     bt ecx, 0x1d
00BE52C4  0F 82 10 F8 FF FF               jb 0x140be4ada
00BE52CA  F7 83 DC 09 00 00 00 00 20 00   test dword ptr [rbx + 0x9dc], 0x200000
00BE52D4  0F 84 00 F8 FF FF               je 0x140be4ada
00BE52DA  41 84 C8                        test r8b, cl
00BE52DD  0F 84 F7 F7 FF FF               je 0x140be4ada
00BE52E3  8B 8B 74 0A 00 00               mov ecx, dword ptr [rbx + 0xa74]
00BE52E9  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE52EF  4C 8B 9B 38 08 00 00            mov r11, qword ptr [rbx + 0x838]
00BE52F6  2B C1                           sub eax, ecx
00BE52F8  4C 8B 83 78 0A 00 00            mov r8, qword ptr [rbx + 0xa78]
00BE52FF  4C 8D 0C 19                     lea r9, [rcx + rbx]
00BE5303  8B C8                           mov ecx, eax
00BE5305  48 C1 E9 03                     shr rcx, 3
00BE5309  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
00BE530D  EB 20                           jmp 0x140be532f
00BE530F  4D 31 01                        xor qword ptr [r9], r8
00BE5312  49 8B C3                        mov rax, r11
00BE5315  49 33 01                        xor rax, qword ptr [r9]
00BE5318  41 0F B6 C8                     movzx ecx, r8b
00BE531C  83 E1 3F                        and ecx, 0x3f
00BE531F  49 D3 C8                        ror r8, cl
00BE5322  4C 03 C0                        add r8, rax
00BE5325  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE532C  4D 03 CD                        add r9, r13
00BE532F  4D 3B CA                        cmp r9, r10
00BE5332  75 DB                           jne 0x140be530f
00BE5334  0F BA B3 DC 09 00 00 15         btr dword ptr [rbx + 0x9dc], 0x15
00BE533C  4C 3B 83 80 0A 00 00            cmp r8, qword ptr [rbx + 0xa80]
00BE5343  0F 84 91 F7 FF FF               je 0x140be4ada
00BE5349  8B 8B 04 08 00 00               mov ecx, dword ptr [rbx + 0x804]
00BE534F  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE5356  48 89 18                        mov qword ptr [rax], rbx
00BE5359  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE535C  48 8B 8B 80 0A 00 00            mov rcx, qword ptr [rbx + 0xa80]
00BE5363  44 39 A3 18 09 00 00            cmp dword ptr [rbx + 0x918], r12d
00BE536A  0F 85 D7 FD FF FF               jne 0x140be5147
00BE5370  48 8B 83 88 05 00 00            mov rax, qword ptr [rbx + 0x588]
00BE5377  E9 D9 FE FF FF                  jmp 0x140be5255
00BE537C  45 33 E4                        xor r12d, r12d
00BE537F  45 85 C9                        test r9d, r9d
00BE5382  74 09                           je 0x140be538d
00BE5384  41 8D 51 06                     lea edx, [r9 + 6]
00BE5388  83 E2 F8                        and edx, 0xfffffff8
00BE538B  EB 03                           jmp 0x140be5390
00BE538D  41 8B D4                        mov edx, r12d
00BE5390  8B B3 04 08 00 00               mov esi, dword ptr [rbx + 0x804]
00BE5396  44 8B 83 44 09 00 00            mov r8d, dword ptr [rbx + 0x944]
00BE539D  41 0F B7 C2                     movzx eax, r10w
00BE53A1  8D 0C 40                        lea ecx, [rax + rax*2]
00BE53A4  8D 04 CA                        lea eax, [rdx + rcx*8]
00BE53A7  8D 4E 30                        lea ecx, [rsi + 0x30]
00BE53AA  03 C8                           add ecx, eax
00BE53AC  3B 8B 64 0A 00 00               cmp ecx, dword ptr [rbx + 0xa64]
00BE53B2  0F 86 0D 01 00 00               jbe 0x140be54c5
00BE53B8  8B D1                           mov edx, ecx
00BE53BA  48 8B CB                        mov rcx, rbx
00BE53BD  E8 36 27 00 00                  call 0x140be7af8
00BE53C2  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00BE53C6  48 8B F8                        mov rdi, rax
00BE53C9  48 85 C0                        test rax, rax
00BE53CC  75 2F                           jne 0x140be53fd
00BE53CE  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00BE53D3  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
00BE53DA  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00BE53DF  48 89 3E                        mov qword ptr [rsi], rdi
00BE53E2  85 C9                           test ecx, ecx
00BE53E4  0F 89 6D 0A 00 00               jns 0x140be5e57
00BE53EA  81 F9 0E 01 00 C0               cmp ecx, 0xc000010e
00BE53F0  0F 84 61 0A 00 00               je 0x140be5e57
00BE53F6  8B C1                           mov eax, ecx
00BE53F8  E9 F3 0A 00 00                  jmp 0x140be5ef0
00BE53FD  8B 8B D8 09 00 00               mov ecx, dword ptr [rbx + 0x9d8]
00BE5403  F6 C1 02                        test cl, 2
00BE5406  0F 85 9F 00 00 00               jne 0x140be54ab
00BE540C  8B 83 04 08 00 00               mov eax, dword ptr [rbx + 0x804]
00BE5412  81 E1 00 00 00 10               and ecx, 0x10000000
00BE5418  4C 8B 83 E8 07 00 00            mov r8, qword ptr [rbx + 0x7e8]
00BE541F  F7 D9                           neg ecx
00BE5421  41 B9 01 00 00 00               mov r9d, 1
00BE5427  1B D2                           sbb edx, edx
00BE5429  23 93 44 09 00 00               and edx, dword ptr [rbx + 0x944]
00BE542F  41 3B C5                        cmp eax, r13d
00BE5432  72 14                           jb 0x140be5448
00BE5434  8B C8                           mov ecx, eax
00BE5436  48 C1 E9 03                     shr rcx, 3
00BE543A  4C 89 23                        mov qword ptr [rbx], r12
00BE543D  83 C0 F8                        add eax, -8
00BE5440  49 03 DD                        add rbx, r13
00BE5443  49 2B C9                        sub rcx, r9
00BE5446  75 F2                           jne 0x140be543a
00BE5448  85 C0                           test eax, eax
00BE544A  74 0B                           je 0x140be5457
00BE544C  44 88 23                        mov byte ptr [rbx], r12b
00BE544F  49 03 D9                        add rbx, r9
00BE5452  83 C0 FF                        add eax, -1
00BE5455  75 F5                           jne 0x140be544c
00BE5457  8B 9F 44 09 00 00               mov ebx, dword ptr [rdi + 0x944]
00BE545D  89 97 44 09 00 00               mov dword ptr [rdi + 0x944], edx
00BE5463  83 FA 03                        cmp edx, 3
00BE5466  74 2E                           je 0x140be5496
00BE5468  F7 87 D8 09 00 00 00 00 00 08   test dword ptr [rdi + 0x9d8], 0x8000000
00BE5472  75 19                           jne 0x140be548d
00BE5474  85 D2                           test edx, edx
00BE5476  74 15                           je 0x140be548d
00BE5478  48 8B 87 38 02 00 00            mov rax, qword ptr [rdi + 0x238]
00BE547F  49 8D 48 F8                     lea rcx, [r8 - 8]
00BE5483  48 8B 11                        mov rdx, qword ptr [rcx]
00BE5486  E8 D5 55 00 00                  call 0x140beaa60
00BE548B  EB 18                           jmp 0x140be54a5
00BE548D  48 8B 87 08 01 00 00            mov rax, qword ptr [rdi + 0x108]
00BE5494  EB 07                           jmp 0x140be549d
00BE5496  48 8B 87 68 03 00 00            mov rax, qword ptr [rdi + 0x368]
00BE549D  49 8B C8                        mov rcx, r8
00BE54A0  E8 BB 55 00 00                  call 0x140beaa60
00BE54A5  89 9F 44 09 00 00               mov dword ptr [rdi + 0x944], ebx
00BE54AB  83 A7 D8 09 00 00 FD            and dword ptr [rdi + 0x9d8], 0xfffffffd
00BE54B2  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
00BE54B6  44 0F B7 95 F8 00 00 00         movzx r10d, word ptr [rbp + 0xf8]
00BE54BE  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
00BE54C3  EB 0D                           jmp 0x140be54d2
00BE54C5  48 8B FB                        mov rdi, rbx
00BE54C8  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
00BE54CC  89 8B 04 08 00 00               mov dword ptr [rbx + 0x804], ecx
00BE54D2  BA 06 00 00 00                  mov edx, 6
00BE54D7  48 8D 0C 37                     lea rcx, [rdi + rsi]
00BE54DB  B8 01 00 00 00                  mov eax, 1
00BE54E0  01 87 2C 08 00 00               add dword ptr [rdi + 0x82c], eax
00BE54E6  48 8B C1                        mov rax, rcx
00BE54E9  8D 72 FB                        lea esi, [rdx - 5]
00BE54EC  44 8D 42 2A                     lea r8d, [rdx + 0x2a]
00BE54F0  4C 89 20                        mov qword ptr [rax], r12
00BE54F3  41 83 C0 F8                     add r8d, -8
00BE54F7  49 03 C5                        add rax, r13
00BE54FA  48 2B D6                        sub rdx, rsi
00BE54FD  75 F1                           jne 0x140be54f0
00BE54FF  45 85 C0                        test r8d, r8d
00BE5502  74 0C                           je 0x140be5510
00BE5504  44 88 20                        mov byte ptr [rax], r12b
00BE5507  48 03 C6                        add rax, rsi
00BE550A  41 83 C0 FF                     add r8d, -1
00BE550E  75 F4                           jne 0x140be5504
00BE5510  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BE5515  48 89 59 08                     mov qword ptr [rcx + 8], rbx
00BE5519  C7 01 1E 00 00 00               mov dword ptr [rcx], 0x1e
00BE551F  44 89 61 10                     mov dword ptr [rcx + 0x10], r12d
00BE5523  48 8B 97 38 08 00 00            mov rdx, qword ptr [rdi + 0x838]
00BE552A  48 8B C2                        mov rax, rdx
00BE552D  EB 02                           jmp 0x140be5531
00BE552F  33 D0                           xor edx, eax
00BE5531  48 C1 E8 1F                     shr rax, 0x1f
00BE5535  48 85 C0                        test rax, rax
00BE5538  75 F5                           jne 0x140be552f
00BE553A  0F BA F2 1F                     btr edx, 0x1f
00BE553E  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00BE5542  89 51 14                        mov dword ptr [rcx + 0x14], edx
00BE5545  4C 89 79 18                     mov qword ptr [rcx + 0x18], r15
00BE5549  41 8B 46 50                     mov eax, dword ptr [r14 + 0x50]
00BE554D  89 41 20                        mov dword ptr [rcx + 0x20], eax
00BE5550  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00BE5554  89 41 24                        mov dword ptr [rcx + 0x24], eax
00BE5557  66 44 89 51 28                  mov word ptr [rcx + 0x28], r10w
00BE555C  48 83 C1 30                     add rcx, 0x30
00BE5560  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00BE5565  45 85 C9                        test r9d, r9d
00BE5568  74 11                           je 0x140be557b
00BE556A  45 8D 71 FF                     lea r14d, [r9 - 1]
00BE556E  49 83 C6 07                     add r14, 7
00BE5572  49 83 E6 F8                     and r14, 0xfffffffffffffff8
00BE5576  4C 03 F1                        add r14, rcx
00BE5579  EB 03                           jmp 0x140be557e
00BE557B  4C 8B F1                        mov r14, rcx
00BE557E  41 0F B7 C2                     movzx eax, r10w
00BE5582  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00BE5587  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BE558B  4D 8D 04 CE                     lea r8, [r14 + rcx*8]
00BE558F  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
00BE5593  45 85 C9                        test r9d, r9d
00BE5596  74 0B                           je 0x140be55a3
00BE5598  48 8D 43 0C                     lea rax, [rbx + 0xc]
00BE559C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00BE55A1  EB 05                           jmp 0x140be55a8
00BE55A3  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
00BE55A8  66 45 3B E2                     cmp r12w, r10w
00BE55AC  73 25                           jae 0x140be55d3
00BE55AE  49 8D 46 08                     lea rax, [r14 + 8]
00BE55B2  41 0F B7 D2                     movzx edx, r10w
00BE55B6  B9 02 00 00 00                  mov ecx, 2
00BE55BB  4C 89 60 F8                     mov qword ptr [rax - 8], r12
00BE55BF  C7 00 00 00 00 80               mov dword ptr [rax], 0x80000000
00BE55C5  48 83 C0 0C                     add rax, 0xc
00BE55C9  48 2B CE                        sub rcx, rsi
00BE55CC  75 ED                           jne 0x140be55bb
00BE55CE  48 2B D6                        sub rdx, rsi
00BE55D1  75 E3                           jne 0x140be55b6
00BE55D3  4D 3B F0                        cmp r14, r8
00BE55D6  0F 84 6C 08 00 00               je 0x140be5e48
00BE55DC  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
00BE55E0  45 33 DB                        xor r11d, r11d
00BE55E3  41 F7 44 24 24 00 00 00 02      test dword ptr [r12 + 0x24], 0x2000000
00BE55EC  45 8B EB                        mov r13d, r11d
00BE55EF  75 42                           jne 0x140be5633
00BE55F1  41 8B 0C 24                     mov ecx, dword ptr [r12]
00BE55F5  49 8D 44 24 04                  lea rax, [r12 + 4]
00BE55FA  81 F9 49 4E 49 54               cmp ecx, 0x54494e49
00BE5600  75 08                           jne 0x140be560a
00BE5602  81 38 4B 44 42 47               cmp dword ptr [rax], 0x4742444b
00BE5608  74 29                           je 0x140be5633
00BE560A  81 F9 50 41 47 45               cmp ecx, 0x45474150
00BE5610  75 29                           jne 0x140be563b
00BE5612  0F B7 08                        movzx ecx, word ptr [rax]
00BE5615  B8 77 78 00 00                  mov eax, 0x7877
00BE561A  66 3B C8                        cmp cx, ax
00BE561D  74 14                           je 0x140be5633
00BE561F  B8 77 72 00 00                  mov eax, 0x7277
00BE5624  66 3B C8                        cmp cx, ax
00BE5627  74 0A                           je 0x140be5633
00BE5629  B8 77 77 00 00                  mov eax, 0x7777
00BE562E  66 3B C8                        cmp cx, ax
00BE5631  75 1A                           jne 0x140be564d
00BE5633  44 8B EE                        mov r13d, esi
00BE5636  E9 E3 00 00 00                  jmp 0x140be571e
00BE563B  81 F9 45 52 52 41               cmp ecx, 0x41525245
00BE5641  75 0A                           jne 0x140be564d
00BE5643  B9 54 41 00 00                  mov ecx, 0x4154
00BE5648  66 39 08                        cmp word ptr [rax], cx
00BE564B  74 E6                           je 0x140be5633
00BE564D  48 8B 97 50 09 00 00            mov rdx, qword ptr [rdi + 0x950]
00BE5654  4D 8B C4                        mov r8, r12
00BE5657  4C 8B 8F 58 09 00 00            mov r9, qword ptr [rdi + 0x958]
00BE565E  4C 2B C2                        sub r8, rdx
00BE5661  4C 8B 97 60 09 00 00            mov r10, qword ptr [rdi + 0x960]
00BE5668  41 BB 07 00 00 00               mov r11d, 7
00BE566E  48 8B 9F 68 09 00 00            mov rbx, qword ptr [rdi + 0x968]
00BE5675  41 8A 0C 10                     mov cl, byte ptr [r8 + rdx]
00BE5679  8A 02                           mov al, byte ptr [rdx]
00BE567B  48 03 D6                        add rdx, rsi
00BE567E  3A C8                           cmp cl, al
00BE5680  75 0B                           jne 0x140be568d
00BE5682  41 83 C3 FF                     add r11d, -1
00BE5686  75 ED                           jne 0x140be5675
00BE5688  E9 86 00 00 00                  jmp 0x140be5713
00BE568D  BA 08 00 00 00                  mov edx, 8
00BE5692  4D 8B C4                        mov r8, r12
00BE5695  49 8B 08                        mov rcx, qword ptr [r8]
00BE5698  49 83 C0 08                     add r8, 8
00BE569C  49 8B 01                        mov rax, qword ptr [r9]
00BE569F  49 83 C1 08                     add r9, 8
00BE56A3  48 3B C8                        cmp rcx, rax
00BE56A6  75 26                           jne 0x140be56ce
00BE56A8  83 C2 F8                        add edx, -8
00BE56AB  83 FA 08                        cmp edx, 8
00BE56AE  73 E5                           jae 0x140be5695
00BE56B0  45 33 DB                        xor r11d, r11d
00BE56B3  85 D2                           test edx, edx
00BE56B5  74 5C                           je 0x140be5713
00BE56B7  41 8A 08                        mov cl, byte ptr [r8]
00BE56BA  4C 03 C6                        add r8, rsi
00BE56BD  41 8A 01                        mov al, byte ptr [r9]
00BE56C0  4C 03 CE                        add r9, rsi
00BE56C3  3A C8                           cmp cl, al
00BE56C5  75 0A                           jne 0x140be56d1
00BE56C7  83 C2 FF                        add edx, -1
00BE56CA  75 EB                           jne 0x140be56b7
00BE56CC  EB 45                           jmp 0x140be5713
00BE56CE  45 33 DB                        xor r11d, r11d
00BE56D1  49 8B D4                        mov rdx, r12
00BE56D4  41 B8 04 00 00 00               mov r8d, 4
00BE56DA  49 2B D2                        sub rdx, r10
00BE56DD  41 83 C9 FF                     or r9d, 0xffffffff
00BE56E1  42 8A 0C 12                     mov cl, byte ptr [rdx + r10]
00BE56E5  41 8A 02                        mov al, byte ptr [r10]
00BE56E8  4C 03 D6                        add r10, rsi
00BE56EB  3A C8                           cmp cl, al
00BE56ED  75 07                           jne 0x140be56f6
00BE56EF  45 03 C1                        add r8d, r9d
00BE56F2  75 ED                           jne 0x140be56e1
00BE56F4  EB 1D                           jmp 0x140be5713
00BE56F6  49 8B D4                        mov rdx, r12
00BE56F9  41 B8 06 00 00 00               mov r8d, 6
00BE56FF  48 2B D3                        sub rdx, rbx
00BE5702  8A 0C 1A                        mov cl, byte ptr [rdx + rbx]
00BE5705  8A 03                           mov al, byte ptr [rbx]
00BE5707  48 03 DE                        add rbx, rsi
00BE570A  3A C8                           cmp cl, al
00BE570C  75 0B                           jne 0x140be5719
00BE570E  45 03 C1                        add r8d, r9d
00BE5711  75 EF                           jne 0x140be5702
00BE5713  44 8B EE                        mov r13d, esi
00BE5716  45 33 DB                        xor r11d, r11d
00BE5719  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BE571E  41 8B 4C 24 24                  mov ecx, dword ptr [r12 + 0x24]
00BE5723  85 C9                           test ecx, ecx
00BE5725  79 05                           jns 0x140be572c
00BE5727  44 8B EE                        mov r13d, esi
00BE572A  EB 05                           jmp 0x140be5731
00BE572C  45 85 ED                        test r13d, r13d
00BE572F  74 23                           je 0x140be5754
00BE5731  41 81 3C 24 49 4E 49 54         cmp dword ptr [r12], 0x54494e49
00BE5739  75 19                           jne 0x140be5754
00BE573B  41 81 7C 24 04 4B 44 42 47      cmp dword ptr [r12 + 4], 0x4742444b
00BE5744  75 0E                           jne 0x140be5754
00BE5746  F7 87 DC 09 00 00 00 20 00 00   test dword ptr [rdi + 0x9dc], 0x2000
00BE5750  45 0F 45 EB                     cmovne r13d, r11d
00BE5754  F7 87 DC 09 00 00 00 40 00 00   test dword ptr [rdi + 0x9dc], 0x4000
00BE575E  74 1B                           je 0x140be577b
00BE5760  0F BA E1 1D                     bt ecx, 0x1d
00BE5764  73 15                           jae 0x140be577b
00BE5766  4C 3B BF E0 05 00 00            cmp r15, qword ptr [rdi + 0x5e0]
00BE576D  74 09                           je 0x140be5778
00BE576F  4C 3B BF E8 05 00 00            cmp r15, qword ptr [rdi + 0x5e8]
00BE5776  75 03                           jne 0x140be577b
00BE5778  44 8B EE                        mov r13d, esi
00BE577B  41 8B 74 24 10                  mov esi, dword ptr [r12 + 0x10]
00BE5780  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00BE5785  3B F0                           cmp esi, eax
00BE5787  41 8B 54 24 0C                  mov edx, dword ptr [r12 + 0xc]
00BE578C  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00BE5791  0F 46 F0                        cmovbe esi, eax
00BE5794  03 F2                           add esi, edx
00BE5796  89 55 80                        mov dword ptr [rbp - 0x80], edx
00BE5799  89 B5 F8 00 00 00               mov dword ptr [rbp + 0xf8], esi
00BE579F  44 8B E2                        mov r12d, edx
00BE57A2  49 3B D8                        cmp rbx, r8
00BE57A5  0F 84 7C 01 00 00               je 0x140be5927
00BE57AB  8B 03                           mov eax, dword ptr [rbx]
00BE57AD  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
00BE57B0  44 8B F9                        mov r15d, ecx
00BE57B3  3B C2                           cmp eax, edx
00BE57B5  0F 86 74 01 00 00               jbe 0x140be592f
00BE57BB  3B CE                           cmp ecx, esi
00BE57BD  0F 87 81 01 00 00               ja 0x140be5944
00BE57C3  45 85 ED                        test r13d, r13d
00BE57C6  0F 85 8A 01 00 00               jne 0x140be5956
00BE57CC  44 8B C8                        mov r9d, eax
00BE57CF  41 89 46 04                     mov dword ptr [r14 + 4], eax
00BE57D3  44 2B CA                        sub r9d, edx
00BE57D6  41 89 16                        mov dword ptr [r14], edx
00BE57D9  44 8B DA                        mov r11d, edx
00BE57DC  41 8B D9                        mov ebx, r9d
00BE57DF  4C 03 5C 24 58                  add r11, qword ptr [rsp + 0x58]
00BE57E4  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00BE57E8  49 03 DB                        add rbx, r11
00BE57EB  4C 8D 45 00                     lea r8, [rbp]
00BE57EF  44 8B E0                        mov r12d, eax
00BE57F2  33 C0                           xor eax, eax
00BE57F4  44 8B D0                        mov r10d, eax
00BE57F7  49 8B 08                        mov rcx, qword ptr [r8]
00BE57FA  8B 02                           mov eax, dword ptr [rdx]
00BE57FC  48 03 C1                        add rax, rcx
00BE57FF  4C 3B D8                        cmp r11, rax
00BE5802  73 09                           jae 0x140be580d
00BE5804  48 3B D9                        cmp rbx, rcx
00BE5807  0F 87 2A 01 00 00               ja 0x140be5937
00BE580D  41 FF C2                        inc r10d
00BE5810  49 83 C0 08                     add r8, 8
00BE5814  48 83 C2 04                     add rdx, 4
00BE5818  41 83 FA 06                     cmp r10d, 6
00BE581C  72 D9                           jb 0x140be57f7
00BE581E  44 01 8F 48 08 00 00            add dword ptr [rdi + 0x848], r9d
00BE5825  4D 8B D3                        mov r10, r11
00BE5828  8B B7 34 08 00 00               mov esi, dword ptr [rdi + 0x834]
00BE582E  49 8B C3                        mov rax, r11
00BE5831  4C 8B B7 38 08 00 00            mov r14, qword ptr [rdi + 0x838]
00BE5838  41 8B C9                        mov ecx, r9d
00BE583B  49 03 CB                        add rcx, r11
00BE583E  4C 3B D9                        cmp r11, rcx
00BE5841  73 0C                           jae 0x140be584f
00BE5843  0F 18 00                        prefetchnta byte ptr [rax]
00BE5846  48 83 C0 40                     add rax, 0x40
00BE584A  48 3B C1                        cmp rax, rcx
00BE584D  72 F4                           jb 0x140be5843
00BE584F  41 8B D9                        mov ebx, r9d
00BE5852  4D 8B C6                        mov r8, r14
00BE5855  C1 EB 07                        shr ebx, 7
00BE5858  BA 01 00 00 00                  mov edx, 1
00BE585D  85 DB                           test ebx, ebx
00BE585F  74 5C                           je 0x140be58bd
00BE5861  48 BF 01 20 00 04 80 00 10 70   movabs rdi, 0x7010008004002001
00BE586B  B8 08 00 00 00                  mov eax, 8
00BE5870  4D 33 02                        xor r8, qword ptr [r10]
00BE5873  8B CE                           mov ecx, esi
00BE5875  49 D3 C0                        rol r8, cl
00BE5878  4D 33 42 08                     xor r8, qword ptr [r10 + 8]
00BE587C  49 83 C2 10                     add r10, 0x10
00BE5880  49 D3 C0                        rol r8, cl
00BE5883  48 2B C2                        sub rax, rdx
00BE5886  75 E8                           jne 0x140be5870
00BE5888  49 8B CA                        mov rcx, r10
00BE588B  49 2B CB                        sub rcx, r11
00BE588E  49 33 CE                        xor rcx, r14
00BE5891  48 8B C1                        mov rax, rcx
00BE5894  48 C1 C0 11                     rol rax, 0x11
00BE5898  48 33 C8                        xor rcx, rax
00BE589B  48 8B C7                        mov rax, rdi
00BE589E  48 F7 E1                        mul rcx
00BE58A1  33 C2                           xor eax, edx
00BE58A3  48 89 55 60                     mov qword ptr [rbp + 0x60], rdx
00BE58A7  33 F0                           xor esi, eax
00BE58A9  BA 01 00 00 00                  mov edx, 1
00BE58AE  83 E6 3F                        and esi, 0x3f
00BE58B1  0F 44 F2                        cmove esi, edx
00BE58B4  83 C3 FF                        add ebx, -1
00BE58B7  75 B2                           jne 0x140be586b
00BE58B9  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
00BE58BD  41 83 E1 7F                     and r9d, 0x7f
00BE58C1  41 83 F9 08                     cmp r9d, 8
00BE58C5  72 1C                           jb 0x140be58e3
00BE58C7  41 8B C1                        mov eax, r9d
00BE58CA  48 C1 E8 03                     shr rax, 3
00BE58CE  4D 33 02                        xor r8, qword ptr [r10]
00BE58D1  8B CE                           mov ecx, esi
00BE58D3  49 D3 C0                        rol r8, cl
00BE58D6  49 83 C2 08                     add r10, 8
00BE58DA  41 83 C1 F8                     add r9d, -8
00BE58DE  48 2B C2                        sub rax, rdx
00BE58E1  75 EB                           jne 0x140be58ce
00BE58E3  45 33 DB                        xor r11d, r11d
00BE58E6  45 85 C9                        test r9d, r9d
00BE58E9  74 15                           je 0x140be5900
00BE58EB  41 0F B6 02                     movzx eax, byte ptr [r10]
00BE58EF  8B CE                           mov ecx, esi
00BE58F1  4C 33 C0                        xor r8, rax
00BE58F4  4C 03 D2                        add r10, rdx
00BE58F7  49 D3 C0                        rol r8, cl
00BE58FA  41 83 C1 FF                     add r9d, -1
00BE58FE  75 EB                           jne 0x140be58eb
00BE5900  49 8B C0                        mov rax, r8
00BE5903  EB 03                           jmp 0x140be5908
00BE5905  44 33 C0                        xor r8d, eax
00BE5908  48 C1 E8 1F                     shr rax, 0x1f
00BE590C  48 85 C0                        test rax, rax
00BE590F  75 F4                           jne 0x140be5905
00BE5911  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00BE5916  41 0F BA F0 1F                  btr r8d, 0x1f
00BE591B  8B B5 F8 00 00 00               mov esi, dword ptr [rbp + 0xf8]
00BE5921  44 89 40 08                     mov dword ptr [rax + 8], r8d
00BE5925  EB 13                           jmp 0x140be593a
00BE5927  41 8B C3                        mov eax, r11d
00BE592A  45 8B FB                        mov r15d, r11d
00BE592D  3B C2                           cmp eax, edx
00BE592F  0F 82 2B 03 00 00               jb 0x140be5c60
00BE5935  EB 0D                           jmp 0x140be5944
00BE5937  45 33 DB                        xor r11d, r11d
00BE593A  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BE593F  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00BE5944  44 3B FE                        cmp r15d, esi
00BE5947  0F 87 13 03 00 00               ja 0x140be5c60
00BE594D  49 3B D8                        cmp rbx, r8
00BE5950  0F 84 0A 03 00 00               je 0x140be5c60
00BE5956  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00BE595B  4D 3B F0                        cmp r14, r8
00BE595E  0F 84 FC 02 00 00               je 0x140be5c60
00BE5964  45 8B 7E 04                     mov r15d, dword ptr [r14 + 4]
00BE5968  44 3B FE                        cmp r15d, esi
00BE596B  0F 87 EF 02 00 00               ja 0x140be5c60
00BE5971  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00BE5976  BA 01 00 00 00                  mov edx, 1
00BE597B  4D 3B F0                        cmp r14, r8
00BE597E  0F 84 DC 02 00 00               je 0x140be5c60
00BE5984  45 85 ED                        test r13d, r13d
00BE5987  74 08                           je 0x140be5991
00BE5989  41 B0 80                        mov r8b, 0x80
00BE598C  E9 96 02 00 00                  jmp 0x140be5c27
00BE5991  8B 5B 04                        mov ebx, dword ptr [rbx + 4]
00BE5994  45 8B 26                        mov r12d, dword ptr [r14]
00BE5997  44 3B E3                        cmp r12d, ebx
00BE599A  0F 83 1C 01 00 00               jae 0x140be5abc
00BE59A0  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE59A6  0F BA E1 14                     bt ecx, 0x14
00BE59AA  0F 83 CD 06 00 00               jae 0x140be607d
00BE59B0  44 39 9F 18 09 00 00            cmp dword ptr [rdi + 0x918], r11d
00BE59B7  0F 85 FF 00 00 00               jne 0x140be5abc
00BE59BD  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE59C7  4C 89 9F 28 09 00 00            mov qword ptr [rdi + 0x928], r11
00BE59CE  48 03 C7                        add rax, rdi
00BE59D1  48 C7 87 30 09 00 00 0F 01 00 00  mov qword ptr [rdi + 0x930], 0x10f
00BE59DC  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE59E3  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00BE59E8  48 89 87 38 09 00 00            mov qword ptr [rdi + 0x938], rax
00BE59EF  89 97 18 09 00 00               mov dword ptr [rdi + 0x918], edx
00BE59F5  0F BA E1 1D                     bt ecx, 0x1d
00BE59F9  0F 82 BD 00 00 00               jb 0x140be5abc
00BE59FF  F7 87 DC 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9dc], 0x200000
00BE5A09  0F 84 AD 00 00 00               je 0x140be5abc
00BE5A0F  84 CA                           test dl, cl
00BE5A11  0F 84 A5 00 00 00               je 0x140be5abc
00BE5A17  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE5A1D  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE5A23  4C 8B 9F 38 08 00 00            mov r11, qword ptr [rdi + 0x838]
00BE5A2A  2B C1                           sub eax, ecx
00BE5A2C  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE5A33  4C 8D 0C 39                     lea r9, [rcx + rdi]
00BE5A37  8B C8                           mov ecx, eax
00BE5A39  48 C1 E9 03                     shr rcx, 3
00BE5A3D  4D 8D 14 C9                     lea r10, [r9 + rcx*8]
00BE5A41  EB 21                           jmp 0x140be5a64
00BE5A43  4D 31 01                        xor qword ptr [r9], r8
00BE5A46  49 8B C3                        mov rax, r11
00BE5A49  49 33 01                        xor rax, qword ptr [r9]
00BE5A4C  41 0F B6 C8                     movzx ecx, r8b
00BE5A50  83 E1 3F                        and ecx, 0x3f
00BE5A53  49 D3 C8                        ror r8, cl
00BE5A56  4C 03 C0                        add r8, rax
00BE5A59  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE5A60  49 83 C1 08                     add r9, 8
00BE5A64  4D 3B CA                        cmp r9, r10
00BE5A67  75 DA                           jne 0x140be5a43
00BE5A69  0F BA B7 DC 09 00 00 15         btr dword ptr [rdi + 0x9dc], 0x15
00BE5A71  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE5A78  74 42                           je 0x140be5abc
00BE5A7A  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE5A81  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE5A87  48 89 38                        mov qword ptr [rax], rdi
00BE5A8A  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE5A8D  33 C0                           xor eax, eax
00BE5A8F  48 8B 8F 80 0A 00 00            mov rcx, qword ptr [rdi + 0xa80]
00BE5A96  39 87 18 09 00 00               cmp dword ptr [rdi + 0x918], eax
00BE5A9C  75 0E                           jne 0x140be5aac
00BE5A9E  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE5AA5  49 33 C8                        xor rcx, r8
00BE5AA8  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE5AAC  33 D2                           xor edx, edx
00BE5AAE  41 B9 00 01 00 00               mov r9d, 0x100
00BE5AB4  48 8B CF                        mov rcx, rdi
00BE5AB7  E8 C8 28 00 00                  call 0x140be8384
00BE5ABC  4C 8B DB                        mov r11, rbx
00BE5ABF  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00BE5AC3  4C 03 5C 24 58                  add r11, qword ptr [rsp + 0x58]
00BE5AC8  4C 8D 45 00                     lea r8, [rbp]
00BE5ACC  45 8B CC                        mov r9d, r12d
00BE5ACF  44 2B CB                        sub r9d, ebx
00BE5AD2  41 8B D9                        mov ebx, r9d
00BE5AD5  49 03 DB                        add rbx, r11
00BE5AD8  33 C0                           xor eax, eax
00BE5ADA  44 8B D0                        mov r10d, eax
00BE5ADD  49 8B 08                        mov rcx, qword ptr [r8]
00BE5AE0  8B 02                           mov eax, dword ptr [rdx]
00BE5AE2  48 03 C1                        add rax, rcx
00BE5AE5  4C 3B D8                        cmp r11, rax
00BE5AE8  73 09                           jae 0x140be5af3
00BE5AEA  48 3B D9                        cmp rbx, rcx
00BE5AED  0F 87 1F 01 00 00               ja 0x140be5c12
00BE5AF3  41 FF C2                        inc r10d
00BE5AF6  49 83 C0 08                     add r8, 8
00BE5AFA  48 83 C2 04                     add rdx, 4
00BE5AFE  41 83 FA 06                     cmp r10d, 6
00BE5B02  72 D9                           jb 0x140be5add
00BE5B04  41 83 F9 04                     cmp r9d, 4
00BE5B08  0F 82 04 01 00 00               jb 0x140be5c12
00BE5B0E  44 01 8F 48 08 00 00            add dword ptr [rdi + 0x848], r9d
00BE5B15  4D 8B D3                        mov r10, r11
00BE5B18  8B B7 34 08 00 00               mov esi, dword ptr [rdi + 0x834]
00BE5B1E  49 8B C3                        mov rax, r11
00BE5B21  4C 8B B7 38 08 00 00            mov r14, qword ptr [rdi + 0x838]
00BE5B28  41 8B C9                        mov ecx, r9d
00BE5B2B  49 03 CB                        add rcx, r11
00BE5B2E  4C 3B D9                        cmp r11, rcx
00BE5B31  73 0C                           jae 0x140be5b3f
00BE5B33  0F 18 00                        prefetchnta byte ptr [rax]
00BE5B36  48 83 C0 40                     add rax, 0x40
00BE5B3A  48 3B C1                        cmp rax, rcx
00BE5B3D  72 F4                           jb 0x140be5b33
00BE5B3F  41 8B D9                        mov ebx, r9d
00BE5B42  4D 8B C6                        mov r8, r14
00BE5B45  C1 EB 07                        shr ebx, 7
00BE5B48  BA 01 00 00 00                  mov edx, 1
00BE5B4D  85 DB                           test ebx, ebx
00BE5B4F  74 5C                           je 0x140be5bad
00BE5B51  48 BF 01 20 00 04 80 00 10 70   movabs rdi, 0x7010008004002001
00BE5B5B  B8 08 00 00 00                  mov eax, 8
00BE5B60  4D 33 02                        xor r8, qword ptr [r10]
00BE5B63  8B CE                           mov ecx, esi
00BE5B65  49 D3 C0                        rol r8, cl
00BE5B68  4D 33 42 08                     xor r8, qword ptr [r10 + 8]
00BE5B6C  49 83 C2 10                     add r10, 0x10
00BE5B70  49 D3 C0                        rol r8, cl
00BE5B73  48 2B C2                        sub rax, rdx
00BE5B76  75 E8                           jne 0x140be5b60
00BE5B78  49 8B CA                        mov rcx, r10
00BE5B7B  49 2B CB                        sub rcx, r11
00BE5B7E  49 33 CE                        xor rcx, r14
00BE5B81  48 8B C1                        mov rax, rcx
00BE5B84  48 C1 C0 11                     rol rax, 0x11
00BE5B88  48 33 C8                        xor rcx, rax
00BE5B8B  48 8B C7                        mov rax, rdi
00BE5B8E  48 F7 E1                        mul rcx
00BE5B91  33 F0                           xor esi, eax
00BE5B93  48 89 55 68                     mov qword ptr [rbp + 0x68], rdx
00BE5B97  33 F2                           xor esi, edx
00BE5B99  BA 01 00 00 00                  mov edx, 1
00BE5B9E  83 E6 3F                        and esi, 0x3f
00BE5BA1  0F 44 F2                        cmove esi, edx
00BE5BA4  83 C3 FF                        add ebx, -1
00BE5BA7  75 B2                           jne 0x140be5b5b
00BE5BA9  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
00BE5BAD  41 83 E1 7F                     and r9d, 0x7f
00BE5BB1  41 83 F9 08                     cmp r9d, 8
00BE5BB5  72 1C                           jb 0x140be5bd3
00BE5BB7  41 8B C1                        mov eax, r9d
00BE5BBA  48 C1 E8 03                     shr rax, 3
00BE5BBE  4D 33 02                        xor r8, qword ptr [r10]
00BE5BC1  8B CE                           mov ecx, esi
00BE5BC3  49 D3 C0                        rol r8, cl
00BE5BC6  49 83 C2 08                     add r10, 8
00BE5BCA  41 83 C1 F8                     add r9d, -8
00BE5BCE  48 2B C2                        sub rax, rdx
00BE5BD1  75 EB                           jne 0x140be5bbe
00BE5BD3  45 33 DB                        xor r11d, r11d
00BE5BD6  45 85 C9                        test r9d, r9d
00BE5BD9  74 15                           je 0x140be5bf0
00BE5BDB  41 0F B6 02                     movzx eax, byte ptr [r10]
00BE5BDF  8B CE                           mov ecx, esi
00BE5BE1  4C 33 C0                        xor r8, rax
00BE5BE4  4C 03 D2                        add r10, rdx
00BE5BE7  49 D3 C0                        rol r8, cl
00BE5BEA  41 83 C1 FF                     add r9d, -1
00BE5BEE  75 EB                           jne 0x140be5bdb
00BE5BF0  49 8B C0                        mov rax, r8
00BE5BF3  EB 03                           jmp 0x140be5bf8
00BE5BF5  44 32 C0                        xor r8b, al
00BE5BF8  48 C1 E8 07                     shr rax, 7
00BE5BFC  48 85 C0                        test rax, rax
00BE5BFF  75 F4                           jne 0x140be5bf5
00BE5C01  8B B5 F8 00 00 00               mov esi, dword ptr [rbp + 0xf8]
00BE5C07  41 80 E0 7F                     and r8b, 0x7f
00BE5C0B  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00BE5C10  EB 06                           jmp 0x140be5c18
00BE5C12  45 33 DB                        xor r11d, r11d
00BE5C15  41 B0 80                        mov r8b, 0x80
00BE5C18  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00BE5C1D  BA 01 00 00 00                  mov edx, 1
00BE5C22  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BE5C27  44 88 00                        mov byte ptr [rax], r8b
00BE5C2A  48 83 C3 0C                     add rbx, 0xc
00BE5C2E  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00BE5C33  49 83 C6 0C                     add r14, 0xc
00BE5C37  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00BE5C3C  48 03 C2                        add rax, rdx
00BE5C3F  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00BE5C44  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00BE5C49  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00BE5C4E  4D 3B F0                        cmp r14, r8
00BE5C51  74 04                           je 0x140be5c57
00BE5C53  45 8B 7E 04                     mov r15d, dword ptr [r14 + 4]
00BE5C57  44 3B FE                        cmp r15d, esi
00BE5C5A  0F 86 1B FD FF FF               jbe 0x140be597b
00BE5C60  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00BE5C65  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00BE5C6A  45 85 ED                        test r13d, r13d
00BE5C6D  0F 85 67 01 00 00               jne 0x140be5dda
00BE5C73  44 3B E6                        cmp r12d, esi
00BE5C76  0F 84 5E 01 00 00               je 0x140be5dda
00BE5C7C  45 8B DC                        mov r11d, r12d
00BE5C7F  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00BE5C83  4D 03 DF                        add r11, r15
00BE5C86  45 89 66 0C                     mov dword ptr [r14 + 0xc], r12d
00BE5C8A  44 8B CE                        mov r9d, esi
00BE5C8D  41 89 76 10                     mov dword ptr [r14 + 0x10], esi
00BE5C91  45 2B CC                        sub r9d, r12d
00BE5C94  48 8D 55 00                     lea rdx, [rbp]
00BE5C98  41 8B D9                        mov ebx, r9d
00BE5C9B  49 03 DB                        add rbx, r11
00BE5C9E  45 33 ED                        xor r13d, r13d
00BE5CA1  45 8B C5                        mov r8d, r13d
00BE5CA4  45 8D 65 08                     lea r12d, [r13 + 8]
00BE5CA8  4C 8B 12                        mov r10, qword ptr [rdx]
00BE5CAB  8B 01                           mov eax, dword ptr [rcx]
00BE5CAD  49 03 C2                        add rax, r10
00BE5CB0  4C 3B D8                        cmp r11, rax
00BE5CB3  73 09                           jae 0x140be5cbe
00BE5CB5  49 3B DA                        cmp rbx, r10
00BE5CB8  0F 87 14 01 00 00               ja 0x140be5dd2
00BE5CBE  41 FF C0                        inc r8d
00BE5CC1  49 03 D4                        add rdx, r12
00BE5CC4  48 83 C1 04                     add rcx, 4
00BE5CC8  41 83 F8 06                     cmp r8d, 6
00BE5CCC  72 DA                           jb 0x140be5ca8
00BE5CCE  44 01 8F 48 08 00 00            add dword ptr [rdi + 0x848], r9d
00BE5CD5  4D 8B D3                        mov r10, r11
00BE5CD8  8B B7 34 08 00 00               mov esi, dword ptr [rdi + 0x834]
00BE5CDE  49 8B C3                        mov rax, r11
00BE5CE1  4C 8B B7 38 08 00 00            mov r14, qword ptr [rdi + 0x838]
00BE5CE8  41 8B C9                        mov ecx, r9d
00BE5CEB  49 03 CB                        add rcx, r11
00BE5CEE  4C 3B D9                        cmp r11, rcx
00BE5CF1  73 0C                           jae 0x140be5cff
00BE5CF3  0F 18 00                        prefetchnta byte ptr [rax]
00BE5CF6  48 83 C0 40                     add rax, 0x40
00BE5CFA  48 3B C1                        cmp rax, rcx
00BE5CFD  72 F4                           jb 0x140be5cf3
00BE5CFF  41 8B D9                        mov ebx, r9d
00BE5D02  4D 8B C6                        mov r8, r14
00BE5D05  C1 EB 07                        shr ebx, 7
00BE5D08  41 BD 01 00 00 00               mov r13d, 1
00BE5D0E  85 DB                           test ebx, ebx
00BE5D10  74 58                           je 0x140be5d6a
00BE5D12  49 BF 01 20 00 04 80 00 10 70   movabs r15, 0x7010008004002001
00BE5D1C  49 8B C4                        mov rax, r12
00BE5D1F  4D 33 02                        xor r8, qword ptr [r10]
00BE5D22  8B CE                           mov ecx, esi
00BE5D24  4D 03 D4                        add r10, r12
00BE5D27  49 D3 C0                        rol r8, cl
00BE5D2A  4D 33 02                        xor r8, qword ptr [r10]
00BE5D2D  4D 03 D4                        add r10, r12
00BE5D30  49 D3 C0                        rol r8, cl
00BE5D33  49 2B C5                        sub rax, r13
00BE5D36  75 E7                           jne 0x140be5d1f
00BE5D38  49 8B CA                        mov rcx, r10
00BE5D3B  49 2B CB                        sub rcx, r11
00BE5D3E  49 33 CE                        xor rcx, r14
00BE5D41  48 8B C1                        mov rax, rcx
00BE5D44  48 C1 C0 11                     rol rax, 0x11
00BE5D48  48 33 C8                        xor rcx, rax
00BE5D4B  49 8B C7                        mov rax, r15
00BE5D4E  48 F7 E1                        mul rcx
00BE5D51  33 F0                           xor esi, eax
00BE5D53  48 89 55 70                     mov qword ptr [rbp + 0x70], rdx
00BE5D57  33 F2                           xor esi, edx
00BE5D59  83 E6 3F                        and esi, 0x3f
00BE5D5C  41 0F 44 F5                     cmove esi, r13d
00BE5D60  83 C3 FF                        add ebx, -1
00BE5D63  75 B7                           jne 0x140be5d1c
00BE5D65  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00BE5D6A  41 83 E1 7F                     and r9d, 0x7f
00BE5D6E  45 3B CC                        cmp r9d, r12d
00BE5D71  72 1B                           jb 0x140be5d8e
00BE5D73  41 8B C1                        mov eax, r9d
00BE5D76  48 C1 E8 03                     shr rax, 3
00BE5D7A  4D 33 02                        xor r8, qword ptr [r10]
00BE5D7D  8B CE                           mov ecx, esi
00BE5D7F  49 D3 C0                        rol r8, cl
00BE5D82  4D 03 D4                        add r10, r12
00BE5D85  41 83 C1 F8                     add r9d, -8
00BE5D89  49 2B C5                        sub rax, r13
00BE5D8C  75 EC                           jne 0x140be5d7a
00BE5D8E  45 33 DB                        xor r11d, r11d
00BE5D91  45 85 C9                        test r9d, r9d
00BE5D94  74 15                           je 0x140be5dab
00BE5D96  41 0F B6 02                     movzx eax, byte ptr [r10]
00BE5D9A  8B CE                           mov ecx, esi
00BE5D9C  4C 33 C0                        xor r8, rax
00BE5D9F  4D 03 D5                        add r10, r13
00BE5DA2  49 D3 C0                        rol r8, cl
00BE5DA5  41 83 C1 FF                     add r9d, -1
00BE5DA9  75 EB                           jne 0x140be5d96
00BE5DAB  49 8B C0                        mov rax, r8
00BE5DAE  EB 03                           jmp 0x140be5db3
00BE5DB0  44 33 C0                        xor r8d, eax
00BE5DB3  48 C1 E8 1F                     shr rax, 0x1f
00BE5DB7  48 85 C0                        test rax, rax
00BE5DBA  75 F4                           jne 0x140be5db0
00BE5DBC  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00BE5DC1  41 0F BA F0 1F                  btr r8d, 0x1f
00BE5DC6  8B B5 F8 00 00 00               mov esi, dword ptr [rbp + 0xf8]
00BE5DCC  45 89 46 14                     mov dword ptr [r14 + 0x14], r8d
00BE5DD0  EB 03                           jmp 0x140be5dd5
00BE5DD2  45 33 DB                        xor r11d, r11d
00BE5DD5  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00BE5DDA  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00BE5DDF  48 3B D9                        cmp rbx, rcx
00BE5DE2  74 38                           je 0x140be5e1c
00BE5DE4  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
00BE5DE7  39 03                           cmp dword ptr [rbx], eax
00BE5DE9  72 31                           jb 0x140be5e1c
00BE5DEB  39 73 04                        cmp dword ptr [rbx + 4], esi
00BE5DEE  77 2C                           ja 0x140be5e1c
00BE5DF0  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00BE5DF5  4C 3B C1                        cmp r8, rcx
00BE5DF8  74 19                           je 0x140be5e13
00BE5DFA  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00BE5DFF  C6 00 80                        mov byte ptr [rax], 0x80
00BE5E02  48 FF C0                        inc rax
00BE5E05  49 83 C0 0C                     add r8, 0xc
00BE5E09  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00BE5E0E  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00BE5E13  48 83 C3 0C                     add rbx, 0xc
00BE5E17  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00BE5E1C  4C 8B 65 88                     mov r12, qword ptr [rbp - 0x78]
00BE5E20  49 83 C6 18                     add r14, 0x18
00BE5E24  49 83 C4 28                     add r12, 0x28
00BE5E28  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00BE5E2D  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
00BE5E31  4C 3B 75 A0                     cmp r14, qword ptr [rbp - 0x60]
00BE5E35  74 0A                           je 0x140be5e41
00BE5E37  BE 01 00 00 00                  mov esi, 1
00BE5E3C  E9 A2 F7 FF FF                  jmp 0x140be55e3
00BE5E41  48 8B 7D 98                     mov rdi, qword ptr [rbp - 0x68]
00BE5E45  45 33 E4                        xor r12d, r12d
00BE5E48  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00BE5E4D  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
00BE5E54  48 89 3E                        mov qword ptr [rsi], rdi
00BE5E57  44 8B B5 F0 00 00 00            mov r14d, dword ptr [rbp + 0xf0]
00BE5E5E  B9 04 00 00 80                  mov ecx, 0x80000004
00BE5E63  41 83 E6 EF                     and r14d, 0xffffffef
00BE5E67  41 8B C6                        mov eax, r14d
00BE5E6A  23 C1                           and eax, ecx
00BE5E6C  3B C1                           cmp eax, ecx
00BE5E6E  74 7E                           je 0x140be5eee
00BE5E70  4C 8B 7D F0                     mov r15, qword ptr [rbp - 0x10]
00BE5E74  41 BD 00 00 00 80               mov r13d, 0x80000000
00BE5E7A  48 8B 87 08 02 00 00            mov rax, qword ptr [rdi + 0x208]
00BE5E81  49 8B CF                        mov rcx, r15
00BE5E84  45 0B F5                        or r14d, r13d
00BE5E87  E8 D4 4B 00 00                  call 0x140beaa60
00BE5E8C  8B 88 94 00 00 00               mov ecx, dword ptr [rax + 0x94]
00BE5E92  83 F9 14                        cmp ecx, 0x14
00BE5E95  72 57                           jb 0x140be5eee
00BE5E97  8B 80 90 00 00 00               mov eax, dword ptr [rax + 0x90]
00BE5E9D  48 8D 3C 08                     lea rdi, [rax + rcx]
00BE5EA1  49 03 FF                        add rdi, r15
00BE5EA4  4A 8D 1C 38                     lea rbx, [rax + r15]
00BE5EA8  EB 3F                           jmp 0x140be5ee9
00BE5EAA  44 39 63 0C                     cmp dword ptr [rbx + 0xc], r12d
00BE5EAE  74 3E                           je 0x140be5eee
00BE5EB0  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00BE5EB3  85 C0                           test eax, eax
00BE5EB5  74 37                           je 0x140be5eee
00BE5EB7  4A 8B 14 38                     mov rdx, qword ptr [rax + r15]
00BE5EBB  48 85 D2                        test rdx, rdx
00BE5EBE  74 25                           je 0x140be5ee5
00BE5EC0  45 8B C6                        mov r8d, r14d
00BE5EC3  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00BE5EC8  E8 37 DB FF FF                  call 0x140be3a04
00BE5ECD  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00BE5ED2  48 89 0E                        mov qword ptr [rsi], rcx
00BE5ED5  42 8D 0C 28                     lea ecx, [rax + r13]
00BE5ED9  41 85 CD                        test r13d, ecx
00BE5EDC  75 07                           jne 0x140be5ee5
00BE5EDE  3D 0E 01 00 C0                  cmp eax, 0xc000010e
00BE5EE3  75 0B                           jne 0x140be5ef0
00BE5EE5  48 83 C3 14                     add rbx, 0x14
00BE5EE9  48 3B DF                        cmp rbx, rdi
00BE5EEC  75 BC                           jne 0x140be5eaa
00BE5EEE  33 C0                           xor eax, eax
00BE5EF0  48 81 C4 98 01 00 00            add rsp, 0x198
00BE5EF7  41 5F                           pop r15
00BE5EF9  41 5E                           pop r14
00BE5EFB  41 5D                           pop r13
00BE5EFD  41 5C                           pop r12
00BE5EFF  5F                              pop rdi
00BE5F00  5E                              pop rsi
00BE5F01  5B                              pop rbx
00BE5F02  5D                              pop rbp
00BE5F03  C3                              ret
00BE5F04  CC                              int3
00BE5F05  41 B9 05 00 00 00               mov r9d, 5
00BE5F0B  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00BE5F10  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE5F1A  4C 8B C6                        mov r8, rsi
00BE5F1D  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE5F23  C1 C1 65                        rol ecx, 0x65
00BE5F26  41 8D 51 05                     lea edx, [r9 + 5]
00BE5F2A  E8 31 77 91 FF                  call 0x1404fd660
00BE5F2F  CC                              int3
00BE5F30  41 B9 05 00 00 00               mov r9d, 5
00BE5F36  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00BE5F3B  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE5F45  4C 8B C6                        mov r8, rsi
00BE5F48  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE5F4E  C1 C1 65                        rol ecx, 0x65
00BE5F51  41 8D 51 05                     lea edx, [r9 + 5]
00BE5F55  E8 06 77 91 FF                  call 0x1404fd660
00BE5F5A  CC                              int3
00BE5F5B  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE5F65  41 B9 07 00 00 00               mov r9d, 7
00BE5F6B  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE5F71  4D 8B C7                        mov r8, r15
00BE5F74  C1 C1 65                        rol ecx, 0x65
00BE5F77  48 8B D6                        mov rdx, rsi
00BE5F7A  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00BE5F7F  E8 DC 76 91 FF                  call 0x1404fd660
00BE5F84  CC                              int3
00BE5F85  45 33 C9                        xor r9d, r9d
00BE5F88  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE5F92  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE5F98  4D 8B C7                        mov r8, r15
00BE5F9B  C1 C1 65                        rol ecx, 0x65
00BE5F9E  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00BE5FA3  41 8D 51 0A                     lea edx, [r9 + 0xa]
00BE5FA7  E8 B4 76 91 FF                  call 0x1404fd660
00BE5FAC  CC                              int3
00BE5FAD  41 B9 01 00 00 00               mov r9d, 1
00BE5FB3  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE5FBD  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE5FC3  4D 8B C7                        mov r8, r15
00BE5FC6  C1 C1 65                        rol ecx, 0x65
00BE5FC9  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00BE5FCE  41 8D 51 09                     lea edx, [r9 + 9]
00BE5FD2  E8 89 76 91 FF                  call 0x1404fd660
00BE5FD7  CC                              int3
00BE5FD8  44 8B C8                        mov r9d, eax
00BE5FDB  4D 8B C7                        mov r8, r15
00BE5FDE  33 C0                           xor eax, eax
00BE5FE0  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE5FEA  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE5FF0  C1 C1 65                        rol ecx, 0x65
00BE5FF3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BE5FF8  8D 50 0A                        lea edx, [rax + 0xa]
00BE5FFB  E8 60 76 91 FF                  call 0x1404fd660
00BE6000  CC                              int3
00BE6001  44 8B C8                        mov r9d, eax
00BE6004  33 C0                           xor eax, eax
00BE6006  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE6010  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE6016  C1 C1 65                        rol ecx, 0x65
00BE6019  8D 50 0A                        lea edx, [rax + 0xa]
00BE601C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BE6021  E8 3A 76 91 FF                  call 0x1404fd660
00BE6026  CC                              int3
00BE6027  41 B9 02 00 00 00               mov r9d, 2
00BE602D  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE6037  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE603D  4D 8B C7                        mov r8, r15
00BE6040  C1 C1 65                        rol ecx, 0x65
00BE6043  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00BE6048  41 8D 51 08                     lea edx, [r9 + 8]
00BE604C  E8 0F 76 91 FF                  call 0x1404fd660
00BE6051  CC                              int3
00BE6052  41 B9 03 00 00 00               mov r9d, 3
00BE6058  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00BE605D  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE6067  4D 8B C7                        mov r8, r15
00BE606A  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE6070  C1 C1 65                        rol ecx, 0x65
00BE6073  41 8D 51 07                     lea edx, [r9 + 7]
00BE6077  E8 E4 75 91 FF                  call 0x1404fd660
00BE607C  CC                              int3
00BE607D  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00BE6082  41 B9 06 00 00 00               mov r9d, 6
00BE6088  C7 85 E0 00 00 00 09 00 00 E8   mov dword ptr [rbp + 0xe0], 0xe8000009
00BE6092  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
00BE6098  C1 C1 65                        rol ecx, 0x65
00BE609B  41 8D 51 04                     lea edx, [r9 + 4]
00BE609F  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00BE60A4  E8 B7 75 91 FF                  call 0x1404fd660
00BE60A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BE3A04(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p58;

    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (408);
    v_stack_m190 = *(unsigned __int64 *)(a1);
    result = KeGuardDispatchICall(a2, v_rsp - 216 + 48, a3, a4);
    *(unsigned __int64 *)(v_rsp - 216 + 248) = result;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 216 - 16) = *(unsigned __int64 *)(v_rsp - 216 + 56);
    if (*(unsigned __int64 *)(v_rsp - 216 + 56) != 0) goto loc_00BE3A87;
    if (((*(unsigned int *)(v_stack_m190 + 2520)) & (0x100000ULL)) == 0) goto loc_00BE5F05;
    goto loc_00BE5EF0;
loc_00BE3A87:
    *(unsigned __int64 *)(v_rsp - 216 - 80) = 0;
loc_00BE3A97:
    *(unsigned __int8 *)(v_rsp - 216 - 72) = 0;
    result = (v_rsp - 216 - 72) + (4 - 3);
    a1 = (unsigned int)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE3A97;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2092))) == 0) goto loc_00BE3C89;
loc_00BE3AD2:
    v_r10 = v_stack_m190;
    if (*(unsigned __int64 *)(v_stack_m190 + 2752) != 0) { v_r10 = *(unsigned __int64 *)(v_stack_m190 + 2752); }
    a3 = ((unsigned int)(*(unsigned int *)(v_r10 + 2088))) + (v_r10);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 80))) == 0) goto loc_00BE3AFB;
    v_r11 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 76)))) <= 0) {
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 72)));
        v_r11 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 76)));
        a3 = (a3) + (v_r10);
    }
    if (((unsigned int)(v_r11)) == 0) goto loc_00BE3C16;
    v_rdi = (unsigned int)((0) - ((unsigned int)(v_r11)));
loc_00BE3B1C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) - (1));
    if (condition_is_equal) goto loc_00BE3BE3;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00BE3BD4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE3BC7;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00BE3BBB;
    a1 = (unsigned int)((a1) - (18));
    if (condition_is_equal) goto loc_00BE3BB4;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00BE3B87;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00BE3B5F;
    if (((unsigned int)(a1)) == 10) goto loc_00BE3BE3;
    goto loc_00BE3BF8;
loc_00BE3B5F:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 32))) & (0xFFFULL));
    a2 = ((unsigned int)(*(unsigned int *)(a3 + 40))) + (0xFFFULL);
    a2 = (a2) + (a1);
    a2 = (a2) >> (12);
    goto loc_00BE3BF8;
loc_00BE3B87:
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(a3 + 36))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 36)) - 1) & ((unsigned int)(result)));
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + (7));
    a2 = (unsigned int)((a2) & (0xFFFFFFF8ULL));
    result = (unsigned int)((*(unsigned __int16 *)(a3 + 40)) + (2));
    goto loc_00BE3BF8;
loc_00BE3BB4:
    goto loc_00BE3BCC;
loc_00BE3BBB:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 28))) + (3));
    result = (unsigned int)((result) << (4));
    goto loc_00BE3BF8;
loc_00BE3BC7:
loc_00BE3BCC:
    result = (unsigned int)((*(unsigned __int16 *)(a3 + 32)) + (55));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    goto loc_00BE3BF8;
loc_00BE3BD4:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 24))) + (2));
    result = (unsigned int)((result + result * 2) << (3));
    goto loc_00BE3BF8;
loc_00BE3BE3:
    a2 = (a2) >> (3);
loc_00BE3BF8:
    a3 = (a3) + (a2 * 4 + 48);
    v_rdi = (v_rdi) - (1);
    if (condition_is_not_equal) goto loc_00BE3B1C;
loc_00BE3C16:
    *(unsigned int *)(v_rsp - 216 - 80) = 1;
    a1 = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)(v_r10)));
    *(unsigned int *)(v_rsp - 216 - 72) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 216 - 76) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == 1) goto loc_00BE3C40;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == 12) goto loc_00BE3C40;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) != 43) goto loc_00BE3C4C;
loc_00BE3C40:
    if ((*(unsigned __int64 *)(a3 + 8)) != (*(unsigned __int64 *)(v_rsp - 216 + 248))) goto loc_00BE3C4C;
    if ((*(unsigned int *)(a3 + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 68))))) goto loc_00BE3C6D;
loc_00BE3C4C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) + (-33));
    if (((unsigned int)(result)) > 1) goto loc_00BE3C5D;
    if ((*(unsigned __int64 *)(a3 + 32)) == (*(unsigned __int64 *)(v_rsp - 216 - 16))) goto loc_00BE3C6D;
loc_00BE3C5D:
    a4 = (unsigned int)((0) + (1));
    if (((unsigned int)(a4)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2092))))) goto loc_00BE3C7C;
    a3 = 0;
    goto loc_00BE3AD2;
loc_00BE3C6D:
    if (0 == 0) goto loc_00BE3C7C;
    goto loc_00BE5EF0;
loc_00BE3C7C:
loc_00BE3C89:
    *(unsigned int *)(v_rsp - 216 + 248) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 240)));
    *(unsigned __int64 *)(v_rsp - 216 - 104) = v_stack_m190;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_rsp - 216 + 232), v_rsp - 216 + 120, a3, a4);
    a3 = 0;
    v_stack_m168 = result;
    v_stack_m160 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 140)));
    v_stack_m198 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 140)));
    v_stack_m180 = *(unsigned __int64 *)(v_rsp - 216 + 128);
    if (*(unsigned __int64 *)(v_rsp - 216 + 128) != 0) goto loc_00BE3CFA;
    if (((*(unsigned int *)(v_stack_m190 + 2520)) & (0x100000ULL)) == 0) goto loc_00BE5F30;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 + 224)) = v_stack_m190;
    goto loc_00BE53F6;
loc_00BE3CFA:
    *(unsigned __int64 *)(v_rsp - 216 - 64) = 0;
loc_00BE3D07:
    *(unsigned __int8 *)(v_rsp - 216 - 56) = 0;
    result = (v_rsp - 216 - 56) + 1;
    a1 = (unsigned int)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE3D07;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2092))) == 0) goto loc_00BE3EE4;
loc_00BE3D33:
    v_r10 = v_stack_m190;
    if (*(unsigned __int64 *)(v_stack_m190 + 2752) != 0) { v_r10 = *(unsigned __int64 *)(v_stack_m190 + 2752); }
    a3 = ((unsigned int)(*(unsigned int *)(v_r10 + 2088))) + (v_r10);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 64))) == 0) goto loc_00BE3D5C;
    v_r11 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 60)))) <= 0) {
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 56)));
        v_r11 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 60)));
        a3 = (a3) + (v_r10);
    }
    if (((unsigned int)(v_r11)) == 0) goto loc_00BE3E70;
    v_rdi = (unsigned int)((0) - ((unsigned int)(v_r11)));
loc_00BE3D7E:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) - (1));
    if (condition_is_equal) goto loc_00BE3E45;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00BE3E36;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE3E29;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00BE3E1D;
    a1 = (unsigned int)((a1) - (18));
    if (condition_is_equal) goto loc_00BE3E16;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00BE3DE9;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00BE3DC1;
    if (((unsigned int)(a1)) == 10) goto loc_00BE3E45;
    goto loc_00BE3E5A;
loc_00BE3DC1:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 32))) & (0xFFFULL));
    a2 = ((unsigned int)(*(unsigned int *)(a3 + 40))) + (0xFFFULL);
    a2 = (a2) + (a1);
    a2 = (a2) >> (12);
    goto loc_00BE3E5A;
loc_00BE3DE9:
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(a3 + 36))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 36)) - 1) & ((unsigned int)(result)));
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + (7));
    a2 = (unsigned int)((a2) & (0xFFFFFFF8ULL));
    result = (unsigned int)((*(unsigned __int16 *)(a3 + 40)) + (2));
    goto loc_00BE3E5A;
loc_00BE3E16:
    goto loc_00BE3E2E;
loc_00BE3E1D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 28))) + (3));
    result = (unsigned int)((result) << (4));
    goto loc_00BE3E5A;
loc_00BE3E29:
loc_00BE3E2E:
    result = (unsigned int)((*(unsigned __int16 *)(a3 + 32)) + (55));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    goto loc_00BE3E5A;
loc_00BE3E36:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 24))) + (2));
    result = (unsigned int)((result + result * 2) << (3));
    goto loc_00BE3E5A;
loc_00BE3E45:
    a2 = (a2) >> (3);
loc_00BE3E5A:
    a3 = (a3) + (a2 * 4 + 48);
    v_rdi = (v_rdi) - (1);
    if (condition_is_not_equal) goto loc_00BE3D7E;
loc_00BE3E70:
    *(unsigned int *)(v_rsp - 216 - 64) = 1;
    a1 = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)(v_r10)));
    *(unsigned int *)(v_rsp - 216 - 56) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 216 - 60) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == 1) goto loc_00BE3E9A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) == 12) goto loc_00BE3E9A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) != 43) goto loc_00BE3EAB;
loc_00BE3E9A:
    if ((*(unsigned __int64 *)(a3 + 8)) != v_stack_m168) goto loc_00BE3EAB;
    if ((*(unsigned int *)(a3 + 16)) == ((unsigned int)((unsigned int)(v_stack_m160)))) goto loc_00BE3EC8;
loc_00BE3EAB:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) + (-33));
    if (((unsigned int)(result)) > 1) goto loc_00BE3EB8;
    if ((*(unsigned __int64 *)(a3 + 32)) == v_stack_m180) goto loc_00BE3EC8;
loc_00BE3EB8:
    a4 = (unsigned int)((0) + (1));
    if (((unsigned int)(a4)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2092))))) goto loc_00BE3EDD;
    a3 = 0;
    goto loc_00BE3D33;
loc_00BE3EC8:
    v_r12 = 0;
    if (0 != 0) goto loc_00BE3F8A;
    goto loc_00BE3EE7;
loc_00BE3EDD:
loc_00BE3EE4:
    v_r12 = 0;
loc_00BE3EE7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 240)))) & (16)) == 0) goto loc_00BE3F0C;
    v_r14 = (unsigned int)(*(unsigned int *)(v_rsp - 216 + 248));
    if (((*(unsigned int *)(v_stack_m190 + 2524)) & (0x400ULL)) == 0) {
        v_r14 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 240)));
        v_r14 = (unsigned int)((v_r14) & (0xFFFFFFEFULL));
        *(unsigned int *)(v_rsp - 216 + 248) = (unsigned int)(v_r14);
    }
    if ((((unsigned __int8)(v_r14)) & (16)) == 0) goto loc_00BE3F2C;
    result = sub_00BE8D30(v_stack_m190, v_stack_m180, a3, a4);
    if ((unsigned int)(result) == 0) {
        v_r14 = (unsigned int)((v_r14) & (0xFFFFFFEFULL));
        *(unsigned int *)(v_rsp - 216 + 248) = (unsigned int)(v_r14);
    }
    if ((((unsigned __int8)(v_r14)) & (2)) == 0) goto loc_00BE3F94;
    result = KeGuardDispatchICall(v_stack_m180, v_stack_m180, a3, a4);
    a3 = 0;
    result = KeGuardDispatchICall(v_stack_m180, (unsigned __int8)(a3 + 1), a3, v_rsp - 216 - 48);
    if (result == 0) goto loc_00BE3F8A;
    if ((*(unsigned int *)(v_rsp - 216 - 48)) < 40) goto loc_00BE3F8A;
    a1 = ((unsigned int)(*(unsigned int *)(result + 12))) + (v_stack_m180);
    result = KeGuardDispatchICall(a1, v_stack_m190 + 2416, a3 + 1 + 4, v_rsp - 216 - 48);
    if ((unsigned int)(result) == 0) goto loc_00BE3F9A;
loc_00BE3F8A:
    goto loc_00BE5E4D;
loc_00BE3F94:
loc_00BE3F9A:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (1));
    *(unsigned int *)(v_rsp - 216 - 128) = (unsigned int)(result);
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) ^ (1));
    v_rdi = (unsigned int)((v_rdi) + (1));
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1624) * 1), v_stack_m190 + 2416, a3 + 1 + 4, v_rsp - 216 - 48);
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1328), 1, a3 + 1 + 4, v_rsp - 216 - 48);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m190 + 1320))) == (*(unsigned __int64 *)(v_stack_m190 + 1320))) goto loc_00BE403E;
loc_00BE400B:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m190 + 1320))) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1880));
    a3 = ((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1896) * 1))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1888) + a1 * 1));
    if (v_stack_m180 < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1888) + a1 * 1))) goto loc_00BE4026;
    if (v_stack_m180 < a3) goto loc_00BE4030;
loc_00BE4026:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m190 + 1320)))) != (*(unsigned __int64 *)(v_stack_m190 + 1320))) goto loc_00BE400B;
    goto loc_00BE403E;
loc_00BE4030:
    result = KeGuardDispatchICall(a1, (unsigned int)((unsigned int)(v_rdi)), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1880));
loc_00BE403E:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1328), (unsigned int)((unsigned int)(v_rdi)), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1880));
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1328), (unsigned int)((unsigned int)(v_rdi)), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1880));
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2520)) & (0x20000000ULL)) == 0) goto loc_00BE4080;
    result = sub_00BEFF8C(v_stack_m190, v_stack_m180, (unsigned int)((unsigned int)(v_r14)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1880));
    goto loc_00BE53D3;
loc_00BE4080:
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 216 + 32) = 0;
    *(unsigned int *)(v_rsp - 216 - 24) = 0;
    result = KeGuardDispatchICall(v_stack_m180, 1, a3, v_stack_m198);
    if (result != 0) goto loc_00BE40B0;
    v_stack_m198 = 0;
    goto loc_00BE40B4;
loc_00BE40B0:
loc_00BE40B4:
    *(unsigned __int64 *)(v_rsp - 216 + 8) = result;
    *(unsigned int *)(v_rsp - 216 - 36) = (unsigned int)((unsigned int)(v_stack_m198));
    result = KeGuardDispatchICall(v_stack_m180, 1, 12, v_stack_m198);
    *(unsigned __int64 *)(v_rsp - 216 - 96) = result;
    if (result != 0) goto loc_00BE40ED;
    v_stack_m198 = 0;
    goto loc_00BE40F1;
loc_00BE40ED:
loc_00BE40F1:
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_m198));
    *(unsigned __int64 *)(v_rsp - 216 + 16) = result;
    *(unsigned int *)(v_rsp - 216 - 32) = (unsigned int)((unsigned int)(v_stack_m198));
    result = KeGuardDispatchICall(v_stack_m180, 1, 10, v_stack_m198);
    if (result != 0) goto loc_00BE4129;
    v_stack_m198 = 0;
    goto loc_00BE412D;
loc_00BE4129:
loc_00BE412D:
    *(unsigned __int64 *)(v_rsp - 216 + 24) = result;
    *(unsigned int *)(v_rsp - 216 - 28) = (unsigned int)((unsigned int)(v_stack_m198));
    result = KeGuardDispatchICall(v_stack_m180, 1, 10, v_stack_m198);
    if (result != 0) goto loc_00BE4271;
    if (condition_is_above_or_equal) goto loc_00BE5F5B;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2328)) != 0) goto loc_00BE4267;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2344) = 0;
    result = (result) + (*(unsigned __int64 *)(v_rsp - 216 - 104));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2352) = 271;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2336) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2360) = v_stack_m180;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2328) = 1;
    if (condition_is_below) goto loc_00BE4267;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2524)) & (0x200000ULL)) == 0) goto loc_00BE4267;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2520))))) == 0) goto loc_00BE4267;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE4210;
loc_00BE41EF:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2676)) + *(unsigned __int64 *)(v_rsp - 216 - 104) * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2676)) + *(unsigned __int64 *)(v_rsp - 216 - 104) * 1) + (8);
loc_00BE4210:
    if (a4 != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2676)) + *(unsigned __int64 *)(v_rsp - 216 - 104) * 1 + a1 * 8)) goto loc_00BE41EF;
    if (a3 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2688))) goto loc_00BE4267;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1416)) = *(unsigned __int64 *)(v_rsp - 216 - 104);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1416);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2328)) == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 1416);
        a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(*(unsigned __int64 *)(v_rsp - 216 - 104), a2, a3, 256);
loc_00BE4267:
    goto loc_00BE4A2B;
loc_00BE4271:
    result = KeGuardDispatchICall(v_stack_m180, v_rsp - 216 - 8, a3, 256);
    *(unsigned __int64 *)(v_rsp - 216 + 40) = result;
    *(unsigned int *)(v_rsp - 216 - 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 8)));
    *(unsigned int *)(v_rsp - 216 - 40) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 84)));
    *(unsigned __int64 *)(v_rsp - 216) = v_stack_m180;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) + 288)) <= (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2660))) goto loc_00BE4383;
    result = sub_00BE7AF8(*(unsigned __int64 *)(v_rsp - 216 - 104), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) + 288)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2372)), 256);
    *(unsigned __int64 *)(v_rsp - 216 - 112) = result;
    if (result == 0) goto loc_00BE4A26;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2520)))) & (2)) != 0) goto loc_00BE437A;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2520))) & (0x10000000ULL));
    a1 = (unsigned int)(-(a1));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) + 288))) & (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2372)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)))) < 8) goto loc_00BE4317;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052))))) >> (3);
loc_00BE4308:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104)) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052))) + (-8));
    v_rbx = (*(unsigned __int64 *)(v_rsp - 216 - 104)) + (8);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00BE4308;
loc_00BE4317:
    if ((unsigned int)(result) == 0) goto loc_00BE4326;
loc_00BE431B:
    *(unsigned __int8 *)(v_rbx) = 0;
    v_rbx = (v_rbx) + (1);
    result = (unsigned int)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE431B;
loc_00BE4326:
    *(unsigned int *)(result + 2372) = (unsigned int)(a2);
    if (((unsigned int)(a2)) == 3) goto loc_00BE4365;
    if (((*(unsigned int *)(result + 2520)) & (0x8000000ULL)) != 0) goto loc_00BE435C;
    if ((unsigned int)(a2) == 0) goto loc_00BE435C;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024) - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024), 256);
    goto loc_00BE4374;
loc_00BE435C:
    goto loc_00BE436C;
loc_00BE4365:
loc_00BE436C:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024), 256);
loc_00BE4374:
    *(unsigned int *)(result + 2372) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 2372)));
loc_00BE437A:
    goto loc_00BE4390;
loc_00BE4383:
    *(unsigned __int64 *)(v_rsp - 216 - 112) = (unsigned int)(*(unsigned int *)(result + 2372));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052) = (unsigned int)(result);
loc_00BE4390:
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 216 - 120) = (unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1;
    v_stack_m170 = 6;
loc_00BE43BA:
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 40)));
loc_00BE43D2:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1) = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx + 48))) + (-8));
    result = ((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1) + (8);
    a2 = (6) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_00BE43D2;
    if ((unsigned int)(a1) == 0) goto loc_00BE43EF;
loc_00BE43E5:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (v_rbx + 1);
    a1 = (unsigned int)((a1) + (-1));
    if (condition_is_not_equal) goto loc_00BE43E5;
loc_00BE43EF:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1) = 0;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1 + 8) = *(unsigned __int64 *)(v_rsp - 216);
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 40)));
    if ((*(unsigned __int64 *)(v_rsp - 216)) >= (*(unsigned __int64 *)(v_rsp - 216) + (unsigned int)(*(unsigned int *)(v_rsp - 216 - 40)) * 1)) goto loc_00BE4429;
loc_00BE441D:
    result = (*(unsigned __int64 *)(v_rsp - 216)) + (64);
    if (result < (*(unsigned __int64 *)(v_rsp - 216) + (unsigned int)(*(unsigned int *)(v_rsp - 216 - 40)) * 1)) goto loc_00BE441D;
loc_00BE4429:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 40))))) >> (7));
    if ((unsigned int)(v_r11) == 0) goto loc_00BE449A;
loc_00BE4447:
loc_00BE444C:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216)));
    a3 = (a3) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216) + 8));
    a4 = (*(unsigned __int64 *)(v_rsp - 216)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE444C;
    a1 = (a4) - (*(unsigned __int64 *)(v_rsp - 216));
    a1 = (a1) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104));
    a1 = (a1) ^ (a1);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2100))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 40)))));
    *(unsigned __int64 *)(v_rsp - 216 + 72) = a2;
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(a2)));
    v_rbx = (unsigned int)((v_rbx) & (63));
    if (condition_is_equal) { v_rbx = 1; }
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE4447;
loc_00BE449A:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m178)))) & (127));
    if (((unsigned int)(a2)) < 8) goto loc_00BE44C5;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00BE44B1:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a2 = (unsigned int)((a2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE44B1;
loc_00BE44C5:
    if ((unsigned int)(a2) == 0) goto loc_00BE44DD;
loc_00BE44C9:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BE44C9;
loc_00BE44DD:
    result = (a3) >> (31);
    v_rbx = 0;
    goto loc_00BE44EF;
loc_00BE44E8:
    a3 = (unsigned int)((a3) ^ ((unsigned int)(result)));
    result = (result) >> (31);
loc_00BE44EF:
    if (result != 0) goto loc_00BE44E8;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1 + 20) = a3;
    v_r12 = (v_rsp - 216 - 40) + (4);
    v_r10 = ((unsigned int)(*(unsigned int *)(result + 2372)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) * 1) + (result + 48);
    v_r13 = (v_rsp - 216) + (8);
    if (condition_is_not_equal) goto loc_00BE43BA;
    if (*(unsigned __int64 *)(v_rsp - 216 - 112) == 0) goto loc_00BE4A26;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 24) = v_stack_m180;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120)) = 44;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2520)) & (0x8100000ULL)) != 0) goto loc_00BE456F;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2524)) & (0x8000ULL)) == 0) goto loc_00BE456F;
    result = sub_00BE8D30(*(unsigned __int64 *)(v_rsp - 216 - 112), v_stack_m180, a3, a4);
    if ((unsigned int)(result) != 0) {
    }
    v_stack_m1A8 = v_rsp - 216 - 44;
    *(unsigned __int64 *)(v_rsp - 216 - 104) = *(unsigned __int64 *)(v_rsp - 216 - 112);
    v_stack_m1B0 = v_rsp - 216 - 88;
    v_stack_m1B8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248)));
    v_stack_m190 = *(unsigned __int64 *)(v_rsp - 216 - 112);
    result = sub_00BE60B0(v_rsp - 216 - 104, v_stack_m168, (unsigned int)(v_stack_m160), v_stack_m180);
    if (!sign_flag) goto loc_00BE45C7;
    v_r12 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 + 224)) = v_stack_m190;
    goto loc_00BE53EA;
loc_00BE45C7:
    v_r12 = (v_r12) - (v_stack_m190);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(v_rsp - 216 - 104));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 216 - 44))) - (*(unsigned int *)(v_rsp - 216 - 88)));
    *(unsigned __int64 *)(v_rsp - 216 - 120) = v_r12;
    v_r11 = ((unsigned int)(*(unsigned int *)(v_rsp - 216 - 88))) + (*(unsigned __int64 *)(v_rsp - 216 + 224));
loc_00BE4601:
    *(unsigned __int64 *)(v_r12 + 192) = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result + 48))) + (-8));
    result = (v_r12 + 192) + (6 + 2);
    a2 = (6) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE4601;
    if ((unsigned int)(a1) == 0) goto loc_00BE4621;
loc_00BE4617:
    *(unsigned __int8 *)(result) = (unsigned __int8)(a2);
    result = (result) + (6 - 5);
    a1 = (unsigned int)((a1) + (-1));
    if (condition_is_not_equal) goto loc_00BE4617;
loc_00BE4621:
    *(unsigned int *)(v_r12 + 192) = (unsigned int)(a2);
    *(unsigned __int64 *)(v_r12 + 192 + 8) = v_r11;
    *(unsigned int *)(v_r12 + 192 + 16) = (unsigned int)(a4);
    a1 = ((unsigned int)((unsigned int)(a4))) + (v_r11);
    if (v_r11 >= a1) goto loc_00BE465D;
loc_00BE4651:
    result = (v_r11) + (64);
    if (result < a1) goto loc_00BE4651;
loc_00BE465D:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (7));
    if ((unsigned int)(v_rsi) == 0) goto loc_00BE46CA;
loc_00BE4679:
loc_00BE467C:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2104)) ^ (*(unsigned __int64 *)(v_r11));
    v_r10 = (v_r11) + (6 + 2);
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r10));
    v_r10 = (v_r10) + (6 + 2);
    result = (6 + 2) - (1);
    if (condition_is_not_equal) goto loc_00BE467C;
    a1 = (v_r10) - (v_r11);
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2104));
    a1 = (a1) ^ (a1);
    *(unsigned __int64 *)(v_rsp - 216 + 80) = 1;
    a2 = (unsigned int)((1) ^ ((unsigned int)(v_r12)));
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2100))) ^ ((unsigned int)(a2)));
    v_rdi = (unsigned int)((v_rdi) & (63));
    if (condition_is_equal) { v_rdi = 1; }
    v_rsi = (unsigned int)((v_rsi) + (-1));
    if (condition_is_not_equal) goto loc_00BE4679;
loc_00BE46CA:
    a4 = (unsigned int)((a4) & (127));
    if (((unsigned int)(a4)) < ((unsigned int)(6 + 2))) goto loc_00BE46EE;
    result = ((unsigned int)((unsigned int)(a4))) >> (3);
loc_00BE46DA:
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r10));
    v_r10 = (v_r10) + (6 + 2);
    a4 = (unsigned int)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE46DA;
loc_00BE46EE:
    v_r11 = 0;
    if ((unsigned int)(a4) == 0) goto loc_00BE470B;
loc_00BE46F6:
    a3 = (a3) ^ (*(unsigned __int8 *)(v_r10));
    v_r10 = (v_r10) + (1);
    a4 = (unsigned int)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE46F6;
loc_00BE470B:
    goto loc_00BE4713;
loc_00BE4710:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BE4713:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BE4710;
    *(unsigned int *)(v_r12 + 192 + 20) = a3;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 240) = (unsigned int)(result + 48);
    v_stack_m190 = *(unsigned __int64 *)(v_rsp - 216 - 104);
    if (*(unsigned __int64 *)(v_rsp - 216 - 120) + 96 != 0) goto loc_00BE4994;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) + 48)) <= (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2660))) goto loc_00BE4831;
    result = sub_00BE7AF8(*(unsigned __int64 *)(v_rsp - 216 - 104), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) + 48)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2372)), a4);
    v_r11 = 0;
    if (result == 0) goto loc_00BE4A26;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2520)))) & (2)) != 0) goto loc_00BE4828;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2520))) & (0x10000000ULL));
    a1 = (unsigned int)(-(a1));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)) + 48))) & (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2372)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052)))) < ((unsigned int)(6 + 2))) goto loc_00BE47C2;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052))))) >> (3);
loc_00BE47B4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104)) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052))) + (-8));
    v_rbx = (*(unsigned __int64 *)(v_rsp - 216 - 104)) + (6 + 2);
    a1 = (a1) - (result + 48 - 47);
    if (condition_is_not_equal) goto loc_00BE47B4;
loc_00BE47C2:
    if ((unsigned int)(result) == 0) goto loc_00BE47D1;
loc_00BE47C6:
    *(unsigned __int8 *)(v_rbx) = 0;
    v_rbx = (v_rbx) + (result + 48 - 47);
    result = (unsigned int)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE47C6;
loc_00BE47D1:
    *(unsigned int *)(result + 2372) = (unsigned int)(a2);
    if (((unsigned int)(a2)) == 3) goto loc_00BE4810;
    if (((*(unsigned int *)(result + 2520)) & (0x8000000ULL)) != 0) goto loc_00BE4807;
    if ((unsigned int)(a2) == 0) goto loc_00BE4807;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024) - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024), result + 48 - 47);
    goto loc_00BE481F;
loc_00BE4807:
    goto loc_00BE4817;
loc_00BE4810:
loc_00BE4817:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2024), result + 48 - 47);
loc_00BE481F:
    *(unsigned int *)(result + 2372) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 2372)));
    v_r11 = 0;
loc_00BE4828:
    goto loc_00BE483A;
loc_00BE4831:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2052) = (unsigned int)(result);
loc_00BE483A:
    v_rsi = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 104) + 2052))) + ((unsigned int)(*(unsigned int *)(result + 2372)));
loc_00BE4854:
    *(unsigned __int64 *)(v_rsi) = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result + 48))) + (-8));
    result = (v_rsi) + (6 + 2);
    a2 = (1 + 5) - (1);
    if (condition_is_not_equal) goto loc_00BE4854;
    if ((unsigned int)(a1) == 0) goto loc_00BE4871;
loc_00BE4866:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (1);
    a1 = (unsigned int)((a1) + (-1));
    if (condition_is_not_equal) goto loc_00BE4866;
loc_00BE4871:
    *(unsigned int *)(v_rsi) = 13;
    *(unsigned __int64 *)(v_rsi + 8) = *(unsigned __int64 *)(v_rsp - 216 - 96);
    *(unsigned int *)(v_rsi + 16) = (unsigned int)((unsigned int)(v_stack_m188));
    if ((*(unsigned __int64 *)(v_rsp - 216 - 96)) >= (*(unsigned __int64 *)(v_rsp - 216 - 96) + (unsigned int)(v_stack_m188) * 1)) goto loc_00BE48B8;
loc_00BE48AC:
    result = (*(unsigned __int64 *)(v_rsp - 216 - 96)) + (64);
    if (result < (*(unsigned __int64 *)(v_rsp - 216 - 96) + (unsigned int)(v_stack_m188) * 1)) goto loc_00BE48AC;
loc_00BE48B8:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m188)))) >> (7));
    if ((unsigned int)(v_r11) == 0) goto loc_00BE492E;
loc_00BE48D7:
loc_00BE48DA:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 96)));
    a4 = (*(unsigned __int64 *)(v_rsp - 216 - 96)) + (6 + 2);
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (6 + 2);
    result = (6 + 2) - (1);
    if (condition_is_not_equal) goto loc_00BE48DA;
    a1 = (a4) - (*(unsigned __int64 *)(v_rsp - 216 - 96));
    a1 = (a1) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2104));
    a1 = (a1) ^ (a1);
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 2372)) + 2100))) ^ ((unsigned int)(*(unsigned __int64 *)(v_rsp - 216 - 120))));
    *(unsigned __int64 *)(v_rsp - 216 + 88) = a2;
    v_r10 = (unsigned int)((v_r10) ^ ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = 1; }
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE48D7;
loc_00BE492E:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m188)))) & (127));
    if (((unsigned int)(a2)) < ((unsigned int)(6 + 2))) goto loc_00BE4958;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00BE4944:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (6 + 2);
    a2 = (unsigned int)((a2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE4944;
loc_00BE4958:
    if ((unsigned int)(a2) == 0) goto loc_00BE4971;
loc_00BE495C:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BE495C;
loc_00BE4971:
    goto loc_00BE4979;
loc_00BE4976:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BE4979:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BE4976;
    *(unsigned int *)(v_rsi + 20) = a3;
    goto loc_00BE49A6;
loc_00BE4994:
    *(unsigned int *)(v_rsi) = 13;
loc_00BE49A6:
    if (((*(unsigned int *)(1 + 2520)) & (0x20000000ULL)) == 0) goto loc_00BE49C9;
    if ((unsigned int)((unsigned int)(v_stack_m188)) != 0) {
        a4 = v_rsi + 28;
        a3 = (unsigned int)((unsigned int)(v_stack_m188));
        a2 = *(unsigned __int64 *)(v_rsp - 216 - 96);
        a1 = 1;
        result = sub_0051AF4C(a1, a2, a3, a4);
    }
    v_r14 = 0;
    *(unsigned int *)(v_rsi + 24) = 0;
    if ((*(unsigned int *)(v_rsp - 216 - 128)) != 0) {
        *(unsigned int *)(v_rsi + 24) = 1;
    }
    if (1 == 0) goto loc_00BE4A26;
    v_stack_m190 = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 144) = 35;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 160)) < 148) goto loc_00BE4AA3;
    result = KeGuardDispatchICall(v_stack_m180, a2, a3, a4);
    if (result != 0) goto loc_00BE4A3F;
loc_00BE4A26:
loc_00BE4A2B:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 + 224)) = v_stack_m190;
    goto loc_00BE53F6;
loc_00BE4A3F:
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_m190 + 80))) + (v_stack_m180);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 184))) | (2));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 184) = (unsigned int)(a2);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 112)) < v_stack_m180) goto loc_00BE4A7F;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 112);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 112)) < a3) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 112));
        a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (4));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 168) = result;
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 184) = (unsigned int)(a1);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 120)) < v_stack_m180) goto loc_00BE4AA3;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 120);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 120)) < a3) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 152) + 120));
        a1 = (unsigned int)((a1) | ((unsigned int)(6 + 2)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 176) = result;
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 184) = (unsigned int)(a1);
    }
    v_stack_m190 = 1;
    *(unsigned __int64 *)(v_rsp - 216 - 104) = 1;
    if (((*(unsigned int *)(1 + 2520)) & (0x200000ULL)) == 0) goto loc_00BE5E45;
    result = KeGuardDispatchICall(v_stack_m180, a2, a3, a4);
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp - 216 - 112) = result;
    if (result != 0) goto loc_00BE4AE4;
loc_00BE4ADA:
    goto loc_00BE53D3;
loc_00BE4AE4:
    *(unsigned __int16 *)(v_rsp - 216 + 248) = (unsigned __int16)(*(unsigned __int16 *)(result + 6));
    a4 = (a2) >> (3);
    *(unsigned __int64 *)(v_rsp - 216 - 96) = a4;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 6)) != 0) goto loc_00BE4C36;
    if (condition_is_above_or_equal) goto loc_00BE5F85;
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE4ADA;
    *(unsigned __int64 *)(1 + 2344) = 0;
    result = (result) + (1);
    *(unsigned __int64 *)(1 + 2352) = 271;
    *(unsigned __int64 *)(1 + 2336) = result;
    *(unsigned __int64 *)(1 + 2360) = v_stack_m180;
    *(unsigned int *)(1 + 2328) = 1;
    if (condition_is_below) goto loc_00BE4ADA;
    if (((*(unsigned int *)(1 + 2524)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 2520))))) == 0) goto loc_00BE4ADA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE4BD6;
loc_00BE4BB6:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1)) ^ (*(unsigned __int64 *)(1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1) + (6 + 2);
loc_00BE4BD6:
    if (a2 != ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8)) goto loc_00BE4BB6;
    if (a3 == (*(unsigned __int64 *)(1 + 2688))) goto loc_00BE4ADA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416)) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(1 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052)));
    result = *(unsigned __int64 *)(1 + 1416);
    if ((*(unsigned int *)(1 + 2328)) == 0) {
        result = *(unsigned __int64 *)(1 + 1416);
        a1 = (*(unsigned __int64 *)(1 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
loc_00BE4C24:
    a2 = 0;
    result = sub_00BE8384(1, a2, a3, 256);
    goto loc_00BE4ADA;
loc_00BE4C36:
    v_r11 = (*(unsigned __int16 *)(result + 20)) + (24);
    v_r11 = (v_r11) + (result);
    *(unsigned __int64 *)(v_rsp - 216 - 120) = v_r11;
    a2 = 0;
    v_stack_m170 = v_stack_m168 + 256 + 256 * 2 * 4;
    v_stack_m188 = 0;
    if ((unsigned __int16)(*(unsigned __int64 *)(1 + 2104)) == 0) goto loc_00BE5261;
    *(unsigned __int64 *)(v_rsp - 216 - 128) = v_r11 + 8;
    v_r14 = 0;
loc_00BE4C8B:
    v_r13 = (unsigned int)(*(unsigned int *)(v_r11 + 8 + 8));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 8)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8))))) { v_r13 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8))); }
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 4)));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 4)))));
    if (0 == 0) goto loc_00BE4CBE;
    if (((unsigned int)(v_r13)) < (*(unsigned int *)(v_r11 + 0 - 1 + 0 - 1 * 4 * 8 + 12))) goto loc_00BE503B;
loc_00BE4CBE:
    if (v_stack_m168 == (v_stack_m168 + 256 + 256 * 2 * 4)) goto loc_00BE5007;
loc_00BE4CC7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168)))) >= ((unsigned int)(v_r13))) goto loc_00BE4FF2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168 + 4)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 4))))) goto loc_00BE4FF2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 4))))) goto loc_00BE514F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168 + 4)))) > ((unsigned int)(v_r13))) goto loc_00BE514F;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m168 + 8))))) != 0) goto loc_00BE4D0D;
    if (((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_m168 + 8)) + v_stack_m180 * 1)) & (32)) == 0) goto loc_00BE4FE3;
loc_00BE4D0D:
    v_rsi = (unsigned int)(*(unsigned int *)(v_r11 + 8 + 8));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 8)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8))))) { v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8))); }
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 4)))));
    result = KeGuardDispatchICall(v_stack_m168, v_stack_m180, (unsigned int)(*(unsigned int *)(v_r11 + 8 + 4)), v_stack_m168 + 256 + 256 * 2 * 4);
    if ((*(unsigned int *)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 4))))) goto loc_00BE4D43;
    if ((*(unsigned int *)(result + 4)) <= ((unsigned int)(v_rsi))) goto loc_00BE4E6F;
loc_00BE4D43:
    result = (unsigned int)((result) - ((unsigned int)(v_stack_m180)));
    result = (unsigned int)((result) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (condition_is_above_or_equal) goto loc_00BE6001;
    v_r11 = 0;
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE4E6F;
    *(unsigned __int64 *)(1 + 2344) = 0;
    result = (result) + (1);
    *(unsigned __int64 *)(1 + 2352) = 271;
    *(unsigned __int64 *)(1 + 2336) = result;
    *(unsigned __int64 *)(1 + 2360) = v_stack_m180;
    *(unsigned int *)(1 + 2328) = (unsigned int)(v_r11 + 1);
    if (condition_is_below) goto loc_00BE4E6F;
    if (((*(unsigned int *)(1 + 2524)) & (0x200000ULL)) == 0) goto loc_00BE4E6F;
    if ((((unsigned __int8)(v_r11 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 2520))))) == 0) goto loc_00BE4E6F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE4E18;
loc_00BE4DF7:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1)) ^ (*(unsigned __int64 *)(1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1) + (8);
loc_00BE4E18:
    if (a2 != ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8)) goto loc_00BE4DF7;
    if (a3 == (*(unsigned __int64 *)(1 + 2688))) goto loc_00BE4E6F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416)) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(1 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052)));
    result = *(unsigned __int64 *)(1 + 1416);
    if ((*(unsigned int *)(1 + 2328)) == 0) {
        result = *(unsigned __int64 *)(1 + 1416);
        a1 = (*(unsigned __int64 *)(1 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(1, a2, a3, 256);
loc_00BE4E6F:
    a3 = ((unsigned int)(*(unsigned int *)(result))) + (v_stack_m180);
    result = KeGuardDispatchICall(result, v_stack_m180, a3, 256);
    if ((*(unsigned int *)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 8 + 4))))) goto loc_00BE4E99;
    if ((*(unsigned int *)(result + 4)) <= ((unsigned int)(v_rsi))) goto loc_00BE4FC8;
loc_00BE4E99:
    result = (unsigned int)((result) - ((unsigned int)(v_stack_m180)));
    result = (unsigned int)((result) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    if (condition_is_above_or_equal) goto loc_00BE5FD8;
    v_r14 = 0;
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE4FDA;
    *(unsigned __int64 *)(1 + 2344) = 0;
    *(unsigned __int64 *)(1 + 2336) = 1 + v_rsi * 1;
    *(unsigned int *)(1 + 2328) = (unsigned int)(v_r14 + 1);
    *(unsigned __int64 *)(1 + 2352) = 271;
    *(unsigned __int64 *)(1 + 2360) = v_stack_m180;
    if ((*(unsigned int *)(1 + 2328)) < 0) goto loc_00BE4FDA;
    if (((*(unsigned int *)(1 + 2524)) & (0x200000ULL)) == 0) goto loc_00BE4FDA;
    if ((((unsigned __int8)(v_r14 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 2520))))) == 0) goto loc_00BE4FDA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE4F6F;
loc_00BE4F4E:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1)) ^ (*(unsigned __int64 *)(1 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1) + (8);
loc_00BE4F6F:
    if (a2 != ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8)) goto loc_00BE4F4E;
    if (a3 == (*(unsigned __int64 *)(1 + 2688))) goto loc_00BE4FDA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416)) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(1 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052)));
    result = *(unsigned __int64 *)(1 + 1416);
    if ((*(unsigned int *)(1 + 2328)) == 0) {
        result = *(unsigned __int64 *)(1 + 1416);
        a1 = (*(unsigned __int64 *)(1 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(1, a2, a3, 256);
    goto loc_00BE4FDA;
loc_00BE4FC8:
    v_r14 = 0;
loc_00BE4FDA:
loc_00BE4FE3:
    v_r12 = (v_stack_m168) + (12);
    if (v_r12 != v_stack_m170) goto loc_00BE4CC7;
loc_00BE4FF2:
loc_00BE5007:
    a2 = (*(unsigned __int64 *)(v_rsp - 216 - 128)) + (40);
    *(unsigned __int64 *)(v_rsp - 216 - 128) = a2;
    a1 = (unsigned int)(((unsigned int)(v_stack_m188)) + (1));
    v_stack_m188 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248))))) goto loc_00BE4C8B;
    a2 = 0;
    goto loc_00BE5267;
loc_00BE503B:
    if (condition_is_above_or_equal) goto loc_00BE5FAD;
    v_r12 = 0;
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE4ADA;
    *(unsigned __int64 *)(1 + 2344) = 0;
    *(unsigned __int64 *)(1 + 2336) = 1 + v_rsi * 1;
    *(unsigned int *)(1 + 2328) = (unsigned int)(v_r12 + 1);
    *(unsigned __int64 *)(1 + 2352) = 271;
    *(unsigned __int64 *)(1 + 2360) = v_stack_m180;
    if ((*(unsigned int *)(1 + 2328)) < 0) goto loc_00BE4ADA;
    if (((*(unsigned int *)(1 + 2524)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 2520))))) == 0) goto loc_00BE4ADA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE50F9;
loc_00BE50D8:
    result = (*(unsigned __int64 *)(1 + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1) + (8);
loc_00BE50F9:
    if (a4 != ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8)) goto loc_00BE50D8;
    if (a3 == (*(unsigned __int64 *)(1 + 2688))) goto loc_00BE4ADA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416)) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(1 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052)));
    result = *(unsigned __int64 *)(1 + 2688);
    if ((*(unsigned int *)(1 + 2328)) == 0) {
        a2 = a3;
        a2 = (a2) ^ (*(unsigned __int64 *)(1 + 2688));
        result = *(unsigned __int64 *)(1 + 1416);
        *(unsigned __int64 *)(result + 24) = a2;
    }
    goto loc_00BE4C24;
loc_00BE514F:
    if (condition_is_above_or_equal) goto loc_00BE6027;
    v_r12 = 0;
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE4ADA;
    *(unsigned __int64 *)(1 + 2344) = 0;
    *(unsigned __int64 *)(1 + 2336) = 1 + v_rsi * 1;
    *(unsigned int *)(1 + 2328) = (unsigned int)(v_r12 + 1);
    *(unsigned __int64 *)(1 + 2352) = 271;
    *(unsigned __int64 *)(1 + 2360) = v_stack_m180;
    if ((*(unsigned int *)(1 + 2328)) < 0) goto loc_00BE4ADA;
    if (((*(unsigned int *)(1 + 2524)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 2520))))) == 0) goto loc_00BE4ADA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE520D;
loc_00BE51EC:
    result = (*(unsigned __int64 *)(1 + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1) + (8);
loc_00BE520D:
    if (a4 != ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8)) goto loc_00BE51EC;
    if (a3 == (*(unsigned __int64 *)(1 + 2688))) goto loc_00BE4ADA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416)) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(1 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052)));
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE5147;
loc_00BE5255:
    a1 = (*(unsigned __int64 *)(1 + 2688)) ^ (a3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416) + 24) = a1;
    goto loc_00BE5147;
loc_00BE5261:
loc_00BE5267:
    if (0 == v_stack_m170) goto loc_00BE537C;
    if (0 >= v_stack_m170) goto loc_00BE6052;
    v_r12 = 0;
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE4ADA;
    *(unsigned __int64 *)(1 + 2344) = 0;
    *(unsigned __int64 *)(1 + 2336) = 1 + v_rsi * 1;
    *(unsigned __int64 *)(1 + 2352) = 271;
    *(unsigned __int64 *)(1 + 2360) = v_stack_m180;
    *(unsigned int *)(1 + 2328) = 1;
    if ((*(unsigned int *)(1 + 2328)) < 0) goto loc_00BE4ADA;
    if (((*(unsigned int *)(1 + 2524)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 2520))))) == 0) goto loc_00BE4ADA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE532F;
loc_00BE530F:
    result = (*(unsigned __int64 *)(1 + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(1 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(1 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1) + (1 + 7);
loc_00BE532F:
    if (a4 != ((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8)) goto loc_00BE530F;
    if (a3 == (*(unsigned __int64 *)(1 + 2688))) goto loc_00BE4ADA;
    *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416)) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(1 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052)));
    if ((*(unsigned int *)(1 + 2328)) != 0) goto loc_00BE5147;
    goto loc_00BE5255;
loc_00BE537C:
    v_r12 = 0;
    if ((unsigned int)(a4) == 0) goto loc_00BE538D;
    a2 = (unsigned int)((a4 + 6) & (0xFFFFFFF8ULL));
    goto loc_00BE5390;
loc_00BE538D:
loc_00BE5390:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052)) + 48) + ((unsigned int)(0 + (unsigned __int16)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8) + (unsigned __int16)((unsigned int)(*(unsigned int *)(1 + 2676)) + 1 * 1 + a1 * 8) * 2 * 8)));
    if (((unsigned int)(a1)) <= (*(unsigned int *)(1 + 2660))) goto loc_00BE54C5;
    result = sub_00BE7AF8(1, (unsigned int)((unsigned int)(a1)), (unsigned int)(*(unsigned int *)(1 + 2372)), a4);
    *(unsigned __int64 *)(v_rsp - 216 - 112) = result;
    if (result != 0) goto loc_00BE53FD;
loc_00BE53D3:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 + 224)) = v_stack_m190;
    if (!sign_flag) goto loc_00BE5E57;
loc_00BE53EA:
    if (((unsigned int)((unsigned int)(0xC000009AULL))) == 0xC000010EULL) goto loc_00BE5E57;
loc_00BE53F6:
    goto loc_00BE5EF0;
loc_00BE53FD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 2520)))) & (2)) != 0) goto loc_00BE54AB;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2520))) & (0x10000000ULL));
    a1 = (unsigned int)(-(a1));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (*(unsigned int *)(1 + 2372)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052)))) < ((unsigned int)(1 + 7))) goto loc_00BE5448;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1 + 2052))))) >> (3);
loc_00BE543A:
    *(unsigned __int64 *)(1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 2052))) + (-8));
    v_rbx = (1) + (1 + 7);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00BE543A;
loc_00BE5448:
    if ((unsigned int)(result) == 0) goto loc_00BE5457;
loc_00BE544C:
    *(unsigned __int8 *)(v_rbx) = 0;
    v_rbx = (v_rbx) + (1);
    result = (unsigned int)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE544C;
loc_00BE5457:
    *(unsigned int *)(v_stack_m190 + 2372) = (unsigned int)(a2);
    if (((unsigned int)(a2)) == 3) goto loc_00BE5496;
    if (((*(unsigned int *)(v_stack_m190 + 2520)) & (0x8000000ULL)) != 0) goto loc_00BE548D;
    if ((unsigned int)(a2) == 0) goto loc_00BE548D;
    result = KeGuardDispatchICall(*(unsigned __int64 *)(1 + 2024) - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 2024) - 8), *(unsigned __int64 *)(1 + 2024), 1);
    goto loc_00BE54A5;
loc_00BE548D:
    goto loc_00BE549D;
loc_00BE5496:
loc_00BE549D:
    result = KeGuardDispatchICall(*(unsigned __int64 *)(1 + 2024), *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 2024) - 8), *(unsigned __int64 *)(1 + 2024), 1);
loc_00BE54A5:
    *(unsigned int *)(v_stack_m190 + 2372) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)));
loc_00BE54AB:
    goto loc_00BE54D2;
loc_00BE54C5:
    *(unsigned __int64 *)(v_rsp - 216 - 112) = (unsigned int)(*(unsigned int *)(v_stack_m190 + 2372));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2052) = (unsigned int)(*(unsigned __int64 *)(1 + 2024));
loc_00BE54D2:
loc_00BE54F0:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1) = 0;
    a3 = (unsigned int)((6 + 42) + (-8));
    result = ((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1) + (1 + 7);
    a2 = (6) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE54F0;
    if (a3 == 0) goto loc_00BE5510;
loc_00BE5504:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (6 - 5);
    a3 = (unsigned int)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BE5504;
loc_00BE5510:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1 + 8) = v_stack_m168;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1) = 30;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1 + 16) = 0;
    goto loc_00BE5531;
loc_00BE552F:
    a2 = (unsigned int)((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2104)) ^ ((unsigned int)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2104))));
loc_00BE5531:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2104)) >> (31);
    if (result != 0) goto loc_00BE552F;
    *(unsigned __int64 *)(v_rsp - 216 - 104) = (unsigned int)(*(unsigned int *)(v_stack_m190 + 2372));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1 + 20) = (unsigned int)(a2);
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1 + 24) = v_stack_m180;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 80)));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1 + 36) = (unsigned int)((unsigned int)(v_stack_m160));
    *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1 + 40) = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248));
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + *(unsigned __int64 *)(v_rsp - 216 + 224) * 1) + (48);
    v_stack_m160 = a1;
    if ((unsigned int)(*(unsigned __int64 *)(v_rsp - 216 - 96)) == 0) goto loc_00BE557B;
    v_r14 = (*(unsigned __int64 *)(v_rsp - 216 - 96) - 1) + (7);
    v_r14 = (v_r14) & (-8);
    v_r14 = (v_r14) + (a1);
    goto loc_00BE557E;
loc_00BE557B:
loc_00BE557E:
    v_stack_m188 = a1;
    *(unsigned __int64 *)(v_rsp - 216 - 96) = a1 + (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248)) + (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248)) * 2 * 8;
    if ((unsigned int)(*(unsigned __int64 *)(v_rsp - 216 - 96)) == 0) goto loc_00BE55A3;
    v_stack_m178 = v_stack_m168 + 12;
    goto loc_00BE55A8;
loc_00BE55A3:
    v_stack_m178 = v_stack_m170;
loc_00BE55A8:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248)))) goto loc_00BE55D3;
loc_00BE55B6:
loc_00BE55BB:
    *(unsigned __int64 *)(a1 + 8 - 8) = 0;
    *(unsigned int *)(a1 + 8) = 0x80000000ULL;
    result = (a1 + 8) + (12);
    a1 = (2) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE55BB;
    a2 = ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248))) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE55B6;
loc_00BE55D3:
    if (a1 == (a1 + (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248)) + (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 216 + 248)) * 2 * 8)) goto loc_00BE5E48;
    v_r11 = 0;
loc_00BE55E3:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 36)) & (0x2000000ULL)) != 0) goto loc_00BE5633;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120))))) != 0x54494E49ULL) goto loc_00BE560A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 4)) == 0x4742444BULL) goto loc_00BE5633;
loc_00BE560A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120))))) != 0x45474150ULL) goto loc_00BE563B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 4))) == ((unsigned __int16)((unsigned int)(0x7877ULL)))) goto loc_00BE5633;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 4))) == ((unsigned __int16)((unsigned int)(0x7277ULL)))) goto loc_00BE5633;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 4))) != ((unsigned __int16)((unsigned int)(0x7777ULL)))) goto loc_00BE564D;
loc_00BE5633:
    goto loc_00BE571E;
loc_00BE563B:
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 4))) != 0x41525245ULL) goto loc_00BE564D;
    if ((*(unsigned __int16 *)((unsigned int)(0x7777ULL))) == ((unsigned __int16)((unsigned int)(0x4154ULL)))) goto loc_00BE5633;
loc_00BE564D:
    a3 = (*(unsigned __int64 *)(v_rsp - 216 - 120)) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2384));
loc_00BE5675:
    a2 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2384)) + (6 - 5);
    if (((unsigned __int8)(*(unsigned __int8 *)(a3 + *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2384) * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2384))))) goto loc_00BE568D;
    v_r11 = (unsigned int)((7) + (-1));
    if (condition_is_not_equal) goto loc_00BE5675;
    goto loc_00BE5713;
loc_00BE568D:
loc_00BE5695:
    a3 = (*(unsigned __int64 *)(v_rsp - 216 - 120)) + (8);
    a4 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2392)) + (8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 120))) != (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2392)))) goto loc_00BE56CE;
    a2 = (unsigned int)((8) + (-8));
    if (((unsigned int)(a2)) >= 8) goto loc_00BE5695;
    v_r11 = 0;
    if ((unsigned int)(a2) == 0) goto loc_00BE5713;
loc_00BE56B7:
    a3 = (a3) + (6 - 5);
    a4 = (a4) + (6 - 5);
    if (((unsigned __int8)(*(unsigned __int8 *)(a3))) != ((unsigned __int8)(*(unsigned __int8 *)(a4)))) goto loc_00BE56D1;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BE56B7;
    goto loc_00BE5713;
loc_00BE56CE:
    v_r11 = 0;
loc_00BE56D1:
    a2 = (*(unsigned __int64 *)(v_rsp - 216 - 120)) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2400));
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
loc_00BE56E1:
    v_r10 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2400)) + (6 - 5);
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2400) * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2400))))) goto loc_00BE56F6;
    a3 = (unsigned int)((4) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00BE56E1;
    goto loc_00BE5713;
loc_00BE56F6:
    a2 = (*(unsigned __int64 *)(v_rsp - 216 - 120)) - (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2408));
loc_00BE5702:
    v_rbx = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2408)) + (6 - 5);
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2408) * 1))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2408))))) goto loc_00BE5719;
    a3 = (unsigned int)((6) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00BE5702;
loc_00BE5713:
    v_r11 = 0;
loc_00BE5719:
loc_00BE571E:
    if (!sign_flag) goto loc_00BE572C;
    goto loc_00BE5731;
loc_00BE572C:
    if ((unsigned int)((unsigned int)((unsigned int)(6 - 5))) == 0) goto loc_00BE5754;
loc_00BE5731:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120))) != 0x54494E49ULL) goto loc_00BE5754;
    v_r13 = (unsigned int)((unsigned int)(6 - 5));
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 4)) == 0x4742444BULL) {
        v_r13 = (unsigned int)((unsigned int)(6 - 5));
        if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2524)) & (0x2000ULL)) != 0) { v_r13 = 0; }
    }
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2524)) & (0x4000ULL)) == 0) goto loc_00BE577B;
    if (condition_is_above_or_equal) goto loc_00BE577B;
    if (v_stack_m180 == (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 1504))) goto loc_00BE5778;
    if (v_stack_m180 == (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 1512))) {
        v_r13 = (unsigned int)(6 - 5);
    }
    v_rsi = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 16));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 16)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 8))))) { v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 8))); }
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 12)))));
    *(unsigned int *)(v_rsp - 216 - 128) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 12)));
    *(unsigned int *)(v_rsp - 216 + 248) = (unsigned int)(v_rsi);
    if (v_stack_m168 == v_stack_m170) goto loc_00BE5927;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 12))))) goto loc_00BE592F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168 + 4)))) > ((unsigned int)(v_rsi))) goto loc_00BE5944;
    if ((unsigned int)(v_r13) != 0) goto loc_00BE5956;
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168)));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 12)))));
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 12)));
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 120) + 12))))) + (v_stack_m180);
    v_rbx = ((unsigned int)((unsigned int)(a4))) + (v_r11);
    result = 0;
loc_00BE57F7:
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 216 - 40))) + (*(unsigned __int64 *)(v_rsp - 216));
    if (v_r11 >= result) goto loc_00BE580D;
    if (v_rbx > (*(unsigned __int64 *)(v_rsp - 216))) goto loc_00BE5937;
loc_00BE580D:
    v_r10 = (unsigned int)((0) + 1);
    a3 = (v_rsp - 216) + (8);
    a2 = (v_rsp - 216 - 40) + (4);
    if (((unsigned int)(v_r10)) < 6) goto loc_00BE57F7;
    a1 = ((unsigned int)((unsigned int)(a4))) + (v_r11);
    if (v_r11 >= a1) goto loc_00BE584F;
loc_00BE5843:
    result = (v_r11) + (64);
    if (result < a1) goto loc_00BE5843;
loc_00BE584F:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (7));
    if ((unsigned int)(v_rbx) == 0) goto loc_00BE58BD;
loc_00BE586B:
loc_00BE5870:
    a3 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2104)) ^ (*(unsigned __int64 *)(v_r11));
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r11 + 8));
    v_r10 = (v_r11) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE5870;
    a1 = (v_r10) - (v_r11);
    a1 = (a1) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2104));
    a1 = (a1) ^ (a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372))) ^ (1));
    *(unsigned __int64 *)(v_rsp - 216 + 96) = 1;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m190 + 2372)) + 2100))) ^ ((unsigned int)(result)));
    v_rsi = (unsigned int)((v_rsi) & (63));
    if (condition_is_equal) { v_rsi = 1; }
    v_rbx = (unsigned int)((v_rbx) + (-1));
    if (condition_is_not_equal) goto loc_00BE586B;
loc_00BE58BD:
    a4 = (unsigned int)((a4) & (127));
    if (((unsigned int)(a4)) < 8) goto loc_00BE58E3;
    result = ((unsigned int)((unsigned int)(a4))) >> (3);
loc_00BE58CE:
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r10));
    v_r10 = (v_r10) + (8);
    a4 = (unsigned int)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE58CE;
loc_00BE58E3:
    v_r11 = 0;
    if ((unsigned int)(a4) == 0) goto loc_00BE5900;
loc_00BE58EB:
    a3 = (a3) ^ (*(unsigned __int8 *)(v_r10));
    v_r10 = (v_r10) + (1);
    a4 = (unsigned int)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE58EB;
loc_00BE5900:
    goto loc_00BE5908;
loc_00BE5905:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BE5908:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BE5905;
    *(unsigned int *)(v_stack_m188 + 8) = a3;
    goto loc_00BE593A;
loc_00BE5927:
loc_00BE592F:
    if (0 < 1) goto loc_00BE5C60;
    goto loc_00BE5944;
loc_00BE5937:
    v_r11 = 0;
loc_00BE593A:
loc_00BE5944:
    if (0 > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248))))) goto loc_00BE5C60;
    if (v_stack_m168 == v_stack_m170) goto loc_00BE5C60;
loc_00BE5956:
    if (v_stack_m178 == v_stack_m170) goto loc_00BE5C60;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178 + 4)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248))))) goto loc_00BE5C60;
loc_00BE597B:
    if (v_stack_m178 == v_stack_m170) goto loc_00BE5C60;
    if ((unsigned int)(v_r13) == 0) goto loc_00BE5991;
    goto loc_00BE5C27;
loc_00BE5991:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168 + 4))))) goto loc_00BE5ABC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168 + 4))))) goto loc_00BE607D;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2328)) != 0) goto loc_00BE5ABC;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2344) = 0;
    result = (v_stack_m160) + (*(unsigned __int64 *)(v_rsp - 216 - 112));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2352) = 271;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2336) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2360) = v_stack_m180;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2328) = 1;
    if (condition_is_below) goto loc_00BE5ABC;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2524)) & (0x200000ULL)) == 0) goto loc_00BE5ABC;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2520))))) == 0) goto loc_00BE5ABC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE5A64;
loc_00BE5A43:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2104)) ^ (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2676)) + *(unsigned __int64 *)(v_rsp - 216 - 112) * 1));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a4 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2676)) + *(unsigned __int64 *)(v_rsp - 216 - 112) * 1) + (8);
loc_00BE5A64:
    if (a4 != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2676)) + *(unsigned __int64 *)(v_rsp - 216 - 112) * 1 + a1 * 8)) goto loc_00BE5A43;
    if (a3 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2688))) goto loc_00BE5ABC;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 1416)) = *(unsigned __int64 *)(v_rsp - 216 - 112);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2052)));
    result = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2328)) == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 1416);
        a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(*(unsigned __int64 *)(v_rsp - 216 - 112), a2, a3, 256);
loc_00BE5ABC:
    v_r11 = ((unsigned int)(*(unsigned int *)(v_stack_m168 + 4))) + (v_stack_m180);
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m168 + 4)))));
    v_rbx = ((unsigned int)((unsigned int)(a4))) + (v_r11);
    result = 0;
loc_00BE5ADD:
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 216 - 40))) + (*(unsigned __int64 *)(v_rsp - 216));
    if (v_r11 >= result) goto loc_00BE5AF3;
    if (v_rbx > (*(unsigned __int64 *)(v_rsp - 216))) goto loc_00BE5C12;
loc_00BE5AF3:
    v_r10 = (unsigned int)((0) + 1);
    a3 = (v_rsp - 216) + (8);
    a2 = (v_rsp - 216 - 40) + (4);
    if (((unsigned int)(v_r10)) < 6) goto loc_00BE5ADD;
    if (((unsigned int)(a4)) < 4) goto loc_00BE5C12;
    a1 = ((unsigned int)((unsigned int)(a4))) + (v_r11);
    if (v_r11 >= a1) goto loc_00BE5B3F;
loc_00BE5B33:
    result = (v_r11) + (64);
    if (result < a1) goto loc_00BE5B33;
loc_00BE5B3F:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (7));
    if ((unsigned int)(v_rbx) == 0) goto loc_00BE5BAD;
loc_00BE5B5B:
loc_00BE5B60:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2104)) ^ (*(unsigned __int64 *)(v_r11));
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r11 + 8));
    v_r10 = (v_r11) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE5B60;
    a1 = (v_r10) - (v_r11);
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2104));
    a1 = (a1) ^ (a1);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2100))) ^ ((unsigned int)(*(unsigned __int64 *)(v_rsp - 216 - 112))));
    *(unsigned __int64 *)(v_rsp - 216 + 104) = 1;
    v_rsi = (unsigned int)((v_rsi) ^ (1));
    v_rsi = (unsigned int)((v_rsi) & (63));
    if (condition_is_equal) { v_rsi = 1; }
    v_rbx = (unsigned int)((v_rbx) + (-1));
    if (condition_is_not_equal) goto loc_00BE5B5B;
loc_00BE5BAD:
    a4 = (unsigned int)((a4) & (127));
    if (((unsigned int)(a4)) < 8) goto loc_00BE5BD3;
    result = ((unsigned int)((unsigned int)(a4))) >> (3);
loc_00BE5BBE:
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r10));
    v_r10 = (v_r10) + (8);
    a4 = (unsigned int)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE5BBE;
loc_00BE5BD3:
    v_r11 = 0;
    if ((unsigned int)(a4) == 0) goto loc_00BE5BF0;
loc_00BE5BDB:
    a3 = (a3) ^ (*(unsigned __int8 *)(v_r10));
    v_r10 = (v_r10) + (1);
    a4 = (unsigned int)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE5BDB;
loc_00BE5BF0:
    goto loc_00BE5BF8;
loc_00BE5BF5:
    a3 = (unsigned __int8)((a3) ^ ((unsigned __int8)(a3)));
loc_00BE5BF8:
    result = (a3) >> (7);
    if (result != 0) goto loc_00BE5BF5;
    a3 = (unsigned __int8)((a3) & (127));
    goto loc_00BE5C18;
loc_00BE5C12:
    v_r11 = 0;
loc_00BE5C18:
loc_00BE5C27:
    *(unsigned __int8 *)(v_stack_m160) = 128;
    v_rbx = (v_stack_m168) + (12);
    v_r14 = (v_stack_m178) + (12);
    result = (v_stack_m160) + (1);
    v_stack_m168 = v_rbx;
    v_stack_m160 = result;
    v_stack_m178 = v_r14;
    v_r15 = (unsigned int)(*(unsigned int *)(v_stack_m178 + 4));
    if (v_r14 != v_stack_m170) {
        v_r15 = *(unsigned int *)(v_r14 + 4);
    }
    if (((unsigned int)(v_r15)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248))))) goto loc_00BE597B;
loc_00BE5C60:
    if ((unsigned int)(v_r13) != 0) goto loc_00BE5DDA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248))))) goto loc_00BE5DDA;
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178))))) + (v_stack_m180);
    *(unsigned int *)(v_stack_m188 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178)));
    *(unsigned int *)(v_stack_m188 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248)));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m178)))));
    v_rbx = ((unsigned int)((unsigned int)(a4))) + (v_r11);
    v_r13 = 0;
loc_00BE5CA8:
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 216 - 40))) + (*(unsigned __int64 *)(v_rsp - 216));
    if (v_r11 >= result) goto loc_00BE5CBE;
    if (v_rbx > (*(unsigned __int64 *)(v_rsp - 216))) goto loc_00BE5DD2;
loc_00BE5CBE:
    a3 = (unsigned int)((0) + 1);
    a2 = (v_rsp - 216) + (v_r13 + 8);
    a1 = (v_rsp - 216 - 40) + (4);
    if (a3 < 6) goto loc_00BE5CA8;
    a1 = ((unsigned int)((unsigned int)(a4))) + (v_r11);
    if (v_r11 >= a1) goto loc_00BE5CFF;
loc_00BE5CF3:
    result = (v_r11) + (64);
    if (result < a1) goto loc_00BE5CF3;
loc_00BE5CFF:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (7));
    if ((unsigned int)(v_rbx) == 0) goto loc_00BE5D6A;
loc_00BE5D1C:
loc_00BE5D1F:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2104)) ^ (*(unsigned __int64 *)(v_r11));
    v_r10 = (v_r11) + (v_r13 + 8);
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r10));
    v_r10 = (v_r10) + (v_r13 + 8);
    result = (v_r13 + 8) - (1);
    if (condition_is_not_equal) goto loc_00BE5D1F;
    a1 = (v_r10) - (v_r11);
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2104));
    a1 = (a1) ^ (a1);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 216 - 112) + 2100))) ^ ((unsigned int)(v_stack_m180)));
    *(unsigned __int64 *)(v_rsp - 216 + 112) = a2;
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(a2)));
    v_rsi = (unsigned int)((v_rsi) & (63));
    if (condition_is_equal) { v_rsi = 1; }
    v_rbx = (unsigned int)((v_rbx) + (-1));
    if (condition_is_not_equal) goto loc_00BE5D1C;
loc_00BE5D6A:
    a4 = (unsigned int)((a4) & (127));
    if (((unsigned int)(a4)) < ((unsigned int)(v_r13 + 8))) goto loc_00BE5D8E;
    result = ((unsigned int)((unsigned int)(a4))) >> (3);
loc_00BE5D7A:
    a3 = (a3) ^ (*(unsigned __int64 *)(v_r10));
    v_r10 = (v_r10) + (v_r13 + 8);
    a4 = (unsigned int)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE5D7A;
loc_00BE5D8E:
    v_r11 = 0;
    if ((unsigned int)(a4) == 0) goto loc_00BE5DAB;
loc_00BE5D96:
    a3 = (a3) ^ (*(unsigned __int8 *)(v_r10));
    v_r10 = (v_r10) + (1);
    a4 = (unsigned int)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE5D96;
loc_00BE5DAB:
    goto loc_00BE5DB3;
loc_00BE5DB0:
    a3 = (unsigned int)((a3) ^ (a3));
loc_00BE5DB3:
    result = (a3) >> (31);
    if (result != 0) goto loc_00BE5DB0;
    *(unsigned int *)(v_stack_m188 + 20) = a3;
    goto loc_00BE5DD5;
loc_00BE5DD2:
    v_r11 = 0;
loc_00BE5DD5:
loc_00BE5DDA:
    if (v_stack_m168 == v_stack_m170) goto loc_00BE5E1C;
    if ((*(unsigned int *)(v_stack_m168)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 - 128))))) goto loc_00BE5E1C;
    if ((*(unsigned int *)(v_stack_m168 + 4)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 216 + 248))))) goto loc_00BE5E1C;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 216 - 128));
    if (v_stack_m178 != v_stack_m170) {
        result = v_stack_m160;
        *(unsigned __int8 *)(result) = 128;
        result = (result) + 1;
        a3 = (v_stack_m178) + (12);
        v_stack_m160 = result;
        v_stack_m178 = a3;
    }
    v_rbx = (v_stack_m168) + (12);
    v_stack_m168 = v_rbx;
loc_00BE5E1C:
    v_r14 = (v_stack_m188) + (24);
    v_r12 = (*(unsigned __int64 *)(v_rsp - 216 - 120)) + (40);
    v_stack_m188 = v_r14;
    *(unsigned __int64 *)(v_rsp - 216 - 120) = v_r12;
    if (v_r14 == (*(unsigned __int64 *)(v_rsp - 216 - 96))) goto loc_00BE5E41;
    goto loc_00BE55E3;
loc_00BE5E41:
loc_00BE5E45:
    v_r12 = 0;
loc_00BE5E48:
    v_stack_m190 = *(unsigned __int64 *)(v_rsp - 216 - 104);
loc_00BE5E4D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 + 224)) = *(unsigned __int64 *)(v_rsp - 216 - 104);
loc_00BE5E57:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 216 + 240))) & (0xFFFFFFEFULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & ((unsigned int)((unsigned int)(0x80000004ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000004ULL)))) goto loc_00BE5EEE;
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)((unsigned int)(0x80000000ULL))));
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_rsp - 216 - 16), a2, a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 148)))) < 20) goto loc_00BE5EEE;
    v_rdi = ((unsigned int)(*(unsigned int *)(result + 144)) + (unsigned int)(*(unsigned int *)(result + 148)) * 1) + (*(unsigned __int64 *)(v_rsp - 216 - 16));
    goto loc_00BE5EE9;
loc_00BE5EAA:
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 144)) + *(unsigned __int64 *)(v_rsp - 216 - 16) * 1 + 12)) == 0) goto loc_00BE5EEE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 144)) + *(unsigned __int64 *)(v_rsp - 216 - 16) * 1 + 16))) == 0) goto loc_00BE5EEE;
    if (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 144)) + *(unsigned __int64 *)(v_rsp - 216 - 16) * 1 + 16)) + *(unsigned __int64 *)(v_rsp - 216 - 16) * 1) == 0) goto loc_00BE5EE5;
    result = sub_00BE3A04(v_stack_m190, *(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 144)) + *(unsigned __int64 *)(v_rsp - 216 - 16) * 1 + 16)) + *(unsigned __int64 *)(v_rsp - 216 - 16) * 1), (unsigned int)((unsigned int)(v_r14)), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 216 + 224)) = v_stack_m190;
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00BE5EE5;
    if (((unsigned int)(result)) != 0xC000010EULL) goto loc_00BE5EF0;
loc_00BE5EE5:
    v_rbx = ((unsigned int)(*(unsigned int *)(result + 144)) + *(unsigned __int64 *)(v_rsp - 216 - 16) * 1) + (20);
loc_00BE5EE9:
    if (v_rbx != v_rdi) goto loc_00BE5EAA;
loc_00BE5EEE:
    result = 0;
loc_00BE5EF0:
    v_rsp = (v_rsp) + (408);
    return result;
loc_00BE5F05:
    v_stack_p20 = (unsigned int)((unsigned int)(v_r14));
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), 5 + 5, *(unsigned __int64 *)(v_rsp - 216 + 224), 5);
loc_00BE5F30:
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 216 + 224);
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), 5 + 5, *(unsigned __int64 *)(v_rsp - 216 + 224), 5);
loc_00BE5F5B:
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), *(unsigned __int64 *)(v_rsp - 216 + 224), *(unsigned __int64 *)(v_rsp - 216 - 16), 7);
loc_00BE5F85:
    a4 = 0;
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), a4 + 10, *(unsigned __int64 *)(v_rsp - 216 - 16), a4);
loc_00BE5FAD:
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    v_stack_p20 = v_r14;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), 1 + 9, *(unsigned __int64 *)(v_rsp - 216 - 16), 1);
loc_00BE5FD8:
    result = 0;
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), result + 10, *(unsigned __int64 *)(v_rsp - 216 - 16), (unsigned int)((unsigned int)(result)));
loc_00BE6001:
    result = 0;
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), result + 10, *(unsigned __int64 *)(v_rsp - 216 - 16), (unsigned int)((unsigned int)(result)));
loc_00BE6027:
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    v_stack_p20 = v_r14;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), 2 + 8, *(unsigned __int64 *)(v_rsp - 216 - 16), 2);
loc_00BE6052:
    v_stack_p20 = 2 + 8;
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), 3 + 7, *(unsigned __int64 *)(v_rsp - 216 - 16), 3);
loc_00BE607D:
    *(unsigned int *)(v_rsp - 216 + 224) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((unsigned int)(*(unsigned int *)(v_rsp - 216 + 224)), 6 + 4, v_stack_p58, 6);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00BE3A04(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p58;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (408);
    v_stack_m190 = *(uint64_t *)(arg1);
    result = KeGuardDispatchICall(Arg2, local_rsp - 216 + 48, Arg3, a4);
    *(uint64_t *)(local_rsp - 0xD8 + 0xF8) = result;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0xD8 - 0x10) = *(uint64_t *)(local_rsp - 0xD8 + 0x38);
    if (*(uint64_t *)(local_rsp - 0xD8 + 0x38) != 0) goto loc_00BE3A87;
    if (((*(uint32_t *)(v_stack_m190 + 0x9D8)) & (0x100000ULL)) == 0) goto loc_00BE5F05;
    goto loc_00BE5EF0;
loc_00BE3A87:
    *(uint64_t *)(local_rsp - 0xD8 - 0x50) = 0;
loc_00BE3A97:
    *(uint8_t *)(local_rsp - 0xD8 - 0x48) = 0;
    result = (local_rsp - 216 - 72) + (4 - 3);
    Arg1 = (uint32_t)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE3A97;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x82C))) == 0) goto loc_00BE3C89;
loc_00BE3AD2:
    local_r10 = v_stack_m190;
    if (*(uint64_t *)(v_stack_m190 + 0xAC0) != 0) { local_r10 = *(uint64_t *)(v_stack_m190 + 0xAC0); }
    Arg3 = ((uint32_t)(*(uint32_t *)(local_r10 + 0x828))) + (local_r10);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x50))) == 0) goto loc_00BE3AFB;
    local_r11 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x4C)))) <= 0) {
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x48)));
        local_r11 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x4C)));
        Arg3 = (Arg3) + (local_r10);
    }
    if (((uint32_t)(local_r11)) == 0) goto loc_00BE3C16;
    local_rdi = (uint32_t)((0) - ((uint32_t)(local_r11)));
loc_00BE3B1C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3))) - (1));
    if (condition_is_equal) goto loc_00BE3BE3;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00BE3BD4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE3BC7;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00BE3BBB;
    Arg1 = (uint32_t)((Arg1) - (18));
    if (condition_is_equal) goto loc_00BE3BB4;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00BE3B87;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00BE3B5F;
    if (((uint32_t)(Arg1)) == 10) goto loc_00BE3BE3;
    goto loc_00BE3BF8;
loc_00BE3B5F:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x20))) & (0xFFFULL));
    Arg2 = ((uint32_t)(*(uint32_t *)(Arg3 + 0x28))) + (0xFFFULL);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) >> (12);
    goto loc_00BE3BF8;
loc_00BE3B87:
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(Arg3 + 0x24))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x24)) - 1) & ((uint32_t)(result)));
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + (7));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFF8ULL));
    result = (uint32_t)((*(uint16_t *)(Arg3 + 0x28)) + (2));
    goto loc_00BE3BF8;
loc_00BE3BB4:
    goto loc_00BE3BCC;
loc_00BE3BBB:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x1C))) + (3));
    result = (uint32_t)((result) << (4));
    goto loc_00BE3BF8;
loc_00BE3BC7:
loc_00BE3BCC:
    result = (uint32_t)((*(uint16_t *)(Arg3 + 0x20)) + (55));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    goto loc_00BE3BF8;
loc_00BE3BD4:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x18))) + (2));
    result = (uint32_t)((result + result * 2) << (3));
    goto loc_00BE3BF8;
loc_00BE3BE3:
    Arg2 = (Arg2) >> (3);
loc_00BE3BF8:
    Arg3 = (Arg3) + (Arg2 * 4 + 48);
    local_rdi = (local_rdi) - (1);
    if (condition_is_not_equal) goto loc_00BE3B1C;
loc_00BE3C16:
    *(uint32_t *)(local_rsp - 0xD8 - 0x50) = 1;
    Arg1 = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)(local_r10)));
    *(uint32_t *)(local_rsp - 0xD8 - 0x48) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0xD8 - 0x4C) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) == 1) goto loc_00BE3C40;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) == 12) goto loc_00BE3C40;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) != 43) goto loc_00BE3C4C;
loc_00BE3C40:
    if ((*(uint64_t *)(Arg3 + 0x8)) != (*(uint64_t *)(local_rsp - 0xD8 + 0xF8))) goto loc_00BE3C4C;
    if ((*(uint32_t *)(Arg3 + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0x44))))) goto loc_00BE3C6D;
loc_00BE3C4C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3))) + (-33));
    if (((uint32_t)(result)) > 1) goto loc_00BE3C5D;
    if ((*(uint64_t *)(Arg3 + 0x20)) == (*(uint64_t *)(local_rsp - 0xD8 - 0x10))) goto loc_00BE3C6D;
loc_00BE3C5D:
    a4 = (uint32_t)((0) + (1));
    if (((uint32_t)(a4)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x82C))))) goto loc_00BE3C7C;
    Arg3 = 0;
    goto loc_00BE3AD2;
loc_00BE3C6D:
    if (0 == 0) goto loc_00BE3C7C;
    goto loc_00BE5EF0;
loc_00BE3C7C:
loc_00BE3C89:
    *(uint32_t *)(local_rsp - 0xD8 + 0xF8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF0)));
    *(uint64_t *)(local_rsp - 0xD8 - 0x68) = v_stack_m190;
    result = KeGuardDispatchICall(*(uint64_t *)(local_rsp - 0xD8 + 0xE8), local_rsp - 216 + 120, Arg3, a4);
    Arg3 = 0;
    v_stack_m168 = result;
    v_stack_m160 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0x8C)));
    v_stack_m198 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0x8C)));
    v_stack_m180 = *(uint64_t *)(local_rsp - 0xD8 + 0x80);
    if (*(uint64_t *)(local_rsp - 0xD8 + 0x80) != 0) goto loc_00BE3CFA;
    if (((*(uint32_t *)(v_stack_m190 + 0x9D8)) & (0x100000ULL)) == 0) goto loc_00BE5F30;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 + 0xE0)) = v_stack_m190;
    goto loc_00BE53F6;
loc_00BE3CFA:
    *(uint64_t *)(local_rsp - 0xD8 - 0x40) = 0;
loc_00BE3D07:
    *(uint8_t *)(local_rsp - 0xD8 - 0x38) = 0;
    result = (local_rsp - 216 - 56) + 1;
    Arg1 = (uint32_t)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE3D07;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x82C))) == 0) goto loc_00BE3EE4;
loc_00BE3D33:
    local_r10 = v_stack_m190;
    if (*(uint64_t *)(v_stack_m190 + 0xAC0) != 0) { local_r10 = *(uint64_t *)(v_stack_m190 + 0xAC0); }
    Arg3 = ((uint32_t)(*(uint32_t *)(local_r10 + 0x828))) + (local_r10);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x40))) == 0) goto loc_00BE3D5C;
    local_r11 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x3C)))) <= 0) {
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x38)));
        local_r11 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x3C)));
        Arg3 = (Arg3) + (local_r10);
    }
    if (((uint32_t)(local_r11)) == 0) goto loc_00BE3E70;
    local_rdi = (uint32_t)((0) - ((uint32_t)(local_r11)));
loc_00BE3D7E:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3))) - (1));
    if (condition_is_equal) goto loc_00BE3E45;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00BE3E36;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE3E29;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00BE3E1D;
    Arg1 = (uint32_t)((Arg1) - (18));
    if (condition_is_equal) goto loc_00BE3E16;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00BE3DE9;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00BE3DC1;
    if (((uint32_t)(Arg1)) == 10) goto loc_00BE3E45;
    goto loc_00BE3E5A;
loc_00BE3DC1:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x20))) & (0xFFFULL));
    Arg2 = ((uint32_t)(*(uint32_t *)(Arg3 + 0x28))) + (0xFFFULL);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) >> (12);
    goto loc_00BE3E5A;
loc_00BE3DE9:
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(Arg3 + 0x24))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x24)) - 1) & ((uint32_t)(result)));
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + (7));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFF8ULL));
    result = (uint32_t)((*(uint16_t *)(Arg3 + 0x28)) + (2));
    goto loc_00BE3E5A;
loc_00BE3E16:
    goto loc_00BE3E2E;
loc_00BE3E1D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x1C))) + (3));
    result = (uint32_t)((result) << (4));
    goto loc_00BE3E5A;
loc_00BE3E29:
loc_00BE3E2E:
    result = (uint32_t)((*(uint16_t *)(Arg3 + 0x20)) + (55));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    goto loc_00BE3E5A;
loc_00BE3E36:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x18))) + (2));
    result = (uint32_t)((result + result * 2) << (3));
    goto loc_00BE3E5A;
loc_00BE3E45:
    Arg2 = (Arg2) >> (3);
loc_00BE3E5A:
    Arg3 = (Arg3) + (Arg2 * 4 + 48);
    local_rdi = (local_rdi) - (1);
    if (condition_is_not_equal) goto loc_00BE3D7E;
loc_00BE3E70:
    *(uint32_t *)(local_rsp - 0xD8 - 0x40) = 1;
    Arg1 = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)(local_r10)));
    *(uint32_t *)(local_rsp - 0xD8 - 0x38) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0xD8 - 0x3C) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) == 1) goto loc_00BE3E9A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) == 12) goto loc_00BE3E9A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) != 43) goto loc_00BE3EAB;
loc_00BE3E9A:
    if ((*(uint64_t *)(Arg3 + 0x8)) != v_stack_m168) goto loc_00BE3EAB;
    if ((*(uint32_t *)(Arg3 + 0x10)) == ((uint32_t)((uint32_t)(v_stack_m160)))) goto loc_00BE3EC8;
loc_00BE3EAB:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3))) + (-33));
    if (((uint32_t)(result)) > 1) goto loc_00BE3EB8;
    if ((*(uint64_t *)(Arg3 + 0x20)) == v_stack_m180) goto loc_00BE3EC8;
loc_00BE3EB8:
    a4 = (uint32_t)((0) + (1));
    if (((uint32_t)(a4)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x82C))))) goto loc_00BE3EDD;
    Arg3 = 0;
    goto loc_00BE3D33;
loc_00BE3EC8:
    local_r12 = 0;
    if (0 != 0) goto loc_00BE3F8A;
    goto loc_00BE3EE7;
loc_00BE3EDD:
loc_00BE3EE4:
    local_r12 = 0;
loc_00BE3EE7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF0)))) & (16)) == 0) goto loc_00BE3F0C;
    local_r14 = (uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8));
    if (((*(uint32_t *)(v_stack_m190 + 0x9DC)) & (0x400ULL)) == 0) {
        local_r14 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF0)));
        local_r14 = (uint32_t)((local_r14) & (0xFFFFFFEFULL));
        *(uint32_t *)(local_rsp - 0xD8 + 0xF8) = (uint32_t)(local_r14);
    }
    if ((((uint8_t)(local_r14)) & (16)) == 0) goto loc_00BE3F2C;
    result = sub_00BE8D30(v_stack_m190, v_stack_m180, Arg3, a4);
    if ((uint32_t)(result) == 0) {
        local_r14 = (uint32_t)((local_r14) & (0xFFFFFFEFULL));
        *(uint32_t *)(local_rsp - 0xD8 + 0xF8) = (uint32_t)(local_r14);
    }
    if ((((uint8_t)(local_r14)) & (2)) == 0) goto loc_00BE3F94;
    result = KeGuardDispatchICall(v_stack_m180, v_stack_m180, Arg3, a4);
    Arg3 = 0;
    result = KeGuardDispatchICall(v_stack_m180, (uint8_t)(Arg3 + 1), Arg3, local_rsp - 216 - 48);
    if (result == 0) goto loc_00BE3F8A;
    if ((*(uint32_t *)(local_rsp - 0xD8 - 0x30)) < 40) goto loc_00BE3F8A;
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0xC))) + (v_stack_m180);
    result = KeGuardDispatchICall(Arg1, v_stack_m190 + 2416, Arg3 + 1 + 4, local_rsp - 216 - 48);
    if ((uint32_t)(result) == 0) goto loc_00BE3F9A;
loc_00BE3F8A:
    goto loc_00BE5E4D;
loc_00BE3F94:
loc_00BE3F9A:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (1));
    *(uint32_t *)(local_rsp - 0xD8 - 0x80) = (uint32_t)(result);
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) ^ (1));
    local_rdi = (uint32_t)((local_rdi) + (1));
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x658) * 1), v_stack_m190 + 2416, Arg3 + 1 + 4, local_rsp - 216 - 48);
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x530), 1, Arg3 + 1 + 4, local_rsp - 216 - 48);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m190 + 0x528))) == (*(uint64_t *)(v_stack_m190 + 0x528))) goto loc_00BE403E;
loc_00BE400B:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m190 + 0x528))) - (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x758));
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x768) * 1))) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x760) + arg1 * 1));
    if (v_stack_m180 < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x760) + arg1 * 1))) goto loc_00BE4026;
    if (v_stack_m180 < Arg3) goto loc_00BE4030;
loc_00BE4026:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m190 + 0x528)))) != (*(uint64_t *)(v_stack_m190 + 0x528))) goto loc_00BE400B;
    goto loc_00BE403E;
loc_00BE4030:
    result = KeGuardDispatchICall(Arg1, (uint32_t)((uint32_t)(local_rdi)), Arg3, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x758));
loc_00BE403E:
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x530), (uint32_t)((uint32_t)(local_rdi)), Arg3, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x758));
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x530), (uint32_t)((uint32_t)(local_rdi)), Arg3, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x758));
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x9D8)) & (0x20000000ULL)) == 0) goto loc_00BE4080;
    result = sub_00BEFF8C(v_stack_m190, v_stack_m180, (uint32_t)((uint32_t)(local_r14)), *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x758));
    goto loc_00BE53D3;
loc_00BE4080:
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0xD8 + 0x20) = 0;
    *(uint32_t *)(local_rsp - 0xD8 - 0x18) = 0;
    result = KeGuardDispatchICall(v_stack_m180, 1, Arg3, v_stack_m198);
    if (result != 0) goto loc_00BE40B0;
    v_stack_m198 = 0;
    goto loc_00BE40B4;
loc_00BE40B0:
loc_00BE40B4:
    *(uint64_t *)(local_rsp - 0xD8 + 0x8) = result;
    *(uint32_t *)(local_rsp - 0xD8 - 0x24) = (uint32_t)((uint32_t)(v_stack_m198));
    result = KeGuardDispatchICall(v_stack_m180, 1, 12, v_stack_m198);
    *(uint64_t *)(local_rsp - 0xD8 - 0x60) = result;
    if (result != 0) goto loc_00BE40ED;
    v_stack_m198 = 0;
    goto loc_00BE40F1;
loc_00BE40ED:
loc_00BE40F1:
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_m198));
    *(uint64_t *)(local_rsp - 0xD8 + 0x10) = result;
    *(uint32_t *)(local_rsp - 0xD8 - 0x20) = (uint32_t)((uint32_t)(v_stack_m198));
    result = KeGuardDispatchICall(v_stack_m180, 1, 10, v_stack_m198);
    if (result != 0) goto loc_00BE4129;
    v_stack_m198 = 0;
    goto loc_00BE412D;
loc_00BE4129:
loc_00BE412D:
    *(uint64_t *)(local_rsp - 0xD8 + 0x18) = result;
    *(uint32_t *)(local_rsp - 0xD8 - 0x1C) = (uint32_t)((uint32_t)(v_stack_m198));
    result = KeGuardDispatchICall(v_stack_m180, 1, 10, v_stack_m198);
    if (result != 0) goto loc_00BE4271;
    if (condition_is_above_or_equal) goto loc_00BE5F5B;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x918)) != 0) goto loc_00BE4267;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x928) = 0;
    result = (result) + (*(uint64_t *)(local_rsp - 0xD8 - 0x68));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x930) = 271;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x920) = result;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x938) = v_stack_m180;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x918) = 1;
    if (condition_is_below) goto loc_00BE4267;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE4267;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x9D8))))) == 0) goto loc_00BE4267;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE4210;
loc_00BE41EF:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA74)) + *(uint64_t *)(local_rsp - 0xD8 - 0x68) * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA74)) + *(uint64_t *)(local_rsp - 0xD8 - 0x68) * 1) + (8);
loc_00BE4210:
    if (a4 != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA74)) + *(uint64_t *)(local_rsp - 0xD8 - 0x68) * 1 + Arg1 * 8)) goto loc_00BE41EF;
    if (Arg3 == (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA80))) goto loc_00BE4267;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x588)) = *(uint64_t *)(local_rsp - 0xD8 - 0x68);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)));
    result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x588);
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x918)) == 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x588);
        Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(*(uint64_t *)(local_rsp - 0xD8 - 0x68), Arg2, Arg3, 256);
loc_00BE4267:
    goto loc_00BE4A2B;
loc_00BE4271:
    result = KeGuardDispatchICall(v_stack_m180, local_rsp - 216 - 8, Arg3, 256);
    *(uint64_t *)(local_rsp - 0xD8 + 0x28) = result;
    *(uint32_t *)(local_rsp - 0xD8 - 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x8)));
    *(uint32_t *)(local_rsp - 0xD8 - 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x54)));
    *(uint64_t *)(local_rsp - 0xD8) = v_stack_m180;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) + 288)) <= (*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA64))) goto loc_00BE4383;
    result = sub_00BE7AF8(*(uint64_t *)(local_rsp - 0xD8 - 0x68), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) + 288)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x944)), 256);
    *(uint64_t *)(local_rsp - 0xD8 - 0x70) = result;
    if (result == 0) goto loc_00BE4A26;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x9D8)))) & (2)) != 0) goto loc_00BE437A;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x9D8))) & (0x10000000ULL));
    Arg1 = (uint32_t)(-(Arg1));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) + 288))) & (*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x944)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)))) < 8) goto loc_00BE4317;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804))))) >> (3);
loc_00BE4308:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68)) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804))) + (-8));
    local_rbx = (*(uint64_t *)(local_rsp - 0xD8 - 0x68)) + (8);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00BE4308;
loc_00BE4317:
    if ((uint32_t)(result) == 0) goto loc_00BE4326;
loc_00BE431B:
    *(uint8_t *)(local_rbx) = 0;
    local_rbx = (local_rbx) + (1);
    result = (uint32_t)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE431B;
loc_00BE4326:
    *(uint32_t *)(result + 0x944) = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) == 3) goto loc_00BE4365;
    if (((*(uint32_t *)(result + 0x9D8)) & (0x8000000ULL)) != 0) goto loc_00BE435C;
    if ((uint32_t)(Arg2) == 0) goto loc_00BE435C;
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8) - 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8), 256);
    goto loc_00BE4374;
loc_00BE435C:
    goto loc_00BE436C;
loc_00BE4365:
loc_00BE436C:
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8), 256);
loc_00BE4374:
    *(uint32_t *)(result + 0x944) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x944)));
loc_00BE437A:
    goto loc_00BE4390;
loc_00BE4383:
    *(uint64_t *)(local_rsp - 0xD8 - 0x70) = (uint32_t)(*(uint32_t *)(result + 0x944));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804) = (uint32_t)(result);
loc_00BE4390:
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0xD8 - 0x78) = (uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1;
    v_stack_m170 = 6;
loc_00BE43BA:
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28)));
loc_00BE43D2:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1) = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx + 48))) + (-8));
    result = ((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1) + (8);
    Arg2 = (6) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_00BE43D2;
    if ((uint32_t)(Arg1) == 0) goto loc_00BE43EF;
loc_00BE43E5:
    *(uint8_t *)(result) = 0;
    result = (result) + (local_rbx + 1);
    Arg1 = (uint32_t)((Arg1) + (-1));
    if (condition_is_not_equal) goto loc_00BE43E5;
loc_00BE43EF:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1) = 0;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1 + 0x8) = *(uint64_t *)(local_rsp - 0xD8);
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28)));
    if ((*(uint64_t *)(local_rsp - 0xD8)) >= (*(uint64_t *)(local_rsp - 0xD8) + (uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28)) * 1)) goto loc_00BE4429;
loc_00BE441D:
    result = (*(uint64_t *)(local_rsp - 0xD8)) + (64);
    if (result < (*(uint64_t *)(local_rsp - 0xD8) + (uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28)) * 1)) goto loc_00BE441D;
loc_00BE4429:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28))))) >> (7));
    if ((uint32_t)(local_r11) == 0) goto loc_00BE449A;
loc_00BE4447:
loc_00BE444C:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838)) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8)));
    Arg3 = (Arg3) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8) + 0x8));
    a4 = (*(uint64_t *)(local_rsp - 0xD8)) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE444C;
    Arg1 = (a4) - (*(uint64_t *)(local_rsp - 0xD8));
    Arg1 = (Arg1) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x834))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28)))));
    *(uint64_t *)(local_rsp - 0xD8 + 0x48) = Arg2;
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(Arg2)));
    local_rbx = (uint32_t)((local_rbx) & (63));
    if (condition_is_equal) { local_rbx = 1; }
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE4447;
loc_00BE449A:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m178)))) & (127));
    if (((uint32_t)(Arg2)) < 8) goto loc_00BE44C5;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00BE44B1:
    Arg3 = (Arg3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (8);
    Arg2 = (uint32_t)((Arg2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE44B1;
loc_00BE44C5:
    if ((uint32_t)(Arg2) == 0) goto loc_00BE44DD;
loc_00BE44C9:
    Arg3 = (Arg3) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (1);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BE44C9;
loc_00BE44DD:
    result = (Arg3) >> (31);
    local_rbx = 0;
    goto loc_00BE44EF;
loc_00BE44E8:
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(result)));
    result = (result) >> (31);
loc_00BE44EF:
    if (result != 0) goto loc_00BE44E8;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1 + 0x14) = Arg3;
    local_r12 = (local_rsp - 216 - 40) + (4);
    local_r10 = ((uint32_t)(*(uint32_t *)(result + 0x944)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) * 1) + (result + 48);
    local_r13 = (local_rsp - 216) + (8);
    if (condition_is_not_equal) goto loc_00BE43BA;
    if (*(uint64_t *)(local_rsp - 0xD8 - 0x70) == 0) goto loc_00BE4A26;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x18) = v_stack_m180;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78)) = 44;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x9D8)) & (0x8100000ULL)) != 0) goto loc_00BE456F;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x9DC)) & (0x8000ULL)) == 0) goto loc_00BE456F;
    result = sub_00BE8D30(*(uint64_t *)(local_rsp - 0xD8 - 0x70), v_stack_m180, Arg3, a4);
    if ((uint32_t)(result) != 0) {
    }
    v_stack_m1A8 = local_rsp - 216 - 44;
    *(uint64_t *)(local_rsp - 0xD8 - 0x68) = *(uint64_t *)(local_rsp - 0xD8 - 0x70);
    v_stack_m1B0 = local_rsp - 216 - 88;
    v_stack_m1B8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8)));
    v_stack_m190 = *(uint64_t *)(local_rsp - 0xD8 - 0x70);
    result = sub_00BE60B0(local_rsp - 216 - 104, v_stack_m168, (uint32_t)(v_stack_m160), v_stack_m180);
    if (!sign_flag) goto loc_00BE45C7;
    local_r12 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 + 0xE0)) = v_stack_m190;
    goto loc_00BE53EA;
loc_00BE45C7:
    local_r12 = (local_r12) - (v_stack_m190);
    local_r12 = (local_r12) + (*(uint64_t *)(local_rsp - 0xD8 - 0x68));
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x2C))) - (*(uint32_t *)(local_rsp - 0xD8 - 0x58)));
    *(uint64_t *)(local_rsp - 0xD8 - 0x78) = local_r12;
    local_r11 = ((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x58))) + (*(uint64_t *)(local_rsp - 0xD8 + 0xE0));
loc_00BE4601:
    *(uint64_t *)(local_r12 + 0xC0) = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result + 48))) + (-8));
    result = (local_r12 + 192) + (6 + 2);
    Arg2 = (6) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE4601;
    if ((uint32_t)(Arg1) == 0) goto loc_00BE4621;
loc_00BE4617:
    *(uint8_t *)(result) = (uint8_t)(Arg2);
    result = (result) + (6 - 5);
    Arg1 = (uint32_t)((Arg1) + (-1));
    if (condition_is_not_equal) goto loc_00BE4617;
loc_00BE4621:
    *(uint32_t *)(local_r12 + 0xC0) = (uint32_t)(Arg2);
    *(uint64_t *)(local_r12 + 0xC0 + 0x8) = local_r11;
    *(uint32_t *)(local_r12 + 0xC0 + 0x10) = (uint32_t)(a4);
    Arg1 = ((uint32_t)((uint32_t)(a4))) + (local_r11);
    if (local_r11 >= Arg1) goto loc_00BE465D;
loc_00BE4651:
    result = (local_r11) + (64);
    if (result < Arg1) goto loc_00BE4651;
loc_00BE465D:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(a4))) >> (7));
    if ((uint32_t)(local_rsi) == 0) goto loc_00BE46CA;
loc_00BE4679:
loc_00BE467C:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x838)) ^ (*(uint64_t *)(local_r11));
    local_r10 = (local_r11) + (6 + 2);
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r10));
    local_r10 = (local_r10) + (6 + 2);
    result = (6 + 2) - (1);
    if (condition_is_not_equal) goto loc_00BE467C;
    Arg1 = (local_r10) - (local_r11);
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    *(uint64_t *)(local_rsp - 0xD8 + 0x50) = 1;
    Arg2 = (uint32_t)((1) ^ ((uint32_t)(local_r12)));
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x834))) ^ ((uint32_t)(Arg2)));
    local_rdi = (uint32_t)((local_rdi) & (63));
    if (condition_is_equal) { local_rdi = 1; }
    local_rsi = (uint32_t)((local_rsi) + (-1));
    if (condition_is_not_equal) goto loc_00BE4679;
loc_00BE46CA:
    a4 = (uint32_t)((a4) & (127));
    if (((uint32_t)(a4)) < ((uint32_t)(6 + 2))) goto loc_00BE46EE;
    result = ((uint32_t)((uint32_t)(a4))) >> (3);
loc_00BE46DA:
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r10));
    local_r10 = (local_r10) + (6 + 2);
    a4 = (uint32_t)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE46DA;
loc_00BE46EE:
    local_r11 = 0;
    if ((uint32_t)(a4) == 0) goto loc_00BE470B;
loc_00BE46F6:
    Arg3 = (Arg3) ^ (*(uint8_t *)(local_r10));
    local_r10 = (local_r10) + (1);
    a4 = (uint32_t)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE46F6;
loc_00BE470B:
    goto loc_00BE4713;
loc_00BE4710:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BE4713:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BE4710;
    *(uint32_t *)(local_r12 + 0xC0 + 0x14) = Arg3;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xF0) = (uint32_t)(result + 48);
    v_stack_m190 = *(uint64_t *)(local_rsp - 0xD8 - 0x68);
    if (*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 96 != 0) goto loc_00BE4994;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) + 48)) <= (*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0xA64))) goto loc_00BE4831;
    result = sub_00BE7AF8(*(uint64_t *)(local_rsp - 0xD8 - 0x68), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) + 48)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x944)), a4);
    local_r11 = 0;
    if (result == 0) goto loc_00BE4A26;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x9D8)))) & (2)) != 0) goto loc_00BE4828;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x9D8))) & (0x10000000ULL));
    Arg1 = (uint32_t)(-(Arg1));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)) + 48))) & (*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x944)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804)))) < ((uint32_t)(6 + 2))) goto loc_00BE47C2;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804))))) >> (3);
loc_00BE47B4:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68)) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804))) + (-8));
    local_rbx = (*(uint64_t *)(local_rsp - 0xD8 - 0x68)) + (6 + 2);
    Arg1 = (Arg1) - (result + 48 - 47);
    if (condition_is_not_equal) goto loc_00BE47B4;
loc_00BE47C2:
    if ((uint32_t)(result) == 0) goto loc_00BE47D1;
loc_00BE47C6:
    *(uint8_t *)(local_rbx) = 0;
    local_rbx = (local_rbx) + (result + 48 - 47);
    result = (uint32_t)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE47C6;
loc_00BE47D1:
    *(uint32_t *)(result + 0x944) = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) == 3) goto loc_00BE4810;
    if (((*(uint32_t *)(result + 0x9D8)) & (0x8000000ULL)) != 0) goto loc_00BE4807;
    if ((uint32_t)(Arg2) == 0) goto loc_00BE4807;
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8) - 8, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8), result + 48 - 47);
    goto loc_00BE481F;
loc_00BE4807:
    goto loc_00BE4817;
loc_00BE4810:
loc_00BE4817:
    result = KeGuardDispatchICall(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8) - 0x8), *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x7E8), result + 48 - 47);
loc_00BE481F:
    *(uint32_t *)(result + 0x944) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x944)));
    local_r11 = 0;
loc_00BE4828:
    goto loc_00BE483A;
loc_00BE4831:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x804) = (uint32_t)(result);
loc_00BE483A:
    local_rsi = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x68) + 0x804))) + ((uint32_t)(*(uint32_t *)(result + 0x944)));
loc_00BE4854:
    *(uint64_t *)(local_rsi) = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result + 48))) + (-8));
    result = (local_rsi) + (6 + 2);
    Arg2 = (1 + 5) - (1);
    if (condition_is_not_equal) goto loc_00BE4854;
    if ((uint32_t)(Arg1) == 0) goto loc_00BE4871;
loc_00BE4866:
    *(uint8_t *)(result) = 0;
    result = (result) + (1);
    Arg1 = (uint32_t)((Arg1) + (-1));
    if (condition_is_not_equal) goto loc_00BE4866;
loc_00BE4871:
    *(uint32_t *)(local_rsi) = 13;
    *(uint64_t *)(local_rsi + 0x8) = *(uint64_t *)(local_rsp - 0xD8 - 0x60);
    *(uint32_t *)(local_rsi + 0x10) = (uint32_t)((uint32_t)(v_stack_m188));
    if ((*(uint64_t *)(local_rsp - 0xD8 - 0x60)) >= (*(uint64_t *)(local_rsp - 0xD8 - 0x60) + (uint32_t)(v_stack_m188) * 1)) goto loc_00BE48B8;
loc_00BE48AC:
    result = (*(uint64_t *)(local_rsp - 0xD8 - 0x60)) + (64);
    if (result < (*(uint64_t *)(local_rsp - 0xD8 - 0x60) + (uint32_t)(v_stack_m188) * 1)) goto loc_00BE48AC;
loc_00BE48B8:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m188)))) >> (7));
    if ((uint32_t)(local_r11) == 0) goto loc_00BE492E;
loc_00BE48D7:
loc_00BE48DA:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838)) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x60)));
    a4 = (*(uint64_t *)(local_rsp - 0xD8 - 0x60)) + (6 + 2);
    Arg3 = (Arg3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (6 + 2);
    result = (6 + 2) - (1);
    if (condition_is_not_equal) goto loc_00BE48DA;
    Arg1 = (a4) - (*(uint64_t *)(local_rsp - 0xD8 - 0x60));
    Arg1 = (Arg1) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x944)) + 0x834))) ^ ((uint32_t)(*(uint64_t *)(local_rsp - 0xD8 - 0x78))));
    *(uint64_t *)(local_rsp - 0xD8 + 0x58) = Arg2;
    local_r10 = (uint32_t)((local_r10) ^ ((uint32_t)(Arg2)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = 1; }
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE48D7;
loc_00BE492E:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m188)))) & (127));
    if (((uint32_t)(Arg2)) < ((uint32_t)(6 + 2))) goto loc_00BE4958;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00BE4944:
    Arg3 = (Arg3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (6 + 2);
    Arg2 = (uint32_t)((Arg2) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE4944;
loc_00BE4958:
    if ((uint32_t)(Arg2) == 0) goto loc_00BE4971;
loc_00BE495C:
    Arg3 = (Arg3) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (1);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BE495C;
loc_00BE4971:
    goto loc_00BE4979;
loc_00BE4976:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BE4979:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BE4976;
    *(uint32_t *)(local_rsi + 0x14) = Arg3;
    goto loc_00BE49A6;
loc_00BE4994:
    *(uint32_t *)(local_rsi) = 13;
loc_00BE49A6:
    if (((*(uint32_t *)(1 + 0x9D8)) & (0x20000000ULL)) == 0) goto loc_00BE49C9;
    if ((uint32_t)((uint32_t)(v_stack_m188)) != 0) {
        a4 = local_rsi + 28;
        Arg3 = (uint32_t)((uint32_t)(v_stack_m188));
        Arg2 = *(uint64_t *)(local_rsp - 0xD8 - 0x60);
        Arg1 = 1;
        result = sub_0051AF4C(Arg1, Arg2, Arg3, a4);
    }
    local_r14 = 0;
    *(uint32_t *)(local_rsi + 0x18) = 0;
    if ((*(uint32_t *)(local_rsp - 0xD8 - 0x80)) != 0) {
        *(uint32_t *)(local_rsi + 0x18) = 1;
    }
    if (1 == 0) goto loc_00BE4A26;
    v_stack_m190 = 1;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x90) = 35;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xA0)) < 148) goto loc_00BE4AA3;
    result = KeGuardDispatchICall(v_stack_m180, Arg2, Arg3, a4);
    if (result != 0) goto loc_00BE4A3F;
loc_00BE4A26:
loc_00BE4A2B:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 + 0xE0)) = v_stack_m190;
    goto loc_00BE53F6;
loc_00BE4A3F:
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x50))) + (v_stack_m180);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xB8))) | (2));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xB8) = (uint32_t)(Arg2);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x70)) < v_stack_m180) goto loc_00BE4A7F;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x70);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x70)) < Arg3) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x70));
        Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (4));
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xA8) = result;
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xB8) = (uint32_t)(Arg1);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x78)) < v_stack_m180) goto loc_00BE4AA3;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x78);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x78)) < Arg3) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x98) + 0x78));
        Arg1 = (uint32_t)((Arg1) | ((uint32_t)(6 + 2)));
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xB0) = result;
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xB8) = (uint32_t)(Arg1);
    }
    v_stack_m190 = 1;
    *(uint64_t *)(local_rsp - 0xD8 - 0x68) = 1;
    if (((*(uint32_t *)(1 + 0x9D8)) & (0x200000ULL)) == 0) goto loc_00BE5E45;
    result = KeGuardDispatchICall(v_stack_m180, Arg2, Arg3, a4);
    local_r12 = 0;
    *(uint64_t *)(local_rsp - 0xD8 - 0x70) = result;
    if (result != 0) goto loc_00BE4AE4;
loc_00BE4ADA:
    goto loc_00BE53D3;
loc_00BE4AE4:
    *(uint16_t *)(local_rsp - 0xD8 + 0xF8) = (uint16_t)(*(uint16_t *)(result + 0x6));
    a4 = (Arg2) >> (3);
    *(uint64_t *)(local_rsp - 0xD8 - 0x60) = a4;
    if ((uint16_t)(*(uint16_t *)(result + 0x6)) != 0) goto loc_00BE4C36;
    if (condition_is_above_or_equal) goto loc_00BE5F85;
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE4ADA;
    *(uint64_t *)(1 + 0x928) = 0;
    result = (result) + (1);
    *(uint64_t *)(1 + 0x930) = 271;
    *(uint64_t *)(1 + 0x920) = result;
    *(uint64_t *)(1 + 0x938) = v_stack_m180;
    *(uint32_t *)(1 + 0x918) = 1;
    if (condition_is_below) goto loc_00BE4ADA;
    if (((*(uint32_t *)(1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x9D8))))) == 0) goto loc_00BE4ADA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE4BD6;
loc_00BE4BB6:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 0x1 * 1)) ^ (*(uint64_t *)(1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(1 + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(1 + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1) + (6 + 2);
loc_00BE4BD6:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8)) goto loc_00BE4BB6;
    if (Arg3 == (*(uint64_t *)(1 + 0xA80))) goto loc_00BE4ADA;
    *(uint64_t *)(*(uint64_t *)(1 + 0x588)) = 1;
    *(uint32_t *)(*(uint64_t *)(1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804)));
    result = *(uint64_t *)(1 + 0x588);
    if ((*(uint32_t *)(1 + 0x918)) == 0) {
        result = *(uint64_t *)(1 + 0x588);
        Arg1 = (*(uint64_t *)(1 + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
loc_00BE4C24:
    Arg2 = 0;
    result = sub_00BE8384(1, Arg2, Arg3, 256);
    goto loc_00BE4ADA;
loc_00BE4C36:
    local_r11 = (*(uint16_t *)(result + 0x14)) + (24);
    local_r11 = (local_r11) + (result);
    *(uint64_t *)(local_rsp - 0xD8 - 0x78) = local_r11;
    Arg2 = 0;
    v_stack_m170 = v_stack_m168 + 256 + 256 * 2 * 4;
    v_stack_m188 = 0;
    if ((uint16_t)(*(uint64_t *)(1 + 0x838)) == 0) goto loc_00BE5261;
    *(uint64_t *)(local_rsp - 0xD8 - 0x80) = local_r11 + 8;
    local_r14 = 0;
loc_00BE4C8B:
    local_r13 = (uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x8)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8))))) { local_r13 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8))); }
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4)));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4)))));
    if (0 == 0) goto loc_00BE4CBE;
    if (((uint32_t)(local_r13)) < (*(uint32_t *)(local_r11 + 0x0 - 0x1 + 0x0 - 0x1 * 4 * 8 + 0xC))) goto loc_00BE503B;
loc_00BE4CBE:
    if (v_stack_m168 == (v_stack_m168 + 256 + 256 * 2 * 4)) goto loc_00BE5007;
loc_00BE4CC7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168)))) >= ((uint32_t)(local_r13))) goto loc_00BE4FF2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4))))) goto loc_00BE4FF2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4))))) goto loc_00BE514F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4)))) > ((uint32_t)(local_r13))) goto loc_00BE514F;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x8))))) != 0) goto loc_00BE4D0D;
    if (((*(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x8)) + v_stack_m180 * 1)) & (32)) == 0) goto loc_00BE4FE3;
loc_00BE4D0D:
    local_rsi = (uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x8)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8))))) { local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8))); }
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4)))));
    result = KeGuardDispatchICall(v_stack_m168, v_stack_m180, (uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4)), v_stack_m168 + 256 + 256 * 2 * 4);
    if ((*(uint32_t *)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4))))) goto loc_00BE4D43;
    if ((*(uint32_t *)(result + 0x4)) <= ((uint32_t)(local_rsi))) goto loc_00BE4E6F;
loc_00BE4D43:
    result = (uint32_t)((result) - ((uint32_t)(v_stack_m180)));
    result = (uint32_t)((result) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (condition_is_above_or_equal) goto loc_00BE6001;
    local_r11 = 0;
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE4E6F;
    *(uint64_t *)(1 + 0x928) = 0;
    result = (result) + (1);
    *(uint64_t *)(1 + 0x930) = 271;
    *(uint64_t *)(1 + 0x920) = result;
    *(uint64_t *)(1 + 0x938) = v_stack_m180;
    *(uint32_t *)(1 + 0x918) = (uint32_t)(local_r11 + 1);
    if (condition_is_below) goto loc_00BE4E6F;
    if (((*(uint32_t *)(1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE4E6F;
    if ((((uint8_t)(local_r11 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x9D8))))) == 0) goto loc_00BE4E6F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE4E18;
loc_00BE4DF7:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 0x1 * 1)) ^ (*(uint64_t *)(1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(1 + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(1 + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1) + (8);
loc_00BE4E18:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8)) goto loc_00BE4DF7;
    if (Arg3 == (*(uint64_t *)(1 + 0xA80))) goto loc_00BE4E6F;
    *(uint64_t *)(*(uint64_t *)(1 + 0x588)) = 1;
    *(uint32_t *)(*(uint64_t *)(1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804)));
    result = *(uint64_t *)(1 + 0x588);
    if ((*(uint32_t *)(1 + 0x918)) == 0) {
        result = *(uint64_t *)(1 + 0x588);
        Arg1 = (*(uint64_t *)(1 + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(1, Arg2, Arg3, 256);
loc_00BE4E6F:
    Arg3 = ((uint32_t)(*(uint32_t *)(result))) + (v_stack_m180);
    result = KeGuardDispatchICall(result, v_stack_m180, Arg3, 256);
    if ((*(uint32_t *)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x8 + 0x4))))) goto loc_00BE4E99;
    if ((*(uint32_t *)(result + 0x4)) <= ((uint32_t)(local_rsi))) goto loc_00BE4FC8;
loc_00BE4E99:
    result = (uint32_t)((result) - ((uint32_t)(v_stack_m180)));
    result = (uint32_t)((result) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    if (condition_is_above_or_equal) goto loc_00BE5FD8;
    local_r14 = 0;
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE4FDA;
    *(uint64_t *)(1 + 0x928) = 0;
    *(uint64_t *)(1 + 0x920) = 1 + local_rsi * 1;
    *(uint32_t *)(1 + 0x918) = (uint32_t)(local_r14 + 1);
    *(uint64_t *)(1 + 0x930) = 271;
    *(uint64_t *)(1 + 0x938) = v_stack_m180;
    if ((*(uint32_t *)(1 + 0x918)) < 0) goto loc_00BE4FDA;
    if (((*(uint32_t *)(1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE4FDA;
    if ((((uint8_t)(local_r14 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x9D8))))) == 0) goto loc_00BE4FDA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE4F6F;
loc_00BE4F4E:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 0x1 * 1)) ^ (*(uint64_t *)(1 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(1 + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(1 + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1) + (8);
loc_00BE4F6F:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8)) goto loc_00BE4F4E;
    if (Arg3 == (*(uint64_t *)(1 + 0xA80))) goto loc_00BE4FDA;
    *(uint64_t *)(*(uint64_t *)(1 + 0x588)) = 1;
    *(uint32_t *)(*(uint64_t *)(1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804)));
    result = *(uint64_t *)(1 + 0x588);
    if ((*(uint32_t *)(1 + 0x918)) == 0) {
        result = *(uint64_t *)(1 + 0x588);
        Arg1 = (*(uint64_t *)(1 + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(1, Arg2, Arg3, 256);
    goto loc_00BE4FDA;
loc_00BE4FC8:
    local_r14 = 0;
loc_00BE4FDA:
loc_00BE4FE3:
    local_r12 = (v_stack_m168) + (12);
    if (local_r12 != v_stack_m170) goto loc_00BE4CC7;
loc_00BE4FF2:
loc_00BE5007:
    Arg2 = (*(uint64_t *)(local_rsp - 0xD8 - 0x80)) + (40);
    *(uint64_t *)(local_rsp - 0xD8 - 0x80) = Arg2;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m188)) + (1));
    v_stack_m188 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8))))) goto loc_00BE4C8B;
    Arg2 = 0;
    goto loc_00BE5267;
loc_00BE503B:
    if (condition_is_above_or_equal) goto loc_00BE5FAD;
    local_r12 = 0;
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE4ADA;
    *(uint64_t *)(1 + 0x928) = 0;
    *(uint64_t *)(1 + 0x920) = 1 + local_rsi * 1;
    *(uint32_t *)(1 + 0x918) = (uint32_t)(local_r12 + 1);
    *(uint64_t *)(1 + 0x930) = 271;
    *(uint64_t *)(1 + 0x938) = v_stack_m180;
    if ((*(uint32_t *)(1 + 0x918)) < 0) goto loc_00BE4ADA;
    if (((*(uint32_t *)(1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x9D8))))) == 0) goto loc_00BE4ADA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE50F9;
loc_00BE50D8:
    result = (*(uint64_t *)(1 + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 0x1 * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(1 + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(1 + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1) + (8);
loc_00BE50F9:
    if (a4 != ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8)) goto loc_00BE50D8;
    if (Arg3 == (*(uint64_t *)(1 + 0xA80))) goto loc_00BE4ADA;
    *(uint64_t *)(*(uint64_t *)(1 + 0x588)) = 1;
    *(uint32_t *)(*(uint64_t *)(1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804)));
    result = *(uint64_t *)(1 + 0xA80);
    if ((*(uint32_t *)(1 + 0x918)) == 0) {
        Arg2 = Arg3;
        Arg2 = (Arg2) ^ (*(uint64_t *)(1 + 0xA80));
        result = *(uint64_t *)(1 + 0x588);
        *(uint64_t *)(result + 0x18) = Arg2;
    }
    goto loc_00BE4C24;
loc_00BE514F:
    if (condition_is_above_or_equal) goto loc_00BE6027;
    local_r12 = 0;
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE4ADA;
    *(uint64_t *)(1 + 0x928) = 0;
    *(uint64_t *)(1 + 0x920) = 1 + local_rsi * 1;
    *(uint32_t *)(1 + 0x918) = (uint32_t)(local_r12 + 1);
    *(uint64_t *)(1 + 0x930) = 271;
    *(uint64_t *)(1 + 0x938) = v_stack_m180;
    if ((*(uint32_t *)(1 + 0x918)) < 0) goto loc_00BE4ADA;
    if (((*(uint32_t *)(1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x9D8))))) == 0) goto loc_00BE4ADA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE520D;
loc_00BE51EC:
    result = (*(uint64_t *)(1 + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 0x1 * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(1 + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(1 + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1) + (8);
loc_00BE520D:
    if (a4 != ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8)) goto loc_00BE51EC;
    if (Arg3 == (*(uint64_t *)(1 + 0xA80))) goto loc_00BE4ADA;
    *(uint64_t *)(*(uint64_t *)(1 + 0x588)) = 1;
    *(uint32_t *)(*(uint64_t *)(1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804)));
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE5147;
loc_00BE5255:
    Arg1 = (*(uint64_t *)(1 + 0xA80)) ^ (Arg3);
    *(void **)(*(uint64_t *)(1 + 0x588) + 0x18) = Arg1;
    goto loc_00BE5147;
loc_00BE5261:
loc_00BE5267:
    if (0 == v_stack_m170) goto loc_00BE537C;
    if (0 >= v_stack_m170) goto loc_00BE6052;
    local_r12 = 0;
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE4ADA;
    *(uint64_t *)(1 + 0x928) = 0;
    *(uint64_t *)(1 + 0x920) = 1 + local_rsi * 1;
    *(uint64_t *)(1 + 0x930) = 271;
    *(uint64_t *)(1 + 0x938) = v_stack_m180;
    *(uint32_t *)(1 + 0x918) = 1;
    if ((*(uint32_t *)(1 + 0x918)) < 0) goto loc_00BE4ADA;
    if (((*(uint32_t *)(1 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE4ADA;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x9D8))))) == 0) goto loc_00BE4ADA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE532F;
loc_00BE530F:
    result = (*(uint64_t *)(1 + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 0x1 * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(1 + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(1 + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1) + (1 + 7);
loc_00BE532F:
    if (a4 != ((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8)) goto loc_00BE530F;
    if (Arg3 == (*(uint64_t *)(1 + 0xA80))) goto loc_00BE4ADA;
    *(uint64_t *)(*(uint64_t *)(1 + 0x588)) = 1;
    *(uint32_t *)(*(uint64_t *)(1 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804)));
    if ((*(uint32_t *)(1 + 0x918)) != 0) goto loc_00BE5147;
    goto loc_00BE5255;
loc_00BE537C:
    local_r12 = 0;
    if ((uint32_t)(a4) == 0) goto loc_00BE538D;
    Arg2 = (uint32_t)((a4 + 6) & (0xFFFFFFF8ULL));
    goto loc_00BE5390;
loc_00BE538D:
loc_00BE5390:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804)) + 48) + ((uint32_t)(0 + (uint16_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8) + (uint16_t)((uint32_t)(*(uint32_t *)(1 + 0xA74)) + 1 * 1 + Arg1 * 8) * 2 * 8)));
    if (((uint32_t)(Arg1)) <= (*(uint32_t *)(1 + 0xA64))) goto loc_00BE54C5;
    result = sub_00BE7AF8(1, (uint32_t)((uint32_t)(Arg1)), (uint32_t)(*(uint32_t *)(1 + 0x944)), a4);
    *(uint64_t *)(local_rsp - 0xD8 - 0x70) = result;
    if (result != 0) goto loc_00BE53FD;
loc_00BE53D3:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 + 0xE0)) = v_stack_m190;
    if (!sign_flag) goto loc_00BE5E57;
loc_00BE53EA:
    if (((uint32_t)((uint32_t)(0xC000009AULL))) == 0xC000010EULL) goto loc_00BE5E57;
loc_00BE53F6:
    goto loc_00BE5EF0;
loc_00BE53FD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x9D8)))) & (2)) != 0) goto loc_00BE54AB;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x9D8))) & (0x10000000ULL));
    Arg1 = (uint32_t)(-(Arg1));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (*(uint32_t *)(1 + 0x944)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804)))) < ((uint32_t)(1 + 7))) goto loc_00BE5448;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x804))))) >> (3);
loc_00BE543A:
    *(uint64_t *)(1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x804))) + (-8));
    local_rbx = (1) + (1 + 7);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00BE543A;
loc_00BE5448:
    if ((uint32_t)(result) == 0) goto loc_00BE5457;
loc_00BE544C:
    *(uint8_t *)(local_rbx) = 0;
    local_rbx = (local_rbx) + (1);
    result = (uint32_t)((result) + (-1));
    if (condition_is_not_equal) goto loc_00BE544C;
loc_00BE5457:
    *(uint32_t *)(v_stack_m190 + 0x944) = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) == 3) goto loc_00BE5496;
    if (((*(uint32_t *)(v_stack_m190 + 0x9D8)) & (0x8000000ULL)) != 0) goto loc_00BE548D;
    if ((uint32_t)(Arg2) == 0) goto loc_00BE548D;
    result = KeGuardDispatchICall(*(uint64_t *)(1 + 0x7E8) - 8, *(uint64_t *)(*(uint64_t *)(1 + 0x7E8) - 0x8), *(uint64_t *)(1 + 0x7E8), 1);
    goto loc_00BE54A5;
loc_00BE548D:
    goto loc_00BE549D;
loc_00BE5496:
loc_00BE549D:
    result = KeGuardDispatchICall(*(uint64_t *)(1 + 0x7E8), *(uint64_t *)(*(uint64_t *)(1 + 0x7E8) - 0x8), *(uint64_t *)(1 + 0x7E8), 1);
loc_00BE54A5:
    *(uint32_t *)(v_stack_m190 + 0x944) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)));
loc_00BE54AB:
    goto loc_00BE54D2;
loc_00BE54C5:
    *(uint64_t *)(local_rsp - 0xD8 - 0x70) = (uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x804) = (uint32_t)(*(uint64_t *)(1 + 0x7E8));
loc_00BE54D2:
loc_00BE54F0:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1) = 0;
    Arg3 = (uint32_t)((6 + 42) + (-8));
    result = ((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1) + (1 + 7);
    Arg2 = (6) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE54F0;
    if (Arg3 == 0) goto loc_00BE5510;
loc_00BE5504:
    *(uint8_t *)(result) = 0;
    result = (result) + (6 - 5);
    Arg3 = (uint32_t)((Arg3) + (-1));
    if (condition_is_not_equal) goto loc_00BE5504;
loc_00BE5510:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1 + 0x8) = v_stack_m168;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1) = 30;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1 + 0x10) = 0;
    goto loc_00BE5531;
loc_00BE552F:
    Arg2 = (uint32_t)((*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x838)) ^ ((uint32_t)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x838))));
loc_00BE5531:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x838)) >> (31);
    if (result != 0) goto loc_00BE552F;
    *(uint64_t *)(local_rsp - 0xD8 - 0x68) = (uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1 + 0x14) = (uint32_t)(Arg2);
    *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1 + 0x18) = v_stack_m180;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x50)));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1 + 0x24) = (uint32_t)((uint32_t)(v_stack_m160));
    *(uint16_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1 + 0x28) = (uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8));
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + *(uint64_t *)(local_rsp - 0xD8 + 0xE0) * 1) + (48);
    v_stack_m160 = Arg1;
    if ((uint32_t)(*(uint64_t *)(local_rsp - 0xD8 - 0x60)) == 0) goto loc_00BE557B;
    local_r14 = (*(uint64_t *)(local_rsp - 0xD8 - 0x60) - 1) + (7);
    local_r14 = (local_r14) & (-8);
    local_r14 = (local_r14) + (Arg1);
    goto loc_00BE557E;
loc_00BE557B:
loc_00BE557E:
    v_stack_m188 = Arg1;
    *(void **)(local_rsp - 0xD8 - 0x60) = Arg1 + (uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8)) + (uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8)) * 2 * 8;
    if ((uint32_t)(*(uint64_t *)(local_rsp - 0xD8 - 0x60)) == 0) goto loc_00BE55A3;
    v_stack_m178 = v_stack_m168 + 12;
    goto loc_00BE55A8;
loc_00BE55A3:
    v_stack_m178 = v_stack_m170;
loc_00BE55A8:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8)))) goto loc_00BE55D3;
loc_00BE55B6:
loc_00BE55BB:
    *(uint64_t *)(arg1 + 0x8 - 0x8) = 0;
    *(uint32_t *)(arg1 + 0x8) = 0x80000000ULL;
    result = (Arg1 + 8) + (12);
    Arg1 = (2) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE55BB;
    Arg2 = ((uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8))) - (6 - 5);
    if (condition_is_not_equal) goto loc_00BE55B6;
loc_00BE55D3:
    if (Arg1 == (Arg1 + (uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8)) + (uint16_t)(*(uint16_t *)(local_rsp - 0xD8 + 0xF8)) * 2 * 8)) goto loc_00BE5E48;
    local_r11 = 0;
loc_00BE55E3:
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x24)) & (0x2000000ULL)) != 0) goto loc_00BE5633;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78))))) != 0x54494E49ULL) goto loc_00BE560A;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x4)) == 0x4742444BULL) goto loc_00BE5633;
loc_00BE560A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78))))) != 0x45474150ULL) goto loc_00BE563B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x4))) == ((uint16_t)((uint32_t)(0x7877ULL)))) goto loc_00BE5633;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x4))) == ((uint16_t)((uint32_t)(0x7277ULL)))) goto loc_00BE5633;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x4))) != ((uint16_t)((uint32_t)(0x7777ULL)))) goto loc_00BE564D;
loc_00BE5633:
    goto loc_00BE571E;
loc_00BE563B:
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x4))) != 0x41525245ULL) goto loc_00BE564D;
    if ((*(uint16_t *)((uint32_t)(0x7777ULL))) == ((uint16_t)((uint32_t)(0x4154ULL)))) goto loc_00BE5633;
loc_00BE564D:
    Arg3 = (*(uint64_t *)(local_rsp - 0xD8 - 0x78)) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x950));
loc_00BE5675:
    Arg2 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x950)) + (6 - 5);
    if (((uint8_t)(*(uint8_t *)(Arg3 + *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x950) * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x950))))) goto loc_00BE568D;
    local_r11 = (uint32_t)((7) + (-1));
    if (condition_is_not_equal) goto loc_00BE5675;
    goto loc_00BE5713;
loc_00BE568D:
loc_00BE5695:
    Arg3 = (*(uint64_t *)(local_rsp - 0xD8 - 0x78)) + (8);
    a4 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x958)) + (8);
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78))) != (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x958)))) goto loc_00BE56CE;
    Arg2 = (uint32_t)((8) + (-8));
    if (((uint32_t)(Arg2)) >= 8) goto loc_00BE5695;
    local_r11 = 0;
    if ((uint32_t)(Arg2) == 0) goto loc_00BE5713;
loc_00BE56B7:
    Arg3 = (Arg3) + (6 - 5);
    a4 = (a4) + (6 - 5);
    if (((uint8_t)(*(uint8_t *)(Arg3))) != ((uint8_t)(*(uint8_t *)(a4)))) goto loc_00BE56D1;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BE56B7;
    goto loc_00BE5713;
loc_00BE56CE:
    local_r11 = 0;
loc_00BE56D1:
    Arg2 = (*(uint64_t *)(local_rsp - 0xD8 - 0x78)) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x960));
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
loc_00BE56E1:
    local_r10 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x960)) + (6 - 5);
    if (((uint8_t)(*(uint8_t *)(Arg2 + *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x960) * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x960))))) goto loc_00BE56F6;
    Arg3 = (uint32_t)((4) + ((uint32_t)(a4)));
    if (condition_is_not_equal) goto loc_00BE56E1;
    goto loc_00BE5713;
loc_00BE56F6:
    Arg2 = (*(uint64_t *)(local_rsp - 0xD8 - 0x78)) - (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x968));
loc_00BE5702:
    local_rbx = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x968)) + (6 - 5);
    if (((uint8_t)(*(uint8_t *)(Arg2 + *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x968) * 1))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x968))))) goto loc_00BE5719;
    Arg3 = (uint32_t)((6) + ((uint32_t)(a4)));
    if (condition_is_not_equal) goto loc_00BE5702;
loc_00BE5713:
    local_r11 = 0;
loc_00BE5719:
loc_00BE571E:
    if (!sign_flag) goto loc_00BE572C;
    goto loc_00BE5731;
loc_00BE572C:
    if ((uint32_t)((uint32_t)((uint32_t)(6 - 5))) == 0) goto loc_00BE5754;
loc_00BE5731:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78))) != 0x54494E49ULL) goto loc_00BE5754;
    local_r13 = (uint32_t)((uint32_t)(6 - 5));
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x4)) == 0x4742444BULL) {
        local_r13 = (uint32_t)((uint32_t)(6 - 5));
        if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x9DC)) & (0x2000ULL)) != 0) { local_r13 = 0; }
    }
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x9DC)) & (0x4000ULL)) == 0) goto loc_00BE577B;
    if (condition_is_above_or_equal) goto loc_00BE577B;
    if (v_stack_m180 == (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x5E0))) goto loc_00BE5778;
    if (v_stack_m180 == (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x5E8))) {
        local_r13 = (uint32_t)(6 - 5);
    }
    local_rsi = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x10)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x8))))) { local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0x8))); }
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xC)))));
    *(uint32_t *)(local_rsp - 0xD8 - 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xC)));
    *(uint32_t *)(local_rsp - 0xD8 + 0xF8) = (uint32_t)(local_rsi);
    if (v_stack_m168 == v_stack_m170) goto loc_00BE5927;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xC))))) goto loc_00BE592F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4)))) > ((uint32_t)(local_rsi))) goto loc_00BE5944;
    if ((uint32_t)(local_r13) != 0) goto loc_00BE5956;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168)));
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xC)))));
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xC)));
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x78) + 0xC))))) + (v_stack_m180);
    local_rbx = ((uint32_t)((uint32_t)(a4))) + (local_r11);
    result = 0;
loc_00BE57F7:
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28))) + (*(uint64_t *)(local_rsp - 0xD8));
    if (local_r11 >= result) goto loc_00BE580D;
    if (local_rbx > (*(uint64_t *)(local_rsp - 0xD8))) goto loc_00BE5937;
loc_00BE580D:
    local_r10 = (uint32_t)((0) + 1);
    Arg3 = (local_rsp - 216) + (8);
    Arg2 = (local_rsp - 216 - 40) + (4);
    if (((uint32_t)(local_r10)) < 6) goto loc_00BE57F7;
    Arg1 = ((uint32_t)((uint32_t)(a4))) + (local_r11);
    if (local_r11 >= Arg1) goto loc_00BE584F;
loc_00BE5843:
    result = (local_r11) + (64);
    if (result < Arg1) goto loc_00BE5843;
loc_00BE584F:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(a4))) >> (7));
    if ((uint32_t)(local_rbx) == 0) goto loc_00BE58BD;
loc_00BE586B:
loc_00BE5870:
    Arg3 = (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x838)) ^ (*(uint64_t *)(local_r11));
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r11 + 0x8));
    local_r10 = (local_r11) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE5870;
    Arg1 = (local_r10) - (local_r11);
    Arg1 = (Arg1) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944))) ^ (1));
    *(uint64_t *)(local_rsp - 0xD8 + 0x60) = 1;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0x944)) + 0x834))) ^ ((uint32_t)(result)));
    local_rsi = (uint32_t)((local_rsi) & (63));
    if (condition_is_equal) { local_rsi = 1; }
    local_rbx = (uint32_t)((local_rbx) + (-1));
    if (condition_is_not_equal) goto loc_00BE586B;
loc_00BE58BD:
    a4 = (uint32_t)((a4) & (127));
    if (((uint32_t)(a4)) < 8) goto loc_00BE58E3;
    result = ((uint32_t)((uint32_t)(a4))) >> (3);
loc_00BE58CE:
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r10));
    local_r10 = (local_r10) + (8);
    a4 = (uint32_t)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE58CE;
loc_00BE58E3:
    local_r11 = 0;
    if ((uint32_t)(a4) == 0) goto loc_00BE5900;
loc_00BE58EB:
    Arg3 = (Arg3) ^ (*(uint8_t *)(local_r10));
    local_r10 = (local_r10) + (1);
    a4 = (uint32_t)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE58EB;
loc_00BE5900:
    goto loc_00BE5908;
loc_00BE5905:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BE5908:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BE5905;
    *(uint32_t *)(v_stack_m188 + 0x8) = Arg3;
    goto loc_00BE593A;
loc_00BE5927:
loc_00BE592F:
    if (0 < 1) goto loc_00BE5C60;
    goto loc_00BE5944;
loc_00BE5937:
    local_r11 = 0;
loc_00BE593A:
loc_00BE5944:
    if (0 > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8))))) goto loc_00BE5C60;
    if (v_stack_m168 == v_stack_m170) goto loc_00BE5C60;
loc_00BE5956:
    if (v_stack_m178 == v_stack_m170) goto loc_00BE5C60;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x4)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8))))) goto loc_00BE5C60;
loc_00BE597B:
    if (v_stack_m178 == v_stack_m170) goto loc_00BE5C60;
    if ((uint32_t)(local_r13) == 0) goto loc_00BE5991;
    goto loc_00BE5C27;
loc_00BE5991:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4))))) goto loc_00BE5ABC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4))))) goto loc_00BE607D;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x918)) != 0) goto loc_00BE5ABC;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x928) = 0;
    result = (v_stack_m160) + (*(uint64_t *)(local_rsp - 0xD8 - 0x70));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x930) = 271;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x920) = result;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x938) = v_stack_m180;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x918) = 1;
    if (condition_is_below) goto loc_00BE5ABC;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE5ABC;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x9D8))))) == 0) goto loc_00BE5ABC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE5A64;
loc_00BE5A43:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x838)) ^ (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA74)) + *(uint64_t *)(local_rsp - 0xD8 - 0x70) * 1));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA78))) & (63));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA78)) + (result);
    Arg3 = (Arg3) ^ (0xEFAULL);
    a4 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA74)) + *(uint64_t *)(local_rsp - 0xD8 - 0x70) * 1) + (8);
loc_00BE5A64:
    if (a4 != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA74)) + *(uint64_t *)(local_rsp - 0xD8 - 0x70) * 1 + Arg1 * 8)) goto loc_00BE5A43;
    if (Arg3 == (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA80))) goto loc_00BE5ABC;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x588)) = *(uint64_t *)(local_rsp - 0xD8 - 0x70);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x804)));
    result = 0;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x918)) == 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x588);
        Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0xA80)) ^ (Arg3);
        *(void **)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(*(uint64_t *)(local_rsp - 0xD8 - 0x70), Arg2, Arg3, 256);
loc_00BE5ABC:
    local_r11 = ((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4))) + (v_stack_m180);
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m168 + 0x4)))));
    local_rbx = ((uint32_t)((uint32_t)(a4))) + (local_r11);
    result = 0;
loc_00BE5ADD:
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28))) + (*(uint64_t *)(local_rsp - 0xD8));
    if (local_r11 >= result) goto loc_00BE5AF3;
    if (local_rbx > (*(uint64_t *)(local_rsp - 0xD8))) goto loc_00BE5C12;
loc_00BE5AF3:
    local_r10 = (uint32_t)((0) + 1);
    Arg3 = (local_rsp - 216) + (8);
    Arg2 = (local_rsp - 216 - 40) + (4);
    if (((uint32_t)(local_r10)) < 6) goto loc_00BE5ADD;
    if (((uint32_t)(a4)) < 4) goto loc_00BE5C12;
    Arg1 = ((uint32_t)((uint32_t)(a4))) + (local_r11);
    if (local_r11 >= Arg1) goto loc_00BE5B3F;
loc_00BE5B33:
    result = (local_r11) + (64);
    if (result < Arg1) goto loc_00BE5B33;
loc_00BE5B3F:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(a4))) >> (7));
    if ((uint32_t)(local_rbx) == 0) goto loc_00BE5BAD;
loc_00BE5B5B:
loc_00BE5B60:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x838)) ^ (*(uint64_t *)(local_r11));
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r11 + 0x8));
    local_r10 = (local_r11) + (16);
    result = (8) - (1);
    if (condition_is_not_equal) goto loc_00BE5B60;
    Arg1 = (local_r10) - (local_r11);
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x834))) ^ ((uint32_t)(*(uint64_t *)(local_rsp - 0xD8 - 0x70))));
    *(uint64_t *)(local_rsp - 0xD8 + 0x68) = 1;
    local_rsi = (uint32_t)((local_rsi) ^ (1));
    local_rsi = (uint32_t)((local_rsi) & (63));
    if (condition_is_equal) { local_rsi = 1; }
    local_rbx = (uint32_t)((local_rbx) + (-1));
    if (condition_is_not_equal) goto loc_00BE5B5B;
loc_00BE5BAD:
    a4 = (uint32_t)((a4) & (127));
    if (((uint32_t)(a4)) < 8) goto loc_00BE5BD3;
    result = ((uint32_t)((uint32_t)(a4))) >> (3);
loc_00BE5BBE:
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r10));
    local_r10 = (local_r10) + (8);
    a4 = (uint32_t)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE5BBE;
loc_00BE5BD3:
    local_r11 = 0;
    if ((uint32_t)(a4) == 0) goto loc_00BE5BF0;
loc_00BE5BDB:
    Arg3 = (Arg3) ^ (*(uint8_t *)(local_r10));
    local_r10 = (local_r10) + (1);
    a4 = (uint32_t)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE5BDB;
loc_00BE5BF0:
    goto loc_00BE5BF8;
loc_00BE5BF5:
    Arg3 = (uint8_t)((Arg3) ^ ((uint8_t)(Arg3)));
loc_00BE5BF8:
    result = (Arg3) >> (7);
    if (result != 0) goto loc_00BE5BF5;
    Arg3 = (uint8_t)((Arg3) & (127));
    goto loc_00BE5C18;
loc_00BE5C12:
    local_r11 = 0;
loc_00BE5C18:
loc_00BE5C27:
    *(uint8_t *)(v_stack_m160) = 128;
    local_rbx = (v_stack_m168) + (12);
    local_r14 = (v_stack_m178) + (12);
    result = (v_stack_m160) + (1);
    v_stack_m168 = local_rbx;
    v_stack_m160 = result;
    v_stack_m178 = local_r14;
    local_r15 = (uint32_t)(*(uint32_t *)(v_stack_m178 + 0x4));
    if (local_r14 != v_stack_m170) {
        local_r15 = *(uint32_t *)(local_r14 + 0x4);
    }
    if (((uint32_t)(local_r15)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8))))) goto loc_00BE597B;
loc_00BE5C60:
    if ((uint32_t)(local_r13) != 0) goto loc_00BE5DDA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8))))) goto loc_00BE5DDA;
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178))))) + (v_stack_m180);
    *(uint32_t *)(v_stack_m188 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178)));
    *(uint32_t *)(v_stack_m188 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8)));
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m178)))));
    local_rbx = ((uint32_t)((uint32_t)(a4))) + (local_r11);
    local_r13 = 0;
loc_00BE5CA8:
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x28))) + (*(uint64_t *)(local_rsp - 0xD8));
    if (local_r11 >= result) goto loc_00BE5CBE;
    if (local_rbx > (*(uint64_t *)(local_rsp - 0xD8))) goto loc_00BE5DD2;
loc_00BE5CBE:
    Arg3 = (uint32_t)((0) + 1);
    Arg2 = (local_rsp - 216) + (local_r13 + 8);
    Arg1 = (local_rsp - 216 - 40) + (4);
    if (Arg3 < 6) goto loc_00BE5CA8;
    Arg1 = ((uint32_t)((uint32_t)(a4))) + (local_r11);
    if (local_r11 >= Arg1) goto loc_00BE5CFF;
loc_00BE5CF3:
    result = (local_r11) + (64);
    if (result < Arg1) goto loc_00BE5CF3;
loc_00BE5CFF:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(a4))) >> (7));
    if ((uint32_t)(local_rbx) == 0) goto loc_00BE5D6A;
loc_00BE5D1C:
loc_00BE5D1F:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x838)) ^ (*(uint64_t *)(local_r11));
    local_r10 = (local_r11) + (local_r13 + 8);
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r10));
    local_r10 = (local_r10) + (local_r13 + 8);
    result = (local_r13 + 8) - (1);
    if (condition_is_not_equal) goto loc_00BE5D1F;
    Arg1 = (local_r10) - (local_r11);
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0xD8 - 0x70) + 0x834))) ^ ((uint32_t)(v_stack_m180)));
    *(uint64_t *)(local_rsp - 0xD8 + 0x70) = Arg2;
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(Arg2)));
    local_rsi = (uint32_t)((local_rsi) & (63));
    if (condition_is_equal) { local_rsi = 1; }
    local_rbx = (uint32_t)((local_rbx) + (-1));
    if (condition_is_not_equal) goto loc_00BE5D1C;
loc_00BE5D6A:
    a4 = (uint32_t)((a4) & (127));
    if (((uint32_t)(a4)) < ((uint32_t)(local_r13 + 8))) goto loc_00BE5D8E;
    result = ((uint32_t)((uint32_t)(a4))) >> (3);
loc_00BE5D7A:
    Arg3 = (Arg3) ^ (*(uint64_t *)(local_r10));
    local_r10 = (local_r10) + (local_r13 + 8);
    a4 = (uint32_t)((a4) + (-8));
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00BE5D7A;
loc_00BE5D8E:
    local_r11 = 0;
    if ((uint32_t)(a4) == 0) goto loc_00BE5DAB;
loc_00BE5D96:
    Arg3 = (Arg3) ^ (*(uint8_t *)(local_r10));
    local_r10 = (local_r10) + (1);
    a4 = (uint32_t)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00BE5D96;
loc_00BE5DAB:
    goto loc_00BE5DB3;
loc_00BE5DB0:
    Arg3 = (uint32_t)((Arg3) ^ (Arg3));
loc_00BE5DB3:
    result = (Arg3) >> (31);
    if (result != 0) goto loc_00BE5DB0;
    *(uint32_t *)(v_stack_m188 + 0x14) = Arg3;
    goto loc_00BE5DD5;
loc_00BE5DD2:
    local_r11 = 0;
loc_00BE5DD5:
loc_00BE5DDA:
    if (v_stack_m168 == v_stack_m170) goto loc_00BE5E1C;
    if ((*(uint32_t *)(v_stack_m168)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x80))))) goto loc_00BE5E1C;
    if ((*(uint32_t *)(v_stack_m168 + 0x4)) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF8))))) goto loc_00BE5E1C;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0xD8 - 0x80));
    if (v_stack_m178 != v_stack_m170) {
        result = v_stack_m160;
        *(uint8_t *)(result) = 128;
        result = (result) + 1;
        Arg3 = (v_stack_m178) + (12);
        v_stack_m160 = result;
        v_stack_m178 = Arg3;
    }
    local_rbx = (v_stack_m168) + (12);
    v_stack_m168 = local_rbx;
loc_00BE5E1C:
    local_r14 = (v_stack_m188) + (24);
    local_r12 = (*(uint64_t *)(local_rsp - 0xD8 - 0x78)) + (40);
    v_stack_m188 = local_r14;
    *(uint64_t *)(local_rsp - 0xD8 - 0x78) = local_r12;
    if (local_r14 == (*(uint64_t *)(local_rsp - 0xD8 - 0x60))) goto loc_00BE5E41;
    goto loc_00BE55E3;
loc_00BE5E41:
loc_00BE5E45:
    local_r12 = 0;
loc_00BE5E48:
    v_stack_m190 = *(uint64_t *)(local_rsp - 0xD8 - 0x68);
loc_00BE5E4D:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 + 0xE0)) = *(uint64_t *)(local_rsp - 0xD8 - 0x68);
loc_00BE5E57:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xF0))) & (0xFFFFFFEFULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & ((uint32_t)((uint32_t)(0x80000004ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000004ULL)))) goto loc_00BE5EEE;
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)((uint32_t)(0x80000000ULL))));
    result = KeGuardDispatchICall(*(uint64_t *)(local_rsp - 0xD8 - 0x10), Arg2, Arg3, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x94)))) < 20) goto loc_00BE5EEE;
    local_rdi = ((uint32_t)(*(uint32_t *)(result + 0x90)) + (uint32_t)(*(uint32_t *)(result + 0x94)) * 1) + (*(uint64_t *)(local_rsp - 0xD8 - 0x10));
    goto loc_00BE5EE9;
loc_00BE5EAA:
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x90)) + *(uint64_t *)(local_rsp - 0xD8 - 0x10) * 1 + 0xC)) == 0) goto loc_00BE5EEE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x90)) + *(uint64_t *)(local_rsp - 0xD8 - 0x10) * 1 + 0x10))) == 0) goto loc_00BE5EEE;
    if (*(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x90)) + *(uint64_t *)(local_rsp - 0xD8 - 0x10) * 1 + 0x10)) + *(uint64_t *)(local_rsp - 0xD8 - 0x10) * 1) == 0) goto loc_00BE5EE5;
    result = sub_00BE3A04(v_stack_m190, *(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x90)) + *(uint64_t *)(local_rsp - 0xD8 - 0x10) * 1 + 0x10)) + *(uint64_t *)(local_rsp - 0xD8 - 0x10) * 1), (uint32_t)((uint32_t)(local_r14)), a4);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xD8 + 0xE0)) = v_stack_m190;
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00BE5EE5;
    if (((uint32_t)(result)) != 0xC000010EULL) goto loc_00BE5EF0;
loc_00BE5EE5:
    local_rbx = ((uint32_t)(*(uint32_t *)(result + 0x90)) + *(uint64_t *)(local_rsp - 0xD8 - 0x10) * 1) + (20);
loc_00BE5EE9:
    if (local_rbx != local_rdi) goto loc_00BE5EAA;
loc_00BE5EEE:
    result = 0;
loc_00BE5EF0:
    local_rsp = (local_rsp) + (408);
    return result;
loc_00BE5F05:
    v_stack_p20 = (uint32_t)((uint32_t)(local_r14));
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), 5 + 5, *(uint64_t *)(local_rsp - 0xD8 + 0xE0), 5);
loc_00BE5F30:
    v_stack_p20 = *(uint64_t *)(local_rsp - 0xD8 + 0xE0);
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), 5 + 5, *(uint64_t *)(local_rsp - 0xD8 + 0xE0), 5);
loc_00BE5F5B:
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), *(uint64_t *)(local_rsp - 0xD8 + 0xE0), *(uint64_t *)(local_rsp - 0xD8 - 0x10), 7);
loc_00BE5F85:
    a4 = 0;
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), a4 + 10, *(uint64_t *)(local_rsp - 0xD8 - 0x10), a4);
loc_00BE5FAD:
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    v_stack_p20 = local_r14;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), 1 + 9, *(uint64_t *)(local_rsp - 0xD8 - 0x10), 1);
loc_00BE5FD8:
    result = 0;
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), result + 10, *(uint64_t *)(local_rsp - 0xD8 - 0x10), (uint32_t)((uint32_t)(result)));
loc_00BE6001:
    result = 0;
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), result + 10, *(uint64_t *)(local_rsp - 0xD8 - 0x10), (uint32_t)((uint32_t)(result)));
loc_00BE6027:
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    v_stack_p20 = local_r14;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), 2 + 8, *(uint64_t *)(local_rsp - 0xD8 - 0x10), 2);
loc_00BE6052:
    v_stack_p20 = 2 + 8;
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), 3 + 7, *(uint64_t *)(local_rsp - 0xD8 - 0x10), 3);
loc_00BE607D:
    *(uint32_t *)(local_rsp - 0xD8 + 0xE0) = 0xE8000009ULL;
    v_stack_p20 = 0;
    result = KeBugCheckEx((uint32_t)(*(uint32_t *)(local_rsp - 0xD8 + 0xE0)), 6 + 4, v_stack_p58, 6);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=initkdbg&rva=0x00BE3A04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
