# DifPoFxReportDevicePoweredOnWrapper

- RVA: `0x00639A00`–`0x00639B50` (길이 `336` bytes)
- VA: `0x0000000140639A00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00639A28` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00639A50` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00639A7E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639AA5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639ABE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00639AC6` → [PopFxHandleReportDevicePoweredOn](../26/PopFxHandleReportDevicePoweredOn_function_0026D980.md) (function, `0x0026D980`)
- `0x00639AEF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639B16` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639B2F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00639A62` → RVA `0x00F048B8` (`.data`; read)
- `0x00639A6B` → RVA `0x00F04980` (`.data`; read)
- `0x00639A77` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00639A00  48 8B C4                        mov rax, rsp
00639A03  48 89 58 08                     mov qword ptr [rax + 8], rbx
00639A07  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00639A0B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00639A0F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00639A13  41 56                           push r14
00639A15  48 83 EC 30                     sub rsp, 0x30
00639A19  48 8B E9                        mov rbp, rcx
00639A1C  0F 57 C0                        xorps xmm0, xmm0
00639A1F  B9 B9 00 00 00                  mov ecx, 0xb9
00639A24  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00639A28  E8 07 C0 E5 FF                  call 0x140495a34
00639A2D  48 8B F8                        mov rdi, rax
00639A30  48 85 C0                        test rax, rax
00639A33  0F 84 8A 00 00 00               je 0x140639ac3
00639A39  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00639A3C  A8 18                           test al, 0x18
00639A3E  74 0C                           je 0x140639a4c
00639A40  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00639A45  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00639A4A  EB 0E                           jmp 0x140639a5a
00639A4C  A8 04                           test al, 4
00639A4E  74 0A                           je 0x140639a5a
00639A50  E8 B3 A1 E9 FF                  call 0x1404d3c08
00639A55  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00639A5A  40 32 F6                        xor sil, sil
00639A5D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00639A62  40 38 35 4F AE 8C 00            cmp byte ptr [rip + 0x8cae4f], sil
00639A69  75 0C                           jne 0x140639a77
00639A6B  F7 05 0B AF 8C 00 00 08 00 00   test dword ptr [rip + 0x8caf0b], 0x800
00639A75  74 13                           je 0x140639a8a
00639A77  48 8D 0D 02 A4 8C 00            lea rcx, [rip + 0x8ca402]
00639A7E  E8 9D CB BD FF                  call 0x140216620
00639A83  40 8A F0                        mov sil, al
00639A86  84 C0                           test al, al
00639A88  74 39                           je 0x140639ac3
00639A8A  4C 8D 77 20                     lea r14, [rdi + 0x20]
00639A8E  49 8B 1E                        mov rbx, qword ptr [r14]
00639A91  EB 1A                           jmp 0x140639aad
00639A93  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639A97  48 85 C0                        test rax, rax
00639A9A  74 0E                           je 0x140639aaa
00639A9C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639AA0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639AA5  E8 26 10 08 00                  call 0x1406baad0
00639AAA  48 8B 1B                        mov rbx, qword ptr [rbx]
00639AAD  49 3B DE                        cmp rbx, r14
00639AB0  75 E1                           jne 0x140639a93
00639AB2  40 84 F6                        test sil, sil
00639AB5  74 0C                           je 0x140639ac3
00639AB7  48 8D 0D C2 A3 8C 00            lea rcx, [rip + 0x8ca3c2]
00639ABE  E8 BD 03 D1 FF                  call 0x140349e80
00639AC3  48 8B CD                        mov rcx, rbp
00639AC6  E8 B5 3E C3 FF                  call 0x14026d980
00639ACB  48 85 FF                        test rdi, rdi
00639ACE  74 64                           je 0x140639b34
00639AD0  40 32 F6                        xor sil, sil
00639AD3  40 38 35 DE AD 8C 00            cmp byte ptr [rip + 0x8cadde], sil
00639ADA  75 0C                           jne 0x140639ae8
00639ADC  F7 05 9A AE 8C 00 00 08 00 00   test dword ptr [rip + 0x8cae9a], 0x800
00639AE6  74 13                           je 0x140639afb
00639AE8  48 8D 0D 91 A3 8C 00            lea rcx, [rip + 0x8ca391]
00639AEF  E8 2C CB BD FF                  call 0x140216620
00639AF4  40 8A F0                        mov sil, al
00639AF7  84 C0                           test al, al
00639AF9  74 39                           je 0x140639b34
00639AFB  48 83 C7 30                     add rdi, 0x30
00639AFF  48 8B 1F                        mov rbx, qword ptr [rdi]
00639B02  EB 1A                           jmp 0x140639b1e
00639B04  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639B08  48 85 C0                        test rax, rax
00639B0B  74 0E                           je 0x140639b1b
00639B0D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639B11  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639B16  E8 B5 0F 08 00                  call 0x1406baad0
00639B1B  48 8B 1B                        mov rbx, qword ptr [rbx]
00639B1E  48 3B DF                        cmp rbx, rdi
00639B21  75 E1                           jne 0x140639b04
00639B23  40 84 F6                        test sil, sil
00639B26  74 0C                           je 0x140639b34
00639B28  48 8D 0D 51 A3 8C 00            lea rcx, [rip + 0x8ca351]
00639B2F  E8 4C 03 D1 FF                  call 0x140349e80
00639B34  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00639B39  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00639B3E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00639B43  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00639B48  48 83 C4 30                     add rsp, 0x30
00639B4C  41 5E                           pop r14
00639B4E  C3                              ret
00639B4F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPoFxReportDevicePoweredOnWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(185, a2, a3, a4);
    if (result == 0) goto loc_00639AC3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00639A4C;
    v_stack_m18 = v_stack_p0;
    goto loc_00639A5A;
loc_00639A4C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9219663)) != 0) goto loc_00639A77;
    if (((*(unsigned int *)(v_rip + 9219851)) & (0x800ULL)) == 0) goto loc_00639A8A;
loc_00639A77:
    result = ExAcquireRundownProtection(v_rip + 9217026, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639AC3;
loc_00639A8A:
    goto loc_00639AAD;
loc_00639A93:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00639AAD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00639A93;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9216962;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PopFxHandleReportDevicePoweredOn(a1, a2, a3, a4);
    if (result == 0) goto loc_00639B34;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9219550)) != 0) goto loc_00639AE8;
    if (((*(unsigned int *)(v_rip + 9219738)) & (0x800ULL)) == 0) goto loc_00639AFB;
loc_00639AE8:
    result = ExAcquireRundownProtection(v_rip + 9216913, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639B34;
loc_00639AFB:
    v_rdi = (result) + (48);
    goto loc_00639B1E;
loc_00639B04:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00639B1E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00639B04;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9216849;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifPoFxReportDevicePoweredOnWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(185, a2, a3, a4);
    if (result == 0) goto loc_00639AC3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00639A4C;
    v_stack_m18 = v_stack_p0;
    goto loc_00639A5A;
loc_00639A4C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CAE4F)) != 0) goto loc_00639A77;
    if (((*(uint32_t *)(v_rip + 0x8CAF0B)) & (0x800ULL)) == 0) goto loc_00639A8A;
loc_00639A77:
    result = ExAcquireRundownProtection(v_rip + 9217026, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00639AC3;
loc_00639A8A:
    goto loc_00639AAD;
loc_00639A93:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00639AAD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00639A93;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9216962;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = PopFxHandleReportDevicePoweredOn(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00639B34;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CADDE)) != 0) goto loc_00639AE8;
    if (((*(uint32_t *)(v_rip + 0x8CAE9A)) & (0x800ULL)) == 0) goto loc_00639AFB;
loc_00639AE8:
    result = ExAcquireRundownProtection(v_rip + 9216913, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00639B34;
loc_00639AFB:
    local_rdi = (result) + (48);
    goto loc_00639B1E;
loc_00639B04:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00639B1E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00639B04;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9216849;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00639A00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00639A00[BB_00639A00]
  bb_00639A39[BB_00639A39]
  bb_00639A40[BB_00639A40]
  bb_00639A4C[BB_00639A4C]
  bb_00639A50[BB_00639A50]
  bb_00639A5A[BB_00639A5A]
  bb_00639A6B[BB_00639A6B]
  bb_00639A77[BB_00639A77]
  bb_00639A8A[BB_00639A8A]
  bb_00639A93[BB_00639A93]
  bb_00639A9C[BB_00639A9C]
  bb_00639AAA[BB_00639AAA]
  bb_00639AAD[BB_00639AAD]
  bb_00639AB2[BB_00639AB2]
  bb_00639AB7[BB_00639AB7]
  bb_00639AC3[BB_00639AC3]
  bb_00639AD0[BB_00639AD0]
  bb_00639ADC[BB_00639ADC]
  bb_00639AE8[BB_00639AE8]
  bb_00639AFB[BB_00639AFB]
  bb_00639B04[BB_00639B04]
  bb_00639B0D[BB_00639B0D]
  bb_00639B1B[BB_00639B1B]
  bb_00639B1E[BB_00639B1E]
  bb_00639B23[BB_00639B23]
  bb_00639B28[BB_00639B28]
  bb_00639B34[BB_00639B34]
  bb_00639B4F[BB_00639B4F]
  bb_00639A00 -->|branch| bb_00639AC3
  bb_00639A00 -->|fallthrough| bb_00639A39
  bb_00639A39 -->|branch| bb_00639A4C
  bb_00639A39 -->|fallthrough| bb_00639A40
  bb_00639A40 -->|branch| bb_00639A5A
  bb_00639A4C -->|branch| bb_00639A5A
  bb_00639A4C -->|fallthrough| bb_00639A50
  bb_00639A50 -->|flow| bb_00639A5A
  bb_00639A5A -->|branch| bb_00639A77
  bb_00639A5A -->|fallthrough| bb_00639A6B
  bb_00639A6B -->|branch| bb_00639A8A
  bb_00639A6B -->|fallthrough| bb_00639A77
  bb_00639A77 -->|branch| bb_00639AC3
  bb_00639A77 -->|fallthrough| bb_00639A8A
  bb_00639A8A -->|branch| bb_00639AAD
  bb_00639A93 -->|branch| bb_00639AAA
  bb_00639A93 -->|fallthrough| bb_00639A9C
  bb_00639A9C -->|flow| bb_00639AAA
  bb_00639AAA -->|flow| bb_00639AAD
  bb_00639AAD -->|branch| bb_00639A93
  bb_00639AAD -->|fallthrough| bb_00639AB2
  bb_00639AB2 -->|branch| bb_00639AC3
  bb_00639AB2 -->|fallthrough| bb_00639AB7
  bb_00639AB7 -->|flow| bb_00639AC3
  bb_00639AC3 -->|branch| bb_00639B34
  bb_00639AC3 -->|fallthrough| bb_00639AD0
  bb_00639AD0 -->|branch| bb_00639AE8
  bb_00639AD0 -->|fallthrough| bb_00639ADC
  bb_00639ADC -->|branch| bb_00639AFB
  bb_00639ADC -->|fallthrough| bb_00639AE8
  bb_00639AE8 -->|branch| bb_00639B34
  bb_00639AE8 -->|fallthrough| bb_00639AFB
  bb_00639AFB -->|branch| bb_00639B1E
  bb_00639B04 -->|branch| bb_00639B1B
  bb_00639B04 -->|fallthrough| bb_00639B0D
  bb_00639B0D -->|flow| bb_00639B1B
  bb_00639B1B -->|flow| bb_00639B1E
  bb_00639B1E -->|branch| bb_00639B04
  bb_00639B1E -->|fallthrough| bb_00639B23
  bb_00639B23 -->|branch| bb_00639B34
  bb_00639B23 -->|fallthrough| bb_00639B28
  bb_00639B28 -->|flow| bb_00639B34
```
