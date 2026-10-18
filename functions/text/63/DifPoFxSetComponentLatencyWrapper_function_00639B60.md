# DifPoFxSetComponentLatencyWrapper

- RVA: `0x00639B60`–`0x00639CD2` (길이 `370` bytes)
- VA: `0x0000000140639B60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `101`개 명령, `370/370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00639B96` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00639BBE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00639BF6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639C1D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639C36` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00639C44` → [PoFxSetComponentLatency](../2B/PoFxSetComponentLatency_function_002BF390.md) (function, `0x002BF390`)
- `0x00639C6D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639C94` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639CAD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00639BD0` → RVA `0x00F048B8` (`.data`; read)
- `0x00639BE3` → RVA `0x00F04980` (`.data`; read)
- `0x00639BEF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00639B60  48 8B C4                        mov rax, rsp
00639B63  48 89 58 08                     mov qword ptr [rax + 8], rbx
00639B67  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00639B6B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00639B6F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00639B73  41 54                           push r12
00639B75  41 56                           push r14
00639B77  41 57                           push r15
00639B79  48 83 EC 40                     sub rsp, 0x40
00639B7D  0F 57 C0                        xorps xmm0, xmm0
00639B80  4C 8B E1                        mov r12, rcx
00639B83  B9 B8 00 00 00                  mov ecx, 0xb8
00639B88  4D 8B F0                        mov r14, r8
00639B8B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00639B8F  44 8B FA                        mov r15d, edx
00639B92  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00639B96  E8 99 BE E5 FF                  call 0x140495a34
00639B9B  48 8B F0                        mov rsi, rax
00639B9E  48 85 C0                        test rax, rax
00639BA1  0F 84 94 00 00 00               je 0x140639c3b
00639BA7  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00639BAA  A8 18                           test al, 0x18
00639BAC  74 0C                           je 0x140639bba
00639BAE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00639BB3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00639BB8  EB 0E                           jmp 0x140639bc8
00639BBA  A8 04                           test al, 4
00639BBC  74 0A                           je 0x140639bc8
00639BBE  E8 45 A0 E9 FF                  call 0x1404d3c08
00639BC3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00639BC8  40 32 ED                        xor bpl, bpl
00639BCB  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00639BD0  40 38 2D E1 AC 8C 00            cmp byte ptr [rip + 0x8cace1], bpl
00639BD7  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00639BDC  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00639BE1  75 0C                           jne 0x140639bef
00639BE3  F7 05 93 AD 8C 00 00 08 00 00   test dword ptr [rip + 0x8cad93], 0x800
00639BED  74 13                           je 0x140639c02
00639BEF  48 8D 0D 8A A2 8C 00            lea rcx, [rip + 0x8ca28a]
00639BF6  E8 25 CA BD FF                  call 0x140216620
00639BFB  40 8A E8                        mov bpl, al
00639BFE  84 C0                           test al, al
00639C00  74 39                           je 0x140639c3b
00639C02  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00639C06  48 8B 1F                        mov rbx, qword ptr [rdi]
00639C09  EB 1A                           jmp 0x140639c25
00639C0B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639C0F  48 85 C0                        test rax, rax
00639C12  74 0E                           je 0x140639c22
00639C14  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639C18  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639C1D  E8 AE 0E 08 00                  call 0x1406baad0
00639C22  48 8B 1B                        mov rbx, qword ptr [rbx]
00639C25  48 3B DF                        cmp rbx, rdi
00639C28  75 E1                           jne 0x140639c0b
00639C2A  40 84 ED                        test bpl, bpl
00639C2D  74 0C                           je 0x140639c3b
00639C2F  48 8D 0D 4A A2 8C 00            lea rcx, [rip + 0x8ca24a]
00639C36  E8 45 02 D1 FF                  call 0x140349e80
00639C3B  4D 8B C6                        mov r8, r14
00639C3E  41 8B D7                        mov edx, r15d
00639C41  49 8B CC                        mov rcx, r12
00639C44  E8 47 57 C8 FF                  call 0x1402bf390
00639C49  48 85 F6                        test rsi, rsi
00639C4C  74 64                           je 0x140639cb2
00639C4E  40 32 FF                        xor dil, dil
00639C51  40 38 3D 60 AC 8C 00            cmp byte ptr [rip + 0x8cac60], dil
00639C58  75 0C                           jne 0x140639c66
00639C5A  F7 05 1C AD 8C 00 00 08 00 00   test dword ptr [rip + 0x8cad1c], 0x800
00639C64  74 13                           je 0x140639c79
00639C66  48 8D 0D 13 A2 8C 00            lea rcx, [rip + 0x8ca213]
00639C6D  E8 AE C9 BD FF                  call 0x140216620
00639C72  40 8A F8                        mov dil, al
00639C75  84 C0                           test al, al
00639C77  74 39                           je 0x140639cb2
00639C79  48 83 C6 30                     add rsi, 0x30
00639C7D  48 8B 1E                        mov rbx, qword ptr [rsi]
00639C80  EB 1A                           jmp 0x140639c9c
00639C82  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639C86  48 85 C0                        test rax, rax
00639C89  74 0E                           je 0x140639c99
00639C8B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639C8F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639C94  E8 37 0E 08 00                  call 0x1406baad0
00639C99  48 8B 1B                        mov rbx, qword ptr [rbx]
00639C9C  48 3B DE                        cmp rbx, rsi
00639C9F  75 E1                           jne 0x140639c82
00639CA1  40 84 FF                        test dil, dil
00639CA4  74 0C                           je 0x140639cb2
00639CA6  48 8D 0D D3 A1 8C 00            lea rcx, [rip + 0x8ca1d3]
00639CAD  E8 CE 01 D1 FF                  call 0x140349e80
00639CB2  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00639CB7  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00639CBC  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00639CC1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00639CC6  48 83 C4 40                     add rsp, 0x40
00639CCA  41 5F                           pop r15
00639CCC  41 5E                           pop r14
00639CCE  41 5C                           pop r12
00639CD0  C3                              ret
00639CD1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPoFxSetComponentLatencyWrapper(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
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
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(184, a2, a3, a4);
    if (result == 0) goto loc_00639C3B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00639BBA;
    v_stack_m38 = v_stack_p0;
    goto loc_00639BC8;
loc_00639BBA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = (unsigned int)((unsigned int)(a2));
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9219297)) != 0) goto loc_00639BEF;
    if (((*(unsigned int *)(v_rip + 9219475)) & (0x800ULL)) == 0) goto loc_00639C02;
loc_00639BEF:
    result = ExAcquireRundownProtection(v_rip + 9216650, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639C3B;
loc_00639C02:
    goto loc_00639C25;
loc_00639C0B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00639C25:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00639C0B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9216586;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PoFxSetComponentLatency(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if (result == 0) goto loc_00639CB2;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9219168)) != 0) goto loc_00639C66;
    if (((*(unsigned int *)(v_rip + 9219356)) & (0x800ULL)) == 0) goto loc_00639C79;
loc_00639C66:
    result = ExAcquireRundownProtection(v_rip + 9216531, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639CB2;
loc_00639C79:
    v_rsi = (result) + (48);
    goto loc_00639C9C;
loc_00639C82:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00639C9C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00639C82;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9216467;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifPoFxSetComponentLatencyWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
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
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(184, Arg2, Arg3, a4);
    if (result == 0) goto loc_00639C3B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00639BBA;
    v_stack_m38 = v_stack_p0;
    goto loc_00639BC8;
loc_00639BBA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8CACE1)) != 0) goto loc_00639BEF;
    if (((*(uint32_t *)(v_rip + 0x8CAD93)) & (0x800ULL)) == 0) goto loc_00639C02;
loc_00639BEF:
    result = ExAcquireRundownProtection(v_rip + 9216650, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00639C3B;
loc_00639C02:
    goto loc_00639C25;
loc_00639C0B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00639C25:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00639C0B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9216586;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = PoFxSetComponentLatency(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if (result == 0) goto loc_00639CB2;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CAC60)) != 0) goto loc_00639C66;
    if (((*(uint32_t *)(v_rip + 0x8CAD1C)) & (0x800ULL)) == 0) goto loc_00639C79;
loc_00639C66:
    result = ExAcquireRundownProtection(v_rip + 9216531, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00639CB2;
loc_00639C79:
    local_rsi = (result) + (48);
    goto loc_00639C9C;
loc_00639C82:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_00639C9C:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00639C82;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9216467;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00639B60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00639B60[BB_00639B60]
  bb_00639BA7[BB_00639BA7]
  bb_00639BAE[BB_00639BAE]
  bb_00639BBA[BB_00639BBA]
  bb_00639BBE[BB_00639BBE]
  bb_00639BC8[BB_00639BC8]
  bb_00639BE3[BB_00639BE3]
  bb_00639BEF[BB_00639BEF]
  bb_00639C02[BB_00639C02]
  bb_00639C0B[BB_00639C0B]
  bb_00639C14[BB_00639C14]
  bb_00639C22[BB_00639C22]
  bb_00639C25[BB_00639C25]
  bb_00639C2A[BB_00639C2A]
  bb_00639C2F[BB_00639C2F]
  bb_00639C3B[BB_00639C3B]
  bb_00639C4E[BB_00639C4E]
  bb_00639C5A[BB_00639C5A]
  bb_00639C66[BB_00639C66]
  bb_00639C79[BB_00639C79]
  bb_00639C82[BB_00639C82]
  bb_00639C8B[BB_00639C8B]
  bb_00639C99[BB_00639C99]
  bb_00639C9C[BB_00639C9C]
  bb_00639CA1[BB_00639CA1]
  bb_00639CA6[BB_00639CA6]
  bb_00639CB2[BB_00639CB2]
  bb_00639CD1[BB_00639CD1]
  bb_00639B60 -->|branch| bb_00639C3B
  bb_00639B60 -->|fallthrough| bb_00639BA7
  bb_00639BA7 -->|branch| bb_00639BBA
  bb_00639BA7 -->|fallthrough| bb_00639BAE
  bb_00639BAE -->|branch| bb_00639BC8
  bb_00639BBA -->|branch| bb_00639BC8
  bb_00639BBA -->|fallthrough| bb_00639BBE
  bb_00639BBE -->|flow| bb_00639BC8
  bb_00639BC8 -->|branch| bb_00639BEF
  bb_00639BC8 -->|fallthrough| bb_00639BE3
  bb_00639BE3 -->|branch| bb_00639C02
  bb_00639BE3 -->|fallthrough| bb_00639BEF
  bb_00639BEF -->|branch| bb_00639C3B
  bb_00639BEF -->|fallthrough| bb_00639C02
  bb_00639C02 -->|branch| bb_00639C25
  bb_00639C0B -->|branch| bb_00639C22
  bb_00639C0B -->|fallthrough| bb_00639C14
  bb_00639C14 -->|flow| bb_00639C22
  bb_00639C22 -->|flow| bb_00639C25
  bb_00639C25 -->|branch| bb_00639C0B
  bb_00639C25 -->|fallthrough| bb_00639C2A
  bb_00639C2A -->|branch| bb_00639C3B
  bb_00639C2A -->|fallthrough| bb_00639C2F
  bb_00639C2F -->|flow| bb_00639C3B
  bb_00639C3B -->|branch| bb_00639CB2
  bb_00639C3B -->|fallthrough| bb_00639C4E
  bb_00639C4E -->|branch| bb_00639C66
  bb_00639C4E -->|fallthrough| bb_00639C5A
  bb_00639C5A -->|branch| bb_00639C79
  bb_00639C5A -->|fallthrough| bb_00639C66
  bb_00639C66 -->|branch| bb_00639CB2
  bb_00639C66 -->|fallthrough| bb_00639C79
  bb_00639C79 -->|branch| bb_00639C9C
  bb_00639C82 -->|branch| bb_00639C99
  bb_00639C82 -->|fallthrough| bb_00639C8B
  bb_00639C8B -->|flow| bb_00639C99
  bb_00639C99 -->|flow| bb_00639C9C
  bb_00639C9C -->|branch| bb_00639C82
  bb_00639C9C -->|fallthrough| bb_00639CA1
  bb_00639CA1 -->|branch| bb_00639CB2
  bb_00639CA1 -->|fallthrough| bb_00639CA6
  bb_00639CA6 -->|flow| bb_00639CB2
```
