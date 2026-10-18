# DifZwDeleteFileWrapper

- RVA: `0x00640BF0`–`0x00640D4D` (길이 `349` bytes)
- VA: `0x0000000140640BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00640C1D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00640C45` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00640C73` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00640C9A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00640CB3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00640CBB` → [ZwDeleteFile](../6A/ZwDeleteFile_function_006AEC30.md) (function, `0x006AEC30`)
- `0x00640CE8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00640D0F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00640D28` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00640C57` → RVA `0x00F048B8` (`.data`; read)
- `0x00640C60` → RVA `0x00F04980` (`.data`; read)
- `0x00640C6C` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00640BF0  4C 8B DC                        mov r11, rsp
00640BF3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00640BF7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00640BFB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00640BFF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00640C03  41 56                           push r14
00640C05  48 83 EC 40                     sub rsp, 0x40
00640C09  33 C0                           xor eax, eax
00640C0B  0F 57 C0                        xorps xmm0, xmm0
00640C0E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00640C13  48 8B E9                        mov rbp, rcx
00640C16  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00640C1A  8D 48 71                        lea ecx, [rax + 0x71]
00640C1D  E8 12 4E E5 FF                  call 0x140495a34
00640C22  48 8B F0                        mov rsi, rax
00640C25  48 85 C0                        test rax, rax
00640C28  0F 84 8A 00 00 00               je 0x140640cb8
00640C2E  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00640C31  A8 18                           test al, 0x18
00640C33  74 0C                           je 0x140640c41
00640C35  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00640C3A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00640C3F  EB 0E                           jmp 0x140640c4f
00640C41  A8 04                           test al, 4
00640C43  74 0A                           je 0x140640c4f
00640C45  E8 BE 2F E9 FF                  call 0x1404d3c08
00640C4A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00640C4F  40 32 FF                        xor dil, dil
00640C52  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00640C57  40 38 3D 5A 3C 8C 00            cmp byte ptr [rip + 0x8c3c5a], dil
00640C5E  75 0C                           jne 0x140640c6c
00640C60  F7 05 16 3D 8C 00 00 08 00 00   test dword ptr [rip + 0x8c3d16], 0x800
00640C6A  74 13                           je 0x140640c7f
00640C6C  48 8D 0D 0D 32 8C 00            lea rcx, [rip + 0x8c320d]
00640C73  E8 A8 59 BD FF                  call 0x140216620
00640C78  40 8A F8                        mov dil, al
00640C7B  84 C0                           test al, al
00640C7D  74 39                           je 0x140640cb8
00640C7F  4C 8D 76 20                     lea r14, [rsi + 0x20]
00640C83  49 8B 1E                        mov rbx, qword ptr [r14]
00640C86  EB 1A                           jmp 0x140640ca2
00640C88  48 8D 43 F0                     lea rax, [rbx - 0x10]
00640C8C  48 85 C0                        test rax, rax
00640C8F  74 0E                           je 0x140640c9f
00640C91  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00640C95  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00640C9A  E8 31 9E 07 00                  call 0x1406baad0
00640C9F  48 8B 1B                        mov rbx, qword ptr [rbx]
00640CA2  49 3B DE                        cmp rbx, r14
00640CA5  75 E1                           jne 0x140640c88
00640CA7  40 84 FF                        test dil, dil
00640CAA  74 0C                           je 0x140640cb8
00640CAC  48 8D 0D CD 31 8C 00            lea rcx, [rip + 0x8c31cd]
00640CB3  E8 C8 91 D0 FF                  call 0x140349e80
00640CB8  48 8B CD                        mov rcx, rbp
00640CBB  E8 70 DF 06 00                  call 0x1406aec30
00640CC0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00640CC4  48 85 F6                        test rsi, rsi
00640CC7  74 64                           je 0x140640d2d
00640CC9  40 32 FF                        xor dil, dil
00640CCC  40 38 3D E5 3B 8C 00            cmp byte ptr [rip + 0x8c3be5], dil
00640CD3  75 0C                           jne 0x140640ce1
00640CD5  F7 05 A1 3C 8C 00 00 08 00 00   test dword ptr [rip + 0x8c3ca1], 0x800
00640CDF  74 13                           je 0x140640cf4
00640CE1  48 8D 0D 98 31 8C 00            lea rcx, [rip + 0x8c3198]
00640CE8  E8 33 59 BD FF                  call 0x140216620
00640CED  40 8A F8                        mov dil, al
00640CF0  84 C0                           test al, al
00640CF2  74 39                           je 0x140640d2d
00640CF4  48 83 C6 30                     add rsi, 0x30
00640CF8  48 8B 1E                        mov rbx, qword ptr [rsi]
00640CFB  EB 1A                           jmp 0x140640d17
00640CFD  48 8D 43 F0                     lea rax, [rbx - 0x10]
00640D01  48 85 C0                        test rax, rax
00640D04  74 0E                           je 0x140640d14
00640D06  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00640D0A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00640D0F  E8 BC 9D 07 00                  call 0x1406baad0
00640D14  48 8B 1B                        mov rbx, qword ptr [rbx]
00640D17  48 3B DE                        cmp rbx, rsi
00640D1A  75 E1                           jne 0x140640cfd
00640D1C  40 84 FF                        test dil, dil
00640D1F  74 0C                           je 0x140640d2d
00640D21  48 8D 0D 58 31 8C 00            lea rcx, [rip + 0x8c3158]
00640D28  E8 53 91 D0 FF                  call 0x140349e80
00640D2D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00640D31  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00640D36  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00640D3B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00640D40  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00640D45  48 83 C4 40                     add rsp, 0x40
00640D49  41 5E                           pop r14
00640D4B  C3                              ret
00640D4C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwDeleteFileWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(result + 113, a2, a3, a4);
    if (result == 0) goto loc_00640CB8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00640C41;
    v_stack_m28 = v_stack_p0;
    goto loc_00640C4F;
loc_00640C41:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9190490)) != 0) goto loc_00640C6C;
    if (((*(unsigned int *)(v_rip + 9190678)) & (0x800ULL)) == 0) goto loc_00640C7F;
loc_00640C6C:
    result = ExAcquireRundownProtection(v_rip + 9187853, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00640CB8;
loc_00640C7F:
    goto loc_00640CA2;
loc_00640C88:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00640CA2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00640C88;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9187789;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwDeleteFile(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_00640D2D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9190373)) != 0) goto loc_00640CE1;
    if (((*(unsigned int *)(v_rip + 9190561)) & (0x800ULL)) == 0) goto loc_00640CF4;
loc_00640CE1:
    result = ExAcquireRundownProtection(v_rip + 9187736, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00640D2D;
loc_00640CF4:
    v_rsi = (result) + (48);
    goto loc_00640D17;
loc_00640CFD:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00640D17:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00640CFD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9187672;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwDeleteFileWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(result + 113, a2, a3, a4);
    if (result == 0) goto loc_00640CB8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00640C41;
    v_stack_m28 = v_stack_p0;
    goto loc_00640C4F;
loc_00640C41:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C3C5A)) != 0) goto loc_00640C6C;
    if (((*(uint32_t *)(v_rip + 0x8C3D16)) & (0x800ULL)) == 0) goto loc_00640C7F;
loc_00640C6C:
    result = ExAcquireRundownProtection(v_rip + 9187853, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00640CB8;
loc_00640C7F:
    goto loc_00640CA2;
loc_00640C88:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00640CA2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00640C88;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9187789;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwDeleteFile(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_00640D2D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C3BE5)) != 0) goto loc_00640CE1;
    if (((*(uint32_t *)(v_rip + 0x8C3CA1)) & (0x800ULL)) == 0) goto loc_00640CF4;
loc_00640CE1:
    result = ExAcquireRundownProtection(v_rip + 9187736, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00640D2D;
loc_00640CF4:
    local_rsi = (result) + (48);
    goto loc_00640D17;
loc_00640CFD:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00640D17:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00640CFD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9187672;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00640BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00640BF0[BB_00640BF0]
  bb_00640C2E[BB_00640C2E]
  bb_00640C35[BB_00640C35]
  bb_00640C41[BB_00640C41]
  bb_00640C45[BB_00640C45]
  bb_00640C4F[BB_00640C4F]
  bb_00640C60[BB_00640C60]
  bb_00640C6C[BB_00640C6C]
  bb_00640C7F[BB_00640C7F]
  bb_00640C88[BB_00640C88]
  bb_00640C91[BB_00640C91]
  bb_00640C9F[BB_00640C9F]
  bb_00640CA2[BB_00640CA2]
  bb_00640CA7[BB_00640CA7]
  bb_00640CAC[BB_00640CAC]
  bb_00640CB8[BB_00640CB8]
  bb_00640CC9[BB_00640CC9]
  bb_00640CD5[BB_00640CD5]
  bb_00640CE1[BB_00640CE1]
  bb_00640CF4[BB_00640CF4]
  bb_00640CFD[BB_00640CFD]
  bb_00640D06[BB_00640D06]
  bb_00640D14[BB_00640D14]
  bb_00640D17[BB_00640D17]
  bb_00640D1C[BB_00640D1C]
  bb_00640D21[BB_00640D21]
  bb_00640D2D[BB_00640D2D]
  bb_00640D4C[BB_00640D4C]
  bb_00640BF0 -->|branch| bb_00640CB8
  bb_00640BF0 -->|fallthrough| bb_00640C2E
  bb_00640C2E -->|branch| bb_00640C41
  bb_00640C2E -->|fallthrough| bb_00640C35
  bb_00640C35 -->|branch| bb_00640C4F
  bb_00640C41 -->|branch| bb_00640C4F
  bb_00640C41 -->|fallthrough| bb_00640C45
  bb_00640C45 -->|flow| bb_00640C4F
  bb_00640C4F -->|branch| bb_00640C6C
  bb_00640C4F -->|fallthrough| bb_00640C60
  bb_00640C60 -->|branch| bb_00640C7F
  bb_00640C60 -->|fallthrough| bb_00640C6C
  bb_00640C6C -->|branch| bb_00640CB8
  bb_00640C6C -->|fallthrough| bb_00640C7F
  bb_00640C7F -->|branch| bb_00640CA2
  bb_00640C88 -->|branch| bb_00640C9F
  bb_00640C88 -->|fallthrough| bb_00640C91
  bb_00640C91 -->|flow| bb_00640C9F
  bb_00640C9F -->|flow| bb_00640CA2
  bb_00640CA2 -->|branch| bb_00640C88
  bb_00640CA2 -->|fallthrough| bb_00640CA7
  bb_00640CA7 -->|branch| bb_00640CB8
  bb_00640CA7 -->|fallthrough| bb_00640CAC
  bb_00640CAC -->|flow| bb_00640CB8
  bb_00640CB8 -->|branch| bb_00640D2D
  bb_00640CB8 -->|fallthrough| bb_00640CC9
  bb_00640CC9 -->|branch| bb_00640CE1
  bb_00640CC9 -->|fallthrough| bb_00640CD5
  bb_00640CD5 -->|branch| bb_00640CF4
  bb_00640CD5 -->|fallthrough| bb_00640CE1
  bb_00640CE1 -->|branch| bb_00640D2D
  bb_00640CE1 -->|fallthrough| bb_00640CF4
  bb_00640CF4 -->|branch| bb_00640D17
  bb_00640CFD -->|branch| bb_00640D14
  bb_00640CFD -->|fallthrough| bb_00640D06
  bb_00640D06 -->|flow| bb_00640D14
  bb_00640D14 -->|flow| bb_00640D17
  bb_00640D17 -->|branch| bb_00640CFD
  bb_00640D17 -->|fallthrough| bb_00640D1C
  bb_00640D1C -->|branch| bb_00640D2D
  bb_00640D1C -->|fallthrough| bb_00640D21
  bb_00640D21 -->|flow| bb_00640D2D
```
