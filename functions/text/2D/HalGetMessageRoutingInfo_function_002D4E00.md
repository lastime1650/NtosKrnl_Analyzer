# HalGetMessageRoutingInfo

- RVA: `0x002D4E00`–`0x002D540D` (길이 `1,549` bytes)
- VA: `0x00000001402D4E00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006FC20`
- 디코드: `324`개 명령, `1,549/1,549` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x002D4E70` → [HalpInterruptAffinityIsSteerable](HalpInterruptAffinityIsSteerable_function_002D5414.md) (function, `0x002D5414`)
- `0x002D4EF6` → [HalpGetProcessorStateByNtIndex](HalpGetProcessorStateByNtIndex_function_002D5598.md) (function, `0x002D5598`)
- `0x002D50BA` → [HalpInterruptSetProblemEx](../48/HalpInterruptSetProblemEx_function_0048AC8C.md) (function, `0x0048AC8C`)
- `0x002D53F5` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)

### Direct callers
- [sub_00B203FA](../../page/B2/Unknown_function_00B203FA.md) at `0x00B20543`

### Static image references
- `0x002D4ED3` → RVA `0x00F231B8` (`.data`; read)
- `0x002D4EEA` → RVA `0x00E10200` (`.data`; read)
- `0x002D4F5C` → RVA `0x00F90698` (`.data`; read)
- `0x002D4FE0` → RVA `0x00E101E8` (`.data`; read)
- `0x002D5042` → RVA `0x00010AA8` (`.rdata`; read)
- `0x002D5049` → RVA `0x00F906B8` (`.data`; write)
- `0x002D5050` → RVA `0x00F906C8` (`.data`; write)
- `0x002D5057` → RVA `0x00F90694` (`.data`; write)
- `0x002D5061` → RVA `0x00F906A0` (`.data`; write)
- `0x002D5067` → RVA `0x00F906D0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002D53DB` → [sub_006DDB06 + 0x6](../6D/Unknown_function_006DDB06.md) (`tail-transfer`)
  - `0x002D53E7` → [sub_006DDB06](../6D/Unknown_function_006DDB06.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002D4E00  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002D4E05  55                              push rbp
002D4E06  56                              push rsi
002D4E07  57                              push rdi
002D4E08  41 54                           push r12
002D4E0A  41 55                           push r13
002D4E0C  41 56                           push r14
002D4E0E  41 57                           push r15
002D4E10  48 8B EC                        mov rbp, rsp
002D4E13  48 83 EC 60                     sub rsp, 0x60
002D4E17  33 C0                           xor eax, eax
002D4E19  45 33 E4                        xor r12d, r12d
002D4E1C  0F 57 C0                        xorps xmm0, xmm0
002D4E1F  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
002D4E23  48 8B F2                        mov rsi, rdx
002D4E26  44 89 65 50                     mov dword ptr [rbp + 0x50], r12d
002D4E2A  48 8B F9                        mov rdi, rcx
002D4E2D  44 88 65 40                     mov byte ptr [rbp + 0x40], r12b
002D4E31  44 8D 68 01                     lea r13d, [rax + 1]
002D4E35  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
002D4E39  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
002D4E3D  44 39 29                        cmp dword ptr [rcx], r13d
002D4E40  0F 87 78 05 00 00               ja 0x1402d53be
002D4E46  48 83 C1 10                     add rcx, 0x10
002D4E4A  48 8B 19                        mov rbx, qword ptr [rcx]
002D4E4D  48 85 DB                        test rbx, rbx
002D4E50  0F 84 EC 00 00 00               je 0x1402d4f42
002D4E56  48 8D 43 FF                     lea rax, [rbx - 1]
002D4E5A  45 8A F5                        mov r14b, r13b
002D4E5D  48 33 C3                        xor rax, rbx
002D4E60  48 23 C3                        and rax, rbx
002D4E63  48 3B C3                        cmp rax, rbx
002D4E66  0F 85 D6 00 00 00               jne 0x1402d4f42
002D4E6C  48 8D 55 40                     lea rdx, [rbp + 0x40]
002D4E70  E8 9F 05 00 00                  call 0x1402d5414
002D4E75  85 C0                           test eax, eax
002D4E77  0F 88 C5 01 00 00               js 0x1402d5042
002D4E7D  44 8B 7F 20                     mov r15d, dword ptr [rdi + 0x20]
002D4E81  41 8B CF                        mov ecx, r15d
002D4E84  44 0F B7 47 18                  movzx r8d, word ptr [rdi + 0x18]
002D4E89  66 44 89 45 E0                  mov word ptr [rbp - 0x20], r8w
002D4E8E  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
002D4E92  41 2B CD                        sub ecx, r13d
002D4E95  0F 85 AF 00 00 00               jne 0x1402d4f4a
002D4E9B  45 84 F6                        test r14b, r14b
002D4E9E  0F 84 BF 03 00 00               je 0x1402d5263
002D4EA4  44 89 65 50                     mov dword ptr [rbp + 0x50], r12d
002D4EA8  43 8D 0C 28                     lea ecx, [r8 + r13]
002D4EAC  48 85 DB                        test rbx, rbx
002D4EAF  0F 84 C1 01 00 00               je 0x1402d5076
002D4EB5  48 0F BC D3                     bsf rdx, rbx
002D4EB9  41 0F B7 C8                     movzx ecx, r8w
002D4EBD  45 8B CC                        mov r9d, r12d
002D4EC0  0F B6 C2                        movzx eax, dl
002D4EC3  48 0F B3 C3                     btr rbx, rax
002D4EC7  C1 E1 06                        shl ecx, 6
002D4ECA  0F B6 C2                        movzx eax, dl
002D4ECD  03 C8                           add ecx, eax
002D4ECF  48 89 5D D8                     mov qword ptr [rbp - 0x28], rbx
002D4ED3  48 8B 05 DE E2 C4 00            mov rax, qword ptr [rip + 0xc4e2de]
002D4EDA  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
002D4EDD  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
002D4EE0  44 38 65 40                     cmp byte ptr [rbp + 0x40], r12b
002D4EE4  0F 85 EE 04 00 00               jne 0x1402d53d8
002D4EEA  3B 0D 10 B3 B3 00               cmp ecx, dword ptr [rip + 0xb3b310]
002D4EF0  0F 83 E2 02 00 00               jae 0x1402d51d8
002D4EF6  E8 9D 06 00 00                  call 0x1402d5598
002D4EFB  48 85 C0                        test rax, rax
002D4EFE  0F 84 FE 04 00 00               je 0x1402d5402
002D4F04  8B 07                           mov eax, dword ptr [rdi]
002D4F06  44 89 2E                        mov dword ptr [rsi], r13d
002D4F09  85 C0                           test eax, eax
002D4F0B  0F 85 02 03 00 00               jne 0x1402d5213
002D4F11  44 89 6E 08                     mov dword ptr [rsi + 8], r13d
002D4F15  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
002D4F18  89 46 54                        mov dword ptr [rsi + 0x54], eax
002D4F1B  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
002D4F1E  89 46 50                        mov dword ptr [rsi + 0x50], eax
002D4F21  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
002D4F24  89 46 58                        mov dword ptr [rsi + 0x58], eax
002D4F27  33 C0                           xor eax, eax
002D4F29  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
002D4F31  48 83 C4 60                     add rsp, 0x60
002D4F35  41 5F                           pop r15
002D4F37  41 5E                           pop r14
002D4F39  41 5D                           pop r13
002D4F3B  41 5C                           pop r12
002D4F3D  5F                              pop rdi
002D4F3E  5E                              pop rsi
002D4F3F  5D                              pop rbp
002D4F40  C3                              ret
002D4F41  CC                              int3
002D4F42  45 8A F4                        mov r14b, r12b
002D4F45  E9 22 FF FF FF                  jmp 0x1402d4e6c
002D4F4A  41 2B CD                        sub ecx, r13d
002D4F4D  0F 84 A8 01 00 00               je 0x1402d50fb
002D4F53  41 3B CD                        cmp ecx, r13d
002D4F56  0F 85 2D 04 00 00               jne 0x1402d5389
002D4F5C  44 38 25 35 B7 CB 00            cmp byte ptr [rip + 0xcbb735], r12b
002D4F63  0F 84 77 03 00 00               je 0x1402d52e0
002D4F69  45 8A D4                        mov r10b, r12b
002D4F6C  43 8D 0C 28                     lea ecx, [r8 + r13]
002D4F70  41 B9 25 02 00 C0               mov r9d, 0xc0000225
002D4F76  48 85 DB                        test rbx, rbx
002D4F79  75 2A                           jne 0x1402d4fa5
002D4F7B  66 45 03 C5                     add r8w, r13w
002D4F7F  45 0F B7 C0                     movzx r8d, r8w
002D4F83  66 44 89 45 E0                  mov word ptr [rbp - 0x20], r8w
002D4F88  44 3B C1                        cmp r8d, ecx
002D4F8B  0F 83 92 02 00 00               jae 0x1402d5223
002D4F91  4A 8B 1C C5 08 00 00 00         mov rbx, qword ptr [r8*8 + 8]
002D4F99  44 0F B7 45 E0                  movzx r8d, word ptr [rbp - 0x20]
002D4F9E  EB D0                           jmp 0x1402d4f70
002D4FA0  48 85 DB                        test rbx, rbx
002D4FA3  74 6B                           je 0x1402d5010
002D4FA5  48 0F BC D3                     bsf rdx, rbx
002D4FA9  41 0F B7 C8                     movzx ecx, r8w
002D4FAD  0F B6 C2                        movzx eax, dl
002D4FB0  48 0F B3 C3                     btr rbx, rax
002D4FB4  C1 E1 06                        shl ecx, 6
002D4FB7  0F B6 C2                        movzx eax, dl
002D4FBA  03 C8                           add ecx, eax
002D4FBC  48 8B 05 F5 E1 C4 00            mov rax, qword ptr [rip + 0xc4e1f5]
002D4FC3  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
002D4FC6  41 8B CC                        mov ecx, r12d
002D4FC9  89 45 50                        mov dword ptr [rbp + 0x50], eax
002D4FCC  85 C9                           test ecx, ecx
002D4FCE  0F 88 30 FF FF FF               js 0x1402d4f04
002D4FD4  3B 05 26 B2 B3 00               cmp eax, dword ptr [rip + 0xb3b226]
002D4FDA  0F 83 40 03 00 00               jae 0x1402d5320
002D4FE0  48 8B 0D 01 B2 B3 00            mov rcx, qword ptr [rip + 0xb3b201]
002D4FE7  48 8D 04 40                     lea rax, [rax + rax*2]
002D4FEB  83 3C C1 06                     cmp dword ptr [rcx + rax*8], 6
002D4FEF  0F 85 CC 00 00 00               jne 0x1402d50c1
002D4FF5  8B 44 C1 08                     mov eax, dword ptr [rcx + rax*8 + 8]
002D4FF9  45 84 D2                        test r10b, r10b
002D4FFC  74 3C                           je 0x1402d503a
002D4FFE  39 45 F0                        cmp dword ptr [rbp - 0x10], eax
002D5001  0F 85 95 00 00 00               jne 0x1402d509c
002D5007  41 0F B7 C8                     movzx ecx, r8w
002D500B  41 03 CD                        add ecx, r13d
002D500E  EB 90                           jmp 0x1402d4fa0
002D5010  66 45 03 C5                     add r8w, r13w
002D5014  41 0F B7 C0                     movzx eax, r8w
002D5018  66 89 45 E0                     mov word ptr [rbp - 0x20], ax
002D501C  44 0F B7 C0                     movzx r8d, ax
002D5020  3B C1                           cmp eax, ecx
002D5022  0F 83 FB 01 00 00               jae 0x1402d5223
002D5028  48 8B 1C C5 08 00 00 00         mov rbx, qword ptr [rax*8 + 8]
002D5030  44 0F B7 45 E0                  movzx r8d, word ptr [rbp - 0x20]
002D5035  E9 66 FF FF FF                  jmp 0x1402d4fa0
002D503A  45 8A D5                        mov r10b, r13b
002D503D  89 45 F0                        mov dword ptr [rbp - 0x10], eax
002D5040  EB C5                           jmp 0x1402d5007
002D5042  4C 8D 0D 5F BA D3 FF            lea r9, [rip - 0x2c45a1]
002D5049  4C 89 25 68 B6 CB 00            mov qword ptr [rip + 0xcbb668], r12
002D5050  4C 89 0D 71 B6 CB 00            mov qword ptr [rip + 0xcbb671], r9
002D5057  C7 05 33 B6 CB 00 27 00 00 00   mov dword ptr [rip + 0xcbb633], 0x27
002D5061  89 05 39 B6 CB 00               mov dword ptr [rip + 0xcbb639], eax
002D5067  C7 05 5F B6 CB 00 DA 04 00 00   mov dword ptr [rip + 0xcbb65f], 0x4da
002D5071  E9 B3 FE FF FF                  jmp 0x1402d4f29
002D5076  66 45 03 C5                     add r8w, r13w
002D507A  41 0F B7 C0                     movzx eax, r8w
002D507E  66 89 45 E0                     mov word ptr [rbp - 0x20], ax
002D5082  3B C1                           cmp eax, ecx
002D5084  0F 83 1B 02 00 00               jae 0x1402d52a5
002D508A  48 8B 1C C5 08 00 00 00         mov rbx, qword ptr [rax*8 + 8]
002D5092  44 0F B7 45 E0                  movzx r8d, word ptr [rbp - 0x20]
002D5097  E9 10 FE FF FF                  jmp 0x1402d4eac
002D509C  44 38 65 40                     cmp byte ptr [rbp + 0x40], r12b
002D50A0  75 9B                           jne 0x1402d503d
002D50A2  C7 44 24 20 A8 05 00 00         mov dword ptr [rsp + 0x20], 0x5a8
002D50AA  45 33 C0                        xor r8d, r8d
002D50AD  4C 8D 0D F4 B9 D3 FF            lea r9, [rip - 0x2c460c]
002D50B4  33 C9                           xor ecx, ecx
002D50B6  41 8D 50 14                     lea edx, [r8 + 0x14]
002D50BA  E8 CD 5B 1B 00                  call 0x14048ac8c
002D50BF  EB 30                           jmp 0x1402d50f1
002D50C1  4C 8D 0D E0 B9 D3 FF            lea r9, [rip - 0x2c4620]
002D50C8  4C 89 25 E9 B5 CB 00            mov qword ptr [rip + 0xcbb5e9], r12
002D50CF  4C 89 0D F2 B5 CB 00            mov qword ptr [rip + 0xcbb5f2], r9
002D50D6  C7 05 B4 B5 CB 00 14 00 00 00   mov dword ptr [rip + 0xcbb5b4], 0x14
002D50E0  44 89 25 B9 B5 CB 00            mov dword ptr [rip + 0xcbb5b9], r12d
002D50E7  C7 05 DF B5 CB 00 7B 05 00 00   mov dword ptr [rip + 0xcbb5df], 0x57b
002D50F1  B8 0D 00 00 C0                  mov eax, 0xc000000d
002D50F6  E9 2E FE FF FF                  jmp 0x1402d4f29
002D50FB  44 38 25 96 B5 CB 00            cmp byte ptr [rip + 0xcbb596], r12b
002D5102  0F 85 C3 02 00 00               jne 0x1402d53cb
002D5108  43 8D 0C 28                     lea ecx, [r8 + r13]
002D510C  41 B9 25 02 00 C0               mov r9d, 0xc0000225
002D5112  48 85 DB                        test rbx, rbx
002D5115  75 2C                           jne 0x1402d5143
002D5117  66 45 03 C5                     add r8w, r13w
002D511B  41 0F B7 C0                     movzx eax, r8w
002D511F  66 89 45 E0                     mov word ptr [rbp - 0x20], ax
002D5123  44 0F B7 C0                     movzx r8d, ax
002D5127  3B C1                           cmp eax, ecx
002D5129  0F 83 E6 01 00 00               jae 0x1402d5315
002D512F  48 8B 1C C5 08 00 00 00         mov rbx, qword ptr [rax*8 + 8]
002D5137  44 0F B7 45 E0                  movzx r8d, word ptr [rbp - 0x20]
002D513C  EB CE                           jmp 0x1402d510c
002D513E  48 85 DB                        test rbx, rbx
002D5141  74 5C                           je 0x1402d519f
002D5143  48 0F BC D3                     bsf rdx, rbx
002D5147  41 0F B7 C8                     movzx ecx, r8w
002D514B  0F B6 C2                        movzx eax, dl
002D514E  48 0F B3 C3                     btr rbx, rax
002D5152  C1 E1 06                        shl ecx, 6
002D5155  0F B6 C2                        movzx eax, dl
002D5158  03 C8                           add ecx, eax
002D515A  48 8B 05 57 E0 C4 00            mov rax, qword ptr [rip + 0xc4e057]
002D5161  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
002D5164  41 8B CC                        mov ecx, r12d
002D5167  89 45 50                        mov dword ptr [rbp + 0x50], eax
002D516A  85 C9                           test ecx, ecx
002D516C  78 5B                           js 0x1402d51c9
002D516E  3B 05 8C B0 B3 00               cmp eax, dword ptr [rip + 0xb3b08c]
002D5174  0F 83 DB 01 00 00               jae 0x1402d5355
002D517A  48 8B 0D 67 B0 B3 00            mov rcx, qword ptr [rip + 0xb3b067]
002D5181  48 8D 04 40                     lea rax, [rax + rax*2]
002D5185  83 3C C1 05                     cmp dword ptr [rcx + rax*8], 5
002D5189  0F 85 9F 00 00 00               jne 0x1402d522e
002D518F  8B 44 C1 08                     mov eax, dword ptr [rcx + rax*8 + 8]
002D5193  09 45 F0                        or dword ptr [rbp - 0x10], eax
002D5196  41 0F B7 C8                     movzx ecx, r8w
002D519A  41 03 CD                        add ecx, r13d
002D519D  EB 9F                           jmp 0x1402d513e
002D519F  66 45 03 C5                     add r8w, r13w
002D51A3  41 0F B7 C0                     movzx eax, r8w
002D51A7  66 89 45 E0                     mov word ptr [rbp - 0x20], ax
002D51AB  44 0F B7 C0                     movzx r8d, ax
002D51AF  3B C1                           cmp eax, ecx
002D51B1  0F 83 5E 01 00 00               jae 0x1402d5315
002D51B7  48 8B 1C C5 08 00 00 00         mov rbx, qword ptr [rax*8 + 8]
002D51BF  44 0F B7 45 E0                  movzx r8d, word ptr [rbp - 0x20]
002D51C4  E9 75 FF FF FF                  jmp 0x1402d513e
002D51C9  44 39 65 F0                     cmp dword ptr [rbp - 0x10], r12d
002D51CD  0F 85 31 FD FF FF               jne 0x1402d4f04
002D51D3  E9 19 FF FF FF                  jmp 0x1402d50f1
002D51D8  41 B9 0D 00 00 C0               mov r9d, 0xc000000d
002D51DE  44 89 0D BB B4 CB 00            mov dword ptr [rip + 0xcbb4bb], r9d
002D51E5  4C 8D 0D BC B8 D3 FF            lea r9, [rip - 0x2c4744]
002D51EC  4C 89 0D D5 B4 CB 00            mov qword ptr [rip + 0xcbb4d5], r9
002D51F3  4C 89 25 BE B4 CB 00            mov qword ptr [rip + 0xcbb4be], r12
002D51FA  C7 05 90 B4 CB 00 15 00 00 00   mov dword ptr [rip + 0xcbb490], 0x15
002D5204  C7 05 C2 B4 CB 00 20 05 00 00   mov dword ptr [rip + 0xcbb4c2], 0x520
002D520E  E9 DE FE FF FF                  jmp 0x1402d50f1
002D5213  C7 46 08 03 00 00 00            mov dword ptr [rsi + 8], 3
002D521A  44 89 7E 50                     mov dword ptr [rsi + 0x50], r15d
002D521E  E9 04 FD FF FF                  jmp 0x1402d4f27
002D5223  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
002D5226  41 8B C9                        mov ecx, r9d
002D5229  E9 9E FD FF FF                  jmp 0x1402d4fcc
002D522E  4C 8D 0D 73 B8 D3 FF            lea r9, [rip - 0x2c478d]
002D5235  4C 89 25 7C B4 CB 00            mov qword ptr [rip + 0xcbb47c], r12
002D523C  4C 89 0D 85 B4 CB 00            mov qword ptr [rip + 0xcbb485], r9
002D5243  C7 05 47 B4 CB 00 14 00 00 00   mov dword ptr [rip + 0xcbb447], 0x14
002D524D  44 89 25 4C B4 CB 00            mov dword ptr [rip + 0xcbb44c], r12d
002D5254  C7 05 72 B4 CB 00 46 05 00 00   mov dword ptr [rip + 0xcbb472], 0x546
002D525E  E9 8E FE FF FF                  jmp 0x1402d50f1
002D5263  44 38 65 40                     cmp byte ptr [rbp + 0x40], r12b
002D5267  0F 85 37 FC FF FF               jne 0x1402d4ea4
002D526D  4C 8D 0D 34 B8 D3 FF            lea r9, [rip - 0x2c47cc]
002D5274  4C 89 25 3D B4 CB 00            mov qword ptr [rip + 0xcbb43d], r12
002D527B  4C 89 0D 46 B4 CB 00            mov qword ptr [rip + 0xcbb446], r9
002D5282  C7 05 08 B4 CB 00 15 00 00 00   mov dword ptr [rip + 0xcbb408], 0x15
002D528C  C7 05 0A B4 CB 00 0D 00 00 C0   mov dword ptr [rip + 0xcbb40a], 0xc000000d
002D5296  C7 05 30 B4 CB 00 FC 04 00 00   mov dword ptr [rip + 0xcbb430], 0x4fc
002D52A0  E9 4C FE FF FF                  jmp 0x1402d50f1
002D52A5  41 B9 25 02 00 C0               mov r9d, 0xc0000225
002D52AB  44 89 0D EE B3 CB 00            mov dword ptr [rip + 0xcbb3ee], r9d
002D52B2  4C 8D 0D EF B7 D3 FF            lea r9, [rip - 0x2c4811]
002D52B9  4C 89 0D 08 B4 CB 00            mov qword ptr [rip + 0xcbb408], r9
002D52C0  4C 89 25 F1 B3 CB 00            mov qword ptr [rip + 0xcbb3f1], r12
002D52C7  C7 05 C3 B3 CB 00 15 00 00 00   mov dword ptr [rip + 0xcbb3c3], 0x15
002D52D1  C7 05 F5 B3 CB 00 15 05 00 00   mov dword ptr [rip + 0xcbb3f5], 0x515
002D52DB  E9 11 FE FF FF                  jmp 0x1402d50f1
002D52E0  4C 8D 0D C1 B7 D3 FF            lea r9, [rip - 0x2c483f]
002D52E7  4C 89 25 CA B3 CB 00            mov qword ptr [rip + 0xcbb3ca], r12
002D52EE  4C 89 0D D3 B3 CB 00            mov qword ptr [rip + 0xcbb3d3], r9
002D52F5  C7 05 95 B3 CB 00 14 00 00 00   mov dword ptr [rip + 0xcbb395], 0x14
002D52FF  44 89 25 9A B3 CB 00            mov dword ptr [rip + 0xcbb39a], r12d
002D5306  C7 05 C0 B3 CB 00 61 05 00 00   mov dword ptr [rip + 0xcbb3c0], 0x561
002D5310  E9 DC FD FF FF                  jmp 0x1402d50f1
002D5315  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
002D5318  41 8B C9                        mov ecx, r9d
002D531B  E9 4A FE FF FF                  jmp 0x1402d516a
002D5320  4C 8D 0D 81 B7 D3 FF            lea r9, [rip - 0x2c487f]
002D5327  4C 89 25 8A B3 CB 00            mov qword ptr [rip + 0xcbb38a], r12
002D532E  4C 89 0D 93 B3 CB 00            mov qword ptr [rip + 0xcbb393], r9
002D5335  C7 05 55 B3 CB 00 15 00 00 00   mov dword ptr [rip + 0xcbb355], 0x15
002D533F  44 89 25 5A B3 CB 00            mov dword ptr [rip + 0xcbb35a], r12d
002D5346  C7 05 80 B3 CB 00 6C 05 00 00   mov dword ptr [rip + 0xcbb380], 0x56c
002D5350  E9 9C FD FF FF                  jmp 0x1402d50f1
002D5355  4C 8D 0D 4C B7 D3 FF            lea r9, [rip - 0x2c48b4]
002D535C  4C 89 25 55 B3 CB 00            mov qword ptr [rip + 0xcbb355], r12
002D5363  4C 89 0D 5E B3 CB 00            mov qword ptr [rip + 0xcbb35e], r9
002D536A  C7 05 20 B3 CB 00 15 00 00 00   mov dword ptr [rip + 0xcbb320], 0x15
002D5374  89 0D 26 B3 CB 00               mov dword ptr [rip + 0xcbb326], ecx
002D537A  C7 05 4C B3 CB 00 3C 05 00 00   mov dword ptr [rip + 0xcbb34c], 0x53c
002D5384  E9 68 FD FF FF                  jmp 0x1402d50f1
002D5389  4C 8D 0D 18 B7 D3 FF            lea r9, [rip - 0x2c48e8]
002D5390  4C 89 25 21 B3 CB 00            mov qword ptr [rip + 0xcbb321], r12
002D5397  4C 89 0D 2A B3 CB 00            mov qword ptr [rip + 0xcbb32a], r9
002D539E  C7 05 EC B2 CB 00 14 00 00 00   mov dword ptr [rip + 0xcbb2ec], 0x14
002D53A8  44 89 25 F1 B2 CB 00            mov dword ptr [rip + 0xcbb2f1], r12d
002D53AF  C7 05 17 B3 CB 00 BA 05 00 00   mov dword ptr [rip + 0xcbb317], 0x5ba
002D53B9  E9 33 FD FF FF                  jmp 0x1402d50f1
002D53BE  C7 44 24 20 C0 04 00 00         mov dword ptr [rsp + 0x20], 0x4c0
002D53C6  E9 DF FC FF FF                  jmp 0x1402d50aa
002D53CB  C7 44 24 20 31 05 00 00         mov dword ptr [rsp + 0x20], 0x531
002D53D3  E9 D2 FC FF FF                  jmp 0x1402d50aa
002D53D8  45 85 C9                        test r9d, r9d
002D53DB  0F 88 2B 87 40 00               js 0x1406ddb0c
002D53E1  3B 0D 19 AE B3 00               cmp ecx, dword ptr [rip + 0xb3ae19]
002D53E7  0F 83 19 87 40 00               jae 0x1406ddb06
002D53ED  48 8D 55 D0                     lea rdx, [rbp - 0x30]
002D53F1  48 8D 4D 50                     lea rcx, [rbp + 0x50]
002D53F5  E8 86 00 14 00                  call 0x140415480
002D53FA  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
002D53FD  44 8B C8                        mov r9d, eax
002D5400  EB D6                           jmp 0x1402d53d8
002D5402  41 B9 25 02 00 C0               mov r9d, 0xc0000225
002D5408  E9 D1 FD FF FF                  jmp 0x1402d51de
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalGetMessageRoutingInfo(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_r12 = 0;
    v_stack_m58 = 0;
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((*(unsigned int *)(a1)) > ((unsigned int)(result + 1))) goto loc_002D53BE;
    a1 = (a1) + (16);
    if (*(unsigned __int64 *)(a1) == 0) goto loc_002D4F42;
    result = (*(unsigned __int64 *)(a1) - 1) ^ (*(unsigned __int64 *)(a1));
    result = (result) & (*(unsigned __int64 *)(a1));
    if (result != (*(unsigned __int64 *)(a1))) goto loc_002D4F42;
loc_002D4E6C:
    result = HalpInterruptAffinityIsSteerable(a1, v_stack_p8, a3, a4);
    if (sign_flag) goto loc_002D5042;
    v_stack_m58 = (unsigned __int16)(*(unsigned __int16 *)(a1 + 24));
    v_stack_m68 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) - ((unsigned int)(result + 1)));
    if (condition_is_not_equal) goto loc_002D4F4A;
    if ((unsigned __int8)((unsigned __int8)(result + 1)) == 0) goto loc_002D5263;
loc_002D4EA4:
    v_stack_p18 = 0;
loc_002D4EAC:
    if (*(unsigned __int64 *)(a1) == 0) goto loc_002D5076;
    a1 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 24))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(v_stack_p8))));
    v_stack_m60 = *(unsigned __int64 *)(a1);
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12903134) + a1 * 4)));
    if (v_stack_p8 != 0) goto loc_002D53D8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12903134) + a1 * 4)))) >= (*(unsigned int *)(v_rip + 11776784))) goto loc_002D51D8;
    result = HalpGetProcessorStateByNtIndex((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12903134) + a1 * 4)), v_stack_p8, *(unsigned __int16 *)(a1 + 24), 0);
    if (result == 0) goto loc_002D5402;
loc_002D4F04:
    *(unsigned int *)(a2) = (unsigned int)(result + 1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) != 0) goto loc_002D5213;
    *(unsigned int *)(a2 + 8) = (unsigned int)(result + 1);
    *(unsigned int *)(a2 + 84) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    *(unsigned int *)(a2 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)));
    *(unsigned int *)(a2 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
loc_002D4F27:
    result = 0;
loc_002D4F29:
    v_rsp = (v_rsp) + (96);
    return result;
loc_002D4F42:
    goto loc_002D4E6C;
loc_002D4F4A:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12903134) + a1 * 4))) - ((unsigned int)(result + 1)));
    if (condition_is_equal) goto loc_002D50FB;
    if (((unsigned int)(a1)) != ((unsigned int)(result + 1))) goto loc_002D5389;
    if ((*(unsigned __int8 *)(v_rip + 13350709)) == 0) goto loc_002D52E0;
loc_002D4F70:
    if (v_stack_p10 != 0) goto loc_002D4FA5;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 24)) + ((unsigned __int16)(result + 1)));
    v_stack_m58 = (unsigned __int16)((unsigned __int16)(a3));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(*(unsigned __int16 *)(a1 + 24) + result + 1 * 1))) goto loc_002D5223;
    goto loc_002D4F70;
loc_002D4FA0:
    if (*(unsigned __int64 *)((unsigned __int16)(a3) * 8 + 8) == 0) goto loc_002D5010;
loc_002D4FA5:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m58)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(v_stack_p8))));
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902901) + a1 * 4)));
loc_002D4FCC:
    if (sign_flag) goto loc_002D4F04;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902901) + a1 * 4)))) >= (*(unsigned int *)(v_rip + 11776550))) goto loc_002D5320;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11776513) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902901) + a1 * 4)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902901) + a1 * 4)) * 2 * 8)) != 6) goto loc_002D50C1;
    if (0 == 0) goto loc_002D503A;
    if (v_stack_m48 != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11776513) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902901) + a1 * 4)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902901) + a1 * 4)) * 2 * 8 + 8))))) goto loc_002D509C;
loc_002D5007:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m58)) + ((unsigned int)(result + 1)));
    goto loc_002D4FA0;
loc_002D5010:
    a3 = (unsigned __int16)((v_stack_m58) + ((unsigned __int16)(result + 1)));
    v_stack_m58 = (unsigned __int16)((unsigned __int16)(a3));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(a1))) goto loc_002D5223;
    goto loc_002D4FA0;
loc_002D503A:
loc_002D503D:
    v_stack_m48 = (unsigned int)((unsigned __int16)(a3));
    goto loc_002D5007;
loc_002D5042:
    *(unsigned __int64 *)(v_rip + 13350504) = 0;
    *(unsigned __int64 *)(v_rip + 13350513) = v_rip - 2901409;
    *(unsigned int *)(v_rip + 13350451) = 39;
    *(unsigned int *)(v_rip + 13350457) = (unsigned int)((unsigned __int16)(a3));
    *(unsigned int *)(v_rip + 13350495) = 0x4DAULL;
    goto loc_002D4F29;
loc_002D5076:
    a3 = (unsigned __int16)((v_stack_m58) + ((unsigned __int16)(result + 1)));
    v_stack_m58 = (unsigned __int16)((unsigned __int16)(a3));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(a1))) goto loc_002D52A5;
    goto loc_002D4EAC;
loc_002D509C:
    if (v_stack_p8 != 0) goto loc_002D503D;
    v_stack_p20 = 0x5A8ULL;
loc_002D50AA:
    a3 = 0;
    a1 = 0;
    result = HalpInterruptSetProblemEx(a1, a3 + 20, a3, v_rip - 2901516);
    goto loc_002D50F1;
loc_002D50C1:
    *(unsigned __int64 *)(v_rip + 13350377) = 0;
    *(unsigned __int64 *)(v_rip + 13350386) = v_rip - 2901536;
    *(unsigned int *)(v_rip + 13350324) = 20;
    *(unsigned int *)(v_rip + 13350329) = 0;
    *(unsigned int *)(v_rip + 13350367) = 0x57BULL;
loc_002D50F1:
    goto loc_002D4F29;
loc_002D50FB:
    if ((*(unsigned __int8 *)(v_rip + 13350294)) != 0) goto loc_002D53CB;
loc_002D510C:
    if (*(unsigned __int64 *)((unsigned __int16)(a3) * 8 + 8) != 0) goto loc_002D5143;
    a3 = (unsigned __int16)((a3) + ((unsigned __int16)(result + 1)));
    v_stack_m58 = (unsigned __int16)((unsigned __int16)(a3));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(a3 + result + 1 * 1))) goto loc_002D5315;
    goto loc_002D510C;
loc_002D513E:
    if (*(unsigned __int64 *)((unsigned __int16)(a3) * 8 + 8) == 0) goto loc_002D519F;
loc_002D5143:
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m58)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(a3 + 20))));
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902487) + a1 * 4)));
loc_002D516A:
    if (sign_flag) goto loc_002D51C9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902487) + a1 * 4)))) >= (*(unsigned int *)(v_rip + 11776140))) goto loc_002D5355;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11776103) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902487) + a1 * 4)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12902487) + a1 * 4)) * 2 * 8)) != 5) goto loc_002D522E;
    a1 = (unsigned int)(((unsigned __int16)(v_stack_m58)) + ((unsigned int)(result + 1)));
    goto loc_002D513E;
loc_002D519F:
    a3 = (unsigned __int16)((v_stack_m58) + ((unsigned __int16)(result + 1)));
    v_stack_m58 = (unsigned __int16)((unsigned __int16)(a3));
    if (((unsigned int)((unsigned __int16)(a3))) >= ((unsigned int)(a1))) goto loc_002D5315;
    goto loc_002D513E;
loc_002D51C9:
    if (v_stack_m48 != 0) goto loc_002D4F04;
    goto loc_002D50F1;
loc_002D51D8:
loc_002D51DE:
    *(unsigned int *)(v_rip + 13350075) = (unsigned int)((unsigned int)(0xC000000DULL));
    *(unsigned __int64 *)(v_rip + 13350101) = v_rip - 2901828;
    *(unsigned __int64 *)(v_rip + 13350078) = 0;
    *(unsigned int *)(v_rip + 13350032) = 21;
    *(unsigned int *)(v_rip + 13350082) = 0x520ULL;
    goto loc_002D50F1;
loc_002D5213:
    *(unsigned int *)(a2 + 8) = 3;
    *(unsigned int *)(a2 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    goto loc_002D4F27;
loc_002D5223:
    goto loc_002D4FCC;
loc_002D522E:
    *(unsigned __int64 *)(v_rip + 13350012) = 0;
    *(unsigned __int64 *)(v_rip + 13350021) = v_rip - 2901901;
    *(unsigned int *)(v_rip + 13349959) = 20;
    *(unsigned int *)(v_rip + 13349964) = 0;
    *(unsigned int *)(v_rip + 13350002) = 0x546ULL;
    goto loc_002D50F1;
loc_002D5263:
    if (v_stack_p8 != 0) goto loc_002D4EA4;
    *(unsigned __int64 *)(v_rip + 13349949) = 0;
    *(unsigned __int64 *)(v_rip + 13349958) = v_rip - 2901964;
    *(unsigned int *)(v_rip + 13349896) = 21;
    *(unsigned int *)(v_rip + 13349898) = 0xC000000DULL;
    *(unsigned int *)(v_rip + 13349936) = 0x4FCULL;
    goto loc_002D50F1;
loc_002D52A5:
    *(unsigned int *)(v_rip + 13349870) = (unsigned int)((unsigned int)(0xC0000225ULL));
    *(unsigned __int64 *)(v_rip + 13349896) = v_rip - 2902033;
    *(unsigned __int64 *)(v_rip + 13349873) = 0;
    *(unsigned int *)(v_rip + 13349827) = 21;
    *(unsigned int *)(v_rip + 13349877) = 0x515ULL;
    goto loc_002D50F1;
loc_002D52E0:
    *(unsigned __int64 *)(v_rip + 13349834) = 0;
    *(unsigned __int64 *)(v_rip + 13349843) = v_rip - 2902079;
    *(unsigned int *)(v_rip + 13349781) = 20;
    *(unsigned int *)(v_rip + 13349786) = 0;
    *(unsigned int *)(v_rip + 13349824) = 0x561ULL;
    goto loc_002D50F1;
loc_002D5315:
    goto loc_002D516A;
loc_002D5320:
    *(unsigned __int64 *)(v_rip + 13349770) = 0;
    *(unsigned __int64 *)(v_rip + 13349779) = v_rip - 2902143;
    *(unsigned int *)(v_rip + 13349717) = 21;
    *(unsigned int *)(v_rip + 13349722) = 0;
    *(unsigned int *)(v_rip + 13349760) = 0x56CULL;
    goto loc_002D50F1;
loc_002D5355:
    *(unsigned __int64 *)(v_rip + 13349717) = 0;
    *(unsigned __int64 *)(v_rip + 13349726) = v_rip - 2902196;
    *(unsigned int *)(v_rip + 13349664) = 21;
    *(unsigned int *)(v_rip + 13349670) = (unsigned int)((unsigned int)((unsigned int)(v_rip - 2902079)));
    *(unsigned int *)(v_rip + 13349708) = 0x53CULL;
    goto loc_002D50F1;
loc_002D5389:
    *(unsigned __int64 *)(v_rip + 13349665) = 0;
    *(unsigned __int64 *)(v_rip + 13349674) = v_rip - 2902248;
    *(unsigned int *)(v_rip + 13349612) = 20;
    *(unsigned int *)(v_rip + 13349617) = 0;
    *(unsigned int *)(v_rip + 13349655) = 0x5BAULL;
    goto loc_002D50F1;
loc_002D53BE:
    v_stack_p20 = 0x4C0ULL;
    goto loc_002D50AA;
loc_002D53CB:
    v_stack_p20 = 0x531ULL;
    goto loc_002D50AA;
loc_002D53D8:
    result = KeEnumerateNextProcessor(v_stack_p18, v_stack_m68, v_stack_m58, v_rip - 2902248);
    goto loc_002D53D8;
loc_002D5402:
    goto loc_002D51DE;
}
```

## 5. (Beta) C Style

```c
int64_t HalGetMessageRoutingInfo(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (96);
    result = 0;
    local_r12 = 0;
    v_stack_m58 = 0;
    v_stack_p18 = 0;
    v_stack_p8 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((*(uint32_t *)(arg1)) > ((uint32_t)(result + 1))) goto loc_002D53BE;
    Arg1 = (Arg1) + (16);
    if (*(uint64_t *)(arg1) == 0) goto loc_002D4F42;
    result = (*(uint64_t *)(arg1) - 1) ^ (*(uint64_t *)(arg1));
    result = (result) & (*(uint64_t *)(arg1));
    if (result != (*(uint64_t *)(arg1))) goto loc_002D4F42;
loc_002D4E6C:
    result = HalpInterruptAffinityIsSteerable(Arg1, v_stack_p8, a3, a4);
    if (sign_flag) goto loc_002D5042;
    v_stack_m58 = (uint16_t)(*(uint16_t *)(arg1 + 0x18));
    v_stack_m68 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) - ((uint32_t)(result + 1)));
    if (condition_is_not_equal) goto loc_002D4F4A;
    if ((uint8_t)((uint8_t)(result + 1)) == 0) goto loc_002D5263;
loc_002D4EA4:
    v_stack_p18 = 0;
loc_002D4EAC:
    if (*(uint64_t *)(arg1) == 0) goto loc_002D5076;
    Arg1 = (uint32_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x18))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(v_stack_p8))));
    v_stack_m60 = *(uint64_t *)(arg1);
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E2DE) + arg1 * 4)));
    if (v_stack_p8 != 0) goto loc_002D53D8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E2DE) + arg1 * 4)))) >= (*(uint32_t *)(v_rip + 0xB3B310))) goto loc_002D51D8;
    result = HalpGetProcessorStateByNtIndex((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E2DE) + arg1 * 4)), v_stack_p8, *(uint16_t *)(arg1 + 0x18), 0);
    if (result == 0) goto loc_002D5402;
loc_002D4F04:
    *(uint32_t *)(arg2) = (uint32_t)(result + 1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) != 0) goto loc_002D5213;
    *(uint32_t *)(arg2 + 0x8) = (uint32_t)(result + 1);
    *(uint32_t *)(arg2 + 0x54) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    *(uint32_t *)(arg2 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    *(uint32_t *)(arg2 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
loc_002D4F27:
    result = 0;
loc_002D4F29:
    local_rsp = (local_rsp) + (96);
    return result;
loc_002D4F42:
    goto loc_002D4E6C;
loc_002D4F4A:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E2DE) + arg1 * 4))) - ((uint32_t)(result + 1)));
    if (condition_is_equal) goto loc_002D50FB;
    if (((uint32_t)(Arg1)) != ((uint32_t)(result + 1))) goto loc_002D5389;
    if ((*(uint8_t *)(v_rip + 0xCBB735)) == 0) goto loc_002D52E0;
loc_002D4F70:
    if (v_stack_p10 != 0) goto loc_002D4FA5;
    a3 = (uint16_t)((*(uint16_t *)(arg1 + 0x18)) + ((uint16_t)(result + 1)));
    v_stack_m58 = (uint16_t)((uint16_t)(a3));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(*(uint16_t *)(arg1 + 0x18) + result + 1 * 1))) goto loc_002D5223;
    goto loc_002D4F70;
loc_002D4FA0:
    if (*(uint64_t *)((uint16_t)(a3) * 8 + 0x8) == 0) goto loc_002D5010;
loc_002D4FA5:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m58)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(v_stack_p8))));
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E1F5) + arg1 * 4)));
loc_002D4FCC:
    if (sign_flag) goto loc_002D4F04;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E1F5) + arg1 * 4)))) >= (*(uint32_t *)(v_rip + 0xB3B226))) goto loc_002D5320;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xB3B201) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E1F5) + arg1 * 4)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E1F5) + arg1 * 4)) * 2 * 8)) != 6) goto loc_002D50C1;
    if (0 == 0) goto loc_002D503A;
    if (v_stack_m48 != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB3B201) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E1F5) + arg1 * 4)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E1F5) + arg1 * 4)) * 2 * 8 + 0x8))))) goto loc_002D509C;
loc_002D5007:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m58)) + ((uint32_t)(result + 1)));
    goto loc_002D4FA0;
loc_002D5010:
    a3 = (uint16_t)((v_stack_m58) + ((uint16_t)(result + 1)));
    v_stack_m58 = (uint16_t)((uint16_t)(a3));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(Arg1))) goto loc_002D5223;
    goto loc_002D4FA0;
loc_002D503A:
loc_002D503D:
    v_stack_m48 = (uint32_t)((uint16_t)(a3));
    goto loc_002D5007;
loc_002D5042:
    *(uint64_t *)(v_rip + 0xCBB668) = 0;
    *(uint64_t *)(v_rip + 0xCBB671) = v_rip - 2901409;
    *(uint32_t *)(v_rip + 0xCBB633) = 39;
    *(uint32_t *)(v_rip + 0xCBB639) = (uint32_t)((uint16_t)(a3));
    *(uint32_t *)(v_rip + 0xCBB65F) = 0x4DAULL;
    goto loc_002D4F29;
loc_002D5076:
    a3 = (uint16_t)((v_stack_m58) + ((uint16_t)(result + 1)));
    v_stack_m58 = (uint16_t)((uint16_t)(a3));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(Arg1))) goto loc_002D52A5;
    goto loc_002D4EAC;
loc_002D509C:
    if (v_stack_p8 != 0) goto loc_002D503D;
    v_stack_p20 = 0x5A8ULL;
loc_002D50AA:
    a3 = 0;
    Arg1 = 0;
    result = HalpInterruptSetProblemEx(Arg1, a3 + 20, a3, v_rip - 2901516);
    goto loc_002D50F1;
loc_002D50C1:
    *(uint64_t *)(v_rip + 0xCBB5E9) = 0;
    *(uint64_t *)(v_rip + 0xCBB5F2) = v_rip - 2901536;
    *(uint32_t *)(v_rip + 0xCBB5B4) = 20;
    *(uint32_t *)(v_rip + 0xCBB5B9) = 0;
    *(uint32_t *)(v_rip + 0xCBB5DF) = 0x57BULL;
loc_002D50F1:
    goto loc_002D4F29;
loc_002D50FB:
    if ((*(uint8_t *)(v_rip + 0xCBB596)) != 0) goto loc_002D53CB;
loc_002D510C:
    if (*(uint64_t *)((uint16_t)(a3) * 8 + 0x8) != 0) goto loc_002D5143;
    a3 = (uint16_t)((a3) + ((uint16_t)(result + 1)));
    v_stack_m58 = (uint16_t)((uint16_t)(a3));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(a3 + result + 1 * 1))) goto loc_002D5315;
    goto loc_002D510C;
loc_002D513E:
    if (*(uint64_t *)((uint16_t)(a3) * 8 + 0x8) == 0) goto loc_002D519F;
loc_002D5143:
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m58)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(a3 + 20))));
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E057) + arg1 * 4)));
loc_002D516A:
    if (sign_flag) goto loc_002D51C9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E057) + arg1 * 4)))) >= (*(uint32_t *)(v_rip + 0xB3B08C))) goto loc_002D5355;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0xB3B067) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E057) + arg1 * 4)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC4E057) + arg1 * 4)) * 2 * 8)) != 5) goto loc_002D522E;
    Arg1 = (uint32_t)(((uint16_t)(v_stack_m58)) + ((uint32_t)(result + 1)));
    goto loc_002D513E;
loc_002D519F:
    a3 = (uint16_t)((v_stack_m58) + ((uint16_t)(result + 1)));
    v_stack_m58 = (uint16_t)((uint16_t)(a3));
    if (((uint32_t)((uint16_t)(a3))) >= ((uint32_t)(Arg1))) goto loc_002D5315;
    goto loc_002D513E;
loc_002D51C9:
    if (v_stack_m48 != 0) goto loc_002D4F04;
    goto loc_002D50F1;
loc_002D51D8:
loc_002D51DE:
    *(uint32_t *)(v_rip + 0xCBB4BB) = (uint32_t)((uint32_t)(0xC000000DULL));
    *(uint64_t *)(v_rip + 0xCBB4D5) = v_rip - 2901828;
    *(uint64_t *)(v_rip + 0xCBB4BE) = 0;
    *(uint32_t *)(v_rip + 0xCBB490) = 21;
    *(uint32_t *)(v_rip + 0xCBB4C2) = 0x520ULL;
    goto loc_002D50F1;
loc_002D5213:
    *(uint32_t *)(arg2 + 0x8) = 3;
    *(uint32_t *)(arg2 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    goto loc_002D4F27;
loc_002D5223:
    goto loc_002D4FCC;
loc_002D522E:
    *(uint64_t *)(v_rip + 0xCBB47C) = 0;
    *(uint64_t *)(v_rip + 0xCBB485) = v_rip - 2901901;
    *(uint32_t *)(v_rip + 0xCBB447) = 20;
    *(uint32_t *)(v_rip + 0xCBB44C) = 0;
    *(uint32_t *)(v_rip + 0xCBB472) = 0x546ULL;
    goto loc_002D50F1;
loc_002D5263:
    if (v_stack_p8 != 0) goto loc_002D4EA4;
    *(uint64_t *)(v_rip + 0xCBB43D) = 0;
    *(uint64_t *)(v_rip + 0xCBB446) = v_rip - 2901964;
    *(uint32_t *)(v_rip + 0xCBB408) = 21;
    *(uint32_t *)(v_rip + 0xCBB40A) = 0xC000000DULL;
    *(uint32_t *)(v_rip + 0xCBB430) = 0x4FCULL;
    goto loc_002D50F1;
loc_002D52A5:
    *(uint32_t *)(v_rip + 0xCBB3EE) = (uint32_t)((uint32_t)(0xC0000225ULL));
    *(uint64_t *)(v_rip + 0xCBB408) = v_rip - 2902033;
    *(uint64_t *)(v_rip + 0xCBB3F1) = 0;
    *(uint32_t *)(v_rip + 0xCBB3C3) = 21;
    *(uint32_t *)(v_rip + 0xCBB3F5) = 0x515ULL;
    goto loc_002D50F1;
loc_002D52E0:
    *(uint64_t *)(v_rip + 0xCBB3CA) = 0;
    *(uint64_t *)(v_rip + 0xCBB3D3) = v_rip - 2902079;
    *(uint32_t *)(v_rip + 0xCBB395) = 20;
    *(uint32_t *)(v_rip + 0xCBB39A) = 0;
    *(uint32_t *)(v_rip + 0xCBB3C0) = 0x561ULL;
    goto loc_002D50F1;
loc_002D5315:
    goto loc_002D516A;
loc_002D5320:
    *(uint64_t *)(v_rip + 0xCBB38A) = 0;
    *(uint64_t *)(v_rip + 0xCBB393) = v_rip - 2902143;
    *(uint32_t *)(v_rip + 0xCBB355) = 21;
    *(uint32_t *)(v_rip + 0xCBB35A) = 0;
    *(uint32_t *)(v_rip + 0xCBB380) = 0x56CULL;
    goto loc_002D50F1;
loc_002D5355:
    *(uint64_t *)(v_rip + 0xCBB355) = 0;
    *(uint64_t *)(v_rip + 0xCBB35E) = v_rip - 2902196;
    *(uint32_t *)(v_rip + 0xCBB320) = 21;
    *(uint32_t *)(v_rip + 0xCBB326) = (uint32_t)((uint32_t)((uint32_t)(v_rip - 2902079)));
    *(uint32_t *)(v_rip + 0xCBB34C) = 0x53CULL;
    goto loc_002D50F1;
loc_002D5389:
    *(uint64_t *)(v_rip + 0xCBB321) = 0;
    *(uint64_t *)(v_rip + 0xCBB32A) = v_rip - 2902248;
    *(uint32_t *)(v_rip + 0xCBB2EC) = 20;
    *(uint32_t *)(v_rip + 0xCBB2F1) = 0;
    *(uint32_t *)(v_rip + 0xCBB317) = 0x5BAULL;
    goto loc_002D50F1;
loc_002D53BE:
    v_stack_p20 = 0x4C0ULL;
    goto loc_002D50AA;
loc_002D53CB:
    v_stack_p20 = 0x531ULL;
    goto loc_002D50AA;
loc_002D53D8:
    result = KeEnumerateNextProcessor(v_stack_p18, v_stack_m68, v_stack_m58, v_rip - 2902248);
    goto loc_002D53D8;
loc_002D5402:
    goto loc_002D51DE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x18` | `16` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x8` | `32` | `W` |
| `Arg2` | `+ 0x50` | `32` | `W` |
| `Arg2` | `+ 0x54` | `32` | `W` |
| `Arg2` | `+ 0x58` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D4E00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
