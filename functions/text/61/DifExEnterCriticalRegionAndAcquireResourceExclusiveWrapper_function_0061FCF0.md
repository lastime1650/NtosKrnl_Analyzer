# DifExEnterCriticalRegionAndAcquireResourceExclusiveWrapper

- RVA: `0x0061FCF0`–`0x0061FE51` (길이 `353` bytes)
- VA: `0x000000014061FCF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061FD1F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061FD47` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061FD75` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061FD9C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061FDB5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061FDBD` → [ExEnterCriticalRegionAndAcquireResourceExclusive](../21/ExEnterCriticalRegionAndAcquireResourceExclusive_function_00214DE0.md) (function, `0x00214DE0`)
- `0x0061FDEB` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061FE12` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061FE2B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061FD59` → RVA `0x00F048B8` (`.data`; read)
- `0x0061FD62` → RVA `0x00F04980` (`.data`; read)
- `0x0061FD6E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061FCF0  4C 8B DC                        mov r11, rsp
0061FCF3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0061FCF7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0061FCFB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0061FCFF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0061FD03  41 56                           push r14
0061FD05  48 83 EC 40                     sub rsp, 0x40
0061FD09  33 C0                           xor eax, eax
0061FD0B  0F 57 C0                        xorps xmm0, xmm0
0061FD0E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0061FD13  48 8B E9                        mov rbp, rcx
0061FD16  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0061FD1A  B9 96 01 00 00                  mov ecx, 0x196
0061FD1F  E8 10 5D E7 FF                  call 0x140495a34
0061FD24  48 8B F0                        mov rsi, rax
0061FD27  48 85 C0                        test rax, rax
0061FD2A  0F 84 8A 00 00 00               je 0x14061fdba
0061FD30  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061FD33  A8 18                           test al, 0x18
0061FD35  74 0C                           je 0x14061fd43
0061FD37  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0061FD3C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061FD41  EB 0E                           jmp 0x14061fd51
0061FD43  A8 04                           test al, 4
0061FD45  74 0A                           je 0x14061fd51
0061FD47  E8 BC 3E EB FF                  call 0x1404d3c08
0061FD4C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061FD51  40 32 FF                        xor dil, dil
0061FD54  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0061FD59  40 38 3D 58 4B 8E 00            cmp byte ptr [rip + 0x8e4b58], dil
0061FD60  75 0C                           jne 0x14061fd6e
0061FD62  F7 05 14 4C 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4c14], 0x800
0061FD6C  74 13                           je 0x14061fd81
0061FD6E  48 8D 0D 0B 41 8E 00            lea rcx, [rip + 0x8e410b]
0061FD75  E8 A6 68 BF FF                  call 0x140216620
0061FD7A  40 8A F8                        mov dil, al
0061FD7D  84 C0                           test al, al
0061FD7F  74 39                           je 0x14061fdba
0061FD81  4C 8D 76 20                     lea r14, [rsi + 0x20]
0061FD85  49 8B 1E                        mov rbx, qword ptr [r14]
0061FD88  EB 1A                           jmp 0x14061fda4
0061FD8A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061FD8E  48 85 C0                        test rax, rax
0061FD91  74 0E                           je 0x14061fda1
0061FD93  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061FD97  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061FD9C  E8 2F AD 09 00                  call 0x1406baad0
0061FDA1  48 8B 1B                        mov rbx, qword ptr [rbx]
0061FDA4  49 3B DE                        cmp rbx, r14
0061FDA7  75 E1                           jne 0x14061fd8a
0061FDA9  40 84 FF                        test dil, dil
0061FDAC  74 0C                           je 0x14061fdba
0061FDAE  48 8D 0D CB 40 8E 00            lea rcx, [rip + 0x8e40cb]
0061FDB5  E8 C6 A0 D2 FF                  call 0x140349e80
0061FDBA  48 8B CD                        mov rcx, rbp
0061FDBD  E8 1E 50 BF FF                  call 0x140214de0
0061FDC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0061FDC7  48 85 F6                        test rsi, rsi
0061FDCA  74 64                           je 0x14061fe30
0061FDCC  40 32 FF                        xor dil, dil
0061FDCF  40 38 3D E2 4A 8E 00            cmp byte ptr [rip + 0x8e4ae2], dil
0061FDD6  75 0C                           jne 0x14061fde4
0061FDD8  F7 05 9E 4B 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4b9e], 0x800
0061FDE2  74 13                           je 0x14061fdf7
0061FDE4  48 8D 0D 95 40 8E 00            lea rcx, [rip + 0x8e4095]
0061FDEB  E8 30 68 BF FF                  call 0x140216620
0061FDF0  40 8A F8                        mov dil, al
0061FDF3  84 C0                           test al, al
0061FDF5  74 39                           je 0x14061fe30
0061FDF7  48 83 C6 30                     add rsi, 0x30
0061FDFB  48 8B 1E                        mov rbx, qword ptr [rsi]
0061FDFE  EB 1A                           jmp 0x14061fe1a
0061FE00  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061FE04  48 85 C0                        test rax, rax
0061FE07  74 0E                           je 0x14061fe17
0061FE09  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061FE0D  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061FE12  E8 B9 AC 09 00                  call 0x1406baad0
0061FE17  48 8B 1B                        mov rbx, qword ptr [rbx]
0061FE1A  48 3B DE                        cmp rbx, rsi
0061FE1D  75 E1                           jne 0x14061fe00
0061FE1F  40 84 FF                        test dil, dil
0061FE22  74 0C                           je 0x14061fe30
0061FE24  48 8D 0D 55 40 8E 00            lea rcx, [rip + 0x8e4055]
0061FE2B  E8 50 A0 D2 FF                  call 0x140349e80
0061FE30  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0061FE35  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0061FE3A  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0061FE3F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0061FE44  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0061FE49  48 83 C4 40                     add rsp, 0x40
0061FE4D  41 5E                           pop r14
0061FE4F  C3                              ret
0061FE50  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExEnterCriticalRegionAndAcquireResourceExclusiveWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(406, a2, a3, a4);
    if (result == 0) goto loc_0061FDBA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061FD43;
    v_stack_m28 = v_stack_p0;
    goto loc_0061FD51;
loc_0061FD43:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9325400)) != 0) goto loc_0061FD6E;
    if (((*(unsigned int *)(v_rip + 9325588)) & (0x800ULL)) == 0) goto loc_0061FD81;
loc_0061FD6E:
    result = ExAcquireRundownProtection(v_rip + 9322763, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061FDBA;
loc_0061FD81:
    goto loc_0061FDA4;
loc_0061FD8A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061FDA4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061FD8A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9322699;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExEnterCriticalRegionAndAcquireResourceExclusive(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_0061FE30;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9325282)) != 0) goto loc_0061FDE4;
    if (((*(unsigned int *)(v_rip + 9325470)) & (0x800ULL)) == 0) goto loc_0061FDF7;
loc_0061FDE4:
    result = ExAcquireRundownProtection(v_rip + 9322645, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061FE30;
loc_0061FDF7:
    v_rsi = (result) + (48);
    goto loc_0061FE1A;
loc_0061FE00:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061FE1A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061FE00;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9322581;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExEnterCriticalRegionAndAcquireResourceExclusiveWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(406, a2, a3, a4);
    if (result == 0) goto loc_0061FDBA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061FD43;
    v_stack_m28 = v_stack_p0;
    goto loc_0061FD51;
loc_0061FD43:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E4B58)) != 0) goto loc_0061FD6E;
    if (((*(uint32_t *)(v_rip + 0x8E4C14)) & (0x800ULL)) == 0) goto loc_0061FD81;
loc_0061FD6E:
    result = ExAcquireRundownProtection(v_rip + 9322763, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061FDBA;
loc_0061FD81:
    goto loc_0061FDA4;
loc_0061FD8A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061FDA4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061FD8A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9322699;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExEnterCriticalRegionAndAcquireResourceExclusive(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_0061FE30;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E4AE2)) != 0) goto loc_0061FDE4;
    if (((*(uint32_t *)(v_rip + 0x8E4B9E)) & (0x800ULL)) == 0) goto loc_0061FDF7;
loc_0061FDE4:
    result = ExAcquireRundownProtection(v_rip + 9322645, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061FE30;
loc_0061FDF7:
    local_rsi = (result) + (48);
    goto loc_0061FE1A;
loc_0061FE00:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061FE1A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061FE00;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9322581;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061FCF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061FCF0[BB_0061FCF0]
  bb_0061FD30[BB_0061FD30]
  bb_0061FD37[BB_0061FD37]
  bb_0061FD43[BB_0061FD43]
  bb_0061FD47[BB_0061FD47]
  bb_0061FD51[BB_0061FD51]
  bb_0061FD62[BB_0061FD62]
  bb_0061FD6E[BB_0061FD6E]
  bb_0061FD81[BB_0061FD81]
  bb_0061FD8A[BB_0061FD8A]
  bb_0061FD93[BB_0061FD93]
  bb_0061FDA1[BB_0061FDA1]
  bb_0061FDA4[BB_0061FDA4]
  bb_0061FDA9[BB_0061FDA9]
  bb_0061FDAE[BB_0061FDAE]
  bb_0061FDBA[BB_0061FDBA]
  bb_0061FDCC[BB_0061FDCC]
  bb_0061FDD8[BB_0061FDD8]
  bb_0061FDE4[BB_0061FDE4]
  bb_0061FDF7[BB_0061FDF7]
  bb_0061FE00[BB_0061FE00]
  bb_0061FE09[BB_0061FE09]
  bb_0061FE17[BB_0061FE17]
  bb_0061FE1A[BB_0061FE1A]
  bb_0061FE1F[BB_0061FE1F]
  bb_0061FE24[BB_0061FE24]
  bb_0061FE30[BB_0061FE30]
  bb_0061FE50[BB_0061FE50]
  bb_0061FCF0 -->|branch| bb_0061FDBA
  bb_0061FCF0 -->|fallthrough| bb_0061FD30
  bb_0061FD30 -->|branch| bb_0061FD43
  bb_0061FD30 -->|fallthrough| bb_0061FD37
  bb_0061FD37 -->|branch| bb_0061FD51
  bb_0061FD43 -->|branch| bb_0061FD51
  bb_0061FD43 -->|fallthrough| bb_0061FD47
  bb_0061FD47 -->|flow| bb_0061FD51
  bb_0061FD51 -->|branch| bb_0061FD6E
  bb_0061FD51 -->|fallthrough| bb_0061FD62
  bb_0061FD62 -->|branch| bb_0061FD81
  bb_0061FD62 -->|fallthrough| bb_0061FD6E
  bb_0061FD6E -->|branch| bb_0061FDBA
  bb_0061FD6E -->|fallthrough| bb_0061FD81
  bb_0061FD81 -->|branch| bb_0061FDA4
  bb_0061FD8A -->|branch| bb_0061FDA1
  bb_0061FD8A -->|fallthrough| bb_0061FD93
  bb_0061FD93 -->|flow| bb_0061FDA1
  bb_0061FDA1 -->|flow| bb_0061FDA4
  bb_0061FDA4 -->|branch| bb_0061FD8A
  bb_0061FDA4 -->|fallthrough| bb_0061FDA9
  bb_0061FDA9 -->|branch| bb_0061FDBA
  bb_0061FDA9 -->|fallthrough| bb_0061FDAE
  bb_0061FDAE -->|flow| bb_0061FDBA
  bb_0061FDBA -->|branch| bb_0061FE30
  bb_0061FDBA -->|fallthrough| bb_0061FDCC
  bb_0061FDCC -->|branch| bb_0061FDE4
  bb_0061FDCC -->|fallthrough| bb_0061FDD8
  bb_0061FDD8 -->|branch| bb_0061FDF7
  bb_0061FDD8 -->|fallthrough| bb_0061FDE4
  bb_0061FDE4 -->|branch| bb_0061FE30
  bb_0061FDE4 -->|fallthrough| bb_0061FDF7
  bb_0061FDF7 -->|branch| bb_0061FE1A
  bb_0061FE00 -->|branch| bb_0061FE17
  bb_0061FE00 -->|fallthrough| bb_0061FE09
  bb_0061FE09 -->|flow| bb_0061FE17
  bb_0061FE17 -->|flow| bb_0061FE1A
  bb_0061FE1A -->|branch| bb_0061FE00
  bb_0061FE1A -->|fallthrough| bb_0061FE1F
  bb_0061FE1F -->|branch| bb_0061FE30
  bb_0061FE1F -->|fallthrough| bb_0061FE24
  bb_0061FE24 -->|flow| bb_0061FE30
```
