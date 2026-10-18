# Xp10ExecuteLz77PassMinMatchLen3

- RVA: `0x0079859C`–`0x00798CEE` (길이 `1,874` bytes)
- VA: `0x000000014079859C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BECA4`
- 디코드: `492`개 명령, `1,874/1,874` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [Xp10CompressBuffer](Xp10CompressBuffer_function_007972F4.md) at `0x00797479`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079859C  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
007985A1  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
007985A6  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
007985AB  53                              push rbx
007985AC  55                              push rbp
007985AD  56                              push rsi
007985AE  57                              push rdi
007985AF  41 54                           push r12
007985B1  41 55                           push r13
007985B3  41 56                           push r14
007985B5  41 57                           push r15
007985B7  48 83 EC 58                     sub rsp, 0x58
007985BB  48 8B 01                        mov rax, qword ptr [rcx]
007985BE  4C 8B D1                        mov r10, rcx
007985C1  45 33 F6                        xor r14d, r14d
007985C4  49 8B E8                        mov rbp, r8
007985C7  4D 8B D9                        mov r11, r9
007985CA  44 89 34 24                     mov dword ptr [rsp], r14d
007985CE  4C 8D 42 01                     lea r8, [rdx + 1]
007985D2  0F B7 08                        movzx ecx, word ptr [rax]
007985D5  49 8D BA 20 16 00 00            lea rdi, [r10 + 0x1620]
007985DC  83 E1 1F                        and ecx, 0x1f
007985DF  45 89 72 18                     mov dword ptr [r10 + 0x18], r14d
007985E3  41 8D 46 01                     lea eax, [r14 + 1]
007985E7  D3 E0                           shl eax, cl
007985E9  B9 F2 0E 00 00                  mov ecx, 0xef2
007985EE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007985F2  48 8B C2                        mov rax, rdx
007985F5  F3 48 AB                        rep stosq qword ptr [rdi], rax
007985F8  49 8D BA B0 8D 00 00            lea rdi, [r10 + 0x8db0]
007985FF  B9 EE 12 00 00                  mov ecx, 0x12ee
00798604  F3 48 AB                        rep stosq qword ptr [rdi], rax
00798607  0F B6 02                        movzx eax, byte ptr [rdx]
0079860A  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00798612  66 41 89 01                     mov word ptr [r9], ax
00798616  48 83 C1 F1                     add rcx, -0xf
0079861A  49 83 C1 02                     add r9, 2
0079861E  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00798623  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
00798628  48 8D 45 D8                     lea rax, [rbp - 0x28]
0079862C  4C 89 4C 24 08                  mov qword ptr [rsp + 8], r9
00798631  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00798636  4C 3B C0                        cmp r8, rax
00798639  0F 83 54 06 00 00               jae 0x140798c93
0079863F  4C 3B C9                        cmp r9, rcx
00798642  0F 83 43 06 00 00               jae 0x140798c8b
00798648  44 8B 4C 24 20                  mov r9d, dword ptr [rsp + 0x20]
0079864D  4D 8D 7A 08                     lea r15, [r10 + 8]
00798651  49 8B D8                        mov rbx, r8
00798654  44 89 74 24 04                  mov dword ptr [rsp + 4], r14d
00798659  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0079865E  4D 8B E8                        mov r13, r8
00798661  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00798666  44 89 74 24 1C                  mov dword ptr [rsp + 0x1c], r14d
0079866B  44 89 74 24 18                  mov dword ptr [rsp + 0x18], r14d
00798670  41 0F B6 48 02                  movzx ecx, byte ptr [r8 + 2]
00798675  4D 8D 70 01                     lea r14, [r8 + 1]
00798679  41 0F B6 06                     movzx eax, byte ptr [r14]
0079867D  C1 E0 03                        shl eax, 3
00798680  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00798685  8D 14 48                        lea edx, [rax + rcx*2]
00798688  41 0F B6 00                     movzx eax, byte ptr [r8]
0079868C  03 D0                           add edx, eax
0079868E  4D 8B 9C D2 20 16 00 00         mov r11, qword ptr [r10 + rdx*8 + 0x1620]
00798696  4D 89 84 D2 20 16 00 00         mov qword ptr [r10 + rdx*8 + 0x1620], r8
0079869E  41 8A 00                        mov al, byte ptr [r8]
007986A1  41 38 03                        cmp byte ptr [r11], al
007986A4  0F 85 4B 03 00 00               jne 0x1407989f5
007986AA  41 8A 06                        mov al, byte ptr [r14]
007986AD  41 38 43 01                     cmp byte ptr [r11 + 1], al
007986B1  0F 85 3E 03 00 00               jne 0x1407989f5
007986B7  41 8A 40 02                     mov al, byte ptr [r8 + 2]
007986BB  41 38 43 02                     cmp byte ptr [r11 + 2], al
007986BF  0F 85 30 03 00 00               jne 0x1407989f5
007986C5  41 8B C0                        mov eax, r8d
007986C8  41 2B C3                        sub eax, r11d
007986CB  41 3B C1                        cmp eax, r9d
007986CE  0F 83 21 03 00 00               jae 0x1407989f5
007986D4  4D 3B C3                        cmp r8, r11
007986D7  0F 84 18 03 00 00               je 0x1407989f5
007986DD  41 0F B6 7B 03                  movzx edi, byte ptr [r11 + 3]
007986E2  BB 01 00 00 00                  mov ebx, 1
007986E7  41 0F B6 40 03                  movzx eax, byte ptr [r8 + 3]
007986EC  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
007986F3  40 3A F8                        cmp dil, al
007986F6  74 54                           je 0x14079874c
007986F8  03 C2                           add eax, edx
007986FA  49 8B 8C C2 B0 8D 00 00         mov rcx, qword ptr [r10 + rax*8 + 0x8db0]
00798702  8D 04 3A                        lea eax, [rdx + rdi]
00798705  4D 89 9C C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r11
0079870D  41 8B 00                        mov eax, dword ptr [r8]
00798710  39 01                           cmp dword ptr [rcx], eax
00798712  0F 85 21 02 00 00               jne 0x140798939
00798718  41 0F B6 78 03                  movzx edi, byte ptr [r8 + 3]
0079871D  40 38 79 03                     cmp byte ptr [rcx + 3], dil
00798721  0F 85 12 02 00 00               jne 0x140798939
00798727  41 8B C0                        mov eax, r8d
0079872A  2B C1                           sub eax, ecx
0079872C  41 3B C1                        cmp eax, r9d
0079872F  0F 83 04 02 00 00               jae 0x140798939
00798735  4C 3B C1                        cmp r8, rcx
00798738  0F 84 FB 01 00 00               je 0x140798939
0079873E  8D 04 3A                        lea eax, [rdx + rdi]
00798741  4C 8B D9                        mov r11, rcx
00798744  4D 89 84 C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r8
0079874C  41 0F B6 5B 04                  movzx ebx, byte ptr [r11 + 4]
00798751  41 0F B6 70 04                  movzx esi, byte ptr [r8 + 4]
00798756  40 3A DE                        cmp bl, sil
00798759  0F 84 83 00 00 00               je 0x1407987e2
0079875F  41 8A 38                        mov dil, byte ptr [r8]
00798762  41 8A 16                        mov dl, byte ptr [r14]
00798765  8D 42 61                        lea eax, [rdx + 0x61]
00798768  41 02 40 02                     add al, byte ptr [r8 + 2]
0079876C  D0 C8                           ror al, 1
0079876E  40 32 C7                        xor al, dil
00798771  41 02 78 03                     add dil, byte ptr [r8 + 3]
00798775  C0 C0 03                        rol al, 3
00798778  0F B6 C8                        movzx ecx, al
0079877B  40 C0 C7 03                     rol dil, 3
0079877F  40 32 FA                        xor dil, dl
00798782  40 D0 CF                        ror dil, 1
00798785  40 0F B6 C7                     movzx eax, dil
00798789  8D 3C 88                        lea edi, [rax + rcx*4]
0079878C  03 FF                           add edi, edi
0079878E  8D 04 37                        lea eax, [rdi + rsi]
00798791  49 8B 8C C2 B0 8D 00 00         mov rcx, qword ptr [r10 + rax*8 + 0x8db0]
00798799  8D 04 1F                        lea eax, [rdi + rbx]
0079879C  4D 89 9C C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r11
007987A4  8B 01                           mov eax, dword ptr [rcx]
007987A6  41 39 00                        cmp dword ptr [r8], eax
007987A9  0F 85 91 01 00 00               jne 0x140798940
007987AF  41 0F B6 50 04                  movzx edx, byte ptr [r8 + 4]
007987B4  3A 51 04                        cmp dl, byte ptr [rcx + 4]
007987B7  0F 85 83 01 00 00               jne 0x140798940
007987BD  41 8B C0                        mov eax, r8d
007987C0  2B C1                           sub eax, ecx
007987C2  41 3B C1                        cmp eax, r9d
007987C5  0F 83 75 01 00 00               jae 0x140798940
007987CB  4C 3B C1                        cmp r8, rcx
007987CE  0F 84 6C 01 00 00               je 0x140798940
007987D4  8D 04 17                        lea eax, [rdi + rdx]
007987D7  4C 8B D9                        mov r11, rcx
007987DA  4D 89 84 C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r8
007987E2  41 0F B6 58 05                  movzx ebx, byte ptr [r8 + 5]
007987E7  41 0F B6 73 05                  movzx esi, byte ptr [r11 + 5]
007987EC  40 3A DE                        cmp bl, sil
007987EF  0F 84 9B 00 00 00               je 0x140798890
007987F5  41 8A 48 04                     mov cl, byte ptr [r8 + 4]
007987F9  41 8A 38                        mov dil, byte ptr [r8]
007987FC  40 8A C7                        mov al, dil
007987FF  40 D2 C7                        rol dil, cl
00798802  D0 C8                           ror al, 1
00798804  04 45                           add al, 0x45
00798806  32 C1                           xor al, cl
00798808  40 0F B6 CF                     movzx ecx, dil
0079880C  C0 C0 03                        rol al, 3
0079880F  0F B6 D0                        movzx edx, al
00798812  41 8A 40 03                     mov al, byte ptr [r8 + 3]
00798816  C0 C0 03                        rol al, 3
00798819  41 32 06                        xor al, byte ptr [r14]
0079881C  D0 C8                           ror al, 1
0079881E  0F B6 C0                        movzx eax, al
00798821  03 D0                           add edx, eax
00798823  41 0F B6 40 02                  movzx eax, byte ptr [r8 + 2]
00798828  33 C8                           xor ecx, eax
0079882A  8D 3C 91                        lea edi, [rcx + rdx*4]
0079882D  03 FF                           add edi, edi
0079882F  8D 04 1F                        lea eax, [rdi + rbx]
00798832  49 8B 8C C2 B0 8D 00 00         mov rcx, qword ptr [r10 + rax*8 + 0x8db0]
0079883A  8D 04 37                        lea eax, [rdi + rsi]
0079883D  4D 89 9C C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r11
00798845  8B 01                           mov eax, dword ptr [rcx]
00798847  41 39 00                        cmp dword ptr [r8], eax
0079884A  0F 85 57 01 00 00               jne 0x1407989a7
00798850  8A 41 04                        mov al, byte ptr [rcx + 4]
00798853  41 38 40 04                     cmp byte ptr [r8 + 4], al
00798857  0F 85 4A 01 00 00               jne 0x1407989a7
0079885D  41 0F B6 50 05                  movzx edx, byte ptr [r8 + 5]
00798862  3A 51 05                        cmp dl, byte ptr [rcx + 5]
00798865  0F 85 3C 01 00 00               jne 0x1407989a7
0079886B  41 8B C0                        mov eax, r8d
0079886E  2B C1                           sub eax, ecx
00798870  41 3B C1                        cmp eax, r9d
00798873  0F 83 2E 01 00 00               jae 0x1407989a7
00798879  4C 3B C1                        cmp r8, rcx
0079887C  0F 84 25 01 00 00               je 0x1407989a7
00798882  8D 04 17                        lea eax, [rdi + rdx]
00798885  4C 8B D9                        mov r11, rcx
00798888  4D 89 84 C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r8
00798890  49 8D 58 06                     lea rbx, [r8 + 6]
00798894  49 8B C3                        mov rax, r11
00798897  49 2B C0                        sub rax, r8
0079889A  48 8D 53 08                     lea rdx, [rbx + 8]
0079889E  48 03 D0                        add rdx, rax
007988A1  49 8B F8                        mov rdi, r8
007988A4  49 2B FB                        sub rdi, r11
007988A7  B9 06 00 00 00                  mov ecx, 6
007988AC  48 8D 45 D8                     lea rax, [rbp - 0x28]
007988B0  48 3B D8                        cmp rbx, rax
007988B3  0F 83 16 01 00 00               jae 0x1407989cf
007988B9  41 8D 41 E0                     lea eax, [r9 - 0x20]
007988BD  3B C8                           cmp ecx, eax
007988BF  0F 83 0A 01 00 00               jae 0x1407989cf
007988C5  8B 42 F8                        mov eax, dword ptr [rdx - 8]
007988C8  39 03                           cmp dword ptr [rbx], eax
007988CA  0F 85 FF 00 00 00               jne 0x1407989cf
007988D0  8B 42 FC                        mov eax, dword ptr [rdx - 4]
007988D3  39 44 17 FC                     cmp dword ptr [rdi + rdx - 4], eax
007988D7  0F 85 EF 00 00 00               jne 0x1407989cc
007988DD  8B 02                           mov eax, dword ptr [rdx]
007988DF  39 04 3A                        cmp dword ptr [rdx + rdi], eax
007988E2  0F 85 DF 00 00 00               jne 0x1407989c7
007988E8  8B 42 04                        mov eax, dword ptr [rdx + 4]
007988EB  39 44 17 04                     cmp dword ptr [rdi + rdx + 4], eax
007988EF  0F 85 CD 00 00 00               jne 0x1407989c2
007988F5  8B 42 08                        mov eax, dword ptr [rdx + 8]
007988F8  39 44 17 08                     cmp dword ptr [rdi + rdx + 8], eax
007988FC  0F 85 BB 00 00 00               jne 0x1407989bd
00798902  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
00798905  39 44 17 0C                     cmp dword ptr [rdi + rdx + 0xc], eax
00798909  0F 85 A9 00 00 00               jne 0x1407989b8
0079890F  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
00798912  39 44 17 10                     cmp dword ptr [rdi + rdx + 0x10], eax
00798916  0F 85 97 00 00 00               jne 0x1407989b3
0079891C  8B 42 14                        mov eax, dword ptr [rdx + 0x14]
0079891F  39 44 17 14                     cmp dword ptr [rdi + rdx + 0x14], eax
00798923  0F 85 85 00 00 00               jne 0x1407989ae
00798929  83 C1 20                        add ecx, 0x20
0079892C  48 83 C3 20                     add rbx, 0x20
00798930  48 83 C2 20                     add rdx, 0x20
00798934  E9 73 FF FF FF                  jmp 0x1407988ac
00798939  B9 03 00 00 00                  mov ecx, 3
0079893E  EB 0C                           jmp 0x14079894c
00798940  B9 04 00 00 00                  mov ecx, 4
00798945  8B 9C 24 A8 00 00 00            mov ebx, dword ptr [rsp + 0xa8]
0079894C  45 8A 30                        mov r14b, byte ptr [r8]
0079894F  49 8B EF                        mov rbp, r15
00798952  44 8B 3C 24                     mov r15d, dword ptr [rsp]
00798956  33 F6                           xor esi, esi
00798958  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
00798960  4C 8B 64 24 28                  mov r12, qword ptr [rsp + 0x28]
00798965  8B 45 00                        mov eax, dword ptr [rbp]
00798968  49 8B D0                        mov rdx, r8
0079896B  48 2B D0                        sub rdx, rax
0079896E  44 38 32                        cmp byte ptr [rdx], r14b
00798971  0F 85 C4 00 00 00               jne 0x140798a3b
00798977  41 8A 04 24                     mov al, byte ptr [r12]
0079897B  38 42 01                        cmp byte ptr [rdx + 1], al
0079897E  0F 85 B7 00 00 00               jne 0x140798a3b
00798984  41 8A 40 02                     mov al, byte ptr [r8 + 2]
00798988  38 42 02                        cmp byte ptr [rdx + 2], al
0079898B  0F 85 AA 00 00 00               jne 0x140798a3b
00798991  49 3B D0                        cmp rdx, r8
00798994  0F 84 A1 00 00 00               je 0x140798a3b
0079899A  B8 03 00 00 00                  mov eax, 3
0079899F  49 8D 58 03                     lea rbx, [r8 + 3]
007989A3  8B F8                           mov edi, eax
007989A5  EB 6E                           jmp 0x140798a15
007989A7  B9 05 00 00 00                  mov ecx, 5
007989AC  EB 97                           jmp 0x140798945
007989AE  83 C1 1C                        add ecx, 0x1c
007989B1  EB 1C                           jmp 0x1407989cf
007989B3  83 C1 18                        add ecx, 0x18
007989B6  EB 17                           jmp 0x1407989cf
007989B8  83 C1 14                        add ecx, 0x14
007989BB  EB 12                           jmp 0x1407989cf
007989BD  83 C1 10                        add ecx, 0x10
007989C0  EB 0D                           jmp 0x1407989cf
007989C2  83 C1 0C                        add ecx, 0xc
007989C5  EB 08                           jmp 0x1407989cf
007989C7  83 C1 08                        add ecx, 8
007989CA  EB 03                           jmp 0x1407989cf
007989CC  83 C1 04                        add ecx, 4
007989CF  8B C1                           mov eax, ecx
007989D1  4A 8D 14 00                     lea rdx, [rax + r8]
007989D5  EB 14                           jmp 0x1407989eb
007989D7  42 8A 04 18                     mov al, byte ptr [rax + r11]
007989DB  38 02                           cmp byte ptr [rdx], al
007989DD  0F 85 62 FF FF FF               jne 0x140798945
007989E3  FF C1                           inc ecx
007989E5  8B C1                           mov eax, ecx
007989E7  4A 8D 14 01                     lea rdx, [rcx + r8]
007989EB  48 3B D5                        cmp rdx, rbp
007989EE  72 E7                           jb 0x1407989d7
007989F0  E9 50 FF FF FF                  jmp 0x140798945
007989F5  33 DB                           xor ebx, ebx
007989F7  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
007989FE  8D 4B 01                        lea ecx, [rbx + 1]
00798A01  E9 46 FF FF FF                  jmp 0x14079894c
00798A06  8A 04 10                        mov al, byte ptr [rax + rdx]
00798A09  38 03                           cmp byte ptr [rbx], al
00798A0B  75 0D                           jne 0x140798a1a
00798A0D  FF C7                           inc edi
00798A0F  8B C7                           mov eax, edi
00798A11  4A 8D 1C 07                     lea rbx, [rdi + r8]
00798A15  49 3B DA                        cmp rbx, r10
00798A18  72 EC                           jb 0x140798a06
00798A1A  3B F9                           cmp edi, ecx
00798A1C  72 16                           jb 0x140798a34
00798A1E  BB 02 00 00 00                  mov ebx, 2
00798A23  4C 8B DA                        mov r11, rdx
00798A26  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
00798A2D  44 8B FE                        mov r15d, esi
00798A30  8B CF                           mov ecx, edi
00798A32  EB 07                           jmp 0x140798a3b
00798A34  8B 9C 24 A8 00 00 00            mov ebx, dword ptr [rsp + 0xa8]
00798A3B  FF C6                           inc esi
00798A3D  48 83 C5 04                     add rbp, 4
00798A41  83 FE 04                        cmp esi, 4
00798A44  0F 82 1B FF FF FF               jb 0x140798965
00798A4A  3B 4C 24 1C                     cmp ecx, dword ptr [rsp + 0x1c]
00798A4E  45 8B F7                        mov r14d, r15d
00798A51  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
00798A59  8B F1                           mov esi, ecx
00798A5B  0F 42 5C 24 04                  cmovb ebx, dword ptr [rsp + 4]
00798A60  4D 0F 42 C5                     cmovb r8, r13
00798A64  44 0F 42 74 24 18               cmovb r14d, dword ptr [rsp + 0x18]
00798A6A  4D 8B E8                        mov r13, r8
00798A6D  0F 42 74 24 1C                  cmovb esi, dword ptr [rsp + 0x1c]
00798A72  4D 8B C4                        mov r8, r12
00798A75  4C 0F 42 5C 24 10               cmovb r11, qword ptr [rsp + 0x10]
00798A7B  49 8B C0                        mov rax, r8
00798A7E  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
00798A83  8B FB                           mov edi, ebx
00798A85  48 8B AC 24 B0 00 00 00         mov rbp, qword ptr [rsp + 0xb0]
00798A8D  49 2B C4                        sub rax, r12
00798A90  44 89 3C 24                     mov dword ptr [rsp], r15d
00798A94  4D 8D 7A 08                     lea r15, [r10 + 8]
00798A98  44 89 74 24 18                  mov dword ptr [rsp + 0x18], r14d
00798A9D  89 5C 24 04                     mov dword ptr [rsp + 4], ebx
00798AA1  4C 89 5C 24 10                  mov qword ptr [rsp + 0x10], r11
00798AA6  89 74 24 1C                     mov dword ptr [rsp + 0x1c], esi
00798AAA  48 83 F8 02                     cmp rax, 2
00798AAE  0F 8E BC FB FF FF               jle 0x140798670
00798AB4  4C 8B 4C 24 08                  mov r9, qword ptr [rsp + 8]
00798AB9  41 8B EE                        mov ebp, r14d
00798ABC  89 2C 24                        mov dword ptr [rsp], ebp
00798ABF  EB 1B                           jmp 0x140798adc
00798AC1  41 0F B6 04 24                  movzx eax, byte ptr [r12]
00798AC6  49 8B C9                        mov rcx, r9
00798AC9  66 41 89 01                     mov word ptr [r9], ax
00798ACD  49 83 C1 02                     add r9, 2
00798AD1  0F B7 01                        movzx eax, word ptr [rcx]
00798AD4  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
00798AD9  49 FF C4                        inc r12
00798ADC  4D 3B E5                        cmp r12, r13
00798ADF  72 E0                           jb 0x140798ac1
00798AE1  45 33 F6                        xor r14d, r14d
00798AE4  49 8B D9                        mov rbx, r9
00798AE7  45 8B DE                        mov r11d, r14d
00798AEA  8B CF                           mov ecx, edi
00798AEC  85 FF                           test edi, edi
00798AEE  0F 84 5C 01 00 00               je 0x140798c50
00798AF4  83 E9 01                        sub ecx, 1
00798AF7  0F 84 AA 00 00 00               je 0x140798ba7
00798AFD  83 F9 01                        cmp ecx, 1
00798B00  75 3C                           jne 0x140798b3e
00798B02  8D 41 0F                        lea eax, [rcx + 0xf]
00798B05  03 C5                           add eax, ebp
00798B07  66 C1 E0 04                     shl ax, 4
00798B0B  66 41 89 01                     mov word ptr [r9], ax
00798B0F  41 8B 54 AA 08                  mov edx, dword ptr [r10 + rbp*4 + 8]
00798B14  85 ED                           test ebp, ebp
00798B16  74 26                           je 0x140798b3e
00798B18  49 8D 4F 08                     lea rcx, [r15 + 8]
00798B1C  83 FD 03                        cmp ebp, 3
00798B1F  72 08                           jb 0x140798b29
00798B21  8B 01                           mov eax, dword ptr [rcx]
00798B23  41 89 47 0C                     mov dword ptr [r15 + 0xc], eax
00798B27  EB 05                           jmp 0x140798b2e
00798B29  83 FD 02                        cmp ebp, 2
00798B2C  72 06                           jb 0x140798b34
00798B2E  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
00798B32  89 01                           mov dword ptr [rcx], eax
00798B34  41 8B 07                        mov eax, dword ptr [r15]
00798B37  41 89 47 04                     mov dword ptr [r15 + 4], eax
00798B3B  41 89 17                        mov dword ptr [r15], edx
00798B3E  48 8B 6C 24 10                  mov rbp, qword ptr [rsp + 0x10]
00798B43  41 0F B7 01                     movzx eax, word ptr [r9]
00798B47  8D 7E FD                        lea edi, [rsi - 3]
00798B4A  41 BF 0F 00 00 00               mov r15d, 0xf
00798B50  41 3B FF                        cmp edi, r15d
00798B53  0F 82 AE 00 00 00               jb 0x140798c07
00798B59  66 41 03 C7                     add ax, r15w
00798B5D  4D 8D 41 02                     lea r8, [r9 + 2]
00798B61  66 41 89 01                     mov word ptr [r9], ax
00798B65  4D 8D 48 01                     lea r9, [r8 + 1]
00798B69  4C 89 4C 24 08                  mov qword ptr [rsp + 8], r9
00798B6E  81 FF F6 00 00 00               cmp edi, 0xf6
00798B74  76 78                           jbe 0x140798bee
00798B76  81 C7 0A FF FF FF               add edi, 0xffffff0a
00798B7C  44 89 B4 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r14d
00798B84  0F BD CF                        bsr ecx, edi
00798B87  8D 41 E8                        lea eax, [rcx - 0x18]
00798B8A  41 88 00                        mov byte ptr [r8], al
00798B8D  83 FF 01                        cmp edi, 1
00798B90  76 67                           jbe 0x140798bf9
00798B92  41 01 4A 18                     add dword ptr [r10 + 0x18], ecx
00798B96  41 8D 47 F2                     lea eax, [r15 - 0xe]
00798B9A  D3 E0                           shl eax, cl
00798B9C  2B F8                           sub edi, eax
00798B9E  41 89 39                        mov dword ptr [r9], edi
00798BA1  49 83 C1 04                     add r9, 4
00798BA5  EB 4D                           jmp 0x140798bf4
00798BA7  48 8B 6C 24 10                  mov rbp, qword ptr [rsp + 0x10]
00798BAC  41 8B CD                        mov ecx, r13d
00798BAF  2B CD                           sub ecx, ebp
00798BB1  44 89 B4 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r14d
00798BB9  44 0F BD D9                     bsr r11d, ecx
00798BBD  B8 14 00 00 00                  mov eax, 0x14
00798BC2  41 03 C3                        add eax, r11d
00798BC5  66 C1 E0 04                     shl ax, 4
00798BC9  66 41 89 01                     mov word ptr [r9], ax
00798BCD  41 8B 42 10                     mov eax, dword ptr [r10 + 0x10]
00798BD1  41 89 42 14                     mov dword ptr [r10 + 0x14], eax
00798BD5  41 8B 42 0C                     mov eax, dword ptr [r10 + 0xc]
00798BD9  41 89 42 10                     mov dword ptr [r10 + 0x10], eax
00798BDD  41 8B 42 08                     mov eax, dword ptr [r10 + 8]
00798BE1  41 89 42 0C                     mov dword ptr [r10 + 0xc], eax
00798BE5  41 89 4A 08                     mov dword ptr [r10 + 8], ecx
00798BE9  E9 55 FF FF FF                  jmp 0x140798b43
00798BEE  41 2A FF                        sub dil, r15b
00798BF1  41 88 38                        mov byte ptr [r8], dil
00798BF4  4C 89 4C 24 08                  mov qword ptr [rsp + 8], r9
00798BF9  41 0F B6 00                     movzx eax, byte ptr [r8]
00798BFD  41 FF 84 82 1C 0B 00 00         inc dword ptr [r10 + rax*4 + 0xb1c]
00798C05  EB 10                           jmp 0x140798c17
00798C07  66 03 F8                        add di, ax
00798C0A  66 41 89 39                     mov word ptr [r9], di
00798C0E  49 83 C1 02                     add r9, 2
00798C12  4C 89 4C 24 08                  mov qword ptr [rsp + 8], r9
00798C17  0F B7 03                        movzx eax, word ptr [rbx]
00798C1A  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
00798C1F  83 7C 24 04 01                  cmp dword ptr [rsp + 4], 1
00798C24  75 26                           jne 0x140798c4c
00798C26  45 85 DB                        test r11d, r11d
00798C29  74 21                           je 0x140798c4c
00798C2B  45 01 5A 18                     add dword ptr [r10 + 0x18], r11d
00798C2F  41 8B CB                        mov ecx, r11d
00798C32  B8 01 00 00 00                  mov eax, 1
00798C37  D3 E0                           shl eax, cl
00798C39  41 8B CD                        mov ecx, r13d
00798C3C  2B C8                           sub ecx, eax
00798C3E  2B CD                           sub ecx, ebp
00798C40  41 89 09                        mov dword ptr [r9], ecx
00798C43  49 83 C1 04                     add r9, 4
00798C47  4C 89 4C 24 08                  mov qword ptr [rsp + 8], r9
00798C4C  8B C6                           mov eax, esi
00798C4E  EB 1F                           jmp 0x140798c6f
00798C50  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00798C55  66 41 89 01                     mov word ptr [r9], ax
00798C59  49 83 C1 02                     add r9, 2
00798C5D  0F B7 03                        movzx eax, word ptr [rbx]
00798C60  4C 89 4C 24 08                  mov qword ptr [rsp + 8], r9
00798C65  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
00798C6A  B8 01 00 00 00                  mov eax, 1
00798C6F  48 8B AC 24 B0 00 00 00         mov rbp, qword ptr [rsp + 0xb0]
00798C77  4E 8D 04 28                     lea r8, [rax + r13]
00798C7B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00798C80  4C 3B 44 24 38                  cmp r8, qword ptr [rsp + 0x38]
00798C85  0F 82 B4 F9 FF FF               jb 0x14079863f
00798C8B  4C 8B 9C 24 B8 00 00 00         mov r11, qword ptr [rsp + 0xb8]
00798C93  4C 3B C5                        cmp r8, rbp
00798C96  73 34                           jae 0x140798ccc
00798C98  4C 8B 9C 24 C0 00 00 00         mov r11, qword ptr [rsp + 0xc0]
00798CA0  4D 3B CB                        cmp r9, r11
00798CA3  73 1F                           jae 0x140798cc4
00798CA5  41 0F B6 00                     movzx eax, byte ptr [r8]
00798CA9  49 8B C9                        mov rcx, r9
00798CAC  66 41 89 01                     mov word ptr [r9], ax
00798CB0  49 FF C0                        inc r8
00798CB3  49 83 C1 02                     add r9, 2
00798CB7  0F B7 01                        movzx eax, word ptr [rcx]
00798CBA  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
00798CBF  4C 3B C5                        cmp r8, rbp
00798CC2  72 DC                           jb 0x140798ca0
00798CC4  4C 8B 9C 24 B8 00 00 00         mov r11, qword ptr [rsp + 0xb8]
00798CCC  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00798CD4  45 2B CB                        sub r9d, r11d
00798CD7  44 89 08                        mov dword ptr [rax], r9d
00798CDA  33 C0                           xor eax, eax
00798CDC  48 83 C4 58                     add rsp, 0x58
00798CE0  41 5F                           pop r15
00798CE2  41 5E                           pop r14
00798CE4  41 5D                           pop r13
00798CE6  41 5C                           pop r12
00798CE8  5F                              pop rdi
00798CE9  5E                              pop rsi
00798CEA  5D                              pop rbp
00798CEB  5B                              pop rbx
00798CEC  C3                              ret
00798CED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Xp10ExecuteLz77PassMinMatchLen3(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    v_r14 = 0;
    v_stack_m98 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1))) & (31));
    *(unsigned int *)(a1 + 24) = 0;
    result = (unsigned int)((v_r14 + 1) << ((unsigned __int8)(a1)));
    v_stack_m78 = (unsigned int)(result);
    *(unsigned __int16 *)(a4) = (unsigned __int16)(*(unsigned __int8 *)(a2));
    a1 = (a5) + (-15);
    a4 = (a4) + (2);
    v_stack_m58 = a1;
    v_stack_m90 = a4;
    v_stack_m60 = a3 - 40;
    if ((a2 + 1) >= (a3 - 40)) goto loc_00798C93;
loc_0079863F:
    if (a4 >= a1) goto loc_00798C8B;
    v_stack_m94 = 0;
    v_stack_m88 = a2 + 1;
    v_stack_m68 = a2 + 1;
    v_stack_m7C = 0;
    v_stack_m80 = 0;
loc_00798670:
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 1 + 1)) << (3));
    v_stack_m70 = a2 + 1 + 1;
    a2 = (unsigned int)((result + *(unsigned __int8 *)(a2 + 1 + 2) * 2) + ((unsigned int)(*(unsigned __int8 *)(a2 + 1))));
    *(unsigned __int64 *)(a1 + a2 * 8 + 5664) = a2 + 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664))) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1)))) goto loc_007989F5;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 1)))) goto loc_007989F5;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 2)))) goto loc_007989F5;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - ((unsigned int)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_007989F5;
    if ((a2 + 1) == (*(unsigned __int64 *)(a1 + a2 * 8 + 5664))) goto loc_007989F5;
    v_stack_p10 = 1;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 3))) == ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 3)))) goto loc_0079874C;
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 1 + 3)) + ((unsigned int)(a2)));
    *(unsigned __int64 *)(a1 + a2 + *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 3) * 1 * 8 + 36272) = *(unsigned __int64 *)(a1 + a2 * 8 + 5664);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + result * 8 + 36272))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 1))))) goto loc_00798939;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + result * 8 + 36272) + 3)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 3)))) goto loc_00798939;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - ((unsigned int)(*(unsigned __int64 *)(a1 + result * 8 + 36272))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_00798939;
    if ((a2 + 1) == (*(unsigned __int64 *)(a1 + result * 8 + 36272))) goto loc_00798939;
    *(unsigned __int64 *)(a1 + a2 + *(unsigned __int8 *)(a2 + 1 + 3) * 1 * 8 + 36272) = a2 + 1;
loc_0079874C:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + result * 8 + 36272) + 4))) == ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 4)))) goto loc_007987E2;
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 1 + 1) + 97) + (*(unsigned __int8 *)(a2 + 1 + 2)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1))));
    v_rdi = (unsigned __int8)((*(unsigned __int8 *)(a2 + 1)) + (*(unsigned __int8 *)(a2 + 1 + 3)));
    v_rdi = (unsigned __int8)((v_rdi) ^ ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 1))));
    v_rdi = (unsigned int)(((unsigned __int8)(v_rdi) + (unsigned __int8)(result) * 4) + ((unsigned int)((unsigned __int8)(v_rdi) + (unsigned __int8)(result) * 4)));
    *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + result * 8 + 36272) + 4) * 1 * 8 + 36272) = *(unsigned __int64 *)(a1 + result * 8 + 36272);
    if ((*(unsigned int *)(a2 + 1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272)))))) goto loc_00798940;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 4))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272) + 4))) goto loc_00798940;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - ((unsigned int)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_00798940;
    if ((a2 + 1) == (*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272))) goto loc_00798940;
    *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272) = a2 + 1;
loc_007987E2:
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 5))) == ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272) + 5)))) goto loc_00798890;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 1))) + (69));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 4))));
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 1 + 3)) ^ (*(unsigned __int8 *)(a2 + 1 + 1)));
    a2 = (unsigned int)(((unsigned __int8)(result)) + ((unsigned int)((unsigned __int8)(result))));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 1))) ^ ((unsigned int)(*(unsigned __int8 *)(a2 + 1 + 2))));
    v_rdi = (unsigned int)((a1 + a2 * 4) + ((unsigned int)(a1 + a2 * 4)));
    *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272) + 5) * 1 * 8 + 36272) = *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272);
    if ((*(unsigned int *)(a2 + 1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272)))))) goto loc_007989A7;
    if ((*(unsigned __int8 *)(a2 + 1 + 4)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272) + 4)))) goto loc_007989A7;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 5))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272) + 5))) goto loc_007989A7;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - ((unsigned int)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_007989A7;
    if ((a2 + 1) == (*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272))) goto loc_007989A7;
    *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272) = a2 + 1;
loc_00798890:
    result = (*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272)) - (a2 + 1);
    a2 = (a2 + 1 + 6 + 8) + (result);
    v_rdi = (a2 + 1) - (*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272));
loc_007988AC:
    if ((a2 + 1 + 6) >= (a3 - 40)) goto loc_007989CF;
    if (6 >= ((unsigned int)((unsigned int)(v_stack_m78) - 32))) goto loc_007989CF;
    if ((*(unsigned int *)(a2 + 1 + 6)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 - 8))))) goto loc_007989CF;
    if ((*(unsigned int *)(v_rdi + a2 * 1 - 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 - 4))))) goto loc_007989CC;
    if ((*(unsigned int *)(a2 + v_rdi * 1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_007989C7;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4))))) goto loc_007989C2;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))))) goto loc_007989BD;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 12)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12))))) goto loc_007989B8;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) goto loc_007989B3;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 20)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 20))))) goto loc_007989AE;
    a1 = (unsigned int)((6) + (32));
    v_rbx = (a2 + 1 + 6) + (32);
    a2 = (a2) + (32);
    goto loc_007988AC;
loc_00798939:
    goto loc_0079894C;
loc_00798940:
loc_00798945:
loc_0079894C:
    v_rsi = 0;
loc_00798965:
    a2 = (a2 + 1) - ((unsigned int)(*(unsigned int *)(a1 + 8)));
    if ((*(unsigned __int8 *)(a2)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1)))) goto loc_00798A3B;
    if ((*(unsigned __int8 *)(a2 + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m70)))) goto loc_00798A3B;
    if ((*(unsigned __int8 *)(a2 + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 2)))) goto loc_00798A3B;
    if (a2 == (a2 + 1)) goto loc_00798A3B;
    goto loc_00798A15;
loc_007989A7:
    goto loc_00798945;
loc_007989AE:
    a1 = (unsigned int)((5) + (28));
    goto loc_007989CF;
loc_007989B3:
    a1 = (unsigned int)((a1) + (24));
    goto loc_007989CF;
loc_007989B8:
    a1 = (unsigned int)((a1) + (20));
    goto loc_007989CF;
loc_007989BD:
    a1 = (unsigned int)((a1) + (16));
    goto loc_007989CF;
loc_007989C2:
    a1 = (unsigned int)((a1) + (12));
    goto loc_007989CF;
loc_007989C7:
    a1 = (unsigned int)((a1) + (8));
    goto loc_007989CF;
loc_007989CC:
    a1 = (unsigned int)((a1) + (4));
loc_007989CF:
    goto loc_007989EB;
loc_007989D7:
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)(a1)) + a2 + 1 * 1)) != ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(a1)) + *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272) * 1)))) goto loc_00798945;
    a1 = (unsigned int)((a1) + 1);
loc_007989EB:
    if ((a1 + a2 + 1 * 1) < (a1 + 8)) goto loc_007989D7;
    goto loc_00798945;
loc_007989F5:
    v_rbx = 0;
    v_stack_p10 = 0;
    goto loc_0079894C;
loc_00798A06:
    if ((*(unsigned __int8 *)(v_rbx)) != ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(a1)) + a1 + a2 + 1 * 1 * 1)))) goto loc_00798A1A;
    v_rdi = (unsigned int)((3) + 1);
loc_00798A15:
    if ((v_rdi + a2 + 1 * 1) < v_stack_p18) goto loc_00798A06;
loc_00798A1A:
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_rbx + 1))) goto loc_00798A34;
    v_stack_p10 = 2;
    goto loc_00798A3B;
loc_00798A34:
loc_00798A3B:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_rbp = (a1 + 8) + (4);
    if (((unsigned int)(v_rsi)) < 4) goto loc_00798965;
    v_rbx = (unsigned int)(v_stack_p10);
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) < v_stack_m7C) { v_rbx = v_stack_m94; }
    a3 = a2 + 1;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) < v_stack_m7C) { a3 = a2 + 1; }
    v_r14 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) < v_stack_m7C) { v_r14 = v_stack_m80; }
    v_rsi = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi))));
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) < v_stack_m7C) { v_rsi = v_stack_m7C; }
    v_r11 = a1 + a2 + 1 * 1;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) < v_stack_m7C) { v_r11 = v_stack_m88; }
    result = (v_stack_m70) - (v_stack_m68);
    v_stack_m98 = 0;
    v_stack_m80 = (unsigned int)(v_r14);
    v_stack_m94 = (unsigned int)(v_rbx);
    v_stack_m88 = v_r11;
    v_stack_m7C = (unsigned int)(v_rsi);
    if (result <= 2) goto loc_00798670;
    v_stack_m98 = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    goto loc_00798ADC;
loc_00798AC1:
    *(unsigned __int16 *)(v_stack_m90) = (unsigned __int16)(*(unsigned __int8 *)(v_stack_m68));
    a4 = (v_stack_m90) + (2);
    v_r12 = (v_stack_m68) + 1;
loc_00798ADC:
    if (v_r12 < a3) goto loc_00798AC1;
    v_r14 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) == 0) goto loc_00798C50;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx))))) - (1));
    if (condition_is_equal) goto loc_00798BA7;
    if (((unsigned int)(a1)) != 1) goto loc_00798B3E;
    result = (unsigned int)((a1 + 15) + ((unsigned int)((unsigned int)((unsigned int)(v_r14)))));
    result = (unsigned __int16)((result) << (4));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
    if ((unsigned int)((unsigned int)((unsigned int)(v_r14))) == 0) goto loc_00798B3E;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) < 3) goto loc_00798B29;
    *(unsigned int *)(v_stack_p8 + 8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8 + 8)));
    goto loc_00798B2E;
loc_00798B29:
    result = (unsigned int)(*(unsigned int *)(v_stack_p8 + 8 + 8));
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) >= 2) {
        result = *(unsigned int *)(v_stack_p8 + 8 + 4);
        *(unsigned int *)(v_stack_p8 + 8 + 8) = (unsigned int)(result);
    }
    *(unsigned int *)(v_stack_p8 + 8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8)));
    *(unsigned int *)(v_stack_p8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + (unsigned int)((unsigned int)(v_r14)) * 4 + 8)));
loc_00798B3E:
loc_00798B43:
    if (((unsigned int)(v_rsi - 3)) < 15) goto loc_00798C07;
    result = (unsigned __int16)((*(unsigned __int16 *)(a4)) + (15));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
    v_stack_m90 = a4 + 2 + 1;
    if (((unsigned int)(v_rsi - 3)) <= 246) goto loc_00798BEE;
    v_rdi = (unsigned int)((v_rsi - 3) + (0xFFFFFF0AULL));
    v_stack_p10 = 0;
    *(unsigned __int8 *)(a4 + 2) = (unsigned __int8)(v_stack_p8 + 8 + 8 - 24);
    if (((unsigned int)(v_rdi)) <= 1) goto loc_00798BF9;
    result = (unsigned int)((15 - 14) << ((unsigned __int8)(v_stack_p8 + 8 + 8)));
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result)));
    *(unsigned int *)(a4 + 2 + 1) = (unsigned int)(v_rdi);
    a4 = (a4 + 2 + 1) + (4);
    goto loc_00798BF4;
loc_00798BA7:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(v_stack_m88)));
    v_stack_p10 = 0;
    result = (unsigned int)((20) + (0));
    result = (unsigned __int16)((result) << (4));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
    *(unsigned int *)(v_stack_p8 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)));
    *(unsigned int *)(v_stack_p8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 12)));
    *(unsigned int *)(v_stack_p8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8)));
    *(unsigned int *)(v_stack_p8 + 8) = (unsigned int)(a1);
    goto loc_00798B43;
loc_00798BEE:
    v_rdi = (unsigned __int8)((v_rdi) - (15));
    *(unsigned __int8 *)(a4 + 2) = (unsigned __int8)(v_rdi);
loc_00798BF4:
    v_stack_m90 = a4;
loc_00798BF9:
    goto loc_00798C17;
loc_00798C07:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)(*(unsigned __int8 *)(a4 + 2))));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(v_rdi);
    a4 = (a4) + (2);
    v_stack_m90 = a4;
loc_00798C17:
    if (v_stack_m94 != 1) goto loc_00798C4C;
    result = *(unsigned __int16 *)(a4);
    if (0 != 0) {
        a1 = 0;
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
        a1 = (unsigned int)(a3);
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
        a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_m88)));
        *(unsigned int *)(a4) = (unsigned int)(a1);
        a4 = (a4) + (4);
        v_stack_m90 = a4;
    }
    goto loc_00798C6F;
loc_00798C50:
    *(unsigned __int16 *)(a4) = (unsigned __int16)(*(unsigned __int8 *)(a3));
    a4 = (a4) + (2);
    v_stack_m90 = a4;
loc_00798C6F:
    if ((1 + a3 * 1) < v_stack_m60) goto loc_0079863F;
loc_00798C8B:
loc_00798C93:
    if ((1 + a3 * 1) >= v_stack_p18) goto loc_00798CCC;
loc_00798CA0:
    if (a4 >= a5) goto loc_00798CC4;
    *(unsigned __int16 *)(a4) = (unsigned __int16)(*(unsigned __int8 *)(1 + a3 * 1));
    a3 = (1 + a3 * 1) + 1;
    a4 = (a4) + (2);
    if (a3 < v_stack_p18) goto loc_00798CA0;
loc_00798CC4:
loc_00798CCC:
    a4 = (unsigned int)((a4) - ((unsigned int)(v_stack_p20)));
    *(unsigned int *)(a6) = (unsigned int)(a4);
    result = 0;
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Xp10ExecuteLz77PassMinMatchLen3(void *Arg1, void *Arg2, void *Arg3, void *Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    local_r14 = 0;
    v_stack_m98 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1))) & (31));
    *(uint32_t *)(arg1 + 0x18) = 0;
    result = (uint32_t)((local_r14 + 1) << ((uint8_t)(Arg1)));
    v_stack_m78 = (uint32_t)(result);
    *(uint16_t *)(arg4) = (uint16_t)(*(uint8_t *)(arg2));
    Arg1 = (Arg5) + (-15);
    Arg4 = (Arg4) + (2);
    v_stack_m58 = Arg1;
    v_stack_m90 = Arg4;
    v_stack_m60 = Arg3 - 40;
    if ((Arg2 + 1) >= (Arg3 - 40)) goto loc_00798C93;
loc_0079863F:
    if (Arg4 >= Arg1) goto loc_00798C8B;
    v_stack_m94 = 0;
    v_stack_m88 = Arg2 + 1;
    v_stack_m68 = Arg2 + 1;
    v_stack_m7C = 0;
    v_stack_m80 = 0;
loc_00798670:
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1 + 0x1)) << (3));
    v_stack_m70 = Arg2 + 1 + 1;
    Arg2 = (uint32_t)((result + *(uint8_t *)(arg2 + 0x1 + 0x2) * 2) + ((uint32_t)(*(uint8_t *)(arg2 + 0x1))));
    *(void **)(arg1 + arg2 * 8 + 0x1620) = Arg2 + 1;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620))) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1)))) goto loc_007989F5;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x1)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x1)))) goto loc_007989F5;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x2)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x2)))) goto loc_007989F5;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - ((uint32_t)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_007989F5;
    if ((Arg2 + 1) == (*(uint64_t *)(arg1 + arg2 * 8 + 0x1620))) goto loc_007989F5;
    v_stack_p10 = 1;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x3))) == ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x3)))) goto loc_0079874C;
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1 + 0x3)) + ((uint32_t)(Arg2)));
    *(uint64_t *)(arg1 + arg2 + *(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x3) * 1 * 8 + 0x8DB0) = *(uint64_t *)(arg1 + arg2 * 8 + 0x1620);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1))))) goto loc_00798939;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0) + 0x3)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x3)))) goto loc_00798939;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - ((uint32_t)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_00798939;
    if ((Arg2 + 1) == (*(uint64_t *)(arg1 + result * 8 + 0x8DB0))) goto loc_00798939;
    *(void **)(arg1 + arg2 + *(uint8_t *)(arg2 + 0x1 + 0x3) * 1 * 8 + 0x8DB0) = Arg2 + 1;
loc_0079874C:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0) + 0x4))) == ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x4)))) goto loc_007987E2;
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x1 + 0x1) + 97) + (*(uint8_t *)(arg2 + 0x1 + 0x2)));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(arg2 + 0x1))));
    local_rdi = (uint8_t)((*(uint8_t *)(arg2 + 0x1)) + (*(uint8_t *)(arg2 + 0x1 + 0x3)));
    local_rdi = (uint8_t)((local_rdi) ^ ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x1))));
    local_rdi = (uint32_t)(((uint8_t)(local_rdi) + (uint8_t)(result) * 4) + ((uint32_t)((uint8_t)(local_rdi) + (uint8_t)(result) * 4)));
    *(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0) + 0x4) * 1 * 8 + 0x8DB0) = *(uint64_t *)(arg1 + result * 8 + 0x8DB0);
    if ((*(uint32_t *)(arg2 + 0x1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0)))))) goto loc_00798940;
    if (((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x4))) != (*(uint8_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0) + 0x4))) goto loc_00798940;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - ((uint32_t)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_00798940;
    if ((Arg2 + 1) == (*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0))) goto loc_00798940;
    *(void **)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0) = Arg2 + 1;
loc_007987E2:
    if (((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x5))) == ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0) + 0x5)))) goto loc_00798890;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg2 + 0x1))) + (69));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x4))));
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x1 + 0x3)) ^ (*(uint8_t *)(arg2 + 0x1 + 0x1)));
    Arg2 = (uint32_t)(((uint8_t)(result)) + ((uint32_t)((uint8_t)(result))));
    Arg1 = (uint32_t)(((uint8_t)(*(uint8_t *)(arg2 + 0x1))) ^ ((uint32_t)(*(uint8_t *)(arg2 + 0x1 + 0x2))));
    local_rdi = (uint32_t)((Arg1 + Arg2 * 4) + ((uint32_t)(Arg1 + Arg2 * 4)));
    *(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0) + 0x5) * 1 * 8 + 0x8DB0) = *(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0);
    if ((*(uint32_t *)(arg2 + 0x1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0)))))) goto loc_007989A7;
    if ((*(uint8_t *)(arg2 + 0x1 + 0x4)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0) + 0x4)))) goto loc_007989A7;
    if (((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x5))) != (*(uint8_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0) + 0x5))) goto loc_007989A7;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - ((uint32_t)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_007989A7;
    if ((Arg2 + 1) == (*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0))) goto loc_007989A7;
    *(void **)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0) = Arg2 + 1;
loc_00798890:
    result = (*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0)) - (Arg2 + 1);
    Arg2 = (Arg2 + 1 + 6 + 8) + (result);
    local_rdi = (Arg2 + 1) - (*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0));
loc_007988AC:
    if ((Arg2 + 1 + 6) >= (Arg3 - 40)) goto loc_007989CF;
    if (6 >= ((uint32_t)((uint32_t)(v_stack_m78) - 32))) goto loc_007989CF;
    if ((*(uint32_t *)(arg2 + 0x1 + 0x6)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 - 0x8))))) goto loc_007989CF;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 - 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 - 0x4))))) goto loc_007989CC;
    if ((*(uint32_t *)(arg2 + local_rdi * 1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_007989C7;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4))))) goto loc_007989C2;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))))) goto loc_007989BD;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0xC)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC))))) goto loc_007989B8;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) goto loc_007989B3;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x14)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x14))))) goto loc_007989AE;
    Arg1 = (uint32_t)((6) + (32));
    local_rbx = (Arg2 + 1 + 6) + (32);
    Arg2 = (Arg2) + (32);
    goto loc_007988AC;
loc_00798939:
    goto loc_0079894C;
loc_00798940:
loc_00798945:
loc_0079894C:
    local_rsi = 0;
loc_00798965:
    Arg2 = (Arg2 + 1) - ((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    if ((*(uint8_t *)(arg2)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1)))) goto loc_00798A3B;
    if ((*(uint8_t *)(arg2 + 0x1)) != ((uint8_t)(*(uint8_t *)(v_stack_m70)))) goto loc_00798A3B;
    if ((*(uint8_t *)(arg2 + 0x2)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x2)))) goto loc_00798A3B;
    if (Arg2 == (Arg2 + 1)) goto loc_00798A3B;
    goto loc_00798A15;
loc_007989A7:
    goto loc_00798945;
loc_007989AE:
    Arg1 = (uint32_t)((5) + (28));
    goto loc_007989CF;
loc_007989B3:
    Arg1 = (uint32_t)((Arg1) + (24));
    goto loc_007989CF;
loc_007989B8:
    Arg1 = (uint32_t)((Arg1) + (20));
    goto loc_007989CF;
loc_007989BD:
    Arg1 = (uint32_t)((Arg1) + (16));
    goto loc_007989CF;
loc_007989C2:
    Arg1 = (uint32_t)((Arg1) + (12));
    goto loc_007989CF;
loc_007989C7:
    Arg1 = (uint32_t)((Arg1) + (8));
    goto loc_007989CF;
loc_007989CC:
    Arg1 = (uint32_t)((Arg1) + (4));
loc_007989CF:
    goto loc_007989EB;
loc_007989D7:
    if ((*(uint8_t *)((uint32_t)((uint32_t)(arg1)) + arg2 + 0x1 * 1)) != ((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(arg1)) + *(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0) * 1)))) goto loc_00798945;
    Arg1 = (uint32_t)((Arg1) + 1);
loc_007989EB:
    if ((Arg1 + Arg2 + 1 * 1) < (Arg1 + 8)) goto loc_007989D7;
    goto loc_00798945;
loc_007989F5:
    local_rbx = 0;
    v_stack_p10 = 0;
    goto loc_0079894C;
loc_00798A06:
    if ((*(uint8_t *)(local_rbx)) != ((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(arg1)) + arg1 + arg2 + 0x1 * 1 * 1)))) goto loc_00798A1A;
    local_rdi = (uint32_t)((3) + 1);
loc_00798A15:
    if ((local_rdi + Arg2 + 1 * 1) < v_stack_p18) goto loc_00798A06;
loc_00798A1A:
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_rbx + 1))) goto loc_00798A34;
    v_stack_p10 = 2;
    goto loc_00798A3B;
loc_00798A34:
loc_00798A3B:
    local_rsi = (uint32_t)((local_rsi) + 1);
    local_rbp = (Arg1 + 8) + (4);
    if (((uint32_t)(local_rsi)) < 4) goto loc_00798965;
    local_rbx = (uint32_t)(v_stack_p10);
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) < v_stack_m7C) { local_rbx = v_stack_m94; }
    Arg3 = Arg2 + 1;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) < v_stack_m7C) { Arg3 = Arg2 + 1; }
    local_r14 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) < v_stack_m7C) { local_r14 = v_stack_m80; }
    local_rsi = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi))));
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) < v_stack_m7C) { local_rsi = v_stack_m7C; }
    local_r11 = Arg1 + Arg2 + 1 * 1;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) < v_stack_m7C) { local_r11 = v_stack_m88; }
    result = (v_stack_m70) - (v_stack_m68);
    v_stack_m98 = 0;
    v_stack_m80 = (uint32_t)(local_r14);
    v_stack_m94 = (uint32_t)(local_rbx);
    v_stack_m88 = local_r11;
    v_stack_m7C = (uint32_t)(local_rsi);
    if (result <= 2) goto loc_00798670;
    v_stack_m98 = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    goto loc_00798ADC;
loc_00798AC1:
    *(uint16_t *)(v_stack_m90) = (uint16_t)(*(uint8_t *)(v_stack_m68));
    Arg4 = (v_stack_m90) + (2);
    local_r12 = (v_stack_m68) + 1;
loc_00798ADC:
    if (local_r12 < Arg3) goto loc_00798AC1;
    local_r14 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) == 0) goto loc_00798C50;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx))))) - (1));
    if (condition_is_equal) goto loc_00798BA7;
    if (((uint32_t)(Arg1)) != 1) goto loc_00798B3E;
    result = (uint32_t)((Arg1 + 15) + ((uint32_t)((uint32_t)((uint32_t)(local_r14)))));
    result = (uint16_t)((result) << (4));
    *(uint16_t *)(arg4) = (uint16_t)(result);
    if ((uint32_t)((uint32_t)((uint32_t)(local_r14))) == 0) goto loc_00798B3E;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) < 3) goto loc_00798B29;
    *(uint32_t *)(v_stack_p8 + 0x8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8 + 0x8)));
    goto loc_00798B2E;
loc_00798B29:
    result = (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8 + 0x8));
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) >= 2) {
        result = *(uint32_t *)(v_stack_p8 + 0x8 + 0x4);
        *(uint32_t *)(v_stack_p8 + 0x8 + 0x8) = (uint32_t)(result);
    }
    *(uint32_t *)(v_stack_p8 + 0x8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8)));
    *(uint32_t *)(v_stack_p8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + (uint32_t)((uint32_t)(local_r14)) * 4 + 0x8)));
loc_00798B3E:
loc_00798B43:
    if (((uint32_t)(local_rsi - 3)) < 15) goto loc_00798C07;
    result = (uint16_t)((*(uint16_t *)(arg4)) + (15));
    *(uint16_t *)(arg4) = (uint16_t)(result);
    v_stack_m90 = Arg4 + 2 + 1;
    if (((uint32_t)(local_rsi - 3)) <= 246) goto loc_00798BEE;
    local_rdi = (uint32_t)((local_rsi - 3) + (0xFFFFFF0AULL));
    v_stack_p10 = 0;
    *(uint8_t *)(arg4 + 0x2) = (uint8_t)(v_stack_p8 + 8 + 8 - 24);
    if (((uint32_t)(local_rdi)) <= 1) goto loc_00798BF9;
    result = (uint32_t)((15 - 14) << ((uint8_t)(v_stack_p8 + 8 + 8)));
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result)));
    *(uint32_t *)(arg4 + 0x2 + 0x1) = (uint32_t)(local_rdi);
    Arg4 = (Arg4 + 2 + 1) + (4);
    goto loc_00798BF4;
loc_00798BA7:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(v_stack_m88)));
    v_stack_p10 = 0;
    result = (uint32_t)((20) + (0));
    result = (uint16_t)((result) << (4));
    *(uint16_t *)(arg4) = (uint16_t)(result);
    *(uint32_t *)(v_stack_p8 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)));
    *(uint32_t *)(v_stack_p8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC)));
    *(uint32_t *)(v_stack_p8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8)));
    *(uint32_t *)(v_stack_p8 + 0x8) = (uint32_t)(Arg1);
    goto loc_00798B43;
loc_00798BEE:
    local_rdi = (uint8_t)((local_rdi) - (15));
    *(uint8_t *)(arg4 + 0x2) = (uint8_t)(local_rdi);
loc_00798BF4:
    v_stack_m90 = Arg4;
loc_00798BF9:
    goto loc_00798C17;
loc_00798C07:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)(*(uint8_t *)(arg4 + 0x2))));
    *(uint16_t *)(arg4) = (uint16_t)(local_rdi);
    Arg4 = (Arg4) + (2);
    v_stack_m90 = Arg4;
loc_00798C17:
    if (v_stack_m94 != 1) goto loc_00798C4C;
    result = *(uint16_t *)(arg4);
    if (0 != 0) {
        Arg1 = 0;
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
        Arg1 = (uint32_t)(Arg3);
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_m88)));
        *(uint32_t *)(arg4) = (uint32_t)(Arg1);
        Arg4 = (Arg4) + (4);
        v_stack_m90 = Arg4;
    }
    goto loc_00798C6F;
loc_00798C50:
    *(uint16_t *)(arg4) = (uint16_t)(*(uint8_t *)(arg3));
    Arg4 = (Arg4) + (2);
    v_stack_m90 = Arg4;
loc_00798C6F:
    if ((1 + Arg3 * 1) < v_stack_m60) goto loc_0079863F;
loc_00798C8B:
loc_00798C93:
    if ((1 + Arg3 * 1) >= v_stack_p18) goto loc_00798CCC;
loc_00798CA0:
    if (Arg4 >= Arg5) goto loc_00798CC4;
    *(uint16_t *)(arg4) = (uint16_t)(*(uint8_t *)(1 + arg3 * 1));
    Arg3 = (1 + Arg3 * 1) + 1;
    Arg4 = (Arg4) + (2);
    if (Arg3 < v_stack_p18) goto loc_00798CA0;
loc_00798CC4:
loc_00798CCC:
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(v_stack_p20)));
    *(uint32_t *)(arg6) = (uint32_t)(Arg4);
    result = 0;
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x1C + rax*4` | `32` | `R/W` |
| `Arg1` | `+ 0x1620` | `64` | `R` |
| `Arg1` | `+ 0x8DB0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x1` | `64` | `R` |
| `Arg3` | `- 0x28` | `64` | `R` |
| `Arg4` | `+ 0x0` | `16` | `W` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079859C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
