# LocalGetRelativeAttributeForString

- RVA: `0x00AC74E4`–`0x00AC8045` (길이 `2,913` bytes)
- VA: `0x0000000140AC74E4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE088`
- 디코드: `822`개 명령, `2,913/2,913` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **55**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AC758A` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC759D` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC75B5` → [IsLegalAttributeChar2](../7A/IsLegalAttributeChar2_function_007A598C.md) (function, `0x007A598C`)
- `0x00AC75EF` → [DecodeAttributeName](../A0/DecodeAttributeName_function_00A03460.md) (function, `0x00A03460`)
- `0x00AC7639` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00AC764A` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00AC766C` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7688` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC769C` → [GetValueType](../7A/GetValueType_function_007A57E4.md) (function, `0x007A57E4`)
- `0x00AC76B3` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC76C8` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC76DC` → [GetFlags](../7A/GetFlags_function_007A56D4.md) (function, `0x007A56D4`)
- `0x00AC7700` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7770` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC778C` → [GetDigitFromChar](../7A/GetDigitFromChar_function_007A5654.md) (function, `0x007A5654`)
- `0x00AC77D4` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7835` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00AC7871` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7889` → [LocalGetSidForString](../92/LocalGetSidForString_function_009292B4.md) (function, `0x009292B4`)
- `0x00AC78B1` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00AC78DA` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00AC78EF` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7932` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7942` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC799D` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC79AD` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7A38` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (function, `0x00502674`)
- `0x00AC7A6C` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7A7E` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7AFC` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (function, `0x00502674`)
- `0x00AC7B27` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7BB1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AC7C05` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7C18` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7C41` → [GetDigitFromChar](../7A/GetDigitFromChar_function_007A5654.md) (function, `0x007A5654`)
- `0x00AC7C81` → [GetDigitFromChar](../7A/GetDigitFromChar_function_007A5654.md) (function, `0x007A5654`)
- `0x00AC7C97` → [GetDigitFromChar](../7A/GetDigitFromChar_function_007A5654.md) (function, `0x007A5654`)
- `0x00AC7CCF` → [GetDigitFromChar](../7A/GetDigitFromChar_function_007A5654.md) (function, `0x007A5654`)
- `0x00AC7CF5` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7D05` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7D3F` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7D57` → [LocalGetSidForString](../92/LocalGetSidForString_function_009292B4.md) (function, `0x009292B4`)
- `0x00AC7D76` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00AC7D9A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AC7DB6` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00AC7DCA` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7E11` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7E6F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AC7E92` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7F09` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (function, `0x00502674`)
- `0x00AC7F4A` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7F5C` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7FAB` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (function, `0x00502674`)
- `0x00AC7FE8` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)
- `0x00AC7FFA` → [iswspace](../../text/50/iswspace_function_00500800.md) (function, `0x00500800`)

### Direct callers
- [LocalGetAclForString](../92/LocalGetAclForString_function_00927F30.md) at `0x00928B16`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **39**
  - `0x00AC758A` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC759D` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC766C` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7688` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC76B3` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC76C8` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7700` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7770` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC77D4` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7871` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC78B1` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00AC78EF` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7932` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7942` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC799D` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC79AD` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7A38` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (`PAGE` → `.text`)
  - `0x00AC7A6C` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7A7E` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7AFC` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (`PAGE` → `.text`)
  - `0x00AC7B27` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7BB1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AC7C05` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7C18` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7CF5` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7D05` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7D3F` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7D76` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00AC7D9A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AC7DCA` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7E11` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7E6F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AC7E92` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7F09` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (`PAGE` → `.text`)
  - `0x00AC7F4A` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7F5C` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7FAB` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (`PAGE` → `.text`)
  - `0x00AC7FE8` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
  - `0x00AC7FFA` → [iswspace](../../text/50/iswspace_function_00500800.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC74E4  48 8B C4                        mov rax, rsp
00AC74E7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00AC74EB  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00AC74EF  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AC74F3  55                              push rbp
00AC74F4  53                              push rbx
00AC74F5  56                              push rsi
00AC74F6  57                              push rdi
00AC74F7  41 54                           push r12
00AC74F9  41 55                           push r13
00AC74FB  41 56                           push r14
00AC74FD  41 57                           push r15
00AC74FF  48 8D 68 B9                     lea rbp, [rax - 0x47]
00AC7503  48 81 EC 88 00 00 00            sub rsp, 0x88
00AC750A  45 33 F6                        xor r14d, r14d
00AC750D  49 8B C1                        mov rax, r9
00AC7510  4C 89 75 CF                     mov qword ptr [rbp - 0x31], r14
00AC7514  45 8B FE                        mov r15d, r14d
00AC7517  4C 89 75 BF                     mov qword ptr [rbp - 0x41], r14
00AC751B  41 8B F6                        mov esi, r14d
00AC751E  4C 89 75 E7                     mov qword ptr [rbp - 0x19], r14
00AC7522  45 8B E6                        mov r12d, r14d
00AC7525  66 44 89 75 7F                  mov word ptr [rbp + 0x7f], r14w
00AC752A  44 89 75 DB                     mov dword ptr [rbp - 0x25], r14d
00AC752E  44 89 75 C7                     mov dword ptr [rbp - 0x39], r14d
00AC7532  44 88 75 4F                     mov byte ptr [rbp + 0x4f], r14b
00AC7536  44 88 B5 87 00 00 00            mov byte ptr [rbp + 0x87], r14b
00AC753D  44 88 75 77                     mov byte ptr [rbp + 0x77], r14b
00AC7541  4C 89 75 DF                     mov qword ptr [rbp - 0x21], r14
00AC7545  44 89 75 CB                     mov dword ptr [rbp - 0x35], r14d
00AC7549  48 85 C9                        test rcx, rcx
00AC754C  0F 84 E1 0A 00 00               je 0x140ac8033
00AC7552  48 85 D2                        test rdx, rdx
00AC7555  0F 84 D8 0A 00 00               je 0x140ac8033
00AC755B  4D 85 C0                        test r8, r8
00AC755E  0F 84 CF 0A 00 00               je 0x140ac8033
00AC7564  48 85 C0                        test rax, rax
00AC7567  0F 84 C6 0A 00 00               je 0x140ac8033
00AC756D  66 83 39 28                     cmp word ptr [rcx], 0x28
00AC7571  4D 89 30                        mov qword ptr [r8], r14
00AC7574  45 89 31                        mov dword ptr [r9], r14d
00AC7577  74 0A                           je 0x140ac7583
00AC7579  BF 38 05 00 00                  mov edi, 0x538
00AC757E  E9 CC 00 00 00                  jmp 0x140ac764f
00AC7583  48 8D 79 02                     lea rdi, [rcx + 2]
00AC7587  0F B7 0F                        movzx ecx, word ptr [rdi]
00AC758A  E8 71 92 A3 FF                  call 0x140500800
00AC758F  41 BD 02 00 00 00               mov r13d, 2
00AC7595  EB 0B                           jmp 0x140ac75a2
00AC7597  49 03 FD                        add rdi, r13
00AC759A  0F B7 0F                        movzx ecx, word ptr [rdi]
00AC759D  E8 5E 92 A3 FF                  call 0x140500800
00AC75A2  85 C0                           test eax, eax
00AC75A4  75 F1                           jne 0x140ac7597
00AC75A6  66 83 3F 22                     cmp word ptr [rdi], 0x22
00AC75AA  75 CD                           jne 0x140ac7579
00AC75AC  49 03 FD                        add rdi, r13
00AC75AF  48 8B DF                        mov rbx, rdi
00AC75B2  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC75B5  E8 D2 E3 CD FF                  call 0x1407a598c
00AC75BA  84 C0                           test al, al
00AC75BC  74 1A                           je 0x140ac75d8
00AC75BE  66 85 C9                        test cx, cx
00AC75C1  74 B6                           je 0x140ac7579
00AC75C3  49 03 DD                        add rbx, r13
00AC75C6  8D 46 01                        lea eax, [rsi + 1]
00AC75C9  3B C6                           cmp eax, esi
00AC75CB  72 04                           jb 0x140ac75d1
00AC75CD  8B F0                           mov esi, eax
00AC75CF  EB E1                           jmp 0x140ac75b2
00AC75D1  BF 16 02 00 00                  mov edi, 0x216
00AC75D6  EB 77                           jmp 0x140ac764f
00AC75D8  66 83 F9 22                     cmp cx, 0x22
00AC75DC  75 9B                           jne 0x140ac7579
00AC75DE  85 F6                           test esi, esi
00AC75E0  74 97                           je 0x140ac7579
00AC75E2  8D 14 36                        lea edx, [rsi + rsi]
00AC75E5  48 8B CF                        mov rcx, rdi
00AC75E8  4C 8D 45 E7                     lea r8, [rbp - 0x19]
00AC75EC  49 03 DD                        add rbx, r13
00AC75EF  E8 6C BE F3 FF                  call 0x140a03460
00AC75F4  8B F8                           mov edi, eax
00AC75F6  85 C0                           test eax, eax
00AC75F8  75 33                           jne 0x140ac762d
00AC75FA  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00AC75FE  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AC7602  48 FF C0                        inc rax
00AC7605  66 44 39 34 41                  cmp word ptr [rcx + rax*2], r14w
00AC760A  75 F6                           jne 0x140ac7602
00AC760C  FF C0                           inc eax
00AC760E  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00AC7612  03 C0                           add eax, eax
00AC7614  89 45 EF                        mov dword ptr [rbp - 0x11], eax
00AC7617  44 8D 78 14                     lea r15d, [rax + 0x14]
00AC761B  44 89 7D 6F                     mov dword ptr [rbp + 0x6f], r15d
00AC761F  41 83 FF 14                     cmp r15d, 0x14
00AC7623  73 44                           jae 0x140ac7669
00AC7625  BF 16 02 00 00                  mov edi, 0x216
00AC762A  4D 8B FC                        mov r15, r12
00AC762D  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00AC7631  48 85 C0                        test rax, rax
00AC7634  74 08                           je 0x140ac763e
00AC7636  48 8B C8                        mov rcx, rax
00AC7639  E8 C6 AD E0 FF                  call 0x1408d2404
00AC763E  85 FF                           test edi, edi
00AC7640  74 0D                           je 0x140ac764f
00AC7642  4D 85 FF                        test r15, r15
00AC7645  74 08                           je 0x140ac764f
00AC7647  49 8B CF                        mov rcx, r15
00AC764A  E8 B5 AD E0 FF                  call 0x1408d2404
00AC764F  8B C7                           mov eax, edi
00AC7651  48 81 C4 88 00 00 00            add rsp, 0x88
00AC7658  41 5F                           pop r15
00AC765A  41 5E                           pop r14
00AC765C  41 5D                           pop r13
00AC765E  41 5C                           pop r12
00AC7660  5F                              pop rdi
00AC7661  5E                              pop rsi
00AC7662  5B                              pop rbx
00AC7663  5D                              pop rbp
00AC7664  C3                              ret
00AC7665  CC                              int3
00AC7666  49 03 DD                        add rbx, r13
00AC7669  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC766C  E8 8F 91 A3 FF                  call 0x140500800
00AC7671  85 C0                           test eax, eax
00AC7673  75 F1                           jne 0x140ac7666
00AC7675  66 83 3B 2C                     cmp word ptr [rbx], 0x2c
00AC7679  74 07                           je 0x140ac7682
00AC767B  BF 38 05 00 00                  mov edi, 0x538
00AC7680  EB A8                           jmp 0x140ac762a
00AC7682  49 03 DD                        add rbx, r13
00AC7685  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC7688  E8 73 91 A3 FF                  call 0x140500800
00AC768D  85 C0                           test eax, eax
00AC768F  75 F1                           jne 0x140ac7682
00AC7691  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
00AC7695  48 8B CB                        mov rcx, rbx
00AC7698  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00AC769C  E8 43 E1 CD FF                  call 0x1407a57e4
00AC76A1  8B F8                           mov edi, eax
00AC76A3  85 C0                           test eax, eax
00AC76A5  75 83                           jne 0x140ac762a
00AC76A7  48 8B 5D CF                     mov rbx, qword ptr [rbp - 0x31]
00AC76AB  EB 03                           jmp 0x140ac76b0
00AC76AD  49 03 DD                        add rbx, r13
00AC76B0  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC76B3  E8 48 91 A3 FF                  call 0x140500800
00AC76B8  85 C0                           test eax, eax
00AC76BA  75 F1                           jne 0x140ac76ad
00AC76BC  66 83 3B 2C                     cmp word ptr [rbx], 0x2c
00AC76C0  75 B9                           jne 0x140ac767b
00AC76C2  49 03 DD                        add rbx, r13
00AC76C5  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC76C8  E8 33 91 A3 FF                  call 0x140500800
00AC76CD  85 C0                           test eax, eax
00AC76CF  75 F1                           jne 0x140ac76c2
00AC76D1  4C 8D 45 DB                     lea r8, [rbp - 0x25]
00AC76D5  48 8B CB                        mov rcx, rbx
00AC76D8  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00AC76DC  E8 F3 DF CD FF                  call 0x1407a56d4
00AC76E1  8B F8                           mov edi, eax
00AC76E3  85 C0                           test eax, eax
00AC76E5  0F 85 3F FF FF FF               jne 0x140ac762a
00AC76EB  F7 45 DB C0 FF 00 00            test dword ptr [rbp - 0x25], 0xffc0
00AC76F2  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00AC76F6  74 05                           je 0x140ac76fd
00AC76F8  EB 81                           jmp 0x140ac767b
00AC76FA  49 03 F5                        add rsi, r13
00AC76FD  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7700  E8 FB 90 A3 FF                  call 0x140500800
00AC7705  85 C0                           test eax, eax
00AC7707  75 F1                           jne 0x140ac76fa
00AC7709  66 83 3E 2C                     cmp word ptr [rsi], 0x2c
00AC770D  0F 85 68 FF FF FF               jne 0x140ac767b
00AC7713  0F B7 4D 7F                     movzx ecx, word ptr [rbp + 0x7f]
00AC7717  49 03 F5                        add rsi, r13
00AC771A  48 8B DE                        mov rbx, rsi
00AC771D  83 E9 01                        sub ecx, 1
00AC7720  0F 84 AB 03 00 00               je 0x140ac7ad1
00AC7726  83 E9 01                        sub ecx, 1
00AC7729  0F 84 D1 02 00 00               je 0x140ac7a00
00AC772F  83 E9 01                        sub ecx, 1
00AC7732  0F 84 E6 01 00 00               je 0x140ac791e
00AC7738  41 2B CD                        sub ecx, r13d
00AC773B  0F 84 13 01 00 00               je 0x140ac7854
00AC7741  83 E9 01                        sub ecx, 1
00AC7744  0F 84 B6 02 00 00               je 0x140ac7a00
00AC774A  83 F9 0A                        cmp ecx, 0xa
00AC774D  0F 85 28 FF FF FF               jne 0x140ac767b
00AC7753  0F B7 03                        movzx eax, word ptr [rbx]
00AC7756  66 41 BD 29 00                  mov r13w, 0x29
00AC775B  66 85 C0                        test ax, ax
00AC775E  0F 84 8B 00 00 00               je 0x140ac77ef
00AC7764  0F B7 C8                        movzx ecx, ax
00AC7767  EB 07                           jmp 0x140ac7770
00AC7769  48 83 C3 02                     add rbx, 2
00AC776D  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC7770  E8 8B 90 A3 FF                  call 0x140500800
00AC7775  85 C0                           test eax, eax
00AC7777  75 F0                           jne 0x140ac7769
00AC7779  45 8B CE                        mov r9d, r14d
00AC777C  44 0F B7 13                     movzx r10d, word ptr [rbx]
00AC7780  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
00AC7784  41 0F B7 CA                     movzx ecx, r10w
00AC7788  45 8D 41 01                     lea r8d, [r9 + 1]
00AC778C  E8 C3 DE CD FF                  call 0x1407a5654
00AC7791  84 C0                           test al, al
00AC7793  74 12                           je 0x140ac77a7
00AC7795  48 83 C3 02                     add rbx, 2
00AC7799  45 3B C1                        cmp r8d, r9d
00AC779C  0F 82 CF 03 00 00               jb 0x140ac7b71
00AC77A2  45 8B C8                        mov r9d, r8d
00AC77A5  EB D5                           jmp 0x140ac777c
00AC77A7  41 D1 E8                        shr r8d, 1
00AC77AA  41 FF C4                        inc r12d
00AC77AD  43 8D 04 38                     lea eax, [r8 + r15]
00AC77B1  41 3B C7                        cmp eax, r15d
00AC77B4  0F 82 B7 03 00 00               jb 0x140ac7b71
00AC77BA  44 8D 78 04                     lea r15d, [rax + 4]
00AC77BE  44 3B F8                        cmp r15d, eax
00AC77C1  0F 82 AA 03 00 00               jb 0x140ac7b71
00AC77C7  41 0F B7 CA                     movzx ecx, r10w
00AC77CB  EB 07                           jmp 0x140ac77d4
00AC77CD  48 83 C3 02                     add rbx, 2
00AC77D1  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC77D4  E8 27 90 A3 FF                  call 0x140500800
00AC77D9  85 C0                           test eax, eax
00AC77DB  75 F0                           jne 0x140ac77cd
00AC77DD  0F B7 03                        movzx eax, word ptr [rbx]
00AC77E0  66 83 F8 2C                     cmp ax, 0x2c
00AC77E4  75 09                           jne 0x140ac77ef
00AC77E6  48 83 C3 02                     add rbx, 2
00AC77EA  E9 64 FF FF FF                  jmp 0x140ac7753
00AC77EF  66 41 3B C5                     cmp ax, r13w
00AC77F3  0F 85 46 03 00 00               jne 0x140ac7b3f
00AC77F9  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00AC77FF  41 8D 4C 24 FF                  lea ecx, [r12 - 1]
00AC7804  48 C1 E1 02                     shl rcx, 2
00AC7808  49 3B C8                        cmp rcx, r8
00AC780B  0F 87 B2 02 00 00               ja 0x140ac7ac3
00AC7811  42 8D 04 39                     lea eax, [rcx + r15]
00AC7815  41 3B C7                        cmp eax, r15d
00AC7818  0F 82 A5 02 00 00               jb 0x140ac7ac3
00AC781E  8D 58 03                        lea ebx, [rax + 3]
00AC7821  3B D8                           cmp ebx, eax
00AC7823  73 08                           jae 0x140ac782d
00AC7825  41 8B D8                        mov ebx, r8d
00AC7828  BF 16 02 00 00                  mov edi, 0x216
00AC782D  83 E3 FC                        and ebx, 0xfffffffc
00AC7830  8B CB                           mov ecx, ebx
00AC7832  89 5D D7                        mov dword ptr [rbp - 0x29], ebx
00AC7835  E8 4E E7 E5 FF                  call 0x140925f88
00AC783A  33 C9                           xor ecx, ecx
00AC783C  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00AC7840  4C 8B F8                        mov r15, rax
00AC7843  48 85 C0                        test rax, rax
00AC7846  0F 85 2C 03 00 00               jne 0x140ac7b78
00AC784C  8D 78 08                        lea edi, [rax + 8]
00AC784F  E9 D9 FD FF FF                  jmp 0x140ac762d
00AC7854  0F B7 03                        movzx eax, word ptr [rbx]
00AC7857  66 41 BD 29 00                  mov r13w, 0x29
00AC785C  66 85 C0                        test ax, ax
00AC785F  0F 84 A5 00 00 00               je 0x140ac790a
00AC7865  0F B7 C8                        movzx ecx, ax
00AC7868  EB 07                           jmp 0x140ac7871
00AC786A  48 83 C3 02                     add rbx, 2
00AC786E  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC7871  E8 8A 8F A3 FF                  call 0x140500800
00AC7876  85 C0                           test eax, eax
00AC7878  75 F0                           jne 0x140ac786a
00AC787A  4C 8D 4D 4F                     lea r9, [rbp + 0x4f]
00AC787E  48 8B CB                        mov rcx, rbx
00AC7881  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00AC7885  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00AC7889  E8 26 1A E6 FF                  call 0x1409292b4
00AC788E  8B F8                           mov edi, eax
00AC7890  85 C0                           test eax, eax
00AC7892  0F 85 30 02 00 00               jne 0x140ac7ac8
00AC7898  4C 8B 75 DF                     mov r14, qword ptr [rbp - 0x21]
00AC789C  33 C0                           xor eax, eax
00AC789E  4D 85 F6                        test r14, r14
00AC78A1  0F 84 96 07 00 00               je 0x140ac803d
00AC78A7  48 8B 5D CF                     mov rbx, qword ptr [rbp - 0x31]
00AC78AB  49 8B CE                        mov rcx, r14
00AC78AE  41 FF C4                        inc r12d
00AC78B1  E8 BA 59 99 FF                  call 0x14045d270
00AC78B6  42 8D 0C 38                     lea ecx, [rax + r15]
00AC78BA  41 3B CF                        cmp ecx, r15d
00AC78BD  0F 82 00 02 00 00               jb 0x140ac7ac3
00AC78C3  44 8D 79 04                     lea r15d, [rcx + 4]
00AC78C7  44 3B F9                        cmp r15d, ecx
00AC78CA  0F 82 F3 01 00 00               jb 0x140ac7ac3
00AC78D0  33 C0                           xor eax, eax
00AC78D2  38 45 4F                        cmp byte ptr [rbp + 0x4f], al
00AC78D5  74 15                           je 0x140ac78ec
00AC78D7  49 8B CE                        mov rcx, r14
00AC78DA  E8 25 AB E0 FF                  call 0x1408d2404
00AC78DF  45 33 F6                        xor r14d, r14d
00AC78E2  4C 89 75 DF                     mov qword ptr [rbp - 0x21], r14
00AC78E6  EB 04                           jmp 0x140ac78ec
00AC78E8  48 83 C3 02                     add rbx, 2
00AC78EC  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC78EF  E8 0C 8F A3 FF                  call 0x140500800
00AC78F4  85 C0                           test eax, eax
00AC78F6  75 F0                           jne 0x140ac78e8
00AC78F8  0F B7 03                        movzx eax, word ptr [rbx]
00AC78FB  66 83 F8 2C                     cmp ax, 0x2c
00AC78FF  75 09                           jne 0x140ac790a
00AC7901  48 83 C3 02                     add rbx, 2
00AC7905  E9 4A FF FF FF                  jmp 0x140ac7854
00AC790A  66 41 3B C5                     cmp ax, r13w
00AC790E  0F 84 E5 FE FF FF               je 0x140ac77f9
00AC7914  BF 38 05 00 00                  mov edi, 0x538
00AC7919  E9 AA 01 00 00                  jmp 0x140ac7ac8
00AC791E  0F B7 03                        movzx eax, word ptr [rbx]
00AC7921  66 41 BD 29 00                  mov r13w, 0x29
00AC7926  66 85 C0                        test ax, ax
00AC7929  0F 84 9D 00 00 00               je 0x140ac79cc
00AC792F  0F B7 C8                        movzx ecx, ax
00AC7932  E8 C9 8E A3 FF                  call 0x140500800
00AC7937  85 C0                           test eax, eax
00AC7939  74 14                           je 0x140ac794f
00AC793B  48 83 C3 02                     add rbx, 2
00AC793F  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC7942  E8 B9 8E A3 FF                  call 0x140500800
00AC7947  85 C0                           test eax, eax
00AC7949  75 F0                           jne 0x140ac793b
00AC794B  44 8B 7D 6F                     mov r15d, dword ptr [rbp + 0x6f]
00AC794F  66 83 3B 22                     cmp word ptr [rbx], 0x22
00AC7953  75 BF                           jne 0x140ac7914
00AC7955  48 83 C3 02                     add rbx, 2
00AC7959  0F B7 03                        movzx eax, word ptr [rbx]
00AC795C  66 83 F8 22                     cmp ax, 0x22
00AC7960  74 1B                           je 0x140ac797d
00AC7962  66 85 C0                        test ax, ax
00AC7965  74 16                           je 0x140ac797d
00AC7967  48 83 C3 02                     add rbx, 2
00AC796B  41 8D 46 01                     lea eax, [r14 + 1]
00AC796F  41 3B C6                        cmp eax, r14d
00AC7972  0F 82 4B 01 00 00               jb 0x140ac7ac3
00AC7978  44 8B F0                        mov r14d, eax
00AC797B  EB DC                           jmp 0x140ac7959
00AC797D  41 8D 4E 01                     lea ecx, [r14 + 1]
00AC7981  41 3B CE                        cmp ecx, r14d
00AC7984  0F 82 39 01 00 00               jb 0x140ac7ac3
00AC798A  44 8B F1                        mov r14d, ecx
00AC798D  66 83 F8 22                     cmp ax, 0x22
00AC7991  75 81                           jne 0x140ac7914
00AC7993  48 83 C3 02                     add rbx, 2
00AC7997  41 FF C4                        inc r12d
00AC799A  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC799D  E8 5E 8E A3 FF                  call 0x140500800
00AC79A2  85 C0                           test eax, eax
00AC79A4  74 14                           je 0x140ac79ba
00AC79A6  48 83 C3 02                     add rbx, 2
00AC79AA  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC79AD  E8 4E 8E A3 FF                  call 0x140500800
00AC79B2  85 C0                           test eax, eax
00AC79B4  75 F0                           jne 0x140ac79a6
00AC79B6  44 8B 7D 6F                     mov r15d, dword ptr [rbp + 0x6f]
00AC79BA  0F B7 03                        movzx eax, word ptr [rbx]
00AC79BD  66 83 F8 2C                     cmp ax, 0x2c
00AC79C1  75 09                           jne 0x140ac79cc
00AC79C3  48 83 C3 02                     add rbx, 2
00AC79C7  E9 52 FF FF FF                  jmp 0x140ac791e
00AC79CC  66 41 3B C5                     cmp ax, r13w
00AC79D0  0F 85 3E FF FF FF               jne 0x140ac7914
00AC79D6  41 8B C6                        mov eax, r14d
00AC79D9  48 03 C0                        add rax, rax
00AC79DC  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00AC79E2  49 3B C0                        cmp rax, r8
00AC79E5  0F 87 D8 00 00 00               ja 0x140ac7ac3
00AC79EB  42 8D 0C 38                     lea ecx, [rax + r15]
00AC79EF  41 3B CF                        cmp ecx, r15d
00AC79F2  0F 82 CB 00 00 00               jb 0x140ac7ac3
00AC79F8  44 8B F9                        mov r15d, ecx
00AC79FB  E9 FF FD FF FF                  jmp 0x140ac77ff
00AC7A00  44 0F B7 75 7F                  movzx r14d, word ptr [rbp + 0x7f]
00AC7A05  33 C9                           xor ecx, ecx
00AC7A07  0F B7 03                        movzx eax, word ptr [rbx]
00AC7A0A  66 41 BD 29 00                  mov r13w, 0x29
00AC7A0F  66 85 C0                        test ax, ax
00AC7A12  0F 84 95 00 00 00               je 0x140ac7aad
00AC7A18  48 8D 45 CB                     lea rax, [rbp - 0x35]
00AC7A1C  89 4D CB                        mov dword ptr [rbp - 0x35], ecx
00AC7A1F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC7A24  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00AC7A28  45 33 C9                        xor r9d, r9d
00AC7A2B  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00AC7A33  48 8B D3                        mov rdx, rbx
00AC7A36  33 C9                           xor ecx, ecx
00AC7A38  E8 37 AC A3 FF                  call 0x140502674
00AC7A3D  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00AC7A41  33 D2                           xor edx, edx
00AC7A43  48 3B CB                        cmp rcx, rbx
00AC7A46  75 05                           jne 0x140ac7a4d
00AC7A48  48 85 C0                        test rax, rax
00AC7A4B  74 53                           je 0x140ac7aa0
00AC7A4D  39 55 CB                        cmp dword ptr [rbp - 0x35], edx
00AC7A50  75 71                           jne 0x140ac7ac3
00AC7A52  66 41 83 FE 06                  cmp r14w, 6
00AC7A57  75 0A                           jne 0x140ac7a63
00AC7A59  48 83 F8 01                     cmp rax, 1
00AC7A5D  0F 87 B1 FE FF FF               ja 0x140ac7914
00AC7A63  48 8B D9                        mov rbx, rcx
00AC7A66  41 FF C4                        inc r12d
00AC7A69  0F B7 09                        movzx ecx, word ptr [rcx]
00AC7A6C  E8 8F 8D A3 FF                  call 0x140500800
00AC7A71  33 C9                           xor ecx, ecx
00AC7A73  85 C0                           test eax, eax
00AC7A75  74 17                           je 0x140ac7a8e
00AC7A77  48 83 C3 02                     add rbx, 2
00AC7A7B  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC7A7E  E8 7D 8D A3 FF                  call 0x140500800
00AC7A83  85 C0                           test eax, eax
00AC7A85  75 F0                           jne 0x140ac7a77
00AC7A87  44 0F B7 75 7F                  movzx r14d, word ptr [rbp + 0x7f]
00AC7A8C  33 C9                           xor ecx, ecx
00AC7A8E  0F B7 03                        movzx eax, word ptr [rbx]
00AC7A91  66 83 F8 2C                     cmp ax, 0x2c
00AC7A95  75 16                           jne 0x140ac7aad
00AC7A97  48 83 C3 02                     add rbx, 2
00AC7A9B  E9 67 FF FF FF                  jmp 0x140ac7a07
00AC7AA0  BF 38 05 00 00                  mov edi, 0x538
00AC7AA5  4C 8B FA                        mov r15, rdx
00AC7AA8  E9 80 FB FF FF                  jmp 0x140ac762d
00AC7AAD  66 41 3B C5                     cmp ax, r13w
00AC7AB1  0F 85 5D FE FF FF               jne 0x140ac7914
00AC7AB7  41 8B C4                        mov eax, r12d
00AC7ABA  48 C1 E0 03                     shl rax, 3
00AC7ABE  E9 19 FF FF FF                  jmp 0x140ac79dc
00AC7AC3  BF 16 02 00 00                  mov edi, 0x216
00AC7AC8  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
00AC7ACC  E9 5C FB FF FF                  jmp 0x140ac762d
00AC7AD1  0F B7 03                        movzx eax, word ptr [rbx]
00AC7AD4  66 41 BD 29 00                  mov r13w, 0x29
00AC7AD9  66 85 C0                        test ax, ax
00AC7ADC  74 6E                           je 0x140ac7b4c
00AC7ADE  48 8D 45 CB                     lea rax, [rbp - 0x35]
00AC7AE2  44 89 75 CB                     mov dword ptr [rbp - 0x35], r14d
00AC7AE6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC7AEB  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00AC7AEF  45 33 C9                        xor r9d, r9d
00AC7AF2  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00AC7AF7  48 8B D3                        mov rdx, rbx
00AC7AFA  33 C9                           xor ecx, ecx
00AC7AFC  E8 73 AB A3 FF                  call 0x140502674
00AC7B01  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00AC7B05  48 3B CB                        cmp rcx, rbx
00AC7B08  75 05                           jne 0x140ac7b0f
00AC7B0A  48 85 C0                        test rax, rax
00AC7B0D  74 30                           je 0x140ac7b3f
00AC7B0F  44 39 75 CB                     cmp dword ptr [rbp - 0x35], r14d
00AC7B13  75 5C                           jne 0x140ac7b71
00AC7B15  48 8B D9                        mov rbx, rcx
00AC7B18  41 FF C4                        inc r12d
00AC7B1B  0F B7 09                        movzx ecx, word ptr [rcx]
00AC7B1E  EB 07                           jmp 0x140ac7b27
00AC7B20  48 83 C3 02                     add rbx, 2
00AC7B24  0F B7 0B                        movzx ecx, word ptr [rbx]
00AC7B27  E8 D4 8C A3 FF                  call 0x140500800
00AC7B2C  85 C0                           test eax, eax
00AC7B2E  75 F0                           jne 0x140ac7b20
00AC7B30  0F B7 03                        movzx eax, word ptr [rbx]
00AC7B33  66 83 F8 2C                     cmp ax, 0x2c
00AC7B37  75 13                           jne 0x140ac7b4c
00AC7B39  48 83 C3 02                     add rbx, 2
00AC7B3D  EB 92                           jmp 0x140ac7ad1
00AC7B3F  BF 38 05 00 00                  mov edi, 0x538
00AC7B44  4D 8B FE                        mov r15, r14
00AC7B47  E9 E1 FA FF FF                  jmp 0x140ac762d
00AC7B4C  66 41 3B C5                     cmp ax, r13w
00AC7B50  75 ED                           jne 0x140ac7b3f
00AC7B52  41 8B C4                        mov eax, r12d
00AC7B55  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00AC7B5B  48 C1 E0 03                     shl rax, 3
00AC7B5F  49 3B C0                        cmp rax, r8
00AC7B62  77 0D                           ja 0x140ac7b71
00AC7B64  42 8D 0C 38                     lea ecx, [rax + r15]
00AC7B68  41 3B CF                        cmp ecx, r15d
00AC7B6B  0F 83 87 FE FF FF               jae 0x140ac79f8
00AC7B71  BF 16 02 00 00                  mov edi, 0x216
00AC7B76  EB CC                           jmp 0x140ac7b44
00AC7B78  0F B7 45 7F                     movzx eax, word ptr [rbp + 0x7f]
00AC7B7C  46 8D 34 A5 10 00 00 00         lea r14d, [r12*4 + 0x10]
00AC7B84  44 8B 45 F7                     mov r8d, dword ptr [rbp - 9]
00AC7B88  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
00AC7B8C  4D 03 C0                        add r8, r8
00AC7B8F  66 41 89 4F 06                  mov word ptr [r15 + 6], cx
00AC7B94  41 8B CE                        mov ecx, r14d
00AC7B97  66 41 89 47 04                  mov word ptr [r15 + 4], ax
00AC7B9C  49 03 CF                        add rcx, r15
00AC7B9F  8B 45 DB                        mov eax, dword ptr [rbp - 0x25]
00AC7BA2  45 89 37                        mov dword ptr [r15], r14d
00AC7BA5  44 03 75 EF                     add r14d, dword ptr [rbp - 0x11]
00AC7BA9  41 89 47 08                     mov dword ptr [r15 + 8], eax
00AC7BAD  45 89 67 0C                     mov dword ptr [r15 + 0xc], r12d
00AC7BB1  E8 8A EC BF FF                  call 0x1406c6840
00AC7BB6  0F B7 4D 7F                     movzx ecx, word ptr [rbp + 0x7f]
00AC7BBA  45 8B E6                        mov r12d, r14d
00AC7BBD  4D 03 E7                        add r12, r15
00AC7BC0  83 E9 01                        sub ecx, 1
00AC7BC3  0F 84 B8 03 00 00               je 0x140ac7f81
00AC7BC9  83 E9 01                        sub ecx, 1
00AC7BCC  0F 84 09 03 00 00               je 0x140ac7edb
00AC7BD2  83 E9 01                        sub ecx, 1
00AC7BD5  0F 84 1E 02 00 00               je 0x140ac7df9
00AC7BDB  83 E9 02                        sub ecx, 2
00AC7BDE  0F 84 43 01 00 00               je 0x140ac7d27
00AC7BE4  83 E9 01                        sub ecx, 1
00AC7BE7  0F 84 EE 02 00 00               je 0x140ac7edb
00AC7BED  83 F9 0A                        cmp ecx, 0xa
00AC7BF0  0F 85 F9 01 00 00               jne 0x140ac7def
00AC7BF6  0F B7 06                        movzx eax, word ptr [rsi]
00AC7BF9  66 85 C0                        test ax, ax
00AC7BFC  0F 84 18 04 00 00               je 0x140ac801a
00AC7C02  0F B7 C8                        movzx ecx, ax
00AC7C05  E8 F6 8B A3 FF                  call 0x140500800
00AC7C0A  45 33 D2                        xor r10d, r10d
00AC7C0D  85 C0                           test eax, eax
00AC7C0F  74 16                           je 0x140ac7c27
00AC7C11  48 83 C6 02                     add rsi, 2
00AC7C15  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7C18  E8 E3 8B A3 FF                  call 0x140500800
00AC7C1D  85 C0                           test eax, eax
00AC7C1F  75 F0                           jne 0x140ac7c11
00AC7C21  8B 5D D7                        mov ebx, dword ptr [rbp - 0x29]
00AC7C24  45 33 D2                        xor r10d, r10d
00AC7C27  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7C2A  4C 8B CE                        mov r9, rsi
00AC7C2D  45 8B C2                        mov r8d, r10d
00AC7C30  EB 0B                           jmp 0x140ac7c3d
00AC7C32  49 83 C1 02                     add r9, 2
00AC7C36  41 FF C0                        inc r8d
00AC7C39  41 0F B7 09                     movzx ecx, word ptr [r9]
00AC7C3D  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
00AC7C41  E8 0E DA CD FF                  call 0x1407a5654
00AC7C46  84 C0                           test al, al
00AC7C48  75 E8                           jne 0x140ac7c32
00AC7C4A  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
00AC7C4D  45 89 74 87 10                  mov dword ptr [r15 + rax*4 + 0x10], r14d
00AC7C52  41 8D 40 01                     lea eax, [r8 + 1]
00AC7C56  D1 E8                           shr eax, 1
00AC7C58  4D 8D 41 FE                     lea r8, [r9 - 2]
00AC7C5C  41 83 C6 04                     add r14d, 4
00AC7C60  41 89 04 24                     mov dword ptr [r12], eax
00AC7C64  45 8B D6                        mov r10d, r14d
00AC7C67  4D 03 D7                        add r10, r15
00AC7C6A  44 8D 58 FF                     lea r11d, [rax - 1]
00AC7C6E  44 03 F0                        add r14d, eax
00AC7C71  4C 3B C6                        cmp r8, rsi
00AC7C74  76 4C                           jbe 0x140ac7cc2
00AC7C76  41 0F B7 08                     movzx ecx, word ptr [r8]
00AC7C7A  48 8D 95 87 00 00 00            lea rdx, [rbp + 0x87]
00AC7C81  E8 CE D9 CD FF                  call 0x1407a5654
00AC7C86  84 C0                           test al, al
00AC7C88  0F 84 61 01 00 00               je 0x140ac7def
00AC7C8E  41 0F B7 48 FE                  movzx ecx, word ptr [r8 - 2]
00AC7C93  48 8D 55 77                     lea rdx, [rbp + 0x77]
00AC7C97  E8 B8 D9 CD FF                  call 0x1407a5654
00AC7C9C  84 C0                           test al, al
00AC7C9E  0F 84 4B 01 00 00               je 0x140ac7def
00AC7CA4  8A 4D 77                        mov cl, byte ptr [rbp + 0x77]
00AC7CA7  49 83 E8 04                     sub r8, 4
00AC7CAB  C0 E1 04                        shl cl, 4
00AC7CAE  B8 FF FF FF FF                  mov eax, 0xffffffff
00AC7CB3  0A 8D 87 00 00 00               or cl, byte ptr [rbp + 0x87]
00AC7CB9  43 88 0C 13                     mov byte ptr [r11 + r10], cl
00AC7CBD  44 03 D8                        add r11d, eax
00AC7CC0  EB AF                           jmp 0x140ac7c71
00AC7CC2  75 21                           jne 0x140ac7ce5
00AC7CC4  41 0F B7 08                     movzx ecx, word ptr [r8]
00AC7CC8  48 8D 95 87 00 00 00            lea rdx, [rbp + 0x87]
00AC7CCF  E8 80 D9 CD FF                  call 0x1407a5654
00AC7CD4  84 C0                           test al, al
00AC7CD6  0F 84 13 01 00 00               je 0x140ac7def
00AC7CDC  8A 85 87 00 00 00               mov al, byte ptr [rbp + 0x87]
00AC7CE2  41 88 02                        mov byte ptr [r10], al
00AC7CE5  41 0F B7 09                     movzx ecx, word ptr [r9]
00AC7CE9  49 8B F1                        mov rsi, r9
00AC7CEC  FF 45 C7                        inc dword ptr [rbp - 0x39]
00AC7CEF  45 8B E6                        mov r12d, r14d
00AC7CF2  4D 03 E7                        add r12, r15
00AC7CF5  E8 06 8B A3 FF                  call 0x140500800
00AC7CFA  85 C0                           test eax, eax
00AC7CFC  74 13                           je 0x140ac7d11
00AC7CFE  48 83 C6 02                     add rsi, 2
00AC7D02  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7D05  E8 F6 8A A3 FF                  call 0x140500800
00AC7D0A  85 C0                           test eax, eax
00AC7D0C  75 F0                           jne 0x140ac7cfe
00AC7D0E  8B 5D D7                        mov ebx, dword ptr [rbp - 0x29]
00AC7D11  0F B7 06                        movzx eax, word ptr [rsi]
00AC7D14  66 83 F8 2C                     cmp ax, 0x2c
00AC7D18  0F 85 FC 02 00 00               jne 0x140ac801a
00AC7D1E  48 83 C6 02                     add rsi, 2
00AC7D22  E9 CF FE FF FF                  jmp 0x140ac7bf6
00AC7D27  0F B7 06                        movzx eax, word ptr [rsi]
00AC7D2A  66 85 C0                        test ax, ax
00AC7D2D  0F 84 B2 00 00 00               je 0x140ac7de5
00AC7D33  0F B7 C8                        movzx ecx, ax
00AC7D36  EB 07                           jmp 0x140ac7d3f
00AC7D38  48 83 C6 02                     add rsi, 2
00AC7D3C  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7D3F  E8 BC 8A A3 FF                  call 0x140500800
00AC7D44  85 C0                           test eax, eax
00AC7D46  75 F0                           jne 0x140ac7d38
00AC7D48  4C 8D 4D 4F                     lea r9, [rbp + 0x4f]
00AC7D4C  48 8B CE                        mov rcx, rsi
00AC7D4F  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00AC7D53  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00AC7D57  E8 58 15 E6 FF                  call 0x1409292b4
00AC7D5C  8B F8                           mov edi, eax
00AC7D5E  85 C0                           test eax, eax
00AC7D60  0F 85 C7 F8 FF FF               jne 0x140ac762d
00AC7D66  48 8B 5D DF                     mov rbx, qword ptr [rbp - 0x21]
00AC7D6A  48 85 DB                        test rbx, rbx
00AC7D6D  0F 84 BA F8 FF FF               je 0x140ac762d
00AC7D73  48 8B CB                        mov rcx, rbx
00AC7D76  E8 F5 54 99 FF                  call 0x14045d270
00AC7D7B  8B 4D C7                        mov ecx, dword ptr [rbp - 0x39]
00AC7D7E  48 8B D3                        mov rdx, rbx
00AC7D81  44 8B C0                        mov r8d, eax
00AC7D84  45 89 74 8F 10                  mov dword ptr [r15 + rcx*4 + 0x10], r14d
00AC7D89  41 83 C6 04                     add r14d, 4
00AC7D8D  41 8B CE                        mov ecx, r14d
00AC7D90  44 03 F0                        add r14d, eax
00AC7D93  49 03 CF                        add rcx, r15
00AC7D96  41 89 04 24                     mov dword ptr [r12], eax
00AC7D9A  E8 A1 EA BF FF                  call 0x1406c6840
00AC7D9F  FF 45 C7                        inc dword ptr [rbp - 0x39]
00AC7DA2  33 C0                           xor eax, eax
00AC7DA4  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00AC7DA8  45 8B E6                        mov r12d, r14d
00AC7DAB  4D 03 E7                        add r12, r15
00AC7DAE  38 45 4F                        cmp byte ptr [rbp + 0x4f], al
00AC7DB1  74 14                           je 0x140ac7dc7
00AC7DB3  48 8B CB                        mov rcx, rbx
00AC7DB6  E8 49 A6 E0 FF                  call 0x1408d2404
00AC7DBB  33 DB                           xor ebx, ebx
00AC7DBD  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
00AC7DC1  EB 04                           jmp 0x140ac7dc7
00AC7DC3  48 83 C6 02                     add rsi, 2
00AC7DC7  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7DCA  E8 31 8A A3 FF                  call 0x140500800
00AC7DCF  85 C0                           test eax, eax
00AC7DD1  75 F0                           jne 0x140ac7dc3
00AC7DD3  0F B7 06                        movzx eax, word ptr [rsi]
00AC7DD6  66 83 F8 2C                     cmp ax, 0x2c
00AC7DDA  75 09                           jne 0x140ac7de5
00AC7DDC  48 83 C6 02                     add rsi, 2
00AC7DE0  E9 42 FF FF FF                  jmp 0x140ac7d27
00AC7DE5  66 41 3B C5                     cmp ax, r13w
00AC7DE9  0F 84 CC 00 00 00               je 0x140ac7ebb
00AC7DEF  BF 38 05 00 00                  mov edi, 0x538
00AC7DF4  E9 34 F8 FF FF                  jmp 0x140ac762d
00AC7DF9  0F B7 06                        movzx eax, word ptr [rsi]
00AC7DFC  66 85 C0                        test ax, ax
00AC7DFF  0F 84 A8 00 00 00               je 0x140ac7ead
00AC7E05  0F B7 C8                        movzx ecx, ax
00AC7E08  EB 07                           jmp 0x140ac7e11
00AC7E0A  48 83 C6 02                     add rsi, 2
00AC7E0E  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7E11  E8 EA 89 A3 FF                  call 0x140500800
00AC7E16  85 C0                           test eax, eax
00AC7E18  75 F0                           jne 0x140ac7e0a
00AC7E1A  66 83 3E 22                     cmp word ptr [rsi], 0x22
00AC7E1E  0F 85 F0 FA FF FF               jne 0x140ac7914
00AC7E24  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
00AC7E28  4C 8D 7E 02                     lea r15, [rsi + 2]
00AC7E2C  33 D2                           xor edx, edx
00AC7E2E  8B CA                           mov ecx, edx
00AC7E30  EB 13                           jmp 0x140ac7e45
00AC7E32  66 85 C0                        test ax, ax
00AC7E35  0F 84 D9 FA FF FF               je 0x140ac7914
00AC7E3B  49 83 C7 02                     add r15, 2
00AC7E3F  FF C1                           inc ecx
00AC7E41  41 0F B7 07                     movzx eax, word ptr [r15]
00AC7E45  66 83 F8 22                     cmp ax, 0x22
00AC7E49  75 E7                           jne 0x140ac7e32
00AC7E4B  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
00AC7E4E  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
00AC7E52  44 89 74 82 10                  mov dword ptr [rdx + rax*4 + 0x10], r14d
00AC7E57  45 8D 34 4E                     lea r14d, [r14 + rcx*2]
00AC7E5B  8B C1                           mov eax, ecx
00AC7E5D  48 8D 56 02                     lea rdx, [rsi + 2]
00AC7E61  49 8B CC                        mov rcx, r12
00AC7E64  41 83 C6 02                     add r14d, 2
00AC7E68  48 8D 1C 00                     lea rbx, [rax + rax]
00AC7E6C  4C 8B C3                        mov r8, rbx
00AC7E6F  E8 CC E9 BF FF                  call 0x1406c6840
00AC7E74  33 C0                           xor eax, eax
00AC7E76  49 8D 77 02                     lea rsi, [r15 + 2]
00AC7E7A  66 42 89 04 23                  mov word ptr [rbx + r12], ax
00AC7E7F  45 8B E6                        mov r12d, r14d
00AC7E82  4C 03 65 BF                     add r12, qword ptr [rbp - 0x41]
00AC7E86  FF 45 C7                        inc dword ptr [rbp - 0x39]
00AC7E89  EB 04                           jmp 0x140ac7e8f
00AC7E8B  48 83 C6 02                     add rsi, 2
00AC7E8F  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7E92  E8 69 89 A3 FF                  call 0x140500800
00AC7E97  85 C0                           test eax, eax
00AC7E99  75 F0                           jne 0x140ac7e8b
00AC7E9B  0F B7 06                        movzx eax, word ptr [rsi]
00AC7E9E  66 83 F8 2C                     cmp ax, 0x2c
00AC7EA2  75 09                           jne 0x140ac7ead
00AC7EA4  48 83 C6 02                     add rsi, 2
00AC7EA8  E9 4C FF FF FF                  jmp 0x140ac7df9
00AC7EAD  66 41 3B C5                     cmp ax, r13w
00AC7EB1  0F 85 5D FA FF FF               jne 0x140ac7914
00AC7EB7  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
00AC7EBB  8B 5D D7                        mov ebx, dword ptr [rbp - 0x29]
00AC7EBE  48 8B 45 5F                     mov rax, qword ptr [rbp + 0x5f]
00AC7EC2  48 8B 4D 57                     mov rcx, qword ptr [rbp + 0x57]
00AC7EC6  4C 89 38                        mov qword ptr [rax], r15
00AC7EC9  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00AC7ECD  89 18                           mov dword ptr [rax], ebx
00AC7ECF  48 8D 46 02                     lea rax, [rsi + 2]
00AC7ED3  48 89 01                        mov qword ptr [rcx], rax
00AC7ED6  E9 52 F7 FF FF                  jmp 0x140ac762d
00AC7EDB  33 C9                           xor ecx, ecx
00AC7EDD  0F B7 06                        movzx eax, word ptr [rsi]
00AC7EE0  66 85 C0                        test ax, ax
00AC7EE3  0F 84 31 01 00 00               je 0x140ac801a
00AC7EE9  48 8D 45 CB                     lea rax, [rbp - 0x35]
00AC7EED  89 4D CB                        mov dword ptr [rbp - 0x35], ecx
00AC7EF0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC7EF5  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00AC7EF9  45 33 C9                        xor r9d, r9d
00AC7EFC  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00AC7F04  48 8B D6                        mov rdx, rsi
00AC7F07  33 C9                           xor ecx, ecx
00AC7F09  E8 66 A7 A3 FF                  call 0x140502674
00AC7F0E  33 C9                           xor ecx, ecx
00AC7F10  48 39 75 CF                     cmp qword ptr [rbp - 0x31], rsi
00AC7F14  75 09                           jne 0x140ac7f1f
00AC7F16  48 85 C0                        test rax, rax
00AC7F19  0F 84 D0 FE FF FF               je 0x140ac7def
00AC7F1F  39 4D CB                        cmp dword ptr [rbp - 0x35], ecx
00AC7F22  0F 85 01 01 00 00               jne 0x140ac8029
00AC7F28  8B 55 C7                        mov edx, dword ptr [rbp - 0x39]
00AC7F2B  45 89 74 97 10                  mov dword ptr [r15 + rdx*4 + 0x10], r14d
00AC7F30  FF C2                           inc edx
00AC7F32  49 89 04 24                     mov qword ptr [r12], rax
00AC7F36  41 83 C6 08                     add r14d, 8
00AC7F3A  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00AC7F3E  45 8B E6                        mov r12d, r14d
00AC7F41  4D 03 E7                        add r12, r15
00AC7F44  89 55 C7                        mov dword ptr [rbp - 0x39], edx
00AC7F47  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7F4A  E8 B1 88 A3 FF                  call 0x140500800
00AC7F4F  33 C9                           xor ecx, ecx
00AC7F51  85 C0                           test eax, eax
00AC7F53  74 16                           je 0x140ac7f6b
00AC7F55  48 83 C6 02                     add rsi, 2
00AC7F59  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7F5C  E8 9F 88 A3 FF                  call 0x140500800
00AC7F61  85 C0                           test eax, eax
00AC7F63  75 F0                           jne 0x140ac7f55
00AC7F65  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
00AC7F69  33 C9                           xor ecx, ecx
00AC7F6B  0F B7 06                        movzx eax, word ptr [rsi]
00AC7F6E  66 83 F8 2C                     cmp ax, 0x2c
00AC7F72  0F 85 A2 00 00 00               jne 0x140ac801a
00AC7F78  48 83 C6 02                     add rsi, 2
00AC7F7C  E9 5C FF FF FF                  jmp 0x140ac7edd
00AC7F81  33 C9                           xor ecx, ecx
00AC7F83  0F B7 06                        movzx eax, word ptr [rsi]
00AC7F86  66 85 C0                        test ax, ax
00AC7F89  0F 84 8B 00 00 00               je 0x140ac801a
00AC7F8F  48 8D 45 CB                     lea rax, [rbp - 0x35]
00AC7F93  89 4D CB                        mov dword ptr [rbp - 0x35], ecx
00AC7F96  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC7F9B  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00AC7F9F  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00AC7FA3  45 33 C9                        xor r9d, r9d
00AC7FA6  33 C9                           xor ecx, ecx
00AC7FA8  48 8B D6                        mov rdx, rsi
00AC7FAB  E8 C4 A6 A3 FF                  call 0x140502674
00AC7FB0  33 C9                           xor ecx, ecx
00AC7FB2  48 39 75 CF                     cmp qword ptr [rbp - 0x31], rsi
00AC7FB6  75 09                           jne 0x140ac7fc1
00AC7FB8  48 85 C0                        test rax, rax
00AC7FBB  0F 84 2E FE FF FF               je 0x140ac7def
00AC7FC1  39 4D CB                        cmp dword ptr [rbp - 0x35], ecx
00AC7FC4  75 63                           jne 0x140ac8029
00AC7FC6  8B 55 C7                        mov edx, dword ptr [rbp - 0x39]
00AC7FC9  45 89 74 97 10                  mov dword ptr [r15 + rdx*4 + 0x10], r14d
00AC7FCE  FF C2                           inc edx
00AC7FD0  49 89 04 24                     mov qword ptr [r12], rax
00AC7FD4  41 83 C6 08                     add r14d, 8
00AC7FD8  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00AC7FDC  45 8B E6                        mov r12d, r14d
00AC7FDF  4D 03 E7                        add r12, r15
00AC7FE2  89 55 C7                        mov dword ptr [rbp - 0x39], edx
00AC7FE5  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7FE8  E8 13 88 A3 FF                  call 0x140500800
00AC7FED  33 C9                           xor ecx, ecx
00AC7FEF  85 C0                           test eax, eax
00AC7FF1  74 15                           je 0x140ac8008
00AC7FF3  48 83 C6 02                     add rsi, 2
00AC7FF7  0F B7 0E                        movzx ecx, word ptr [rsi]
00AC7FFA  E8 01 88 A3 FF                  call 0x140500800
00AC7FFF  85 C0                           test eax, eax
00AC8001  75 F0                           jne 0x140ac7ff3
00AC8003  8B 5D D7                        mov ebx, dword ptr [rbp - 0x29]
00AC8006  33 C9                           xor ecx, ecx
00AC8008  0F B7 06                        movzx eax, word ptr [rsi]
00AC800B  66 83 F8 2C                     cmp ax, 0x2c
00AC800F  75 09                           jne 0x140ac801a
00AC8011  48 83 C6 02                     add rsi, 2
00AC8015  E9 69 FF FF FF                  jmp 0x140ac7f83
00AC801A  66 41 3B C5                     cmp ax, r13w
00AC801E  0F 84 9A FE FF FF               je 0x140ac7ebe
00AC8024  E9 C6 FD FF FF                  jmp 0x140ac7def
00AC8029  BF 16 02 00 00                  mov edi, 0x216
00AC802E  E9 FA F5 FF FF                  jmp 0x140ac762d
00AC8033  BF 57 00 00 00                  mov edi, 0x57
00AC8038  E9 F0 F5 FF FF                  jmp 0x140ac762d
00AC803D  4C 8B F8                        mov r15, rax
00AC8040  E9 E8 F5 FF FF                  jmp 0x140ac762d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalGetRelativeAttributeForString(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (136);
    v_r14 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 49) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = 0;
    *(unsigned __int16 *)(v_rsp - 71 + 127) = 0;
    *(unsigned int *)(v_rsp - 71 - 37) = 0;
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 79) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 135) = 0;
    *(unsigned __int8 *)(v_rsp - 71 + 119) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 33) = 0;
    *(unsigned int *)(v_rsp - 71 - 53) = 0;
    if (a1 == 0) goto loc_00AC8033;
    if (a2 == 0) goto loc_00AC8033;
    if (a3 == 0) goto loc_00AC8033;
    if (a4 == 0) goto loc_00AC8033;
    *(unsigned __int64 *)(a3) = 0;
    *(unsigned int *)(a4) = 0;
    if ((*(unsigned __int16 *)(a1)) == 40) goto loc_00AC7583;
loc_00AC7579:
    goto loc_00AC764F;
loc_00AC7583:
    result = iswspace(*(unsigned __int16 *)(a1 + 2), a2, a3, a4);
    goto loc_00AC75A2;
loc_00AC7597:
    v_rdi = (a1 + 2) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rdi), a2, a3, a4);
loc_00AC75A2:
    if ((unsigned int)(result) != 0) goto loc_00AC7597;
    if ((*(unsigned __int16 *)(v_rdi)) != 34) goto loc_00AC7579;
    v_rdi = (v_rdi) + (2);
loc_00AC75B2:
    result = IsLegalAttributeChar2(*(unsigned __int16 *)(v_rdi), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AC75D8;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)) == 0) goto loc_00AC7579;
    v_rbx = (v_rdi) + (2);
    if (((unsigned int)(0 + 1)) < 0) goto loc_00AC75D1;
    goto loc_00AC75B2;
loc_00AC75D1:
    goto loc_00AC764F;
loc_00AC75D8:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi))) != 34) goto loc_00AC7579;
    if ((unsigned int)((unsigned int)((unsigned int)(0 + 1))) == 0) goto loc_00AC7579;
    v_rbx = (v_rbx) + (2);
    result = DecodeAttributeName(534, (unsigned int)((unsigned int)(0 + 1)) + (unsigned int)((unsigned int)(0 + 1)) * 1, v_rsp - 71 - 25, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC762D;
    result = (result) | (-1);
loc_00AC7602:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 25) + result * 2)) != 0) goto loc_00AC7602;
    result = (unsigned int)((result) + 1);
    *(unsigned __int64 *)(v_rsp - 71 - 9) = result;
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned int *)(v_rsp - 71 - 17) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 71 + 111) = (unsigned int)(result + 20);
    if (((unsigned int)(result + 20)) >= 20) goto loc_00AC7669;
loc_00AC762A:
loc_00AC762D:
    result = *(unsigned __int64 *)(v_rsp - 71 - 25);
    if (*(unsigned __int64 *)(v_rsp - 71 - 25) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 25);
        result = PdcCloseEvent(a1, (unsigned int)((unsigned int)(0 + 1)) + (unsigned int)((unsigned int)(0 + 1)) * 1, v_rsp - 71 - 25, a4);
    }
    if (534 == 0) goto loc_00AC764F;
    if (0 != 0) {
        a1 = 0;
        result = PdcCloseEvent(a1, (unsigned int)((unsigned int)(0 + 1)) + (unsigned int)((unsigned int)(0 + 1)) * 1, v_rsp - 71 - 25, a4);
    }
    v_rsp = (v_rsp) + (136);
    return 534;
loc_00AC7666:
    v_rbx = (v_rbx) + (2);
loc_00AC7669:
    result = iswspace(*(unsigned __int16 *)(v_rbx), (unsigned int)((unsigned int)(0 + 1)) + (unsigned int)((unsigned int)(0 + 1)) * 1, v_rsp - 71 - 25, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7666;
    if ((*(unsigned __int16 *)(v_rbx)) == 44) goto loc_00AC7682;
loc_00AC767B:
    goto loc_00AC762A;
loc_00AC7682:
    v_rbx = (v_rbx) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rbx), (unsigned int)((unsigned int)(0 + 1)) + (unsigned int)((unsigned int)(0 + 1)) * 1, v_rsp - 71 - 25, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7682;
    result = GetValueType(v_rbx, v_rsp - 71 - 49, v_rsp - 71 + 127, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC762A;
    goto loc_00AC76B0;
loc_00AC76AD:
    v_rbx = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
loc_00AC76B0:
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 - 49, v_rsp - 71 + 127, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC76AD;
    if ((*(unsigned __int16 *)(v_rbx)) != 44) goto loc_00AC767B;
loc_00AC76C2:
    v_rbx = (v_rbx) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 - 49, v_rsp - 71 + 127, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC76C2;
    result = GetFlags(v_rbx, v_rsp - 71 - 49, v_rsp - 71 - 37, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC762A;
    if (((*(unsigned int *)(v_rsp - 71 - 37)) & (0xFFC0ULL)) == 0) goto loc_00AC76FD;
    goto loc_00AC767B;
loc_00AC76FA:
    v_rsi = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
loc_00AC76FD:
    result = iswspace(*(unsigned __int16 *)(v_rsi), v_rsp - 71 - 49, v_rsp - 71 - 37, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC76FA;
    if ((*(unsigned __int16 *)(v_rsi)) != 44) goto loc_00AC767B;
    v_rsi = (v_rsi) + (2);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsp - 71 + 127)) - (1));
    if (condition_is_equal) goto loc_00AC7AD1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AC7A00;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AC791E;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AC7854;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AC7A00;
    if (((unsigned int)(a1)) != 10) goto loc_00AC767B;
loc_00AC7753:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AC77EF;
    goto loc_00AC7770;
loc_00AC7769:
    v_rbx = (v_rsi) + (2);
loc_00AC7770:
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 - 49, v_rsp - 71 - 37, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7769;
loc_00AC777C:
    result = GetDigitFromChar((unsigned __int16)(*(unsigned __int16 *)(v_rbx)), v_rsp - 71 + 111, 0 + 1, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00AC77A7;
    v_rbx = (v_rbx) + (2);
    if (((unsigned int)(0 + 1)) < 0) goto loc_00AC7B71;
    goto loc_00AC777C;
loc_00AC77A7:
    a3 = (unsigned int)((0 + 1) >> (1));
    v_r12 = (unsigned int)((0) + 1);
    if (((unsigned int)(a3 + 0 * 1)) < 0) goto loc_00AC7B71;
    if (((unsigned int)(a3 + 0 * 1 + 4)) < ((unsigned int)(a3 + 0 * 1))) goto loc_00AC7B71;
    goto loc_00AC77D4;
loc_00AC77CD:
    v_rbx = (v_rbx) + (2);
loc_00AC77D4:
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 + 111, a3, (unsigned int)((unsigned int)(0 + 1)));
    if ((unsigned int)(result) != 0) goto loc_00AC77CD;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 44) goto loc_00AC77EF;
    v_rbx = (v_rbx) + (2);
    goto loc_00AC7753;
loc_00AC77EF:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 41) goto loc_00AC7B3F;
loc_00AC77F9:
loc_00AC77FF:
    a1 = (v_r12 - 1) << (2);
    if (a1 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00AC7AC3;
    if (((unsigned int)(a1 + a3 + 0 * 1 + 4 * 1)) < ((unsigned int)(a3 + 0 * 1 + 4))) goto loc_00AC7AC3;
    v_rbx = a1 + a3 + 0 * 1 + 4 * 1 + 3;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(a1 + a3 + 0 * 1 + 4 * 1 + 3)) < ((unsigned int)(a1 + a3 + 0 * 1 + 4 * 1))) {
        v_rbx = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
        v_rdi = 534;
    }
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFCULL));
    *(unsigned int *)(v_rsp - 71 - 41) = (unsigned int)(v_rbx);
    result = SddlpAlloc((unsigned int)((unsigned int)(v_rbx)), v_rsp - 71 + 111, (unsigned int)(0xFFFFFFFFULL), (unsigned int)((unsigned int)(0 + 1)));
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 65) = result;
    if (result != 0) goto loc_00AC7B78;
    goto loc_00AC762D;
loc_00AC7854:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00AC790A;
    goto loc_00AC7871;
loc_00AC786A:
    v_rbx = (v_rbx) + (2);
loc_00AC7871:
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 + 111, (unsigned int)(0xFFFFFFFFULL), (unsigned int)((unsigned int)(0 + 1)));
    if ((unsigned int)(result) != 0) goto loc_00AC786A;
    result = LocalGetSidForString(v_rbx, v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC7AC8;
    result = 0;
    if (*(unsigned __int64 *)(v_rsp - 71 - 33) == 0) goto loc_00AC803D;
    v_r12 = (unsigned int)((v_r12) + 1);
    result = RtlLengthSid(*(unsigned __int64 *)(v_rsp - 71 - 33), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if (((unsigned int)(result + result * 1)) < ((unsigned int)(result))) goto loc_00AC7AC3;
    if (((unsigned int)(result + result * 1 + 4)) < ((unsigned int)(result + result * 1))) goto loc_00AC7AC3;
    result = 0;
    if ((*(unsigned __int8 *)(v_rsp - 71 + 79)) == 0) goto loc_00AC78EC;
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 71 - 33), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    v_r14 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 33) = 0;
    goto loc_00AC78EC;
loc_00AC78E8:
    v_rbx = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
loc_00AC78EC:
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC78E8;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 44) goto loc_00AC790A;
    v_rbx = (v_rbx) + (2);
    goto loc_00AC7854;
loc_00AC790A:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) == 41) goto loc_00AC77F9;
loc_00AC7914:
    goto loc_00AC7AC8;
loc_00AC791E:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00AC79CC;
    result = iswspace((unsigned __int16)(*(unsigned __int16 *)(v_rbx)), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if ((unsigned int)(result) == 0) goto loc_00AC794F;
loc_00AC793B:
    v_rbx = (v_rbx) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC793B;
loc_00AC794F:
    if ((*(unsigned __int16 *)(v_rbx)) != 34) goto loc_00AC7914;
    v_rbx = (v_rbx) + (2);
loc_00AC7959:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) == 34) goto loc_00AC797D;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00AC797D;
    v_rbx = (v_rbx) + (2);
    if (((unsigned int)(v_r14 + 1)) < 0) goto loc_00AC7AC3;
    goto loc_00AC7959;
loc_00AC797D:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14 + 1)) + 1)) < ((unsigned int)((unsigned int)((unsigned int)(v_r14 + 1))))) goto loc_00AC7AC3;
    if (((unsigned __int16)(v_r14 + 1)) != 34) goto loc_00AC7914;
    v_rbx = (v_rbx) + (2);
    v_r12 = (unsigned int)((v_r12) + 1);
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if ((unsigned int)(result) == 0) goto loc_00AC79BA;
loc_00AC79A6:
    v_rbx = (v_rbx) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC79A6;
loc_00AC79BA:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 44) goto loc_00AC79CC;
    v_rbx = (v_rbx) + (2);
    goto loc_00AC791E;
loc_00AC79CC:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 41) goto loc_00AC7914;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14 + 1)) + 1))))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14 + 1)) + 1)))));
loc_00AC79DC:
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00AC7AC3;
    if (((unsigned int)(result + (unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)) * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111))))) goto loc_00AC7AC3;
loc_00AC79F8:
    goto loc_00AC77FF;
loc_00AC7A00:
    a1 = 0;
loc_00AC7A07:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00AC7AAD;
    *(unsigned int *)(v_rsp - 71 - 53) = 0;
    v_stack_p28 = v_rsp - 71 - 53;
    a4 = 0;
    v_stack_p20 = 1;
    a1 = 0;
    result = wcstoxq(a1, v_rbx, v_rsp - 71 - 49, a4);
    a2 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 71 - 49)) != v_rbx) goto loc_00AC7A4D;
    if (result == 0) goto loc_00AC7AA0;
loc_00AC7A4D:
    if ((*(unsigned int *)(v_rsp - 71 - 53)) != 0) goto loc_00AC7AC3;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 71 + 127))) != 6) goto loc_00AC7A63;
    if (result > 1) goto loc_00AC7914;
loc_00AC7A63:
    v_r12 = (unsigned int)((v_r12) + 1);
    result = iswspace(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 49)), a2, v_rsp - 71 - 49, a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AC7A8E;
loc_00AC7A77:
    v_rbx = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rbx), a2, v_rsp - 71 - 49, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7A77;
    a1 = 0;
loc_00AC7A8E:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 44) goto loc_00AC7AAD;
    v_rbx = (v_rbx) + (2);
    goto loc_00AC7A07;
loc_00AC7AA0:
    goto loc_00AC762D;
loc_00AC7AAD:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 41) goto loc_00AC7914;
    result = ((unsigned int)((unsigned int)(v_r12))) << (3);
    goto loc_00AC79DC;
loc_00AC7AC3:
loc_00AC7AC8:
    goto loc_00AC762D;
loc_00AC7AD1:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00AC7B4C;
    *(unsigned int *)(v_rsp - 71 - 53) = (unsigned int)(*(unsigned __int16 *)(v_rsp - 71 + 127));
    v_stack_p28 = v_rsp - 71 - 53;
    a4 = 0;
    v_stack_p20 = (unsigned int)(*(unsigned __int16 *)(v_rsp - 71 + 127));
    a1 = 0;
    result = wcstoxq(a1, v_rbx, v_rsp - 71 - 49, a4);
    if ((*(unsigned __int64 *)(v_rsp - 71 - 49)) != v_rbx) goto loc_00AC7B0F;
    if (result == 0) goto loc_00AC7B3F;
loc_00AC7B0F:
    if ((*(unsigned int *)(v_rsp - 71 - 53)) != ((unsigned int)(*(unsigned __int16 *)(v_rsp - 71 + 127)))) goto loc_00AC7B71;
    v_r12 = (unsigned int)((v_r12) + 1);
    goto loc_00AC7B27;
loc_00AC7B20:
    v_rbx = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
loc_00AC7B27:
    result = iswspace(*(unsigned __int16 *)(v_rbx), v_rbx, v_rsp - 71 - 49, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7B20;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 44) goto loc_00AC7B4C;
    v_rbx = (v_rbx) + (2);
    goto loc_00AC7AD1;
loc_00AC7B3F:
loc_00AC7B44:
    goto loc_00AC762D;
loc_00AC7B4C:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) != 41) goto loc_00AC7B3F;
    result = ((unsigned int)((unsigned int)(v_r12))) << (3);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00AC7B71;
    if (((unsigned int)(result + *(unsigned __int16 *)(v_rsp - 71 + 127) * 1)) >= ((unsigned int)(*(unsigned __int16 *)(v_rsp - 71 + 127)))) goto loc_00AC79F8;
loc_00AC7B71:
    goto loc_00AC7B44;
loc_00AC7B78:
    a3 = ((unsigned int)(*(unsigned int *)(v_rsp - 71 - 9))) + ((unsigned int)(*(unsigned int *)(v_rsp - 71 - 9)));
    *(unsigned __int16 *)(*(unsigned __int16 *)(v_rsp - 71 + 127) + 6) = (unsigned __int16)(result + *(unsigned __int16 *)(v_rsp - 71 + 127) * 1);
    *(unsigned __int16 *)(*(unsigned __int16 *)(v_rsp - 71 + 127) + 4) = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 71 + 127));
    a1 = ((unsigned int)((unsigned int)(v_r12 * 4 + 16))) + (*(unsigned __int16 *)(v_rsp - 71 + 127));
    *(unsigned int *)(*(unsigned __int16 *)(v_rsp - 71 + 127)) = (unsigned int)(v_r12 * 4 + 16);
    v_r14 = (unsigned int)((v_r12 * 4 + 16) + (*(unsigned int *)(v_rsp - 71 - 17)));
    *(unsigned int *)(*(unsigned __int16 *)(v_rsp - 71 + 127) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 37)));
    *(unsigned int *)(*(unsigned __int16 *)(v_rsp - 71 + 127) + 12) = (unsigned int)(v_r12);
    result = memcpy(a1, *(unsigned __int64 *)(v_rsp - 71 - 25), a3, a4);
    v_r12 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int16 *)(v_rsp - 71 + 127));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsp - 71 + 127)) - (1));
    if (condition_is_equal) goto loc_00AC7F81;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AC7EDB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AC7DF9;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AC7D27;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AC7EDB;
    if (((unsigned int)(a1)) != 10) goto loc_00AC7DEF;
loc_00AC7BF6:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AC801A;
    result = iswspace((unsigned __int16)(*(unsigned __int16 *)(v_rsi)), *(unsigned __int64 *)(v_rsp - 71 - 25), a3, a4);
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AC7C27;
loc_00AC7C11:
    v_rsi = (v_rsi) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rsi), *(unsigned __int64 *)(v_rsp - 71 - 25), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7C11;
    v_r10 = 0;
loc_00AC7C27:
    goto loc_00AC7C3D;
loc_00AC7C32:
    a4 = (v_rsi) + (2);
    a3 = (unsigned int)((0) + 1);
loc_00AC7C3D:
    result = GetDigitFromChar(*(unsigned __int16 *)(a4), v_rsp - 71 + 111, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AC7C32;
    *(unsigned int *)(*(unsigned __int16 *)(v_rsp - 71 + 127) + (unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)) * 4 + 16) = (unsigned int)(v_r14);
    result = (unsigned int)((a3 + 1) >> (1));
    v_r14 = (unsigned int)((v_r14) + (4));
    *(unsigned int *)(v_r12) = (unsigned int)(result);
    v_r10 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int16 *)(v_rsp - 71 + 127));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
loc_00AC7C71:
    if ((a4 - 2) <= v_rsi) goto loc_00AC7CC2;
    result = GetDigitFromChar(*(unsigned __int16 *)(a4 - 2), v_rsp - 71 + 135, a4 - 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AC7DEF;
    result = GetDigitFromChar(*(unsigned __int16 *)(a4 - 2 - 2), v_rsp - 71 + 119, a4 - 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AC7DEF;
    a3 = (a4 - 2) - (4);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rsp - 71 + 119)) << (4));
    a1 = (unsigned __int8)((a1) | (*(unsigned __int8 *)(v_rsp - 71 + 135)));
    *(unsigned __int8 *)(result - 1 + v_r10 * 1) = (unsigned __int8)(a1);
    v_r11 = (unsigned int)((result - 1) + ((unsigned int)((unsigned int)(0xFFFFFFFFULL))));
    goto loc_00AC7C71;
loc_00AC7CC2:
    if (condition_is_not_equal) goto loc_00AC7CE5;
    result = GetDigitFromChar(*(unsigned __int16 *)(a3), v_rsp - 71 + 135, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AC7DEF;
    *(unsigned __int8 *)(v_r10) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 135));
loc_00AC7CE5:
    v_r12 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int16 *)(v_rsp - 71 + 127));
    result = iswspace(*(unsigned __int16 *)(a4), v_rsp - 71 + 135, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AC7D11;
loc_00AC7CFE:
    v_rsi = (a4) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rsi), v_rsp - 71 + 135, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7CFE;
loc_00AC7D11:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 44) goto loc_00AC801A;
    v_rsi = (v_rsi) + (2);
    goto loc_00AC7BF6;
loc_00AC7D27:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AC7DE5;
    goto loc_00AC7D3F;
loc_00AC7D38:
    v_rsi = (v_rsi) + (2);
loc_00AC7D3F:
    result = iswspace(*(unsigned __int16 *)(v_rsi), v_rsp - 71 + 135, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7D38;
    result = LocalGetSidForString(v_rsi, v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC762D;
    if (*(unsigned __int64 *)(v_rsp - 71 - 33) == 0) goto loc_00AC762D;
    result = RtlLengthSid(*(unsigned __int64 *)(v_rsp - 71 - 33), v_rsp - 71 - 33, v_rsp - 71 - 49, v_rsp - 71 + 79);
    *(unsigned int *)(*(unsigned __int16 *)(v_rsp - 71 + 127) + (unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)) * 4 + 16) = (unsigned int)(v_r14);
    v_r14 = (unsigned int)((v_r14) + (4));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    a1 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int16 *)(v_rsp - 71 + 127));
    *(unsigned int *)(v_r12) = (unsigned int)(result);
    result = memcpy(a1, *(unsigned __int64 *)(v_rsp - 71 - 33), (unsigned int)((unsigned int)(result)), v_rsp - 71 + 79);
    result = 0;
    v_r12 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int16 *)(v_rsp - 71 + 127));
    if ((*(unsigned __int8 *)(v_rsp - 71 + 79)) == 0) goto loc_00AC7DC7;
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 71 - 33), *(unsigned __int64 *)(v_rsp - 71 - 33), (unsigned int)((unsigned int)(result)), v_rsp - 71 + 79);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 33) = 0;
    goto loc_00AC7DC7;
loc_00AC7DC3:
    v_rsi = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
loc_00AC7DC7:
    result = iswspace(*(unsigned __int16 *)(v_rsi), *(unsigned __int64 *)(v_rsp - 71 - 33), (unsigned int)((unsigned int)(result)), v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC7DC3;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 44) goto loc_00AC7DE5;
    v_rsi = (v_rsi) + (2);
    goto loc_00AC7D27;
loc_00AC7DE5:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) == 41) goto loc_00AC7EBB;
loc_00AC7DEF:
    goto loc_00AC762D;
loc_00AC7DF9:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AC7EAD;
    goto loc_00AC7E11;
loc_00AC7E0A:
    v_rsi = (v_rsi) + (2);
loc_00AC7E11:
    result = iswspace(*(unsigned __int16 *)(v_rsi), *(unsigned __int64 *)(v_rsp - 71 - 33), (unsigned int)((unsigned int)(result)), v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC7E0A;
    if ((*(unsigned __int16 *)(v_rsi)) != 34) goto loc_00AC7914;
    a2 = 0;
    goto loc_00AC7E45;
loc_00AC7E32:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi + 2)) == 0) goto loc_00AC7914;
    v_r15 = (v_rsi + 2) + (2);
    a1 = (unsigned int)((0) + 1);
loc_00AC7E45:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) != 34) goto loc_00AC7E32;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)) * 4 + 16) = (unsigned int)(v_r14);
    v_r14 = (unsigned int)((v_r14 + a1 * 2) + (2));
    result = memcpy(v_r12, v_rsi + 2, (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 1, v_rsp - 71 + 79);
    result = 0;
    *(unsigned __int16 *)((unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 1 + v_r12 * 1) = 0;
    v_r12 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int64 *)(v_rsp - 71 - 65));
    goto loc_00AC7E8F;
loc_00AC7E8B:
    v_rsi = (v_r15 + 2) + (2);
loc_00AC7E8F:
    result = iswspace(*(unsigned __int16 *)(v_rsi), v_rsi + 2, (unsigned int)((unsigned int)(a1)) + (unsigned int)((unsigned int)(a1)) * 1, v_rsp - 71 + 79);
    if ((unsigned int)(result) != 0) goto loc_00AC7E8B;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 44) goto loc_00AC7EAD;
    v_rsi = (v_rsi) + (2);
    goto loc_00AC7DF9;
loc_00AC7EAD:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 41) goto loc_00AC7914;
loc_00AC7EBB:
loc_00AC7EBE:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 95)) = *(unsigned __int64 *)(v_rsp - 71 - 65);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 103)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 41)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87)) = v_rsi + 2;
    goto loc_00AC762D;
loc_00AC7EDB:
    a1 = 0;
loc_00AC7EDD:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AC801A;
    *(unsigned int *)(v_rsp - 71 - 53) = 0;
    v_stack_p28 = v_rsp - 71 - 53;
    a4 = 0;
    v_stack_p20 = 1;
    a1 = 0;
    result = wcstoxq(a1, v_rsi, v_rsp - 71 - 49, a4);
    a1 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 71 - 49)) != v_rsi) goto loc_00AC7F1F;
    if (result == 0) goto loc_00AC7DEF;
loc_00AC7F1F:
    if ((*(unsigned int *)(v_rsp - 71 - 53)) != 0) goto loc_00AC8029;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)) * 4 + 16) = (unsigned int)(v_r14);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57))) + 1);
    *(unsigned __int64 *)(v_r12) = result;
    v_r14 = (unsigned int)((v_r14) + (8));
    v_r12 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int64 *)(v_rsp - 71 - 65));
    *(unsigned int *)(v_rsp - 71 - 57) = (unsigned int)(a2);
    result = iswspace(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 49)), a2, v_rsp - 71 - 49, a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AC7F6B;
loc_00AC7F55:
    v_rsi = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rsi), a2, v_rsp - 71 - 49, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7F55;
    a1 = 0;
loc_00AC7F6B:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 44) goto loc_00AC801A;
    v_rsi = (v_rsi) + (2);
    goto loc_00AC7EDD;
loc_00AC7F81:
    a1 = 0;
loc_00AC7F83:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rsi)) == 0) goto loc_00AC801A;
    *(unsigned int *)(v_rsp - 71 - 53) = 0;
    v_stack_p28 = v_rsp - 71 - 53;
    v_stack_p20 = 0;
    a4 = 0;
    a1 = 0;
    result = wcstoxq(a1, v_rsi, v_rsp - 71 - 49, a4);
    a1 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 71 - 49)) != v_rsi) goto loc_00AC7FC1;
    if (result == 0) goto loc_00AC7DEF;
loc_00AC7FC1:
    if ((*(unsigned int *)(v_rsp - 71 - 53)) != 0) goto loc_00AC8029;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 65) + (unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)) * 4 + 16) = (unsigned int)(v_r14);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57))) + 1);
    *(unsigned __int64 *)(v_r12) = result;
    v_r14 = (unsigned int)((v_r14) + (8));
    v_r12 = ((unsigned int)((unsigned int)(v_r14))) + (*(unsigned __int64 *)(v_rsp - 71 - 65));
    *(unsigned int *)(v_rsp - 71 - 57) = (unsigned int)(a2);
    result = iswspace(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 49)), a2, v_rsp - 71 - 49, a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AC8008;
loc_00AC7FF3:
    v_rsi = (*(unsigned __int64 *)(v_rsp - 71 - 49)) + (2);
    result = iswspace(*(unsigned __int16 *)(v_rsi), a2, v_rsp - 71 - 49, a4);
    if ((unsigned int)(result) != 0) goto loc_00AC7FF3;
    a1 = 0;
loc_00AC8008:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 44) goto loc_00AC801A;
    v_rsi = (v_rsi) + (2);
    goto loc_00AC7F83;
loc_00AC801A:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) == 41) goto loc_00AC7EBE;
    goto loc_00AC7DEF;
loc_00AC8029:
    goto loc_00AC762D;
loc_00AC8033:
    goto loc_00AC762D;
loc_00AC803D:
    goto loc_00AC762D;
}
```

## 5. (Beta) C Style

```c
int64_t LocalGetRelativeAttributeForString(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (136);
    local_r14 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = 0;
    *(uint16_t *)(local_rsp - 0x47 + 0x7F) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x25) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x4F) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x87) = 0;
    *(uint8_t *)(local_rsp - 0x47 + 0x77) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = 0;
    if (Arg1 == 0) goto loc_00AC8033;
    if (Arg2 == 0) goto loc_00AC8033;
    if (Arg3 == 0) goto loc_00AC8033;
    if (Arg4 == NULL) goto loc_00AC8033;
    *(uint64_t *)(Arg3) = 0;
    *(uint32_t *)(arg4) = 0;
    if ((*(uint16_t *)(Arg1)) == 40) goto loc_00AC7583;
loc_00AC7579:
    goto loc_00AC764F;
loc_00AC7583:
    result = iswspace(*(uint16_t *)(Arg1 + 0x2), Arg2, Arg3, Arg4);
    goto loc_00AC75A2;
loc_00AC7597:
    local_rdi = (Arg1 + 2) + (2);
    result = iswspace(*(uint16_t *)(local_rdi), Arg2, Arg3, Arg4);
loc_00AC75A2:
    if ((uint32_t)(result) != 0) goto loc_00AC7597;
    if ((*(uint16_t *)(local_rdi)) != 34) goto loc_00AC7579;
    local_rdi = (local_rdi) + (2);
loc_00AC75B2:
    result = IsLegalAttributeChar2(*(uint16_t *)(local_rdi), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AC75D8;
    if ((uint16_t)(*(uint16_t *)(local_rdi)) == 0) goto loc_00AC7579;
    local_rbx = (local_rdi) + (2);
    if (((uint32_t)(0 + 1)) < 0) goto loc_00AC75D1;
    goto loc_00AC75B2;
loc_00AC75D1:
    goto loc_00AC764F;
loc_00AC75D8:
    if (((uint16_t)(*(uint16_t *)(local_rdi))) != 34) goto loc_00AC7579;
    if ((uint32_t)((uint32_t)((uint32_t)(0 + 1))) == 0) goto loc_00AC7579;
    local_rbx = (local_rbx) + (2);
    result = DecodeAttributeName(534, (uint32_t)((uint32_t)(0 + 1)) + (uint32_t)((uint32_t)(0 + 1)) * 1, local_rsp - 71 - 25, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC762D;
    result = (result) | (-1);
loc_00AC7602:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x19) + result * 2)) != 0) goto loc_00AC7602;
    result = (uint32_t)((result) + 1);
    *(uint64_t *)(local_rsp - 0x47 - 0x9) = result;
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint32_t *)(local_rsp - 0x47 - 0x11) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x47 + 0x6F) = (uint32_t)(result + 20);
    if (((uint32_t)(result + 20)) >= 20) goto loc_00AC7669;
loc_00AC762A:
loc_00AC762D:
    result = *(uint64_t *)(local_rsp - 0x47 - 0x19);
    if (*(uint64_t *)(local_rsp - 0x47 - 0x19) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x19);
        result = PdcCloseEvent(Arg1, (uint32_t)((uint32_t)(0 + 1)) + (uint32_t)((uint32_t)(0 + 1)) * 1, local_rsp - 71 - 25, Arg4);
    }
    if (534 == 0) goto loc_00AC764F;
    if (0 != 0) {
        Arg1 = 0;
        result = PdcCloseEvent(Arg1, (uint32_t)((uint32_t)(0 + 1)) + (uint32_t)((uint32_t)(0 + 1)) * 1, local_rsp - 71 - 25, Arg4);
    }
    local_rsp = (local_rsp) + (136);
    return 534;
loc_00AC7666:
    local_rbx = (local_rbx) + (2);
loc_00AC7669:
    result = iswspace(*(uint16_t *)(local_rbx), (uint32_t)((uint32_t)(0 + 1)) + (uint32_t)((uint32_t)(0 + 1)) * 1, local_rsp - 71 - 25, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7666;
    if ((*(uint16_t *)(local_rbx)) == 44) goto loc_00AC7682;
loc_00AC767B:
    goto loc_00AC762A;
loc_00AC7682:
    local_rbx = (local_rbx) + (2);
    result = iswspace(*(uint16_t *)(local_rbx), (uint32_t)((uint32_t)(0 + 1)) + (uint32_t)((uint32_t)(0 + 1)) * 1, local_rsp - 71 - 25, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7682;
    result = GetValueType(local_rbx, local_rsp - 71 - 49, local_rsp - 71 + 127, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC762A;
    goto loc_00AC76B0;
loc_00AC76AD:
    local_rbx = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
loc_00AC76B0:
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 - 49, local_rsp - 71 + 127, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC76AD;
    if ((*(uint16_t *)(local_rbx)) != 44) goto loc_00AC767B;
loc_00AC76C2:
    local_rbx = (local_rbx) + (2);
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 - 49, local_rsp - 71 + 127, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC76C2;
    result = GetFlags(local_rbx, local_rsp - 71 - 49, local_rsp - 71 - 37, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC762A;
    if (((*(uint32_t *)(local_rsp - 0x47 - 0x25)) & (0xFFC0ULL)) == 0) goto loc_00AC76FD;
    goto loc_00AC767B;
loc_00AC76FA:
    local_rsi = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
loc_00AC76FD:
    result = iswspace(*(uint16_t *)(local_rsi), local_rsp - 71 - 49, local_rsp - 71 - 37, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC76FA;
    if ((*(uint16_t *)(local_rsi)) != 44) goto loc_00AC767B;
    local_rsi = (local_rsi) + (2);
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsp - 0x47 + 0x7F)) - (1));
    if (condition_is_equal) goto loc_00AC7AD1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AC7A00;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AC791E;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AC7854;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AC7A00;
    if (((uint32_t)(Arg1)) != 10) goto loc_00AC767B;
loc_00AC7753:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_00AC77EF;
    goto loc_00AC7770;
loc_00AC7769:
    local_rbx = (local_rsi) + (2);
loc_00AC7770:
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 - 49, local_rsp - 71 - 37, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7769;
loc_00AC777C:
    result = GetDigitFromChar((uint16_t)(*(uint16_t *)(local_rbx)), local_rsp - 71 + 111, 0 + 1, 0);
    if ((uint8_t)(result) == 0) goto loc_00AC77A7;
    local_rbx = (local_rbx) + (2);
    if (((uint32_t)(0 + 1)) < 0) goto loc_00AC7B71;
    goto loc_00AC777C;
loc_00AC77A7:
    Arg3 = (uint32_t)((0 + 1) >> (1));
    local_r12 = (uint32_t)((0) + 1);
    if (((uint32_t)(Arg3 + 0 * 1)) < 0) goto loc_00AC7B71;
    if (((uint32_t)(Arg3 + 0 * 1 + 4)) < ((uint32_t)(Arg3 + 0 * 1))) goto loc_00AC7B71;
    goto loc_00AC77D4;
loc_00AC77CD:
    local_rbx = (local_rbx) + (2);
loc_00AC77D4:
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 + 111, Arg3, (uint32_t)((uint32_t)(0 + 1)));
    if ((uint32_t)(result) != 0) goto loc_00AC77CD;
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 44) goto loc_00AC77EF;
    local_rbx = (local_rbx) + (2);
    goto loc_00AC7753;
loc_00AC77EF:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 41) goto loc_00AC7B3F;
loc_00AC77F9:
loc_00AC77FF:
    Arg1 = (local_r12 - 1) << (2);
    if (Arg1 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00AC7AC3;
    if (((uint32_t)(Arg1 + Arg3 + 0 * 1 + 4 * 1)) < ((uint32_t)(Arg3 + 0 * 1 + 4))) goto loc_00AC7AC3;
    local_rbx = Arg1 + Arg3 + 0 * 1 + 4 * 1 + 3;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(Arg1 + Arg3 + 0 * 1 + 4 * 1 + 3)) < ((uint32_t)(Arg1 + Arg3 + 0 * 1 + 4 * 1))) {
        local_rbx = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
        local_rdi = 534;
    }
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFCULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x29) = (uint32_t)(local_rbx);
    result = SddlpAlloc((uint32_t)((uint32_t)(local_rbx)), local_rsp - 71 + 111, (uint32_t)(0xFFFFFFFFULL), (uint32_t)((uint32_t)(0 + 1)));
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x41) = result;
    if (result != 0) goto loc_00AC7B78;
    goto loc_00AC762D;
loc_00AC7854:
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_00AC790A;
    goto loc_00AC7871;
loc_00AC786A:
    local_rbx = (local_rbx) + (2);
loc_00AC7871:
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 + 111, (uint32_t)(0xFFFFFFFFULL), (uint32_t)((uint32_t)(0 + 1)));
    if ((uint32_t)(result) != 0) goto loc_00AC786A;
    result = LocalGetSidForString(local_rbx, local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC7AC8;
    result = 0;
    if (*(uint64_t *)(local_rsp - 0x47 - 0x21) == 0) goto loc_00AC803D;
    local_r12 = (uint32_t)((local_r12) + 1);
    result = RtlLengthSid(*(uint64_t *)(local_rsp - 0x47 - 0x21), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if (((uint32_t)(result + result * 1)) < ((uint32_t)(result))) goto loc_00AC7AC3;
    if (((uint32_t)(result + result * 1 + 4)) < ((uint32_t)(result + result * 1))) goto loc_00AC7AC3;
    result = 0;
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x4F)) == 0) goto loc_00AC78EC;
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x47 - 0x21), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    local_r14 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = 0;
    goto loc_00AC78EC;
loc_00AC78E8:
    local_rbx = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
loc_00AC78EC:
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC78E8;
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 44) goto loc_00AC790A;
    local_rbx = (local_rbx) + (2);
    goto loc_00AC7854;
loc_00AC790A:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) == 41) goto loc_00AC77F9;
loc_00AC7914:
    goto loc_00AC7AC8;
loc_00AC791E:
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_00AC79CC;
    result = iswspace((uint16_t)(*(uint16_t *)(local_rbx)), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if ((uint32_t)(result) == 0) goto loc_00AC794F;
loc_00AC793B:
    local_rbx = (local_rbx) + (2);
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC793B;
loc_00AC794F:
    if ((*(uint16_t *)(local_rbx)) != 34) goto loc_00AC7914;
    local_rbx = (local_rbx) + (2);
loc_00AC7959:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) == 34) goto loc_00AC797D;
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_00AC797D;
    local_rbx = (local_rbx) + (2);
    if (((uint32_t)(local_r14 + 1)) < 0) goto loc_00AC7AC3;
    goto loc_00AC7959;
loc_00AC797D:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14 + 1)) + 1)) < ((uint32_t)((uint32_t)((uint32_t)(local_r14 + 1))))) goto loc_00AC7AC3;
    if (((uint16_t)(local_r14 + 1)) != 34) goto loc_00AC7914;
    local_rbx = (local_rbx) + (2);
    local_r12 = (uint32_t)((local_r12) + 1);
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if ((uint32_t)(result) == 0) goto loc_00AC79BA;
loc_00AC79A6:
    local_rbx = (local_rbx) + (2);
    result = iswspace(*(uint16_t *)(local_rbx), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC79A6;
loc_00AC79BA:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 44) goto loc_00AC79CC;
    local_rbx = (local_rbx) + (2);
    goto loc_00AC791E;
loc_00AC79CC:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 41) goto loc_00AC7914;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14 + 1)) + 1))))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14 + 1)) + 1)))));
loc_00AC79DC:
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00AC7AC3;
    if (((uint32_t)(result + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)) * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F))))) goto loc_00AC7AC3;
loc_00AC79F8:
    goto loc_00AC77FF;
loc_00AC7A00:
    Arg1 = 0;
loc_00AC7A07:
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_00AC7AAD;
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = 0;
    v_stack_p28 = local_rsp - 71 - 53;
    Arg4 = 0;
    v_stack_p20 = 1;
    Arg1 = 0;
    result = wcstoxq(Arg1, local_rbx, local_rsp - 71 - 49, Arg4);
    Arg2 = 0;
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x31)) != local_rbx) goto loc_00AC7A4D;
    if (result == 0) goto loc_00AC7AA0;
loc_00AC7A4D:
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x35)) != 0) goto loc_00AC7AC3;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x47 + 0x7F))) != 6) goto loc_00AC7A63;
    if (result > 1) goto loc_00AC7914;
loc_00AC7A63:
    local_r12 = (uint32_t)((local_r12) + 1);
    result = iswspace(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31)), Arg2, local_rsp - 71 - 49, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AC7A8E;
loc_00AC7A77:
    local_rbx = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
    result = iswspace(*(uint16_t *)(local_rbx), Arg2, local_rsp - 71 - 49, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7A77;
    Arg1 = 0;
loc_00AC7A8E:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 44) goto loc_00AC7AAD;
    local_rbx = (local_rbx) + (2);
    goto loc_00AC7A07;
loc_00AC7AA0:
    goto loc_00AC762D;
loc_00AC7AAD:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 41) goto loc_00AC7914;
    result = ((uint32_t)((uint32_t)(local_r12))) << (3);
    goto loc_00AC79DC;
loc_00AC7AC3:
loc_00AC7AC8:
    goto loc_00AC762D;
loc_00AC7AD1:
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_00AC7B4C;
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = (uint32_t)(*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    v_stack_p28 = local_rsp - 71 - 53;
    Arg4 = 0;
    v_stack_p20 = (uint32_t)(*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    Arg1 = 0;
    result = wcstoxq(Arg1, local_rbx, local_rsp - 71 - 49, Arg4);
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x31)) != local_rbx) goto loc_00AC7B0F;
    if (result == 0) goto loc_00AC7B3F;
loc_00AC7B0F:
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x35)) != ((uint32_t)(*(uint16_t *)(local_rsp - 0x47 + 0x7F)))) goto loc_00AC7B71;
    local_r12 = (uint32_t)((local_r12) + 1);
    goto loc_00AC7B27;
loc_00AC7B20:
    local_rbx = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
loc_00AC7B27:
    result = iswspace(*(uint16_t *)(local_rbx), local_rbx, local_rsp - 71 - 49, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7B20;
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 44) goto loc_00AC7B4C;
    local_rbx = (local_rbx) + (2);
    goto loc_00AC7AD1;
loc_00AC7B3F:
loc_00AC7B44:
    goto loc_00AC762D;
loc_00AC7B4C:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) != 41) goto loc_00AC7B3F;
    result = ((uint32_t)((uint32_t)(local_r12))) << (3);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00AC7B71;
    if (((uint32_t)(result + *(uint16_t *)(local_rsp - 0x47 + 0x7F) * 1)) >= ((uint32_t)(*(uint16_t *)(local_rsp - 0x47 + 0x7F)))) goto loc_00AC79F8;
loc_00AC7B71:
    goto loc_00AC7B44;
loc_00AC7B78:
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x9))) + ((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x9)));
    *(uint16_t *)(*(uint16_t *)(local_rsp - 0x47 + 0x7F) + 0x6) = (uint16_t)(result + *(uint16_t *)(local_rsp - 0x47 + 0x7F) * 1);
    *(uint16_t *)(*(uint16_t *)(local_rsp - 0x47 + 0x7F) + 0x4) = (uint16_t)(*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    Arg1 = ((uint32_t)((uint32_t)(local_r12 * 4 + 16))) + (*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    *(uint32_t *)(*(uint16_t *)(local_rsp - 0x47 + 0x7F)) = (uint32_t)(local_r12 * 4 + 16);
    local_r14 = (uint32_t)((local_r12 * 4 + 16) + (*(uint32_t *)(local_rsp - 0x47 - 0x11)));
    *(uint32_t *)(*(uint16_t *)(local_rsp - 0x47 + 0x7F) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x25)));
    *(uint32_t *)(*(uint16_t *)(local_rsp - 0x47 + 0x7F) + 0xC) = (uint32_t)(local_r12);
    result = memcpy(Arg1, *(uint64_t *)(local_rsp - 0x47 - 0x19), Arg3, Arg4);
    local_r12 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsp - 0x47 + 0x7F)) - (1));
    if (condition_is_equal) goto loc_00AC7F81;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AC7EDB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AC7DF9;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AC7D27;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AC7EDB;
    if (((uint32_t)(Arg1)) != 10) goto loc_00AC7DEF;
loc_00AC7BF6:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_00AC801A;
    result = iswspace((uint16_t)(*(uint16_t *)(local_rsi)), *(uint64_t *)(local_rsp - 0x47 - 0x19), Arg3, Arg4);
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AC7C27;
loc_00AC7C11:
    local_rsi = (local_rsi) + (2);
    result = iswspace(*(uint16_t *)(local_rsi), *(uint64_t *)(local_rsp - 0x47 - 0x19), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7C11;
    local_r10 = 0;
loc_00AC7C27:
    goto loc_00AC7C3D;
loc_00AC7C32:
    Arg4 = (local_rsi) + (2);
    Arg3 = (uint32_t)((0) + 1);
loc_00AC7C3D:
    result = GetDigitFromChar(*(uint16_t *)(arg4), local_rsp - 71 + 111, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AC7C32;
    *(uint32_t *)(*(uint16_t *)(local_rsp - 0x47 + 0x7F) + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)) * 4 + 0x10) = (uint32_t)(local_r14);
    result = (uint32_t)((Arg3 + 1) >> (1));
    local_r14 = (uint32_t)((local_r14) + (4));
    *(uint32_t *)(local_r12) = (uint32_t)(result);
    local_r10 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
loc_00AC7C71:
    if ((Arg4 - 2) <= local_rsi) goto loc_00AC7CC2;
    result = GetDigitFromChar(*(uint16_t *)(arg4 - 0x2), local_rsp - 71 + 135, Arg4 - 2, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AC7DEF;
    result = GetDigitFromChar(*(uint16_t *)(arg4 - 0x2 - 0x2), local_rsp - 71 + 119, Arg4 - 2, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AC7DEF;
    Arg3 = (Arg4 - 2) - (4);
    Arg1 = (uint8_t)((*(uint8_t *)(local_rsp - 0x47 + 0x77)) << (4));
    Arg1 = (uint8_t)((Arg1) | (*(uint8_t *)(local_rsp - 0x47 + 0x87)));
    *(uint8_t *)(result - 0x1 + local_r10 * 1) = (uint8_t)(Arg1);
    local_r11 = (uint32_t)((result - 1) + ((uint32_t)((uint32_t)(0xFFFFFFFFULL))));
    goto loc_00AC7C71;
loc_00AC7CC2:
    if (condition_is_not_equal) goto loc_00AC7CE5;
    result = GetDigitFromChar(*(uint16_t *)(Arg3), local_rsp - 71 + 135, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AC7DEF;
    *(uint8_t *)(local_r10) = (uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x87));
loc_00AC7CE5:
    local_r12 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    result = iswspace(*(uint16_t *)(arg4), local_rsp - 71 + 135, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AC7D11;
loc_00AC7CFE:
    local_rsi = (Arg4) + (2);
    result = iswspace(*(uint16_t *)(local_rsi), local_rsp - 71 + 135, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7CFE;
loc_00AC7D11:
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 44) goto loc_00AC801A;
    local_rsi = (local_rsi) + (2);
    goto loc_00AC7BF6;
loc_00AC7D27:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_00AC7DE5;
    goto loc_00AC7D3F;
loc_00AC7D38:
    local_rsi = (local_rsi) + (2);
loc_00AC7D3F:
    result = iswspace(*(uint16_t *)(local_rsi), local_rsp - 71 + 135, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7D38;
    result = LocalGetSidForString(local_rsi, local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC762D;
    if (*(uint64_t *)(local_rsp - 0x47 - 0x21) == 0) goto loc_00AC762D;
    result = RtlLengthSid(*(uint64_t *)(local_rsp - 0x47 - 0x21), local_rsp - 71 - 33, local_rsp - 71 - 49, local_rsp - 71 + 79);
    *(uint32_t *)(*(uint16_t *)(local_rsp - 0x47 + 0x7F) + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)) * 4 + 0x10) = (uint32_t)(local_r14);
    local_r14 = (uint32_t)((local_r14) + (4));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    Arg1 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    *(uint32_t *)(local_r12) = (uint32_t)(result);
    result = memcpy(Arg1, *(uint64_t *)(local_rsp - 0x47 - 0x21), (uint32_t)((uint32_t)(result)), local_rsp - 71 + 79);
    result = 0;
    local_r12 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint16_t *)(local_rsp - 0x47 + 0x7F));
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x4F)) == 0) goto loc_00AC7DC7;
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x47 - 0x21), *(uint64_t *)(local_rsp - 0x47 - 0x21), (uint32_t)((uint32_t)(result)), local_rsp - 71 + 79);
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = 0;
    goto loc_00AC7DC7;
loc_00AC7DC3:
    local_rsi = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
loc_00AC7DC7:
    result = iswspace(*(uint16_t *)(local_rsi), *(uint64_t *)(local_rsp - 0x47 - 0x21), (uint32_t)((uint32_t)(result)), local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC7DC3;
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 44) goto loc_00AC7DE5;
    local_rsi = (local_rsi) + (2);
    goto loc_00AC7D27;
loc_00AC7DE5:
    if (((uint16_t)(*(uint16_t *)(local_rsi))) == 41) goto loc_00AC7EBB;
loc_00AC7DEF:
    goto loc_00AC762D;
loc_00AC7DF9:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_00AC7EAD;
    goto loc_00AC7E11;
loc_00AC7E0A:
    local_rsi = (local_rsi) + (2);
loc_00AC7E11:
    result = iswspace(*(uint16_t *)(local_rsi), *(uint64_t *)(local_rsp - 0x47 - 0x21), (uint32_t)((uint32_t)(result)), local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC7E0A;
    if ((*(uint16_t *)(local_rsi)) != 34) goto loc_00AC7914;
    Arg2 = 0;
    goto loc_00AC7E45;
loc_00AC7E32:
    if ((uint16_t)(*(uint16_t *)(local_rsi + 0x2)) == 0) goto loc_00AC7914;
    local_r15 = (local_rsi + 2) + (2);
    Arg1 = (uint32_t)((0) + 1);
loc_00AC7E45:
    if (((uint16_t)(*(uint16_t *)(local_r15))) != 34) goto loc_00AC7E32;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)) * 4 + 0x10) = (uint32_t)(local_r14);
    local_r14 = (uint32_t)((local_r14 + Arg1 * 2) + (2));
    result = memcpy(local_r12, local_rsi + 2, (uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 1, local_rsp - 71 + 79);
    result = 0;
    *(uint16_t *)((uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 1 + local_r12 * 1) = 0;
    local_r12 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint64_t *)(local_rsp - 0x47 - 0x41));
    goto loc_00AC7E8F;
loc_00AC7E8B:
    local_rsi = (local_r15 + 2) + (2);
loc_00AC7E8F:
    result = iswspace(*(uint16_t *)(local_rsi), local_rsi + 2, (uint32_t)((uint32_t)(Arg1)) + (uint32_t)((uint32_t)(Arg1)) * 1, local_rsp - 71 + 79);
    if ((uint32_t)(result) != 0) goto loc_00AC7E8B;
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 44) goto loc_00AC7EAD;
    local_rsi = (local_rsi) + (2);
    goto loc_00AC7DF9;
loc_00AC7EAD:
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 41) goto loc_00AC7914;
loc_00AC7EBB:
loc_00AC7EBE:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x5F)) = *(uint64_t *)(local_rsp - 0x47 - 0x41);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x67)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x29)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57)) = local_rsi + 2;
    goto loc_00AC762D;
loc_00AC7EDB:
    Arg1 = 0;
loc_00AC7EDD:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_00AC801A;
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = 0;
    v_stack_p28 = local_rsp - 71 - 53;
    Arg4 = 0;
    v_stack_p20 = 1;
    Arg1 = 0;
    result = wcstoxq(Arg1, local_rsi, local_rsp - 71 - 49, Arg4);
    Arg1 = 0;
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x31)) != local_rsi) goto loc_00AC7F1F;
    if (result == 0) goto loc_00AC7DEF;
loc_00AC7F1F:
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x35)) != 0) goto loc_00AC8029;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)) * 4 + 0x10) = (uint32_t)(local_r14);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39))) + 1);
    *(uint64_t *)(local_r12) = result;
    local_r14 = (uint32_t)((local_r14) + (8));
    local_r12 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint64_t *)(local_rsp - 0x47 - 0x41));
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = (uint32_t)(Arg2);
    result = iswspace(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31)), Arg2, local_rsp - 71 - 49, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AC7F6B;
loc_00AC7F55:
    local_rsi = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
    result = iswspace(*(uint16_t *)(local_rsi), Arg2, local_rsp - 71 - 49, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7F55;
    Arg1 = 0;
loc_00AC7F6B:
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 44) goto loc_00AC801A;
    local_rsi = (local_rsi) + (2);
    goto loc_00AC7EDD;
loc_00AC7F81:
    Arg1 = 0;
loc_00AC7F83:
    if ((uint16_t)(*(uint16_t *)(local_rsi)) == 0) goto loc_00AC801A;
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = 0;
    v_stack_p28 = local_rsp - 71 - 53;
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg1 = 0;
    result = wcstoxq(Arg1, local_rsi, local_rsp - 71 - 49, Arg4);
    Arg1 = 0;
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x31)) != local_rsi) goto loc_00AC7FC1;
    if (result == 0) goto loc_00AC7DEF;
loc_00AC7FC1:
    if ((*(uint32_t *)(local_rsp - 0x47 - 0x35)) != 0) goto loc_00AC8029;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x41) + (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)) * 4 + 0x10) = (uint32_t)(local_r14);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39))) + 1);
    *(uint64_t *)(local_r12) = result;
    local_r14 = (uint32_t)((local_r14) + (8));
    local_r12 = ((uint32_t)((uint32_t)(local_r14))) + (*(uint64_t *)(local_rsp - 0x47 - 0x41));
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = (uint32_t)(Arg2);
    result = iswspace(*(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31)), Arg2, local_rsp - 71 - 49, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AC8008;
loc_00AC7FF3:
    local_rsi = (*(uint64_t *)(local_rsp - 0x47 - 0x31)) + (2);
    result = iswspace(*(uint16_t *)(local_rsi), Arg2, local_rsp - 71 - 49, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AC7FF3;
    Arg1 = 0;
loc_00AC8008:
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 44) goto loc_00AC801A;
    local_rsi = (local_rsi) + (2);
    goto loc_00AC7F83;
loc_00AC801A:
    if (((uint16_t)(*(uint16_t *)(local_rsi))) == 41) goto loc_00AC7EBE;
    goto loc_00AC7DEF;
loc_00AC8029:
    goto loc_00AC762D;
loc_00AC8033:
    goto loc_00AC762D;
loc_00AC803D:
    goto loc_00AC762D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC74E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
