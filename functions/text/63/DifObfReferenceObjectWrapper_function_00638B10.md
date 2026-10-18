# DifObfReferenceObjectWrapper

- RVA: `0x00638B10`–`0x00638C76` (길이 `358` bytes)
- VA: `0x0000000140638B10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `95`개 명령, `358/358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00638B3F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00638B67` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00638B95` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00638BBC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638BD5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00638BE2` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00638C10` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00638C37` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638C50` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00638B79` → RVA `0x00F048B8` (`.data`; read)
- `0x00638B82` → RVA `0x00F04980` (`.data`; read)
- `0x00638B8E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00638B10  4C 8B DC                        mov r11, rsp
00638B13  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00638B17  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00638B1B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00638B1F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00638B23  41 56                           push r14
00638B25  48 83 EC 40                     sub rsp, 0x40
00638B29  33 C0                           xor eax, eax
00638B2B  0F 57 C0                        xorps xmm0, xmm0
00638B2E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00638B33  48 8B E9                        mov rbp, rcx
00638B36  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00638B3A  B9 C4 00 00 00                  mov ecx, 0xc4
00638B3F  E8 F0 CE E5 FF                  call 0x140495a34
00638B44  48 8B F0                        mov rsi, rax
00638B47  48 85 C0                        test rax, rax
00638B4A  0F 84 8A 00 00 00               je 0x140638bda
00638B50  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00638B53  A8 18                           test al, 0x18
00638B55  74 0C                           je 0x140638b63
00638B57  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00638B5C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00638B61  EB 0E                           jmp 0x140638b71
00638B63  A8 04                           test al, 4
00638B65  74 0A                           je 0x140638b71
00638B67  E8 9C B0 E9 FF                  call 0x1404d3c08
00638B6C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00638B71  40 32 FF                        xor dil, dil
00638B74  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00638B79  40 38 3D 38 BD 8C 00            cmp byte ptr [rip + 0x8cbd38], dil
00638B80  75 0C                           jne 0x140638b8e
00638B82  F7 05 F4 BD 8C 00 00 08 00 00   test dword ptr [rip + 0x8cbdf4], 0x800
00638B8C  74 13                           je 0x140638ba1
00638B8E  48 8D 0D EB B2 8C 00            lea rcx, [rip + 0x8cb2eb]
00638B95  E8 86 DA BD FF                  call 0x140216620
00638B9A  40 8A F8                        mov dil, al
00638B9D  84 C0                           test al, al
00638B9F  74 39                           je 0x140638bda
00638BA1  4C 8D 76 20                     lea r14, [rsi + 0x20]
00638BA5  49 8B 1E                        mov rbx, qword ptr [r14]
00638BA8  EB 1A                           jmp 0x140638bc4
00638BAA  48 8D 43 F0                     lea rax, [rbx - 0x10]
00638BAE  48 85 C0                        test rax, rax
00638BB1  74 0E                           je 0x140638bc1
00638BB3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00638BB7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00638BBC  E8 0F 1F 08 00                  call 0x1406baad0
00638BC1  48 8B 1B                        mov rbx, qword ptr [rbx]
00638BC4  49 3B DE                        cmp rbx, r14
00638BC7  75 E1                           jne 0x140638baa
00638BC9  40 84 FF                        test dil, dil
00638BCC  74 0C                           je 0x140638bda
00638BCE  48 8D 0D AB B2 8C 00            lea rcx, [rip + 0x8cb2ab]
00638BD5  E8 A6 12 D1 FF                  call 0x140349e80
00638BDA  BA 44 66 6C 74                  mov edx, 0x746c6644
00638BDF  48 8B CD                        mov rcx, rbp
00638BE2  E8 29 7B BD FF                  call 0x140210710
00638BE7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00638BEC  48 85 F6                        test rsi, rsi
00638BEF  74 64                           je 0x140638c55
00638BF1  40 32 FF                        xor dil, dil
00638BF4  40 38 3D BD BC 8C 00            cmp byte ptr [rip + 0x8cbcbd], dil
00638BFB  75 0C                           jne 0x140638c09
00638BFD  F7 05 79 BD 8C 00 00 08 00 00   test dword ptr [rip + 0x8cbd79], 0x800
00638C07  74 13                           je 0x140638c1c
00638C09  48 8D 0D 70 B2 8C 00            lea rcx, [rip + 0x8cb270]
00638C10  E8 0B DA BD FF                  call 0x140216620
00638C15  40 8A F8                        mov dil, al
00638C18  84 C0                           test al, al
00638C1A  74 39                           je 0x140638c55
00638C1C  48 83 C6 30                     add rsi, 0x30
00638C20  48 8B 1E                        mov rbx, qword ptr [rsi]
00638C23  EB 1A                           jmp 0x140638c3f
00638C25  48 8D 43 F0                     lea rax, [rbx - 0x10]
00638C29  48 85 C0                        test rax, rax
00638C2C  74 0E                           je 0x140638c3c
00638C2E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00638C32  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00638C37  E8 94 1E 08 00                  call 0x1406baad0
00638C3C  48 8B 1B                        mov rbx, qword ptr [rbx]
00638C3F  48 3B DE                        cmp rbx, rsi
00638C42  75 E1                           jne 0x140638c25
00638C44  40 84 FF                        test dil, dil
00638C47  74 0C                           je 0x140638c55
00638C49  48 8D 0D 30 B2 8C 00            lea rcx, [rip + 0x8cb230]
00638C50  E8 2B 12 D1 FF                  call 0x140349e80
00638C55  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00638C5A  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00638C5F  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00638C64  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00638C69  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00638C6E  48 83 C4 40                     add rsp, 0x40
00638C72  41 5E                           pop r14
00638C74  C3                              ret
00638C75  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifObfReferenceObjectWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
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
    result = DifGetAPIThunkContextById(196, a2, a3, a4);
    if (result == 0) goto loc_00638BDA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00638B63;
    v_stack_m28 = v_stack_p0;
    goto loc_00638B71;
loc_00638B63:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9223480)) != 0) goto loc_00638B8E;
    if (((*(unsigned int *)(v_rip + 9223668)) & (0x800ULL)) == 0) goto loc_00638BA1;
loc_00638B8E:
    result = ExAcquireRundownProtection(v_rip + 9220843, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00638BDA;
loc_00638BA1:
    goto loc_00638BC4;
loc_00638BAA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00638BC4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00638BAA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9220779;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00638C55;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9223357)) != 0) goto loc_00638C09;
    if (((*(unsigned int *)(v_rip + 9223545)) & (0x800ULL)) == 0) goto loc_00638C1C;
loc_00638C09:
    result = ExAcquireRundownProtection(v_rip + 9220720, (unsigned int)(0x746C6644ULL), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00638C55;
loc_00638C1C:
    v_rsi = (result) + (48);
    goto loc_00638C3F;
loc_00638C25:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    }
loc_00638C3F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00638C25;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9220656;
        result = ExReleaseRundownProtection(a1, (unsigned int)(0x746C6644ULL), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifObfReferenceObjectWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(196, a2, a3, a4);
    if (result == 0) goto loc_00638BDA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00638B63;
    v_stack_m28 = v_stack_p0;
    goto loc_00638B71;
loc_00638B63:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CBD38)) != 0) goto loc_00638B8E;
    if (((*(uint32_t *)(v_rip + 0x8CBDF4)) & (0x800ULL)) == 0) goto loc_00638BA1;
loc_00638B8E:
    result = ExAcquireRundownProtection(v_rip + 9220843, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00638BDA;
loc_00638BA1:
    goto loc_00638BC4;
loc_00638BAA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00638BC4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00638BAA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9220779;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x746C6644ULL), a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00638C55;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CBCBD)) != 0) goto loc_00638C09;
    if (((*(uint32_t *)(v_rip + 0x8CBD79)) & (0x800ULL)) == 0) goto loc_00638C1C;
loc_00638C09:
    result = ExAcquireRundownProtection(v_rip + 9220720, (uint32_t)(0x746C6644ULL), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00638C55;
loc_00638C1C:
    local_rsi = (result) + (48);
    goto loc_00638C3F;
loc_00638C25:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, (uint32_t)(0x746C6644ULL), a3, a4);
    }
loc_00638C3F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00638C25;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9220656;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)(0x746C6644ULL), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00638B10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00638B10[BB_00638B10]
  bb_00638B50[BB_00638B50]
  bb_00638B57[BB_00638B57]
  bb_00638B63[BB_00638B63]
  bb_00638B67[BB_00638B67]
  bb_00638B71[BB_00638B71]
  bb_00638B82[BB_00638B82]
  bb_00638B8E[BB_00638B8E]
  bb_00638BA1[BB_00638BA1]
  bb_00638BAA[BB_00638BAA]
  bb_00638BB3[BB_00638BB3]
  bb_00638BC1[BB_00638BC1]
  bb_00638BC4[BB_00638BC4]
  bb_00638BC9[BB_00638BC9]
  bb_00638BCE[BB_00638BCE]
  bb_00638BDA[BB_00638BDA]
  bb_00638BF1[BB_00638BF1]
  bb_00638BFD[BB_00638BFD]
  bb_00638C09[BB_00638C09]
  bb_00638C1C[BB_00638C1C]
  bb_00638C25[BB_00638C25]
  bb_00638C2E[BB_00638C2E]
  bb_00638C3C[BB_00638C3C]
  bb_00638C3F[BB_00638C3F]
  bb_00638C44[BB_00638C44]
  bb_00638C49[BB_00638C49]
  bb_00638C55[BB_00638C55]
  bb_00638C75[BB_00638C75]
  bb_00638B10 -->|branch| bb_00638BDA
  bb_00638B10 -->|fallthrough| bb_00638B50
  bb_00638B50 -->|branch| bb_00638B63
  bb_00638B50 -->|fallthrough| bb_00638B57
  bb_00638B57 -->|branch| bb_00638B71
  bb_00638B63 -->|branch| bb_00638B71
  bb_00638B63 -->|fallthrough| bb_00638B67
  bb_00638B67 -->|flow| bb_00638B71
  bb_00638B71 -->|branch| bb_00638B8E
  bb_00638B71 -->|fallthrough| bb_00638B82
  bb_00638B82 -->|branch| bb_00638BA1
  bb_00638B82 -->|fallthrough| bb_00638B8E
  bb_00638B8E -->|branch| bb_00638BDA
  bb_00638B8E -->|fallthrough| bb_00638BA1
  bb_00638BA1 -->|branch| bb_00638BC4
  bb_00638BAA -->|branch| bb_00638BC1
  bb_00638BAA -->|fallthrough| bb_00638BB3
  bb_00638BB3 -->|flow| bb_00638BC1
  bb_00638BC1 -->|flow| bb_00638BC4
  bb_00638BC4 -->|branch| bb_00638BAA
  bb_00638BC4 -->|fallthrough| bb_00638BC9
  bb_00638BC9 -->|branch| bb_00638BDA
  bb_00638BC9 -->|fallthrough| bb_00638BCE
  bb_00638BCE -->|flow| bb_00638BDA
  bb_00638BDA -->|branch| bb_00638C55
  bb_00638BDA -->|fallthrough| bb_00638BF1
  bb_00638BF1 -->|branch| bb_00638C09
  bb_00638BF1 -->|fallthrough| bb_00638BFD
  bb_00638BFD -->|branch| bb_00638C1C
  bb_00638BFD -->|fallthrough| bb_00638C09
  bb_00638C09 -->|branch| bb_00638C55
  bb_00638C09 -->|fallthrough| bb_00638C1C
  bb_00638C1C -->|branch| bb_00638C3F
  bb_00638C25 -->|branch| bb_00638C3C
  bb_00638C25 -->|fallthrough| bb_00638C2E
  bb_00638C2E -->|flow| bb_00638C3C
  bb_00638C3C -->|flow| bb_00638C3F
  bb_00638C3F -->|branch| bb_00638C25
  bb_00638C3F -->|fallthrough| bb_00638C44
  bb_00638C44 -->|branch| bb_00638C55
  bb_00638C44 -->|fallthrough| bb_00638C49
  bb_00638C49 -->|flow| bb_00638C55
```
